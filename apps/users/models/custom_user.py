from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.conf import settings
import datetime
import jwt

from apps.users.models.custom_user_manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
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
    last_change = models.DateTimeField(
        _('last password change'), blank=True, auto_now_add=True)
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

    # remove the fielsd of the parent
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
        token = jwt.encode(
            {
                'username': self.username,
                'email': self.email,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=6)
            },
            settings.SECRET_KEY,
            algorithm='HS256'
        )
        return token
