from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Account, Transaction, Category
from .serializers import AccountSerializer, TransactionSerializer, \
                         CategorySerializer


class AccountViewSet(ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Should return queryset with accounts of the current user."""
        return Account.objects.filter(owner__id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TransactionViewSet(ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Should return queryset with transactions for the current account."""
        return Transaction.objects.filter(account__owner__id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, context={'request': self.request})

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user, context={'request': self.request})


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Should return queryset with categories of the current user."""
        return Category.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, type=Category.CUSTOM)

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user, type=Category.CUSTOM)
