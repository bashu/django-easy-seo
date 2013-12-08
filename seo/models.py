# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache
from django.utils.encoding import smart_unicode
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType

from .settings import INTENTS, CACHE_PREFIX
from .managers import SeoManager


def make_key(cls, pk, intent):
    return ':'.join(map(smart_unicode, ('o', cls._meta, pk, intent)))


class Seo(models.Model):

    title = models.CharField(
        verbose_name=_('title'), max_length=200, default='', blank=True)
    description = models.CharField(
        verbose_name=_('description'), max_length=200, default='', blank=True)
    keywords = models.CharField(
        verbose_name=_('keywords'), max_length=1000, default='', blank=True)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    objects = SeoManager()

    class Meta:
        verbose_name = _('SEO fields')
        verbose_name_plural = _('SEO fields')
        unique_together = ("content_type", "object_id")

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Seo, self).save(*args, **kwargs)

        for intent in INTENTS:
            cache_key = '%s:%s' % (CACHE_PREFIX, make_key(
                self.content_object, self.object_id, intent))
            cache.delete(cache_key)

    def delete(self, *args, **kwargs):
        object_id = self.object_id
        content_object = self.content_object
        super(Seo, self).delete(*args, **kwargs)

        for intent in INTENTS:
            cache_key = '%s:%s' % (CACHE_PREFIX, make_key(
                content_object, object_id, intent))
            cache.delete(cache_key)
