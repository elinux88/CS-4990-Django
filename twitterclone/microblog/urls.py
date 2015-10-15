from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', login_required(views.TemplateView.as_view()), name="idealist"),
]
