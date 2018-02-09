from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^business/$', TemplateView.as_view(template_name="nami/business.html"), name="business"),
]
