from urllib.request import urlopen

_conf_url = \
        "https://raw.githubusercontent.com/inducer/sphinxconfig/main/sphinxconfig.py"
with urlopen(_conf_url) as _inf:
    exec(compile(_inf.read(), _conf_url, "exec"), globals())

copyright = "2008-21, Andreas Kloeckner"

ver_dic = {}
exec(
    compile(
        open("../pycuda/__init__.py").read(), "../pycuda/__init__.py", "exec"
    ),
    ver_dic,
)
version = ".".join(str(x) for x in ver_dic["VERSION"])
# The full version, including alpha/beta/rc tags.
release = ver_dic["VERSION_TEXT"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "codepy": ("https://documen.tician.de/codepy/", None),
    "pytest": ("https://docs.pytest.org/en/stable/", None),
}

nitpick_ignore_regex = [
    ["py:class", r"numpy.(float32|u?int32)"],  # not sure why these don't work?
]
