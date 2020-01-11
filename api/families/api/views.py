from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from api.users.models import User
from api.users.api.serializers import UserSerializer
from api.families.models import Family
from .serializers import BaseFamilySerializer, CreateFamilySerializer, MemberSerializer


class FamilyViewSet(viewsets.ModelViewSet):
    serializer_class = BaseFamilySerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == "POST" or self.request.method == "PATCH":
            return CreateFamilySerializer

        return self.serializer_class

    def get_queryset(self):
        """This view should return list of families where current user is a member."""
        user_id = self.request.user.id

        return Family.objects.filter(members__in=[user_id])

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, url_path="members", methods=["get", "put", "delete"])
    def members(self, request, pk=None):
        family = self.get_object()

        if request.method == "PUT":
            serializer = MemberSerializer(data=request.data)

            if serializer.is_valid():
                ids = serializer.data.get("ids", [])
                family.members.add(*ids)
                family.save()

                recent_members = User.objects.filter(id__in=ids)

                return Response(UserSerializer(recent_members, many=True).data)
            else:
                return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        elif request.method == "DELETE":
            serializer = MemberSerializer(data=request.data)

            if serializer.is_valid():
                ids = serializer.data.get("ids", [])
                family.members.remove(*ids)
                family.save()

                return Response({"status": "Deleted."})
            else:
                return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        page = self.paginate_queryset(family.members.all())
        serializer = UserSerializer(page, many=True)

        return self.get_paginated_response(serializer.data)
