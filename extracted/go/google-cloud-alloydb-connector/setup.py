# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import io
import os

import setuptools

name = "google-cloud-alloydb-connector"
description = "A Python client library for connecting securely to your Google Cloud AlloyDB instances."

release_status = "Development Status :: 5 - Production/Stable"
dependencies = [
    "aiofiles",
    "aiohttp",
    "cryptography>=42.0.0",
    "requests",
    "google-auth",
    "protobuf",
    "google-cloud-alloydb",
    "google-api-core",
]

package_root = os.path.abspath(os.path.dirname(__file__))

readme_filename = os.path.join(package_root, "README.md")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

version = {}
with open(
    os.path.join(package_root, "google/cloud/alloydb/connector/version.py")
) as fp:
    exec(fp.read(), version)
version = version["__version__"]

# Only include packages under the 'google' namespace. Do not include tests,
# samples, etc.
packages = [
    package
    for package in setuptools.find_namespace_packages()
    if package.startswith("google")
]


setuptools.setup(
    name=name,
    version=version,
    description=description,
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Google LLC",
    author_email="googleapis-packages@google.com",
    license="Apache 2.0",
    url="https://github.com/GoogleCloudPlatform/alloydb-python-connector",
    classifiers=[
        release_status,
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    platforms="Posix; MacOS X; Windows",
    packages=packages,
    install_requires=dependencies,
    extras_require={
        "pg8000": ["pg8000>=1.31.1"],
        "asyncpg": ["asyncpg>=0.30.0"],
    },
    python_requires=">=3.9",
    include_package_data=True,
    zip_safe=False,
    package_data={"google.cloud.alloydb.connector": ["py.typed"]},
)
