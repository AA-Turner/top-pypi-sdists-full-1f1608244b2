"""GTKWave save file generator.

This module provides tools for generating GTKWave save files.

`GTKWave`__ is an application for viewing VCD data. When opening a VCD file with
GTKWave, by default, no VCD variables (signals) are displayed. It is thus useful to have
an accompanying "save" file which configures various aspects of how GTKWave shows the
VCD data, including which variables are displayed, variable aliases, color information,
and more.

__ http://gtkwave.sourceforge.net

"""

import datetime
import math
import os
import time
import warnings
from contextlib import contextmanager
from enum import Enum, Flag, auto
from typing import IO, Any, Dict, Generator, List, Optional, Sequence, Tuple, Union


class GTKWFlag(Flag):
    """These are the valid GTKWave trace flags."""

    highlight = auto()
    "Highlight the trace item"

    hex = auto()  #: Hexadecimal data value representation
    dec = auto()  #: Decimal data value representation
    bin = auto()  #: Binary data value representation
    oct = auto()  #: Octal data value representation

    rjustify = auto()
    "Right-justify signal name/alias"
    invert = auto()
    reverse = auto()
    exclude = auto()
    blank = auto()  #: Used for blank, label, and/or analog height

    signed = auto()
    "Signed (2's compliment) data representation"
    ascii = auto()
    "ASCII character representation"

    collapsed = auto()  #: Used for closed groups
    ftranslated = auto()  #: Trace translated with filter file
    ptranslated = auto()  #: Trace translated with filter process

    analog_step = auto()  #: Show trace as discrete analog steps
    analog_interpolated = auto()  #: Show trace as analog with interpolation
    analog_blank_stretch = auto()  #: Used to extend height of analog data
    real = auto()  #: Real (floating point) data value representation
    analog_fullscale = auto()  #: Analog data scaled using full simulation time
    zerofill = auto()
    onefill = auto()
    closed = auto()

    grp_begin = auto()
    "Begin a group of signals"
    grp_end = auto()
    "End a group of signals"

    bingray = auto()
    graybin = auto()
    real2bits = auto()
    ttranslated = auto()

    popcnt = auto()
    "Show the population count, i.e. the number of set bits"

    fpdecshift = auto()


class GTKWColor(Enum):
    """The colors used by GTKWave.

    The `cycle` color is special and indicates the GTKWave should cycle through this
    list of colors, starting from the last selected color.

    """

    cycle = -1
    "Cycle between colors"
    normal = 0
    "Default color"
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    violet = 7

    def _cycle(self):
        return GTKWColor((self.value + 1) % 8)


class GTKWSave:
    """Write GTKWave save files.

    This class provides methods for writing the various pieces of a GTKWave save file. A
    GTKWave save file compliments a VCD dump file with dump file specific configuration
    GTKWave uses to display the dump file.

    A GTKWave save file is line-oriented ASCII text. Each line consists of a single
    configuration directive. All directives are optional.

    Some directives, such as :meth:`dumpfile()`, are for general GTKWave configuration.
    These general directives may be added anywhere in the save file and in any order
    relative to other directives. Directives may also be duplicated--the last one added
    will be used by GTKWave.

    The :meth:`trace()`, :meth:`trace_bits()`, :meth:`group()`, and :meth:`blank`
    directives add signals to the "Signals" list which are traced in the "Waves" frame.
    The order in which these signal traces are added determines the order in GTKWave.

    """

    def __init__(self, savefile: IO[str]) -> None:
        self.file = savefile
        self.path = getattr(savefile, "name", None)
        self._flags = GTKWFlag(0)
        self._color_stack = [GTKWColor.normal]
        self._filter_files: List[str] = []
        self._filter_procs: List[str] = []

    def _p(self, *args: object, **kwargs) -> None:
        print(*args, file=self.file, **kwargs)

    def _set_flags(self, flags: GTKWFlag) -> None:
        if flags != self._flags:
            self._p(f"@{flags.value:x}")
            self._flags = flags

    def _set_color(self, color: Optional[Union[GTKWColor, str, int]]) -> None:
        if color is not None:
            if not isinstance(color, GTKWColor):
                warnings.warn(
                    "Using str and int for colors is deprecated. "
                    "Use vcd.gtkw.GTKWColor instead.",
                    DeprecationWarning,
                    stacklevel=2,
                )
                if isinstance(color, str):
                    color = GTKWColor.__members__[color]
                else:
                    assert isinstance(color, int)
                    color = GTKWColor(color)
                assert isinstance(color, GTKWColor)

            if color == GTKWColor.cycle:
                self._color_stack[-1] = self._color_stack[-1]._cycle()
            else:
                self._color_stack[-1] = color
            self._p(f"[color] {self._color_stack[-1].value}")

    def _set_translate_filter_file(self, filter_path: Optional[str]) -> None:
        if filter_path:
            try:
                filter_id = 1 + self._filter_files.index(filter_path)
            except ValueError:
                self._filter_files.append(filter_path)
                filter_id = len(self._filter_files)
            self._p(f"^{filter_id} {filter_path}")

    def _set_translate_filter_proc(self, proc_path: Optional[str]) -> None:
        if proc_path:
            try:
                filter_id = 1 + self._filter_procs.index(proc_path)
            except ValueError:
                self._filter_procs.append(proc_path)
                filter_id = len(self._filter_procs)
            self._p(f"^>{filter_id} {proc_path}")

    def comment(self, *comments: Sequence[str]) -> None:
        """Add comment line(s) to save file."""
        for comment in comments:
            self._p("[*]", comment)

    def dumpfile(self, dump_path: str, abspath: bool = True) -> None:
        """Add VCD dump file path to save file.

        The `[dumpfile]` must be in the save file in order to only have to specify the
        save file on the `gtkwave` command line. I.e.:

            $ gtkwave my.gtkw

        If the `[dumpfile]` is not present in the save file, both the dump and save
        files must be specified to `gtkwave`:

            $ gtkwave my.vcd my.gtkw

        :param dump_path: path to VCD dump file or None to produce special "(null)"
                          value in the save file.
        :param bool abspath: convert *dump_path* to an absolute path.

        """
        if dump_path is None:
            self._p("[dumpfile] (null)")
        else:
            if abspath:
                dump_path = os.path.abspath(dump_path)
            self._p(f'[dumpfile] "{dump_path}"')

    def dumpfile_mtime(
        self,
        mtime: Optional[Union[float, time.struct_time, datetime.datetime]] = None,
        dump_path: Optional[str] = None,
    ) -> None:
        """Add dump file modification time to save file.

        Configuring the dump file's modification time is optional.

        """
        time_format = "%a %b %d %H:%M:%S %Y"
        if mtime is None:
            assert isinstance(dump_path, str)
            mtime = os.stat(dump_path).st_mtime
        if isinstance(mtime, float):
            mtime = time.gmtime(mtime)
        if isinstance(mtime, time.struct_time):
            mtime_str = time.strftime(time_format, mtime)
        elif isinstance(mtime, datetime.datetime):
            mtime_str = mtime.strftime(time_format)
        else:
            raise TypeError(f"Invalid mtime type ({type(mtime)})")
        self._p(f'[dumpfile_mtime] "{mtime_str}"')

    def dumpfile_size(
        self, size: Optional[int] = None, dump_path: Optional[str] = None
    ) -> None:
        """Add dump file size annotation to save file.

        Configuring the dump file's size is optional.

        """
        if size is None:
            assert isinstance(dump_path, str)
            size = os.stat(dump_path).st_size
        self._p(f"[dumpfile_size] {size}")

    def savefile(self, save_path: Optional[str] = None, abspath: bool = True) -> None:
        """Add the path of the save file to the save file.

        With no parameters, the output file's name will be used.

        Configuring the `[savefile]` is optional.

        :param save_path: path to this save file. None will use the output file's path.
        :param bool abspath: determines whether to make the path absolute.

        """
        if save_path is None and self.path is None:
            self._p("[savefile] (null)")
        else:
            if save_path is None:
                save_path = self.path
            if abspath and save_path is not None:
                save_path = os.path.abspath(save_path)
            self._p(f'[savefile] "{save_path}"')

    def timestart(self, timestamp: int = 0) -> None:
        """Add simulation start time to the save file."""
        self._p(f"[timestart] {timestamp}")

    def zoom_markers(
        self, zoom: float = 0.0, marker: int = -1, **kwargs: Dict[str, int]
    ) -> None:
        """Set zoom, primary marker, and markers 'a' - 'z'."""
        self._p(
            f"*{zoom:.6f} {marker}",
            *[kwargs.get(k, -1) for k in "abcdefghijklmnopqrstuvwxyz"],
        )

    def size(self, width: int, height: int) -> None:
        """Set GTKWave window size."""
        self._p(f"[size] {width} {height}")

    def pos(self, x: int = -1, y: int = -1) -> None:
        """Set GTKWave window position."""
        self._p(f"[pos] {x} {y}")

    def treeopen(self, tree: str) -> None:
        """Start with *tree* open in Signal Search Tree (SST).

        GTKWave specifies tree paths with a trailing '.'. The trailing '.' will
        automatically be added if it is omitted in the *tree* parameter.

        :param str tree: scope/path/tree to be opened in GTKWave's SST frame.

        """
        if tree[-1] == ".":
            self._p(f"[treeopen] {tree}")
        else:
            self._p(f"[treeopen] {tree}.")

    def signals_width(self, width: int) -> None:
        """Set width of Signals frame."""
        self._p(f"[signals_width] {width}")

    def sst_expanded(self, is_expanded: bool) -> None:
        """Set whether Signal Search Tree (SST) frame is expanded."""
        self._p(f"[sst_expanded] {int(bool(is_expanded))}")

    def pattern_trace(self, is_enabled: bool) -> None:
        """Enable/disable pattern trace."""
        self._p(f"[pattern_trace] {int(bool(is_enabled))}")

    @contextmanager
    def group(
        self, name: str, closed: bool = False, highlight: bool = False
    ) -> Generator[None, None, None]:
        """Contextmanager helper for :meth:`begin_group` and :meth:`end_group`.

        This context manager starts a new group of signal traces and ends the group when
        leaving the `with` block. E.g.:

            >>> import io
            >>> gtkw = GTKWSave(io.StringIO())
            >>> with gtkw.group("mygroup"):
            ...     gtkw.trace("a.b.x")
            ...     gtkw.trace("a.b.y")
            ...     gtkw.trace("a.b.z")

        :param str name: the name/label of the trace group.
        :param bool closed: group should be closed at GTKWave startup.
        :param bool highlight: group should be highlighted at GTKWave startup.

        """
        self.begin_group(name, closed, highlight)
        try:
            yield None
        finally:
            self.end_group(name, closed, highlight)

    def begin_group(
        self, name: str, closed: bool = False, highlight: bool = False
    ) -> None:
        """Begin a new signal trace group.

        Consider using :meth:`group()` instead of :meth:`begin_group()` and
        :meth:`end_group()`.

        :param str name: the name/label of the trace group.
        :param bool closed: group should be closed at GTKWave startup.
        :param bool highlight: group should be highlighted at GTKWave startup.

        """
        flags = GTKWFlag.grp_begin | GTKWFlag.blank
        if closed:
            flags |= GTKWFlag.closed
        if highlight:
            flags |= GTKWFlag.highlight
        self._set_flags(flags)
        self._p(f"-{name}")
        self._color_stack.append(GTKWColor.normal)

    def end_group(
        self, name: str, closed: bool = False, highlight: bool = False
    ) -> None:
        """End a signal trace group.

        This call must match with a prior call to :meth:`begin_group(). Consider using
        :meth:`group()` instead of :meth:`begin_group()` and :meth:`end_group()`.

        :param str name: the name/label of the trace group.
        :param bool closed: group should be closed at GTKWave startup.
        :param bool highlight: group should be highlighted at GTKWave startup.

        """
        flags = GTKWFlag.grp_end | GTKWFlag.blank
        if closed:
            flags |= GTKWFlag.closed | GTKWFlag.collapsed
        if highlight:
            flags |= GTKWFlag.highlight
        self._set_flags(flags)
        self._p(f"-{name}")
        self._color_stack.pop(-1)

    def blank(
        self, label: str = "", analog_extend: bool = False, highlight: bool = False
    ) -> None:
        """Add blank or label to trace signals list.

        :param str label: Optional label for the blank.
        :param bool analog_extend: extend the height of an immediately preceding analog
                                   trace signal.
        :param bool highlight: blank should be highlighted at GTKWave startup.

        """
        flags = GTKWFlag.blank
        if analog_extend:
            flags |= GTKWFlag.analog_blank_stretch
        if highlight:
            flags |= GTKWFlag.highlight
        self._set_flags(flags)
        self._p(f"-{label}")

    def trace(
        self,
        name: str,
        alias: Optional[str] = None,
        color: Optional[Union[GTKWColor, str, int]] = None,
        datafmt: str = "hex",
        highlight: bool = False,
        rjustify: bool = True,
        extraflags: Union[GTKWFlag, Optional[Sequence[str]]] = GTKWFlag(0),
        translate_filter_file: Optional[str] = None,
        translate_filter_proc: Optional[str] = None,
    ) -> None:
        """Add signal trace to save file.

        :param str name: fully-qualified name of signal to trace.
        :param str alias: optional alias to display instead of the *name*.
        :param GTKWColor color: optional color to use for the signal's trace.
        :param str datafmt: the format used for data display. Must be one of 'hex',
                            'dec', 'bin', 'oct', 'ascii', 'real', or 'signed'.
        :param bool highlight: trace should be highlighted at GTKWave startup.
        :param bool rjustify: trace name/alias should be right-justified.
        :param GTKWFlag extraflags: extra flags to apply to the trace.
        :param str translate_filter_file: path to translate filter file.
        :param str translate_filter_proc: path to translate filter executable.

        .. Note::

            GTKWave versions <= 3.3.64 require vector signal names to have a bit range
            suffix. For example, an 8-bit vector variable "module.myint" would be known
            by GTKWave as "module.myint[7:0]".

            GTKWave versions after 3.3.64 do not use bit-range suffixes.

        """
        if datafmt not in ["hex", "dec", "bin", "oct", "ascii", "real", "signed"]:
            raise ValueError(f"Invalid datafmt ({datafmt})")
        flags = GTKWFlag.__members__[datafmt]
        if isinstance(extraflags, GTKWFlag):
            flags |= extraflags
        else:
            warnings.warn(
                "Using Optional[Sequence[str]] for extraflags is deprecated. "
                "Use vcd.gtkw.GTKWFlag instead.",
                DeprecationWarning,
            )
            if extraflags is not None:
                for flag in GTKWFlag:
                    if flag.name in extraflags:
                        flags |= flag
        if highlight:
            flags |= GTKWFlag.highlight
        if rjustify:
            flags |= GTKWFlag.rjustify
        if translate_filter_file:
            flags |= GTKWFlag.ftranslated
        if translate_filter_proc:
            flags |= GTKWFlag.ptranslated
        self._set_flags(flags)
        self._set_color(color)
        self._set_translate_filter_file(translate_filter_file)
        self._set_translate_filter_proc(translate_filter_proc)
        if alias:
            self._p(f"+{{{alias}}} ", end="")
        self._p(name)

    @contextmanager
    def trace_bits(
        self,
        name: str,
        alias: Optional[str] = None,
        color: Optional[Union[str, int]] = None,
        datafmt: str = "hex",
        highlight: bool = False,
        rjustify: bool = True,
        extraflags: Union[GTKWFlag, Optional[Sequence[str]]] = GTKWFlag(0),
        translate_filter_file: Optional[str] = None,
        translate_filter_proc: Optional[str] = None,
    ) -> Generator[None, None, None]:
        """Contextmanager for tracing bits of a vector signal.

        This allows each individual bit of a vector signal to have its own trace (and
        trace configuration).

            >>> import io
            >>> gtkw = GTKWSave(io.StringIO())
            >>> name = "mod.myint"
            >>> with gtkw.trace_bits(name):
            ...     gtkw.trace_bit(0, name)
            ...     gtkw.trace_bit(1, name)
            ...     gtkw.trace_bit(2, name)
            ...     gtkw.trace_bit(3, name, "special", color=GTKWColor.yellow)

        :param str name: fully-qualified name of the vector variable to trace.
        :param str alias: optional alias to display instead of *name*.
        :param int color: optional trace color.
        :param str datafmt: format for data display.
        :param bool highlight: trace should be highlighted at GTKWave startup.
        :param bool rjustify: trace name/alias should be right-justified.
        :param GTKWFlag extraflags: extra flags to apply to the trace.
        :param str translate_filter_file: path to translate filter file.
        :param str translate_filter_proc: path to translate filter executable.

        """
        self.trace(
            name,
            alias,
            color,
            datafmt,
            highlight,
            rjustify,
            extraflags,
            translate_filter_file,
            translate_filter_proc,
        )
        flags = GTKWFlag.bin
        if isinstance(extraflags, GTKWFlag):
            flags |= extraflags
        else:
            warnings.warn(
                "Using Optional[Sequence[str]] for extraflags is deprecated. "
                "Use vcd.gtkw.GTKWFlag instead.",
                DeprecationWarning,
            )
            if extraflags is not None:
                for flag in GTKWFlag:
                    if flag.name in extraflags:
                        flags |= flag
        if highlight:
            flags |= GTKWFlag.highlight
        if rjustify:
            flags |= GTKWFlag.rjustify
        self._set_flags(flags)
        try:
            yield None
        finally:
            flags = GTKWFlag.blank | GTKWFlag.grp_end | GTKWFlag.collapsed
            if highlight:
                flags |= GTKWFlag.highlight
            self._set_flags(flags)
            self._p("-group_end")

    def trace_bit(
        self,
        index: int,
        name: str,
        alias: Optional[str] = None,
        color: Optional[Union[GTKWColor, str, int]] = None,
    ) -> None:
        """Trace individual bit of vector signal.

        This is meant for use in conjunction with :meth:`trace_bits()`.

        :param int index: index of bit
        :param str name: name of parent vector signal.
        :param str alias: optional alias to display for bit.
        :param int color: optional color for bit's trace.

        """
        self._set_color(color)
        if alias:
            self._p(f"+{{{alias}}} ", end="")
        self._p(f"({index}){name}")


TranslationType = Union[
    Tuple[Union[int, str], str], Tuple[Union[int, str], str, Union[str, int]]
]


def make_translation_filter(
    translations: Sequence[Tuple[Any, ...]],
    datafmt: str = "hex",
    size: Optional[int] = None,
) -> str:
    """Create translation filter.

    The returned translation filter string that can be written to a translation filter
    file usable by GTKWave.

    :param translations:

        Sequence of 2-tuples `(value, alias)` or 3-tuples `(value, alias, color)`.

    :param str datafmt:

        Format to apply to the translation values. This *datafmt* must match the
        *datafmt* used with :meth:`GTKWSave.trace()`, otherwise these translations will
        not be matched by GTKWave.

    :returns: Translation filter string suitable for writing to a translation filter
              file.

    """
    if datafmt == "hex":
        assert isinstance(size, int)
        value_format = f"0{int(math.ceil(size / 4))}x"
    elif datafmt == "oct":
        assert isinstance(size, int)
        value_format = f"0{int(math.ceil(size / 3))}o"
    elif datafmt in ["dec", "signed"]:
        value_format = "d"
    elif datafmt == "bin":
        assert isinstance(size, int)
        value_format = f"0{size}b"
    elif datafmt == "real":
        value_format = ".16g"
    elif datafmt == "ascii":
        value_format = ""
        ascii_translations = []
        for translation in translations:
            value = translation[0]
            rest = list(translation[1:])
            if isinstance(value, int):
                value = bytes((value,)).decode("ascii")
            elif not isinstance(value, str):
                raise TypeError(f"Invalid type ({type(value)}) for ascii translation")
            elif len(value) != 1:
                raise ValueError(f'Invalid ascii string "{value}"')
            ascii_translations.append(tuple([value] + rest))
        translations = ascii_translations
    else:
        raise ValueError(f"invalid datafmt ({datafmt})")

    lines = []

    for translation in translations:
        if len(translation) == 2:
            value, label = translation
            color = None
        else:
            value, label, color = translation

        if datafmt in ["hex", "oct", "bin"]:
            assert isinstance(size, int)
            max_val = 1 << size
            if -value > (max_val >> 1) or value >= max_val:
                raise ValueError(f"Value ({value}) not representable in {size} bits")
            if value < 0:
                # Two's compliment treatment
                value += 1 << size

        value_str = format(value, value_format)

        if color is None:
            lines.append(f"{value_str} {label}")
        else:
            lines.append(f"{value_str} ?{color}?{label}")

    return "\n".join(lines)


def decode_flags(flags: Union[str, int]) -> List[str]:
    """Decode hexadecimal flags from GTKWave save file into flag names.

    This is useful for understanding what, for example "@802022" means when inspecting a
    GTKWave save file.

    :param flags: Hexadecimal flags from GTKWave save file; either as an integer or
                  string with hexadecimal characters.
    :returns: List of flag names

    """
    if isinstance(flags, str):
        decoded = GTKWFlag(int(flags.lstrip("@"), 16))
    else:
        decoded = GTKWFlag(flags)
    return [str(flag.name) for flag in GTKWFlag if flag & decoded]


def spawn_gtkwave_interactive(
    dump_path: str, save_path: str, quiet: bool = False
) -> None:  # pragma: no cover
    """Spawn gtkwave process in interactive mode.

    A process pipeline is constructed such that the contents of the VCD dump file at
    *dump_path* are displayed interactively as the dump file is being written (i.e. with
    :class:`~vcd.writer.VCDWriter`.

    The process pipeline built is approximately equivalent to::

        $ tail -f dump_path | shmidcat | gtkwave -vI save_path

    The ``tail``, ``shmidcat``, and ``gtkwave`` executables must be found in ``$PATH``.

    .. Warning::

        This function does not work on Windows.

    .. Note::

        A child python process of the caller will remain running until the GTKWave
        window is closed. This process ensures that the various other child processes
        are properly reaped.

    :param str dump_path: path to VCD dump file. The dump file must exist, but be empty.
    :param str save_path: path to GTKWave save file. The save file will be read
                          immediately by GTKWave and thus must be completely written.
    :param bool quiet: quiet GTKWave's output by closing its `stdout` and `stderr` file
                       descriptors.

    """
    import signal

    stdin_fd, stdout_fd, stderr_fd = 0, 1, 2

    if not os.fork():
        shmidcat_rd_fd, tail_wr_fd = os.pipe()

        tail_pid = os.fork()
        if not tail_pid:
            os.close(shmidcat_rd_fd)
            os.dup2(tail_wr_fd, stdout_fd)
            os.execlp("tail", "tail", "-n", "+0", "-f", dump_path)

        os.close(tail_wr_fd)
        gtkwave_rd_fd, shmidcat_wr_fd = os.pipe()

        shmidcat_pid = os.fork()
        if not shmidcat_pid:
            os.close(gtkwave_rd_fd)
            os.dup2(shmidcat_rd_fd, stdin_fd)
            os.dup2(shmidcat_wr_fd, stdout_fd)
            os.execlp("shmidcat", "shmidcat")

        os.close(shmidcat_rd_fd)
        os.close(shmidcat_wr_fd)

        gtkwave_pid = os.fork()
        if not gtkwave_pid:
            os.dup2(gtkwave_rd_fd, stdin_fd)
            if quiet:
                devnull = open(os.devnull, "w")
                os.dup2(devnull.fileno(), stdout_fd)
                os.dup2(devnull.fileno(), stderr_fd)
            os.execlp("gtkwave", "gtkwave", "--vcd", "--interactive", save_path)

        # The first forked process exists to do this cleanup...
        os.waitpid(gtkwave_pid, 0)
        os.kill(tail_pid, signal.SIGTERM)
        os.kill(shmidcat_pid, signal.SIGTERM)
        os._exit(0)
