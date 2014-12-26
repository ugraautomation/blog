# -*- coding: utf-8 -*
from django.db.models.base import ModelBase

__author__ = 'b9om'

import os
from tempfile import NamedTemporaryFile
from django.db import models
from django.db.models import ImageField
from _project_.settings.development import *
from PIL import Image as PImage
from os.path import join as pjoin
from django.core.files import File


class ImageThumbnailAbstract(models.Model):

    _image = ImageField(upload_to='uploads/', verbose_name='Изображение', blank=True, null=True)
    _thumbnail = ImageField(upload_to='uploads/', verbose_name='Миниатюра изображения', blank=True,
                            null=True)

    def save(self, *args, **kwargs):
        super(ImageThumbnailAbstract, self).save(*args, **kwargs)
        if self._image:
            pht = PImage.open(pjoin(MEDIA_ROOT, self._image.name))
            self.save_thumbnail(pht, 1, (128, 128))
        super(ImageThumbnailAbstract, self).save(*args, **kwargs)

    def save_thumbnail(self, pht, num, size):
        fn, ext = os.path.splitext(self._image.name)
        pht.thumbnail(size, PImage.ANTIALIAS)
        thumb_fn = fn + '-thumb' + str(num) + ext
        tf = NamedTemporaryFile(delete=True)
        t_ext = str(ext.split('.')[1:][0])
        if t_ext.upper() == 'JPG':
            t_ext = 'JPEG'
        pht.save(tf.name, t_ext)
        thumbnail = getattr(self, '_thumbnail')
        thumbnail.save(thumb_fn, File(open(tf.name)), save=False)
        tf.close()

    def thumbnail_url(self):
        return MEDIA_URL + self._thumbnail.name

    def image_url(self):
        return MEDIA_URL + self._image.name

    def thumbnail_admin(self):
        return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" /></a>""" % (
            (self._image.name, self._thumbnail.name))

    thumbnail_admin.allow_tags = True
    thumbnail_admin.short_description = 'Изображение'

    class Meta:
        abstract = True