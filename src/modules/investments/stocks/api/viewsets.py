from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.decorators import action
from core.rest_framework.viewsets import ActionsModelViewSet
from core.rest_framework.decorators import template_name, viewset_template_name
from modules.investments.stocks import models
from . import serializers

@viewset_template_name(
    list="stocks/invoice_list.html",
    add="stocks/invoice_add.html",
)
class InvoiceViewSet(viewsets.ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    
    def get_queryset(self):
        request = self.request
        user = request.user
        return models.Invoice.objects.filter(user=user).all()

    def get_serializer_class(self):
        if self.action in ["create", "add"]:
            return serializers.InvoiceCreateSerializer
        return serializers.InvoiceListSerializer

    @action(methods=['GET'], detail=False, renderer_classes=[TemplateHTMLRenderer])
    def add(self, request):
        context = { 'serializer': self.get_serializer() }
        return Response(context)
    
class StockViewSet(ActionsModelViewSet):
    serializer_class = serializers.StockSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def get_queryset(self):
        request = self.request
        user = request.user
        return models.Stock.objects.filter(user=user).all()
    
    #@template_name('stock_list.html')
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response = self.get_paginated_response(serializer.data)
            return response

        serializer = self.get_serializer(queryset, many=True)
        return Response({ 'results': serializer.data })
