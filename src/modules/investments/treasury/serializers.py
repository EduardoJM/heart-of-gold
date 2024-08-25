from rest_framework import serializers
from . import models

class TreasuryBondInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TreasuryBondInformation
        fields = "__all__"

class TreasuryBondSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TreasuryBond
        fields = "__all__"
