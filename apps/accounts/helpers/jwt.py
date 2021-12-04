from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework import exceptions
import jwt
from django.conf import settings

from apps.accounts.models.customuser_model import CustomUser


class JWTAuthentication(BaseAuthentication):
    """ Validates the JWT token """

    # error messasges as constants
    ERR_MSG_MISSING_TOKEN = 'Authentication is required, use JWT'
    ERR_MSG_INVALID_TOKEN = 'Token Not Valid'
    ERR_MSG_EXPIRED_TOKEN = 'Token is Expired, login again'
    ERR_MSG_USER_NOT_FOUND = 'No Such User'

    def authenticate(self, request):

        # get the authentication header
        auth_header = get_authorization_header(request)

        # get the content of the auth header
        auth_data = auth_header.decode('utf-8')

        auth_token = auth_data.split(' ')

        # checks if exists an JWT token
        if not auth_data.lower().startswith('bearer'):
            raise exceptions.AuthenticationFailed(self.ERR_MSG_MISSING_TOKEN)
        if len(auth_token) != 2:
            raise exceptions.AuthenticationFailed(self.ERR_MSG_INVALID_TOKEN)

        token = auth_token[1]
        try:
            # get the content of the token
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms='HS256')

            # gets the username from the token data
            username = payload['username']

            # gets the user from the database
            user = CustomUser.objects.get(username=username)

            # returns the user and token
            return (user, token)
        
        except jwt.ExpiredSignatureError as ex:
            # if the token is expired
            raise exceptions.AuthenticationFailed(self.ERR_MSG_EXPIRED_TOKEN)

        except jwt.DecodeError as ex:
            # if the token has an invalid format
            raise exceptions.AuthenticationFailed(self.ERR_MSG_INVALID_TOKEN)

        except CustomUser.DoesNotExist as err:
            # if the user for the given token doen't exist
            raise exceptions.AuthenticationFailed(self.ERR_MSG_USER_NOT_FOUND)
