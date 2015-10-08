from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Idea, Profile, Category, Comment

class IdeaListView(ListView):
    model = Idea

class SecretView(TemplateView):
    template_name="kaizen/secret.html"
