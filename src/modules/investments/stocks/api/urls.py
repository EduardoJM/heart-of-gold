from rest_framework.routers import SimpleRouter
from . import viewsets

router = SimpleRouter()
router.register('invoices', viewsets.InvoiceViewSet, 'invoices')

urlpatterns = router.urls
