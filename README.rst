django-easy-seo
===============

SEO fields for objects of any model registered in admin.

Maintained by `Basil Shubin <https://github.com/bashu>`_,  and some great
`contributors <https://github.com/bashu/django-easy-seo/contributors>`_.

.. image:: https://img.shields.io/pypi/v/django-easy-seo.svg
   :target: https://pypi.python.org/pypi/django-easy-seo/

.. image:: https://img.shields.io/pypi/dm/django-easy-seo.svg
    :target: https://pypi.python.org/pypi/django-easy-seo/

.. image:: https://img.shields.io/github/license/bashu/django-easy-seo.svg
   :target: https://pypi.python.org/pypi/django-easy-seo/

.. raw:: html

   <p align="center">
     <img src="https://raw.githubusercontent.com/bashu/django-easy-seo/develop/logo/sizes%20500x300/color.png" alt="django-easy-seo">
   </p>

Setup
-----

Either clone this repository into your project, or install with ``pip install django-easy-seo``

You'll need to add ``seo`` as a **LAST** item to ``INSTALLED_APPS`` in your project's ``settings.py`` file :

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'seo',  # must be last in a list
    )

Then run ``./manage.py syncdb`` to create the required database tables

Configuration
-------------

There is only one mandatory configuration option you need to set in your ``settings.py`` :

.. code-block:: python

    # Override / extend ModelAdmin classes for a given Models
    SEO_FOR_MODELS = [
        '<app_name>.models.<ModelName>',
    ]

Usage
-----

First of all, load the ``seo_tags`` in every template where you want to use it :

.. code-block:: html+django

    {% load seo_tags %}

Use :

.. code-block:: html+django

    {% seo '<title|keywords|description>' for object %}
  
or :

.. code-block:: html+django

    {% seo '<title|keywords|description>' for object as variable %}
    {{ variable }}

Please see ``example`` application. This application is used to manually test the functionalities of this package. This also serves as a good example.

You need only Django 1.4 or above to run that. It might run on older versions but that is not tested.
