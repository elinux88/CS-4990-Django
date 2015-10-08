from django.contrib import admin
from .models import Idea, Category, Comment

admin.site.register(Idea)
admin.site.register(Category)
admin.site.register(Comment)
