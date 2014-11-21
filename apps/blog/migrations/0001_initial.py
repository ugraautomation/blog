# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit_autosuggest.managers
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('content', models.TextField(help_text='Use Markdown and HTML', verbose_name='content')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('approved', models.BooleanField(help_text='Can be used for draft', verbose_name='approved', default=True)),
                ('link', models.CharField(blank=True, verbose_name='link to original', max_length=500)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('tag', taggit_autosuggest.managers.TaggableManager(through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags', to='taggit.Tag')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Posts',
                'verbose_name_plural': 'Post',
            },
            bases=(models.Model,),
        ),
    ]
