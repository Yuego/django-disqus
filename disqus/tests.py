# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf import settings
from django.core.management.base import CommandError

from disqus.api import DisqusClient

__test__ = {'API_TESTS': """

First, we test if the DisqusClient class can be initialized
and parameters that were passed are set correctly.

>>> c = DisqusClient(foo='bar', bar='foo')
>>> c.foo
u'bar'
>>> c.bar
u'foo'
>>> c.baz
Traceback (most recent call last):
    ...
AttributeError


When a DISQUS API method is called, the call method should be used.

>>> 'call_method' in repr(c.get_forum_list)
True
""",
}

