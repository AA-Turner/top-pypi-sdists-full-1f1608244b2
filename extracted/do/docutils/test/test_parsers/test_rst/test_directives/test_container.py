#! /usr/bin/env python3

# $Id: test_container.py 9425 2023-06-30 14:56:47Z milde $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
Tests for the 'container' directive from body.py.
"""

from pathlib import Path
import sys
import unittest

if __name__ == '__main__':
    # prepend the "docutils root" to the Python library path
    # so we import the local `docutils` package.
    sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

from docutils.frontend import get_default_settings
from docutils.parsers.rst import Parser
from docutils.utils import new_document


class ParserTestCase(unittest.TestCase):
    def test_parser(self):
        parser = Parser()
        settings = get_default_settings(Parser)
        settings.warning_stream = ''
        for name, cases in totest.items():
            for casenum, (case_input, case_expected) in enumerate(cases):
                with self.subTest(id=f'totest[{name!r}][{casenum}]'):
                    document = new_document('test data', settings.copy())
                    parser.parse(case_input, document)
                    output = document.pformat()
                    self.assertEqual(case_expected, output)


totest = {}

totest['container'] = [
["""\
.. container::

   "container" is a generic element, an extension mechanism for
   users & applications.

   Containers may contain arbitrary body elements.
""",
"""\
<document source="test data">
    <container>
        <paragraph>
            "container" is a generic element, an extension mechanism for
            users & applications.
        <paragraph>
            Containers may contain arbitrary body elements.
"""],
["""\
.. container:: custom

   Some text.
""",
"""\
<document source="test data">
    <container classes="custom">
        <paragraph>
            Some text.
"""],
["""\
.. container:: one two three
   four

   Multiple classes.

   Multi-line argument.

   Multiple paragraphs in the container.
""",
"""\
<document source="test data">
    <container classes="one two three four">
        <paragraph>
            Multiple classes.
        <paragraph>
            Multi-line argument.
        <paragraph>
            Multiple paragraphs in the container.
"""],
["""\
.. container::
   :name: my name

   The name argument allows hyperlinks to `my name`_.
""",
"""\
<document source="test data">
    <container ids="my-name" names="my\\ name">
        <paragraph>
            The name argument allows hyperlinks to \n\
            <reference name="my name" refname="my name">
                my name
            .
"""],
]


if __name__ == '__main__':
    unittest.main()
