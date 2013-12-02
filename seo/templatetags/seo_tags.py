# -*- coding: utf-8 -*-

from django import template
from django.core.cache import cache
from django.utils.html import escape
from django.template import Variable
from django.template import TemplateSyntaxError
from django.core.exceptions import ImproperlyConfigured
from django.contrib.sites.models import get_current_site

from caching.invalidation import make_key

from ..settings import INTENTS, CACHE_PREFIX, CACHE_TIMEOUT
from ..models import Seo, Url

register = template.Library()


class SeoNode(template.Node):

    def __init__(self, intent, target_object=None, varname=None):
        self.intent = intent
        self.target_object = target_object
        self.varname = varname

    def get_target_object(self, context):
        if self.target_object:
            return Variable(self.target_object).resolve(context)
        return None

    def render(self, context):
        try:
            request = context['request']
        except KeyError:
            raise ImproperlyConfigured("""`request` was not found in context. Add "django.core.context_processors.request" to `TEMPLATE_CONTEXT_PROCESSORS` in your settings.py.""")

        site = get_current_site(request)
        target_object = self.get_target_object(context)
        if target_object is None:
            cache_key = '%s:%s' % (CACHE_PREFIX, make_key('%s.%s:%s' % (
                site.pk, request.path_info, self.intent)))
            value = cache.get(cache_key)
            if value is None:
                seobj = Url.objects.get_seo_object(request.path_info, site)
                value = getattr(seobj, self.intent, None)
                cache.set(cache_key, value, CACHE_TIMEOUT)  # store in a cache
        else:
            cache_key = '%s:%s' % (CACHE_PREFIX, make_key('%s.%s:%s' % (
                site.pk, target_object.pk, self.intent)))
            value = cache.get(cache_key)
            if value is None:
                seobj = Seo.objects.get_seo_object(target_object, site)
                value = getattr(seobj, self.intent, None)
                cache.set(cache_key, value, CACHE_TIMEOUT)  # store in a cache

        if self.varname is None:
            return escape(value or u'')
        else:
            context[self.varname] = value
            return u''


def seo_tag(parser, token):
    """Get seo data for object"""
    bits = token.split_contents()
    if bits[1] in INTENTS:
        if len(bits) in [4, 6] and bits[2] == 'for':
            if len(bits) == 4:
                return SeoNode(bits[1], target_object=bits[3])
            elif bits[4] == 'as':
                return SeoNode(bits[1], target_object=bits[3], varname=bits[5])
        elif len(bits) in [2, 4]:
            if len(bits) == 2:
                return SeoNode(bits[1])
            elif bits[2] == 'as':
                return SeoNode(bits[1], varname=bits[3])

    raise TemplateSyntaxError(
        """Invalid syntax. Use ``{% seo <title|keywords|description> [for <object>] [as <variable>] %}``""")

register.tag('seo', seo_tag)
