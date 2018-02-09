from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^edit/$', TemplateView.as_view(template_name="robin/edit.html"), name="edit"),
    url(r'^reading/$', TemplateView.as_view(template_name="robin/reading.html"), name="reading"),

]
