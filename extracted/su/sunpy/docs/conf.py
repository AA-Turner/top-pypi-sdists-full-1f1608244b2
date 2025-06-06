"""
Configuration file for the Sphinx documentation builder.
"""
# -- stdlib imports ------------------------------------------------------------

import os
import sys
import datetime
import warnings

from packaging.version import Version

# -- Read the Docs Specific Configuration --------------------------------------

# This needs to be done before sunpy is imported
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    os.environ['SUNPY_CONFIGDIR'] = '/home/docs/'
    os.environ['HOME'] = '/home/docs/'
    os.environ['LANG'] = 'C'
    os.environ['LC_ALL'] = 'C'
    os.environ['PARFIVE_HIDE_PROGRESS'] = 'True'

# -- Check for dependencies ----------------------------------------------------

from sunpy.util import missing_dependencies_by_extra

missing_requirements = missing_dependencies_by_extra("sunpy")["docs"]
if missing_requirements:
    print(
        f"The {' '.join(missing_requirements.keys())} package(s) could not be found and "
        "is needed to build the documentation, please install the 'docs' requirements."
    )
    sys.exit(1)

from matplotlib import MatplotlibDeprecationWarning
from ruamel.yaml import YAML
from sphinx_gallery.sorting import ExplicitOrder
from sunpy_sphinx_theme import PNG_ICON

from astropy.utils.exceptions import AstropyDeprecationWarning
from astropy.io.fits.verify import VerifyWarning
import sunpy
from sunpy.util.exceptions import SunpyDeprecationWarning, SunpyPendingDeprecationWarning

# -- Project information -------------------------------------------------------

# The full version, including alpha/beta/rc tags
from sunpy import __version__

_version = Version(__version__)
version = release = str(_version)
# Avoid "post" appearing in version string in rendered docs
if _version.is_postrelease:
    version = release = _version.base_version
# Avoid long githashes in rendered Sphinx docs
elif _version.is_devrelease:
    version = release = f"{_version.base_version}.dev{_version.dev}"
is_development = _version.is_devrelease
is_release = not(_version.is_prerelease or _version.is_devrelease)

project = "sunpy"
author = "The SunPy Community"
copyright = f'{datetime.datetime.now().year}, {author}'

# Register remote data option with doctest
import doctest

REMOTE_DATA = doctest.register_optionflag('REMOTE_DATA')

# We want to make sure all the following warnings fail the build on CI but not
# when actually building docs on RTD.
if not on_rtd:
    warnings.filterwarnings("error", category=SunpyDeprecationWarning)
    warnings.filterwarnings("error", category=SunpyPendingDeprecationWarning)
    warnings.filterwarnings("error", category=MatplotlibDeprecationWarning)
    warnings.filterwarnings("error", category=AstropyDeprecationWarning)
# Raised all by the sample data now and astropy 7,
# so we want to prevent this failing any of the builds
warnings.filterwarnings("ignore", category=VerifyWarning)

# -- SunPy Sample Data and Config ----------------------------------------------

# We set the logger to debug so that we can see any sample data download errors
# in the CI, especially RTD.
ori_level = sunpy.log.level
sunpy.log.setLevel("DEBUG")

import sunpy.data.sample

sunpy.data.sample.download_all()
sunpy.log.setLevel(ori_level)

# For the linkcheck
linkcheck_ignore = [
    r"https://doi.org/\d+",
    r"https://\w\.element\.io/",
    # Checking all the PR URLs in the changelog takes a very long time
    r"https://github.com/sunpy/sunpy/pull/\d+",
    r"https://docs\.sunpy\.org",
    r"https://inis.iaea.org/collection/NCLCollectionStore/_Public/20/062/20062491.pdf",
    r"https://xrt.cfa.harvard.edu/",
]
linkcheck_anchors = False

# -- General configuration ---------------------------------------------------

# Wrap large function/method signatures
maximum_signature_line_length = 80
# sphinxext-opengraph
ogp_image = "https://raw.githubusercontent.com/sunpy/sunpy-logo/master/generated/sunpy_logo_word.png"
ogp_use_first_image = True
ogp_description_length = 160
ogp_custom_meta_tags = [
    '<meta property="og:ignore_canonical" content="true" />',
]

# Suppress warnings about overriding directives as we overload some of the
# doctest extensions.
suppress_warnings = ['app.add_directive', ]

# Wrap large function/method signatures
maximum_signature_line_length = 80

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
    'matplotlib.sphinxext.plot_directive',
    'sphinx_automodapi.automodapi',
    'sphinx_automodapi.smart_resolver',
    'sphinx_changelog',
    'sphinx_gallery.gen_gallery',
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sunpy.util.sphinx.doctest',
    'sunpy.util.sphinx.generate',
    "sphinxext.opengraph",
    'sphinx_design',
    'sphinx_copybutton',
    'hoverxref.extension',
]

# Set automodapi to generate files inside the generated directory
automodapi_toctreedirnm = "generated/api"

# Add any paths that contain templates here, relative to this directory.
# templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
html_extra_path = ['robots.txt']

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

if is_release:
    exclude_patterns.append('dev_guide/contents/*')

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ".rst"

# The master toctree document.
master_doc = 'index'

# The reST default role (used for this markup: `text`) to use for all
# documents. Set to the "smart" one.
default_role = 'obj'

# Disable having a separate return type row
napoleon_use_rtype = False

# Disable google style docstrings
napoleon_google_docstring = False

# Disable the use of param, which prevents a distinct "Other Parameters" section
napoleon_use_param = False

# Enable nitpicky mode, which forces links to be non-broken
nitpicky = True
# This is not used. See docs/nitpick-exceptions file for the actual listing.
nitpick_ignore = []
for line in open('nitpick-exceptions'):
    if line.strip() == "" or line.startswith("#"):
        continue
    dtype, target = line.split(None, 1)
    target = target.strip()
    nitpick_ignore.append((dtype, target))


# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "python": (
        "https://docs.python.org/3/",
        (None, "http://www.astropy.org/astropy-data/intersphinx/python3.inv"),
    ),
    "numpy": (
        "https://numpy.org/doc/stable/",
        (None, "http://www.astropy.org/astropy-data/intersphinx/numpy.inv"),
    ),
    "scipy": (
        "https://docs.scipy.org/doc/scipy/reference/",
        (None, "http://www.astropy.org/astropy-data/intersphinx/scipy.inv"),
    ),
    "aiapy": ("https://aiapy.readthedocs.io/en/stable/", None),
    "asdf": ("https://asdf.readthedocs.io/en/stable/", None),
    "astropy": ("https://docs.astropy.org/en/stable/", None),
    "dask": ("https://docs.dask.org/en/stable/", None),
    "drms": ("https://docs.sunpy.org/projects/drms/en/stable/", None),
    "hvpy": ("https://hvpy.readthedocs.io/en/latest/", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "mpl_animators": ("https://docs.sunpy.org/projects/mpl-animators/en/stable/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "parfive": ("https://parfive.readthedocs.io/en/stable/", None),
    "reproject": ("https://reproject.readthedocs.io/en/stable/", None),
    "skimage": ("https://scikit-image.org/docs/stable/", None),
    "spiceypy": ("https://spiceypy.readthedocs.io/en/stable/", None),
    "sunkit_image": ("https://docs.sunpy.org/projects/sunkit-image/en/stable/", None),
    "sunkit_instruments": ("https://docs.sunpy.org/projects/sunkit-instruments/en/stable/", None),
    "zeep": ("https://docs.python-zeep.org/en/stable/", None),
    "contourpy": ("https://contourpy.readthedocs.io/en/stable/", None),
}

# -- Options for hoverxref -----------------------------------------------------

if os.environ.get("READTHEDOCS"):
    hoverxref_api_host = "https://readthedocs.org"

    if os.environ.get("PROXIED_API_ENDPOINT"):
        # Use the proxied API endpoint
        # A RTD thing to avoid a CSRF block when docs are using a custom domain
        hoverxref_api_host = "/_"

hoverxref_auto_ref = False
hoverxref_domains = ["py"]
hoverxref_mathjax = True
hoverxref_modal_hover_delay = 500
hoverxref_tooltip_maxwidth = 600  # RTD main window is 696px
hoverxref_intersphinx = list(intersphinx_mapping.keys())
hoverxref_role_types = {
    # Roles within the py domain
    "attr": "tooltip",
    "class": "tooltip",
    "const": "tooltip",
    "data": "tooltip",
    "exc": "tooltip",
    "func": "tooltip",
    "meth": "tooltip",
    "mod": "tooltip",
    "obj": "tooltip",
    # Roles within the std domain
    "confval": "tooltip",
    "hoverxref": "tooltip",
    "ref": "tooltip",  # Would be used by hoverxref_auto_ref if we set it to True
    "term": "tooltip",
}

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sunpy"

# Render inheritance diagrams in SVG
graphviz_output_format = "svg"

graphviz_dot_args = [
    "-Nfontsize=10",
    "-Nfontname=Helvetica Neue, Helvetica, Arial, sans-serif",
    "-Efontsize=10",
    "-Efontname=Helvetica Neue, Helvetica, Arial, sans-serif",
    "-Gfontsize=10",
    "-Gfontname=Helvetica Neue, Helvetica, Arial, sans-serif",
]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

# By default, when rendering docstrings for classes, sphinx.ext.autodoc will
# make docs with the class-level docstring and the class-method docstrings,
# but not the __init__ docstring, which often contains the parameters to
# class constructors across the scientific Python ecosystem. The option below
# will append the __init__ docstring to the class-level docstring when rendering
# the docs. For more options, see:
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autoclass_content
autoclass_content = "both"

# -- Sphinx Gallery ------------------------------------------------------------

# JSOC email os env
# see https://github.com/sunpy/sunpy/wiki/Home:-JSOC
os.environ["JSOC_EMAIL"] = "jsoc@sunpy.org"
sphinx_gallery_conf = {
    'backreferences_dir': os.path.join('generated', 'modules'),
    'filename_pattern': '^((?!skip_).)*$',
    'examples_dirs': os.path.join('..', 'examples'),
    'subsection_order': ExplicitOrder([
        '../examples/acquiring_data',
        '../examples/map',
        '../examples/map_transformations',
        '../examples/time_series',
        '../examples/units_and_coordinates',
        '../examples/plotting',
        '../examples/differential_rotation',
        '../examples/saving_and_loading_data',
        '../examples/computer_vision_techniques',
        '../examples/showcase',
    ]),
    'within_subsection_order': "ExampleTitleSortKey",
    'gallery_dirs': os.path.join('generated', 'gallery'),
    'matplotlib_animations': True,
    # Comes from the theme.
    "default_thumb_file": PNG_ICON,
    'abort_on_example_error': False,
    'plot_gallery': 'True',
    'remove_config_comments': True,
    'doc_module': ('sunpy'),
    'only_warn_on_example_error': True,
}

# -- Linking to OpenCV docs by using rst_epilog --------------------------------

try:
    import requests
    from bs4 import BeautifulSoup

    base_url = "https://docs.opencv.org"

    # The stable-version docs are the first item in the second list on the main page
    all_docs = BeautifulSoup(requests.get(base_url).text, 'html.parser')
    version = all_docs.find_all('ul')[1].li.a.attrs['href'][2:]  # strip leading "./"

    # Find the relative URL to the page for the `cv` namespace
    stable_docs = BeautifulSoup(requests.get(f"{base_url}/{version}/namespaces.html").text,
                                'html.parser')
    cv_namespace = stable_docs.find("a", string="cv").attrs['href']

    # Find the relative URL for warpAffine/filter2D in the `cv` namespace
    all_cv = BeautifulSoup(requests.get(f"{base_url}/{version}/{cv_namespace}").text, 'html.parser')
    warpAffine = all_cv.find("a", string="warpAffine").attrs['href'][6:]  # strip leading "../../"
    filter2D = all_cv.find("a", string="filter2D").attrs['href'][6:]  # strip leading "../../"

    # Construct the full URL for warpAffine/filter2D
    warpAffine_full = f"{base_url}/{version}/{warpAffine}"
    filter2D_full = f"{base_url}/{version}/{filter2D}"
except Exception:
    # In the event of any failure (e.g., no network connectivity)
    warpAffine_full = ""
    filter2D_full = ""

rst_epilog = f"""
.. |cv2_warpAffine| replace:: **cv2.warpAffine()**
.. _cv2_warpAffine: {warpAffine_full}
.. |cv2_filter2D| replace:: **cv2.filter2D()**
.. _cv2_filter2D: {filter2D_full}
"""

# -- Options for sphinx-copybutton ---------------------------------------------

# Python Repl + continuation, Bash, ipython and qtconsole + continuation, jupyter-console + continuation
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True

# -- Stability Page ------------------------------------------------------------

with open('./reference/sunpy_stability.yaml') as estability:
    yaml = YAML(typ='rt')
    sunpy_modules = yaml.load(estability.read())

html_context = {
    'sunpy_modules': sunpy_modules,
    'is_development': not is_release,
}


def jinja_to_rst(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.

    Depending on the building format, we render the page as a jinja template.

    For the linkchecker, we bypass templating as it doesn't support jinja, but we
    remove the jinja blocks so the page is still valid for checking.
    """
    jinja_pages = ["reference/stability", "dev_guide/index"]
    if app.builder.format == 'html':
        if docname in jinja_pages:
            print(f"Jinja rendering {docname}")
            rendered = app.builder.templates.render_string(
                source[0], app.config.html_context
            )
            source[0] = rendered
    else:
        if docname == "dev_guide/index":
            # This page only has a single jinja block that renders if the docs are
            # being built in development mode. We can simply  remove this block.
            for to_replace in ["{% if is_development %}", "{%else%}", "{% endif %}"]:
                source[0] = source[0].replace(to_replace, "")
        if docname == "reference/stability":
            # This page is a bit more complex, so we will remove the entire jinja block
            # leaving on the starting text of the page. Luckily there are no URLs in the
            # jinja block so this is safe.
            source[0] = source[0].split("{")[0]


# -- Sphinx setup --------------------------------------------------------------

def setup(app):
    # Handles the templating for the jinja pages in our docs
    app.connect("source-read", jinja_to_rst)
