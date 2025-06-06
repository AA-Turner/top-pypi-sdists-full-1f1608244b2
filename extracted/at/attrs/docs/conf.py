# SPDX-License-Identifier: MIT

import os

from importlib import metadata
from pathlib import Path


# Set canonical URL from the Read the Docs Domain
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    html_context = {"READTHEDOCS": True}


# -- Path setup -----------------------------------------------------------

PROJECT_ROOT_DIR = Path(__file__).parents[1].resolve()


# -- General configuration ------------------------------------------------

doctest_global_setup = """
from attr import define, frozen, field, validators, Factory
"""

linkcheck_ignore = [
    # Fastly blocks this.
    "https://pypi.org/project/attr/#history",
    # We run into GitHub's rate limits.
    r"https://github.com/.*/(issues|pull)/\d+",
    # Rate limits and the latest tag is missing anyways on release.
    "https://github.com/python-attrs/attrs/tree/.*",
    # GitHub just completely broke anchors hashtag modern web dev.
    "https://github.com/python-attrs/attrs/commit/88aa1c897dfe2ee4aa987e4a56f2ba1344a17238#diff-4fc63db1f2fcb7c6e464ee9a77c3c74e90dd191d1c9ffc3bdd1234d3a6663dc0R48",
]

# In nitpick mode (-n), still ignore any of the following "broken" references
# to non-types.
nitpick_ignore = [
    ("py:class", "Any value"),
    ("py:class", "callable"),
    ("py:class", "callables"),
    ("py:class", "tuple of types"),
]

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "notfound.extension",
    "sphinxcontrib.towncrier",
]

myst_enable_extensions = [
    "colon_fence",
    "smartquotes",
    "deflist",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "attrs"
author = "Hynek Schlawack"
copyright = f"2015, {author}"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# The full version, including alpha/beta/rc tags.
release = metadata.version("attrs")
if "dev" in release:
    release = version = "UNRELEASED"
else:
    # The short X.Y version.
    version = release.rsplit(".", 1)[0]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build"]

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = "any"

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = "furo"
html_theme_options = {
    "sidebar_hide_name": True,
    "light_logo": "attrs_logo.svg",
    "dark_logo": "attrs_logo_white.svg",
    "top_of_page_buttons": [],
    "light_css_variables": {
        "font-stack": "Inter,sans-serif",
        "font-stack--monospace": "BerkeleyMono, MonoLisa, ui-monospace, "
        "SFMono-Regular, Menlo, Consolas, Liberation Mono, monospace",
    },
}
html_css_files = ["custom.css"]


# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# If false, no module index is generated.
html_domain_indices = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# Output file base name for HTML help builder.
htmlhelp_basename = "attrsdoc"

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [("index", "attrs", "attrs Documentation", ["Hynek Schlawack"], 1)]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "attrs",
        "attrs Documentation",
        "Hynek Schlawack",
        "attrs",
        "Python Classes Without Boilerplate",
        "Miscellaneous",
    )
]

epub_description = "Python Classes Without Boilerplate"

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

# Allow non-local URIs so we can have images in CHANGELOG etc.
suppress_warnings = ["image.nonlocal_uri"]


# -- Options for sphinxcontrib.towncrier extension ------------------------

towncrier_draft_autoversion_mode = "draft"
towncrier_draft_include_empty = True
towncrier_draft_working_directory = PROJECT_ROOT_DIR
towncrier_draft_config_path = "pyproject.toml"
