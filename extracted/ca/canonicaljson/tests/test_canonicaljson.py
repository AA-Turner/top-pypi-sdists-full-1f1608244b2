# Copyright 2015 OpenMarket Ltd
# Copyright 2018 New Vector Ltd
# Copyright 2022 The Matrix.org Foundation C.I.C.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from unittest.mock import Mock

from math import inf, nan

from canonicaljson import (
    encode_canonical_json,
    encode_pretty_printed_json,
    iterencode_canonical_json,
    iterencode_pretty_printed_json,
    register_preserialisation_callback,
)

import unittest


class TestCanonicalJson(unittest.TestCase):
    def test_encode_canonical(self) -> None:
        self.assertEqual(encode_canonical_json({}), b"{}")

        # ctrl-chars should be encoded.
        self.assertEqual(
            encode_canonical_json(u"text\u0003\r\n"),
            b'"text\\u0003\\r\\n"',
        )

        # quotes and backslashes should be escaped.
        self.assertEqual(
            encode_canonical_json(r'"\ test'),
            b'"\\"\\\\ test"',
        )

        # non-ascii should come out utf8-encoded.
        self.assertEqual(
            encode_canonical_json({u"la merde amusée": u"💩"}),
            b'{"la merde amus\xc3\xa9e":"\xF0\x9F\x92\xA9"}',
        )

        # so should U+2028 and U+2029
        self.assertEqual(
            encode_canonical_json({u"spaces": u"\u2028 \u2029"}),
            b'{"spaces":"\xe2\x80\xa8 \xe2\x80\xa9"}',
        )

        # but we need to watch out for 'u1234' after backslash, which should
        # get encoded to an escaped backslash, followed by u1234
        self.assertEqual(
            encode_canonical_json(u"\\u1234"),
            b'"\\\\u1234"',
        )

        # Iteratively encoding should work.
        self.assertEqual(list(iterencode_canonical_json({})), [b"{}"])

    def test_ascii(self) -> None:
        """
        Ensure the proper ASCII characters are escaped.

        See https://matrix.org/docs/spec/appendices#grammar.
        """
        # Some characters go to their common shorthands.
        escaped = {
            0x08: b'"\\b"',
            0x09: b'"\\t"',
            0x0A: b'"\\n"',
            0x0C: b'"\\f"',
            0x0D: b'"\\r"',
            0x22: b'"\\""',
            0x5C: b'"\\\\"',
        }
        for c, expected in escaped.items():
            self.assertEqual(encode_canonical_json(chr(c)), expected)

        # Others go to the \uXXXX.
        hex_escaped = list(range(0x08)) + [0x0B] + list(range(0x0E, 0x20))
        for c in hex_escaped:
            self.assertEqual(encode_canonical_json(chr(c)), b'"\\u00%02x"' % (c,))

        # And other characters are passed unescaped.
        unescaped = [0x20, 0x21] + list(range(0x23, 0x5C)) + list(range(0x5D, 0x7E))
        for c in unescaped:
            s = chr(c)
            self.assertEqual(encode_canonical_json(s), b'"' + s.encode("ascii") + b'"')

    def test_encode_pretty_printed(self) -> None:
        self.assertEqual(encode_pretty_printed_json({}), b"{}")
        self.assertEqual(list(iterencode_pretty_printed_json({})), [b"{}"])

        # non-ascii should come out utf8-encoded.
        self.assertEqual(
            encode_pretty_printed_json({u"la merde amusée": u"💩"}),
            b'{\n    "la merde amus\xc3\xa9e": "\xF0\x9F\x92\xA9"\n}',
        )

    def test_unknown_type(self) -> None:
        class Unknown(object):
            pass

        unknown_object = Unknown()
        with self.assertRaises(Exception):
            encode_canonical_json(unknown_object)

        with self.assertRaises(Exception):
            encode_pretty_printed_json(unknown_object)

    def test_invalid_float_values(self) -> None:
        """Infinity/-Infinity/NaN are not allowed in canonicaljson."""

        with self.assertRaises(ValueError):
            encode_canonical_json(inf)

        with self.assertRaises(ValueError):
            encode_pretty_printed_json(inf)

        with self.assertRaises(ValueError):
            encode_canonical_json(-inf)

        with self.assertRaises(ValueError):
            encode_pretty_printed_json(-inf)

        with self.assertRaises(ValueError):
            encode_canonical_json(nan)

        with self.assertRaises(ValueError):
            encode_pretty_printed_json(nan)

    def test_encode_unknown_class_raises(self) -> None:
        class C:
            pass

        with self.assertRaises(Exception):
            encode_canonical_json(C())

    def test_preserialisation_callback(self) -> None:
        class C:
            pass

        # Naughty: this alters the global state of the module. However this
        # `C` class is limited to this test only, so this shouldn't affect
        # other types and other tests.
        register_preserialisation_callback(C, lambda c: "I am a C instance")

        result = encode_canonical_json(C())
        self.assertEqual(result, b'"I am a C instance"')

    def test_cannot_register_preserialisation_callback_for_object(self) -> None:
        with self.assertRaises(Exception):
            register_preserialisation_callback(
                object, lambda c: "shouldn't be able to do this"
            )

    def test_most_recent_preserialisation_callback_called(self) -> None:
        class C:
            pass

        callback1 = Mock(return_value="callback 1 was called")
        callback2 = Mock(return_value="callback 2 was called")

        # Naughty: this alters the global state of the module. However this
        # `C` class is limited to this test only, so this shouldn't affect
        # other types and other tests.
        register_preserialisation_callback(C, callback1)
        register_preserialisation_callback(C, callback2)

        encode_canonical_json(C())

        callback1.assert_not_called()
        callback2.assert_called_once()
