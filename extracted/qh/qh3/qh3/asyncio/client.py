from __future__ import annotations

import asyncio
import ipaddress
import socket
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Callable, cast

from ..quic.configuration import QuicConfiguration
from ..quic.connection import QuicConnection
from ..tls import SessionTicketHandler
from .protocol import QuicConnectionProtocol, QuicStreamHandler

__all__ = ["connect"]

# keep compatibility for Python 3.7 on Windows
if not hasattr(socket, "IPPROTO_IPV6"):
    socket.IPPROTO_IPV6 = 41


@asynccontextmanager
async def connect(
    host: str,
    port: int,
    *,
    configuration: QuicConfiguration | None = None,
    create_protocol: Callable | None = QuicConnectionProtocol,
    session_ticket_handler: SessionTicketHandler | None = None,
    stream_handler: QuicStreamHandler | None = None,
    wait_connected: bool = True,
    local_port: int = 0,
) -> AsyncGenerator[QuicConnectionProtocol]:
    """
    Connect to a QUIC server at the given `host` and `port`.

    :meth:`connect()` returns an awaitable. Awaiting it yields a
    :class:`~qh3.asyncio.QuicConnectionProtocol` which can be used to
    create streams.

    :func:`connect` also accepts the following optional arguments:

    * ``configuration`` is a :class:`~qh3.quic.configuration.QuicConfiguration`
      configuration object.
    * ``create_protocol`` allows customizing the :class:`~asyncio.Protocol` that
      manages the connection. It should be a callable or class accepting the same
      arguments as :class:`~qh3.asyncio.QuicConnectionProtocol` and returning
      an instance of :class:`~qh3.asyncio.QuicConnectionProtocol` or a subclass.
    * ``session_ticket_handler`` is a callback which is invoked by the TLS
      engine when a new session ticket is received.
    * ``stream_handler`` is a callback which is invoked whenever a stream is
      created. It must accept two arguments: a :class:`asyncio.StreamReader`
      and a :class:`asyncio.StreamWriter`.
    * ``local_port`` is the UDP port number that this client wants to bind.
    """
    loop = asyncio.get_running_loop()
    local_host = "::"

    # if host is not an IP address, pass it to enable SNI
    try:
        ipaddress.ip_address(host)
        server_name = None
    except ValueError:
        server_name = host

    # lookup remote address
    infos = await loop.getaddrinfo(host, port, type=socket.SOCK_DGRAM)
    addr = infos[0][4]
    if len(addr) == 2:
        addr = ("::ffff:" + addr[0], addr[1], 0, 0)

    # prepare QUIC connection
    if configuration is None:
        configuration = QuicConfiguration(is_client=True)
    if configuration.server_name is None:
        configuration.server_name = server_name
    connection = QuicConnection(
        configuration=configuration, session_ticket_handler=session_ticket_handler
    )

    # explicitly enable IPv4/IPv6 dual stack
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    completed = False
    try:
        sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
        sock.bind((local_host, local_port, 0, 0))
        completed = True
    finally:
        if not completed:
            sock.close()
    # connect
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: create_protocol(connection, stream_handler=stream_handler),
        sock=sock,
    )
    protocol = cast(QuicConnectionProtocol, protocol)
    try:
        protocol.connect(addr)
        if wait_connected:
            await protocol.wait_connected()
        yield protocol
    finally:
        protocol.close()
        await protocol.wait_closed()
        transport.close()
