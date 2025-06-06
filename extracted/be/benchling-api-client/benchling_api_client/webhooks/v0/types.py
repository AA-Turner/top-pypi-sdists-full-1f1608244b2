"""Contains some shared types for properties."""
from __future__ import annotations

from typing import BinaryIO, Generic, MutableMapping, Optional, TextIO, Tuple, TypeVar, Union

import attr


class Unset:
    def __bool__(self) -> bool:
        return False

    def __copy__(self) -> Unset:
        return UNSET

    def __deepcopy__(self, memo) -> Unset:
        return UNSET


UNSET: Unset = Unset()

# Used as `FileProperty._json_type_string`
FileJsonType = Tuple[Optional[str], Union[BinaryIO, TextIO], Optional[str]]


@attr.s(auto_attribs=True)
class File:
    """Contains information for file uploads."""

    payload: Union[BinaryIO, TextIO]
    file_name: Optional[str] = None
    mime_type: Optional[str] = None

    def to_tuple(self) -> FileJsonType:
        """Return a tuple representation that httpx will accept for multipart/form-data."""
        return self.file_name, self.payload, self.mime_type


T = TypeVar("T")


@attr.s(auto_attribs=True)
class Response(Generic[T]):
    """A response from an endpoint."""

    status_code: int
    content: bytes
    headers: MutableMapping[str, str]
    parsed: Optional[T]


__all__ = ["File", "Response"]
