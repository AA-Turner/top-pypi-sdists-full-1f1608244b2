"""
Code modified from:
https://github.com/r0wb0t/markdown-urlize

A more liberal autolinker

Inspired by Django's urlize function.

Positive examples:

>>> import markdown
>>> md = markdown.Markdown(extensions=['urlize'])

>>> md.convert('http://example.com/')
u'<p><a href="http://example.com/">http://example.com/</a></p>'

>>> md.convert('go to http://example.com')
u'<p>go to <a href="http://example.com">http://example.com</a></p>'

>>> md.convert('example.com')
u'<p><a href="http://example.com">example.com</a></p>'

>>> md.convert('example.net')
u'<p><a href="http://example.net">example.net</a></p>'

>>> md.convert('www.example.us')
u'<p><a href="http://www.example.us">www.example.us</a></p>'

>>> md.convert('(www.example.us/path/?name=val)')
u'<p>(<a href="http://www.example.us/path/?name=val">www.example.us/path/?name=val</a>)</p>'

>>> md.convert('go to <http://example.com> now!')
u'<p>go to <a href="http://example.com">http://example.com</a> now!</p>'

Negative examples:

>>> md.convert('del.icio.us')
u'<p>del.icio.us</p>'

"""

import markdown
import re

# Taken from Django trunk 2f121dfe635b3f497fe1fe03bc8eb97cdf5083b3
# https://github.com/django/django/blob/master/django/core/validators.py#L47
URLIZE_RE = (
    r'((?:(?:http|ftp)s?://|www\.)' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
    r'localhost|' # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+))'
)


class UrlizePattern(markdown.inlinepatterns.Pattern):

    def __init__(self, pattern, markdown_instance=None):
        markdown.inlinepatterns.Pattern.__init__(self, pattern, md=markdown_instance)
        self.compiled_re = re.compile("^(.*?)%s(.*?)$" % pattern,
                                      re.DOTALL | re.UNICODE | re.IGNORECASE)

    """ Return a link Element given an autolink (`http://example/com`). """
    def handleMatch(self, m):
        url = m.group(2)

        if url.startswith('<'):
            url = url[1:-1]

        text = url

        if not url.split('://')[0] in ('http','https','ftp'):
            if '@' in url and not '/' in url:
                url = 'mailto:' + url
            else:
                url = 'http://' + url

        icon = xml.etree.ElementTree.Element("span")
        icon.set('class', 'icon-globe')

        span_text = xml.etree.ElementTree.Element("span")
        span_text.text = markdown.util.AtomicString(" " + text)
        el = xml.etree.ElementTree.Element("a")
        el.set('href', url)
        el.set('target', '_blank')
        el.extend([icon, span_text])
        return el


class UrlizeExtension(markdown.Extension):
    """ Urlize Extension for Python-Markdown. """

    def extendMarkdown(self, md):
        """ Replace autolink with UrlizePattern """
        md.inlinePatterns['autolink'] = UrlizePattern(URLIZE_RE, md)


def makeExtension(**kwargs):
    return UrlizeExtension(**kwargs)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
