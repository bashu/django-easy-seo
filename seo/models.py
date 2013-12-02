# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache
from django.contrib.sites.models import Site
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType

from caching.base import CachingMixin
from caching.invalidation import make_key

from .settings import INTENTS, CACHE_PREFIX
from .managers import SeoManager


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

    site = models.ForeignKey('sites.Site', blank=True, null=True)

    objects = SeoManager()

    class Meta:
        verbose_name = _('SEO fields')
        verbose_name_plural = _('SEO fields')
        unique_together = ("content_type", "object_id")

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Seo, self).save(*args, **kwargs)

        # Now also invalidate the cache used in the templatetag
        for site_id in Site.objects.values_list('pk', flat=True):
            for intent in INTENTS:
                cache_key = '%s:%s' % (CACHE_PREFIX, make_key('%s.%s:%s' % (
                    site_id, self.object_id, intent)))
                cache.delete(cache_key)

    def delete(self, *args, **kwargs):
        object_id = self.object_id
        super(Seo, self).delete(*args, **kwargs)

        # Now also invalidate the cache used in the templatetag
        for site_id in Site.objects.values_list('pk', flat=True):
            for intent in INTENTS:
                cache_key = '%s:%s' % (CACHE_PREFIX, make_key('%s.%s:%s' % (
                    site_id, object_id, intent)))
                cache.delete(cache_key)
