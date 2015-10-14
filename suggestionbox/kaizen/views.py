from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin

from .forms import CommentForm
from .models import Idea, Profile, Category, Comment

class IdeaListView(ListView):
    model = Idea

    def get_queryset(self):
        return Idea.objects.order_by('-pub_date')

class IdeaDetailView(DetailView):
    model = Idea

class CreateIdeaView(CreateView):
    model = Idea
    #exclude = ['profile']
    #fields = ['title', 'description', 'category']
    fields = ['profile', 'title', 'description', 'category']

#   def form_valid(self, form):
#       u = form.save(commit=False)
#       u.profile = Profile.objects.filter(user=self.request.user)
#       u.save()

    def get_success_url(self):
        return reverse('kaizen:idealist')

    def get_context_data(self, *args, **kwargs):
        context = super(IdeaDetailView, self).get_context_data()
        context["form"] = CommentForm(initial={'idea_id': self.object.pk})
        return context;

class PostCommentFormView(FormView, SingleObjectMixin):
    form_class = CommentForm
    model = Idea
    success_url = reverse_lazy('kaizen:comment_success')

    def form_valid(self, form):
       comment = Comment()
       comment.idea = get_object_or_404(Idea, pk=form.cleaned_data["idea_id"])
       comment.profile = form.request.user
       comment.comment_text = form.cleaned_data['comment']
       comment.save()
       return super(PostCommentFormView, self).form_valid(form)

class UpdateIdeaView(UpdateView):
    model = Idea
    fields = ['title', 'description', 'category']

    def get_success_url(self):
        return reverse('kaizen:ideadetail', args=(self.object.pk,))

class SecretView(TemplateView):
    template_name="kaizen/secret.html"


