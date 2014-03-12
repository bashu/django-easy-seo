# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType

from caching.base import CachingManager


class SeoManager(CachingManager):

    def for_object(self, instance):
        ct = ContentType.objects.get_for_model(instance.__class__)

        try:
            return self.filter(content_type=ct).get(object_id=instance.id)
        except ObjectDoesNotExist:
            return None

    def get_seo_object(self, instance):
        return self.for_object(instance)
