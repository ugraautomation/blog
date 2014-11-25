from django.contrib import admin
from apps.blog.models import Post

class AdminPost(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post,AdminPost)
