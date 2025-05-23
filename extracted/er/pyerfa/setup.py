# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst

import os
import re
import sys
import functools
import setuptools
import subprocess
from warnings import warn
import packaging.version
import sysconfig

try:
    # First available on setuptools 70.1 from January 2024
    # https://setuptools.pypa.io/en/stable/history.html#v70-1-0
    from setuptools.command.bdist_wheel import bdist_wheel
except ImportError:
    from wheel.bdist_wheel import bdist_wheel


LIBERFADIR = os.path.join('liberfa', 'erfa')
ERFA_SRC = os.path.join(LIBERFADIR, 'src')
GEN_FILES = [
    os.path.join('erfa', 'core.py'),
    os.path.join('erfa', 'ufunc.c'),
]


# build with Py_LIMITED_API unless in freethreading build (which does not currently
# support the limited API in py313t)
USE_PY_LIMITED_API = not sysconfig.get_config_var("Py_GIL_DISABLED")

class bdist_wheel_abi3(bdist_wheel):
    def get_tag(self):
        python, abi, plat = super().get_tag()

        if USE_PY_LIMITED_API and python.startswith("cp"):
            # on CPython, our wheels are abi3 and compatible back to 3.9
            return "cp39", "abi3", plat

        return python, abi, plat

def newer(source, target):
    import pathlib

    source = pathlib.Path(source)
    if not source.exists():
        raise FileNotFoundError(f"file '{source.resolve()}' does not exist")

    target = pathlib.Path(target)
    if not target.exists():
        return 1

    return source.stat().st_mtime > target.stat().st_mtime


# https://mail.python.org/pipermail/distutils-sig/2007-September/008253.html
class NumpyExtension(setuptools.Extension):
    """Extension type that adds the NumPy include directory to include_dirs."""

    @property
    def include_dirs(self):
        from numpy import get_include
        return self._include_dirs + [get_include()]

    @include_dirs.setter
    def include_dirs(self, include_dirs):
        self._include_dirs = include_dirs


def get_liberfa_versions(path=os.path.join(LIBERFADIR, 'configure.ac')):
    with open(path) as fd:
        s = fd.read()

    mobj = re.search(r'AC_INIT\(\[erfa\],\[(?P<version>[0-9.]+)\]\)', s)
    if not mobj:
        warn('unable to detect liberfa version')
        return []

    version = packaging.version.parse(mobj.group('version'))

    mobj = re.search(
        r'AC_DEFINE\(\[SOFA_VERSION\], \["(?P<version>\d{8}(_\w)?)"\],', s)
    if not mobj:
        warn('unable to detect SOFA version')
        return []
    sofa_version = mobj.group('version')

    return [
        ('PACKAGE_VERSION', version.base_version),
        ('PACKAGE_VERSION_MAJOR', version.major),
        ('PACKAGE_VERSION_MINOR', version.minor),
        ('PACKAGE_VERSION_MICRO', version.micro),
        ('SOFA_VERSION', sofa_version),
    ]


def get_extensions():
    gen_files_exist = all(os.path.isfile(fn) for fn in GEN_FILES)
    gen_files_outdated = False
    if os.path.isdir(ERFA_SRC):
        # assume that 'erfaversion.c' is updated at each release at least
        src = os.path.join(ERFA_SRC, 'erfaversion.c')
        gen_files_outdated = any(newer(src, fn) for fn in GEN_FILES)
    elif not gen_files_exist:
        raise RuntimeError(
            'Missing "liberfa" source files, unable to generate '
            '"erfa/ufunc.c" and "erfa/core.py". '
            'Please check your source tree. '
            'Maybe "git submodule update" could help.')

    if not gen_files_exist or gen_files_outdated:
        print('Run "erfa_generator.py"')
        cmd = [sys.executable, 'erfa_generator.py', ERFA_SRC, '--quiet']
        subprocess.run(cmd, check=True)

    sources = [os.path.join('erfa', 'ufunc.c')]
    include_dirs = []
    libraries = []
    define_macros = []

    if int(os.environ.get('PYERFA_USE_SYSTEM_LIBERFA', 0)):
        print('Using system liberfa')
        libraries.append('erfa')
    else:
        # get all of the .c files in the liberfa/erfa/src directory
        erfafns = os.listdir(ERFA_SRC)
        sources.extend([os.path.join(ERFA_SRC, fn)
                        for fn in erfafns
                        if fn.endswith('.c') and not fn.startswith('t_')])

        include_dirs.append(ERFA_SRC)

        # liberfa configuration
        config_h = os.path.join(LIBERFADIR, 'config.h')
        if not os.path.exists(config_h):
            print('Configure liberfa')
            configure = os.path.join(LIBERFADIR, 'configure')
            try:
                if not os.path.exists(configure):
                    subprocess.run(
                        ['./bootstrap.sh'], check=True, cwd=LIBERFADIR)
                subprocess.run(['./configure'], check=True, cwd=LIBERFADIR)
            except (subprocess.SubprocessError, OSError) as exc:
                warn(f'unable to configure liberfa: {exc}')

        if not os.path.exists(config_h):
            liberfa_versions = get_liberfa_versions()
            if liberfa_versions:
                print('Configure liberfa ("configure.ac" scan)')
                lines = []
                for name, value in liberfa_versions:
                    # making sure strings are correctly quoted
                    lines.append(f'#define {name} {value!r}'.replace("'", '"'))
                with open(config_h, 'w') as fd:
                    fd.write('\n'.join(lines))
            else:
                warn('unable to get liberfa version')

        if os.path.exists(config_h):
            include_dirs.append(LIBERFADIR)
            define_macros.append(('HAVE_CONFIG_H', '1'))
        elif 'sdist' in sys.argv:
            raise RuntimeError('missing "configure" script in "liberfa/erfa"')

    if USE_PY_LIMITED_API:
        define_macros.append(("Py_LIMITED_API", "0x30900f0"))

    erfa_ext = NumpyExtension(
        name="erfa.ufunc",
        sources=sources,
        include_dirs=include_dirs,
        libraries=libraries,
        define_macros=define_macros,
        py_limited_api=USE_PY_LIMITED_API,
        language="c")

    return [erfa_ext]


try:
    with open('erfa/_dev/scm_version.py') as fd:
        source = fd.read()
except FileNotFoundError:
    guess_next_dev = None
else:
    import types
    scm_version = types.ModuleType('scm_version')
    scm_version.__file__ = 'erfa/_dev/scm_version.py'
    code = compile(source, scm_version.__file__, 'exec')
    try:
        exec(code, scm_version.__dict__)
    except ImportError:
        guess_next_dev = None
    else:
        guess_next_dev = functools.partial(scm_version._guess_next_dev,
                                           liberfadir=LIBERFADIR)

use_scm_version = {
    'write_to': os.path.join('erfa', '_version.py'),
    'version_scheme': guess_next_dev,
}

setuptools.setup(
    use_scm_version=use_scm_version,
    ext_modules=get_extensions(),
    cmdclass={"bdist_wheel": bdist_wheel_abi3},
)
