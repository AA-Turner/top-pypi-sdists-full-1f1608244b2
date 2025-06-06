# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify it under
# the terms of the (LGPL) GNU Lesser General Public License as published by the
# Free Software Foundation; either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Library Lesser General Public License
# for more details at ( http://www.gnu.org/licenses/lgpl.html ).
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
# written by: Jurko Gospodnetić ( jurko.gospodnetic@pke.hr )

"""
Suds library transport related unit tests.

Implemented using the 'pytest' testing framework.

"""

if __name__ == "__main__":
    import testutils
    testutils.run_using_pytest(globals())

import suds
from suds.transport import Reply, Request, Transport
import suds.transport.options

import pytest

import sys


class TestBaseTransportClass:

    def test_members(self):
        t = Transport()
        assert t.options.__class__ is suds.transport.options.Options

    @pytest.mark.parametrize("method_name", ("open", "send"))
    def test_methods_should_be_abstract(self, monkeypatch, method_name):
        monkeypatch.delitem(locals(), "e", False)
        transport = Transport()
        f = getattr(transport, method_name)
        e = pytest.raises(Exception, f, "whatever").value
        try:
            assert e.__class__ is Exception
            assert str(e) == "not-implemented"
        finally:
            del e  # explicitly break circular reference chain in Python 3


class TestReply:

    @pytest.mark.parametrize(("code", "headers", "message"), (
        (1, {}, None),
        (1, {}, "ola"),
        (1, {}, b"ola"),
        (1, {}, object()),
        (1, {}, "\u0161u\u0107-mu\u0107 \u4E2D\u539F\u5343\n\u57CE"),
        (2, {"semper": "fi"}, "\u4E2D\u539F\u5343\n\u57CE")))
    def test_construction(self, code, headers, message):
        reply = Reply(code, headers, message)
        assert reply.code is code
        assert reply.headers is headers
        assert reply.message is message

    @pytest.mark.parametrize("message", [x.encode() for x in (
        "",
        "for a bitch it's haaaard...",
        """\
I'm here to kick ass,
and chew bubble gum...
and I'm all out of gum.""",
        "\u0161u\u0107-mu\u0107 pa o\u017Ee\u017Ei.. za 100 \u20AC\n\n"
            "with multiple\nlines...",
        "\n\n\n\n\n\n",
        "\u4E2D\u539F\u5343\u519B\u9010\u848B")])
    def test_string_representation(self, message):
        code = 17
        reply = Reply(code, {"aaa": 1}, message)
        expected = """\
CODE: %s
HEADERS: %s
MESSAGE:
%s""" % (code, reply.headers, message.decode("raw_unicode_escape"))
        assert str(reply) == expected


class TestRequest:

    @pytest.mark.parametrize("message", (
        None,
        "it's hard out here...",
        "\u57CE\u697C\u4E07\u4F17\u68C0\u9605"))
    def test_construct(self, message):
        # Always use the same URL as different ways to specify a Request's URL
        # are tested separately.
        url = "some://url"
        timeout = 10
        request = Request(url, message, timeout)
        assert request.url is url
        assert request.message is message
        assert request.headers == {}
        assert request.timeout == timeout

    def test_construct_with_no_message(self):
        request = Request("some://url")
        assert request.headers == {}
        assert request.message is None

    test_non_ASCII_URLs = [
        "\u4E2D\u539F\u5343\u519B\u9010\u848B",
        "\u57CE\u697C\u4E07\u4F17\u68C0\u9605"] + [
        url_prefix + url_suffix
            for url_prefix in ("", "Jurko")
            for url_suffix in (chr(128), chr(200), chr(1000))]
    @pytest.mark.parametrize("url",
        test_non_ASCII_URLs +  # unicode strings
        [x.encode() for x in test_non_ASCII_URLs])  # byte strings
    def test_non_ASCII_URL(self, url):
        """Transport Request should reject URLs with non-ASCII characters."""
        pytest.raises(UnicodeError, Request, url)

    @pytest.mark.parametrize(("url", "headers", "message"), (
        ("my URL", {}, ""),
        ("", {"aaa": "uf-uf"}, "for a bitch it's haaaard..."),
        ("http://rumple-fif/muka-laka-hiki", {"uno": "eins", "zwei": "due"},
            """\
I'm here to kick ass,
and chew bubble gum...
and I'm all out of gum."""),
        ("", {}, "\u0161u\u0107-mu\u0107 pa o\u017Ee\u017Ei.. za 100 "
            "\u20AC\n\nwith multiple\nlines..."),
        ("", {}, "\n\n\n\n\n\n"),
        ("", {}, "\u4E2D\u539F\u5343\u519B\u9010\u848B")))
    def test_string_representation_with_message(self, url, headers, message):
        for key, value in list(headers.items()):
            old_key = key
            if isinstance(key, str):
                key = key.encode()
                del headers[old_key]
            if isinstance(value, str):
                value = value.encode()
            headers[key] = value
        if isinstance(message, str):
            message = message.encode()
        request = Request(url, message)
        request.headers = headers
        expected = """\
URL: %s
HEADERS: %s
MESSAGE:
%s""" % (url, request.headers, message.decode("raw_unicode_escape"))
        assert str(request) == expected

    def test_string_representation_with_no_message(self):
        url = "look at my silly little URL"
        headers = {suds.byte_str("yuck"): suds.byte_str("ptooiii...")}
        request = Request(url)
        request.headers = headers
        expected = """\
URL: %s
HEADERS: %s""" % (url, request.headers)
        assert str(request) == expected

    test_URLs = [
        "",
        "http://host/path/name",
        "cogito://ergo/sum",
        "haleluya",
        "look  at  me flyyyyyyyy",
        chr(127),
        "Jurko" + chr(127)]
    @pytest.mark.parametrize("url", test_URLs + [
        url.encode("ascii") for url in test_URLs])
    def test_URL(self, url):
        """
        Transport Request accepts its URL as either a byte or a unicode string.

        Internally URL information is kept as the native Python str type.

        """
        request = Request(url)
        assert isinstance(request.url, str)
        if url.__class__ is str:
            assert request.url is url
        else:
            assert request.url == url.decode("ascii")

    test_URLs = [chr(0), "Jurko" + chr(0)] if sys.version_info >= (3, 8) else []  # "https://bugs.python.org/issue32745"
    @pytest.mark.parametrize("url", test_URLs + [
        url.encode("ascii") for url in test_URLs])
    def test_URL_null_bytes(self, url):
        """
        Transport Request accepts its URL as either a byte or a unicode string.

        Internally URL information is kept as the native Python str type.

        """
        request = Request(url)
        assert isinstance(request.url, str)
        if url.__class__ is str:
            assert request.url is url
        else:
            assert request.url == url.decode("ascii")
