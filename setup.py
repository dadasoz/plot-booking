#!/usr/bin/env python

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='landworld',
    # GETTING-STARTED: set your app version:
    version='1.0',
    # GETTING-STARTED: set your app description:
    description='landworld App',
    # GETTING-STARTED: set author name (your name):
    author='Your Name',
    # GETTING-STARTED: set author email (your email):
    author_email='info@landworld.com',
    # GETTING-STARTED: set author url (your url):
    url='http://www.python.org/sigs/distutils-sig/',
    # GETTING-STARTED: define required django version:
    install_requires=[
        'Django==1.8.4',
        'django-braces==1.9.0',
        'django-cors-headers==1.1.0',
        'django-filter==0.13.0',
        'django-oauth-toolkit==0.10.0',
        'djangorestframework==3.3.3',
        'djangorestframework-oauth==1.1.0',
        'Markdown==2.6.6',
        'MarkupSafe==0.23',
        'MySQL-python==1.2.5',
        'oauthlib==1.0.3',
        'path.py==8.2.1',
        'Pillow==3.3.0',
        'python-dateutil==2.5.3',
        'requests==2.2.1',
        'six==1.10.0',
        'wheel==0.24.0',
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
