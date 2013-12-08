# -*- coding: utf-8 -*-

from django.conf import settings

INTENTS = ['title', 'keywords', 'description']

CACHE_PREFIX = getattr(settings, 'SEO_CACHE_PREFIX', 'SEO')
CACHE_TIMEOUT = getattr(settings, 'SEO_CACHE_TIMEOUT', 3600)
