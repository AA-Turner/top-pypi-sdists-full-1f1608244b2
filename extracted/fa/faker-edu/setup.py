"""Provider for Faker which adds information about educational institutions and academics."""

import setuptools

try:
    with open("README.md", "r") as fh:
        long_description = fh.read()  # pylint: disable=invalid-name
except FileNotFoundError:
    # pylint: disable=invalid-name
    long_description = (
        "Provider for [Faker](https://faker.readthedocs.io/) which adds fake "
        "information about educational institutions and academics."
    )

setuptools.setup(
    name="faker-edu",
    version="1.1.0",
    author="Allison Letts, Aaron Crosman, Paul Prescod",
    description="Provider for Faker which adds fake information about "
    "educational institutions and academics.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SFDO-Community-Sprints/Snowfakery-Edu",
    packages=setuptools.find_packages(),
    install_requires=["faker"],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
