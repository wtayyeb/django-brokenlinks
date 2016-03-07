# -*- coding:utf-8 -*-
'''
Created on Nov 23, 2015

@author: Wasim
'''
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from brokenlinks import create_jail, create_filter


class Command(BaseCommand):
    def add_arguments(self, parser):
        # parser.add_argument('', dest='path', help="GG")
        parser.add_argument('-d', '--dir', metavar='dir', type=str, action='store', required=True,
                            help='path to store fail2ban conf files')


    def handle(self, *args, **options):
        dir_ = os.path.abspath(options['dir'])
        filter_filename = os.path.join(dir_, settings.BROKENLINKS_FILTER_NAME + '.conf')
        jail_filename = os.path.join(dir_, settings.BROKENLINKS_JAIL_NAME + '.conf')
        create_filter(filter_filename)
        create_jail(jail_filename)
        print 'following files created. copy or link them into /etc/fail2ban/ to make them work'
        print 'filter file : %s\n jail file : %s' % (filter_filename, jail_filename)
