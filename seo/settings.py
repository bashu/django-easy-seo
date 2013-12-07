# -*- coding: utf-8 -*-

from django.conf import settings

INTENTS = ['title', 'keywords', 'description']
CACHE_TIMEOUT = getattr(settings, 'SEO_CACHE_TIMEOUT', 3600)
