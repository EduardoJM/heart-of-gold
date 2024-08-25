from django.db import transaction
from rest_framework import serializers
from modules.investments.stocks import models

class InvoiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invoice
        exclude = ["user"]

class InvoiceCreateTaxSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    value = serializers.IntegerField()

class InvoiceCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    taxes = InvoiceCreateTaxSerializer(many=True)

    def create(self, validated_data):
        taxes = validated_data.pop('taxes')
        
        with transaction.atomic():
            instance = super().create(validated_data)
            for tax in taxes:
                tax_item = models.Tax.objects.get_or_create(
                    name=tax.get('name')
                )
                models.InvoiceTax.objects.create(
                    tax=tax_item,
                    invoice=instance,
                    value=tax.get('value')
                )

        return instance

    class Meta:
        model = models.Invoice
        fields = "__all__"
