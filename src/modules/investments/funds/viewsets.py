from rest_framework import viewsets
from .models import Fund
from .serializers import FundSerializer

class FundViewSet(viewsets.ModelViewSet):
    serializer_class = FundSerializer

    def get_queryset(self):
        user = self.request.user
        return Fund.objects.filter(user=user)
