from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .managers import *
import re
import json

from django.db import models
from django.core.exceptions import ValidationError, ImproperlyConfigured
from django.core.validators import MaxValueValidator, validate_comma_separated_integer_list
from django.utils.timezone import now
from django.conf import settings
from django.utils.translation import ugettext as _
from model_utils.managers import InheritanceManager
from django.db.models.signals import pre_save, post_save
import io

from django.contrib.auth.models import User
from django.contrib import messages
from django.forms import ModelForm
from django.utils.html import escape, mark_safe

# Create your models here.
class User(AbstractBaseUser):
    first_name = models.CharField(verbose_name='First Name', max_length=30)
    last_name = models.CharField(verbose_name='Last Name', max_length=30)
    email = models.EmailField(verbose_name='Email', max_length=100, unique=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    is_ngo_admin = models.BooleanField(default=False)
    is_donor = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " "+ self.last_name

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()
    def save(self, *args, **kwargs):
        self.username = self.email
        super(User, self).save(*args, **kwargs)
    def has_perm(self, perm, obj=None):
        return self.is_admin
    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


class NGO_Admin(User):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, parent_link=True)
    user.is_ngo_admin = True
    joinedSince = models.CharField(max_length = 4, blank=False)
    objects = NGO_AdminManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    date_of_birth = models.DateField(verbose_name = "DOB", blank = True, null=True)
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Donor(User):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, parent_link=True)
    user.is_donor = True
    objects = DonorManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

