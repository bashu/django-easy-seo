Django SEO
===

SEO fields for objects of any model registered in admin.

[![Latest Version](https://img.shields.io/pypi/v/django-easy-seo.svg)](https://pypi.python.org/pypi/django-easy-seo/)
[![Downloads](https://img.shields.io/pypi/dm/django-easy-seo.svg)](https://pypi.python.org/pypi/django-easy-seo/)
[![License](https://img.shields.io/github/license/bashu/django-easy-seo.svg)](https://pypi.python.org/pypi/django-easy-seo/)

## Setup

Either clone this repository into your project, or install with ```pip install django-easy-seo```

You'll need to add ```seo``` as a **LAST** item to ```INSTALLED_APPS``` in your project's ``settings.py`` file :

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
```html+django
{% load seo_tags %}
```
Use :
```html+django
{% seo '<title|keywords|description>' for <object> %}
```    
or :
```html+django
{% seo '<title|keywords|description>' for <object> as <variable> %}
{{ variable }}
```
Please see ``example`` application. This application is used to manually test the functionalities of this package. This also serves as a good example.

You need only Django 1.4 or above to run that. It might run on older versions but that is not tested.
