from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.

from .models import TodoList,TheFunctions
from django.shortcuts import render_to_response


def index(request):  # Define our function, accept a request

    items = TodoList.objects.all()  # ORM queries the database for all of the to-do entries.

    return render_to_response('luffy/todolist.html', {'items': items})  # Responds with passing the object items (contains info from the DB) to the template index.html



class TodolistView(View):

    def get(self,request):

        readinglists = TodoList.objects.filter(scope__scope__startswith='Reading')
        writinglists = TodoList.objects.filter(scope__scope__startswith='历史文本')
        codingTodolists = TodoList.objects.filter(scope__name__name='franky')

        return render(request, 'luffy/todolist.html', {
            "readinglists": readinglists,
            "writinglists": writinglists,
            "codingTodolists": codingTodolists,
        })
