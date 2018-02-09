from django.contrib import admin

import xadmin
from .models import TodoList, Members,TheFunctions  # Import our todo Model.


# Register your models here.

class MembersAdmin(object):
    list_display = ['name','label']
    search_fields = ['name','label']
    list_filter = ['name','label']


class TheFunctionsAdmin(object):
    list_display = ['name', 'scope']
    search_fields = ['name', 'scope']
    list_filter = ['name', 'scope']


class TodoListAdmin(object):
    list_display = ['scope', 'task', 'description', 'created_time', 'start_date', 'end_date', 'progress_rate']
    search_fields = ['scope', 'task', 'description', 'created_time', 'start_date', 'end_date', 'progress_rate']
    list_filter = ['scope', 'task', 'description', 'created_time', 'start_date', 'end_date', 'progress_rate']


# admin.site.register(TodoList,TodoListAdmin)  # Register the model with the admin

xadmin.site.register(Members, MembersAdmin)
xadmin.site.register(TheFunctions, TheFunctionsAdmin)
xadmin.site.register(TodoList, TodoListAdmin)
