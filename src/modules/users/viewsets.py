from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer


class UserViewSet(viewsets.GenericViewSet):
    @action(detail=False, methods=["GET"], permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = UserSerializer(
            request.user,
            context={"request": request},
        )
        return Response(serializer.data)
