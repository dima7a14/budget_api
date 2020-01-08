from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from api.users import models
from .serializers import UserSerializer, RefreshTokenSerializer


class ListUser(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class CreateUser(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request, *args, **kwargs):
        """
        Register user in system.
        """
        return self.create(request, *args, **kwargs)


class LogoutUser(generics.GenericAPIView):
    serializer_class = RefreshTokenSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args):
        sz = self.get_serializer(data=request.data)
        sz.is_valid(raise_exception=True)
        sz.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

