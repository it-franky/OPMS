"""OPMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView

import xadmin

from franky.views import getform

urlpatterns = [
    url(r'xadmin/', include(xadmin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'luffy/', include('luffy.urls', namespace='luffy')),
    url(r'zoro/', include('zoro.urls', namespace='zoro')),
    url(r'nami/', include('nami.urls', namespace='nami')),
    url(r'sanji/', include('sanji.urls', namespace='sanji')),
    url(r'robin/', include('robin.urls', namespace='robin')),
    url(r'franky/', include('franky.urls', namespace='franky')),
    url(r'^frankymanual/$',
        TemplateView.as_view(template_name="frankymanual/website.html"),
        name="website"),

    url(r'^form/$', getform, name='go_form'),
    url(r'^timetable/$', TemplateView.as_view(template_name="timetable.html"), name="timetable"),

]
