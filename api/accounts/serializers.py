from rest_framework import serializers
from djmoney.settings import CURRENCIES
from djmoney.contrib.django_rest_framework import MoneyField

from api.accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    owner_id = serializers.IntegerField(read_only=True)
    balance = MoneyField(max_digits=14, decimal_places=2)
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
