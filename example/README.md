# Example

To run the example application, make sure you have the required
packages installed.  You can do this using :

```shell
mkvirtualenv example
pip install -r example/requirements.txt
```

This assumes you already have ``virtualenv`` and ``virtualenvwrapper``
installed and configured.

Next, you can setup the Django instance using :

```shell
python example/manage.py syncdb --noinput
python example/manage.py createsuperuser --username=admin --email=admin@example.com
```

And run it off course :
```shell
python example/manage.py runserver
```

Good luck!
