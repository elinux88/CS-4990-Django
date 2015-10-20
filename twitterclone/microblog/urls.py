from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name="postlist"),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.ProfileDetailView.as_view(), name="profiledetail"),
    url(r'^newpost/$', views.CreatePostView.as_view(), name="addpost"),
    #url(r'^$', login_required(views.PostListView.as_view()), name="idealist"),
]
