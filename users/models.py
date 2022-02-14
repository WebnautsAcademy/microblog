import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
# from users.managers import UserManager
from users.managers import UserManager


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    username = models.CharField(max_length=150, unique=True, db_index=True)
    email = models.EmailField(null=True, blank=True)
    first_name = models.CharField(max_length=150, null=True, blank=True, db_index=True)
    last_name = models.CharField(max_length=150, null=True, blank=True, db_index=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    phone = models.CharField(blank=True, null=True, verbose_name=_('phone'), max_length=32)
    is_staff = models.BooleanField(default=False, verbose_name=_('staff status'))

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()
