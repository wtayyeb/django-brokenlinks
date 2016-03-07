# -*- coding:utf-8 -*-
'''
Created on Nov 23, 2015

@author: Wasim
'''

from logging.config import dictConfig
import os

from django.conf import settings

from .confs import AppConf, AppConfLogging


def _setup():
    dictConfig(settings.BROKENLINKS_LOGGING)


def create_filter(filename=None):
    content = '\n'.join((
        '# auto-generated fail2ban-filter by brokenlinks.py',
        '[Definition]',
        'failregex = Broken Link RemoteIP=<HOST> .*',
        'ignoreregex =',
        ''
    ))
    if filename:
        with open(filename, 'w')as f:
            f.write(content)
    return content



def create_jail(filename=None):
    content = '\n'.join((
        '# auto-generated fail2ban-jail by brokenlinks.py',
        '[%s]' % settings.BROKENLINKS_JAIL_NAME,
        'enabled = true',
        'logpath = %s' % settings.BROKENLINKS_LOG_PATH,
        'filter = %s' % settings.BROKENLINKS_FILTER_NAME,
        'action = %s' % settings.BROKENLINKS_ACTION,
        ''
    ))
    if filename:
        with open(filename, 'w')as f:
            f.write(content)
    return content



_setup()

