import sys
import os

OPTIONS = ["PURE_PYTHON"]

for option in OPTIONS:
    globals()[option] = False
    option_name = "--" + option.lower().replace("_", "-")
    if option_name in sys.argv or "MYCP_" + option in os.environ:
        while option_name in sys.argv:
            sys.argv.remove(option_name)
        globals()[option] = True

"""
This module provides helpers for C++11+ projects using pybind11.

LICENSE:

Copyright (c) 2016 Wenzel Jakob <wenzel.jakob@epfl.ch>, All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors
   may be used to endorse or promote products derived from this software
   without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

# IMPORTANT: If you change this file in the pybind11 repo, also review
# setup_helpers.pyi for matching changes.
#
# If you copy this file in, you don't
# need the .pyi file; it's just an interface file for static type checkers.

import contextlib
import os
import platform
import shlex
import shutil
import sysconfig
import tempfile
import threading
import warnings
from functools import lru_cache
from pathlib import Path
import urllib.request
from glob import glob
from setuptools import find_packages, setup
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Optional,
    Tuple,
    TypeVar,
    Union,
)

try:
    from setuptools import Extension as _Extension
    from setuptools.command.build_ext import build_ext as _build_ext
except ImportError:
    from distutils.command.build_ext import build_ext as _build_ext  # type: ignore[assignment]
    from distutils.extension import Extension as _Extension  # type: ignore[assignment]

import distutils.ccompiler
import distutils.errors

WIN = sys.platform.startswith("win32") and "mingw" not in sysconfig.get_platform()
MACOS = sys.platform.startswith("darwin")
STD_TMPL = "/std:c++{}" if WIN else "-std=c++{}"


# It is recommended to use PEP 518 builds if using this module. However, this
# file explicitly supports being copied into a user's project directory
# standalone, and pulling pybind11 with the deprecated setup_requires feature.
# If you copy the file, remember to add it to your MANIFEST.in, and add the current
# directory into your path if it sits beside your setup.py.


class Pybind11Extension(_Extension):
    """
    Build a C++11+ Extension module with pybind11. This automatically adds the
    recommended flags when you init the extension and assumes C++ sources - you
    can further modify the options yourself.

    The customizations are:

    * ``/EHsc`` and ``/bigobj`` on Windows
    * ``stdlib=libc++`` on macOS
    * ``visibility=hidden`` and ``-g0`` on Unix

    Finally, you can set ``cxx_std`` via constructor or afterwards to enable
    flags for C++ std, and a few extra helper flags related to the C++ standard
    level. It is _highly_ recommended you either set this, or use the provided
    ``build_ext``, which will search for the highest supported extension for
    you if the ``cxx_std`` property is not set. Do not set the ``cxx_std``
    property more than once, as flags are added when you set it. Set the
    property to None to disable the addition of C++ standard flags.

    If you want to add pybind11 headers manually, for example for an exact
    git checkout, then set ``include_pybind11=False``.
    """

    # flags are prepended, so that they can be further overridden, e.g. by
    # ``extra_compile_args=["-g"]``.

    def _add_cflags(self, flags: List[str]) -> None:
        self.extra_compile_args[:0] = flags

    def _add_ldflags(self, flags: List[str]) -> None:
        self.extra_link_args[:0] = flags

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self._cxx_level = 0
        cxx_std = kwargs.pop("cxx_std", 0)

        if "language" not in kwargs:
            kwargs["language"] = "c++"

        include_pybind11 = kwargs.pop("include_pybind11", True)

        super().__init__(*args, **kwargs)

        # Include the installed package pybind11 headers
        if False:  # include_pybind11:
            # If using setup_requires, this fails the first time - that's okay
            try:
                import pybind11

                pyinc = pybind11.get_include()

                if pyinc not in self.include_dirs:
                    self.include_dirs.append(pyinc)
            except ModuleNotFoundError:
                pass

        self.cxx_std = cxx_std

        cflags = []
        if WIN:
            cflags += ["/EHsc", "/bigobj"]
        else:
            cflags += ["-fvisibility=hidden"]
            env_cflags = os.environ.get("CFLAGS", "")
            env_cppflags = os.environ.get("CPPFLAGS", "")
            c_cpp_flags = shlex.split(env_cflags) + shlex.split(env_cppflags)
            if not any(opt.startswith("-g") for opt in c_cpp_flags):
                cflags += ["-g0"]
        self._add_cflags(cflags)

    @property
    def cxx_std(self) -> int:
        """
        The CXX standard level. If set, will add the required flags. If left at
        0, it will trigger an automatic search when pybind11's build_ext is
        used. If None, will have no effect.  Besides just the flags, this may
        add a macos-min 10.9 or 10.14 flag if MACOSX_DEPLOYMENT_TARGET is
        unset.
        """
        return self._cxx_level

    @cxx_std.setter
    def cxx_std(self, level: int) -> None:
        if self._cxx_level:
            warnings.warn(
                "You cannot safely change the cxx_level after setting it!", stacklevel=2
            )

        # MSVC 2015 Update 3 and later only have 14 (and later 17) modes, so
        # force a valid flag here.
        if WIN and level == 11:
            level = 14

        self._cxx_level = level

        if not level:
            return

        cflags = [STD_TMPL.format(level)]
        ldflags = []

        if MACOS and "MACOSX_DEPLOYMENT_TARGET" not in os.environ:
            # C++17 requires a higher min version of macOS. An earlier version
            # (10.12 or 10.13) can be set manually via environment variable if
            # you are careful in your feature usage, but 10.14 is the safest
            # setting for general use. However, never set higher than the
            # current macOS version!
            current_macos = tuple(int(x) for x in platform.mac_ver()[0].split(".")[:2])
            desired_macos = (10, 9) if level < 17 else (10, 14)
            macos_string = ".".join(str(x) for x in min(current_macos, desired_macos))
            macosx_min = f"-mmacosx-version-min={macos_string}"
            cflags += [macosx_min]
            ldflags += [macosx_min]

        self._add_cflags(cflags)
        self._add_ldflags(ldflags)


# Just in case someone clever tries to multithread
tmp_chdir_lock = threading.Lock()


@contextlib.contextmanager
def tmp_chdir() -> Iterator[str]:
    "Prepare and enter a temporary directory, cleanup when done"

    # Threadsafe
    with tmp_chdir_lock:
        olddir = os.getcwd()
        try:
            tmpdir = tempfile.mkdtemp()
            os.chdir(tmpdir)
            yield tmpdir
        finally:
            os.chdir(olddir)
            shutil.rmtree(tmpdir)


# cf http://bugs.python.org/issue26689
def has_flag(compiler: Any, flag: str) -> bool:
    """
    Return the flag if a flag name is supported on the
    specified compiler, otherwise None (can be used as a boolean).
    If multiple flags are passed, return the first that matches.
    """

    with tmp_chdir():
        fname = Path("flagcheck.cpp")
        # Don't trigger -Wunused-parameter.
        fname.write_text("int main (int, char **) { return 0; }", encoding="utf-8")

        try:
            compiler.compile([str(fname)], extra_postargs=[flag])
        except distutils.errors.CompileError:
            return False
        return True


# Every call will cache the result
cpp_flag_cache = None


@lru_cache()
def auto_cpp_level(compiler: Any) -> Union[str, int]:
    """
    Return the max supported C++ std level (17, 14, or 11). Returns latest on Windows.
    """

    if WIN:
        return "latest"

    levels = [17, 14, 11]

    for level in levels:
        if has_flag(compiler, STD_TMPL.format(level)):
            return level

    msg = "Unsupported compiler -- at least C++11 support is needed!"
    raise RuntimeError(msg)


class build_ext(_build_ext):  # noqa: N801
    """
    Customized build_ext that allows an auto-search for the highest supported
    C++ level for Pybind11Extension. This is only needed for the auto-search
    for now, and is completely optional otherwise.
    """

    def build_extensions(self) -> None:
        """
        Build extensions, injecting C++ std for Pybind11Extension if needed.
        """

        for ext in self.extensions:
            if hasattr(ext, "_cxx_level") and ext._cxx_level == 0:
                ext.cxx_std = auto_cpp_level(self.compiler)

        super().build_extensions()


def intree_extensions(
    paths: Iterable[str], package_dir: Optional[Dict[str, str]] = None
) -> List[Pybind11Extension]:
    """
    Generate Pybind11Extensions from source files directly located in a Python
    source tree.

    ``package_dir`` behaves as in ``setuptools.setup``.  If unset, the Python
    package root parent is determined as the first parent directory that does
    not contain an ``__init__.py`` file.
    """
    exts = []

    if package_dir is None:
        for path in paths:
            parent, _ = os.path.split(path)
            while os.path.exists(os.path.join(parent, "__init__.py")):
                parent, _ = os.path.split(parent)
            relname, _ = os.path.splitext(os.path.relpath(path, parent))
            qualified_name = relname.replace(os.path.sep, ".")
            exts.append(Pybind11Extension(qualified_name, [path]))
        return exts

    for path in paths:
        for prefix, parent in package_dir.items():
            if path.startswith(parent):
                relname, _ = os.path.splitext(os.path.relpath(path, parent))
                qualified_name = relname.replace(os.path.sep, ".")
                if prefix:
                    qualified_name = prefix + "." + qualified_name
                exts.append(Pybind11Extension(qualified_name, [path]))
                break
        else:
            msg = (
                f"path {path} is not a child of any of the directories listed "
                f"in 'package_dir' ({package_dir})"
            )
            raise ValueError(msg)

    return exts


def naive_recompile(obj: str, src: str) -> bool:
    """
    This will recompile only if the source file changes. It does not check
    header files, so a more advanced function or Ccache is better if you have
    editable header files in your package.
    """
    return os.stat(obj).st_mtime < os.stat(src).st_mtime


def no_recompile(obg: str, src: str) -> bool:  # noqa: ARG001
    """
    This is the safest but slowest choice (and is the default) - will always
    recompile sources.
    """
    return True


S = TypeVar("S", bound="ParallelCompile")

CCompilerMethod = Callable[
    [
        distutils.ccompiler.CCompiler,
        List[str],
        Optional[str],
        Optional[Union[Tuple[str], Tuple[str, Optional[str]]]],
        Optional[List[str]],
        bool,
        Optional[List[str]],
        Optional[List[str]],
        Optional[List[str]],
    ],
    List[str],
]


# Optional parallel compile utility
# inspired by: http://stackoverflow.com/questions/11013851/speeding-up-build-process-with-distutils
# and: https://github.com/tbenthompson/cppimport/blob/stable/cppimport/build_module.py
# and NumPy's parallel distutils module:
#              https://github.com/numpy/numpy/blob/master/numpy/distutils/ccompiler.py
class ParallelCompile:
    """
    Make a parallel compile function. Inspired by
    numpy.distutils.ccompiler.CCompiler.compile and cppimport.

    This takes several arguments that allow you to customize the compile
    function created:

    envvar:
        Set an environment variable to control the compilation threads, like
        NPY_NUM_BUILD_JOBS
    default:
        0 will automatically multithread, or 1 will only multithread if the
        envvar is set.
    max:
        The limit for automatic multithreading if non-zero
    needs_recompile:
        A function of (obj, src) that returns True when recompile is needed.  No
        effect in isolated mode; use ccache instead, see
        https://github.com/matplotlib/matplotlib/issues/1507/

    To use::

        ParallelCompile("NPY_NUM_BUILD_JOBS").install()

    or::

        with ParallelCompile("NPY_NUM_BUILD_JOBS"):
            setup(...)

    By default, this assumes all files need to be recompiled. A smarter
    function can be provided via needs_recompile.  If the output has not yet
    been generated, the compile will always run, and this function is not
    called.
    """

    __slots__ = ("envvar", "default", "max", "_old", "needs_recompile")

    def __init__(
        self,
        envvar: Optional[str] = None,
        default: int = 0,
        max: int = 0,  # pylint: disable=redefined-builtin
        needs_recompile: Callable[[str, str], bool] = no_recompile,
    ) -> None:
        self.envvar = envvar
        self.default = default
        self.max = max
        self.needs_recompile = needs_recompile
        self._old: List[CCompilerMethod] = []

    def function(self) -> CCompilerMethod:
        """
        Builds a function object usable as distutils.ccompiler.CCompiler.compile.
        """

        def compile_function(
            compiler: distutils.ccompiler.CCompiler,
            sources: List[str],
            output_dir: Optional[str] = None,
            macros: Optional[Union[Tuple[str], Tuple[str, Optional[str]]]] = None,
            include_dirs: Optional[List[str]] = None,
            debug: bool = False,
            extra_preargs: Optional[List[str]] = None,
            extra_postargs: Optional[List[str]] = None,
            depends: Optional[List[str]] = None,
        ) -> Any:
            # These lines are directly from distutils.ccompiler.CCompiler
            macros, objects, extra_postargs, pp_opts, build = compiler._setup_compile(  # type: ignore[attr-defined]
                output_dir, macros, include_dirs, sources, depends, extra_postargs
            )
            cc_args = compiler._get_cc_args(pp_opts, debug, extra_preargs)  # type: ignore[attr-defined]

            # The number of threads; start with default.
            threads = self.default

            # Determine the number of compilation threads, unless set by an environment variable.
            if self.envvar is not None:
                threads = int(os.environ.get(self.envvar, self.default))

            def _single_compile(obj: Any) -> None:
                try:
                    src, ext = build[obj]
                except KeyError:
                    return

                if not os.path.exists(obj) or self.needs_recompile(obj, src):
                    compiler._compile(obj, src, ext, cc_args, extra_postargs, pp_opts)  # type: ignore[attr-defined]

            try:
                # Importing .synchronize checks for platforms that have some multiprocessing
                # capabilities but lack semaphores, such as AWS Lambda and Android Termux.
                import multiprocessing.synchronize
                from multiprocessing.pool import ThreadPool
            except ImportError:
                threads = 1

            if threads == 0:
                try:
                    threads = multiprocessing.cpu_count()
                    threads = self.max if self.max and self.max < threads else threads
                except NotImplementedError:
                    threads = 1

            if threads > 1:
                with ThreadPool(threads) as pool:
                    for _ in pool.imap_unordered(_single_compile, objects):
                        pass
            else:
                for ob in objects:
                    _single_compile(ob)

            return objects

        return compile_function

    def install(self: S) -> S:
        """
        Installs the compile function into distutils.ccompiler.CCompiler.compile.
        """
        distutils.ccompiler.CCompiler.compile = self.function()  # type: ignore[assignment]
        return self

    def __enter__(self: S) -> S:
        self._old.append(distutils.ccompiler.CCompiler.compile)
        return self.install()

    def __exit__(self, *args: Any) -> None:
        distutils.ccompiler.CCompiler.compile = self._old.pop()  # type: ignore[assignment]


assert sys.version_info >= (3, 7, 0), "Materialyoucolor requires Python 3.7+"

with open("README.md", "r") as f:
    long_description = f.read()
    f.close()

with open("materialyoucolor/__init__.py", "r") as file:
    VERSION = file.read().split("= ")[-1].split('"')[1].split('"')[0]
    file.close()


def download_files(base_url, folder, file_map):
    files_skipped = 0
    if not os.path.exists(folder):
        os.makedirs(folder)

    if isinstance(file_map, list):
        file_map = dict.fromkeys(file_map)

    elif isinstance(file_map, set):
        _file_map = {}
        for _ in list(file_map):
            _file_map[_] = _
        file_map = _file_map

    for file_url, save_path in file_map.items():
        if not save_path:
            save_path = os.path.basename(file_url)
        if (
            "/" in save_path
            and (_path := os.path.join(folder, *save_path.split("/")[:-1]))
            and not os.path.exists(_path)
        ):
            os.makedirs(_path)

        file_name = os.path.join(folder, save_path)
        if os.path.exists(file_name):
            files_skipped += 1
            continue
        with open(file_name, "w") as write_buffer:
            write_buffer.write(
                urllib.request.urlopen(base_url + file_url).read().decode("utf-8")
            )
            write_buffer.close()
            print("[Downloaded] :", file_name)

    return len(file_map) != files_skipped


# Download files from material foundation
MCU_COMMIT = "1217346b9416e6e55c83c6e9295f6aed001e852e"
MCU_URL = (
    "https://raw.githubusercontent.com/material-foundation/"
    "material-color-utilities/{}/cpp/".format(MCU_COMMIT)
)
MCU_FOLDER = "./materialyoucolor/quantize/"
MCU_FILES = [
    "quantize/wu.h",
    "quantize/wu.cc",
    "quantize/wsmeans.h",
    "quantize/wsmeans.cc",
    "quantize/lab.h",
    "quantize/lab.cc",
    "quantize/celebi.h",
    "quantize/celebi.cc",
    "utils/utils.h",
    "utils/utils.cc",
]
PATCH_FILE = "quantizer_cpp.patch"

# Download files from pybind11
PYBIND_COMMIT = "ddb8b67a8aa8198ec8a028fb28f6870e44e7a467"
PYBIND_URL = (
    "https://raw.githubusercontent.com/pybind/pybind11/" "{}/include/pybind11/".format(
        PYBIND_COMMIT
    )
)
PYBIND_FOLDER = "./materialyoucolor/quantize/pybind11/"
PYBIND_FILES = [
    "cast.h",
    "attr.h",
    "buffer_info.h",
    "gil_safe_call_once.h",
    "options.h",
    "typing.h",
    "gil.h",
    "pytypes.h",
    "pybind11.h",
    "stl.h",
]
PYBIND_EXTRA_FILES = {
    "detail/type_caster_base.h",
    "detail/init.h",
    "detail/internals.h",
    "detail/typeid.h",
    "detail/descr.h",
    "detail/common.h",
    "detail/class.h",
    "stl/filesystem.h",
}

# For stb_image backend
STB_IMAGE_COMMIT = "ae721c50eaf761660b4f90cc590453cdb0c2acd0"
STB_IMAGE_URL = (
    "https://raw.githubusercontent.com/nothings"
    "/stb/{}/".format(STB_IMAGE_COMMIT)
)

if PURE_PYTHON:
    print(
        "\nWarning: Skipping build of extension : `QuantizeCelebi`"
        "\nYou won't be able to use dominant color getting part.\n"
    )
else:
    print("[Info]: Ensuring external files")
    should_apply = download_files(MCU_URL, MCU_FOLDER, MCU_FILES)
    download_files(PYBIND_URL, PYBIND_FOLDER, PYBIND_FILES)
    download_files(PYBIND_URL, PYBIND_FOLDER, PYBIND_EXTRA_FILES)
    download_files(STB_IMAGE_URL, MCU_FOLDER, ["stb_image.h"])
    
    # write __init__.py
    with open(os.path.join(MCU_FOLDER, "__init__.py"), "w") as file:
        file.write("from .celebi import QuantizeCelebi, ImageQuantizeCelebi")
        file.close()
    
    if should_apply:
        print("[Info]: Applying patch: ", PATCH_FILE)
        os.system(
            "patch --directory={} --strip=1 -N < {}".format(
                "./materialyoucolor/quantize/", PATCH_FILE
            )
        )

setup(
    name="materialyoucolor",
    version=VERSION,
    description="Material You color generation algorithms in pure python!",
    author="Ansh Dadwal",
    author_email="anshdadwal298@gmail.com",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    exclude=["README.md", "*.pyc", "example.py"],
    ext_modules=[
        Pybind11Extension(
            "materialyoucolor.quantize.celebi",
            sorted(glob("materialyoucolor/quantize/*.cc")),
            extra_compile_args=["-std=c++17"] if os.name != "nt" else ["/std:c++17"],
        )
        if not PURE_PYTHON
        else ()
    ],
)
