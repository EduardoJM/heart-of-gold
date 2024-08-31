from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from .models import Fund
from .serializers import FundSerializer

@extend_schema(tags=['funds'])
class FundViewSet(viewsets.ModelViewSet):
    serializer_class = FundSerializer

    def get_queryset(self):
        user = self.request.user
        return Fund.objects.filter(user=user)
