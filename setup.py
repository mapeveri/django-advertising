#!/usr/bin/env python
import os
import sys
from setuptools import setup

sys.path.insert(0, 'advertising')
from version import get_version
sys.path.remove('advertising')

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='django-advertising',
    version=get_version(),
    packages=[
        'advertising', 'advertising.templatetags',
        'advertising.static',
    ],
    include_package_data=True,
    license='BSD License',
    zip_safe=False,
    description='Django application for show advertising configurable.',
    long_description=README,
    url='https://github.com/mapeveri/django-advertising',
    author='Peveri Martin',
    author_email='martinpeveri@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
