from django.conf import settings
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db.models.query_utils import Q
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """ manage the CustomUser entities """
    def _create_user(self, username, email, password=None, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """

        # validates the data
        if not username:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('The given email must be set')

        # creates an instance of the CustomUser
        user = self.model(username=self.model.normalize_username(username),
                          email=self.normalize_email(email),
                          **extra_fields
                          )

        # get the encrypted password
        user.password = make_password(password)

        # store the user in db
        user.save(using=self._db)

        # returns the new user
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        """ creates a generic user """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        """ creates the superuser from console """

        # set to true the default value of is_staff and is_su
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # check the value of is_staff. it must be true for superusers
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        # check the value of is_superuser. it must be true for superusers
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        # returns the created user
        return self._create_user(username, email, password, **extra_fields)

    def get_by_natural_key(self, username):
        """ manage both username and email authentication """

        # get the authentication type from the settings
        auth_type = settings.AUTH_AUTHENTICATION_TYPE

        # if is set to booth, try to get the user by username
        if auth_type == 'both':
                user = self.model.objects.get(
                    Q(username__iexact=username) | Q(email__iexact=username)
                )
                return user

        # otherwise, try to get the user by USERNAME_FIELD of the model
        return self.get(**{self.model.USERNAME_FIELD: username})
