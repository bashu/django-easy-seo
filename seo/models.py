# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.encoding import python_2_unicode_compatible

from .managers import SeoManager


@python_2_unicode_compatible
class Seo(models.Model):

    title = models.CharField(
        verbose_name=_('title'), max_length=200, default='', blank=True)
    description = models.CharField(
        verbose_name=_('description'), max_length=200, default='', blank=True)
    keywords = models.CharField(
        verbose_name=_('keywords'), max_length=1000, default='', blank=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    objects = SeoManager()

    class Meta:
        verbose_name = _('SEO fields')
        verbose_name_plural = _('SEO fields')
        unique_together = ("content_type", "object_id")

    def __str__(self):
        return self.title
