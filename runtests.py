#!/usr/bin/env python
import logging
import sys
from os.path import dirname, abspath

from django.conf import settings

if not settings.configured:
    settings.configure(
        DATABASE_ENGINE='sqlite3',
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.admin',
            'django.contrib.sessions',
            'django.contrib.contenttypes',
            'disqus',
        ],
        ROOT_URLCONF='',
        DEBUG=False,
    )

try:
    from django.test.simple import DjangoTestSuiteRunner as TestRunner
except ImportError:
    from django.test.simple import run_tests

    class TestRunner(object):
        def __init__(self, **kwargs):
            self.kwargs = kwargs

        def run_tests(self, apps):
            return run_tests(apps, **self.kwargs)


def runtests(*test_args):
    if not test_args:
        test_args = ['disqus']
    parent = dirname(abspath(__file__))
    sys.path.insert(0, parent)
    tr = TestRunner(verbosity=1, interactive=True)
    failures = tr.run_tests(test_args)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
