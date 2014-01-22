# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.core.cache import cache
from django.contrib.sites.models import Site
from django.utils.encoding import smart_unicode
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType

from .settings import INTENTS, CACHE_PREFIX
from .managers import SeoManager, URLManager


def make_key(cls, pk, intent):
    return ':'.join(map(smart_unicode, ('o', cls._meta, pk, intent)))


class UniqueModel(models.Model):

    class Meta:
        abstract = True

    def clean(self):
        """
        Check for instances with null values in unique_together fields.

        """
        from django.core.exceptions import ValidationError

        super(UniqueModel, self).clean()

        for field_tuple in self._meta.unique_together[:]:
            unique_filter = {}
            unique_fields = []
            null_found = False

            for field_name in field_tuple:
                field_value = getattr(self, field_name)
                if getattr(self, field_name) is None:
                    unique_filter['%s__isnull' % field_name] = True
                    null_found = True
                else:
                    unique_filter['%s' % field_name] = field_value
                    unique_fields.append(field_name)

            if null_found:
                unique_queryset = self.__class__.objects.filter(
                    **unique_filter)

                if self.pk:
                    unique_queryset = unique_queryset.exclude(pk=self.pk)

                if unique_queryset.exists():
                    msg = self.unique_error_message(
                        self.__class__, tuple(unique_fields))
                    raise ValidationError(msg)


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


class URL(UniqueModel):

    url = models.CharField(verbose_name=_('URL'),  max_length=200, default='/', unique=True,
        help_text=_("This should be an absolute path, excluding the domain name. Example: '/events/search/'."))

    site = models.ForeignKey(Site, blank=True, null=True)

    objects = URLManager()

    class Meta:
        verbose_name = _('URL')
        verbose_name_plural = _('URLs')
        unique_together = ("site", "url")

    def get_absolute_url(self):
        if self.site is not None:
            return '%s://%s%s' % (
                getattr(settings, "PROTOCOL", "http"),
                self.site.domain,
                self.url,
            )
        return self.url

    def __unicode__(self):
        return self.url
