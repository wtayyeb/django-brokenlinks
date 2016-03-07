Django Brokenlinks
==================

log brokenlinks to logfile and config fail2ban to ban crawlers hitting many 404 pages.
 
Requirements
------------

`django-appconf`

`Django <https://www.djangoproject.com/>`_ 1.3 or later

Installation
------------

::

    $ pip install django-brokenlinks


Setup
-----

Just add ``'brokenlinks'`` to INSTALLED_APPS and set the BROKENLINKS_LOG_PATH in
your settings.py::

    INSTALLED_APPS = (
        # ...
        'brokenlinks',
        # ...
    )

    BROKENLINKS_LOG_PATH = '/path/to/brokenlinks.log'

then config fail2ban to use it


Author
-----

* w.Tayyeb

