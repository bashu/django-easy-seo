# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django.contrib.contenttypes import generic
from django.core.exceptions import ImproperlyConfigured

from .importpath import importpath
from .forms import SeoForm
from .models import Seo


class SeoAdmin(admin.ModelAdmin):
    model = Seo

    def queryset(self, request):
        return super(SeoAdmin, self).queryset(request).no_cache()

try:
    admin.site.register(Seo, SeoAdmin)
except admin.sites.AlreadyRegistered:
    pass


class SeoInlines(generic.GenericStackedInline):
    model = Seo
    form = SeoForm
    extra = 1
    max_num = 1

    def queryset(self, request):
        return super(SeoInlines, self).queryset(request).no_cache()

for model_name in getattr(settings, 'SEO_FOR_MODELS', []):
    model = importpath(model_name, 'SEO_FOR_MODELS')
    try:
        model_admin = admin.site._registry[model].__class__
    except KeyError:
        raise ImproperlyConfigured(
            "Please put ``seo`` in your settings.py only as last INSTALLED_APPS")
    admin.site.unregister(model)

    setattr(model_admin, 'inlines', getattr(model_admin, 'inlines', []))
    if not SeoInlines in model_admin.inlines:
        model_admin.inlines = list(model_admin.inlines)[:] + [SeoInlines]

    admin.site.register(model, model_admin)
