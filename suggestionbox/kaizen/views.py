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
    fields = ['profile', 'title', 'description', 'category']

    def get_success_url(self):
        return reverse('kaizen:addidea')

class SecretView(TemplateView):
    template_name="kaizen/secret.html"


