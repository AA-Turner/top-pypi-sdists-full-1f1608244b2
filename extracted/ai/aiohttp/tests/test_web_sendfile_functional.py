import asyncio
import bz2
import gzip
import pathlib
import socket
from typing import Any, Iterable, Optional
from unittest import mock

import pytest

import aiohttp
from aiohttp import web
from aiohttp.compression_utils import ZLibBackend
from aiohttp.pytest_plugin import AiohttpClient

try:
    import brotlicffi as brotli
except ImportError:
    import brotli

try:
    import ssl
except ImportError:
    ssl = None  # type: ignore


HELLO_AIOHTTP = b"Hello aiohttp! :-)\n"


@pytest.fixture(scope="module")
def hello_txt(request, tmp_path_factory) -> pathlib.Path:
    """Create a temp path with hello.txt and compressed versions.

    The uncompressed text file path is returned by default. Alternatively, an
    indirect parameter can be passed with an encoding to get a compressed path.
    """
    txt = tmp_path_factory.mktemp("hello-") / "hello.txt"
    hello = {
        None: txt,
        "gzip": txt.with_suffix(f"{txt.suffix}.gz"),
        "br": txt.with_suffix(f"{txt.suffix}.br"),
        "bzip2": txt.with_suffix(f"{txt.suffix}.bz2"),
    }
    # Uncompressed file is not actually written to test it is not required.
    hello["gzip"].write_bytes(gzip.compress(HELLO_AIOHTTP))
    hello["br"].write_bytes(brotli.compress(HELLO_AIOHTTP))
    hello["bzip2"].write_bytes(bz2.compress(HELLO_AIOHTTP))
    encoding = getattr(request, "param", None)
    return hello[encoding]


@pytest.fixture
def loop_with_mocked_native_sendfile(loop: Any):
    def sendfile(transport, fobj, offset, count):
        if count == 0:
            raise ValueError("count must be a positive integer (got 0)")
        raise NotImplementedError

    loop.sendfile = sendfile
    return loop


@pytest.fixture(params=["sendfile", "no_sendfile"], ids=["sendfile", "no_sendfile"])
def sender(request: Any, loop: Any):
    sendfile_mock = None

    def maker(*args, **kwargs):
        ret = web.FileResponse(*args, **kwargs)
        rloop = asyncio.get_running_loop()
        is_patched = rloop.sendfile is sendfile_mock
        assert is_patched if request.param == "no_sendfile" else not is_patched
        return ret

    if request.param == "no_sendfile":
        with mock.patch.object(
            loop,
            "sendfile",
            autospec=True,
            spec_set=True,
            side_effect=NotImplementedError,
        ) as sendfile_mock:
            yield maker
    else:
        yield maker


@pytest.fixture
def app_with_static_route(sender):
    filename = "data.unknown_mime_type"
    filepath = pathlib.Path(__file__).parent / filename

    async def handler(request):
        return sender(filepath)

    app = web.Application()
    app.router.add_get("/", handler)
    return app


async def test_static_file_ok(
    aiohttp_client: Any,
    app_with_static_route: web.Application,
) -> None:
    client = await aiohttp_client(app_with_static_route)

    resp = await client.get("/")
    assert resp.status == 200
    txt = await resp.text()
    assert "file content" == txt.rstrip()
    assert "application/octet-stream" == resp.headers["Content-Type"]
    assert resp.headers.get("Content-Encoding") is None
    await resp.release()
    await client.close()


async def test_zero_bytes_file_ok(aiohttp_client, sender) -> None:
    filepath = pathlib.Path(__file__).parent / "data.zero_bytes"

    async def handler(request):
        return sender(filepath)

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    # Run the request multiple times to ensure
    # that an untrapped exception is not hidden
    # because there is no read of the zero bytes
    for i in range(2):
        resp = await client.get("/")
        assert resp.status == 200
        txt = await resp.text()
        assert "" == txt.rstrip()
        assert "application/octet-stream" == resp.headers["Content-Type"]
        assert resp.headers.get("Content-Encoding") is None
        await resp.release()

    await client.close()


async def test_zero_bytes_file_mocked_native_sendfile(
    aiohttp_client: Any, loop_with_mocked_native_sendfile: Any
) -> None:
    filepath = pathlib.Path(__file__).parent / "data.zero_bytes"

    async def handler(request):
        asyncio.set_event_loop(loop_with_mocked_native_sendfile)
        return web.FileResponse(filepath)

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    # Run the request multiple times to ensure
    # that an untrapped exception is not hidden
    # because there is no read of the zero bytes
    for i in range(2):
        resp = await client.get("/")
        assert resp.status == 200
        txt = await resp.text()
        assert "" == txt.rstrip()
        assert "application/octet-stream" == resp.headers["Content-Type"]
        assert resp.headers.get("Content-Encoding") is None
        assert resp.headers.get("Content-Length") == "0"
        await resp.release()

    await client.close()


async def test_static_file_ok_string_path(
    aiohttp_client: Any,
    app_with_static_route: web.Application,
) -> None:
    client = await aiohttp_client(app_with_static_route)

    resp = await client.get("/")
    assert resp.status == 200
    txt = await resp.text()
    assert "file content" == txt.rstrip()
    assert "application/octet-stream" == resp.headers["Content-Type"]
    assert resp.headers.get("Content-Encoding") is None
    await resp.release()
    await client.close()


async def test_static_file_not_exists(aiohttp_client) -> None:

    app = web.Application()
    client = await aiohttp_client(app)

    resp = await client.get("/fake")
    assert resp.status == 404
    await resp.release()
    await client.close()


async def test_static_file_name_too_long(aiohttp_client) -> None:

    app = web.Application()
    client = await aiohttp_client(app)

    resp = await client.get("/x*500")
    assert resp.status == 404
    await resp.release()
    await client.close()


async def test_static_file_upper_directory(aiohttp_client) -> None:

    app = web.Application()
    client = await aiohttp_client(app)

    resp = await client.get("/../../")
    assert resp.status == 404
    await resp.release()
    await client.close()


async def test_static_file_with_content_type(aiohttp_client, sender) -> None:
    filepath = pathlib.Path(__file__).parent / "aiohttp.jpg"

    async def handler(request):
        return sender(filepath, chunk_size=16)

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/")
    assert resp.status == 200
    body = await resp.read()
    with filepath.open("rb") as f:
        content = f.read()
        assert content == body
    assert resp.headers["Content-Type"] == "image/jpeg"
    assert resp.headers.get("Content-Encoding") is None
    resp.close()
    await resp.release()
    await client.close()


@pytest.mark.parametrize("hello_txt", ["gzip", "br"], indirect=True)
async def test_static_file_custom_content_type(
    hello_txt: pathlib.Path, aiohttp_client: Any, sender: Any
) -> None:
    """Test that custom type without encoding is returned for encoded request."""

    async def handler(request):
        resp = sender(hello_txt, chunk_size=16)
        resp.content_type = "application/pdf"
        return resp

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/")
    assert resp.status == 200
    assert resp.headers.get("Content-Encoding") is None
    assert resp.headers["Content-Type"] == "application/pdf"
    assert await resp.read() == hello_txt.read_bytes()
    resp.close()
    await resp.release()
    await client.close()


@pytest.mark.parametrize(
    ("accept_encoding", "expect_encoding"),
    [("gzip, deflate", "gzip"), ("gzip, deflate, br", "br")],
)
async def test_static_file_custom_content_type_compress(
    hello_txt: pathlib.Path,
    aiohttp_client: Any,
    sender: Any,
    accept_encoding: str,
    expect_encoding: str,
):
    """Test that custom type with encoding is returned for unencoded requests."""

    async def handler(request):
        resp = sender(hello_txt, chunk_size=16)
        resp.content_type = "application/pdf"
        return resp

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/", headers={"Accept-Encoding": accept_encoding})
    assert resp.status == 200
    assert resp.headers.get("Content-Encoding") == expect_encoding
    assert resp.headers["Content-Type"] == "application/pdf"
    assert await resp.read() == HELLO_AIOHTTP
    resp.close()
    await resp.release()
    await client.close()


@pytest.mark.parametrize(
    ("accept_encoding", "expect_encoding"),
    [("gzip, deflate", "gzip"), ("gzip, deflate, br", "br")],
)
@pytest.mark.parametrize("forced_compression", [None, web.ContentCoding.gzip])
@pytest.mark.usefixtures("parametrize_zlib_backend")
async def test_static_file_with_encoding_and_enable_compression(
    hello_txt: pathlib.Path,
    aiohttp_client: Any,
    sender: Any,
    accept_encoding: str,
    expect_encoding: str,
    forced_compression: Optional[web.ContentCoding],
):
    """Test that enable_compression does not double compress when an encoded file is also present."""

    async def handler(request):
        resp = sender(hello_txt)
        resp.enable_compression(forced_compression)
        return resp

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/", headers={"Accept-Encoding": accept_encoding})
    assert resp.status == 200
    assert resp.headers.get("Content-Encoding") == expect_encoding
    assert resp.headers["Content-Type"] == "text/plain"
    assert await resp.read() == HELLO_AIOHTTP
    resp.close()
    await resp.release()
    await client.close()


@pytest.mark.parametrize(
    ("hello_txt", "expect_type"),
    [
        ("gzip", "application/gzip"),
        ("br", "application/x-brotli"),
        ("bzip2", "application/x-bzip2"),
    ],
    indirect=["hello_txt"],
)
async def test_static_file_with_content_encoding(
    hello_txt: pathlib.Path, aiohttp_client: Any, sender: Any, expect_type: str
) -> None:
    """Test requesting static compressed files returns the correct content type and encoding."""

    async def handler(request):
        return sender(hello_txt)

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/")
    assert resp.status == 200
    assert resp.headers.get("Content-Encoding") is None
    assert resp.headers["Content-Type"] == expect_type
    assert await resp.read() == hello_txt.read_bytes()
    resp.close()

    await resp.release()
    await client.close()


async def test_static_file_if_modified_since(
    aiohttp_client: Any,
    app_with_static_route: web.Application,
) -> None:
    client = await aiohttp_client(app_with_static_route)

    resp = await client.get("/")
    assert 200 == resp.status
    lastmod = resp.headers.get("Last-Modified")
    assert lastmod is not None
    resp.close()
    await resp.release()

    resp = await client.get("/", headers={"If-Modified-Since": lastmod})
    body = await resp.read()
    assert 304 == resp.status
    assert resp.headers.get("Content-Length") is None
    assert resp.headers.get("Last-Modified") == lastmod
    assert b"" == body
    resp.close()
    await resp.release()
    await client.close()


async def test_static_file_if_modified_since_past_date(
    aiohttp_client: Any,
    app_with_static_route: web.Application,
) -> None:
    client = await aiohttp_client(app_with_static_route)

    lastmod = "Mon, 1 Jan 1990 01:01:01 GMT"

    resp = await client.get("/", headers={"If-Modified-Since": lastmod})
    assert 200 == resp.status
    resp.close()

    await resp.release()
    await client.close()


async def test_static_file_if_modified_since_invalid_date(
    aiohttp_client: Any,
    app_with_static_route: web.Application,
) -> None:
    client = await aiohttp_client(app_with_static_route)

    lastmod = "not a valid HTTP-date"

    resp = await client.get("/", headers={"If-Modified-Since": lastmod})
    assert 200 == resp.status
    resp.close()

    await resp.release()
    await client.close()


async def test_static_file_if_modified_since_future_date(
    aiohttp_client: Any,
    app_with_static_route: web.Application,
) -> None:
    client = await aiohttp_client(app_with_static_route)

    lastmod = "Fri, 31 Dec 9999 23:59:59 GMT"

    resp = await client.get("/", headers={"If-Modified-Since": lastmod})
    body = await resp.read()
    assert 304 == resp.status
    assert resp.headers.get("Content-Length") is None
    assert resp.headers.get("Last-Modified")
    assert b"" == body
    resp.close()

    await resp.release()
    await client.close()


@pytest.mark.parametrize("if_unmodified_since", ("", "Fri, 31 Dec 0000 23:59:59 GMT"))
async def test_static_file_if_match(
    aiohttp_client: Any,
    app_with_static_route: web.Application,
    if_unmodified_since: str,
) -> None:
    client = await aiohttp_client(app_with_static_route)

    resp = await client.get("/")
    assert 200 == resp.status
    original_etag = resp.headers.get("ETag")

    assert original_etag is not None
    resp.close()
    await resp.release()

    headers = {"If-Match": original_etag, "If-Unmodified-Since": if_unmodified_since}
    resp = await client.head("/", headers=headers)
    body = await resp.read()
    assert 200 == resp.status
    assert resp.headers.get("ETag")
    assert resp.headers.get("Last-Modified")
    assert b"" == body
    resp.close()
    await resp.release()

    await client.close()


@pytest.mark.parametrize("if_unmodified_since", ("", "Fri, 31 Dec 0000 23:59:59 GMT"))
@pytest.mark.parametrize(
    "etags,expected_status",
    [
        (("*",), 200),
        (('"example-tag"', 'W/"weak-tag"'), 412),
    ],
)
async def test_static_file_if_match_custom_tags(
    aiohttp_client: Any,
    app_with_static_route: web.Application,
    if_unmodified_since: str,
    etags: Iterable[str],
    expected_status: Iterable[int],
) -> None:
    client = await aiohttp_client(app_with_static_route)

    if_match = ", ".join(etags)
    headers = {"If-Match": if_match, "If-Unmodified-Since": if_unmodified_since}
    resp = await client.head("/", headers=headers)
    body = await resp.read()
    assert expected_status == resp.status
    assert b"" == body
    resp.close()

    await resp.release()
    await client.close()


@pytest.mark.parametrize("if_modified_since", ("", "Fri, 31 Dec 9999 23:59:59 GMT"))
@pytest.mark.parametrize(
    "additional_etags",
    (
        (),
        ('"some-other-strong-etag"', 'W/"weak-tag"', "invalid-tag"),
    ),
)
async def test_static_file_if_none_match(
    aiohttp_client: Any,
    app_with_static_route: web.Application,
    if_modified_since: str,
    additional_etags: Iterable[str],
) -> None:
    client = await aiohttp_client(app_with_static_route)

    resp = await client.get("/")
    assert 200 == resp.status
    original_etag = resp.headers["ETag"]

    assert resp.headers.get("Last-Modified") is not None
    resp.close()
    await resp.release()

    etag = ",".join((original_etag, *additional_etags))

    resp = await client.get(
        "/", headers={"If-None-Match": etag, "If-Modified-Since": if_modified_since}
    )
    body = await resp.read()
    assert 304 == resp.status
    assert resp.headers.get("Content-Length") is None
    assert resp.headers.get("ETag") == original_etag
    assert b"" == body
    resp.close()
    await resp.release()

    await client.close()


async def test_static_file_if_none_match_star(
    aiohttp_client: Any,
    app_with_static_route: web.Application,
) -> None:
    client = await aiohttp_client(app_with_static_route)

    resp = await client.head("/", headers={"If-None-Match": "*"})
    body = await resp.read()
    assert 304 == resp.status
    assert resp.headers.get("Content-Length") is None
    assert resp.headers.get("ETag")
    assert resp.headers.get("Last-Modified")
    assert b"" == body
    resp.close()

    await resp.release()
    await client.close()


@pytest.mark.parametrize("if_modified_since", ("", "Fri, 31 Dec 9999 23:59:59 GMT"))
async def test_static_file_if_none_match_weak(
    aiohttp_client: Any,
    app_with_static_route: web.Application,
    if_modified_since: str,
) -> None:
    client = await aiohttp_client(app_with_static_route)

    resp = await client.get("/")
    assert 200 == resp.status
    original_etag = resp.headers["ETag"]

    assert resp.headers.get("Last-Modified") is not None
    resp.close()
    resp.release()

    weak_etag = f"W/{original_etag}"

    resp = await client.get(
        "/",
        headers={"If-None-Match": weak_etag, "If-Modified-Since": if_modified_since},
    )
    body = await resp.read()
    assert 304 == resp.status
    assert resp.headers.get("Content-Length") is None
    assert resp.headers.get("ETag") == original_etag
    assert b"" == body
    resp.close()
    resp.release()

    await client.close()


@pytest.mark.skipif(not ssl, reason="ssl not supported")
async def test_static_file_ssl(
    aiohttp_server,
    ssl_ctx,
    aiohttp_client,
    client_ssl_ctx,
) -> None:
    dirname = pathlib.Path(__file__).parent
    filename = "data.unknown_mime_type"
    app = web.Application()
    app.router.add_static("/static", dirname)
    server = await aiohttp_server(app, ssl=ssl_ctx)
    conn = aiohttp.TCPConnector(ssl=client_ssl_ctx)
    client = await aiohttp_client(server, connector=conn)

    resp = await client.get("/static/" + filename)
    assert 200 == resp.status
    txt = await resp.text()
    assert "file content" == txt.rstrip()
    ct = resp.headers["CONTENT-TYPE"]
    assert "application/octet-stream" == ct
    assert resp.headers.get("CONTENT-ENCODING") is None

    await resp.release()
    await client.close()
    await conn.close()


async def test_static_file_directory_traversal_attack(aiohttp_client) -> None:
    dirname = pathlib.Path(__file__).parent
    relpath = "../README.rst"
    full_path = dirname / relpath
    assert full_path.is_file()

    app = web.Application()
    app.router.add_static("/static", dirname)
    client = await aiohttp_client(app)

    resp = await client.get("/static/" + relpath)
    assert 404 == resp.status
    await resp.release()

    url_relpath2 = "/static/dir/../" + relpath
    resp = await client.get(url_relpath2)
    assert 404 == resp.status
    await resp.release()

    url_abspath = "/static/" + str(full_path.resolve())
    resp = await client.get(url_abspath)
    assert 403 == resp.status
    await resp.release()

    await client.close()


@pytest.mark.skip_blockbuster
async def test_static_file_huge(
    aiohttp_client: AiohttpClient, tmp_path: pathlib.Path
) -> None:
    file_path = tmp_path / "huge_data.unknown_mime_type"

    # fill 20MB file
    with file_path.open("wb") as f:
        for i in range(1024 * 20):
            f.write((chr(i % 64 + 0x20) * 1024).encode())

    file_st = file_path.stat()

    app = web.Application()
    app.router.add_static("/static", str(tmp_path))
    client = await aiohttp_client(app)

    resp = await client.get("/static/" + file_path.name)
    assert 200 == resp.status
    ct = resp.headers["CONTENT-TYPE"]
    assert "application/octet-stream" == ct
    assert resp.headers.get("CONTENT-ENCODING") is None
    assert int(resp.headers.get("CONTENT-LENGTH")) == file_st.st_size

    f = file_path.open("rb")
    off = 0
    cnt = 0
    while off < file_st.st_size:
        chunk = await resp.content.readany()
        expected = f.read(len(chunk))
        assert chunk == expected
        off += len(chunk)
        cnt += 1
    f.close()

    await resp.release()
    await client.close()


async def test_static_file_range(aiohttp_client: Any, sender: Any) -> None:
    filepath = pathlib.Path(__file__).parent / "sample.txt"

    filesize = filepath.stat().st_size

    async def handler(request):
        return sender(filepath, chunk_size=16)

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    with filepath.open("rb") as f:
        content = f.read()

    # Ensure the whole file requested in parts is correct
    responses = await asyncio.gather(
        client.get("/", headers={"Range": "bytes=0-999"}),
        client.get("/", headers={"Range": "bytes=1000-1999"}),
        client.get("/", headers={"Range": "bytes=2000-"}),
    )
    assert len(responses) == 3
    assert responses[0].status == 206, "failed 'bytes=0-999': %s" % responses[0].reason
    assert responses[0].headers["Content-Range"] == "bytes 0-999/{}".format(
        filesize
    ), "failed: Content-Range Error"
    assert responses[1].status == 206, (
        "failed 'bytes=1000-1999': %s" % responses[1].reason
    )
    assert responses[1].headers["Content-Range"] == "bytes 1000-1999/{}".format(
        filesize
    ), "failed: Content-Range Error"
    assert responses[2].status == 206, "failed 'bytes=2000-': %s" % responses[2].reason
    assert responses[2].headers["Content-Range"] == "bytes 2000-{}/{}".format(
        filesize - 1, filesize
    ), "failed: Content-Range Error"

    body = await asyncio.gather(
        *(resp.read() for resp in responses),
    )

    assert len(body[0]) == 1000, "failed 'bytes=0-999', received %d bytes" % len(
        body[0]
    )
    assert len(body[1]) == 1000, "failed 'bytes=1000-1999', received %d bytes" % len(
        body[1]
    )
    responses[0].close()
    responses[1].close()
    responses[2].close()

    await asyncio.gather(
        *(resp.release() for resp in responses),
    )

    assert content == b"".join(body)

    await client.close()


async def test_static_file_range_end_bigger_than_size(aiohttp_client, sender):
    filepath = pathlib.Path(__file__).parent / "aiohttp.png"

    async def handler(request):
        return sender(filepath, chunk_size=16)

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    with filepath.open("rb") as f:
        content = f.read()

        # Ensure the whole file requested in parts is correct
        response = await client.get("/", headers={"Range": "bytes=54000-55000"})

        assert response.status == 206, (
            "failed 'bytes=54000-55000': %s" % response.reason
        )
        assert (
            response.headers["Content-Range"] == "bytes 54000-54996/54997"
        ), "failed: Content-Range Error"

        body = await response.read()
        assert len(body) == 997, "failed 'bytes=54000-55000', received %d bytes" % len(
            body
        )

        assert content[54000:] == body

    await response.release()
    await client.close()


async def test_static_file_range_beyond_eof(aiohttp_client, sender) -> None:
    filepath = pathlib.Path(__file__).parent / "aiohttp.png"

    async def handler(request):
        return sender(filepath, chunk_size=16)

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    # Ensure the whole file requested in parts is correct
    response = await client.get("/", headers={"Range": "bytes=1000000-1200000"})

    assert response.status == 416, (
        "failed 'bytes=1000000-1200000': %s" % response.reason
    )

    await response.release()
    await client.close()


async def test_static_file_range_tail(aiohttp_client, sender) -> None:
    filepath = pathlib.Path(__file__).parent / "aiohttp.png"

    async def handler(request):
        return sender(filepath, chunk_size=16)

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    with filepath.open("rb") as f:
        content = f.read()

    # Ensure the tail of the file is correct
    resp = await client.get("/", headers={"Range": "bytes=-500"})
    assert resp.status == 206, resp.reason
    assert (
        resp.headers["Content-Range"] == "bytes 54497-54996/54997"
    ), "failed: Content-Range Error"
    body4 = await resp.read()
    resp.close()
    await resp.release()
    assert content[-500:] == body4

    # Ensure out-of-range tails could be handled
    resp2 = await client.get("/", headers={"Range": "bytes=-99999999999999"})
    assert resp2.status == 206, resp.reason
    assert (
        resp2.headers["Content-Range"] == "bytes 0-54996/54997"
    ), "failed: Content-Range Error"
    await resp2.release()

    await client.close()


async def test_static_file_invalid_range(aiohttp_client, sender) -> None:
    filepath = pathlib.Path(__file__).parent / "aiohttp.png"

    async def handler(request):
        return sender(filepath, chunk_size=16)

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    # range must be in bytes
    resp = await client.get("/", headers={"Range": "blocks=0-10"})
    assert resp.status == 416, "Range must be in bytes"
    resp.close()
    await resp.release()

    # start > end
    resp = await client.get("/", headers={"Range": "bytes=100-0"})
    assert resp.status == 416, "Range start can't be greater than end"
    resp.close()
    await resp.release()

    # start > end
    resp = await client.get("/", headers={"Range": "bytes=10-9"})
    assert resp.status == 416, "Range start can't be greater than end"
    resp.close()
    await resp.release()

    # non-number range
    resp = await client.get("/", headers={"Range": "bytes=a-f"})
    assert resp.status == 416, "Range must be integers"
    resp.close()
    await resp.release()

    # double dash range
    resp = await client.get("/", headers={"Range": "bytes=0--10"})
    assert resp.status == 416, "double dash in range"
    resp.close()
    await resp.release()

    # no range
    resp = await client.get("/", headers={"Range": "bytes=-"})
    assert resp.status == 416, "no range given"
    resp.close()
    await resp.release()

    await client.close()


async def test_static_file_if_unmodified_since_past_with_range(
    aiohttp_client: Any,
    app_with_static_route: web.Application,
) -> None:
    client = await aiohttp_client(app_with_static_route)

    lastmod = "Mon, 1 Jan 1990 01:01:01 GMT"

    resp = await client.get(
        "/", headers={"If-Unmodified-Since": lastmod, "Range": "bytes=2-"}
    )
    assert 412 == resp.status
    resp.close()
    await resp.release()

    await client.close()


async def test_static_file_if_unmodified_since_future_with_range(
    aiohttp_client: Any,
    app_with_static_route: web.Application,
) -> None:
    client = await aiohttp_client(app_with_static_route)

    lastmod = "Fri, 31 Dec 9999 23:59:59 GMT"

    resp = await client.get(
        "/", headers={"If-Unmodified-Since": lastmod, "Range": "bytes=2-"}
    )
    assert 206 == resp.status
    assert resp.headers["Content-Range"] == "bytes 2-12/13"
    assert resp.headers["Content-Length"] == "11"
    resp.close()
    await resp.release()

    await client.close()


async def test_static_file_if_range_past_with_range(
    aiohttp_client: Any,
    app_with_static_route: web.Application,
) -> None:
    client = await aiohttp_client(app_with_static_route)

    lastmod = "Mon, 1 Jan 1990 01:01:01 GMT"

    resp = await client.get("/", headers={"If-Range": lastmod, "Range": "bytes=2-"})
    assert 200 == resp.status
    assert resp.headers["Content-Length"] == "13"
    resp.close()
    await resp.release()
    await client.close()


async def test_static_file_if_range_future_with_range(
    aiohttp_client: Any,
    app_with_static_route: web.Application,
) -> None:
    client = await aiohttp_client(app_with_static_route)

    lastmod = "Fri, 31 Dec 9999 23:59:59 GMT"

    resp = await client.get("/", headers={"If-Range": lastmod, "Range": "bytes=2-"})
    assert 206 == resp.status
    assert resp.headers["Content-Range"] == "bytes 2-12/13"
    assert resp.headers["Content-Length"] == "11"
    resp.close()

    await resp.release()
    await client.close()


async def test_static_file_if_unmodified_since_past_without_range(
    aiohttp_client: Any,
    app_with_static_route: web.Application,
) -> None:
    client = await aiohttp_client(app_with_static_route)

    lastmod = "Mon, 1 Jan 1990 01:01:01 GMT"

    resp = await client.get("/", headers={"If-Unmodified-Since": lastmod})
    assert 412 == resp.status
    resp.close()

    await resp.release()
    await client.close()


async def test_static_file_if_unmodified_since_future_without_range(
    aiohttp_client: Any,
    app_with_static_route: web.Application,
) -> None:
    client = await aiohttp_client(app_with_static_route)

    lastmod = "Fri, 31 Dec 9999 23:59:59 GMT"

    resp = await client.get("/", headers={"If-Unmodified-Since": lastmod})
    assert 200 == resp.status
    assert resp.headers["Content-Length"] == "13"
    resp.close()

    await resp.release()
    await client.close()


async def test_static_file_if_range_past_without_range(
    aiohttp_client: Any,
    app_with_static_route: web.Application,
) -> None:
    client = await aiohttp_client(app_with_static_route)

    lastmod = "Mon, 1 Jan 1990 01:01:01 GMT"

    resp = await client.get("/", headers={"If-Range": lastmod})
    assert 200 == resp.status
    assert resp.headers["Content-Length"] == "13"
    resp.close()

    await resp.release()
    await client.close()


async def test_static_file_if_range_future_without_range(
    aiohttp_client: Any,
    app_with_static_route: web.Application,
) -> None:
    client = await aiohttp_client(app_with_static_route)

    lastmod = "Fri, 31 Dec 9999 23:59:59 GMT"

    resp = await client.get("/", headers={"If-Range": lastmod})
    assert 200 == resp.status
    assert resp.headers["Content-Length"] == "13"
    resp.close()

    await resp.release()
    await client.close()


async def test_static_file_if_unmodified_since_invalid_date(
    aiohttp_client: Any,
    app_with_static_route: web.Application,
) -> None:
    client = await aiohttp_client(app_with_static_route)

    lastmod = "not a valid HTTP-date"

    resp = await client.get("/", headers={"If-Unmodified-Since": lastmod})
    assert 200 == resp.status
    resp.close()

    await resp.release()
    await client.close()


async def test_static_file_if_range_invalid_date(
    aiohttp_client: Any,
    app_with_static_route: web.Application,
) -> None:
    client = await aiohttp_client(app_with_static_route)

    lastmod = "not a valid HTTP-date"

    resp = await client.get("/", headers={"If-Range": lastmod})
    assert 200 == resp.status
    resp.close()
    await resp.release()

    await client.close()


@pytest.mark.usefixtures("parametrize_zlib_backend")
async def test_static_file_compression(aiohttp_client, sender) -> None:
    filepath = pathlib.Path(__file__).parent / "data.unknown_mime_type"

    async def handler(request):
        ret = sender(filepath)
        ret.enable_compression()
        return ret

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app, auto_decompress=False)

    resp = await client.get("/")
    assert resp.status == 200
    zcomp = ZLibBackend.compressobj(wbits=ZLibBackend.MAX_WBITS)
    expected_body = zcomp.compress(b"file content\n") + zcomp.flush()
    assert expected_body == await resp.read()
    assert "application/octet-stream" == resp.headers["Content-Type"]
    assert resp.headers.get("Content-Encoding") == "deflate"
    await resp.release()

    await client.close()


@pytest.mark.skip_blockbuster
async def test_static_file_huge_cancel(
    aiohttp_client: AiohttpClient, tmp_path: pathlib.Path
) -> None:
    file_path = tmp_path / "huge_data.unknown_mime_type"

    # fill 100MB file
    with file_path.open("wb") as f:
        for i in range(1024 * 20):
            f.write((chr(i % 64 + 0x20) * 1024).encode())

    task = None

    async def handler(request):
        nonlocal task
        task = request.task
        # reduce send buffer size
        tr = request.transport
        sock = tr.get_extra_info("socket")
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1024)
        ret = web.FileResponse(file_path)
        return ret

    app = web.Application()

    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/")
    assert resp.status == 200
    task.cancel()
    await asyncio.sleep(0)
    data = b""
    while True:
        try:
            data += await resp.content.read(1024)
        except aiohttp.ClientPayloadError:
            break
    assert len(data) < 1024 * 1024 * 20

    await resp.release()
    await client.close()


async def test_static_file_huge_error(aiohttp_client, tmp_path) -> None:
    file_path = tmp_path / "huge_data.unknown_mime_type"

    # fill 20MB file
    with file_path.open("wb") as f:
        f.seek(20 * 1024 * 1024)
        f.write(b"1")

    async def handler(request):
        # reduce send buffer size
        tr = request.transport
        sock = tr.get_extra_info("socket")
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1024)
        ret = web.FileResponse(file_path)
        return ret

    app = web.Application()

    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/")
    assert resp.status == 200
    # raise an exception on server side
    resp.close()

    await resp.release()
    await client.close()
