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
            referer = force_text(request.META.get('HTTP_REFERER', ''), errors='replace')

            if not self.is_ignorable_request(request, path, domain, referer):
                ua = request.META.get('HTTP_USER_AGENT', '<none>')
                ip = request.META.get('REMOTE_ADDR', '<none>')

                logger.error(
                    "Broken Link RemoteIP=%s Path=%s Referer=%s",
                    request.META.get('REMOTE_ADDR'),
                    path,
                    referer,
                )

                if not settings.DEBUG:
                    mail_managers(
                        "Broken %slink on %s" % (
                            ('INTERNAL ' if self.is_internal_request(domain, referer) else ''),
                            domain
                        ),
                        "Referrer: %s\nRequested URL: %s\nUser agent: %s\n"
                        "IP address: %s\n"
                        "Whois : http://whois.domaintools.com/%s" % (referer, path, ua, ip, ip),
                        fail_silently=True)


        return response

