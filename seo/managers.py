# -*- coding: utf-8 -*-

from django.db.models import Model
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType

from caching.base import CachingManager


class UrlManager(CachingManager):

    def get_seo_object(self, url, site=None):
        from .models import Seo

        try:
            urlobj = self.get(url=url, site=site)
        except ObjectDoesNotExist:
            try:
                urlobj = self.get(url=url, site=None)
            except ObjectDoesNotExist:
                return None

        return Seo.objects.for_model(urlobj)


class SeoManager(CachingManager):

    def get_or_create_for(self, instance, site=None):
        ct = ContentType.objects.get_for_model(instance.__class__)
        return self.get_or_create(
            content_type=ct, object_id=instance.id, site=site)

    def for_model(self, instance, site=None):
        ct = ContentType.objects.get_for_model(instance.__class__)
        try:
            return self.get(content_type=ct, object_id=instance.id, site=site)
        except ObjectDoesNotExist:
            try:
                return self.get(content_type=ct, object_id=instance.id, site=None)
            except ObjectDoesNotExist:
                return None

    def get_seo_object(self, instance, site=None):
        if not isinstance(instance, Model):
            return None
        return self.for_model(instance, site)
