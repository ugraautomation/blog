# -*- coding: utf-8 -*
from django.views.generic import DetailView
from apps.blog import views
from apps.blog.models import Post
from apps.blog.views import Posts, TagView

__author__ = 'b9om'
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

                       url(r'^$', Posts.as_view(), name='posts'),
                       url(r'^(?P<slug>[-\w\d]+)/$', DetailView.as_view(
                           model=Post,
                           template_name='blog/post.html', context_object_name='post'), name='post'),
                       url(r'^tag/([\w-]+)/$', TagView.as_view(), name='tag')
)
