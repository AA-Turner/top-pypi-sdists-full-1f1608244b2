##############################################################################
#
# Copyright (c) 2001, 2002 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""
Parse HTML and compile to :class:`~.TALInterpreter` intermediate code, using
a :class:`~.TALGenerator`.
"""
from html.parser import HTMLParser

from zope.tal.taldefs import ZOPE_I18N_NS
from zope.tal.taldefs import ZOPE_METAL_NS
from zope.tal.taldefs import ZOPE_TAL_NS
from zope.tal.taldefs import I18NError
from zope.tal.taldefs import METALError
from zope.tal.taldefs import TALError
from zope.tal.talgenerator import TALGenerator


class HTMLParseError(Exception):

    def __init__(self, msg, position=(None, None)):
        Exception.__init__(self)
        assert msg
        self.msg = msg
        self.lineno = position[0]
        self.offset = position[1]

    def __str__(self):
        result = self.msg
        if self.lineno is not None:
            result = result + ", at line %d" % self.lineno
        if self.offset is not None:
            result = result + ", column %d" % (self.offset + 1)
        return result


_html_parser_extras = {}
if 'convert_charrefs' in HTMLParser.__init__.__code__.co_names:
    _html_parser_extras['convert_charrefs'] = False  # pragma: NO COVER

#: List of Boolean attributes in HTML that may be given in
#: minimized form (e.g. ``<img ismap>`` rather than ``<img ismap="">``)
#: From http://www.w3.org/TR/xhtml1/#guidelines (C.10)
BOOLEAN_HTML_ATTRS = frozenset([
    "compact", "nowrap", "ismap", "declare", "noshade", "checked",
    "disabled", "readonly", "multiple", "selected", "noresize",
    "defer"
])

#: List of HTML tags with an empty content model; these are
#: rendered in minimized form, e.g. ``<img />``.
#: From http://www.w3.org/TR/xhtml1/#dtds
EMPTY_HTML_TAGS = frozenset([
    "base", "meta", "link", "hr", "br", "param", "img", "area",
    "input", "col", "basefont", "isindex", "frame",
])

#: List of HTML elements that close open paragraph-level elements
#: and are themselves paragraph-level.
PARA_LEVEL_HTML_TAGS = frozenset([
    "h1", "h2", "h3", "h4", "h5", "h6", "p",
])

#: Tags that automatically close other tags.
BLOCK_CLOSING_TAG_MAP = {
    "tr": frozenset(["tr", "td", "th"]),
    "td": frozenset(["td", "th"]),
    "th": frozenset(["td", "th"]),
    "li": frozenset(["li"]),
    "dd": frozenset(["dd", "dt"]),
    "dt": frozenset(["dd", "dt"]),
}

#: List of HTML tags that denote larger sections than paragraphs.
BLOCK_LEVEL_HTML_TAGS = frozenset([
    "blockquote", "table", "tr", "th", "td", "thead", "tfoot", "tbody",
    "noframe", "ul", "ol", "li", "dl", "dt", "dd", "div", "nav",
])

#: Section level HTML tags
SECTION_LEVEL_HTML_TAGS = PARA_LEVEL_HTML_TAGS.union(BLOCK_LEVEL_HTML_TAGS)

TIGHTEN_IMPLICIT_CLOSE_TAGS = PARA_LEVEL_HTML_TAGS.union(BLOCK_CLOSING_TAG_MAP)


class NestingError(HTMLParseError):
    """Exception raised when elements aren't properly nested."""

    def __init__(self, tagstack, endtag, position=(None, None)):
        self.endtag = endtag
        if tagstack:
            if len(tagstack) == 1:
                msg = ('Open tag <%s> does not match close tag </%s>'
                       % (tagstack[0], endtag))
            else:
                msg = ('Open tags <%s> do not match close tag </%s>'
                       % ('>, <'.join(tagstack), endtag))
        else:
            msg = 'No tags are open to match </%s>' % endtag
        HTMLParseError.__init__(self, msg, position)


class EmptyTagError(NestingError):
    """Exception raised when empty elements have an end tag."""

    def __init__(self, tag, position=(None, None)):
        self.tag = tag
        msg = 'Close tag </%s> should be removed' % tag
        HTMLParseError.__init__(self, msg, position)


class OpenTagError(NestingError):
    """Exception raised when a tag is not allowed in another tag."""

    def __init__(self, tagstack, tag, position=(None, None)):
        self.tag = tag
        msg = f'Tag <{tag}> is not allowed in <{tagstack[-1]}>'
        HTMLParseError.__init__(self, msg, position)


class HTMLTALParser(HTMLParser):
    """
    Parser for HTML.

    After you call either :meth:`parseFile` and :meth:`parseString`
    you can retrieve the compiled program using :meth:`getCode`.
    """

    # External API

    def __init__(self, gen=None):
        """
        :keyword TALGenerator gen: The configured (with an expression compiler)
            code generator to use. If one is not given, a default will be used.
        """
        HTMLParser.__init__(self, **_html_parser_extras)
        if gen is None:
            gen = TALGenerator(xml=0)
        self.gen = gen
        self.tagstack = []
        self.nsstack = []
        self.nsdict = {
            'tal': ZOPE_TAL_NS,
            'metal': ZOPE_METAL_NS,
            'i18n': ZOPE_I18N_NS,
        }

    def parseFile(self, file):
        """Parse data in the given file."""
        with open(file) as f:
            data = f.read()

        try:
            self.parseString(data)
        except TALError as e:
            e.setFile(file)
            raise

    def parseString(self, data):
        """Parse data in the given string."""
        self.feed(data)
        self.close()
        while self.tagstack:
            self.implied_endtag(self.tagstack[-1], 2)
        assert self.nsstack == [], self.nsstack

    def getCode(self):
        """
        After parsing, this returns ``(program, macros)``.
        """
        return self.gen.getCode()

    # Overriding HTMLParser methods

    def handle_starttag(self, tag, attrs):
        self.close_para_tags(tag)
        self.scan_xmlns(attrs)
        tag, attrlist, taldict, metaldict, i18ndict \
            = self.process_ns(tag, attrs)
        if tag in EMPTY_HTML_TAGS and "content" in taldict:
            raise TALError(
                "empty HTML tags cannot use tal:content: %s" % repr(tag),
                self.getpos())
        # Support for inline Python code.
        if tag == 'script':
            type_attr = [a for a in attrlist if a[0] == "type"]
            if type_attr and type_attr[0][1].startswith('text/server-'):
                attrlist.remove(type_attr[0])
                taldict = {'script': type_attr[0][1], 'omit-tag': ''}
        self.tagstack.append(tag)
        self.gen.emitStartElement(tag, attrlist, taldict, metaldict, i18ndict,
                                  self.getpos())
        if tag in EMPTY_HTML_TAGS:
            self.implied_endtag(tag, -1)

    def handle_startendtag(self, tag, attrs):
        self.close_para_tags(tag)
        self.scan_xmlns(attrs)
        tag, attrlist, taldict, metaldict, i18ndict \
            = self.process_ns(tag, attrs)
        if "content" in taldict:
            if tag in EMPTY_HTML_TAGS:
                raise TALError(
                    "empty HTML tags cannot use tal:content: %s" % repr(tag),
                    self.getpos())
            self.gen.emitStartElement(tag, attrlist, taldict, metaldict,
                                      i18ndict, self.getpos())
            self.gen.emitEndElement(tag, implied=-1, position=self.getpos())
        else:
            self.gen.emitStartElement(tag, attrlist, taldict, metaldict,
                                      i18ndict, self.getpos(), isend=1)
        self.pop_xmlns()

    def handle_endtag(self, tag):
        if self.tagstack and self.tagstack[-1] == 'script' and tag != 'script':
            self.handle_data('</%s>' % tag)
            return
        if tag in EMPTY_HTML_TAGS:
            # </img> etc. in the source is an error
            raise EmptyTagError(tag, self.getpos())
        self.close_enclosed_tags(tag)
        self.gen.emitEndElement(tag, position=self.getpos())
        self.pop_xmlns()
        self.tagstack.pop()

    def close_para_tags(self, tag):
        if tag in EMPTY_HTML_TAGS:
            return
        close_to = -1
        if tag in BLOCK_CLOSING_TAG_MAP:
            blocks_to_close = BLOCK_CLOSING_TAG_MAP[tag]
            for i, t in enumerate(self.tagstack):
                if t in blocks_to_close:
                    if close_to == -1:
                        close_to = i
                elif t in BLOCK_LEVEL_HTML_TAGS:
                    close_to = -1
        elif tag in SECTION_LEVEL_HTML_TAGS:
            for i in range(len(self.tagstack) - 1, -1, -1):
                closetag = self.tagstack[i]
                if closetag in BLOCK_LEVEL_HTML_TAGS:
                    break
                elif closetag in PARA_LEVEL_HTML_TAGS:
                    if closetag != "p":
                        raise OpenTagError(self.tagstack, tag, self.getpos())
                    close_to = i
        if close_to >= 0:
            while len(self.tagstack) > close_to:
                self.implied_endtag(self.tagstack[-1], 1)

    def close_enclosed_tags(self, tag):
        if tag not in self.tagstack:
            raise NestingError(self.tagstack, tag, self.getpos())
        while tag != self.tagstack[-1]:
            self.implied_endtag(self.tagstack[-1], 1)
        assert self.tagstack[-1] == tag

    def implied_endtag(self, tag, implied):
        assert tag == self.tagstack[-1]
        assert implied in (-1, 1, 2)
        isend = (implied < 0)
        if tag in TIGHTEN_IMPLICIT_CLOSE_TAGS:
            # Pick out trailing whitespace from the program, and
            # insert the close tag before the whitespace.
            white = self.gen.unEmitWhitespace()
        else:
            white = None
        self.gen.emitEndElement(tag, isend=isend, implied=implied,
                                position=self.getpos())
        if white:
            self.gen.emitRawText(white)
        self.tagstack.pop()
        self.pop_xmlns()

    def handle_charref(self, name):
        self.gen.emitRawText("&#%s;" % name)

    def handle_entityref(self, name):
        self.gen.emitRawText("&%s;" % name)

    def handle_data(self, data):
        self.gen.emitRawText(data)

    def handle_comment(self, data):
        self.gen.emitRawText("<!--%s-->" % data)

    def handle_decl(self, data):
        self.gen.emitRawText("<!%s>" % data)

    def handle_pi(self, data):
        self.gen.emitRawText("<?%s>" % data)

    # Internal thingies

    def scan_xmlns(self, attrs):
        nsnew = {}
        for key, value in attrs:
            if key.startswith("xmlns:"):
                nsnew[key[6:]] = value
        self.nsstack.append(self.nsdict)
        if nsnew:
            self.nsdict = self.nsdict.copy()
            self.nsdict.update(nsnew)

    def pop_xmlns(self):
        self.nsdict = self.nsstack.pop()

    _namespaces = {
        ZOPE_TAL_NS: "tal",
        ZOPE_METAL_NS: "metal",
        ZOPE_I18N_NS: "i18n",
    }

    def fixname(self, name):
        if ':' in name:
            prefix, suffix = name.split(':', 1)
            if prefix == 'xmlns':
                nsuri = self.nsdict.get(suffix)
                if nsuri in self._namespaces:
                    return name, name, prefix
            else:
                nsuri = self.nsdict.get(prefix)
                if nsuri in self._namespaces:
                    return name, suffix, self._namespaces[nsuri]
        return name, name, 0

    def process_ns(self, name, attrs):
        attrlist = []
        taldict = {}
        metaldict = {}
        i18ndict = {}
        name, namebase, namens = self.fixname(name)
        for item in attrs:
            key, value = item
            key, keybase, keyns = self.fixname(key)
            ns = keyns or namens  # default to tag namespace
            if ns and ns != 'unknown':
                item = (key, value, ns)
            if ns == 'tal':
                if keybase in taldict:
                    raise TALError("duplicate TAL attribute " +
                                   repr(keybase), self.getpos())
                taldict[keybase] = value
            elif ns == 'metal':
                if keybase in metaldict:
                    raise METALError("duplicate METAL attribute " +
                                     repr(keybase), self.getpos())
                metaldict[keybase] = value
            elif ns == 'i18n':
                if keybase in i18ndict:
                    raise I18NError("duplicate i18n attribute " +
                                    repr(keybase), self.getpos())
                i18ndict[keybase] = value
            attrlist.append(item)
        if namens in ('metal', 'tal', 'i18n'):
            taldict['tal tag'] = namens
        return name, attrlist, taldict, metaldict, i18ndict
