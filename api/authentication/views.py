from rest_framework import status, viewsets
from rest_framework.serializers import Serializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.users.serializers import UserSerializer
from .serializers import RefreshTokenSerializer


class AuthViewSet(viewsets.GenericViewSet):
    serializer_class = Serializer

    @action(detail=False, methods=["post"], permission_classes=[IsAuthenticated])
    def logout(self, request, pk=None):
        sz = RefreshTokenSerializer(data=request.data)
        sz.is_valid(raise_exception=True)
        sz.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["post"], permission_classes=[])
    def register(self, request, pk=None):
        sz = UserSerializer(data=request.data)
        sz.is_valid(raise_exception=True)
        sz.save()

        return Response(status.HTTP_201_CREATED)
