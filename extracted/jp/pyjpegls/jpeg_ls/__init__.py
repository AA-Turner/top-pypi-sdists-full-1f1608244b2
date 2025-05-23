from importlib.metadata import version
import logging

from .CharLS import (
    encode,
    decode,
    write,
    read,
    jlswrite,
    encode_array,
    encode_buffer,
    encode_pixel_data,
    jlsread,
    decode_buffer,
    decode_pixel_data,
)
from _CharLS import decode_from_buffer  # noqa: F401


__version__: str = version("pyjpegls")


# Setup default logging
_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())


def debug_logger() -> None:
    """Setup the logging for debugging."""
    logger = logging.getLogger(__name__)
    logger.handlers = []
    handler = logging.StreamHandler()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(levelname).1s: %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
