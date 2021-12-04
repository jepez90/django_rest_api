from django.conf import settings
from django.contrib.auth.backends import UserModel
from rest_framework import response, status, permissions
from rest_framework.generics import GenericAPIView
from django.contrib.auth import authenticate
from apps.accounts.models.customuser_model import CustomUser

from apps.accounts.serializers import CustomUserSerializer, LogInSerializer


class UserApiView(GenericAPIView):

    serializer_class = CustomUserSerializer

    def post(self, request):
        """ creates a new user """

        permission_classes = (permissions.IsAdminUser,)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        permission_classes = (permissions.IsAuthenticated, )
        user = request.user

        serialized = CustomUserSerializer(user)
        return response.Response({'user': serialized.data})


class LoginApiView(GenericAPIView):
    """ check the credentials of the user and returns an JWT token if the login
    is succes
    """

    serializer_class = LogInSerializer

    # override the default authentication classes to allow acces without JWTtoken
    authentication_classes = []

    def post(self, request):
        # get the data from the request
        # try to get the 3 fields, but only tow are nested
        # if email field is received, ignores the username

        # validates the data
        serialized = self.serializer_class(data=request.data)

        # if the validation doesn't was successfull, return the errors
        if not serialized.is_valid():
            return response.Response(serialized.errors, status.HTTP_400_BAD_REQUEST)

        # get the field used as identity of the user
        if "email" in serialized.data.keys():
            field_as_identity = "email"
        else:
            field_as_identity = "username"

        # try to perform the authentication
        try:
            user = authenticate(
                password=request.data.get("password"),
                username=serialized.data[field_as_identity]
            )
        except UserModel.DoesNotExist:
            # if the user doesn't exists
            message = {
                field_as_identity:
                f'El usuario \'{serialized.data[field_as_identity]}\' no se encuentra registrado'
            }
            return response.Response(message, status.HTTP_401_UNAUTHORIZED)

        # if user is not none, the authentication was successful
        if user:
            serializer = self.serializer_class(user)
            return response.Response(serializer.data, status.HTTP_200_OK)

        # if the user exist but the password is incorrect
        message = {'password': 'Contraseña incorrecta o usuario no autorizado'}
        return response.Response(message, status.HTTP_401_UNAUTHORIZED)
