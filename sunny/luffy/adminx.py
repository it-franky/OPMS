from django.contrib import admin

import xadmin
from .models import TodoList  # Import our todo Model.
# Register your models here.



class TodoListAdmin(object):
    list_display = ['big_class', 'sub_class', 'tasks', 'description','exec_time','exec_place','created_time','progress_rate']
    search_fields = ['big_class', 'sub_class', 'tasks', 'exec_time','exec_place']
    list_filter = ['big_class', 'sub_class', 'exec_time','exec_place','created_time','progress_rate']


# admin.site.register(TodoList,TodoListAdmin)  # Register the model with the admin

xadmin.site.register(TodoList, TodoListAdmin)
