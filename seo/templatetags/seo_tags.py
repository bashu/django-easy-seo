# -*- coding: utf-8 -*-

from django import template
from django.core.cache import cache
from django.utils.html import escape
from django.db.models.base import Model
from django.contrib.sites.models import get_current_site

from classytags.core import Tag, Options
from classytags.arguments import Argument, ChoiceArgument

from ..settings import INTENTS, CACHE_PREFIX, CACHE_TIMEOUT
from ..models import Seo, URL, make_key

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
        if isinstance(instance, Model):  # hey we got a model instance
            cache_key = '%s:%s' % (CACHE_PREFIX, make_key(
                instance, instance.pk, intent))

            value = cache.get(cache_key)
            if not value:
                seobj = Seo.objects.get_seo_object(instance)
                value = getattr(seobj, intent, None)
                cache.set(cache_key, value, CACHE_TIMEOUT)  # store in a cache

        elif isinstance(instance, basestring):  # and here we have a path
            request, path = context['request'], instance
            current_site = get_current_site(request)
            cache_key = '%s:%s%s:%s' % (
                CACHE_PREFIX, current_site.domain, path, intent)

            value = cache.get(cache_key)
            if not value:
                seobj = URL.objects.get_seo_object(path, current_site)
                value = getattr(seobj, intent, None)
                cache.set(cache_key, value, CACHE_TIMEOUT)  # store in a cache

        else:
            raise NotImplementedError

        if varname:
            context[varname] = value
            return ''
        else:
            return escape(value or u'')

register.tag(SeoTag)
