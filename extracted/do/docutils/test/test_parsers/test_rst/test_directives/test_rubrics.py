#! /usr/bin/env python3

# $Id: test_rubrics.py 9425 2023-06-30 14:56:47Z milde $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
Tests for the "rubric" directive.
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

totest['rubrics'] = [
["""\
.. rubric:: This is a rubric
""",
"""\
<document source="test data">
    <rubric>
        This is a rubric
"""],
["""\
.. rubric::
.. rubric:: A rubric has no content

   Invalid content
""",
"""\
<document source="test data">
    <system_message level="3" line="1" source="test data" type="ERROR">
        <paragraph>
            Error in "rubric" directive:
            1 argument(s) required, 0 supplied.
        <literal_block xml:space="preserve">
            .. rubric::
    <system_message level="3" line="2" source="test data" type="ERROR">
        <paragraph>
            Error in "rubric" directive:
            no content permitted.
        <literal_block xml:space="preserve">
            .. rubric:: A rubric has no content
            \n\
               Invalid content
"""],
["""\
.. rubric:: A rubric followed by a block quote
..

   Block quote
""",
"""\
<document source="test data">
    <rubric>
        A rubric followed by a block quote
    <comment xml:space="preserve">
    <block_quote>
        <paragraph>
            Block quote
"""],
["""\
.. rubric:: A Rubric
   :class: foo bar
   :name: Foo Rubric
""",
"""\
<document source="test data">
    <rubric classes="foo bar" ids="foo-rubric" names="foo\\ rubric">
        A Rubric
"""],
]


if __name__ == '__main__':
    unittest.main()
