Django Brokenlinks
==================

log brokenlinks to logfile and config fail2ban to ban crawlers hitting many 404 pages.
 
Requirements
------------

`django-appconf`


Installation
------------

::

    $ pip install django-brokenlinks


Setup
-----

1. Add ``'brokenlinks'`` to INSTALLED_APPS
2. Add ``'brokenlinks.middleware.BrokenLinkEmailsMiddleware'`` to ``MIDDLEWARE_CLASSES``
3. Set the ``BROKENLINKS_LOG_PATH``
4. After change in brokenlinks configs run ``manage.py createbrokenlinksconfs`` once and use the result conf-files with fail2ban 
 
your settings.py will look like below:


    INSTALLED_APPS = (
        # ...
        'brokenlinks',
        # ...
    )

    MIDDLEWARE_CLASSES= (
        'brokenlinks.middleware.BrokenLinkEmailsMiddleware',
        # ...
    )
    
    BROKENLINKS_LOG_PATH = '/path/to/brokenlinks.log'


then config fail2ban to use it


Author
-----

* w.Tayyeb

