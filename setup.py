#!/usr/bin/env python

import os
import re
import sys
import codecs

from setuptools import setup, find_packages


# When creating the sdist, make sure the django.mo file also exists:
if 'sdist' in sys.argv or 'develop' in sys.argv:
    os.chdir('seo')
    try:
        from django.core import management
        management.call_command('compilemessages', stdout=sys.stderr, verbosity=1)
    except ImportError:
        if 'sdist' in sys.argv:
            raise
    finally:
        os.chdir('..')


def read(*parts):
    file_path = os.path.join(os.path.dirname(__file__), *parts)
    return codecs.open(file_path, encoding='utf-8').read()


def find_version(*parts):
    version_file = read(*parts)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return str(version_match.group(1))
    raise RuntimeError("Unable to find version string.")


setup(
    name="django-easy-seo",
    version=find_version('seo', '__init__.py'),
    license="GPLv3 License",

    install_requires=[
        'django-classy-tags',
    ],
    requires=[
        'Django (>=1.4)',
    ],

    description="Adds generic SEO fields for objects in your site",
    long_description=read('README.rst'),
    
    author="Alexander Ivanov",
    author_email="alexander.ivanov@redsolution.ru",

    maintainer='Basil Shubin',
    maintainer_email='basil.shubin@gmail.com',

    url='https://github.com/bashu/django-easy-seo',
    download_url='https://github.com/bashu/django-easy-seo/zipball/master',
    
    packages=find_packages(exclude=('example*',)),
    include_package_data=True,

    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Software Development :: Libraries :: Python Modules',        
    ],
)
