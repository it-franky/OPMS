from django.contrib import admin
import xadmin

from .models import Passwd
# Register your models here.

class PasswdAdmin(object):
    list_display = ['title', 'name', 'password', 'website','mark']
    search_fields = ['title', 'name', 'password', 'website','mark']
    list_filter = ['title', 'name', 'password', 'website','mark']

xadmin.site.register(Passwd, PasswdAdmin)
