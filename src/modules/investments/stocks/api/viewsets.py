from rest_framework import viewsets
from modules.investments.stocks import models
from . import serializers

class InvoiceViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        request = self.request
        user = request.user
        return models.Invoice.objects.filter(user=user).all()

    def get_serializer_class(self):
        if self.action in ["create"]:
            return serializers.InvoiceCreateSerializer
        return serializers.InvoiceListSerializer
