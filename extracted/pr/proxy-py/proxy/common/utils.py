# -*- coding: utf-8 -*-
"""
    proxy.py
    ~~~~~~~~
    ⚡⚡⚡ Fast, Lightweight, Pluggable, TLS interception capable proxy server focused on
    Network monitoring, controls & Application development, testing, debugging.

    :copyright: (c) 2013-present by Abhinav Singh and contributors.
    :license: BSD, see LICENSE for more details.

    .. spelling::

       utils
"""
import os
import ssl
import sys
import socket
import logging
import argparse
import tempfile
import functools
import ipaddress
import contextlib
from types import TracebackType
from typing import Any, Dict, List, Type, Tuple, Callable, Optional

from .types import HostPort
from .constants import (
    CRLF, COLON, HTTP_1_1, IS_WINDOWS, WHITESPACE, DEFAULT_TIMEOUT,
    DEFAULT_THREADLESS, DEFAULT_CONNECT_TIMEOUT, PROXY_AGENT_HEADER_VALUE,
    DEFAULT_SSL_CONTEXT_OPTIONS,
)


if not IS_WINDOWS:  # pragma: no cover
    import resource

logger = logging.getLogger(__name__)


def cert_der_to_dict(der: Optional[bytes]) -> Dict[str, Any]:
    """Parse a DER formatted certificate to a python dict"""
    # pylint: disable=import-outside-toplevel
    import _ssl  # noqa: WPS436

    if not der:
        return {}
    with tempfile.NamedTemporaryFile(delete=False) as cert_file:
        pem = ssl.DER_cert_to_PEM_cert(der)
        cert_file.write(pem.encode())
        cert_file.flush()
        cert_file.seek(0)
    try:
        certificate = _ssl._test_decode_cert(cert_file.name)
    finally:
        cert_file.close()
        os.remove(cert_file.name)
    return certificate or {}


def tls_interception_enabled(flags: argparse.Namespace) -> bool:
    return flags.ca_key_file is not None and \
        flags.ca_cert_dir is not None and \
        flags.ca_signing_key_file is not None and \
        flags.ca_cert_file is not None


def is_threadless(threadless: bool, threaded: bool) -> bool:
    # if default is threadless then return true unless
    # user has overridden mode using threaded flag.
    #
    # if default is not threadless then return true
    # only if user has overridden using --threadless flag
    return (DEFAULT_THREADLESS and not threaded) or (not DEFAULT_THREADLESS and threadless)


def is_py2() -> bool:
    """Exists only to avoid mocking :data:`sys.version_info` in tests."""
    return sys.version_info.major == 2


def text_(s: Any, encoding: str = 'utf-8', errors: str = 'strict') -> Any:
    """Utility to ensure text-like usability.

    If s is of type bytes or int, return s.decode(encoding, errors),
    otherwise return s as it is."""
    if isinstance(s, int):
        return str(s)
    if isinstance(s, bytes):
        return s.decode(encoding, errors)
    return s


def bytes_(s: Any, encoding: str = 'utf-8', errors: str = 'strict') -> Any:
    """Utility to ensure binary-like usability.

    If s is type str or int, return s.encode(encoding, errors),
    otherwise return s as it is."""
    if isinstance(s, int):
        s = str(s)
    if isinstance(s, str):
        return s.encode(encoding, errors)
    return s


def build_http_request(
    method: bytes, url: bytes,
    protocol_version: bytes = HTTP_1_1,
    content_type: Optional[bytes] = None,
    headers: Optional[Dict[bytes, bytes]] = None,
    body: Optional[bytes] = None,
    conn_close: bool = False,
    no_ua: bool = False,
) -> bytes:
    """Build and returns a HTTP request packet."""
    headers = headers or {}
    if content_type is not None:
        headers[b'Content-Type'] = content_type
    has_transfer_encoding = False
    has_user_agent = False
    for k, _ in headers.items():
        if k.lower() == b'transfer-encoding':
            has_transfer_encoding = True
        elif k.lower() == b'user-agent':
            has_user_agent = True
    if body and not has_transfer_encoding:
        headers[b'Content-Length'] = bytes_(len(body))
    if not has_user_agent and not no_ua:
        headers[b'User-Agent'] = PROXY_AGENT_HEADER_VALUE
    return build_http_pkt(
        [method, url, protocol_version],
        headers,
        body,
        conn_close,
    )


def build_http_response(
    status_code: int,
    protocol_version: bytes = HTTP_1_1,
    reason: Optional[bytes] = None,
    headers: Optional[Dict[bytes, bytes]] = None,
    body: Optional[bytes] = None,
    conn_close: bool = False,
    no_cl: bool = False,
) -> bytes:
    """Build and returns a HTTP response packet."""
    line = [protocol_version, bytes_(status_code)]
    if reason:
        line.append(reason)
    headers = headers or {}
    has_transfer_encoding = False
    for k, _ in headers.items():
        if k.lower() == b'transfer-encoding':
            has_transfer_encoding = True
            break
    if not has_transfer_encoding and not no_cl:
        headers[b'Content-Length'] = bytes_(len(body)) if body else b'0'
    return build_http_pkt(line, headers, body, conn_close)


def build_http_header(k: bytes, v: bytes) -> bytes:
    """Build and return a HTTP header line for use in raw packet."""
    return k + COLON + WHITESPACE + v


def build_http_pkt(
    line: List[bytes],
    headers: Optional[Dict[bytes, bytes]] = None,
    body: Optional[bytes] = None,
    conn_close: bool = False,
) -> bytes:
    """Build and returns a HTTP request or response packet."""
    pkt = WHITESPACE.join(line) + CRLF
    headers = headers or {}
    if conn_close:
        headers[b'Connection'] = b'close'
    for k, v in headers.items():
        pkt += build_http_header(k, v) + CRLF
    pkt += CRLF
    if body:
        pkt += body
    return pkt


def build_websocket_handshake_request(
        key: bytes,
        method: bytes = b'GET',
        url: bytes = b'/',
        host: bytes = b'localhost',
) -> bytes:
    """
    Build and returns a Websocket handshake request packet.

    :param key: Sec-WebSocket-Key header value.
    :param method: HTTP method.
    :param url: Websocket request path.
    """
    return build_http_request(
        method, url,
        headers={
            b'Host': host,
            b'Connection': b'upgrade',
            b'Upgrade': b'websocket',
            b'Sec-WebSocket-Key': key,
            b'Sec-WebSocket-Version': b'13',
        },
    )


def build_websocket_handshake_response(accept: bytes) -> bytes:
    """
    Build and returns a Websocket handshake response packet.

    :param accept: Sec-WebSocket-Accept header value
    """
    return build_http_response(
        101, reason=b'Switching Protocols',
        headers={
            b'Upgrade': b'websocket',
            b'Connection': b'Upgrade',
            b'Sec-WebSocket-Accept': accept,
        },
    )


def find_http_line(raw: bytes) -> Tuple[Optional[bytes], bytes]:
    """Find and returns first line ending in CRLF along with following buffer.

    If no ending CRLF is found, line is None."""
    parts = raw.split(CRLF, 1)
    return (None, raw) \
        if len(parts) == 1 \
        else (parts[0], parts[1])


def wrap_socket(
        conn: socket.socket,
        keyfile: str,
        certfile: str,
        cafile: Optional[str] = None,
) -> ssl.SSLSocket:
    """Use this to upgrade server_side socket to TLS."""
    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH, cafile=cafile)
    ctx.options |= DEFAULT_SSL_CONTEXT_OPTIONS
    ctx.verify_mode = ssl.CERT_NONE
    ctx.load_cert_chain(certfile=certfile, keyfile=keyfile)
    return ctx.wrap_socket(conn, server_side=True)


def new_socket_connection(
    addr: HostPort,
    timeout: float = DEFAULT_TIMEOUT,
    connect_timeout: float = DEFAULT_CONNECT_TIMEOUT,
    source_address: Optional[HostPort] = None,
) -> socket.socket:
    conn = None
    try:
        ip = ipaddress.ip_address(addr[0])
        if ip.version == 4:
            conn = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM, 0,
            )
            conn.settimeout(connect_timeout)
            conn.connect(addr)
        else:
            conn = socket.socket(
                socket.AF_INET6, socket.SOCK_STREAM, 0,
            )
            conn.settimeout(connect_timeout)
            conn.connect((addr[0], addr[1], 0, 0))
    except ValueError:
        pass    # does not appear to be an IPv4 or IPv6 address

    if conn is not None:
        conn.settimeout(timeout)
        return conn

    # try to establish dual stack IPv4/IPv6 connection.
    conn = socket.create_connection(
        addr,
        timeout=connect_timeout,
        source_address=source_address,
    )
    conn.settimeout(timeout)
    return conn


class socket_connection(contextlib.ContextDecorator):
    """Same as new_socket_connection but as a context manager and decorator."""

    def __init__(self, addr: HostPort):
        self.addr: HostPort = addr
        self.conn: Optional[socket.socket] = None
        super().__init__()

    def __enter__(self) -> socket.socket:
        self.conn = new_socket_connection(self.addr)
        return self.conn

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType],
    ) -> None:
        if self.conn:
            self.conn.close()

    def __call__(   # type: ignore
            self, func: Callable[..., Any],
    ) -> Callable[[Tuple[Any, ...], Dict[str, Any]], Any]:
        @functools.wraps(func)
        def decorated(*args: Any, **kwargs: Any) -> Any:
            with self as conn:
                return func(conn, *args, **kwargs)
        return decorated


def get_available_port() -> int:
    """Finds and returns an available port on the system."""
    with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.bind(('', 0))
        _, port = sock.getsockname()
    return int(port)


def set_open_file_limit(soft_limit: int) -> None:
    """Configure open file description soft limit on supported OS."""
    # resource module not available on Windows OS
    if IS_WINDOWS:  # pragma: no cover
        return

    # pylint: disable=possibly-used-before-assignment
    curr_soft_limit, curr_hard_limit = resource.getrlimit(
        resource.RLIMIT_NOFILE,
    )
    if curr_soft_limit < soft_limit < curr_hard_limit:
        resource.setrlimit(
            resource.RLIMIT_NOFILE, (soft_limit, curr_hard_limit),
        )
        logger.debug(
            'Open file soft limit set to %d', soft_limit,
        )
