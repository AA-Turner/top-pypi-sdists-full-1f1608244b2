import re
import logging
from typing import Optional
from functools import lru_cache
from normality import collapse_spaces, ascii_text, category_replace

from fingerprints.constants import WS, BRACKETED

log = logging.getLogger(__name__)

CHARACTERS_REMOVE_RE = re.compile(r"[\.\'’]")

PREFIXES_RAW_LIST = [
    "Mr",
    "Ms",
    "Mrs",
    "Mister",
    "Miss",
    "Madam",
    "Madame",
    "Monsieur",
    "Mme",
    "Mmme",
    "Herr",
    "Hr",
    "Frau",
    "Fr",
    "The",
    "Fräulein",
    "Senor",
    "Senorita",
    "Sheik",
    "Sheikh",
    "Shaikh",
    "Sr",
    "Sir",
    "Lady",
    "The",
    "de",
    "of",
]
PREFIXES_RAW = "|".join(PREFIXES_RAW_LIST)
NAME_PATTERN_ = r"^\W*((%s)\.?\s+)*(?P<term>.*?)([\'’]s)?\W*$"
NAME_PATTERN_ = NAME_PATTERN_ % PREFIXES_RAW
PREFIXES = re.compile(NAME_PATTERN_, re.I | re.U)


def clean_entity_prefix(name: str) -> str:
    """Remove prefixes like Mr., Mrs., etc."""
    match = PREFIXES.match(name)
    if match is not None:
        name = match.group("term")
    return name


def clean_brackets(text: str) -> str:
    """Remove any text in brackets. This is meant to handle names of companies
    which include the jurisdiction, like: Turtle Management (Seychelles) Ltd."""
    return BRACKETED.sub(WS, text)


@lru_cache(maxsize=2000)
def clean_name_ascii(text: Optional[str]) -> Optional[str]:
    """Super-hardcore string scrubbing."""
    # transliterate to ascii
    text = ascii_text(text)
    if text is None:
        return None
    # replace punctuation and symbols
    text = CHARACTERS_REMOVE_RE.sub("", text)
    text = text.lower()
    cleaned = category_replace(text)
    cleaned = collapse_spaces(cleaned)
    if cleaned is None or len(cleaned) < 2:
        return None
    return cleaned


@lru_cache(maxsize=2000)
def clean_name_light(text: str) -> Optional[str]:
    """Clean up a name for comparison, but don't convert to ASCII/Latin."""
    # replace punctuation and symbols
    text = CHARACTERS_REMOVE_RE.sub("", text)
    text = text.lower()
    cleaned = category_replace(text)
    cleaned = collapse_spaces(cleaned)
    if cleaned is None or len(cleaned) < 2:
        return None
    return cleaned
