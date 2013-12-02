# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType

from caching.base import CachingManager


class SeoManager(CachingManager):

    def for_model(self, instance, site=None):
        ct = ContentType.objects.get_for_model(instance.__class__)
        try:
            return self.get(content_type=ct, object_id=instance.id, site=site)
        except ObjectDoesNotExist:
            try:
                return self.get(
                    content_type=ct, object_id=instance.id, site=None)
            except ObjectDoesNotExist:
                return None

    def get_seo_object(self, instance, site=None):
        return self.for_model(instance, site)
