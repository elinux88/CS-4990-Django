from django.shortcuts import render
from django.views.generic import DetailView, ListView

class PostListView(ListView):
    model = Post

class ProfileDetailView(DetailView):
    model = Profile

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')[:10]
