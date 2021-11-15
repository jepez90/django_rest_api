from rest_framework import response, status, permissions, exceptions
from rest_framework.generics import GenericAPIView
from django.contrib.auth import authenticate
from apps.user.models.customuser_model import CustomUser

from apps.user.serializers import CustomUserSerializer, LogInSerializer


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
        # try to get the 3 fields, but only thow are nested
        email = request.data.get('email', None)
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        if email and not username:
            try:
                user = self.serializer_class.Meta.model.objects.get(email=email)
                username = user.username
            except CustomUser.DoesNotExist as err:
                username = None
            
        user = authenticate(password=password, username=username)

        if user:
            serializer = self.serializer_class(user)
            return response.Response(serializer.data, status.HTTP_200_OK)

        # if the authentication fail
        message = {'message': 'Invalid credentials, try Again'}
        return response.Response(message, status.HTTP_401_UNAUTHORIZED)
