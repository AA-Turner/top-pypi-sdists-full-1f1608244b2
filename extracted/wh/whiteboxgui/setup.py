#!/usr/bin/env python

"""The setup script."""

import io
from os import path as op
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

here = op.abspath(op.dirname(__file__))

# get the dependencies and installs
with io.open(op.join(here, "requirements.txt"), encoding="utf-8") as f:
    all_reqs = f.read().split("\n")

install_requires = [x.strip() for x in all_reqs if "git+" not in x]
dependency_links = [x.strip().replace("git+", "") for x in all_reqs if "git+" not in x]

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Qiusheng Wu",
    author_email='giswqs@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    description="An interactive GUI for whitebox-tools in a Jupyter-based environment",
    install_requires=install_requires,
    dependency_links=dependency_links,
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='whiteboxgui',
    name='whiteboxgui',
    packages=find_packages(include=['whiteboxgui', 'whiteboxgui.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/giswqs/whiteboxgui',
    version='2.3.0',
    zip_safe=False,
)
