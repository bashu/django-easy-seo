Django SEO
===

Seo fields for objects of any model registed in admin.

[![Latest Version](https://pypip.in/version/django-easy-seo/badge.svg)](https://pypi.python.org/pypi/django-easy-seo/)
[![Downloads](https://pypip.in/download/django-easy-seo/badge.svg)](https://pypi.python.org/pypi/django-easy-seo/)
[![License](https://pypip.in/license/django-easy-seo/badge.svg)](https://pypi.python.org/pypi/django-easy-seo/)

## Setup

Either clone this repository into your project, or install with ```pip install django-easy-seo```

You'll need to add ```seo``` to ```INSTALLED_APPS``` in your projects ``settings.py`` file :

```python
INSTALLED_APPS = (
    ...
    'seo',
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
