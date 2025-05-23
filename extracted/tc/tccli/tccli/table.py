
import os
import sys
import struct

from . import colorama
import six

PY2 = sys.version_info[0] == 2


def determine_terminal_width(default_width=80):
    try:
        from termios import TIOCGWINSZ
        from fcntl import ioctl
    except ImportError:
        return default_width
    try:
        height, width = struct.unpack(
            'hhhh', ioctl(sys.stdout, TIOCGWINSZ, '\000' * 8))[0:2]
    except Exception:
        return default_width
    else:
        return width


def is_a_tty():
    try:
        return os.isatty(sys.stdout.fileno())
    except Exception:
        return False


def center_text(text, length=80, left_edge='|', right_edge='|',
                text_length=None):
    """Center text with specified edge chars.

    You can pass in the length of the text as an arg, otherwise it is computed
    automatically for you.  This can allow you to center a string not based
    on it's literal length (useful if you're using ANSI codes).
    """
    # postcondition: len(returned_text) == length
    if text_length is None:
        text_length = len(text)
    output = []
    char_start = (length // 2) - (text_length // 2) - 1
    output.append(left_edge + ' ' * char_start + text)
    length_so_far = len(left_edge) + char_start + text_length
    right_side_spaces = length - len(right_edge) - length_so_far
    output.append(' ' * right_side_spaces)
    output.append(right_edge)
    final = ''.join(output)
    return final


def align_left(text, length, left_edge='|', right_edge='|', text_length=None,
               left_padding=2):
    """Left align text."""
    # postcondition: len(returned_text) == length
    if text_length is None:
        text_length = len(text)
    computed_length = (
        text_length + left_padding + len(left_edge) + len(right_edge))
    if length - computed_length >= 0:
        padding = left_padding
    else:
        padding = 0
    output = []
    length_so_far = 0
    output.append(left_edge)
    length_so_far += len(left_edge)
    output.append(' ' * padding)
    length_so_far += padding
    output.append(text)
    length_so_far += text_length
    output.append(' ' * (length - length_so_far - len(right_edge)))
    output.append(right_edge)
    return ''.join(output)


def convert_to_vertical_table(sections):
    # Any section that only has a single row is
    # inverted, so:
    # header1 | header2 | header3
    # val1    | val2    | val2
    #
    # becomes:
    #
    # header1 | val1
    # header2 | val2
    # header3 | val3
    for i, section in enumerate(sections):
        if len(section.rows) == 1 and section.headers:
            headers = section.headers
            new_section = Section()
            new_section.title = section.title
            new_section.indent_level = section.indent_level
            for header, element in zip(headers, section.rows[0]):
                new_section.add_row([header, element])
            sections[i] = new_section


class IndentedStream(object):
    def __init__(self, stream, indent_level, left_indent_char='|',
                 right_indent_char='|'):
        self._stream = stream
        self._indent_level = indent_level
        self._left_indent_char = left_indent_char
        self._right_indent_char = right_indent_char

    def write(self, text):
        self._stream.write(self._left_indent_char * self._indent_level)
        if text.endswith('\n'):
            self._stream.write(text[:-1])
            self._stream.write(self._right_indent_char * self._indent_level)
            self._stream.write('\n')
        else:
            self._stream.write(text)

    def __getattr__(self, attr):
        return getattr(self._stream, attr)


class Styler(object):
    def style_title(self, text):
        return text

    def style_header_column(self, text):
        return text

    def style_row_element(self, text):
        return text

    def style_indentation_char(self, text):
        return text


class ColorizedStyler(Styler):
    def __init__(self):
        # autoreset allows us to not have to sent
        # reset sequences for every string.
        colorama.init(autoreset=True)

    def style_title(self, text):
        # Originally bold + underline
        return text

    def style_header_column(self, text):
        # Originally underline
        return text

    def style_row_element(self, text):
        return (colorama.Style.BRIGHT + colorama.Fore.BLUE +
                text + colorama.Style.RESET_ALL + colorama.Style.RESET_ALL)

    def style_indentation_char(self, text):
        return (colorama.Style.DIM + colorama.Fore.YELLOW +
                text + colorama.Style.RESET_ALL)


class MultiTable(object):
    def __init__(self, terminal_width=None, initial_section=True,
                 column_separator='|', terminal=None,
                 styler=None, auto_reformat=True):
        self._auto_reformat = auto_reformat
        if initial_section:
            self._current_section = Section()
            self._sections = [self._current_section]
        else:
            self._current_section = None
            self._sections = []
        if styler is None:
            # Move out to factory.
            import platform
            if is_a_tty() and 'Windows' not in platform.system():
                self._styler = ColorizedStyler()
            else:
                self._styler = Styler()
        else:
            self._styler = styler
        self._rendering_index = 0
        self._column_separator = column_separator
        if terminal_width is None:
            self._terminal_width = determine_terminal_width()

    def add_title(self, title):
        self._current_section.add_title(title)

    def add_row_header(self, headers):
        self._current_section.add_header(headers)

    def add_row(self, row_elements):
        self._current_section.add_row(row_elements)

    def new_section(self, title, indent_level=0):
        self._current_section = Section()
        self._sections.append(self._current_section)
        self._current_section.add_title(title)
        self._current_section.indent_level = indent_level

    def render(self, stream):
        max_width = self._calculate_max_width()
        should_convert_table = self._determine_conversion_needed(max_width)
        if should_convert_table:
            convert_to_vertical_table(self._sections)
            max_width = self._calculate_max_width()
        stream.write('-' * max_width + '\n')
        for section in self._sections:
            self._render_section(section, max_width, stream)

    def _determine_conversion_needed(self, max_width):
        # If we don't know the width of the controlling terminal,
        # then we don't try to resize the table.
        if max_width > self._terminal_width:
            return self._auto_reformat

    def _calculate_max_width(self):
        max_width = max(s.total_width(padding=4, with_border=True,
                                      outer_padding=s.indent_level)
                        for s in self._sections)
        return max_width

    def _render_section(self, section, max_width, stream):
        stream = IndentedStream(stream, section.indent_level,
                                self._styler.style_indentation_char('|'),
                                self._styler.style_indentation_char('|'))
        max_width -= (section.indent_level * 2)
        self._render_title(section, max_width, stream)
        self._render_column_titles(section, max_width, stream)
        self._render_rows(section, max_width, stream)

    def _render_title(self, section, max_width, stream):
        # The title consists of:
        # title        :  |   This is the title      |
        # bottom_border:  ----------------------------
        if section.title:
            title = self._styler.style_title(section.title)
            stream.write(center_text(title, max_width, '|', '|',
                                     len(section.title)) + '\n')
            if not section.headers and not section.rows:
                stream.write('+%s+' % ('-' * (max_width - 2)) + '\n')

    def _render_column_titles(self, section, max_width, stream):
        if not section.headers:
            return
        # In order to render the column titles we need to know
        # the width of each of the columns.
        widths = section.calculate_column_widths(padding=4,
                                                 max_width=max_width)
        # TODO: Built a list instead of +=, it's more efficient.
        current = ''
        length_so_far = 0
        # The first cell needs both left and right edges '|  foo  |'
        # while subsequent cells only need right edges '  foo  |'.
        first = True
        for width, header in zip(widths, section.headers):
            stylized_header = self._styler.style_header_column(header)
            if first:
                left_edge = '|'
                first = False
            else:
                left_edge = ''
            current += center_text(text=stylized_header, length=width,
                                   left_edge=left_edge, right_edge='|',
                                   text_length=len(header))
            length_so_far += width
        self._write_line_break(stream, widths)
        stream.write(current + '\n')

    def _write_line_break(self, stream, widths):
        # Write out something like:
        # +-------+---------+---------+
        parts = []
        first = True
        for width in widths:
            if first:
                parts.append('+%s+' % ('-' * (width - 2)))
                first = False
            else:
                parts.append('%s+' % ('-' * (width - 1)))
        parts.append('\n')
        stream.write(''.join(parts))

    def _render_rows(self, section, max_width, stream):
        if not section.rows:
            return
        widths = section.calculate_column_widths(padding=4,
                                                 max_width=max_width)
        if not widths:
            return
        self._write_line_break(stream, widths)
        for row in section.rows:
            # TODO: Built the string in a list then join instead of using +=,
            # it's more efficient.
            current = ''
            length_so_far = 0
            first = True
            for width, element in zip(widths, row):
                if first:
                    left_edge = '|'
                    first = False
                else:
                    left_edge = ''
                stylized = self._styler.style_row_element(element)
                if PY2:
                    import platform
                    if 'Windows' in platform.system():
                        stylized = stylized.encode('GBK')
                    if 'Linux' in platform.system():
                        stylized = stylized.encode('utf-8')
                current += align_left(text=stylized, length=width,
                                      left_edge=left_edge,
                                      right_edge=self._column_separator,
                                      text_length=len(element))
                length_so_far += width
            stream.write(current + '\n')
        self._write_line_break(stream, widths)


class Section(object):
    def __init__(self):
        self.title = ''
        self.headers = []
        self.rows = []
        self.indent_level = 0
        self._num_cols = None
        self._max_widths = []

    def __repr__(self):
        return ("Section(title=%s, headers=%s, indent_level=%s, num_rows=%s)" %
                (self.title, self.headers, self.indent_level, len(self.rows)))

    def calculate_column_widths(self, padding=0, max_width=None):
        # postcondition: sum(widths) == max_width
        unscaled_widths = [w + padding for w in self._max_widths]
        if max_width is None:
            return unscaled_widths
        if not unscaled_widths:
            return unscaled_widths
        else:
            # Compute scale factor for max_width.
            scale_factor = max_width / float(sum(unscaled_widths))
            scaled = [int(round(scale_factor * w)) for w in unscaled_widths]
            # Once we've scaled the columns, we may be slightly over/under
            # the amount we need so we have to adjust the columns.
            off_by = sum(scaled) - max_width
            while off_by != 0:
                iter_order = list(range(len(scaled)))
                if off_by < 0:
                    iter_order = reversed(iter_order)
                for i in iter_order:
                    if off_by > 0:
                        scaled[i] -= 1
                        off_by -= 1
                    else:
                        scaled[i] += 1
                        off_by += 1
                    if off_by == 0:
                        break
            return scaled

    def total_width(self, padding=0, with_border=False, outer_padding=0):
        total = 0
        # One char on each side == 2 chars total to the width.
        border_padding = 2
        for w in self.calculate_column_widths():
            total += w + padding
        if with_border:
            total += border_padding
        total += outer_padding + outer_padding
        return max(len(self.title) + border_padding + outer_padding +
                   outer_padding, total)

    def add_title(self, title):
        self.title = title

    def add_header(self, headers):
        self._update_max_widths(headers)
        if self._num_cols is None:
            self._num_cols = len(headers)
        self.headers = self._format_headers(headers)

    def _format_headers(self, headers):
        return headers

    def add_row(self, row):
        if self._num_cols is None:
            self._num_cols = len(row)
        if len(row) != self._num_cols:
            raise ValueError("Row should have %s elements, instead "
                             "it has %s" % (self._num_cols, len(row)))
        row = self._format_row(row)
        self.rows.append(row)
        self._update_max_widths(row)

    def _format_row(self, row):
        return [six.text_type(r) for r in row]

    def _update_max_widths(self, row):
        if not self._max_widths:
            self._max_widths = [len(el) for el in row]
        else:
            for i, el in enumerate(row):
                self._max_widths[i] = max(len(el), self._max_widths[i])
