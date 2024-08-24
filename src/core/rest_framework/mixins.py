from .serializers import ActionsSerializers

class ActionViewSetMixin:
    def get_serializer_class(self):
        if not issubclass(self.serializer_class, ActionsSerializers):
            return super().get_serializer_class()
        return self.serializer_class.get_serializer_for_action(self.action)
