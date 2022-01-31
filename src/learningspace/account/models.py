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




STATUS_CHOICES = (
    ("Active", "Active"),
    ("Inactive", "Inactive"),
    ("Deactivated", "Deactivated"),
)


class User(AbstractUser):
    groups = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=13,null=True, blank=True)
    #can add address and extra fields if required
    REQUIRED_FIELDS = ['groups']
    USERNAME_FIELD = 'email'

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
    def is_admin(self):
        if self.groups.id == 1:
            return True
        else:
            return False

# Create your models here.
