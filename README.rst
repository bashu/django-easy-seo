==========
django-seo
==========

SEO fields for objects of any model registered in admin.

Installation:
=============

1. Put ``seo`` as LAST item to your ``INSTALLED_APPS`` in your ``settings.py`` within your django project.

2. Sync your database::

    ./manage.py syncdb

Usage:
======

In settings.py:
---------------

Add names of ModelAdmins to be override::

    SEO_FOR_MODELS = [
        '<app>.models.<Model>',
    ]

In template:
------------

First of all, load the seo_tags in every template you want to use it::

    {% load seo_tags %}

Use::
    {% seo <title|keywords|description> for <object> %}

Or::
    {% seo <title|keywords|description> for <object> as <variable> %}
    {{ <variable> }}
