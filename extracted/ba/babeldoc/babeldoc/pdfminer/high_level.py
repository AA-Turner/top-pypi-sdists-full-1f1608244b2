"""Functions that can be used for the most common use-cases for pdfminer.six"""

import logging
import sys
from collections.abc import Container
from collections.abc import Iterator
from io import StringIO
from typing import Any
from typing import BinaryIO
from typing import cast

from babeldoc.pdfminer.converter import HOCRConverter
from babeldoc.pdfminer.converter import HTMLConverter
from babeldoc.pdfminer.converter import PDFPageAggregator
from babeldoc.pdfminer.converter import TextConverter
from babeldoc.pdfminer.converter import XMLConverter
from babeldoc.pdfminer.image import ImageWriter
from babeldoc.pdfminer.layout import LAParams
from babeldoc.pdfminer.layout import LTPage
from babeldoc.pdfminer.pdfdevice import PDFDevice
from babeldoc.pdfminer.pdfdevice import TagExtractor
from babeldoc.pdfminer.pdfexceptions import PDFValueError
from babeldoc.pdfminer.pdfinterp import PDFPageInterpreter
from babeldoc.pdfminer.pdfinterp import PDFResourceManager
from babeldoc.pdfminer.pdfpage import PDFPage
from babeldoc.pdfminer.utils import AnyIO
from babeldoc.pdfminer.utils import FileOrName
from babeldoc.pdfminer.utils import open_filename


def extract_text_to_fp(
    inf: BinaryIO,
    outfp: AnyIO,
    output_type: str = "text",
    codec: str = "utf-8",
    laparams: LAParams | None = None,
    maxpages: int = 0,
    page_numbers: Container[int] | None = None,
    password: str = "",
    scale: float = 1.0,
    rotation: int = 0,
    layoutmode: str = "normal",
    output_dir: str | None = None,
    strip_control: bool = False,
    debug: bool = False,
    disable_caching: bool = False,
    **kwargs: Any,
) -> None:
    """Parses text from inf-file and writes to outfp file-like object.

    Takes loads of optional arguments but the defaults are somewhat sane.
    Beware laparams: Including an empty LAParams is not the same as passing
    None!

    :param inf: a file-like object to read PDF structure from, such as a
        file handler (using the builtin `open()` function) or a `BytesIO`.
    :param outfp: a file-like object to write the text to.
    :param output_type: May be 'text', 'xml', 'html', 'hocr', 'tag'.
        Only 'text' works properly.
    :param codec: Text decoding codec
    :param laparams: An LAParams object from babeldoc.pdfminer.layout. Default is None
        but may not layout correctly.
    :param maxpages: How many pages to stop parsing after
    :param page_numbers: zero-indexed page numbers to operate on.
    :param password: For encrypted PDFs, the password to decrypt.
    :param scale: Scale factor
    :param rotation: Rotation factor
    :param layoutmode: Default is 'normal', see
        pdfminer.converter.HTMLConverter
    :param output_dir: If given, creates an ImageWriter for extracted images.
    :param strip_control: Does what it says on the tin
    :param debug: Output more logging data
    :param disable_caching: Does what it says on the tin
    :param other:
    :return: nothing, acting as it does on two streams. Use StringIO to get
        strings.
    """
    if debug:
        logging.getLogger().setLevel(logging.DEBUG)

    imagewriter = None
    if output_dir:
        imagewriter = ImageWriter(output_dir)

    rsrcmgr = PDFResourceManager(caching=not disable_caching)
    device: PDFDevice | None = None

    if output_type != "text" and outfp == sys.stdout:
        outfp = sys.stdout.buffer

    if output_type == "text":
        device = TextConverter(
            rsrcmgr,
            outfp,
            codec=codec,
            laparams=laparams,
            imagewriter=imagewriter,
        )

    elif output_type == "xml":
        device = XMLConverter(
            rsrcmgr,
            outfp,
            codec=codec,
            laparams=laparams,
            imagewriter=imagewriter,
            stripcontrol=strip_control,
        )

    elif output_type == "html":
        device = HTMLConverter(
            rsrcmgr,
            outfp,
            codec=codec,
            scale=scale,
            layoutmode=layoutmode,
            laparams=laparams,
            imagewriter=imagewriter,
        )

    elif output_type == "hocr":
        device = HOCRConverter(
            rsrcmgr,
            outfp,
            codec=codec,
            laparams=laparams,
            stripcontrol=strip_control,
        )

    elif output_type == "tag":
        # Binary I/O is required, but we have no good way to test it here.
        device = TagExtractor(rsrcmgr, cast(BinaryIO, outfp), codec=codec)

    else:
        msg = f"Output type can be text, html, xml or tag but is {output_type}"
        raise PDFValueError(msg)

    assert device is not None
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.get_pages(
        inf,
        page_numbers,
        maxpages=maxpages,
        password=password,
        caching=not disable_caching,
    ):
        page.rotate = (page.rotate + rotation) % 360
        interpreter.process_page(page)

    device.close()


def extract_text(
    pdf_file: FileOrName,
    password: str = "",
    page_numbers: Container[int] | None = None,
    maxpages: int = 0,
    caching: bool = True,
    codec: str = "utf-8",
    laparams: LAParams | None = None,
) -> str:
    """Parse and return the text contained in a PDF file.

    :param pdf_file: Either a file path or a file-like object for the PDF file
        to be worked on.
    :param password: For encrypted PDFs, the password to decrypt.
    :param page_numbers: List of zero-indexed page numbers to extract.
    :param maxpages: The maximum number of pages to parse
    :param caching: If resources should be cached
    :param codec: Text decoding codec
    :param laparams: An LAParams object from babeldoc.pdfminer.layout. If None, uses
        some default settings that often work well.
    :return: a string containing all of the text extracted.
    """
    if laparams is None:
        laparams = LAParams()

    with open_filename(pdf_file, "rb") as fp, StringIO() as output_string:
        fp = cast(BinaryIO, fp)  # we opened in binary mode
        rsrcmgr = PDFResourceManager(caching=caching)
        device = TextConverter(rsrcmgr, output_string, codec=codec, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page in PDFPage.get_pages(
            fp,
            page_numbers,
            maxpages=maxpages,
            password=password,
            caching=caching,
        ):
            interpreter.process_page(page)

        return output_string.getvalue()


def extract_pages(
    pdf_file: FileOrName,
    password: str = "",
    page_numbers: Container[int] | None = None,
    maxpages: int = 0,
    caching: bool = True,
    laparams: LAParams | None = None,
) -> Iterator[LTPage]:
    """Extract and yield LTPage objects

    :param pdf_file: Either a file path or a file-like object for the PDF file
        to be worked on.
    :param password: For encrypted PDFs, the password to decrypt.
    :param page_numbers: List of zero-indexed page numbers to extract.
    :param maxpages: The maximum number of pages to parse
    :param caching: If resources should be cached
    :param laparams: An LAParams object from babeldoc.pdfminer.layout. If None, uses
        some default settings that often work well.
    :return: LTPage objects
    """
    if laparams is None:
        laparams = LAParams()

    with open_filename(pdf_file, "rb") as fp:
        fp = cast(BinaryIO, fp)  # we opened in binary mode
        resource_manager = PDFResourceManager(caching=caching)
        device = PDFPageAggregator(resource_manager, laparams=laparams)
        interpreter = PDFPageInterpreter(resource_manager, device)
        for page in PDFPage.get_pages(
            fp,
            page_numbers,
            maxpages=maxpages,
            password=password,
            caching=caching,
        ):
            interpreter.process_page(page)
            layout = device.get_result()
            yield layout
