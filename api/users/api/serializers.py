from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from api.users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(allow_blank=False, allow_null=False, write_only=True, trim_whitespace=True)

    class Meta:
        fields = (
            'id',
            'email',
            'password',
            'first_name',
            'last_name',
            'is_staff',
            'is_active',
            'last_login',
        )
        model = User

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        return instance


class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': 'Token is invalid or expired',
    }

    def validate(self, attrs):
        self.token = attrs['refresh']

        return attrs

    def save(self, **kwargs):
        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except TokenError:
            self.fail('bad_token')

