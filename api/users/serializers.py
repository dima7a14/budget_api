from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from api.users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        allow_blank=False,
        allow_null=False,
        write_only=True,
        trim_whitespace=True,
    )
    new_password = serializers.CharField(
        allow_blank=False,
        allow_null=False,
        write_only=True,
        trim_whitespace=True,
        required=False,
    )
    is_active = serializers.BooleanField(read_only=True, default=True)

    class Meta:
        fields = (
            'id',
            'email',
            'password',
            'new_password',
            'first_name',
            'last_name',
            'is_staff',
            'is_active',
            'created_at',
            'updated_at',
        )
        model = User


    def validate(self, attrs):
        """
        Check that old password is correct and new password is provided.
        """
        old_pass = attrs.get('password', None)
        new_pass = attrs.get('new_password', None)

        if old_pass is not None and self.context['request'].method != 'POST':
            if new_pass is None:
                raise serializers.ValidationError({
                    'new_password': 'New password value is not provided'
                })
            if not self.instance.check_password(old_pass):
                raise serializers.ValidationError({
                    'password': 'Old password is incorrect'
                })

        return super().validate(attrs)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                pass
            elif attr == 'new_password':
                setattr(instance, 'password', make_password(value))
            else:
                setattr(instance, attr, value)

        instance.save()

        return instance
