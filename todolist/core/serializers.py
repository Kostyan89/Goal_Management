from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError, AuthenticationFailed

from core.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password_repeat = serializers.CharField(write_only=True)

    class Meta:
        model = User
        read_only_fields = ('id',)
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'password_repeat'
        )

    def validate(self, attrs: dict) -> dict:
        password: str = attrs.get('password')
        password_repeat: str = attrs.pop('password_repeat', None)
        if password != password_repeat:
            raise ValidationError('passwords are not equal')
        return attrs

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs: dict) -> dict:
        if user := authenticate(username=attrs['username'], password=attrs['password']):
            return user
        raise AuthenticationFailed


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ('id',)
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
        )


class UpdatePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, validators=[validate_password], required=True)

    class Meta:
        model = User
        read_only_fields = ("id",)
        fields = ("old_password", "new_password")

    def validate(self, attrs):
        user: User = self.context['request'].user
        if not user.check_password(attrs['old_password']):
            raise ValidationError({'old_password': 'field is incorrect'})
        return attrs

    def save(self, **kwargs):
        user: User = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save(updated_fields=['password'])
        return user
