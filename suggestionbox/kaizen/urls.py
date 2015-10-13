from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', login_required(views.IdeaListView.as_view()), name="idealist"),
    url(r'^idea/(?P<pk>[0-9]+)/$', views.IdeaDetailView.as_view(), name="ideadetail"),
    url(r'^addidea/$', login_required(views.CreateIdeaView.as_view()), name="addidea"),
    url(r'^editidea/(?P<pk>[0-9]+)/$', login_required(views.UpdateIdeaView.as_view()), name="editidea"),
    url(r'^secrets/$', login_required(views.SecretView.as_view()), name="secret"),
]
