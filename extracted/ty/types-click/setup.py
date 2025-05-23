from setuptools import setup

name = "types-click"
description = "Typing stubs for click"
long_description = '''
## Typing stubs for click

This is a PEP 561 type stub package for the `click` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `click`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/click. All fixes for
types and metadata should be contributed there.

*Note:* The `click` package includes type annotations or type stubs
since version 8.0. Please uninstall the `types-click`
package if you use this or a newer version.


See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `2445eddb4b67fdaa58ec7c2113ff1542021a6206`.
'''.lstrip()

setup(name=name,
      version="7.1.8",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      install_requires=[],
      packages=['click-stubs'],
      package_data={'click-stubs': ['__init__.pyi', '_termui_impl.pyi', 'core.pyi', 'decorators.pyi', 'exceptions.pyi', 'formatting.pyi', 'globals.pyi', 'parser.pyi', 'termui.pyi', 'testing.pyi', 'types.pyi', 'utils.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Typing :: Typed",
      ]
)
