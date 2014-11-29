import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-easy-seo",
    version='0.4.6',
    packages=['seo'],
    include_package_data=True,
    license="GPLv3 License",
    description = "Adds generic SEO fields for objects in your site or specific urls",
    long_description=README,
    author='Basil Shubin',
    author_email='basil.shubin@gmail.com',
    install_requires=[
        'django-classy-tags',
        'django-cache-machine>=0.8',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
    ],
    zip_safe=False,
)
