import collections

from babeldoc.pdfminer.psparser import LIT

LITERAL_DEVICE_GRAY = LIT("DeviceGray")
LITERAL_DEVICE_RGB = LIT("DeviceRGB")
LITERAL_DEVICE_CMYK = LIT("DeviceCMYK")
# Abbreviations for inline images
LITERAL_INLINE_DEVICE_GRAY = LIT("G")
LITERAL_INLINE_DEVICE_RGB = LIT("RGB")
LITERAL_INLINE_DEVICE_CMYK = LIT("CMYK")


class PDFColorSpace:
    def __init__(self, name: str, ncomponents: int) -> None:
        self.name = name
        self.ncomponents = ncomponents

    def __repr__(self) -> str:
        return "<PDFColorSpace: %s, ncomponents=%d>" % (self.name, self.ncomponents)


PREDEFINED_COLORSPACE: dict[str, PDFColorSpace] = collections.OrderedDict()

for name, n in [
    ("DeviceGray", 1),  # default value first
    ("CalRGB", 3),
    ("CalGray", 1),
    ("Lab", 3),
    ("DeviceRGB", 3),
    ("DeviceCMYK", 4),
    ("Separation", 1),
    ("Indexed", 1),
    ("Pattern", 1),
]:
    PREDEFINED_COLORSPACE[name] = PDFColorSpace(name, n)
