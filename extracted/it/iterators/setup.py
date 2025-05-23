import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iterators",
    packages = ['iterators'],
    version="0.2.0",
    author="leangaurav",
    author_email="leangaurav.me@gmail.com",
    description="Iterator utility classes and functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leangaurav/pypi_iterator",
    download_url="https://github.com/leangaurav/pypi_iterator/archive/v_0.2.0.tar.gz",
    keywords = ['ITERATOR', 'TIMEOUT', 'SYNC'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.6',
)
