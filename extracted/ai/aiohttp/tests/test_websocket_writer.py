import asyncio
import random
from typing import Any, Callable
from unittest import mock

import pytest

from aiohttp import WSMsgType
from aiohttp._websocket.reader import WebSocketDataQueue
from aiohttp.http import WebSocketReader, WebSocketWriter


@pytest.fixture
def protocol():
    ret = mock.Mock()
    ret._drain_helper = mock.AsyncMock()
    return ret


@pytest.fixture
def transport():
    ret = mock.Mock()
    ret.is_closing.return_value = False
    return ret


@pytest.fixture
def writer(protocol, transport):
    return WebSocketWriter(protocol, transport, use_mask=False)


async def test_pong(writer: WebSocketWriter) -> None:
    await writer.send_frame(b"", WSMsgType.PONG)
    writer.transport.write.assert_called_with(b"\x8a\x00")  # type: ignore[attr-defined]


async def test_ping(writer: WebSocketWriter) -> None:
    await writer.send_frame(b"", WSMsgType.PING)
    writer.transport.write.assert_called_with(b"\x89\x00")  # type: ignore[attr-defined]


async def test_send_text(writer: WebSocketWriter) -> None:
    await writer.send_frame(b"text", WSMsgType.TEXT)
    writer.transport.write.assert_called_with(b"\x81\x04text")  # type: ignore[attr-defined]


async def test_send_binary(writer: WebSocketWriter) -> None:
    await writer.send_frame(b"binary", WSMsgType.BINARY)
    writer.transport.write.assert_called_with(b"\x82\x06binary")  # type: ignore[attr-defined]


async def test_send_binary_long(writer: WebSocketWriter) -> None:
    await writer.send_frame(b"b" * 127, WSMsgType.BINARY)
    assert writer.transport.write.call_args[0][0].startswith(b"\x82~\x00\x7fb")  # type: ignore[attr-defined]


async def test_send_binary_very_long(writer: WebSocketWriter) -> None:
    await writer.send_frame(b"b" * 65537, WSMsgType.BINARY)
    assert (
        writer.transport.write.call_args_list[0][0][0]
        == b"\x82\x7f\x00\x00\x00\x00\x00\x01\x00\x01"
    )
    assert writer.transport.write.call_args_list[1][0][0] == b"b" * 65537


async def test_close(writer) -> None:
    await writer.close(1001, "msg")
    writer.transport.write.assert_called_with(b"\x88\x05\x03\xe9msg")

    await writer.close(1001, b"msg")
    writer.transport.write.assert_called_with(b"\x88\x05\x03\xe9msg")

    # Test that Service Restart close code is also supported
    await writer.close(1012, b"msg")
    writer.transport.write.assert_called_with(b"\x88\x05\x03\xf4msg")


async def test_send_text_masked(protocol, transport) -> None:
    writer = WebSocketWriter(
        protocol, transport, use_mask=True, random=random.Random(123)
    )
    await writer.send_frame(b"text", WSMsgType.TEXT)
    writer.transport.write.assert_called_with(b"\x81\x84\rg\xb3fy\x02\xcb\x12")  # type: ignore[attr-defined]


async def test_send_compress_text(protocol, transport) -> None:
    writer = WebSocketWriter(protocol, transport, compress=15)
    await writer.send_frame(b"text", WSMsgType.TEXT)
    writer.transport.write.assert_called_with(b"\xc1\x06*I\xad(\x01\x00")  # type: ignore[attr-defined]
    await writer.send_frame(b"text", WSMsgType.TEXT)
    writer.transport.write.assert_called_with(b"\xc1\x05*\x01b\x00\x00")  # type: ignore[attr-defined]


async def test_send_compress_text_notakeover(protocol, transport) -> None:
    writer = WebSocketWriter(protocol, transport, compress=15, notakeover=True)
    await writer.send_frame(b"text", WSMsgType.TEXT)
    writer.transport.write.assert_called_with(b"\xc1\x06*I\xad(\x01\x00")  # type: ignore[attr-defined]
    await writer.send_frame(b"text", WSMsgType.TEXT)
    writer.transport.write.assert_called_with(b"\xc1\x06*I\xad(\x01\x00")  # type: ignore[attr-defined]


async def test_send_compress_text_per_message(protocol, transport) -> None:
    writer = WebSocketWriter(protocol, transport)
    await writer.send_frame(b"text", WSMsgType.TEXT, compress=15)
    writer.transport.write.assert_called_with(b"\xc1\x06*I\xad(\x01\x00")  # type: ignore[attr-defined]
    await writer.send_frame(b"text", WSMsgType.TEXT)
    writer.transport.write.assert_called_with(b"\x81\x04text")  # type: ignore[attr-defined]
    await writer.send_frame(b"text", WSMsgType.TEXT, compress=15)
    writer.transport.write.assert_called_with(b"\xc1\x06*I\xad(\x01\x00")  # type: ignore[attr-defined]


@pytest.mark.parametrize(
    ("max_sync_chunk_size", "payload_point_generator"),
    (
        (16, lambda count: count),
        (4096, lambda count: count),
        (32, lambda count: 64 + count if count % 2 else count),
    ),
)
@pytest.mark.usefixtures("parametrize_zlib_backend")
async def test_concurrent_messages(
    protocol: Any,
    transport: Any,
    max_sync_chunk_size: int,
    payload_point_generator: Callable[[int], int],
) -> None:
    """Ensure messages are compressed correctly when there are multiple concurrent writers.

    This test generates is parametrized to

    - Generate messages that are larger than patch
      WEBSOCKET_MAX_SYNC_CHUNK_SIZE of 16
      where compression will run in the executor

    - Generate messages that are smaller than patch
      WEBSOCKET_MAX_SYNC_CHUNK_SIZE of 4096
      where compression will run in the event loop

    - Interleave generated messages with a
      WEBSOCKET_MAX_SYNC_CHUNK_SIZE of 32
      where compression will run in the event loop
      and in the executor
    """
    with mock.patch(
        "aiohttp._websocket.writer.WEBSOCKET_MAX_SYNC_CHUNK_SIZE", max_sync_chunk_size
    ):
        writer = WebSocketWriter(protocol, transport, compress=15)
        loop = asyncio.get_running_loop()
        queue = WebSocketDataQueue(mock.Mock(_reading_paused=False), 2**16, loop=loop)
        reader = WebSocketReader(queue, 50000)
        writers = []
        payloads = []
        for count in range(1, 64 + 1):
            point = payload_point_generator(count)
            payload = bytes((point,)) * point
            payloads.append(payload)
            writers.append(writer.send_frame(payload, WSMsgType.BINARY))
        await asyncio.gather(*writers)

    for call in writer.transport.write.call_args_list:
        call_bytes = call[0][0]
        result, _ = reader.feed_data(call_bytes)
        assert result is False
        msg = await queue.read()
        bytes_data: bytes = msg.data
        first_char = bytes_data[0:1]
        char_val = ord(first_char)
        assert len(bytes_data) == char_val
        # If we have a concurrency problem, the data
        # tends to get mixed up between messages so
        # we want to validate that all the bytes are
        # the same value
        assert bytes_data == bytes_data[0:1] * char_val
