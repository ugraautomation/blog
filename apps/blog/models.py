# -*- coding: utf-8 -*

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from taggit_autosuggest.managers import TaggableManager
from _project_.settings.development import *
from _project_.class_utils.ImageThumbnail import ImageThumbnailAbstract
from django.utils.translation import ugettext_lazy as _
from django.db import models







class PostManager(models.Manager):
    use_for_related_fields = True

    def approved(self):
        return self.get_queryset().exclude(approved=False)


class Post(ImageThumbnailAbstract):
    title = models.CharField(_(u'title'), max_length=255)
    subtitle = models.CharField(_(u'under title'), max_length=255)
    content = RichTextField(_(u'content'))
    created = models.DateTimeField(_(u'created'), auto_now_add=True)
    author = models.ForeignKey(User, editable=True)
    approved = models.BooleanField(_(u'approved'), default=True,
                                   help_text=_(u'Can be used for draft'))
    link = models.CharField(_(u'link to original'), blank=True, max_length=500)
    slug = models.SlugField(_(u'slug'), default='')
    tag = TaggableManager()
    objects = PostManager()

    class Meta:
        ordering = ['-created']
        verbose_name = _(u'Posts')
        verbose_name_plural = _(u'Post')


    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog:post', (), {
            'slug': self.slug,
        })

    def get_next(self):
        try:
            return Post.objects.all().filter(created__gt=self.created).exclude(pk=self.pk).order_by('created')[:1].get()
        except Post.DoesNotExist:
            return

    def get_prev(self):
        try:
            return Post.objects.all().filter(created__lt=self.created).exclude(pk=self.pk).order_by('-created')[
                   :1].get()
        except Post.DoesNotExist:
            return

    def get_slugs_names(self):
        post = get_object_or_404(Post, pk=self.pk)
        slugs = post.tag.slugs()
        names = post.tag.names()
        ns = zip(names, slugs)
        return ns



