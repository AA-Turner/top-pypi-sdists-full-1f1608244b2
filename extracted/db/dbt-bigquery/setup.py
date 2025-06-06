#!/usr/bin/env python
import sys

# require a supported version of Python
if sys.version_info < (3, 9):
    print("Error: dbt does not support this version of Python.")
    print("Please upgrade to Python 3.9 or higher.")
    sys.exit(1)

try:
    from setuptools import find_namespace_packages
except ImportError:
    # the user has a downlevel version of setuptools.
    print("Error: dbt requires setuptools v40.1.0 or higher.")
    print('Please upgrade setuptools with "pip install --upgrade setuptools" and try again')
    sys.exit(1)

from pathlib import Path
from setuptools import setup


# pull the long description from the README
README = Path(__file__).parent / "README.md"

# used for this adapter's version and in determining the compatible dbt-core version
VERSION = Path(__file__).parent / "dbt/adapters/bigquery/__version__.py"


def _dbt_bigquery_version() -> str:
    """
    Pull the package version from the main package version file
    """
    attributes = {}
    exec(VERSION.read_text(), attributes)
    return attributes["version"]


package_name = "dbt-bigquery"
description = """The BigQuery adapter plugin for dbt"""

setup(
    name="dbt-bigquery",
    version=_dbt_bigquery_version(),
    description="The Bigquery adapter plugin for dbt",
    long_description=README.read_text(),
    long_description_content_type="text/markdown",
    author="dbt Labs",
    author_email="info@dbtlabs.com",
    url="https://github.com/dbt-labs/dbt-bigquery",
    packages=find_namespace_packages(include=["dbt", "dbt.*"]),
    include_package_data=True,
    install_requires=[
        "dbt-common>=1.10,<2.0",
        "dbt-adapters>=1.7,<2.0",
        # 3.20 introduced pyarrow>=3.0 under the `pandas` extra
        "google-cloud-bigquery[pandas]>=3.0,<4.0",
        "google-cloud-storage~=2.4",
        "google-cloud-dataproc~=5.0",
        # ----
        # Expect compatibility with all new versions of these packages, so lower bounds only.
        "google-api-core>=2.11.0",
        # add dbt-core to ensure backwards compatibility of installation, this is not a functional dependency
        "dbt-core>=1.8.0",
    ],
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
)
