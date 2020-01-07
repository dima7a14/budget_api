from rest_framework import serializers

from api.users.api.serializers import UserSerializer
from api.families.models import Family


class FamilySerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    members = UserSerializer(many=True)

    class Meta:
        fields = (
            'id',
            'name',
            'created_at',
            'updated_at',
            'owner',
            'members',
        )
        read_only_fields = ['id', 'created_at', 'updated_at', 'owner', 'members']
        model = Family
        depth = 1
