# -*- coding: utf-8 -*-
import json
import re
import sys
import typing as t

from setuptools import find_packages, setup

with open("portal/__init__.py", "r") as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)


def parse_requirements(packages: t.Dict[str, t.Dict[str, t.Any]]):
    """Parse a group of requirements from `Pipfile.lock`.

    https://setuptools.pypa.io/en/latest/userguide/dependency_management.html

    Args:
        packages: The group name of the requirements.

    Returns:
        The requirements as a list of strings, required by `setuptools.setup`
    """

    requirements: t.List[str] = []
    for name, package in packages.items():
        requirement = name
        if requirement == "cfl-common":
            requirement += f"=={version}"
        else:
            if "extras" in package:
                requirement += f"[{','.join(package['extras'])}]"
            if "version" in package:
                requirement += package["version"]
            if "markers" in package:
                requirement += f"; {package['markers']}"
        requirements.append(requirement)

    return requirements


# Parse Pipfile.lock into strings.
with open("Pipfile.lock", "r", encoding="utf-8") as pipfile_lock:
    lock = json.load(pipfile_lock)
    install_requires = parse_requirements(lock["default"])
    dev_requires = parse_requirements(lock["develop"])

try:
    from semantic_release import setup_hook

    setup_hook(sys.argv)
except ImportError:
    pass

setup(
    name="codeforlife-portal",
    version=version,
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={"dev": dev_requires},
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.12",
        "Framework :: Django",
    ],
    zip_safe=False,
)
