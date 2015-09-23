from django.shortcuts import render
from django.views import generic

from .forms import CommentForm
from .models import Post, Comment, Category

class IndexView(generic.ListView):
    template_name = 'blogapp/index.html'
    model = Post

    def get_queryset(self):
        # SELECT * from blogapp_post ORDER BY pub_date DESC LIMIT 5
        return Post.objects.order_by('-pub_date')[:5]

class PostDetailView(generic.DetailView):
    model = Post

#   def get_context_data(self):
#       context = super(PostDetail, self).get_context_data()
#       context.update({"comment_list": self.get_object().comment_set.all()})
#       return context

class CategoryDetailView(generic.DetailView):
    model = Category

def getCategory(request, categorySlug):
    posts = Post.objects.all().order_by('-pub_date')
    category_posts = []
    for post in posts:
        if post.category.filter(slug=categorySlug):
            category_posts.append(post)

def get_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('blogapp/index')
    else:
        form = CommentForm()
    return render(request, 'blogapp/post_detail.html', {'form': form})
