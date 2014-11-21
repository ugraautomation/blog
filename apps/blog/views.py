from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import ListView
from apps.blog.models import Post


class Posts(ListView):
    context_object_name = 'posts'
    queryset = Post.objects.all().order_by("-created")
    template_name = 'blog/index.html'
    paginate_by = 2




