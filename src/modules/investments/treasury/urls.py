from rest_framework.routers import SimpleRouter
from . import viewsets

router = SimpleRouter()
router.register('bond-infos', viewsets.TreasuryBondInformationViewSet, 'treasury-bond-info')
router.register('bonds', viewsets.TreasuryBondViewSet, 'treasury-bond')

urlpatterns = router.urls
