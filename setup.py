#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-disqus',
    version='0.4.1',
    description='Export comments and integrate DISQUS into your Django website',
    author='Arthur Koziel',
    author_email='arthur@arthurkoziel.com',
    url='http://arthurk.github.com/django-disqus/',
    license='New BSD License',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ],
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'django',
        'six',
    ],
    zip_safe=False,
)
