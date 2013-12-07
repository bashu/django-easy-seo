# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType

from caching.base import CachingManager

from .settings import CACHE_TIMEOUT


class SeoManager(CachingManager):

    def for_model(self, instance):
        ct = ContentType.objects.get_for_model(instance.__class__)

        queryset = self.filter(content_type=ct).cache(CACHE_TIMEOUT)
        try:
            return queryset.get(object_id=instance.id)
        except ObjectDoesNotExist:
            return None

    def get_seo_object(self, instance):
        return self.for_model(instance)
