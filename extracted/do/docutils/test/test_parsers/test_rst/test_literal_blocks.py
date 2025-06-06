#! /usr/bin/env python3

# $Id: test_literal_blocks.py 9425 2023-06-30 14:56:47Z milde $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
Tests for states.py.
"""

from pathlib import Path
import sys
import unittest

if __name__ == '__main__':
    # prepend the "docutils root" to the Python library path
    # so we import the local `docutils` package.
    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

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

totest['indented_literal_blocks'] = [
["""\
A paragraph::

    A literal block.
""",
"""\
<document source="test data">
    <paragraph>
        A paragraph:
    <literal_block xml:space="preserve">
        A literal block.
"""],
["""\
A paragraph with a space after the colons:: \n\

    A literal block.
""",
"""\
<document source="test data">
    <paragraph>
        A paragraph with a space after the colons:
    <literal_block xml:space="preserve">
        A literal block.
"""],
["""\
A paragraph::

    A literal block.

Another paragraph::

    Another literal block.
    With two blank lines following.


A final paragraph.
""",
"""\
<document source="test data">
    <paragraph>
        A paragraph:
    <literal_block xml:space="preserve">
        A literal block.
    <paragraph>
        Another paragraph:
    <literal_block xml:space="preserve">
        Another literal block.
        With two blank lines following.
    <paragraph>
        A final paragraph.
"""],
["""\
A paragraph
on more than
one line::

    A literal block.
""",
"""\
<document source="test data">
    <paragraph>
        A paragraph
        on more than
        one line:
    <literal_block xml:space="preserve">
        A literal block.
"""],
["""\
A paragraph
on more than
one line::
    A literal block
    with no blank line above.
""",
"""\
<document source="test data">
    <paragraph>
        A paragraph
        on more than
        one line:
    <system_message level="3" line="4" source="test data" type="ERROR">
        <paragraph>
            Unexpected indentation.
    <literal_block xml:space="preserve">
        A literal block
        with no blank line above.
"""],
["""\
A paragraph::

    A literal block.
no blank line
""",
"""\
<document source="test data">
    <paragraph>
        A paragraph:
    <literal_block xml:space="preserve">
        A literal block.
    <system_message level="2" line="4" source="test data" type="WARNING">
        <paragraph>
            Literal block ends without a blank line; unexpected unindent.
    <paragraph>
        no blank line
"""],
[r"""
A paragraph\\::

    A literal block.

A paragraph\::

    Not a literal block.
""",
r"""<document source="test data">
    <paragraph>
        A paragraph\:
    <literal_block xml:space="preserve">
        A literal block.
    <paragraph>
        A paragraph::
    <block_quote>
        <paragraph>
            Not a literal block.
"""],
[r"""
\\::

    A literal block.

\::

    Not a literal block.
""",
r"""<document source="test data">
    <paragraph>
        \:
    <literal_block xml:space="preserve">
        A literal block.
    <paragraph>
        ::
    <block_quote>
        <paragraph>
            Not a literal block.
"""],
["""\
A paragraph: ::

    A literal block.
""",
"""\
<document source="test data">
    <paragraph>
        A paragraph:
    <literal_block xml:space="preserve">
        A literal block.
"""],
["""\
A paragraph:

::

    A literal block.
""",
"""\
<document source="test data">
    <paragraph>
        A paragraph:
    <literal_block xml:space="preserve">
        A literal block.
"""],
["""\
A paragraph:
::

    A literal block.
""",
"""\
<document source="test data">
    <system_message level="1" line="2" source="test data" type="INFO">
        <paragraph>
            Possible title underline, too short for the title.
            Treating it as ordinary text because it's so short.
    <paragraph>
        A paragraph:
    <literal_block xml:space="preserve">
        A literal block.
"""],
["""\
A paragraph:

::

    A literal block.
""",
"""\
<document source="test data">
    <paragraph>
        A paragraph:
    <literal_block xml:space="preserve">
        A literal block.
"""],
["""\
A paragraph::

Not a literal block.
""",
"""\
<document source="test data">
    <paragraph>
        A paragraph:
    <system_message level="2" line="3" source="test data" type="WARNING">
        <paragraph>
            Literal block expected; none found.
    <paragraph>
        Not a literal block.
"""],
["""\
A paragraph::

    A wonky literal block.
  Literal line 2.

    Literal line 3.
""",
"""\
<document source="test data">
    <paragraph>
        A paragraph:
    <literal_block xml:space="preserve">
          A wonky literal block.
        Literal line 2.
        \n\
          Literal line 3.
"""],
["""\
EOF, even though a literal block is indicated::
""",
"""\
<document source="test data">
    <paragraph>
        EOF, even though a literal block is indicated:
    <system_message level="2" line="2" source="test data" type="WARNING">
        <paragraph>
            Literal block expected; none found.
"""],
]

totest['quoted_literal_blocks'] = [
["""\
A paragraph::

> A literal block.
""",
"""\
<document source="test data">
    <paragraph>
        A paragraph:
    <literal_block xml:space="preserve">
        > A literal block.
"""],
["""\
A paragraph::


> A literal block.
""",
"""\
<document source="test data">
    <paragraph>
        A paragraph:
    <literal_block xml:space="preserve">
        > A literal block.
"""],
["""\
A paragraph::

> A literal block.
> Line 2.
""",
"""\
<document source="test data">
    <paragraph>
        A paragraph:
    <literal_block xml:space="preserve">
        > A literal block.
        > Line 2.
"""],
["""\
A paragraph::

> A literal block.
  Indented line.
""",
"""\
<document source="test data">
    <paragraph>
        A paragraph:
    <literal_block xml:space="preserve">
        > A literal block.
    <system_message level="3" line="4" source="test data" type="ERROR">
        <paragraph>
            Unexpected indentation.
    <block_quote>
        <paragraph>
            Indented line.
"""],
["""\
A paragraph::

> A literal block.
Text.
""",
"""\
<document source="test data">
    <paragraph>
        A paragraph:
    <literal_block xml:space="preserve">
        > A literal block.
    <system_message level="3" line="4" source="test data" type="ERROR">
        <paragraph>
            Inconsistent literal block quoting.
    <paragraph>
        Text.
"""],
["""\
A paragraph::

> A literal block.
$ Inconsistent line.
""",
"""\
<document source="test data">
    <paragraph>
        A paragraph:
    <literal_block xml:space="preserve">
        > A literal block.
    <system_message level="3" line="4" source="test data" type="ERROR">
        <paragraph>
            Inconsistent literal block quoting.
    <paragraph>
        $ Inconsistent line.
"""],
]


if __name__ == '__main__':
    unittest.main()
