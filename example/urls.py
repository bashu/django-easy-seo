# -*- coding: utf-8 -*-

from django.urls import path
from django.conf.urls import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
]
