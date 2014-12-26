# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor.fields
import taggit_autosuggest.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_image', models.ImageField(upload_to=b'uploads/', null=True, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('_thumbnail', models.ImageField(upload_to=b'uploads/', null=True, verbose_name=b'\xd0\x9c\xd0\xb8\xd0\xbd\xd0\xb8\xd0\xb0\xd1\x82\xd1\x8e\xd1\x80\xd0\xb0 \xd0\xb8\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('subtitle', models.CharField(max_length=255, verbose_name='under title')),
                ('content', ckeditor.fields.RichTextField(verbose_name='content')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('approved', models.BooleanField(default=True, help_text='Can be used for draft', verbose_name='approved')),
                ('link', models.CharField(max_length=500, verbose_name='link to original', blank=True)),
                ('slug', models.SlugField(default=b'', verbose_name='slug')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('tag', taggit_autosuggest.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Posts',
                'verbose_name_plural': 'Post',
            },
            bases=(models.Model,),
        ),
    ]
