from rest_framework import serializers

from api.users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(allow_blank=False, allow_null=False, write_only=True, trim_whitespace=True)
    is_active = serializers.BooleanField(read_only=True, default=True)

    class Meta:
        fields = (
            'id',
            'email',
            'password',
            'first_name',
            'last_name',
            'is_staff',
            'is_active',
            'created_at',
            'updated_at',
        )
        model = User

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        return instance
