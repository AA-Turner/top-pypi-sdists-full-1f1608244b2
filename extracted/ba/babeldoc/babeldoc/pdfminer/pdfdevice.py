import logging
from collections.abc import Iterable
from collections.abc import Sequence
from typing import TYPE_CHECKING
from typing import BinaryIO
from typing import Optional
from typing import cast

from babeldoc.pdfminer.pdfcolor import PDFColorSpace
from babeldoc.pdfminer.pdffont import PDFFont
from babeldoc.pdfminer.pdffont import PDFUnicodeNotDefined
from babeldoc.pdfminer.pdfpage import PDFPage
from babeldoc.pdfminer.pdftypes import PDFStream
from babeldoc.pdfminer.psparser import PSLiteral
from babeldoc.pdfminer.utils import Matrix
from babeldoc.pdfminer.utils import PathSegment
from babeldoc.pdfminer.utils import Point
from babeldoc.pdfminer.utils import Rect
from babeldoc.pdfminer import utils

if TYPE_CHECKING:
    from babeldoc.pdfminer.pdfinterp import PDFGraphicState
    from babeldoc.pdfminer.pdfinterp import PDFResourceManager
    from babeldoc.pdfminer.pdfinterp import PDFStackT
    from babeldoc.pdfminer.pdfinterp import PDFTextState


PDFTextSeq = Iterable[int | float | bytes]

logger = logging.getLogger(__name__)


class PDFDevice:
    """Translate the output of PDFPageInterpreter to the output that is needed"""

    def __init__(self, rsrcmgr: "PDFResourceManager") -> None:
        self.rsrcmgr = rsrcmgr
        self.ctm: Matrix | None = None

    def __repr__(self) -> str:
        return "<PDFDevice>"

    def __enter__(self) -> "PDFDevice":
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        self.close()

    def close(self) -> None:
        pass

    def set_ctm(self, ctm: Matrix) -> None:
        self.ctm = ctm

    def begin_tag(self, tag: PSLiteral, props: Optional["PDFStackT"] = None) -> None:
        pass

    def end_tag(self) -> None:
        pass

    def do_tag(self, tag: PSLiteral, props: Optional["PDFStackT"] = None) -> None:
        pass

    def begin_page(self, page: PDFPage, ctm: Matrix) -> None:
        pass

    def end_page(self, page: PDFPage) -> None:
        pass

    def begin_figure(self, name: str, bbox: Rect, matrix: Matrix) -> None:
        pass

    def end_figure(self, name: str) -> None:
        pass

    def paint_path(
        self,
        graphicstate: "PDFGraphicState",
        stroke: bool,
        fill: bool,
        evenodd: bool,
        path: Sequence[PathSegment],
    ) -> None:
        pass

    def render_image(self, name: str, stream: PDFStream) -> None:
        pass

    def render_string(
        self,
        textstate: "PDFTextState",
        seq: PDFTextSeq,
        ncs: PDFColorSpace,
        graphicstate: "PDFGraphicState",
    ) -> None:
        pass


class PDFTextDevice(PDFDevice):
    def render_string(
        self,
        textstate: "PDFTextState",
        seq: PDFTextSeq,
        ncs: PDFColorSpace,
        graphicstate: "PDFGraphicState",
    ) -> None:
        assert self.ctm is not None
        matrix = utils.mult_matrix(textstate.matrix, self.ctm)
        font = textstate.font
        fontsize = textstate.fontsize
        scaling = textstate.scaling * 0.01
        charspace = textstate.charspace * scaling
        wordspace = textstate.wordspace * scaling
        rise = textstate.rise
        assert font is not None
        if font.is_multibyte():
            wordspace = 0
        dxscale = 0.001 * fontsize * scaling
        if font.is_vertical():
            textstate.linematrix = self.render_string_vertical(
                seq,
                matrix,
                textstate.linematrix,
                font,
                fontsize,
                scaling,
                charspace,
                wordspace,
                rise,
                dxscale,
                ncs,
                graphicstate,
            )
        else:
            textstate.linematrix = self.render_string_horizontal(
                seq,
                matrix,
                textstate.linematrix,
                font,
                fontsize,
                scaling,
                charspace,
                wordspace,
                rise,
                dxscale,
                ncs,
                graphicstate,
            )

    def render_string_horizontal(
        self,
        seq: PDFTextSeq,
        matrix: Matrix,
        pos: Point,
        font: PDFFont,
        fontsize: float,
        scaling: float,
        charspace: float,
        wordspace: float,
        rise: float,
        dxscale: float,
        ncs: PDFColorSpace,
        graphicstate: "PDFGraphicState",
    ) -> Point:
        (x, y) = pos
        needcharspace = False
        for obj in seq:
            if isinstance(obj, (int, float)):
                x -= obj * dxscale
                needcharspace = True
            elif isinstance(obj, bytes):
                for cid in font.decode(obj):
                    if needcharspace:
                        x += charspace
                    x += self.render_char(
                        utils.translate_matrix(matrix, (x, y)),
                        font,
                        fontsize,
                        scaling,
                        rise,
                        cid,
                        ncs,
                        graphicstate,
                    )
                    if cid == 32 and wordspace:
                        x += wordspace
                    needcharspace = True
            else:
                logger.warning(
                    f"Cannot render horizontal string because {obj!r} is not a valid int, float or bytes."
                )
        return (x, y)

    def render_string_vertical(
        self,
        seq: PDFTextSeq,
        matrix: Matrix,
        pos: Point,
        font: PDFFont,
        fontsize: float,
        scaling: float,
        charspace: float,
        wordspace: float,
        rise: float,
        dxscale: float,
        ncs: PDFColorSpace,
        graphicstate: "PDFGraphicState",
    ) -> Point:
        (x, y) = pos
        needcharspace = False
        for obj in seq:
            if isinstance(obj, (int, float)):
                y -= obj * dxscale
                needcharspace = True
            elif isinstance(obj, bytes):
                for cid in font.decode(obj):
                    if needcharspace:
                        y += charspace
                    y += self.render_char(
                        utils.translate_matrix(matrix, (x, y)),
                        font,
                        fontsize,
                        scaling,
                        rise,
                        cid,
                        ncs,
                        graphicstate,
                    )
                    if cid == 32 and wordspace:
                        y += wordspace
                    needcharspace = True
            else:
                logger.warning(
                    f"Cannot render vertical string because {obj!r} is not a valid int, float or bytes."
                )
        return (x, y)

    def render_char(
        self,
        matrix: Matrix,
        font: PDFFont,
        fontsize: float,
        scaling: float,
        rise: float,
        cid: int,
        ncs: PDFColorSpace,
        graphicstate: "PDFGraphicState",
    ) -> float:
        return 0


class TagExtractor(PDFDevice):
    def __init__(
        self,
        rsrcmgr: "PDFResourceManager",
        outfp: BinaryIO,
        codec: str = "utf-8",
    ) -> None:
        PDFDevice.__init__(self, rsrcmgr)
        self.outfp = outfp
        self.codec = codec
        self.pageno = 0
        self._stack: list[PSLiteral] = []

    def render_string(
        self,
        textstate: "PDFTextState",
        seq: PDFTextSeq,
        ncs: PDFColorSpace,
        graphicstate: "PDFGraphicState",
    ) -> None:
        font = textstate.font
        assert font is not None
        text = ""
        for obj in seq:
            if isinstance(obj, str):
                obj = utils.make_compat_bytes(obj)
            if not isinstance(obj, bytes):
                continue
            chars = font.decode(obj)
            for cid in chars:
                try:
                    char = font.to_unichr(cid)
                    text += char
                except PDFUnicodeNotDefined:
                    pass
        self._write(utils.enc(text))

    def begin_page(self, page: PDFPage, ctm: Matrix) -> None:
        output = '<page id="%s" bbox="%s" rotate="%d">' % (
            self.pageno,
            utils.bbox2str(page.mediabox),
            page.rotate,
        )
        self._write(output)

    def end_page(self, page: PDFPage) -> None:
        self._write("</page>\n")
        self.pageno += 1

    def begin_tag(self, tag: PSLiteral, props: Optional["PDFStackT"] = None) -> None:
        s = ""
        if isinstance(props, dict):
            s = "".join(
                [
                    f' {utils.enc(k)}="{utils.make_compat_str(v)}"'
                    for (k, v) in sorted(props.items())
                ],
            )
        out_s = f"<{utils.enc(cast(str, tag.name))}{s}>"
        self._write(out_s)
        self._stack.append(tag)

    def end_tag(self) -> None:
        assert self._stack, str(self.pageno)
        tag = self._stack.pop(-1)
        out_s = "</%s>" % utils.enc(cast(str, tag.name))
        self._write(out_s)

    def do_tag(self, tag: PSLiteral, props: Optional["PDFStackT"] = None) -> None:
        self.begin_tag(tag, props)
        self._stack.pop(-1)

    def _write(self, s: str) -> None:
        self.outfp.write(s.encode(self.codec))
