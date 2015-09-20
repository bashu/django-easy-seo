# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType

try:
    from caching.base import CachingManager
except ImportError:
    class CachingManager(models.Manager):

        def get_query_set(self):
            return CachingQuerySet(self.model, using=self._db)

        def invalidate(self, *args, **kwargs):
            pass

        def no_cache(self):
            return self


    class CachingQuerySet(models.query.QuerySet):

        def no_cache(self):
            return self


class SeoManager(CachingManager):

    def for_object(self, instance):
        ct = ContentType.objects.get_for_model(instance.__class__)

        try:
            return self.filter(content_type=ct).get(object_id=instance.id)
        except ObjectDoesNotExist:
            return None
