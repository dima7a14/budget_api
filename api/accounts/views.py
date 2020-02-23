from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Account
from .serializers import AccountSerializer


class AccountViewSet(ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Should return queryset with accounts of the current user."""
        return Account.objects.filter(owner__id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
