from __future__ import annotations

import ntpath
from functools import cached_property, lru_cache
from io import BytesIO
from operator import itemgetter
from typing import TYPE_CHECKING, BinaryIO

from dissect.ntfs.attr import Attribute, AttributeHeader
from dissect.ntfs.c_ntfs import (
    ATTRIBUTE_TYPE_CODE,
    DEFAULT_RECORD_SIZE,
    FILE_FILE_NAME_INDEX_PRESENT,
    FILE_NAME_DOS,
    FILE_NUMBER_MFT,
    FILE_NUMBER_ROOT,
    IO_REPARSE_TAG,
    c_ntfs,
    segment_reference,
)
from dissect.ntfs.exceptions import (
    BrokenMftError,
    Error,
    FileNotFoundError,
    MftNotAvailableError,
    NotADirectoryError,
    NotAReparsePointError,
)
from dissect.ntfs.index import Index, IndexEntry
from dissect.ntfs.util import AttributeCollection, AttributeMap, apply_fixup

if TYPE_CHECKING:
    from collections.abc import Iterator

    from dissect.ntfs.ntfs import NTFS


class Mft:
    """Interact with the ``$MFT`` (Master File Table).

    Args:
        fh: A file-like object of the $MFT file.
        ntfs: An optional NTFS class instance.
    """

    def __init__(self, fh: BinaryIO, ntfs: NTFS | None = None):
        self.fh = fh
        self.ntfs = ntfs

        self.get = lru_cache(4096)(self.get)

    def __call__(self, ref: int | str | c_ntfs._MFT_SEGMENT_REFERENCE, *args, **kwargs) -> MftRecord:
        return self.get(ref, *args, **kwargs)

    @cached_property
    def root(self) -> MftRecord:
        """Return the root directory MFT record."""
        return self.get(FILE_NUMBER_ROOT)

    def _get_path(self, path: str, root: MftRecord | None = None) -> MftRecord:
        """Resolve a file path to the correct MFT record.

        Args:
            path: The path to resolve.
            root: Optional root record to start resolving from. Useful for relative path lookups.
        """
        root = root or self.root

        # Programmatically we will often use the `/` separator, so replace it with the native path separator of NTFS
        # `/` is an illegal character in NTFS filenames, so it's safe to replace
        search_path = path.replace("/", "\\")
        node = root

        parts = search_path.split("\\")

        for part_num, part in enumerate(parts):
            if not part:
                continue

            while node.is_reparse_point() and part_num < len(parts):
                node = node.reparse_point_record

            if not node.is_dir():
                raise NotADirectoryError(f"Error finding path {path}: {self!r} is not a directory")

            index = node.index("$I30")
            try:
                node = index.search(part).dereference()
            except KeyError:
                raise FileNotFoundError(f"File not found: {path}")

        return node

    def get(self, ref: int | str | c_ntfs._MFT_SEGMENT_REFERENCE, root: MftRecord | None = None) -> MftRecord:
        """Retrieve an MFT record using a variety of methods.

        Supported references are:
            - ``_MFT_SEGMENT_REFERENCE`` cstruct structure
            - integer segment number
            - string file path

        Args:
            ref: Reference to retrieve the record by.
            root: Optional root record to start resolving from. Useful for relative path lookups.

        Raises:
            TypeError: If the reference is of an unsupported type.
        """
        if isinstance(ref, c_ntfs._MFT_SEGMENT_REFERENCE):
            ref = segment_reference(ref)

        if isinstance(ref, int):
            record_size = self.ntfs._record_size if self.ntfs else DEFAULT_RECORD_SIZE

            record = MftRecord.from_fh(self.fh, ref * record_size, ntfs=self.ntfs)
            record.segment = ref
            return record

        if isinstance(ref, str):
            return self._get_path(ref, root)

        raise TypeError(f"Invalid MFT reference: {ref!r}")

    def segments(self, start: int = 0, end: int = -1) -> Iterator[MftRecord]:
        """Yield all valid MFT records, regardless if they're allocated or not.

        Args:
            start: The starting segment number. Use ``-1`` to start from the last segment.
            end: The ending segment number. Use ``-1`` to end with the last segment.
        """
        record_size = self.ntfs._record_size if self.ntfs else DEFAULT_RECORD_SIZE
        last_segment = self.get(FILE_NUMBER_MFT).size() // record_size
        start = last_segment if start == -1 else start
        end = last_segment if end == -1 else end
        step = 1 if start <= end else -1

        for segment in range(start, end + step, step):
            try:
                yield self.get(segment)
            except Error:  # noqa: PERF203
                continue
            except EOFError:
                break


class MftRecord:
    """MFT record parsing and interaction.

    Use the :func:`~MftRecord.from_fh` or :func:`~MftRecord.from_bytes` class methods to instantiate.
    """

    def __init__(self):
        self.ntfs: NTFS | None = None
        self.segment: int | None = None
        self.offset: int | None = None
        self.data: bytes | None = None
        self.header: c_ntfs._FILE_RECORD_SEGMENT_HEADER | None = None

    def __repr__(self) -> str:
        return f"<MftRecord {self.segment}#{self.header.SequenceNumber}>"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, MftRecord):
            return self.segment == other.segment and self.header.SequenceNumber == other.header.SequenceNumber
        return False

    __hash__ = object.__hash__

    @classmethod
    def from_fh(cls, fh: BinaryIO, offset: int, ntfs: NTFS | None = None) -> MftRecord:
        """Parse an MFT record from a file-like object.

        Args:
            fh: The file-like object to parse an MFT record from.
            offset: The offset in the file-like object to parse the MFT record from.
            ntfs: An optional NTFS class instance.
        """
        record_size = ntfs._record_size if ntfs else DEFAULT_RECORD_SIZE

        fh.seek(offset)
        data = fh.read(record_size)

        obj = cls.from_bytes(data, ntfs)
        obj.offset = offset
        return obj

    @classmethod
    def from_bytes(cls, data: bytes, ntfs: NTFS | None = None) -> MftRecord:
        """Parse an MFT record from bytes.

        Args:
            data: The bytes object to parse an MFT record from.
            ntfs: An optional NTFS class instance.

        Raises:
            BrokenMftError: If the MFT record signature is invalid.
        """
        obj = cls()
        obj.ntfs = ntfs

        if data[:4] != b"FILE":
            raise BrokenMftError(f"Invalid MFT record Signature: {data[:4]}")

        obj.data = apply_fixup(data)
        obj.header = c_ntfs._FILE_RECORD_SEGMENT_HEADER(obj.data)
        return obj

    def get(self, path: str) -> MftRecord:
        """Retrieve a :class:`MftRecord` relative to this one.

        Args:
            path: The path to lookup.

        Raises:
            MftNotAvailableError: If no MFT is available.
        """
        if not self.ntfs or not self.ntfs.mft:
            raise MftNotAvailableError
        return self.ntfs.mft.get(path, root=self)

    @cached_property
    def attributes(self) -> AttributeMap:
        """Parse and return the attributes in this MFT record.

        ``$ATTRIBUTE_LIST``'s are only parsed if there's an MFT available on the NTFS object.

        Raises:
            BrokenMftError: If an error occurred parsing the attributes.
        """
        fh = BytesIO(self.data)
        offset = self.header.FirstAttributeOffset
        attrs = AttributeMap()

        attr_list = None
        while True:
            try:
                header = AttributeHeader(fh, offset, self)
            except EOFError:
                break

            if header.type == ATTRIBUTE_TYPE_CODE.END:
                break

            if header.record_length == 0:
                raise BrokenMftError("Attribute RecordLength is 0 but end not yet reached")

            attr = Attribute(header, self)
            attrs.add(attr)

            # If we encounter an attribute list, store it for later use
            # The attribute list can be non-resident, so we need to check if parsing succeeded
            # by checking if attr.attribute exists, in the case we don't have a volume
            if header.type == ATTRIBUTE_TYPE_CODE.ATTRIBUTE_LIST and attr.attribute:
                attr_list = attr

            offset += header.record_length

        if attr_list and self.ntfs and self.ntfs.mft:
            for attr in attr_list.attributes():
                attrs.add(attr)

        return attrs

    @cached_property
    def resident(self) -> bool:
        """Return whether this record's default ``$DATA`` attribute is resident."""
        return any(attr.header.resident for attr in self.attributes[ATTRIBUTE_TYPE_CODE.DATA])

    @cached_property
    def filename(self) -> str | None:
        """Return the first file name, or ``None`` if this record has no file names."""
        filenames = self.filenames()
        return filenames[0] if filenames else None

    def filenames(self, ignore_dos: bool = False) -> list[str]:
        """Return all file names of this record.

        Args:
            ignore_dos: Ignore DOS file name entries.
        """
        result = []
        for attr in self.attributes[ATTRIBUTE_TYPE_CODE.FILE_NAME]:
            if ignore_dos and attr.flags == FILE_NAME_DOS:
                continue
            result.append((attr.flags, attr.file_name))
        return [item[1] for item in sorted(result, key=itemgetter(0))]

    def full_path(self, ignore_dos: bool = False) -> str | None:
        """Return the first full path, or ``None`` if this record has no file names.

        Args:
            ignore_dos: Ignore DOS file name entries.
        """
        paths = self.full_paths(ignore_dos)
        return paths[0] if paths else None

    def full_paths(self, ignore_dos: bool = False) -> list[str]:
        """Return all full paths of this record.

        Args:
            ignore_dos: Ignore DOS file name entries.
        """
        result = []

        for attr in self.attributes[ATTRIBUTE_TYPE_CODE.FILE_NAME]:
            if ignore_dos and attr.flags == FILE_NAME_DOS:
                continue
            result.append((attr.flags, attr.full_path()))

        return [item[1] for item in sorted(result, key=itemgetter(0))]

    def is_dir(self) -> bool:
        """Return whether this record is a directory."""
        return bool(self.header.Flags & FILE_FILE_NAME_INDEX_PRESENT)

    def is_file(self) -> bool:
        """Return whether this record is a file."""
        return not self.is_dir()

    def is_reparse_point(self) -> bool:
        """Return whether this record is a reparse point."""
        return ATTRIBUTE_TYPE_CODE.REPARSE_POINT in self.attributes

    def is_symlink(self) -> bool:
        """Return whether this record is a symlink reparse point."""
        attr = self.attributes[ATTRIBUTE_TYPE_CODE.REPARSE_POINT]
        return bool(attr) and attr.tag == IO_REPARSE_TAG.SYMLINK

    def is_mount_point(self) -> bool:
        """Return whether this record is a mount point reparse point."""
        attr = self.attributes[ATTRIBUTE_TYPE_CODE.REPARSE_POINT]
        return bool(attr) and attr.tag == IO_REPARSE_TAG.MOUNT_POINT

    @cached_property
    def reparse_point_name(self) -> str:
        """Return the (printable) name of this reparse point."""
        if not self.is_reparse_point():
            raise NotAReparsePointError(f"{self!r} is not a reparse point")
        return self.attributes[ATTRIBUTE_TYPE_CODE.REPARSE_POINT].print_name

    @cached_property
    def reparse_point_substitute_name(self) -> str:
        """Return the substitute name of this reparse point."""
        if not self.is_reparse_point():
            raise NotAReparsePointError(f"{self!r} is not a reparse point")
        return self.attributes[ATTRIBUTE_TYPE_CODE.REPARSE_POINT].substitute_name

    @cached_property
    def reparse_point_record(self) -> MftRecord:
        """Resolve a reparse point and return the target record.

        Note: absolute links (such as directory junctions) will *always* fail in the context of a single filesystem.
        Absolute links include the drive letter, of which we have no knowledge here.
        """
        if not self.is_reparse_point():
            raise NotAReparsePointError(f"{self!r} is not a reparse point")

        if not self.ntfs or not self.ntfs.mft:
            raise MftNotAvailableError

        reparse_point = self.attributes[ATTRIBUTE_TYPE_CODE.REPARSE_POINT]

        target_name = reparse_point.print_name
        if reparse_point.relative:
            target_name = ntpath.join(ntpath.dirname(self.full_path()), target_name)

        return self.ntfs.mft.get(target_name)

    def _get_stream_attributes(
        self, name: str, attr_type: ATTRIBUTE_TYPE_CODE = ATTRIBUTE_TYPE_CODE.DATA
    ) -> AttributeCollection[Attribute]:
        """Return the :class:`~dissect.ntfs.util.AttributeCollection` of all attributes with the given name and attribute type.

        Args:
            name: The attribute name, often an empty string.
            attr_type: The attribute type to find.

        Raises:
            FileNotFoundError: If there are no attributes with the given name and type.
        """  # noqa: E501
        attrs = self.attributes.find(name, attr_type)
        if not attrs:
            raise FileNotFoundError(f"No such stream on record {self}: ({name!r}, {attr_type})")
        return attrs

    def open(
        self,
        name: str = "",
        attr_type: ATTRIBUTE_TYPE_CODE = ATTRIBUTE_TYPE_CODE.DATA,
        allocated: bool = False,
    ) -> BinaryIO:
        """Open a stream on the given stream name and type.

        Args:
            name: The stream name, an empty string for the "default" data stream.
            attr_type: The attribute type to open a stream on.
            allocated: Whether to use the real stream size or the allocated stream size (i.e. include slack space).

        Raises:
            FileNotFoundError: If there are no attributes with the given name and type.
        """
        return self._get_stream_attributes(name, attr_type).open(allocated)

    def size(
        self,
        name: str = "",
        attr_type: ATTRIBUTE_TYPE_CODE = ATTRIBUTE_TYPE_CODE.DATA,
        allocated: bool = False,
    ) -> int:
        """Return the stream size of the given stream name and type.

        Args:
            name: The stream name, an empty string for the "default" data stream.
            attr_type: The attribute type to find the stream size of.
            allocated: Whether to use the real stream size or the allocated stream size (i.e. include slack space).

        Raises:
            FileNotFoundError: If there are no attributes with the given name and type.
        """
        return self._get_stream_attributes(name, attr_type).size(allocated)

    def dataruns(
        self, name: str = "", attr_type: ATTRIBUTE_TYPE_CODE = ATTRIBUTE_TYPE_CODE.DATA
    ) -> list[tuple[int, int]]:
        """Return the dataruns of the given stream name and type.

        Args:
            name: The stream name, an empty string for the "default" data stream.
            attr_type: The attribute type to get the dataruns of.

        Raises:
            FileNotFoundError: If there are no attributes with the given name and type.
        """
        return self._get_stream_attributes(name, attr_type).dataruns()

    def has_stream(self, name: str = "", attr_type: ATTRIBUTE_TYPE_CODE = ATTRIBUTE_TYPE_CODE.DATA) -> bool:
        """Return whether or not this record has attributes with the given name and type."""
        return bool(self.attributes.find(name, attr_type))

    def index(self, name: str) -> Index:
        """Open an index on this record.

        Args:
            name: The index name to open. For example, ``"$I30"``.
        """
        return Index(self, name)

    def iterdir(self, dereference: bool = False, ignore_dos: bool = False) -> Iterator[IndexEntry | MftRecord]:
        """Yield directory entries of this record.

        Args:
            dereference: Determines whether to resolve the :class:`~dissect.ntfs.index.IndexEntry`'s to :class:`MftRecord`'s. This impacts performance.
            ignore_dos: Ignore DOS file name entries.

        Raises:
            NotADirectoryError: If this record is not a directory.
        """  # noqa: E501
        if not self.is_dir():
            raise NotADirectoryError(f"{self!r} is not a directory")

        for entry in self.index("$I30").entries():
            if ignore_dos and entry.attribute.flags == FILE_NAME_DOS:
                continue
            yield entry.dereference() if dereference else entry

    def listdir(self, dereference: bool = False, ignore_dos: bool = False) -> dict[str, IndexEntry | MftRecord]:
        """Return a dictionary of the directory entries of this record.

        Args:
            dereference: Determines whether to resolve the :class:`~dissect.ntfs.index.IndexEntry`'s to :class:`MftRecord`'s. This impacts performance.
            ignore_dos: Ignore DOS file name entries.

        Raises:
            NotADirectoryError: If this record is not a directory.
        """  # noqa: E501
        result = {}
        for entry in self.iterdir(dereference, ignore_dos):
            filenames = entry.filenames(ignore_dos) if dereference else [entry.attribute.file_name]
            for filename in filenames:
                result[filename] = entry

        return result
