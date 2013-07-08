==========
django-seo
==========

Seo fields for objects of any model registed in admin or for specified url.

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
    {% seo <title|keywords|description> [for <object>] %}

Or::
    {% seo <title|keywords|description> [for <object>] as <variable> %}
    {{ <variable> }}

Example:
========

``settings.py``::

    INSTALLED_APPS = (
        ...
        'app',
        ...
        'seo',
    )

    SEO_FOR_MODELS = [
        'app.models.Object',
        'app.models.Another',
    ]


``templates/object.html``::

    {% load seo_tags %}
    <html>
        <head>
            <meta name="description" content="{% seo description for object %}" />
            <meta name="keywords" content="{% seo keywords for object %}" />
            <title>{% seo title for object %}</title>
        </head>
        <body>
            {{ object.content }}
            <h1>{% seo title for object as seo_title %}{{ seo_title }}</h1>
        </body>
    </html>

If you are using extend
-----------------------

``templates/base.html``::

    <html>
        <head>
            <meta name="description" content="{% block description %}{% seo description %}{% endblock %}" />
            <meta name="keywords" content="{% block keywords %}{% seo keywords %}{% endblock %}" />
            <title>{% block title %}{% seo title %}{% endblock %}</title>
        </head>
        <body>
            {% block content %}{% endblock %}
        </body>
    </html>

``templates/object.html``::

    {% load seo_tags %}
    {% block description %}{% seo description for object %}{% endblock %}
    {% block keywords %}{% seo keywords for object %}{% endblock %}
    {% block title %}{% seo title for object %}{% endblock %}

    {% block content %}
        {{ object.content }}
    {% endblock %}

``templates/another.html``::

    {% load seo_tags %}
    {% block description %}{% seo description for another %}{% endblock %}
    {% block keywords %}{% seo keywords for another %}{% endblock %}
    {% block title %}{% seo title for another %}{% endblock %}

    {% block content %}
        {{ another.content }}
    {% endblock %}
