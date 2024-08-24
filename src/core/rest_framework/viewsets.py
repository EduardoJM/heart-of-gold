from rest_framework import viewsets
from .mixins import ActionViewSetMixin

class ActionsGenericViewSet(ActionViewSetMixin, viewsets.GenericViewSet):
    pass

class ActionsModelViewSet(ActionViewSetMixin, viewsets.ModelViewSet):
    pass
