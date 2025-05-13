# -*- coding: utf-8 -*-

#! /usr/bin/env python
from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import ez_setup
import hashlib
import time, random
import re
try:
    from urllib2 import quote
    from urllib2 import urlopen
    from urllib2 import HTTPError
except ImportError:
    from urllib.parse import quote
    from urllib.request import urlopen
    from urllib.error import HTTPError

try:
    from setuptools import setup, find_packages
except ImportError:
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

PYTHON_DEPENDENCIES = [
    ["numpy", "Numpy is required for the ArrayTable and ClusterTree classes.", 0],
    ["PyQt", "PyQt4/5 is required for tree visualization and image rendering.", 0],
    ["lxml", "lxml is required from Nexml and Phyloxml support.", 0]
]

CLASSIFIERS= [
    "Development Status :: 6 - Mature",
    "Environment :: Console",
    "Environment :: X11 Applications :: Qt",
    "Intended Audience :: Developers",
    "Intended Audience :: Other Audience",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Natural Language :: English",
    "Operating System :: MacOS",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python",
    "Topic :: Scientific/Engineering :: Bio-Informatics",
    "Topic :: Scientific/Engineering :: Visualization",
    "Topic :: Software Development :: Libraries :: Python Modules",
    ]


HERE = os.path.abspath(os.path.split(os.path.realpath(__file__))[0])

try:
    ETE_VERSION = open(os.path.join(HERE, "VERSION")).readline().strip()
except IOError:
    ETE_VERSION = 'unknown'

MOD_NAME = "ete3"

LONG_DESCRIPTION="""
The Environment for Tree Exploration (ETE) is a Python programming
toolkit that assists in the recontruction, manipulation, analysis and
visualization of phylogenetic trees (although clustering trees or any
other tree-like data structure are also supported).

ETE is currently developed as a tool for researchers working in
phylogenetics and genomics. If you use ETE for a published work,
please cite:

::

   Jaime Huerta-Cepas, François Serra and Peer Bork. "ETE 3: Reconstruction,
   analysis and visualization of phylogenomic data."  Mol Biol Evol (2016) doi:
   10.1093/molbev/msw046

Visit http://etetoolkit.org for more info.
"""


_s = setup(
        include_package_data = True,

        name = MOD_NAME,
        version = ETE_VERSION,
        packages = ["ete3"],

        entry_points = {"console_scripts":
                        ["ete3 = %s.tools.ete:main" %MOD_NAME]},
        requires = ["six"],

        # Project uses reStructuredText, so ensure that the docutils get
        # installed or upgraded on the target machine
        install_requires = [
            ],
        package_data = {

        },
        data_files = [("%s/tools" %MOD_NAME, ["%s/tools/ete_build.cfg" %MOD_NAME])],

        # metadata for upload to PyPI
        author = "Jaime Huerta-Cepas",
        author_email = "jhcepas@gmail.com",
        maintainer = "Jaime Huerta-Cepas",
        maintainer_email = "huerta@embl.de",
        platforms = "OS Independent",
        license = "GPLv3",
        description = "A Python Environment for (phylogenetic) Tree Exploration",
        long_description = LONG_DESCRIPTION,
        classifiers = CLASSIFIERS,
        provides = [MOD_NAME],
        keywords = "tree, tree reconstruction, tree visualization, tree comparison, phylogeny, phylogenetics, phylogenomics",
        url = "http://etetoolkit.org",
        project_urls = {
            "Documentation": "http://etetoolkit.org/docs/latest/tutorial/index.html",
            "Source": "https://github.com/etetoolkit/ete",
        },
        download_url = "http://etetoolkit.org/static/releases/ete3/",

)
