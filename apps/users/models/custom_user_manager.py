from django.conf import settings
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db.models.query_utils import Q
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def _create_user(self, username, email, password=None, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('The given email must be set')

        user = self.model(username=self.model.normalize_username(username),
                          email=self.normalize_email(email),
                          **extra_fields
                          )
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)

    def get_by_natural_key(self, username):
        """ manage both username and email authentication """
        auth_type = settings.AUTH_AUTHENTICATION_TYPE
        if auth_type == 'both':
                user = self.model.objects.get(
                    Q(username__iexact=username) | Q(email__iexact=username)
                )
                return user
        return self.get(**{self.model.USERNAME_FIELD: username})
