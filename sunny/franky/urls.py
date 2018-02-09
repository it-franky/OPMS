from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^resume/$', TemplateView.as_view(template_name="franky/resume.html"), name="resume"),
    url(r'^skillSystem/$', TemplateView.as_view(template_name="franky/skillSystem.html"), name="skillSystem"),

]
