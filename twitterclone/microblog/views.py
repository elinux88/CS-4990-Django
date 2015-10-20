from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from .models import Profile, Post

class PostListView(ListView):
    model = Post
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')

class ProfileDetailView(DetailView):
    model = Profile

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')[:10]

class CreatePostView(CreateView):
    model = Post
    fields = ['body']

    def get_success_url(self):
        return reverse('microblog:postlist')

    def form_valid(self, form):
        u = form.save(commit=False)
        u.profile = Profile.objects.filter(user=self.request.user)[0]
        u.save()
        return super(CreatePostView, self).form_valid(form)
