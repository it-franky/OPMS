from django.conf.urls import url, include
from django.views.generic import TemplateView

from .views import TodolistView

urlpatterns = [
    url(r'^todolist/$', TodolistView.as_view(), name="todolist"),

]
