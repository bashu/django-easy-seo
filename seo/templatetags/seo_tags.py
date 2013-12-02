# -*- coding: utf-8 -*-

from django import template
from django.core.cache import cache
from django.utils.html import escape
from django.contrib.sites.models import get_current_site

from classytags.core import Tag, Options
from classytags.arguments import Argument, ChoiceArgument

from caching.invalidation import make_key

from ..settings import INTENTS, CACHE_PREFIX, CACHE_TIMEOUT
from ..models import Seo

register = template.Library()


class SeoTag(Tag):
    name = 'seo'
    options = Options(
        ChoiceArgument('intent', required=True, choices=INTENTS),
        'for',
        Argument('instance', required=True),
        'as',
        Argument('varname', resolve=False, required=False),
    )

    def render_tag(self, context, intent, instance, varname):
        site = get_current_site(context['request'])

        cache_key = '%s:%s' % (CACHE_PREFIX, make_key('%s.%s:%s' % (
            site.pk, instance.pk, intent)))
        value = cache.get(cache_key)
        if value is None:
            seobj = Seo.objects.get_seo_object(instance, site)
            value = getattr(seobj, self.intent, None)
            cache.set(cache_key, value, CACHE_TIMEOUT)  # store in a cache

        if varname:
            context[varname] = value
            return ''
        else:
            return escape(value or u'')

register.tag(SeoTag)
