from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, View, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView

from .models import Profile, Post

class ListAllPosts(ListView):
    model = Post
    paginate_by = 10
    queryset = Post.objects.all().order_by('-pub_date')

class ProfileDetailView(DetailView):
    model = Profile

class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['bio', 'profile_picture']

    def get_success_url(self):
        return reverse('microblog:profiledetail', args=[Profile.objects.filter(user = self.request.user)[0].id])

class MyFeedView(ListView):
    model = Post
    paginate_by = 10
    template_name = "microblog/myfeed.html"

    def get_queryset(self):
        my_profile, created = Profile.objects.get_or_create(user = self.request.user)
        #my_profile = self.request.user.profile_set.all()[0]
        following_profile_list = list(my_profile.following.all())
        following_profile_list.append(my_profile)
        return Post.objects.filter(profile__in = following_profile_list)

class FollowFormView(SingleObjectMixin, View):
    model = Profile

    def post(self, request, *args, **kwargs):
        try:
            my_profile = self.request.user.profile_set.all()[0]
        except Profile.DoseNotExist:
            my_profile = Profile(user = request.user, bio = '')
        #my_profile = request.user.profile_set.all()[0]
        my_profile.following.add(self.get_object())
        my_profile.save()
        return HttpResponseRedirect(reverse('microblog:followsuccess', kwargs = {'pk': self.get_object().pk}))

class FollowSuccessView(DetailView):
    template_name = 'microblog/follow_success.html'
    model = Profile

class CreatePostView(CreateView):
    model = Post
    fields = ['body']

    def get_success_url(self):
        return reverse('microblog:profiledetail', args=[Profile.objects.filter(user = self.request.user)[0].id])

    def form_valid(self, form):
        u = form.save(commit=False)
        u.profile = Profile.objects.filter(user=self.request.user)[0]
        u.save()
        return super(CreatePostView, self).form_valid(form)
