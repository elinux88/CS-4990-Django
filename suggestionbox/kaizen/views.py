from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Idea, Profile, Category, Comment

class IdeaListView(ListView):
    model = Idea

    def get_queryset(self):
        return Idea.objects.order_by('-pub_date')

class IdeaDetailView(DetailView):
    model = Idea

class CreateIdeaView(CreateView):
    model = Idea
    exclude = ['profile']
    fields = ['title', 'description', 'category']

    def form_valid(self, form):
        u = form.save(commit=False)
        u.profile = Profile.objects.filter(user=self.request.user)
        u.save()

    def get_success_url(self):
        return reverse('kaizen:addidea')

class SecretView(TemplateView):
    template_name="kaizen/secret.html"


