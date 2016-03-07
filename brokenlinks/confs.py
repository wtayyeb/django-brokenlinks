# -*- coding:utf-8 -*-
'''
Created on Nov 23, 2015

@author: Wasim
'''

import os

from appconf import AppConf
from django.conf import settings


class AppConf(AppConf):
    LOG_PATH = os.path.join('var', 'log', 'brokenlinks.log')
    JAIL_NAME = 'brokenlinks-jail'
    FILTER_NAME = 'brokenlinks-filter'
    ACTION = 'iptables-allports'
    PATH_TO_CREATE = os.path.dirname(__file__)


    class Meta:
        prefix = 'BROKENLINKS'


# just to be sure that BROKENLINKS_LOG_PATH exist we need to devide the appconf
# into two classes!

class AppConfLogging(AppConf):
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,

        'formatters': {
            'simple': {
                'class': 'logging.Formatter',
                'format': '%(created)s|%(levelname)s|%(message)s',
            }
        },

        'filters': {
            'debug_false': {
                '()': 'django.utils.log.RequireDebugFalse',
            },
        },

        'handlers': {
            'brokenlinks_handler': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
            #    'filters': ['debug_false', ],
                'filename': settings.BROKENLINKS_LOG_PATH,
                'maxBytes': 5 * 1024 * 1024,
                'formatter': 'simple',
                'backupCount': 5,
            },
        },

        'loggers': {
            'brokenlinks': {
                'level': 'INFO',
                'handlers': ['brokenlinks_handler', ],
                'propagate': False,
            },
        }
    }

    class Meta:
        prefix = 'BROKENLINKS'

