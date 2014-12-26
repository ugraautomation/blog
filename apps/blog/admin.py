from django.contrib import admin
from taggit.models import Tag
from apps.blog.models import Post
import watson





from django.apps import AppConfig


class PostAppConfig(AppConfig):
    name = 'apps.blog'
    def ready(self):
        post_model = self.get_model('Post')
        watson.register(post_model)



class AdminPost(watson.SearchAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["__unicode__", "thumbnail_admin", ]
    exclude = ('_thumbnail', 'author',)
    search_fields = ("content", "title",)

    def save_model(self, request, task, form, change):
        task.author = request.user
        task.save()


admin.site.register(Post, AdminPost)


