from rest_framework.routers import SimpleRouter

from .viewsets import UserViewSet

router = SimpleRouter()
router.register("", UserViewSet, basename="User")

urlpatterns = router.urls
