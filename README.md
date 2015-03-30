Django SEO
===

Seo fields for objects of any model registed in admin.

[![Latest Version](https://pypip.in/version/django-easy-seo/badge.svg)](https://pypi.python.org/pypi/django-easy-seo/)
[![Downloads](https://pypip.in/download/django-easy-seo/badge.svg)](https://pypi.python.org/pypi/django-easy-seo/)
[![License](https://pypip.in/license/django-easy-seo/badge.svg)](https://pypi.python.org/pypi/django-easy-seo/)

## Setup

Either clone this repository into your project, or install with ```pip install django-easy-seo```

You'll need to add ```seo``` as a **LAST** item to ```INSTALLED_APPS``` in your projects ``settings.py`` file :

```python
INSTALLED_APPS = (
    ...
    'seo',  # must be last in a list
)
```

Then run ```./manage.py syncdb``` to create the required database tables

## Configuration

There is only one mandatory configuration option you need to set in your ``settings.py`` :
```python
# Override / extend ModelAdmin classes for a given Models
SEO_FOR_MODELS = [
    '<app_name>.models.<ModelName>',
]
```

## Usage

First of all, load the `seo_tags` in every template where you want to use it :

    {% load seo_tags %}

Use :

    {% seo '<title|keywords|description>' for <object> %}
    
or :

    {% seo '<title|keywords|description>' for <object> as <variable> %}
    {{ <variable> }}

### Examples

Please see `example` application. This application is used to manually test the functionalities of this package. This also serves as a good example. Below is a short summary of what was done:

In ``settings.py`` :
```python
INSTALLED_APPS = (
    ...
    'django.contrib.flatpages',
    ...
    'seo',  # last in a list
)

SEO_FOR_MODELS = [
    'django.contrib.flatpages.models.FlatPage',
]
```

In ``templates/flatpages/default.html`` :
```html
{% load seo_tags %}
<html>
    <head>
        <meta name="description" content="{% seo 'description' for flatpage %}" />
        <meta name="keywords" content="{% seo 'keywords' for flatpage %}" />
        <title>{% seo 'title' for flatpage %}</title>
    </head>
    <body>
        {% seo 'title' for flatpage as title %}
        <h1>{{ title }}</h1>
        {{ flatpage.content }}
    </body>
</html>
```
