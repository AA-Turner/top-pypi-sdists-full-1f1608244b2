# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import datetime
import os
import sys

# Adds path to the folder _ext, where extensions are stored
sys.path.insert(0, os.path.abspath("."))
sys.path.append(os.path.abspath("./_ext"))


# -- Project information -----------------------------------------------------

project = "pdbufr"
author = "ECMWF"

year = datetime.datetime.now().year
years = "2019-%s" % (year,)
copyright = "%s, European Centre for Medium-Range Weather Forecasts (ECMWF)" % (years,)


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    "nbsphinx",
    "sphinx_issues",
    "sphinx_copybutton",
    "xref",
]

# Path to GitHub repo {group}/{project}  (note that `group` is the GitHub user or organization)
issues_github_path = "ecmwf/pdbufr"

# sphinx_tab

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_logo = ""

highlight_language = "none"


xref_links = {
    "eccodes": (
        "ecCodes",
        "https://confluence.ecmwf.int/display/ECC/ecCodes+Home",
    ),
}


rst_prolog = """
.. role:: mval
"""

nbsphinx_prolog = """
{% set docname = env.doc2path(env.docname, base=None) %}

Try this notebook in |Binder|.

.. |Binder| image:: https://mybinder.org/badge.svg
   :target: https://mybinder.org/v2/gh/ecmwf/pdbufr/master?filepath=docs/{{ docname }}
   :alt: Binder
   :class: badge

"""
