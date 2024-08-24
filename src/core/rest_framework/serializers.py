from rest_framework import serializers, status
from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _

class ActionNotFoundException(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = _('the action was not found on data serializers.')

class ActionSerializerInvalidException(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = _('the action serializer is not a valid rest_framework Serializer.')

class ActionsSerializers:
    create: serializers.Serializer = None
    retrieve: serializers.Serializer = None
    list: serializers.Serializer = None
    update: serializers.Serializer = None
    partial_update: serializers.Serializer = None

    @classmethod
    def get_serializer_for_action(cls, action_name: str) -> serializers.Serializer:
        if not hasattr(cls, action_name):
            raise ActionNotFoundException()
        serializer_class = getattr(cls, action_name)
        if not serializer_class:
            raise ActionNotFoundException()
        if not issubclass(serializer_class, serializers.Serializer):
            raise ActionSerializerInvalidException()
        return serializer_class
