#! /usr/bin/env python3
# $Id: test__init__.py 9277 2022-11-26 23:15:13Z milde $
# Author: Günter Milde <milde@users.sf.net>,
# :License: Released under the terms of the `2-Clause BSD license`_, in short:
#
#    Copying and distribution of this file, with or without modification,
#    are permitted in any medium without royalty provided the copyright
#    notice and this notice are preserved.
#    This file is offered as-is, without any warranty.
#
# .. _2-Clause BSD license: https://opensource.org/licenses/BSD-2-Clause
"""
Test module for `docutils.parsers.rst.directives`.
"""

from pathlib import Path
import sys
import unittest

if __name__ == '__main__':
    # prepend the "docutils root" to the Python library path
    # so we import the local `docutils` package.
    sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

import docutils
import docutils.parsers.null
from docutils.parsers.rst import directives


class DirectiveOptionConversionTestCase(unittest.TestCase):

    def test_flag(self):
        # Raise error when there is an argument:
        self.assertEqual(None, directives.flag(''))
        self.assertRaises(ValueError, directives.flag, 'alles')

    def test_unchanged_required(self):
        # Raise error when there is no argument:
        self.assertRaises(ValueError, directives.unchanged_required, None)
        self.assertEqual(3, directives.unchanged_required(3))

    def test_unchanged(self):
        self.assertEqual('', directives.unchanged(''))
        self.assertTrue('something' == directives.unchanged('something'))
        self.assertEqual(3, directives.unchanged(3))
        self.assertEqual([3], directives.unchanged([3]))

    # TODO: 13 more directive option conversion functions.

    def test_parser_name(self):
        self.assertEqual(directives.parser_name(None), None)
        self.assertEqual(directives.parser_name('null'),
                         docutils.parsers.null.Parser)
        self.assertEqual(directives.parser_name('rst'),
                         docutils.parsers.rst.Parser)
        self.assertRaises(ValueError, directives.parser_name, 'fantasy')


if __name__ == '__main__':
    unittest.main()
