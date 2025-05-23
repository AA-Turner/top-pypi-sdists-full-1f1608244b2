# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-strict

"""
TODO(T132414938) Add a module-level docstring
"""


import glob
import json
import os
import sys
from pathlib import Path
from typing import List, Tuple

from setuptools import find_packages, setup


if sys.version_info < (3, 8):
    sys.exit("Error: pyre-check only runs on Python 3.8 and above.")


def get_all_files(root: Path, extension_glob: str) -> List[Tuple[str, List[str]]]:
    if not os.path.isdir(root):
        return []
    result = []
    for absolute_directory, _, _ in os.walk(root):
        relative_directory, files = get_data_files(
            directory=absolute_directory, extension_glob=extension_glob
        )
        if not files:
            continue
        target = os.path.join("lib", "pyre_check", relative_directory)
        result.append((target, files))
    return result


def get_data_files(directory: str, extension_glob: str) -> Tuple[str, List[str]]:
    # We need to relativize data_files, see https://github.com/pypa/wheel/issues/92.
    relative_directory = os.path.relpath(os.path.abspath(directory), os.getcwd())
    return (
        relative_directory,
        glob.glob(os.path.join(relative_directory, extension_glob)),
    )


def find_taint_stubs() -> List[Tuple[str, List[str]]]:
    taint_stubs = []
    for path in Path(os.path.join(os.getcwd(), "taint")).iterdir():
        if path.is_dir():
            relative_directory, temporary_stubs = get_data_files(
                directory=str(path), extension_glob="*"
            )
            if temporary_stubs:
                taint_stubs.append(
                    (
                        os.path.join("lib", "pyre_check", relative_directory),
                        temporary_stubs,
                    )
                )
    relative_directory, third_party_taint_stubs = get_data_files(
        directory=os.path.join(os.getcwd(), "third_party_taint"), extension_glob="*"
    )
    if third_party_taint_stubs:
        taint_stubs.append(
            (
                os.path.join("lib", "pyre_check", relative_directory),
                third_party_taint_stubs,
            )
        )
    return taint_stubs


def run(
    package_name: str,
    package_version: str,
    module_name: str,
    runtime_dependencies: List[str],
    long_description: str,
    **kwargs: object
) -> None:
    setup(
        name=package_name,
        version=package_version,
        description="A performant type checker for Python",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://pyre-check.org/",
        download_url="https://github.com/facebook/pyre-check",
        author="Facebook",
        author_email="pyre@fb.com",
        maintainer="Facebook",
        maintainer_email="pyre@fb.com",
        license="MIT",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Operating System :: MacOS",
            "Operating System :: POSIX :: Linux",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Topic :: Software Development",
            "Typing :: Typed",
        ],
        keywords="typechecker development",
        packages=find_packages(exclude=["tests", "pyre-check"]),
        data_files=[("bin", ["bin/pyre.bin"])]
        + get_all_files(root=Path.cwd() / "typeshed", extension_glob="*.pyi")
        + get_all_files(root=Path.cwd() / "stubs/django", extension_glob="*.pyi")
        + get_all_files(root=Path.cwd() / "stubs/lxml", extension_glob="*.pyi")
        + get_all_files(root=Path.cwd() / "pysa_filters", extension_glob="*.json")
        + find_taint_stubs(),
        python_requires=">=3.8",
        install_requires=runtime_dependencies,
        entry_points=dict(  # noqa we need to do this to make this .format-able
            console_scripts=[
                "pyre = " + module_name + ".client.pyre:main",
                "pyre-upgrade = " + module_name + ".tools.upgrade.upgrade:main",
            ]
        ),
        **kwargs
    )


def main() -> None:
    with open("README.md", encoding="UTF-8") as f:
        long_description = f.read()

    run(
        package_name="pyre-check",
        package_version="0.9.23",
        module_name="pyre_check",
        runtime_dependencies=json.loads(r"""["click>=8.0", "dataclasses-json==0.5.7", "libcst", "psutil", "pyre-extensions>=0.0.29", "tabulate", "testslide>=2.7.0", "typing_extensions", "typing_inspect"]"""),
        long_description=long_description,
    )


if __name__ == "__main__":
    main()
