"""
Graphviz extensions for Markdown.
Renders the output inline, eliminating the need to configure an output
directory.

Supports outputs types of SVG and PNG. The output will be taken from the
filename specified in the tag. Example:

{% dot attack_plan.svg
    digraph G {
        rankdir=LR
        Earth [peripheries=2]
        Mars
        Earth -> Mars
    }
%}

Requires the graphviz library (http://www.graphviz.org/) and python 3

Inspired by jawher/markdown-dot (https://github.com/jawher/markdown-dot)
Forked from sprin/markdown-inline-graphviz (https://github.com/sprin/markdown-inline-graphviz
"""

import re
import markdown
import subprocess
import base64

# Global vars
BLOCK_RE_CURLY_BRACKET = re.compile(
        r'^{%[ ]* (?P<command>\w+)\s+(?P<filename>[^\s]+)\s*\n(?P<content>.*?)%}\s*$',
    re.MULTILINE | re.DOTALL)

BLOCK_RE_GRAVE_ACCENT = re.compile(
        r'^```graphviz[ ]* (?P<command>\w+)\s+(?P<filename>[^\s]+)\s*\n(?P<content>.*?)```\s*$',
    re.MULTILINE | re.DOTALL)

# Command whitelist
SUPPORTED_COMMAMDS = ['dot', 'neato', 'fdp', 'sfdp', 'twopi', 'circo']


class InlineGraphvizExtension(markdown.Extension):

    def extendMarkdown(self, md):
        """ Add InlineGraphvizPreprocessor to the Markdown instance. """
        md.registerExtension(self)
        md.preprocessors.register(
            InlineGraphvizPreprocessor(md), 'graphviz_block', 40
        )


class InlineGraphvizPreprocessor(markdown.preprocessors.Preprocessor):

    def __init__(self, md):
        super(InlineGraphvizPreprocessor, self).__init__(md)

    def run(self, lines):
        """ Match and generate dot code blocks."""

        text = "\n".join(lines)
        while 1:
            m = BLOCK_RE_CURLY_BRACKET.search(text) if BLOCK_RE_CURLY_BRACKET.search(text) else BLOCK_RE_GRAVE_ACCENT.search(text)
            if m:
                command = m.group('command')
                # Whitelist command, prevent command injection.
                if command not in SUPPORTED_COMMAMDS:
                    break
                filename = m.group('filename')
                content = m.group('content')
                filetype = filename[filename.rfind('.')+1:]

                args = [command, '-T'+filetype]
                try:
                    proc = subprocess.Popen(
                        args,
                        stdin=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        stdout=subprocess.PIPE)
                    proc.stdin.write(content.encode('utf-8'))

                    output, err = proc.communicate()

                    if filetype == 'svg':
                        data_url_filetype = 'svg+xml'
                        encoding = 'utf-8'
                        img = output.decode(encoding)

                    if filetype == 'png':
                        data_url_filetype = 'png'
                        encoding = 'base64'
                        output = base64.b64encode(output).decode('utf-8')
                        data_path = "data:image/%s;%s,%s" % (
                            data_url_filetype,
                            encoding,
                            output)
                        img = "![" + filename + "](" + data_path + ")"

                    text = '%s\n%s\n%s' % (
                        text[:m.start()], img, text[m.end():])

                except Exception as e:
                        err = str(e) + ' : ' + str(args)
                        return (
                            '<pre>Error : ' + err + '</pre>'
                            '<pre>' + content + '</pre>').split('\n')

            else:
                break
        text_div_tags = text.replace("<svg", "<div><svg").replace("</svg>", "</svg></div>")
        return text_div_tags.split("\n")


def makeExtension(*args, **kwargs):
    return InlineGraphvizExtension(*args, **kwargs)
