from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .viewsets import FundViewSet

router = SimpleRouter()
router.register('', FundViewSet, basename='Fund')

urlpatterns = [
    path('', include(router.urls)),
]
