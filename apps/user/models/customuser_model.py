from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.conf import settings

from apps.user.models.customuser_manager_model import CustomUserManager

import datetime
import jwt


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """ Model to be used in login """

    username_validator = UnicodeUsernameValidator()

    # holds the manager
    objects = CustomUserManager()

    # fields
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    doccument = models.CharField(
        _('Identity Doccument'), unique=True, max_length=15)
    email = models.EmailField(_('email address'), blank=False, unique=True)
    full_name = models.CharField(_('full name'), max_length=150, blank=True)

    creator = models.ForeignKey(
        'CustomUser', on_delete=models.PROTECT, related_name='created_users', default=1)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    last_change = models.DateTimeField(
        _('last password change'), blank=True, auto_now_add=True)

    # remove the fields of the parent
    first_name = None
    last_name = None

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'full_name', 'doccument']

    email_verified = models.BooleanField(
        _('email_verified'),
        default=False,
        help_text=_(
            'Designates whether this user email is verified. '
        ),
    )

    class Meta():
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def token(self):
        """ generates a JWT token """
        TOKEN_EXPIRE_HOURS = 12
        data = {
            'username': self.username,
            'email': self.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=TOKEN_EXPIRE_HOURS)
        }
        token = jwt.encode(
            data,
            settings.SECRET_KEY,
            algorithm='HS256'
        )
        return token
