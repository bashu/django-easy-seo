# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

from caching.base import CachingMixin, CachingManager


class Seo(CachingMixin, models.Model):

    title = models.CharField(
        verbose_name=_('title'), max_length=200, default='', blank=True)
    description = models.CharField(
        verbose_name=_('description'), max_length=200, default='', blank=True)
    keywords = models.CharField(
        verbose_name=_('keywords'), max_length=1000, default='', blank=True)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    objects = CachingManager()

    class Meta:
        verbose_name = _('SEO fields')
        verbose_name_plural = _('SEO fields')
        unique_together = ("content_type", "object_id")

    def __unicode__(self):
        return self.title


class Url(CachingMixin, models.Model):

    url = models.CharField(
        verbose_name=_('URL'), max_length=200, default='/', unique=True,
        help_text=_("This should be an absolute path, excluding the domain name. Example: '/about/'"),
    )

    objects = CachingManager()

    class Meta:
        verbose_name = _('URL')
        verbose_name_plural = _('URLs')

    def __unicode__(self):
        return self.url

    def get_absolute_url(self):
        return self.url
