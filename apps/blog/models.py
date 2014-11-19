# -*- coding: utf-8 -*
from django.contrib.auth.models import User

from django.db import models
from django.utils.translation import ugettext_lazy as _
from taggit_autosuggest.managers import TaggableManager


class PostManager(models.Manager):
    use_for_related_fields = True

    def approved(self):
        return self.get_query_set().exclude(approved=False)

class Post(models.Model):
    title = models.CharField(_(u'title'), max_length=255)
    content = models.TextField(_(u'content'), help_text=_('Use Markdown and HTML'))
    created = models.DateTimeField(_(u'created'), auto_now_add=True)
    author = models.ForeignKey(User, editable=True)
    approved = models.BooleanField(_(u'approved'), default=True,
        help_text=_(u'Can be used for draft'))
    link = models.CharField(_(u'link to original'), blank=True, max_length=500)
    tag = TaggableManager()

    class Meta:
        ordering = ['-created']
        verbose_name = _(u'Posts')
        verbose_name_plural = _(u'Post')

    objects = PostManager()

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('posts:posts', [self.pk], {})

    def search(self):
        return dict(source=_(u'Post'), title=self.title, desc=self.content)

    def get_next(self):
        try:
            return Post.objects.all().filter(created__gt=self.created).exclude(pk=self.pk).order_by('created')[:1].get()
        except Post.DoesNotExist:
            return

    def get_prev(self):
        try:
            return Post.objects.all().filter(created__lt=self.created).exclude(pk=self.pk).order_by('-created')[:1].get()
        except Post.DoesNotExist:
            return