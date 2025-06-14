#!/usr/bin/env python
import os
from setuptools import setup, find_packages

import tencentcloud

ROOT = os.path.dirname(__file__)

setup(
    name='tencentcloud-sdk-python-dataintegration',
    install_requires=["tencentcloud-sdk-python-common==3.0.1394"],
    version=tencentcloud.__version__,
    description='Tencent Cloud Dataintegration SDK for Python',
    long_description=open('README.rst').read(),
    author='Tencent Cloud',
    url='https://github.com/TencentCloud/tencentcloud-sdk-python',
    maintainer_email="tencentcloudapi@tencent.com",
    scripts=[],
    packages=find_packages(exclude=["tests*"]),
    license="Apache License 2.0",
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
