# -*- coding:utf-8 -*-
'''
Created on Nov 23, 2015

@author: Wasim
'''

import logging

from django.conf import settings
from django.core.mail import mail_managers
from django.middleware.common import BrokenLinkEmailsMiddleware as djBrokenLinkEmailsMiddleware
from django.utils.encoding import force_text


logger = logging.getLogger(__name__)


class BrokenLinkEmailsMiddleware(djBrokenLinkEmailsMiddleware):
    def process_response(self, request, response):
        """
        Send broken link emails for relevant 404 NOT FOUND responses.
        """
        if response.status_code == 404:
            domain = request.get_host()
            path = request.get_full_path()
            referrer = force_text(request.META.get('HTTP_REFERER', ''), errors='replace')

            if not self.is_ignorable_request(request, path, domain, referrer):
                useragent = request.META.get('HTTP_USER_AGENT', '<none>')
                ip = self.get_client_ip(request)

                logger.error(
                    "Broken Link RemoteIP=%s Path=%s Referer=%s",
                    request.META.get('REMOTE_ADDR'),
                    path,
                    referrer,
                )

                if not settings.DEBUG:
                    mail_managers(
                        "Broken %slink on %s" % (
                            ('INTERNAL ' if self.is_internal_request(domain, referrer) else ''),
                            domain
                        ),
                        "Referrer: %(referrer)s\n"
                        "Requested URL: %(path)s\n"
                        "User agent: %(useragent)s\n"
                        "IP address: %(ip)s\n"
                        "Whois : http://whois.domaintools.com/%(ip)s" % dict(
                            referrer=referrer, path=path, useragent=useragent, ip=ip
                        ),
                        fail_silently=True)


        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
