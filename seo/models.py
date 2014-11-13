# -*- coding: utf-8 -*-

from django.db import models
from django.dispatch import receiver
from django.db.models import signals
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType

try:
    from caching.base import CachingMixin

except ImportError:
    class CachingMixin(object):
        pass

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

    objects = SeoManager()

    class Meta:
        verbose_name = _('SEO fields')
        verbose_name_plural = _('SEO fields')
        unique_together = ("content_type", "object_id")

    def __unicode__(self):
        return self.title

@receiver(signals.post_save, sender=Seo)
def force_invalidation(sender, instance, **kwargs):
    if instance is not None and instance.content_object is not None:
        Seo.objects.invalidate(*[
            Seo.objects.for_object(instance.content_object)])
