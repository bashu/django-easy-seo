import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-easy-seo",
    version='0.4.6',
    packages=find_packages(exclude=['example']),
    include_package_data=True,
    license="GPLv3 License",
    description = "Adds generic SEO fields for objects in your site",
    long_description=README,
    author='Basil Shubin',
    author_email='basil.shubin@gmail.com',
    install_requires=[
        'django-classy-tags',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
    ],
    zip_safe=False,
)
