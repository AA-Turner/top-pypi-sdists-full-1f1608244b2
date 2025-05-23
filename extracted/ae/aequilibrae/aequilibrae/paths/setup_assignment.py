# This is a convenience file to allow developers easier compilation of just the assignment module
# Generally compilation is done directly from the root setup.py
# Make sure to keep this up to date with that file

import platform
import numpy as np
from Cython.Build import cythonize

try:
    from setuptools import setup
    from setuptools import Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension

is_win = "WINDOWS" in platform.platform().upper()
prefix = "/" if is_win else "-f"
cpp_std = "/std:c++17" if is_win else "-std=c++17"

ext_modules = [
    Extension(
        "AoN",
        ["AoN.pyx"],
        extra_compile_args=[f"{prefix}openmp", cpp_std],  # do we want -Ofast?
        extra_link_args=[f"{prefix}openmp"],
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
        include_dirs=[np.get_include()],
    )
]

setup(name="AoN", ext_modules=cythonize(ext_modules))
