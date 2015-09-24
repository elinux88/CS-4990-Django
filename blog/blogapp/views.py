from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
#from django.core.urlresolvers import reverse_lazy

#from .forms import CommentForm
from .models import Post, Comment, Category

class IndexView(ListView):
    template_name = 'blogapp/index.html'
    model = Post

    def get_queryset(self):
        # SELECT * from blogapp_post ORDER BY pub_date DESC LIMIT 5
        return Post.objects.order_by('-pub_date')[:5]

class PostDetailView(DetailView):
    model = Post

#   def get_context_data(self, *args, **kwargs):
#      context = super(PostDetailView, self).get_context_data(**kwargs)
#      context.update({"comment_list": self.get_object().comment_set.all()})
#      return context
#
#   def form_valid(self, form):
#      comment = Comment()
#      comment.person = form.cleaned_data['name']
#      comment.comment_text = form.cleaned_data['text']
#      comment.save()
#      return super(PostDetailView, self).form_valid(form)

class CategoryDetailView(DetailView):
    model = Category

