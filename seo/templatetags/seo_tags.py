# -*- coding: utf-8 -*-

from django import template
from django.utils.html import escape
from django.db.models.base import Model

from classytags.core import Tag, Options
from classytags.arguments import Argument, ChoiceArgument

from ..models import Seo

register = template.Library()

INTENTS = ['title', 'keywords', 'description']


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
            seobj = Seo.objects.for_object(instance)
        else:  # have no idea what is that?
            raise NotImplementedError

        value = getattr(seobj, intent, None)

        if varname:
            context[varname] = value
            return ''
        else:
            return escape(value or '')

register.tag(SeoTag)
