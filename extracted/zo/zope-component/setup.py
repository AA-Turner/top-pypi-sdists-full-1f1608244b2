##############################################################################
#
# Copyright (c) 2004 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
# This package is developed by the Zope Toolkit project, documented here:
# http://docs.zope.org/zopetoolkit
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.component package
"""

import os

from setuptools import find_packages
from setuptools import setup


HOOK_REQUIRES = [
]

PERSISTENTREGISTRY_REQUIRES = [
    'persistent',
]

SECURITY_REQUIRES = [
    'zope.location',
    'zope.proxy',
    'zope.security',
]

ZCML_REQUIRES = [
    'zope.configuration',
    'zope.i18nmessageid',
]

MIN_TESTS_REQUIRE = (
    HOOK_REQUIRES
    + ZCML_REQUIRES
    + [
        'zope.testing',
        'zope.testrunner',
    ]
)

TESTS_REQUIRE = (
    MIN_TESTS_REQUIRE
    + PERSISTENTREGISTRY_REQUIRES
    + SECURITY_REQUIRES
)


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


setup(
    name='zope.component',
    version='6.0',
    url='https://github.com/zopefoundation/zope.component',
    project_urls={
        'Documentation': 'https://zopecomponent.readthedocs.io/',
        'Issue Tracker': ('https://github.com/zopefoundation/'
                          'zope.component/issues'),
        'Sources': 'https://github.com/zopefoundation/zope.component',
    },
    license='ZPL 2.1',
    description='Zope Component Architecture',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.dev',
    long_description=(
        read('README.rst')
        + '\n' +
        read('CHANGES.rst')
    ),
    keywords="interface component coupling loose utility adapter",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved",
        "License :: OSI Approved :: Zope Public License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Framework :: Zope :: 3",
        "Framework :: Zope :: 5",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    namespace_packages=['zope', ],
    python_requires='>=3.7',
    install_requires=[
        'setuptools',
        'zope.event',
        'zope.hookable >= 4.2.0',
        'zope.interface >= 5.3',
    ],
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'hook': HOOK_REQUIRES,  # BBB
        'persistentregistry': PERSISTENTREGISTRY_REQUIRES,
        'security': SECURITY_REQUIRES,
        'zcml': ZCML_REQUIRES,
        'mintests': MIN_TESTS_REQUIRE,
        'test': TESTS_REQUIRE,
        'docs': [
            'Sphinx',
            'repoze.sphinx.autointerface',
            'ZODB',
        ],
    },
)
