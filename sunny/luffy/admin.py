from django.contrib import admin

# Register your models here.

from .models import TodoList  # Import our todo Model.


class TodoListAdmin(admin.ModelAdmin):
    list_display = ['big_class', 'sub_class', 'tasks', 'description','exec_time','exec_place','created_time','progress_rate']
    search_fields = ['big_class', 'sub_class', 'tasks', 'exec_time','exec_place']
    list_filter = ['big_class', 'sub_class', 'exec_time','exec_place','created_time','progress_rate']


admin.site.register(TodoList,TodoListAdmin)  # Register the model with the admin
