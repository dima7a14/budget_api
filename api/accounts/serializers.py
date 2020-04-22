from rest_framework import serializers
from djmoney.settings import CURRENCIES
from djmoney.contrib.django_rest_framework import MoneyField

from api.accounts.models import Account, Transaction, Category


class AccountSerializer(serializers.ModelSerializer):
    owner_id = serializers.IntegerField(read_only=True)
    balance = MoneyField(max_digits=14, decimal_places=2, coerce_to_string=False)
    balance_currency = serializers.ChoiceField(CURRENCIES,
                                               error_messages={'invalid_choice': '{input} is not a valid currency'})

    class Meta:
        fields = (
            'id',
            'name',
            'description',
            'created_at',
            'updated_at',
            'balance',
            'balance_currency',
            'owner_id',
        )
        read_only_fields = ['id', 'created_at', 'updated_at', 'owner_id']

        model = Account
        depth = 1


class TransactionSerializer(serializers.ModelSerializer):
    created_by_id = serializers.IntegerField(read_only=True)
    account_id = serializers.IntegerField(required=True)
    category_id = serializers.IntegerField(required=False)
    value = serializers.DecimalField(max_digits=14, decimal_places=2, coerce_to_string=False, required=True)

    class Meta:
        fields = (
            'id',
            'name',
            'description',
            'created_at',
            'updated_at',
            'value',
            'account_id',
            'created_by_id',
            'category_id',
        )
        read_only_fields = ['id', 'created_at', 'updated_at', 'created_by_id']

        model = Transaction
        depth = 1


class CategorySerializer(serializers.ModelSerializer):
    created_by_id = serializers.IntegerField(read_only=True)

    class Meta:
        fields = (
            'id',
            'name',
            'description',
            'created_at',
            'updated_at',
            'type',
            'created_by_id',
        )
        read_only_fields = ['id', 'created_at', 'updated_at', 'created_by_id', 'type']
        model = Category
        depth = 1
