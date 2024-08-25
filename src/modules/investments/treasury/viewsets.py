from rest_framework import viewsets, mixins
from . import models, serializers

class TreasuryBondInformationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.TreasuryBondInformationSerializer
    queryset = models.TreasuryBondInformation.objects.all()

class TreasuryBondViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TreasuryBondSerializer
    
    def get_queryset(self):
        user = self.request.user
        return models.TreasuryBond.objects.filter(user=user).all()
