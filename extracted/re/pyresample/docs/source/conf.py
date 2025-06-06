# -*- coding: utf-8 -*-
#
# pyresample documentation build configuration file, created by
# sphinx-quickstart on Tue Jan  5 13:01:32 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.
"""Sphinx documentation configuration."""
from __future__ import annotations

import os
import sys
from datetime import datetime

from pyresample import __version__  # noqa

# Add `source/` directory to make custom extensions/plugins importable
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# -- General configuration -----------------------------------------------

# sphinxcontrib.apidoc was added to sphinx in 8.2.0 as sphinx.etx.apidoc
needs_sphinx = "8.2.0"

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.doctest', 'sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.intersphinx',
    'sphinx.ext.apidoc', 'sphinx_reredirects', 'doi_role', "sphinx_autodoc_typehints",
]

# DocTest Settings
# don't run regular >>> code blocks
doctest_test_doctest_blocks = ''
# setup imports so we can skip certain doctests
doctest_global_setup = '''
try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

try:
    import cartopy
except ImportError:
    cartopy = None

try:
    from mpl_toolkits.basemap import Basemap
except ImportError:
    Basemap = None
'''

# API docs
apidoc_modules = [
    {
        "path": "../../pyresample",
        "destination": "api/",
        "exclude_patterns": [
            # Prefer to not document test modules. Most users will look at
            # source code if needed and we want to avoid documentation builds
            # suffering from import-time test data creation. We want to keep
            # things contributors might be interested in like satpy.tests.utils.
            "../../pyresample/test/test_*.py",
            "../../pyresample/test/**/test_*.py",
        ],
    },
]
apidoc_separate_modules = True
apidoc_include_private = True

autodoc_mock_imports = ["hashlib._Hash"]
autodoc_type_aliases = {
    "ArrayLike": "numpy.typing.ArrayLike",
    "DTypeLike": "numpy.typing.DTypeLike",
}
autodoc_default_options = {
    "special-members": "__init__, __reduce_ex__",
}
nitpick_ignore_regex: list[tuple[str, str]] = []
autoclass_content = "both"  # append class __init__ docstring to the class docstring



# Napoleon Settings (to support numpy style docs)
napoleon_numpy_docstring = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True

redirects = {
    "data_reduce": "howtos/data_reduce",
    "geo_def": "howtos/data_reduce",
    "geo_filter": "howtos/data_reduce",
    "geometry_utils": "howtos/data_reduce",
    "grid": "howtos/data_reduce",
    "multi": "howtos/data_reduce",
    "plot": "howtos/data_reduce",
    "plot_cartopy_basemap": "howtos/data_reduce",
    "plot_projections": "howtos/data_reduce",
    "preproc": "howtos/data_reduce",
    "spherical_geometry": "howtos/data_reduce",
    "swath": "howtos/data_reduce",
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'pyresample'
copyright = f"2013-{datetime.utcnow():%Y}, Pyresample developers"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

version = __version__.split('+')[0]
# The full version, including alpha/beta/rc tags.
release = __version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
# unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees: list[str] = []

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_use_modindex = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'pyresampledoc'


# -- Options for LaTeX output --------------------------------------------

# The paper size ('letter' or 'a4').
# latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
# latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'pyresample.tex', u'pyresample Documentation',
     u'Esben S. Nielsen', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# Additional stuff for the LaTeX preamble.
# latex_preamble = ''

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_use_modindex = True

# Intersphinx extention
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable', None),
    'scipy': ('https://docs.scipy.org/doc/scipy', None),
    'xarray': ('https://docs.xarray.dev/en/stable', None),
    'dask': ('https://docs.dask.org/en/latest', None),
    'pandas': ('https://pandas.pydata.org/docs', None),
    'trollsift': ('https://trollsift.readthedocs.io/en/stable', None),
    'trollimage': ('https://trollimage.readthedocs.io/en/stable', None),
    'pyproj': ('https://pyproj4.github.io/pyproj/dev/', None),
    'proj': ('https://proj.org/en/stable', None),
    'satpy': ('https://satpy.readthedocs.io/en/stable', None),
    'donfig': ('https://donfig.readthedocs.io/en/latest', None),
}
