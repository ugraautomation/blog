from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import ListView, DetailView
from apps.blog.models import Post


class Posts(ListView):
    context_object_name = 'posts'
    queryset = Post.objects.approved().order_by("-created")
    template_name = 'blog/index.html'
    paginate_by = 10


class TagView(ListView):
    context_object_name = 'posts'
    paginate_by = 10
    template_name = 'blog/index.html'

    def get_queryset(self):
        return Post.objects.approved().filter(tag__slug__in=[self.args[0]])







