from rest_framework import serializers
from modules.investments.stocks import models
from core.rest_framework.serializers import ActionsSerializers

class InvoiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invoice
        exclude = ["user"]

class InvoiceCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Invoice
        fields = "__all__"

class StockSerializer(ActionsSerializers):
    class ListSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.Stock
            fields = "__all__"

    class CreateSerializer(serializers.ModelSerializer):
        ticket = serializers.CharField(max_length=10)
        user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
        class Meta:
            model = models.Stock
            fields = "__all__"
        
        def create(self, validated_data):
            ticket = validated_data.pop('ticket')
            ticket = models.Ticket.objects.update_or_create(ticket=ticket)
            validated_data['ticket'] = ticket
            return super().create(validated_data)

    list = ListSerializer
    create = CreateSerializer
    add = CreateSerializer
