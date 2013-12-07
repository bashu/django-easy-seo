# -*- coding: utf-8 -*-

from django import template
from django.utils.html import escape

from classytags.core import Tag, Options
from classytags.arguments import Argument, ChoiceArgument

from ..settings import INTENTS
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
        seobj = Seo.objects.get_seo_object(instance)

        if varname:
            context[varname] = getattr(seobj, intent, None)
            return ''
        else:
            return escape(getattr(seobj, intent, None) or u'')

register.tag(SeoTag)
