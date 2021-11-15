
from rest_framework import serializers
from apps.user.models.customuser_model import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """ serializer for the user model """
    password = serializers.CharField(
        max_length=255, min_length=6, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'username')

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class LogInSerializer(serializers.ModelSerializer):
    """ serializer to check the login data """
    password = serializers.CharField(
        max_length=255, min_length=6, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'token')
        read_only_fields = ['token']
