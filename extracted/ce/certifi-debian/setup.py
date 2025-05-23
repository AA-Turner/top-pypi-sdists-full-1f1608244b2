#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import with_statement
import re
import os
import sys

# While I generally consider it an antipattern to try and support both
# setuptools and distutils with a single setup.py, in this specific instance
# where certifi is a dependency of setuptools, it can create a circular
# dependency when projects attempt to unbundle stuff from setuptools and pip.
# Though we don't really support that, it makes things easier if we do this and
# should hopefully cause less issues for end users.
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


version_regex = r'__version__ = ["\']([^"\']*)["\']'
with open('certifi/__init__.py', 'r') as f:
    text = f.read()
    match = re.search(version_regex, text)

    if match:
        VERSION = match.group(1)
    else:
        raise RuntimeError("No version number found!")

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel upload')
    sys.exit()

setup(
    name='certifi-debian',
    version=VERSION,
    description='Python package for providing Debian like CA Bundle path.',
    long_description=open('README.rst').read(),
    author='Nicolas Ledez',
    author_email='pypi.python.org@ledez.net',
    url='https://certifiio.readthedocs.io/en/latest/',
    packages=[
        'certifi-debian',
    ],
    package_dir={'certifi-debian': 'certifi'},
    include_package_data=True,
    zip_safe=False,
    license='MPL-2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    project_urls={
        'Documentation': 'https://certifiio.readthedocs.io/en/latest/',
        'Source': 'https://github.com/certifi/python-certifi',
    },
)
