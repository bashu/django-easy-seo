# -*- coding: utf-8 -*-

from django.db import models

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType


class SeoManager(models.Manager):

    def for_model(self, instance):
        ct = ContentType.objects.get_for_model(instance.__class__)

        try:
            return self.filter(content_type=ct).get(object_id=instance.id)
        except ObjectDoesNotExist:
            return None

    def get_seo_object(self, instance):
        return self.for_model(instance)


class URLManager(models.Manager):

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
