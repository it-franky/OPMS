from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^keep/$', TemplateView.as_view(template_name="zoro/keep.html"), name="keep"),
    url(r'^sunny/$', TemplateView.as_view(template_name="zoro/sunny.html"), name="sunny"),

]
