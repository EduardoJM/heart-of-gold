from rest_framework import viewsets, mixins
from drf_spectacular.utils import extend_schema
from . import models, serializers

@extend_schema(tags=['treasury'])
class TreasuryBondInformationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.TreasuryBondInformationSerializer
    queryset = models.TreasuryBondInformation.objects.all()

@extend_schema(tags=['treasury'])
class TreasuryBondViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TreasuryBondSerializer
    
    def get_queryset(self):
        user = self.request.user
        return models.TreasuryBond.objects.filter(user=user).all()
