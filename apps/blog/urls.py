# -*- coding: utf-8 -*
from apps.blog import views
from apps.blog.views import Posts

__author__ = 'b9om'
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

  url(r'^$', Posts.as_view(), name='posts'),
)
