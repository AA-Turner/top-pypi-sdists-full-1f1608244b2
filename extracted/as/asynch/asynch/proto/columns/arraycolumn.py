from itertools import chain
from queue import Queue
from struct import Struct

from .base import Column
from .intcolumn import UInt64Column


class ArrayColumn(Column):
    """
    Nested arrays written in flatten form after information about their
    sizes (offsets really).
    One element of array of arrays can be represented as tree:
    (0 depth)          [[3, 4], [5, 6]]
                      |               |
    (1 depth)      [3, 4]           [5, 6]
                   |    |           |    |
    (leaf)        3     4          5     6

    Offsets (sizes) written in breadth-first search order. In example above
    following sequence of offset will be written: 4 -> 2 -> 4
    1) size of whole array: 4
    2) size of array 1 in depth=1: 2
    3) size of array 2 plus size of all array before in depth=1: 2 + 2 = 4

    After sizes info comes flatten data: 3 -> 4 -> 5 -> 6
    """

    py_types = (list, tuple)
    size_struct = Struct("<Q")

    def __init__(self, nested_column, **kwargs):
        kwargs.update(dict(reader=nested_column.reader, writer=nested_column.writer))
        self.size_column = UInt64Column(**kwargs)
        self.nested_column = nested_column
        self._write_depth_0_size = True
        super().__init__(**kwargs)
        self.null_value = []

    def size_pack(self, value):
        return self.size_struct.pack(value)

    async def size_unpack(
        self,
    ):
        return self.size_struct.unpack(await self.reader.read_bytes(self.size_struct.size))[0]

    async def write_items(
        self,
        items,
    ):
        return await self.write_data(
            items,
        )

    async def write_data(
        self,
        data,
    ):
        # Column of Array(T) is stored in "compact" format and passed to server
        # wrapped into another Array without size of wrapper array.
        self.nested_column = ArrayColumn(self.nested_column)
        self.nested_column.nullable = self.nullable
        self.nullable = False
        self._write_depth_0_size = False
        await self._write(
            data,
        )

    async def read_data(
        self,
        rows,
    ):
        self.nested_column = ArrayColumn(self.nested_column)
        self.nested_column.nullable = self.nullable
        self.nullable = False
        return await self._read(
            rows,
        )

    async def _write_sizes(
        self,
        value,
    ):
        q = Queue()
        q.put((self, value, 0))

        cur_depth = 0
        offset = 0
        nulls_map = []

        while not q.empty():
            column, value, depth = q.get_nowait()

            if cur_depth != depth:
                cur_depth = depth
                offset = 0
                if column.nullable:
                    await self._write_nulls_map(
                        nulls_map,
                    )

                nulls_map = []

            if column.nullable:
                value = value or []

            offset += len(value)
            if (cur_depth == 0 and self._write_depth_0_size) or cur_depth > 0:
                await self.writer.write_bytes(self.size_pack(offset))

            nested_column = column.nested_column
            if isinstance(nested_column, ArrayColumn):
                for x in value:
                    q.put((nested_column, x, cur_depth + 1))
                    nulls_map.append(None if x is None else False)

    async def _write_data(
        self,
        value,
    ):
        if self.nullable:
            value = value or []

        if isinstance(self.nested_column, ArrayColumn):
            value = list(chain.from_iterable(value))

        await self.nested_column._write_data(
            value,
        )

    async def _write_nulls_data(
        self,
        value,
    ):
        if self.nullable:
            value = value or []

        if isinstance(self.nested_column, ArrayColumn):
            value = list(chain.from_iterable(value))
            await self.nested_column._write_nulls_data(
                value,
            )
        else:
            if self.nested_column.nullable:
                await self.nested_column._write_nulls_map(
                    value,
                )

    async def _write(
        self,
        value,
    ):
        value = self.prepare_items(value)
        await self._write_sizes(
            value,
        )
        await self._write_nulls_data(
            value,
        )
        await self._write_data(
            value,
        )

    async def read_state_prefix(
        self,
    ):
        return await self.nested_column.read_state_prefix()

    async def write_state_prefix(
        self,
    ):
        await self.nested_column.write_state_prefix()

    async def _read(
        self,
        size,
    ):
        q = Queue()
        q.put((self, size, 0))

        slices_series = []

        cur_depth = 0
        prev_offset = 0
        slices = []

        if self.nested_column.nullable:
            nulls_map = await self._read_nulls_map(
                size,
            )
        else:
            nulls_map = [0] * size

        nested_column_size = size
        nested_column = self.nested_column

        # Read and store info about slices.
        while not q.empty():
            column, size, depth = q.get_nowait()

            nested_column = column.nested_column

            if cur_depth != depth:
                cur_depth = depth

                slices_series.append((slices, nulls_map))

                if nested_column.nullable:
                    nulls_map = await self._read_nulls_map(
                        prev_offset,
                    )
                else:
                    nulls_map = [0] * prev_offset

                prev_offset = 0
                slices = []

            if isinstance(nested_column, ArrayColumn):
                for _i in range(size):
                    offset = await self.size_unpack()
                    nested_column_size = offset
                    q.put((nested_column, offset - prev_offset, cur_depth + 1))
                    slices.append((prev_offset, offset))
                    prev_offset = offset

            # Read data
            else:
                prev_offset += size

        data = []
        if nested_column_size:
            data = await nested_column._read_data(nested_column_size, nulls_map=nulls_map)

        # Build nested tuple structure.
        for slices, nulls_map in reversed(slices_series):
            nested_data = []
            for (slice_from, slice_to), is_null in zip(slices, nulls_map):
                nested_data.append(None if is_null else list(data[slice_from:slice_to]))

            data = nested_data

        return tuple(data)


def create_array_column(spec, column_by_spec_getter, column_options):
    inner = spec[6:-1]
    return ArrayColumn(column_by_spec_getter(inner), **column_options)
