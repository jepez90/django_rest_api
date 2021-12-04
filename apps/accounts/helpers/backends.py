from django.contrib.auth.backends import ModelBackend, UserModel
from django.conf import settings

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        auth_type = settings.AUTH_AUTHENTICATION_TYPE

        if username is None:

            if auth_type != 'both':
                # the default vehavior
                username = kwargs.get(UserModel.USERNAME_FIELD)
            else:
                # get the email field if it exist
                username = kwargs.get(UserModel.EMAIL_FIELD)

        if username is None or password is None:
            return

        user = UserModel._default_manager.get_by_natural_key(username)
        if user.check_password(password) and self.user_can_authenticate(user):
            return user

