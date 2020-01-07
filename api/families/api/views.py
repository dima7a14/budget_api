from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.families import models
from .serializers import FamilySerializer


class ListFamily(generics.ListCreateAPIView):
    serializer_class = FamilySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """This view should return list of families where current user is a member."""
        user_id = self.request.user.id

        return models.Family.objects.filter(members__in=[user_id])


class DetailFamily(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FamilySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """This view should return a detail of family by id where current user is a member."""
        user_id = self.request.user.id

        return models.Family.objects.filter(members__in=[user_id])
