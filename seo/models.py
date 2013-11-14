# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType

from caching.base import CachingMixin

from .managers import SeoManager, UrlManager


class BaseModel(models.Model):

    class Meta:
        abstract = True

    def clean(self):
        """
        Check for instances with null values in unique_together fields.

        """
        from django.core.exceptions import ValidationError

        super(BaseModel, self).clean()

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


class Url(CachingMixin, BaseModel):

    url = models.CharField(
        verbose_name=_('URL'), max_length=200, default='/',
        help_text=_("This should be an absolute path, excluding the domain name. Example: '/about/'"),
    )

    site = models.ForeignKey('sites.Site', blank=True, null=True)

    objects = UrlManager()

    class Meta:
        verbose_name = _('URL')
        verbose_name_plural = _('URLs')
        unique_together = ("url", "site")

    def __unicode__(self):
        return self.url

    def get_absolute_url(self):
        return self.url
