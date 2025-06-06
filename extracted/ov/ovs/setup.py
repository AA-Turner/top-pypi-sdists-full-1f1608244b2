# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import os.path
import sys

from setuptools.command.build_ext import build_ext
try:
    from setuptools.errors import CCompilerError, ExecError, PlatformError
except ImportError:  # Needed for setuptools < 59.0
    from distutils.errors import CCompilerError
    from distutils.errors import DistutilsExecError as ExecError
    from distutils.errors import DistutilsPlatformError as PlatformError

import setuptools

VERSION = "3.5.1"
README_PATH = os.path.abspath(
    os.path.join(os.path.abspath(__file__), os.pardir, 'README.rst')
)

for x in ("version.py", "dirs.py"):
    if not os.path.exists(f"ovs/{x}"):
        print(f"Ensure {x} is created by running make python/ovs/{x}",
              file=sys.stderr)
        sys.exit(-1)

with open(README_PATH) as fh:
    long_description = fh.read()

ext_errors = (CCompilerError, ExecError, PlatformError)
if sys.platform == 'win32':
    ext_errors += (IOError, ValueError)


class BuildFailed(Exception):
    pass


class try_build_ext(build_ext):
    # This class allows C extension building to fail
    # NOTE: build_ext is not a new-style class

    def run(self):
        try:
            build_ext.run(self)
        except PlatformError:
            raise BuildFailed()

    def build_extension(self, ext):
        try:
            build_ext.build_extension(self, ext)
        except ext_errors:
            raise BuildFailed()


# Allow caller of setup.py to pass in libopenvswitch.a as an object for linking
# plus all the dependencies through the use of 'extra_cflags' and 'extra_libs'
# environment variables when not building a shared openvswitch library.

if os.environ.get('enable_shared', '') == 'no':
    libraries = []
else:
    libraries = ['openvswitch']

extra_cflags = os.environ.get('extra_cflags', '').split()
extra_libs = os.environ.get('extra_libs', '').split()

flow_extras_require = ['netaddr', 'pyparsing']

setup_args = dict(
    name='ovs',
    description='Open vSwitch library',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    version=VERSION,
    url='http://www.openvswitch.org/',
    author='Open vSwitch',
    author_email='dev@openvswitch.org',
    packages=['ovs', 'ovs.compat', 'ovs.compat.sortedcontainers',
              'ovs.db', 'ovs.flow', 'ovs.flowviz', 'ovs.flowviz.odp',
              'ovs.flowviz.ofp', 'ovs.unixctl'],
    keywords=['openvswitch', 'ovs', 'OVSDB'],
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Database :: Front-Ends',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    ext_modules=[setuptools.Extension("ovs._json",
                                      sources=["ovs/_json.c"],
                                      libraries=libraries,
                                      extra_compile_args=extra_cflags,
                                      extra_link_args=extra_libs)],
    cmdclass={'build_ext': try_build_ext},
    install_requires=['sortedcontainers'],
    extras_require={':sys_platform == "win32"': ['pywin32 >= 1.0'],
                    'dns': ['unbound'],
                    'flow': flow_extras_require,
                    'flowviz':
                        [*flow_extras_require, 'click', 'rich', 'graphviz'],
                    },
    scripts=["ovs/flowviz/ovs-flowviz"],
    package_data={'ovs.flowviz': ['ovs-flowviz.conf']},
)

try:
    setuptools.setup(**setup_args)
except BuildFailed:
    BUILD_EXT_WARNING = ("WARNING: The C extension could not be compiled, "
                         "speedups are not enabled.")
    print("*" * 75)
    print(BUILD_EXT_WARNING)
    print("Failure information, if any, is above.")
    print("Retrying the build without the C extension.")
    print("*" * 75)

    del setup_args['cmdclass']
    del setup_args['ext_modules']
    setuptools.setup(**setup_args)
