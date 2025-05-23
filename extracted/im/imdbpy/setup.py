from setuptools import setup
import os

VERSION = "2022.7.9"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="IMDbPY",
    description="IMDbPY is now cinemagoer",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    version=VERSION,
    install_requires=["cinemagoer"],
    url='https://cinemagoer.github.io/',
    project_urls={
        'Source': 'https://github.com/cinemagoer/cinemagoer',
    },
    classifiers=["Development Status :: 7 - Inactive"],
)
