# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

try:
    from urllib import parse, request
except:
    import urllib as parse
    import urllib2 as request

from django.core.management.base import CommandError
try:
    import json
except ImportError:
    from django.utils import simplejson as json


def call(method, data, post=False):
    """
    Calls `method` from the DISQUS API with data either in POST or GET.
    Returns deserialized JSON response.
    """
    url = "%s%s" % ('http://disqus.com/api/', method)
    if post:
        # POST request
        url += "/"
        data = parse.urlencode(data)
    else:
        # GET request
        url += "?%s" % parse.urlencode(data)
        data = ''
    res = json.load(request.urlopen(url, data))
    if not res['succeeded']:
        raise CommandError("'%s' failed: %s\nData: %s" % (method, res['code'], data))
    return res['message']
