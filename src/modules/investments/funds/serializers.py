from rest_framework import serializers
from .models import Fund

class FundSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        instance = super().create(validated_data)
        from .tasks import compute_fund_value
        compute_fund_value.apply_async(args=[instance.pk], countdown=2) 

        return instance
    
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        from .tasks import compute_fund_value
        compute_fund_value.apply_async(args=[instance.pk], countdown=2)

        return instance

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs['currently_value'] = attrs['buy_value']
        return attrs

    class Meta:
        model = Fund
        fields = "__all__"
        read_only_fields = ['currently_value']
