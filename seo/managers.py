# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType


class SeoManager(models.Manager):

    def for_object(self, instance):
        ct = ContentType.objects.get_for_model(instance.__class__)

        try:
            return self.filter(content_type=ct).get(object_id=instance.id)
        except ObjectDoesNotExist:
            return None
