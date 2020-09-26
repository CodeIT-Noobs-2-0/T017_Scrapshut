from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from .models import User, Donor, NGO_Admin
#import nested_admin
from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from django.utils.translation import ugettext_lazy as _
from .models import *


# Register your models here.

class BaseUserAdmin(UserAdmin):
    list_display = ['email', 'is_admin', 'is_donor', 'is_ngo_admin']
    search_fields = ("email", 'is_admin', 'is_donor', 'is_ngo_admin')
    exclude = []

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ['email']


class DonorAdmin(UserAdmin):
    list_display = ('email', 'is_donor', 'is_ngo_admin')
    exclude = []
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ['email']


class NGO_Admin_Admin(UserAdmin):
    list_display = ('email', 'is_donor', 'is_ngo_admin')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    exclude = []
    ordering = ['email']



admin.site.site_header = 'My administration'
admin.site.site_title = 'Classroom'
admin.site.index_title = 'Site admin panel'

admin.site.unregister(Group)
'''
admin.site.register(User, BaseUserAdmin)
admin.site.register(Donor, DonorAdmin)
admin.site.register(NGO_Admin, NGO_Admin_Admin)
'''

admin.site.register(User)
admin.site.register(Donor)
admin.site.register(NGO_Admin)