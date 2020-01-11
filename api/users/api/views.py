from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from api.users import models
from .serializers import UserSerializer, RefreshTokenSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = models.User.objects.all()

    @action(detail=False, methods=["post"], permission_classes=[IsAuthenticated])
    def logout(self, request, pk=None):
        sz = RefreshTokenSerializer(data=request.data)
        sz.is_valid(raise_exception=True)
        sz.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["post"], permission_classes=[])
    def register(self, request, pk=None):
        return self.create(request)

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def info(self, request, pk=None):
        current_user = request.user
        sz = self.get_serializer(current_user)

        return Response(sz.data)
