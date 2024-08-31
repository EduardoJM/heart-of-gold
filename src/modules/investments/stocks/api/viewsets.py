from rest_framework import viewsets
from modules.investments.stocks import models
from drf_spectacular.utils import extend_schema
from . import serializers

@extend_schema(tags=['stocks'])
class InvoiceViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        request = self.request
        user = request.user
        return models.Invoice.objects.filter(user=user).all()

    def get_serializer_class(self):
        if self.action in ["create"]:
            return serializers.InvoiceCreateSerializer
        return serializers.InvoiceListSerializer
