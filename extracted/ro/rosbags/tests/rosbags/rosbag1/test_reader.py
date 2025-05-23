# Copyright 2020 - 2025 Ternaris
# SPDX-License-Identifier: Apache-2.0
"""Reader Tests."""

from __future__ import annotations

from collections import defaultdict
from struct import pack, unpack
from typing import TYPE_CHECKING
from unittest.mock import patch

import pytest

from rosbags.rosbag1 import Reader, ReaderError
from rosbags.rosbag1.reader import IndexData

if TYPE_CHECKING:
    from collections.abc import Sequence
    from pathlib import Path


def serialize(data: dict[str, bytes] | bytes) -> bytes:
    """Serialize record header."""
    if isinstance(data, dict):
        fields: list[bytes] = []
        for key, value in data.items():
            field = b'='.join([key.encode(), value])
            fields.append(pack('<L', len(field)) + field)
        data = b''.join(fields)
    return pack('<L', len(data)) + data


def create_default_header() -> dict[str, bytes]:
    """Create empty rosbag header."""
    return {
        'op': b'\x03',
        'conn_count': pack('<L', 0),
        'chunk_count': pack('<L', 0),
    }


def create_connection(
    cid: int = 1,
    topic: int = 0,
    typ: int = 0,
) -> tuple[dict[str, bytes], dict[str, bytes]]:
    """Create connection record."""
    return {
        'op': b'\x07',
        'conn': pack('<L', cid),
        'topic': f'/topic{topic}'.encode(),
    }, {
        'type': f'foo_msgs/msg/Foo{typ}'.encode(),
        'md5sum': b'AAAA',
        'message_definition': b'MSGDEF',
    }


def create_message(
    cid: int = 1,
    time: int = 0,
    msg: int = 0,
) -> tuple[dict[str, bytes], bytes]:
    """Create message record."""
    return {
        'op': b'\x02',
        'conn': pack('<L', cid),
        'time': pack('<LL', time, 0),
    }, f'MSGCONTENT{msg}'.encode()


def write_bag(
    bag: Path,
    header: dict[str, bytes],
    chunks: Sequence[Sequence[tuple[dict[str, bytes], dict[str, bytes] | bytes]]] = (),
) -> None:
    """Write bag file."""
    magic = b'#ROSBAG V2.0\n'

    pos = 13 + 4096
    conn_count = 0
    chunk_count = len(chunks or [])

    chunks_bytes = b''
    connections = b''
    chunkinfos = b''
    if chunks:
        for chunk in chunks:
            chunk_bytes = b''
            start_time: int = 2**32 - 1
            end_time = 0
            counts: dict[int, int] = defaultdict(int)
            index_count: dict[int, int] = {}
            index_msgs: dict[int, bytes] = {}
            offset = 0

            for head, data in chunk:
                if head.get('op') == b'\x07':
                    conn_count += 1
                    add = serialize(head) + serialize(data)
                    chunk_bytes += add
                    connections += add
                elif head.get('op') == b'\x02':
                    time: int
                    conn: int
                    (time,) = unpack('<Lxxxx', head['time'])
                    (conn,) = unpack('<L', head['conn'])

                    start_time = min([start_time, time])
                    end_time = max([end_time, time])

                    counts[conn] += 1
                    if conn not in index_count:
                        index_count[conn] = 0
                        index_msgs[conn] = b''
                    index_count[conn] += 1
                    index_msgs[conn] += pack('<LLL', time, 0, offset)

                    add = serialize(head) + serialize(data)
                    chunk_bytes += add
                    offset = len(chunk_bytes)
                else:
                    add = serialize(head) + serialize(data)
                    chunk_bytes += add

            chunk_bytes = serialize(
                {
                    'op': b'\x05',
                    'compression': b'none',
                    'size': pack('<L', len(chunk_bytes)),
                },
            ) + serialize(chunk_bytes)
            for cid, count in index_count.items():
                chunk_bytes += serialize(
                    {
                        'op': b'\x04',
                        'ver': pack('<L', 1),
                        'conn': pack('<L', cid),
                        'count': pack('<L', count),
                    },
                ) + serialize(index_msgs[cid])

            chunks_bytes += chunk_bytes
            chunkinfos += serialize(
                {
                    'op': b'\x06',
                    'ver': pack('<L', 1),
                    'chunk_pos': pack('<Q', pos),
                    'start_time': pack('<LL', start_time, 0),
                    'end_time': pack('<LL', end_time, 0),
                    'count': pack('<L', len(counts.keys())),
                },
            ) + serialize(b''.join([pack('<LL', x, y) for x, y in counts.items()]))
            pos += len(chunk_bytes)

    header['conn_count'] = pack('<L', conn_count)
    header['chunk_count'] = pack('<L', chunk_count)
    if 'index_pos' not in header:
        header['index_pos'] = pack('<Q', pos)

    header_bytes = serialize(header)
    header_bytes += b'\x20' * (4096 - len(header_bytes))

    _ = bag.write_bytes(b''.join([magic, header_bytes, chunks_bytes, connections, chunkinfos]))


def test_indexdata() -> None:
    """Test IndexData sort sorder."""
    x42_1_0 = IndexData(42, 1, 0)
    x42_2_0 = IndexData(42, 2, 0)
    x43_3_0 = IndexData(43, 3, 0)

    assert not x42_1_0 < x42_2_0
    assert x42_1_0 <= x42_2_0
    assert x42_1_0 == x42_2_0
    assert not x42_1_0 != x42_2_0  # noqa: SIM202
    assert x42_1_0 >= x42_2_0
    assert not x42_1_0 > x42_2_0

    assert x42_1_0 < x43_3_0
    assert x42_1_0 <= x43_3_0
    assert not x42_1_0 == x43_3_0  # noqa: SIM201
    assert x42_1_0 != x43_3_0
    assert not x42_1_0 >= x43_3_0
    assert not x42_1_0 > x43_3_0


def test_reader(tmp_path: Path) -> None:
    """Test reader reads all messages."""
    # empty bag
    bag = tmp_path / 'test.bag'
    write_bag(bag, create_default_header())
    with Reader(bag) as reader:
        assert reader.message_count == 0
        assert reader.start_time == 2**63 - 1
        assert reader.end_time == 0
        assert reader.duration == 0
        assert not list(reader.messages())

    # empty bag, explicit encryptor
    bag = tmp_path / 'test.bag'
    write_bag(bag, {**create_default_header(), 'encryptor': b''})
    with Reader(bag) as reader:
        assert reader.message_count == 0

    # single message
    write_bag(bag, create_default_header(), chunks=[[create_connection(), create_message(time=42)]])
    with Reader(bag) as reader:
        assert reader.message_count == 1
        assert reader.duration == 1
        assert reader.start_time == 42 * 10**9
        assert reader.end_time == 42 * 10**9 + 1
        assert len(reader.topics.keys()) == 1
        assert reader.topics['/topic0'].msgcount == 1
        msgs = list(reader.messages())
        assert len(msgs) == 1

    # sorts by time on same topic
    write_bag(
        bag,
        create_default_header(),
        chunks=[
            [
                create_connection(),
                create_message(time=10, msg=10),
                create_message(time=5, msg=5),
            ],
        ],
    )
    with Reader(bag) as reader:
        assert reader.message_count == 2
        assert reader.duration == 5 * 10**9 + 1
        assert reader.start_time == 5 * 10**9
        assert reader.end_time == 10 * 10**9 + 1
        assert len(reader.topics.keys()) == 1
        assert reader.topics['/topic0'].msgcount == 2
        msgs = list(reader.messages())
        assert len(msgs) == 2
        assert msgs[0][0].topic == '/topic0'
        assert msgs[0][2] == b'MSGCONTENT5'
        assert msgs[1][0].topic == '/topic0'
        assert msgs[1][2] == b'MSGCONTENT10'

    # sorts by time on different topic
    write_bag(
        bag,
        create_default_header(),
        chunks=[
            [
                create_connection(),
                create_message(time=10, msg=10),
                create_connection(cid=2, topic=2),
                create_message(cid=2, time=5, msg=5),
            ],
        ],
    )
    with Reader(bag) as reader:
        assert len(reader.topics.keys()) == 2
        assert reader.topics['/topic0'].msgcount == 1
        assert reader.topics['/topic2'].msgcount == 1
        msgs = list(reader.messages())
        assert len(msgs) == 2
        assert msgs[0][2] == b'MSGCONTENT5'
        assert msgs[1][2] == b'MSGCONTENT10'

        connections = [x for x in reader.connections if x.topic == '/topic0']
        msgs = list(reader.messages(connections))
        assert len(msgs) == 1
        assert msgs[0][2] == b'MSGCONTENT10'

        msgs = list(reader.messages(start=7 * 10**9))
        assert len(msgs) == 1
        assert msgs[0][2] == b'MSGCONTENT10'

        msgs = list(reader.messages(stop=7 * 10**9))
        assert len(msgs) == 1
        assert msgs[0][2] == b'MSGCONTENT5'


def test_raises_if_user_error(tmp_path: Path) -> None:
    """Test reader raises if user makes error."""
    bag = tmp_path / 'test.bag'
    write_bag(bag, create_default_header(), chunks=[[create_connection(), create_message()]])

    reader = Reader(bag)
    with pytest.raises(ReaderError, match='is not open'):
        _ = next(reader.messages())


def test_failure_cases(tmp_path: Path) -> None:
    """Test failure cases."""
    bag = tmp_path / 'test.bag'
    with pytest.raises(FileNotFoundError, match='does not exist'):
        Reader(bag).open()

    _ = bag.write_text('')
    with (
        pytest.raises(PermissionError),
        patch('pathlib.Path.open', side_effect=PermissionError),
    ):
        Reader(bag).open()

    with (
        patch('pathlib.Path.open', side_effect=IOError),
        pytest.raises(ReaderError, match='not open'),
    ):
        Reader(bag).open()

    with pytest.raises(ReaderError, match='empty'):
        Reader(bag).open()

    _ = bag.write_text('#BADMAGIC')
    with pytest.raises(ReaderError, match='magic is invalid'):
        Reader(bag).open()

    _ = bag.write_text('#ROSBAG V3.0\n')
    with pytest.raises(ReaderError, match='Bag version 300 is not supported.'):
        Reader(bag).open()

    _ = bag.write_bytes(b'#ROSBAG V2.0\x0a\x00')
    with pytest.raises(ReaderError, match='Header could not be read from file.'):
        Reader(bag).open()

    _ = bag.write_bytes(b'#ROSBAG V2.0\x0a\x01\x00\x00\x00')
    with pytest.raises(ReaderError, match='Header could not be read from file.'):
        Reader(bag).open()

    _ = bag.write_bytes(b'#ROSBAG V2.0\x0a\x01\x00\x00\x00\x01')
    with pytest.raises(ReaderError, match='Header field size could not be read.'):
        Reader(bag).open()

    _ = bag.write_bytes(b'#ROSBAG V2.0\x0a\x04\x00\x00\x00\x01\x00\x00\x00')
    with pytest.raises(ReaderError, match='Declared field size is too large for header.'):
        Reader(bag).open()

    _ = bag.write_bytes(b'#ROSBAG V2.0\x0a\x05\x00\x00\x00\x01\x00\x00\x00x')
    with pytest.raises(ReaderError, match='Header field could not be parsed.'):
        Reader(bag).open()

    write_bag(bag, {'encryptor': b'enc', **create_default_header()})
    with pytest.raises(ReaderError, match='is not supported'):
        Reader(bag).open()

    write_bag(bag, {**create_default_header(), 'index_pos': pack('<Q', 0)})
    with pytest.raises(ReaderError, match='Bag is not indexed'):
        Reader(bag).open()

    write_bag(bag, create_default_header(), chunks=[[create_connection(), create_message()]])
    _ = bag.write_bytes(bag.read_bytes().replace(b'none', b'COMP'))
    with pytest.raises(ReaderError, match="Compression 'COMP' is not supported."):
        Reader(bag).open()

    write_bag(bag, create_default_header(), chunks=[[create_connection(), create_message()]])
    _ = bag.write_bytes(bag.read_bytes().replace(b'ver=\x01', b'ver=\x02'))
    with pytest.raises(ReaderError, match='CHUNK_INFO version 2 is not supported.'):
        Reader(bag).open()

    write_bag(bag, create_default_header(), chunks=[[create_connection(), create_message()]])
    _ = bag.write_bytes(bag.read_bytes().replace(b'ver=\x01', b'ver=\x02', 1))
    with pytest.raises(ReaderError, match='IDXDATA version 2 is not supported.'):
        Reader(bag).open()

    write_bag(bag, create_default_header(), chunks=[[create_connection(), create_message()]])
    _ = bag.write_bytes(bag.read_bytes().replace(b'op=\x02', b'op=\x00', 1))
    with Reader(bag) as reader, pytest.raises(ReaderError, match='Expected to find message data.'):
        _ = next(reader.messages())

    write_bag(bag, create_default_header(), chunks=[[create_connection(), create_message()]])
    _ = bag.write_bytes(bag.read_bytes().replace(b'op=\x03', b'op=\x02', 1))
    with pytest.raises(ReaderError, match="Record of type 'MSGDATA' is unexpected."):
        Reader(bag).open()

    # bad uint8 field
    write_bag(
        bag,
        create_default_header(),
        chunks=[
            [
                ({}, {}),
                create_connection(),
                create_message(),
            ]
        ],
    )
    with Reader(bag) as reader, pytest.raises(ReaderError, match="field 'op'"):
        _ = next(reader.messages())

    # bad uint32, uint64, time field
    for name in ('conn_count', 'chunk_pos', 'time'):
        write_bag(bag, create_default_header(), chunks=[[create_connection(), create_message()]])
        _ = bag.write_bytes(bag.read_bytes().replace(name.encode(), b'x' * len(name), 1))
        if name == 'time':
            with pytest.raises(ReaderError, match=f"field '{name}'"), Reader(bag) as reader:
                _ = next(reader.messages())
        else:
            with pytest.raises(ReaderError, match=f"field '{name}'"):
                Reader(bag).open()
