from django.shortcuts import render

# Create your views here.

from .models import TodoList
from django.shortcuts import render_to_response


def index(request):  # Define our function, accept a request

    items = TodoList.objects.all()  # ORM queries the database for all of the to-do entries.

    return render_to_response('todolist.html', {'items': items})  # Responds with passing the object items (contains info from the DB) to the template index.html