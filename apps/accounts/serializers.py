

from django.conf import settings
from rest_framework import serializers
from apps.accounts.models.customuser_model import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """ serializer for the user model """
    password = serializers.CharField(
        max_length=255, min_length=6, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'username')

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class LogInSerializer(serializers.Serializer):
    """ serializer to check the login data """
    __auth_type = settings.AUTH_AUTHENTICATION_TYPE

    password = serializers.CharField(
        max_length=255, min_length=6 , write_only=True)

    email = serializers.EmailField(
        max_length=255, required=__auth_type=="email")

    username = serializers.CharField(
        max_length=255, min_length=2,  required=__auth_type=="username")

    token = serializers.CharField(
        max_length=255, min_length=100, required=False)

    def validate(self, data):
        """
        Check the existence of one of username or email, only if auth_type is both
        """
        email = data.get('email')
        username = data.get('username')
        if self.__auth_type == 'both':
            if email is None and username is None:
                raise serializers.ValidationError(
                    {"username": "Debe existir el campo username o el campo email",
                    "email": "Debe existir el campo username o el campo email"})
        return data

    class Meta:
        read_only_fields = ['token']
