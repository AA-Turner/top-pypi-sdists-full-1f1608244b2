from setuptools import setup

name = "types-pyaudio"
description = "Typing stubs for pyaudio"
long_description = '''
## Typing stubs for pyaudio

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the `pyaudio` package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`pyaudio`.

This version of `types-pyaudio` aims to provide accurate annotations
for `pyaudio==0.2.*`.
The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/pyaudio. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `77d6947479a7ba2cddc6b50d5600a941a84ca4d4` and was tested
with mypy 1.10.0, pyright 1.1.363, and
pytype 2024.4.11.
'''.lstrip()

setup(name=name,
      version="0.2.16.20240516",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/pyaudio.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['pyaudio-stubs'],
      package_data={'pyaudio-stubs': ['__init__.pyi', 'METADATA.toml', 'py.typed']},
      license="Apache-2.0 license",
      python_requires=">=3.8",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
