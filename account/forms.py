from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.forms.widgets import RadioSelect
from django.db import transaction
from django.forms.utils import ValidationError


class DonorSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    is_donor = forms.BooleanField()

    class Meta:
        model = Donor
        fields = ('first_name', 'last_name','is_donor', 'email', 'password1', 'password2', )

class NGO_Admin_SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    is_ngo_admin = forms.BooleanField()
    

    class Meta:
        model = NGO_Admin
        fields = ('first_name', 'last_name','is_ngo_admin', 'email', 'password1', 'password2', )
        



