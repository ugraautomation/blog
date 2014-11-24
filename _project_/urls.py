from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '_project_.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    url(r'^blog/',include('apps.blog.urls','blog')),
    url(r'^ckeditor/', include('ckeditor.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
