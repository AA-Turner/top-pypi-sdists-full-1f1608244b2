import asyncio
import io
import json
import pathlib
import socket
import sys
from typing import Any, Dict, Generator, NoReturn, Optional, Tuple
from unittest import mock

import pytest
from multidict import CIMultiDictProxy, MultiDict
from yarl import URL

import aiohttp
from aiohttp import (
    FormData,
    HttpVersion,
    HttpVersion10,
    HttpVersion11,
    TraceConfig,
    multipart,
    web,
)
from aiohttp.compression_utils import ZLibBackend, ZLibCompressObjProtocol
from aiohttp.hdrs import CONTENT_LENGTH, CONTENT_TYPE, TRANSFER_ENCODING
from aiohttp.pytest_plugin import AiohttpClient, AiohttpServer
from aiohttp.typedefs import Handler
from aiohttp.web_protocol import RequestHandler

try:
    import brotlicffi as brotli
except ImportError:
    import brotli

try:
    import ssl
except ImportError:
    ssl = None  # type: ignore


@pytest.fixture
def here():
    return pathlib.Path(__file__).parent


@pytest.fixture
def fname(here):
    return here / "conftest.py"


def new_dummy_form():
    form = FormData()
    with pytest.warns(DeprecationWarning, match="BytesPayload"):
        form.add_field("name", b"123", content_transfer_encoding="base64")
    return form


async def test_simple_get(aiohttp_client) -> None:
    async def handler(request):
        body = await request.read()
        assert b"" == body
        return web.Response(body=b"OK")

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/")
    assert 200 == resp.status
    txt = await resp.text()
    assert "OK" == txt

    await resp.release()


async def test_simple_get_with_text(aiohttp_client) -> None:
    async def handler(request):
        body = await request.read()
        assert b"" == body
        return web.Response(text="OK", headers={"content-type": "text/plain"})

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/")
    assert 200 == resp.status
    txt = await resp.text()
    assert "OK" == txt

    await resp.release()


async def test_handler_returns_not_response(aiohttp_server, aiohttp_client) -> None:
    asyncio.get_event_loop().set_debug(True)
    logger = mock.Mock()

    async def handler(request):
        return "abc"

    app = web.Application()
    app.router.add_get("/", handler)
    server = await aiohttp_server(app, logger=logger)
    client = await aiohttp_client(server)

    async with client.get("/") as resp:
        assert resp.status == 500


async def test_handler_returns_none(aiohttp_server, aiohttp_client) -> None:
    asyncio.get_event_loop().set_debug(True)
    logger = mock.Mock()

    async def handler(request):
        return None

    app = web.Application()
    app.router.add_get("/", handler)
    server = await aiohttp_server(app, logger=logger)
    client = await aiohttp_client(server)

    async with client.get("/") as resp:
        assert resp.status == 500


async def test_handler_returns_not_response_after_100expect(
    aiohttp_server, aiohttp_client
) -> None:
    async def handler(request: web.Request) -> NoReturn:
        raise Exception("foo")

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    async with client.get("/", expect100=True) as resp:
        assert resp.status == 500


async def test_head_returns_empty_body(aiohttp_client) -> None:
    async def handler(request):
        return web.Response(body=b"test")

    app = web.Application()
    app.router.add_head("/", handler)
    client = await aiohttp_client(app, version=HttpVersion11)

    resp = await client.head("/")
    assert 200 == resp.status
    txt = await resp.text()
    assert "" == txt
    # The Content-Length header should be set to 4 which is
    # the length of the response body if it would have been
    # returned by a GET request.
    assert resp.headers["Content-Length"] == "4"


@pytest.mark.parametrize("status", (201, 204, 404))
async def test_default_content_type_no_body(aiohttp_client: Any, status: int) -> None:
    async def handler(request):
        return web.Response(status=status)

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    async with client.get("/") as resp:
        assert resp.status == status
        assert await resp.read() == b""
        assert "Content-Type" not in resp.headers


async def test_response_before_complete(aiohttp_client: Any) -> None:
    async def handler(request):
        return web.Response(body=b"OK")

    app = web.Application()
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    data = b"0" * 1024 * 1024

    resp = await client.post("/", data=data)
    assert 200 == resp.status
    text = await resp.text()
    assert "OK" == text

    await resp.release()


@pytest.mark.skipif(sys.version_info < (3, 11), reason="Needs Task.cancelling()")
async def test_cancel_shutdown(aiohttp_client: AiohttpClient) -> None:
    async def handler(request: web.Request) -> web.Response:
        t = asyncio.create_task(request.protocol.shutdown())
        # Ensure it's started waiting
        await asyncio.sleep(0)

        t.cancel()
        # Cancellation should not be suppressed
        with pytest.raises(asyncio.CancelledError):
            await t

        # Repeat for second waiter in shutdown()
        with mock.patch.object(request.protocol, "_request_in_progress", False):
            with mock.patch.object(request.protocol, "_current_request", None):
                t = asyncio.create_task(request.protocol.shutdown())
                await asyncio.sleep(0)

                t.cancel()
                with pytest.raises(asyncio.CancelledError):
                    await t

        return web.Response(body=b"OK")

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    async with client.get("/") as resp:
        assert resp.status == 200
        txt = await resp.text()
        assert txt == "OK"


async def test_post_form(aiohttp_client: AiohttpClient) -> None:
    async def handler(request: web.Request) -> web.Response:
        data = await request.post()
        assert {"a": "1", "b": "2", "c": ""} == data
        return web.Response(body=b"OK")

    app = web.Application()
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    resp = await client.post("/", data={"a": 1, "b": 2, "c": ""})
    assert 200 == resp.status
    txt = await resp.text()
    assert "OK" == txt

    await resp.release()


async def test_post_text(aiohttp_client) -> None:
    async def handler(request):
        data = await request.text()
        assert "русский" == data
        data2 = await request.text()
        assert data == data2
        return web.Response(text=data)

    app = web.Application()
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    resp = await client.post("/", data="русский")
    assert 200 == resp.status
    txt = await resp.text()
    assert "русский" == txt

    await resp.release()


async def test_post_json(aiohttp_client) -> None:

    dct = {"key": "текст"}

    async def handler(request):
        data = await request.json()
        assert dct == data
        data2 = await request.json(loads=json.loads)
        assert data == data2
        resp = web.Response()
        resp.content_type = "application/json"
        resp.body = json.dumps(data).encode("utf8")
        return resp

    app = web.Application()
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    headers = {"Content-Type": "application/json"}
    resp = await client.post("/", data=json.dumps(dct), headers=headers)
    assert 200 == resp.status
    data = await resp.json()
    assert dct == data

    await resp.release()


async def test_multipart(aiohttp_client) -> None:
    with multipart.MultipartWriter() as writer:
        writer.append("test")
        writer.append_json({"passed": True})

    async def handler(request):
        reader = await request.multipart()
        assert isinstance(reader, multipart.MultipartReader)

        part = await reader.next()
        assert isinstance(part, multipart.BodyPartReader)
        thing = await part.text()
        assert thing == "test"

        part = await reader.next()
        assert isinstance(part, multipart.BodyPartReader)
        assert part.headers["Content-Type"] == "application/json"
        thing = await part.json()
        assert thing == {"passed": True}

        resp = web.Response()
        resp.content_type = "application/json"
        resp.body = b""
        return resp

    app = web.Application()
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    resp = await client.post("/", data=writer)
    assert 200 == resp.status
    await resp.release()


async def test_multipart_empty(aiohttp_client) -> None:
    with multipart.MultipartWriter() as writer:
        pass

    async def handler(request):
        reader = await request.multipart()
        assert isinstance(reader, multipart.MultipartReader)
        async for part in reader:
            assert False, f"Unexpected part found in reader: {part!r}"
        return web.Response()

    app = web.Application()
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    resp = await client.post("/", data=writer)
    assert 200 == resp.status
    await resp.release()


async def test_multipart_content_transfer_encoding(aiohttp_client) -> None:
    # For issue #1168
    with multipart.MultipartWriter() as writer:
        writer.append(b"\x00" * 10, headers={"Content-Transfer-Encoding": "binary"})

    async def handler(request):
        reader = await request.multipart()
        assert isinstance(reader, multipart.MultipartReader)

        part = await reader.next()
        assert isinstance(part, multipart.BodyPartReader)
        assert part.headers["Content-Transfer-Encoding"] == "binary"
        thing = await part.read()
        assert thing == b"\x00" * 10

        resp = web.Response()
        resp.content_type = "application/json"
        resp.body = b""
        return resp

    app = web.Application()
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    resp = await client.post("/", data=writer)
    assert 200 == resp.status
    await resp.release()


async def test_render_redirect(aiohttp_client) -> None:
    async def handler(request):
        raise web.HTTPMovedPermanently(location="/path")

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/", allow_redirects=False)
    assert 301 == resp.status
    txt = await resp.text()
    assert "301: Moved Permanently" == txt
    assert "/path" == resp.headers["location"]

    await resp.release()


async def test_post_single_file(aiohttp_client) -> None:

    here = pathlib.Path(__file__).parent

    def check_file(fs):
        fullname = here / fs.filename
        with fullname.open("rb") as f:
            test_data = f.read()
            data = fs.file.read()
            assert test_data == data

    async def handler(request):
        data = await request.post()
        assert ["data.unknown_mime_type"] == list(data.keys())
        for fs in data.values():
            await asyncio.to_thread(check_file, fs)
            fs.file.close()
        resp = web.Response(body=b"OK")
        return resp

    app = web.Application()
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    fname = here / "data.unknown_mime_type"

    with fname.open("rb") as fd:
        resp = await client.post("/", data=[fd])
    assert 200 == resp.status

    await resp.release()


async def test_files_upload_with_same_key(aiohttp_client) -> None:
    async def handler(request):
        data = await request.post()
        files = data.getall("file")
        file_names = set()
        for _file in files:
            assert not _file.file.closed
            if _file.filename == "test1.jpeg":
                assert await asyncio.to_thread(_file.file.read) == b"binary data 1"
            if _file.filename == "test2.jpeg":
                assert await asyncio.to_thread(_file.file.read) == b"binary data 2"
            file_names.add(_file.filename)
            _file.file.close()
        assert len(files) == 2
        assert file_names == {"test1.jpeg", "test2.jpeg"}
        resp = web.Response(body=b"OK")
        return resp

    app = web.Application()
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    data = FormData()
    data.add_field(
        "file", b"binary data 1", content_type="image/jpeg", filename="test1.jpeg"
    )
    data.add_field(
        "file", b"binary data 2", content_type="image/jpeg", filename="test2.jpeg"
    )
    resp = await client.post("/", data=data)
    assert 200 == resp.status

    await resp.release()


async def test_post_files(aiohttp_client) -> None:

    here = pathlib.Path(__file__).parent

    def check_file(fs):
        fullname = here / fs.filename
        with fullname.open("rb") as f:
            test_data = f.read()
            data = fs.file.read()
            assert test_data == data

    async def handler(request):
        data = await request.post()
        assert ["data.unknown_mime_type", "conftest.py"] == list(data.keys())
        for fs in data.values():
            await asyncio.to_thread(check_file, fs)
            fs.file.close()
        resp = web.Response(body=b"OK")
        return resp

    app = web.Application()
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    with (here / "data.unknown_mime_type").open("rb") as f1:
        with (here / "conftest.py").open("rb") as f2:
            resp = await client.post("/", data=[f1, f2])
            assert 200 == resp.status

            await resp.release()


async def test_release_post_data(aiohttp_client) -> None:
    async def handler(request):
        await request.release()
        chunk = await request.content.readany()
        assert chunk == b""
        return web.Response()

    app = web.Application()
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    resp = await client.post("/", data="post text")
    assert 200 == resp.status

    await resp.release()


async def test_post_form_with_duplicate_keys(aiohttp_client) -> None:
    async def handler(request):
        data = await request.post()
        lst = list(data.items())
        assert [("a", "1"), ("a", "2")] == lst
        return web.Response()

    app = web.Application()
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    resp = await client.post("/", data=MultiDict([("a", 1), ("a", 2)]))
    assert 200 == resp.status

    await resp.release()


def test_repr_for_application() -> None:
    app = web.Application()
    assert f"<Application 0x{id(app):x}>" == repr(app)


async def test_expect_default_handler_unknown(aiohttp_client) -> None:
    # Test default Expect handler for unknown Expect value.

    # A server that does not understand or is unable to comply with any of
    # the expectation values in the Expect field of a request MUST respond
    # with appropriate error status. The server MUST respond with a 417
    # (Expectation Failed) status if any of the expectations cannot be met
    # or, if there are other problems with the request, some other 4xx
    # status.

    # http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.20
    async def handler(request):
        await request.post()
        pytest.xfail(
            "Handler should not proceed to this point in case of "
            "unknown Expect header"
        )

    app = web.Application()
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    resp = await client.post("/", headers={"Expect": "SPAM"})
    assert 417 == resp.status

    await resp.release()


async def test_100_continue(aiohttp_client) -> None:
    async def handler(request):
        data = await request.post()
        assert b"123" == data["name"]
        return web.Response()

    form = FormData()
    with pytest.warns(DeprecationWarning, match="BytesPayload"):
        form.add_field("name", b"123", content_transfer_encoding="base64")

    app = web.Application()
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    resp = await client.post("/", data=form, expect100=True)
    assert 200 == resp.status

    await resp.release()


async def test_100_continue_custom(aiohttp_client) -> None:

    expect_received = False

    async def handler(request):
        data = await request.post()
        assert b"123" == data["name"]
        return web.Response()

    async def expect_handler(request):
        nonlocal expect_received
        expect_received = True
        if request.version == HttpVersion11:
            await request.writer.write(b"HTTP/1.1 100 Continue\r\n\r\n")

    app = web.Application()
    app.router.add_post("/", handler, expect_handler=expect_handler)
    client = await aiohttp_client(app)

    resp = await client.post("/", data=new_dummy_form(), expect100=True)
    assert 200 == resp.status
    assert expect_received

    await resp.release()


async def test_100_continue_custom_response(aiohttp_client) -> None:
    async def handler(request):
        data = await request.post()
        assert b"123", data["name"]
        return web.Response()

    async def expect_handler(request):
        if request.version == HttpVersion11:
            if auth_err:
                raise web.HTTPForbidden()

            await request.writer.write(b"HTTP/1.1 100 Continue\r\n\r\n")

    app = web.Application()
    app.router.add_post("/", handler, expect_handler=expect_handler)
    client = await aiohttp_client(app)

    auth_err = False
    resp = await client.post("/", data=new_dummy_form(), expect100=True)
    assert 200 == resp.status
    await resp.release()

    auth_err = True
    resp = await client.post("/", data=new_dummy_form(), expect100=True)
    assert 403 == resp.status
    await resp.release()


async def test_expect_handler_custom_response(aiohttp_client) -> None:
    cache = {"foo": "bar"}

    async def handler(request: web.Request) -> web.Response:
        return web.Response(text="handler")

    async def expect_handler(request: web.Request) -> Optional[web.Response]:
        k = request.headers.get("X-Key")
        cached_value = cache.get(k)
        if cached_value:
            return web.Response(text=cached_value)

    app = web.Application()
    # expect_handler is only typed on add_route().
    app.router.add_route("POST", "/", handler, expect_handler=expect_handler)
    client = await aiohttp_client(app)

    async with client.post("/", expect100=True, headers={"X-Key": "foo"}) as resp:
        assert resp.status == 200
        assert await resp.text() == "bar"

    async with client.post("/", expect100=True, headers={"X-Key": "spam"}) as resp:
        assert resp.status == 200
        assert await resp.text() == "handler"


async def test_100_continue_for_not_found(aiohttp_client) -> None:

    app = web.Application()
    client = await aiohttp_client(app)

    resp = await client.post("/not_found", data="data", expect100=True)
    assert 404 == resp.status

    await resp.release()


async def test_100_continue_for_not_allowed(aiohttp_client) -> None:
    async def handler(request):
        return web.Response()

    app = web.Application()
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/", expect100=True)
    assert 405 == resp.status

    await resp.release()


async def test_http11_keep_alive_default(aiohttp_client) -> None:
    async def handler(request):
        return web.Response()

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app, version=HttpVersion11)

    resp = await client.get("/")
    assert 200 == resp.status
    assert resp.version == HttpVersion11
    assert "Connection" not in resp.headers

    await resp.release()


async def test_http10_keep_alive_default(aiohttp_client: AiohttpClient) -> None:
    async def handler(request: web.Request) -> web.Response:
        return web.Response()

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app, version=HttpVersion10)

    resp = await client.get("/")
    assert 200 == resp.status
    assert resp.version == HttpVersion10
    assert resp.headers["Connection"] == "keep-alive"

    await resp.release()


async def test_http10_keep_alive_with_headers_close(aiohttp_client) -> None:
    async def handler(request):
        await request.read()
        return web.Response(body=b"OK")

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app, version=HttpVersion10)

    headers = {"Connection": "close"}
    resp = await client.get("/", headers=headers)
    assert 200 == resp.status
    assert resp.version == HttpVersion10
    assert "Connection" not in resp.headers

    await resp.release()


async def test_http10_keep_alive_with_headers(aiohttp_client) -> None:
    async def handler(request):
        await request.read()
        return web.Response(body=b"OK")

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app, version=HttpVersion10)

    headers = {"Connection": "keep-alive"}
    resp = await client.get("/", headers=headers)
    assert 200 == resp.status
    assert resp.version == HttpVersion10
    assert resp.headers["Connection"] == "keep-alive"

    await resp.release()


async def test_upload_file(aiohttp_client) -> None:

    here = pathlib.Path(__file__).parent
    fname = here / "aiohttp.png"
    with fname.open("rb") as f:
        data = f.read()

    async def handler(request):
        form = await request.post()
        raw_data = await asyncio.to_thread(form["file"].file.read)
        form["file"].file.close()
        assert data == raw_data
        return web.Response()

    app = web.Application()
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    resp = await client.post("/", data={"file": io.BytesIO(data)})
    assert 200 == resp.status

    await resp.release()


async def test_upload_file_object(aiohttp_client) -> None:
    here = pathlib.Path(__file__).parent
    fname = here / "aiohttp.png"
    with fname.open("rb") as f:
        data = f.read()

    async def handler(request):
        form = await request.post()
        raw_data = await asyncio.to_thread(form["file"].file.read)
        form["file"].file.close()
        assert data == raw_data
        return web.Response()

    app = web.Application()
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    with fname.open("rb") as f:
        resp = await client.post("/", data={"file": f})
        assert 200 == resp.status

        await resp.release()


@pytest.mark.parametrize(
    "method", ["get", "post", "options", "post", "put", "patch", "delete"]
)
async def test_empty_content_for_query_without_body(method, aiohttp_client) -> None:
    async def handler(request):
        assert not request.body_exists
        assert not request.can_read_body
        with pytest.warns(DeprecationWarning):
            assert not request.has_body
        return web.Response()

    app = web.Application()
    app.router.add_route(method, "/", handler)
    client = await aiohttp_client(app)

    resp = await client.request(method, "/")
    assert 200 == resp.status


async def test_empty_content_for_query_with_body(aiohttp_client) -> None:
    async def handler(request):
        assert request.body_exists
        assert request.can_read_body
        with pytest.warns(DeprecationWarning):
            assert request.has_body
        body = await request.read()
        return web.Response(body=body)

    app = web.Application()
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    resp = await client.post("/", data=b"data")
    assert 200 == resp.status

    await resp.release()


async def test_get_with_empty_arg(aiohttp_client) -> None:
    async def handler(request):
        assert "arg" in request.query
        assert "" == request.query["arg"]
        return web.Response()

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/?arg")
    assert 200 == resp.status

    await resp.release()


async def test_large_header(aiohttp_client) -> None:
    async def handler(request):
        return web.Response()

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    headers = {"Long-Header": "ab" * 8129}
    resp = await client.get("/", headers=headers)
    assert 400 == resp.status

    await resp.release()


async def test_large_header_allowed(aiohttp_client, aiohttp_server) -> None:
    async def handler(request):
        return web.Response()

    app = web.Application()
    app.router.add_post("/", handler)
    server = await aiohttp_server(app, max_field_size=81920)
    client = await aiohttp_client(server)

    headers = {"Long-Header": "ab" * 8129}
    resp = await client.post("/", headers=headers)
    assert 200 == resp.status

    await resp.release()


async def test_get_with_empty_arg_with_equal(aiohttp_client) -> None:
    async def handler(request):
        assert "arg" in request.query
        assert "" == request.query["arg"]
        return web.Response()

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/?arg=")
    assert 200 == resp.status

    await resp.release()


async def test_response_with_async_gen(aiohttp_client, fname) -> None:

    with fname.open("rb") as f:
        data = f.read()

    data_size = len(data)

    async def stream(f_name):
        with f_name.open("rb") as f:
            data = await asyncio.to_thread(f.read, 100)
            while data:
                yield data
                data = await asyncio.to_thread(f.read, 100)

    async def handler(request):
        headers = {"Content-Length": str(data_size)}
        return web.Response(body=stream(fname), headers=headers)

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/")
    assert 200 == resp.status
    resp_data = await resp.read()
    assert resp_data == data
    assert resp.headers.get("Content-Length") == str(len(resp_data))

    await resp.release()


async def test_response_with_streamer(aiohttp_client, fname) -> None:

    with fname.open("rb") as f:
        data = f.read()

    data_size = len(data)

    with pytest.warns(DeprecationWarning):

        @aiohttp.streamer
        async def stream(writer, f_name):
            with f_name.open("rb") as f:
                data = await asyncio.to_thread(f.read, 100)
                while data:
                    await writer.write(data)
                    data = await asyncio.to_thread(f.read, 100)

    async def handler(request):
        headers = {"Content-Length": str(data_size)}
        return web.Response(body=stream(fname), headers=headers)

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/")
    assert 200 == resp.status
    resp_data = await resp.read()
    assert resp_data == data
    assert resp.headers.get("Content-Length") == str(len(resp_data))


async def test_response_with_async_gen_no_params(aiohttp_client, fname) -> None:

    with fname.open("rb") as f:
        data = f.read()

    data_size = len(data)

    async def stream():
        with fname.open("rb") as f:
            data = await asyncio.to_thread(f.read, 100)
            while data:
                yield data
                data = await asyncio.to_thread(f.read, 100)

    async def handler(request):
        headers = {"Content-Length": str(data_size)}
        return web.Response(body=stream(), headers=headers)

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/")
    assert 200 == resp.status
    resp_data = await resp.read()
    assert resp_data == data
    assert resp.headers.get("Content-Length") == str(len(resp_data))

    await resp.release()


async def test_response_with_streamer_no_params(aiohttp_client, fname) -> None:

    with fname.open("rb") as f:
        data = f.read()

    data_size = len(data)

    with pytest.warns(DeprecationWarning):

        @aiohttp.streamer
        async def stream(writer):
            with fname.open("rb") as f:
                data = await asyncio.to_thread(f.read, 100)
                while data:
                    await writer.write(data)
                    data = await asyncio.to_thread(f.read, 100)

    async def handler(request):
        headers = {"Content-Length": str(data_size)}
        return web.Response(body=stream, headers=headers)

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/")
    assert 200 == resp.status
    resp_data = await resp.read()
    assert resp_data == data
    assert resp.headers.get("Content-Length") == str(len(resp_data))


async def test_response_with_file(aiohttp_client, fname) -> None:
    outer_file_descriptor = None

    with fname.open("rb") as f:
        data = f.read()

    async def handler(request):
        nonlocal outer_file_descriptor
        outer_file_descriptor = fname.open("rb")
        return web.Response(body=outer_file_descriptor)

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/")
    assert 200 == resp.status
    resp_data = await resp.read()
    expected_content_disposition = 'attachment; filename="conftest.py"'
    assert resp_data == data
    assert resp.headers.get("Content-Type") in (
        "application/octet-stream",
        "text/x-python",
        "text/plain",
    )
    assert resp.headers.get("Content-Length") == str(len(resp_data))
    assert resp.headers.get("Content-Disposition") == expected_content_disposition

    await resp.release()

    outer_file_descriptor.close()


async def test_response_with_file_ctype(aiohttp_client, fname) -> None:
    outer_file_descriptor = None

    with fname.open("rb") as f:
        data = f.read()

    async def handler(request):
        nonlocal outer_file_descriptor
        outer_file_descriptor = fname.open("rb")

        return web.Response(
            body=outer_file_descriptor, headers={"content-type": "text/binary"}
        )

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/")
    assert 200 == resp.status
    resp_data = await resp.read()
    expected_content_disposition = 'attachment; filename="conftest.py"'
    assert resp_data == data
    assert resp.headers.get("Content-Type") == "text/binary"
    assert resp.headers.get("Content-Length") == str(len(resp_data))
    assert resp.headers.get("Content-Disposition") == expected_content_disposition

    await resp.release()

    outer_file_descriptor.close()


async def test_response_with_payload_disp(aiohttp_client, fname) -> None:
    outer_file_descriptor = None

    with fname.open("rb") as f:
        data = f.read()

    async def handler(request):
        nonlocal outer_file_descriptor
        outer_file_descriptor = fname.open("rb")
        pl = aiohttp.get_payload(outer_file_descriptor)
        pl.set_content_disposition("inline", filename="test.txt")
        return web.Response(body=pl, headers={"content-type": "text/binary"})

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/")
    assert 200 == resp.status
    resp_data = await resp.read()
    assert resp_data == data
    assert resp.headers.get("Content-Type") == "text/binary"
    assert resp.headers.get("Content-Length") == str(len(resp_data))
    assert resp.headers.get("Content-Disposition") == 'inline; filename="test.txt"'

    await resp.release()

    outer_file_descriptor.close()


async def test_response_with_payload_stringio(aiohttp_client, fname) -> None:
    async def handler(request):
        return web.Response(body=io.StringIO("test"))

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/")
    assert 200 == resp.status
    resp_data = await resp.read()
    assert resp_data == b"test"

    await resp.release()


@pytest.fixture(params=["gzip", "deflate", "deflate-raw"])
def compressor_case(
    request: pytest.FixtureRequest,
    parametrize_zlib_backend: None,
) -> Generator[Tuple[ZLibCompressObjProtocol, str], None, None]:
    encoding: str = request.param
    max_wbits: int = ZLibBackend.MAX_WBITS

    encoding_to_wbits: Dict[str, int] = {
        "deflate": max_wbits,
        "deflate-raw": -max_wbits,
        "gzip": 16 + max_wbits,
    }

    compressor = ZLibBackend.compressobj(wbits=encoding_to_wbits[encoding])
    yield (compressor, "deflate" if encoding.startswith("deflate") else encoding)


async def test_response_with_precompressed_body(
    aiohttp_client: AiohttpClient,
    compressor_case: Tuple[ZLibCompressObjProtocol, str],
) -> None:
    compressor, encoding = compressor_case

    async def handler(request):
        headers = {"Content-Encoding": encoding}
        data = compressor.compress(b"mydata") + compressor.flush()
        return web.Response(body=data, headers=headers)

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/")
    assert 200 == resp.status
    data = await resp.read()
    assert b"mydata" == data
    assert resp.headers.get("Content-Encoding") == encoding

    await resp.release()


async def test_response_with_precompressed_body_brotli(aiohttp_client) -> None:
    async def handler(request):
        headers = {"Content-Encoding": "br"}
        return web.Response(body=brotli.compress(b"mydata"), headers=headers)

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/")
    assert 200 == resp.status
    data = await resp.read()
    assert b"mydata" == data
    assert resp.headers.get("Content-Encoding") == "br"

    await resp.release()


async def test_bad_request_payload(aiohttp_client) -> None:
    async def handler(request):
        assert request.method == "POST"

        with pytest.raises(aiohttp.web.RequestPayloadError):
            await request.content.read()

        return web.Response()

    app = web.Application()
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    resp = await client.post("/", data=b"test", headers={"content-encoding": "gzip"})
    assert 200 == resp.status

    await resp.release()


async def test_stream_response_multiple_chunks(aiohttp_client) -> None:
    async def handler(request):
        resp = web.StreamResponse()
        resp.enable_chunked_encoding()
        await resp.prepare(request)
        await resp.write(b"x")
        await resp.write(b"y")
        await resp.write(b"z")
        return resp

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/")
    assert 200 == resp.status
    data = await resp.read()
    assert b"xyz" == data

    await resp.release()


async def test_start_without_routes(aiohttp_client) -> None:

    app = web.Application()
    client = await aiohttp_client(app)

    resp = await client.get("/")
    assert 404 == resp.status

    await resp.release()


async def test_requests_count(aiohttp_client) -> None:
    async def handler(request):
        return web.Response()

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)
    assert client.server.handler.requests_count == 0

    resp = await client.get("/")
    assert 200 == resp.status
    assert client.server.handler.requests_count == 1
    await resp.release()

    resp = await client.get("/")
    assert 200 == resp.status
    assert client.server.handler.requests_count == 2
    await resp.release()

    resp = await client.get("/")
    assert 200 == resp.status
    assert client.server.handler.requests_count == 3
    await resp.release()


async def test_redirect_url(aiohttp_client) -> None:
    async def redirector(request):
        raise web.HTTPFound(location=URL("/redirected"))

    async def redirected(request):
        return web.Response()

    app = web.Application()
    app.router.add_get("/redirector", redirector)
    app.router.add_get("/redirected", redirected)

    client = await aiohttp_client(app)
    resp = await client.get("/redirector")
    assert resp.status == 200

    await resp.release()


async def test_simple_subapp(aiohttp_client) -> None:
    async def handler(request):
        return web.Response(text="OK")

    app = web.Application()
    subapp = web.Application()
    subapp.router.add_get("/to", handler)
    app.add_subapp("/path", subapp)

    client = await aiohttp_client(app)
    resp = await client.get("/path/to")
    assert resp.status == 200
    txt = await resp.text()
    assert "OK" == txt

    await resp.release()


async def test_subapp_reverse_url(aiohttp_client) -> None:
    async def handler(request):
        raise web.HTTPMovedPermanently(location=subapp.router["name"].url_for())

    async def handler2(request):
        return web.Response(text="OK")

    app = web.Application()
    subapp = web.Application()
    subapp.router.add_get("/to", handler)
    subapp.router.add_get("/final", handler2, name="name")
    app.add_subapp("/path", subapp)

    client = await aiohttp_client(app)
    resp = await client.get("/path/to")
    assert resp.status == 200
    txt = await resp.text()
    assert "OK" == txt
    assert resp.url.path == "/path/final"

    await resp.release()


async def test_subapp_reverse_variable_url(aiohttp_client) -> None:
    async def handler(request):
        raise web.HTTPMovedPermanently(
            location=subapp.router["name"].url_for(part="final")
        )

    async def handler2(request):
        return web.Response(text="OK")

    app = web.Application()
    subapp = web.Application()
    subapp.router.add_get("/to", handler)
    subapp.router.add_get("/{part}", handler2, name="name")
    app.add_subapp("/path", subapp)

    client = await aiohttp_client(app)
    resp = await client.get("/path/to")
    assert resp.status == 200
    txt = await resp.text()
    assert "OK" == txt
    assert resp.url.path == "/path/final"

    await resp.release()


async def test_subapp_reverse_static_url(aiohttp_client) -> None:
    fname = "aiohttp.png"

    async def handler(request):
        raise web.HTTPMovedPermanently(
            location=subapp.router["name"].url_for(filename=fname)
        )

    app = web.Application()
    subapp = web.Application()
    subapp.router.add_get("/to", handler)
    here = pathlib.Path(__file__).parent
    subapp.router.add_static("/static", here, name="name")
    app.add_subapp("/path", subapp)

    client = await aiohttp_client(app)
    resp = await client.get("/path/to")
    assert resp.url.path == "/path/static/" + fname
    assert resp.status == 200
    body = await resp.read()

    await resp.release()

    with (here / fname).open("rb") as f:
        assert body == f.read()


async def test_subapp_app(aiohttp_client) -> None:
    async def handler(request):
        assert request.app is subapp
        return web.Response(text="OK")

    app = web.Application()
    subapp = web.Application()
    subapp.router.add_get("/to", handler)
    app.add_subapp("/path/", subapp)

    client = await aiohttp_client(app)
    resp = await client.get("/path/to")
    assert resp.status == 200
    txt = await resp.text()
    assert "OK" == txt

    await resp.release()


async def test_subapp_not_found(aiohttp_client) -> None:
    async def handler(request):
        return web.Response(text="OK")

    app = web.Application()
    subapp = web.Application()
    subapp.router.add_get("/to", handler)
    app.add_subapp("/path/", subapp)

    client = await aiohttp_client(app)
    resp = await client.get("/path/other")
    assert resp.status == 404

    await resp.release()


async def test_subapp_not_found2(aiohttp_client) -> None:
    async def handler(request):
        return web.Response(text="OK")

    app = web.Application()
    subapp = web.Application()
    subapp.router.add_get("/to", handler)
    app.add_subapp("/path/", subapp)

    client = await aiohttp_client(app)
    resp = await client.get("/invalid/other")
    assert resp.status == 404

    await resp.release()


async def test_subapp_not_allowed(aiohttp_client) -> None:
    async def handler(request):
        return web.Response(text="OK")

    app = web.Application()
    subapp = web.Application()
    subapp.router.add_get("/to", handler)
    app.add_subapp("/path/", subapp)

    client = await aiohttp_client(app)
    resp = await client.post("/path/to")
    assert resp.status == 405
    assert resp.headers["Allow"] == "GET,HEAD"

    await resp.release()


async def test_subapp_cannot_add_app_in_handler(aiohttp_client) -> None:
    async def handler(request):
        request.match_info.add_app(app)
        return web.Response(text="OK")

    app = web.Application()
    subapp = web.Application()
    subapp.router.add_get("/to", handler)
    app.add_subapp("/path/", subapp)

    client = await aiohttp_client(app)
    resp = await client.get("/path/to")
    assert resp.status == 500

    await resp.release()


async def test_subapp_middlewares(aiohttp_client) -> None:
    order = []

    async def handler(request):
        return web.Response(text="OK")

    async def middleware_factory(app, handler: Handler):
        async def middleware(request):
            order.append((1, app))
            resp = await handler(request)
            assert 200 == resp.status
            order.append((2, app))
            return resp

        return middleware

    app = web.Application(middlewares=[middleware_factory])
    subapp1 = web.Application(middlewares=[middleware_factory])
    subapp2 = web.Application(middlewares=[middleware_factory])
    subapp2.router.add_get("/to", handler)
    with pytest.warns(DeprecationWarning):
        subapp1.add_subapp("/b/", subapp2)
        app.add_subapp("/a/", subapp1)
        client = await aiohttp_client(app)

    resp = await client.get("/a/b/to")
    assert resp.status == 200
    assert [
        (1, app),
        (1, subapp1),
        (1, subapp2),
        (2, subapp2),
        (2, subapp1),
        (2, app),
    ] == order

    await resp.release()


async def test_subapp_on_response_prepare(aiohttp_client) -> None:
    order = []

    async def handler(request):
        return web.Response(text="OK")

    def make_signal(app):
        async def on_response(request, response):
            order.append(app)

        return on_response

    app = web.Application()
    app.on_response_prepare.append(make_signal(app))
    subapp1 = web.Application()
    subapp1.on_response_prepare.append(make_signal(subapp1))
    subapp2 = web.Application()
    subapp2.on_response_prepare.append(make_signal(subapp2))
    subapp2.router.add_get("/to", handler)
    subapp1.add_subapp("/b/", subapp2)
    app.add_subapp("/a/", subapp1)

    client = await aiohttp_client(app)
    resp = await client.get("/a/b/to")
    assert resp.status == 200
    assert [app, subapp1, subapp2] == order

    await resp.release()


async def test_subapp_on_startup(aiohttp_server) -> None:
    order = []

    async def on_signal(app):
        order.append(app)

    app = web.Application()
    app.on_startup.append(on_signal)
    subapp1 = web.Application()
    subapp1.on_startup.append(on_signal)
    subapp2 = web.Application()
    subapp2.on_startup.append(on_signal)
    subapp1.add_subapp("/b/", subapp2)
    app.add_subapp("/a/", subapp1)

    await aiohttp_server(app)

    assert [app, subapp1, subapp2] == order


async def test_subapp_on_shutdown(aiohttp_server) -> None:
    order = []

    async def on_signal(app):
        order.append(app)

    app = web.Application()
    app.on_shutdown.append(on_signal)
    subapp1 = web.Application()
    subapp1.on_shutdown.append(on_signal)
    subapp2 = web.Application()
    subapp2.on_shutdown.append(on_signal)
    subapp1.add_subapp("/b/", subapp2)
    app.add_subapp("/a/", subapp1)

    server = await aiohttp_server(app)
    await server.close()

    assert [app, subapp1, subapp2] == order


async def test_subapp_on_cleanup(aiohttp_server) -> None:
    order = []

    async def on_signal(app):
        order.append(app)

    app = web.Application()
    app.on_cleanup.append(on_signal)
    subapp1 = web.Application()
    subapp1.on_cleanup.append(on_signal)
    subapp2 = web.Application()
    subapp2.on_cleanup.append(on_signal)
    subapp1.add_subapp("/b/", subapp2)
    app.add_subapp("/a/", subapp1)

    server = await aiohttp_server(app)
    await server.close()

    assert [app, subapp1, subapp2] == order


@pytest.mark.parametrize(
    "route,expected,middlewares",
    [
        ("/sub/", ["A: root", "C: sub", "D: sub"], "AC"),
        ("/", ["A: root", "B: root"], "AC"),
        ("/sub/", ["A: root", "D: sub"], "A"),
        ("/", ["A: root", "B: root"], "A"),
        ("/sub/", ["C: sub", "D: sub"], "C"),
        ("/", ["B: root"], "C"),
        ("/sub/", ["D: sub"], ""),
        ("/", ["B: root"], ""),
    ],
)
async def test_subapp_middleware_context(aiohttp_client, route, expected, middlewares):
    values = []

    def show_app_context(appname):
        @web.middleware
        async def middleware(request, handler: Handler):
            values.append(f"{appname}: {request.app[my_value]}")
            return await handler(request)

        return middleware

    def make_handler(appname):
        async def handler(request):
            values.append(f"{appname}: {request.app[my_value]}")
            return web.Response(text="Ok")

        return handler

    app = web.Application()
    my_value = web.AppKey("my_value", str)
    app[my_value] = "root"
    if "A" in middlewares:
        app.middlewares.append(show_app_context("A"))
    app.router.add_get("/", make_handler("B"))

    subapp = web.Application()
    subapp[my_value] = "sub"
    if "C" in middlewares:
        subapp.middlewares.append(show_app_context("C"))
    subapp.router.add_get("/", make_handler("D"))
    app.add_subapp("/sub/", subapp)

    client = await aiohttp_client(app)
    resp = await client.get(route)
    assert 200 == resp.status
    assert "Ok" == await resp.text()
    assert expected == values

    await resp.release()


async def test_custom_date_header(aiohttp_client) -> None:
    async def handler(request):
        return web.Response(headers={"Date": "Sun, 30 Oct 2016 03:13:52 GMT"})

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/")
    assert 200 == resp.status
    assert resp.headers["Date"] == "Sun, 30 Oct 2016 03:13:52 GMT"

    await resp.release()


async def test_response_prepared_with_clone(aiohttp_client) -> None:
    async def handler(request):
        cloned = request.clone()
        resp = web.StreamResponse()
        await resp.prepare(cloned)
        return resp

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/")
    assert 200 == resp.status

    await resp.release()


async def test_app_max_client_size(aiohttp_client) -> None:
    async def handler(request):
        await request.post()
        return web.Response(body=b"ok")

    max_size = 1024**2
    app = web.Application()
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)
    data = {"long_string": max_size * "x" + "xxx"}
    with pytest.warns(ResourceWarning):
        resp = await client.post("/", data=data)
    assert 413 == resp.status
    resp_text = await resp.text()
    assert "Maximum request body size 1048576 exceeded, actual body size" in resp_text
    # Maximum request body size X exceeded, actual body size X
    body_size = int(resp_text.split()[-1])
    assert body_size >= max_size

    await resp.release()


async def test_app_max_client_size_adjusted(aiohttp_client) -> None:
    async def handler(request):
        await request.post()
        return web.Response(body=b"ok")

    default_max_size = 1024**2
    custom_max_size = default_max_size * 2
    app = web.Application(client_max_size=custom_max_size)
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)
    data = {"long_string": default_max_size * "x" + "xxx"}

    with pytest.warns(ResourceWarning):
        resp = await client.post("/", data=data)
    assert 200 == resp.status
    resp_text = await resp.text()
    assert "ok" == resp_text
    await resp.release()

    too_large_data = {"log_string": custom_max_size * "x" + "xxx"}
    with pytest.warns(ResourceWarning):
        resp = await client.post("/", data=too_large_data)
    assert 413 == resp.status
    resp_text = await resp.text()
    assert "Maximum request body size 2097152 exceeded, actual body size" in resp_text
    # Maximum request body size X exceeded, actual body size X
    body_size = int(resp_text.split()[-1])
    assert body_size >= custom_max_size

    await resp.release()


async def test_app_max_client_size_none(aiohttp_client) -> None:
    async def handler(request):
        await request.post()
        return web.Response(body=b"ok")

    default_max_size = 1024**2
    custom_max_size = None
    app = web.Application(client_max_size=custom_max_size)
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    data = {"long_string": default_max_size * "x" + "xxx"}
    with pytest.warns(ResourceWarning):
        resp = await client.post("/", data=data)
    assert 200 == resp.status
    resp_text = await resp.text()
    assert "ok" == resp_text
    await resp.release()

    too_large_data = {"log_string": default_max_size * 2 * "x"}
    with pytest.warns(ResourceWarning):
        resp = await client.post("/", data=too_large_data)
    assert 200 == resp.status
    resp_text = await resp.text()
    assert resp_text == "ok"
    await resp.release()


async def test_post_max_client_size(aiohttp_client) -> None:
    async def handler(request):
        await request.post()
        return web.Response()

    app = web.Application(client_max_size=10)
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    with io.BytesIO(b"test") as file_handle:
        data = {"long_string": 1024 * "x", "file": file_handle}
        resp = await client.post("/", data=data)

        assert 413 == resp.status
        resp_text = await resp.text()
        assert (
            "Maximum request body size 10 exceeded, "
            "actual body size 1024" in resp_text
        )
        data["file"].close()

        await resp.release()


async def test_post_max_client_size_for_file(aiohttp_client) -> None:
    async def handler(request):
        await request.post()
        return web.Response()

    app = web.Application(client_max_size=2)
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    with io.BytesIO(b"test") as file_handle:
        data = {"file": file_handle}
        resp = await client.post("/", data=data)

    assert 413 == resp.status

    await resp.release()


async def test_response_with_bodypart(aiohttp_client) -> None:
    async def handler(request):
        reader = await request.multipart()
        part = await reader.next()
        return web.Response(body=part)

    app = web.Application(client_max_size=2)
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    with io.BytesIO(b"test") as file_handle:
        data = {"file": file_handle}
        resp = await client.post("/", data=data)

        assert 200 == resp.status
        body = await resp.read()
        assert body == b"test"

        disp = multipart.parse_content_disposition(resp.headers["content-disposition"])
        assert disp == ("attachment", {"name": "file", "filename": "file"})

        await resp.release()


async def test_response_with_bodypart_named(aiohttp_client, tmp_path) -> None:
    async def handler(request):
        reader = await request.multipart()
        part = await reader.next()
        return web.Response(body=part)

    app = web.Application(client_max_size=2)
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    f = tmp_path / "foobar.txt"
    f.write_text("test", encoding="utf8")
    with f.open("rb") as fd:
        data = {"file": fd}
        resp = await client.post("/", data=data)

        assert 200 == resp.status
        body = await resp.read()
    assert body == b"test"

    disp = multipart.parse_content_disposition(resp.headers["content-disposition"])
    assert disp == ("attachment", {"name": "file", "filename": "foobar.txt"})

    await resp.release()


async def test_response_with_bodypart_invalid_name(aiohttp_client) -> None:
    async def handler(request):
        reader = await request.multipart()
        part = await reader.next()
        return web.Response(body=part)

    app = web.Application(client_max_size=2)
    app.router.add_post("/", handler)
    client = await aiohttp_client(app)

    with aiohttp.MultipartWriter() as mpwriter:
        mpwriter.append(b"test")
        resp = await client.post("/", data=mpwriter)

    assert 200 == resp.status
    body = await resp.read()
    assert body == b"test"

    assert "content-disposition" not in resp.headers

    await resp.release()


async def test_request_clone(aiohttp_client) -> None:
    async def handler(request):
        r2 = request.clone(method="POST")
        assert r2.method == "POST"
        assert r2.match_info is request.match_info
        return web.Response()

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/")
    assert 200 == resp.status
    await resp.release()


async def test_await(aiohttp_server) -> None:
    async def handler(request):
        resp = web.StreamResponse(headers={"content-length": str(4)})
        await resp.prepare(request)
        with pytest.deprecated_call(
            match=r"^drain method is deprecated, use await resp\.write\(\)$",
        ):
            await resp.drain()
        await asyncio.sleep(0.01)
        await resp.write(b"test")
        await asyncio.sleep(0.01)
        await resp.write_eof()
        return resp

    app = web.Application()
    app.router.add_route("GET", "/", handler)
    server = await aiohttp_server(app)

    async with aiohttp.ClientSession() as session:
        resp = await session.get(server.make_url("/"))
        assert resp.status == 200
        assert resp.connection is not None
        await resp.read()
        await resp.release()
        assert resp.connection is None


async def test_response_context_manager(aiohttp_server) -> None:
    async def handler(request):
        return web.Response()

    app = web.Application()
    app.router.add_route("GET", "/", handler)
    server = await aiohttp_server(app)
    session = aiohttp.ClientSession()
    resp = await session.get(server.make_url("/"))
    async with resp:
        assert resp.status == 200
    assert resp.connection is None

    await session.close()


async def test_response_context_manager_error(aiohttp_server) -> None:
    async def handler(request):
        return web.Response(text="some text")

    app = web.Application()
    app.router.add_route("GET", "/", handler)
    server = await aiohttp_server(app)
    session = aiohttp.ClientSession()
    cm = session.get(server.make_url("/"))
    resp = await cm
    with pytest.raises(RuntimeError):
        async with resp:
            assert resp.status == 200
            resp.content.set_exception(RuntimeError())
            await resp.read()
    assert resp.closed

    # Wait for any pending operations to complete
    await resp.wait_for_close()

    assert session._connector is not None
    assert len(session._connector._conns) == 1

    await session.close()


async def aiohttp_client_api_context_manager(aiohttp_server):
    async def handler(request):
        return web.Response()

    app = web.Application()
    app.router.add_route("GET", "/", handler)
    server = await aiohttp_server(app)

    async with aiohttp.ClientSession() as session:
        async with session.get(server.make_url("/")) as resp:
            assert resp.status == 200
            assert resp.connection is None
    assert resp.connection is None


async def test_context_manager_close_on_release(aiohttp_server, mocker) -> None:
    async def handler(request):
        resp = web.StreamResponse()
        await resp.prepare(request)
        with pytest.deprecated_call(
            match=r"^drain method is deprecated, use await resp\.write\(\)$",
        ):
            await resp.drain()
        await asyncio.sleep(10)
        return resp

    app = web.Application()
    app.router.add_route("GET", "/", handler)
    server = await aiohttp_server(app)

    async with aiohttp.ClientSession() as session:
        resp = await session.get(server.make_url("/"))
        proto = resp.connection._protocol
        mocker.spy(proto, "close")
        async with resp:
            assert resp.status == 200
            assert resp.connection is not None
        assert resp.connection is None
        assert proto.close.called

        await resp.release()  # Trigger handler completion


async def test_iter_any(aiohttp_server) -> None:

    data = b"0123456789" * 1024

    async def handler(request):
        buf = []
        async for raw in request.content.iter_any():
            buf.append(raw)
        assert b"".join(buf) == data
        return web.Response()

    app = web.Application()
    app.router.add_route("POST", "/", handler)
    server = await aiohttp_server(app)

    async with aiohttp.ClientSession() as session:
        async with session.post(server.make_url("/"), data=data) as resp:
            assert resp.status == 200


async def test_request_tracing(aiohttp_server: AiohttpServer) -> None:
    on_request_start = mock.AsyncMock()
    on_request_end = mock.AsyncMock()
    on_dns_resolvehost_start = mock.AsyncMock()
    on_dns_resolvehost_end = mock.AsyncMock()
    on_request_redirect = mock.AsyncMock()
    on_connection_create_start = mock.AsyncMock()
    on_connection_create_end = mock.AsyncMock()

    async def redirector(request):
        raise web.HTTPFound(location=URL("/redirected"))

    async def redirected(request):
        return web.Response()

    trace_config = TraceConfig()

    trace_config.on_request_start.append(on_request_start)
    trace_config.on_request_end.append(on_request_end)
    trace_config.on_request_redirect.append(on_request_redirect)
    trace_config.on_connection_create_start.append(on_connection_create_start)
    trace_config.on_connection_create_end.append(on_connection_create_end)
    trace_config.on_dns_resolvehost_start.append(on_dns_resolvehost_start)
    trace_config.on_dns_resolvehost_end.append(on_dns_resolvehost_end)

    app = web.Application()
    app.router.add_get("/redirector", redirector)
    app.router.add_get("/redirected", redirected)
    server = await aiohttp_server(app)

    class FakeResolver:
        _LOCAL_HOST = {0: "127.0.0.1", socket.AF_INET: "127.0.0.1"}

        def __init__(self, fakes):
            # fakes -- dns -> port dict
            self._fakes = fakes
            self._resolver = aiohttp.DefaultResolver()

        async def resolve(self, host, port=0, family=socket.AF_INET):
            fake_port = self._fakes.get(host)
            if fake_port is not None:
                return [
                    {
                        "hostname": host,
                        "host": self._LOCAL_HOST[family],
                        "port": fake_port,
                        "family": socket.AF_INET,
                        "proto": 0,
                        "flags": socket.AI_NUMERICHOST,
                    }
                ]
            else:
                return await self._resolver.resolve(host, port, family)

    resolver = FakeResolver({"example.com": server.port})
    connector = aiohttp.TCPConnector(resolver=resolver)
    client = aiohttp.ClientSession(connector=connector, trace_configs=[trace_config])

    resp = await client.get("http://example.com/redirector", data="foo")

    assert on_request_start.called
    assert on_request_end.called
    assert on_dns_resolvehost_start.called
    assert on_dns_resolvehost_end.called
    assert on_request_redirect.called
    assert on_connection_create_start.called
    assert on_connection_create_end.called

    await resp.release()
    await client.close()


async def test_return_http_exception_deprecated(aiohttp_client) -> None:
    async def handler(request):
        return web.HTTPForbidden()

    app = web.Application()
    app.router.add_route("GET", "/", handler)
    client = await aiohttp_client(app)

    with pytest.warns(DeprecationWarning):
        await client.get("/")


async def test_request_path(aiohttp_client) -> None:
    async def handler(request):
        assert request.path_qs == "/path%20to?a=1"
        assert request.path == "/path to"
        assert request.raw_path == "/path%20to?a=1"
        return web.Response(body=b"OK")

    app = web.Application()
    app.router.add_get("/path to", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/path to", params={"a": "1"})
    assert 200 == resp.status
    txt = await resp.text()
    assert "OK" == txt
    await resp.release()


async def test_app_add_routes(aiohttp_client) -> None:
    async def handler(request):
        return web.Response()

    app = web.Application()
    app.add_routes([web.get("/get", handler)])

    client = await aiohttp_client(app)
    resp = await client.get("/get")
    assert resp.status == 200
    await resp.release()


async def test_request_headers_type(aiohttp_client) -> None:
    async def handler(request):
        assert isinstance(request.headers, CIMultiDictProxy)
        return web.Response()

    app = web.Application()
    app.add_routes([web.get("/get", handler)])

    client = await aiohttp_client(app)
    resp = await client.get("/get")
    assert resp.status == 200
    await resp.release()


async def test_signal_on_error_handler(aiohttp_client) -> None:
    async def on_prepare(request, response):
        response.headers["X-Custom"] = "val"

    app = web.Application()
    app.on_response_prepare.append(on_prepare)

    client = await aiohttp_client(app)
    resp = await client.get("/")
    assert resp.status == 404
    assert resp.headers["X-Custom"] == "val"
    await resp.release()


@pytest.mark.skipif(
    "HttpRequestParserC" not in dir(aiohttp.http_parser),
    reason="C based HTTP parser not available",
)
async def test_bad_method_for_c_http_parser_not_hangs(aiohttp_client) -> None:
    app = web.Application()
    timeout = aiohttp.ClientTimeout(sock_read=0.2)
    client = await aiohttp_client(app, timeout=timeout)
    resp = await client.request("GET1", "/")
    assert 400 == resp.status


async def test_read_bufsize(aiohttp_client) -> None:
    async def handler(request):
        ret = request.content.get_read_buffer_limits()
        data = await request.text()  # read posted data
        return web.Response(text=f"{data} {ret!r}")

    app = web.Application(handler_args={"read_bufsize": 2})
    app.router.add_post("/", handler)

    client = await aiohttp_client(app)
    resp = await client.post("/", data=b"data")
    assert resp.status == 200
    assert await resp.text() == "data (2, 4)"
    await resp.release()


@pytest.mark.parametrize(
    "auto_decompress,len_of", [(True, "uncompressed"), (False, "compressed")]
)
@pytest.mark.usefixtures("parametrize_zlib_backend")
async def test_auto_decompress(
    aiohttp_client,
    auto_decompress,
    len_of,
) -> None:
    async def handler(request):
        data = await request.read()
        return web.Response(text=str(len(data)))

    app = web.Application(handler_args={"auto_decompress": auto_decompress})
    app.router.add_post("/", handler)

    client = await aiohttp_client(app)
    uncompressed = b"dataaaaaaaaaaaaaaaaaaaaaaaaa"
    compressor = ZLibBackend.compressobj(wbits=16 + ZLibBackend.MAX_WBITS)
    compressed = compressor.compress(uncompressed) + compressor.flush()
    assert len(compressed) != len(uncompressed)
    headers = {"content-encoding": "gzip"}
    resp = await client.post("/", data=compressed, headers=headers)
    assert resp.status == 200
    assert await resp.text() == str(len(locals()[len_of]))
    await resp.release()


@pytest.mark.parametrize(
    "status",
    [101, 204],
)
async def test_response_101_204_no_content_length_http11(
    status, aiohttp_client
) -> None:
    async def handler(_):
        return web.Response(status=status)

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app, version="1.1")
    resp = await client.get("/")
    assert CONTENT_LENGTH not in resp.headers
    assert TRANSFER_ENCODING not in resp.headers
    await resp.release()


async def test_stream_response_headers_204(aiohttp_client):
    async def handler(_):
        return web.StreamResponse(status=204)

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)
    resp = await client.get("/")
    assert CONTENT_TYPE not in resp.headers
    assert TRANSFER_ENCODING not in resp.headers
    await resp.release()


async def test_httpfound_cookies_302(aiohttp_client: Any) -> None:
    async def handler(_):
        resp = web.HTTPFound("/")
        resp.set_cookie("my-cookie", "cookie-value")
        raise resp

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app)

    resp = await client.get("/", allow_redirects=False)
    assert "my-cookie" in resp.cookies
    await resp.release()


@pytest.mark.parametrize("status", (101, 204, 304))
@pytest.mark.parametrize("version", (HttpVersion10, HttpVersion11))
async def test_no_body_for_1xx_204_304_responses(
    aiohttp_client: Any, status: int, version: HttpVersion
) -> None:
    """Test no body is present for for 1xx, 204, and 304 responses."""

    async def handler(_):
        return web.Response(status=status, body=b"should not get to client")

    app = web.Application()
    app.router.add_get("/", handler)
    client = await aiohttp_client(app, version=version)
    resp = await client.get("/")
    assert CONTENT_TYPE not in resp.headers
    assert TRANSFER_ENCODING not in resp.headers
    await resp.read() == b""
    await resp.release()


async def test_keepalive_race_condition(aiohttp_client: Any) -> None:
    protocol = None
    orig_data_received = RequestHandler.data_received

    def delay_received(self, data: bytes) -> None:
        """Emulate race condition.

        The keepalive callback needs to be called between data_received() and
        when start() resumes from the waiter set within data_received().
        """
        data = orig_data_received(self, data)
        if protocol is None:  # First request creating the keepalive connection.
            return data

        assert self is protocol
        assert protocol._keepalive_handle is not None
        # Cancel existing callback that would run at some point in future.
        protocol._keepalive_handle.cancel()
        protocol._keepalive_handle = None

        # Set next run time into the past and run callback manually.
        protocol._next_keepalive_close_time = asyncio.get_running_loop().time() - 1
        protocol._process_keepalive()

        return data

    async def handler(request: web.Request) -> web.Response:
        nonlocal protocol
        protocol = request.protocol
        return web.Response()

    target = "aiohttp.web_protocol.RequestHandler.data_received"
    with mock.patch(target, delay_received):
        app = web.Application()
        app.router.add_get("/", handler)
        client = await aiohttp_client(app)

        # Open connection, so we have a keepalive connection and reference to protocol.
        async with client.get("/") as resp:
            assert resp.status == 200
        assert protocol is not None
        # Make 2nd request which will hit the race condition.
        async with client.get("/") as resp:
            assert resp.status == 200


async def test_keepalive_expires_on_time(aiohttp_client: AiohttpClient) -> None:
    """Test that the keepalive handle expires on time."""

    async def handler(request: web.Request) -> web.Response:
        body = await request.read()
        assert b"" == body
        return web.Response(body=b"OK")

    app = web.Application()
    app.router.add_route("GET", "/", handler)

    connector = aiohttp.TCPConnector(limit=1)
    client = await aiohttp_client(app, connector=connector)

    loop = asyncio.get_running_loop()
    now = loop.time()

    # Patch loop time so we can control when the keepalive timeout is processed
    with mock.patch.object(loop, "time") as loop_time_mock:
        loop_time_mock.return_value = now
        resp1 = await client.get("/")
        await resp1.read()
        request_handler = client.server.handler.connections[0]

        # Ensure the keep alive handle is set
        assert request_handler._keepalive_handle is not None

        # Set the loop time to exactly the keepalive timeout
        loop_time_mock.return_value = request_handler._next_keepalive_close_time

        # sleep twice to ensure the keep alive timeout is processed
        await asyncio.sleep(0)
        await asyncio.sleep(0)

        # Ensure the keep alive handle expires
        assert request_handler._keepalive_handle is None
