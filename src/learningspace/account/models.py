import datetime
import random
import string
import logging

from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils import timezone
from django.utils.functional import cached_property
from rest_framework.response import Response
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=13,null=True, blank=True)
    #can add address and extra fields if required
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    @property
    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    @property
    def get_short_name(self):
        return self.first_name

    @property
    def is_student(self):
        if self.groups.id == 2:
            return True
        else:
            return False

    @property
    def is_mentor(self):
        if self.groups.id == 1:
            return True
        else:
            return False

# Create your models here.
