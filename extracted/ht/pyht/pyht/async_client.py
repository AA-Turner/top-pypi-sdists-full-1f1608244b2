from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from datetime import datetime, timedelta
import io
import json
import logging
import os
import sys
import tempfile
import time
from typing import Any, Dict, AsyncGenerator, AsyncIterable, AsyncIterator, Coroutine, Tuple, Optional, Union
from websockets.asyncio.client import connect, ClientConnection
from websockets.exceptions import ConnectionClosed

import aiohttp
import filelock
import grpc
from grpc import ssl_channel_credentials, StatusCode
from grpc.aio import Call, Channel, insecure_channel, secure_channel, UnaryStreamCall

from .client import _audio_begins_at, CLIENT_RETRY_OPTIONS, CongestionCtrl, \
        http_prepare_dict, output_format_to_mime_type, TTSOptions, Format
from .inference_coordinates import get_coordinates_async, InferenceCoordinatesOptions
from .lease import Lease, LeaseFactory
from .protos import api_pb2, api_pb2_grpc
from .telemetry import Metrics, Telemetry
from .utils import prepare_text, SENTENCE_END_REGEX, get_voice_engine_and_protocol


TtsUnaryStream = UnaryStreamCall[api_pb2.TtsRequest, api_pb2.TtsResponse]


# asyncio.to_thread was not added until Python 3.8+, so we make our own here.
if sys.version_info >= (3, 9):
    to_thread = asyncio.to_thread
else:
    import contextvars
    import functools

    async def to_thread(func, /, *args, **kwargs):
        loop = asyncio.get_running_loop()
        ctx = contextvars.copy_context()
        func_call = functools.partial(ctx.run, func, *args, **kwargs)
        return await loop.run_in_executor(None, func_call)


class AsyncClient:
    LEASE_DATA: Optional[bytes] = None
    LEASE_CACHE_PATH: str = os.path.join(tempfile.gettempdir(), 'playht.temporary.lease')
    LEASE_LOCK = asyncio.Lock()

    @dataclass
    class AdvancedOptions:
        api_url: str = "https://api.play.ht/api"
        congestion_ctrl: CongestionCtrl = CongestionCtrl.OFF
        metrics_buffer_size: int = 1000
        remove_ssml_tags: bool = False

        # gRPC (PlayHT2.0-turbo, Play3.0-mini-grpc)
        grpc_addr: Optional[str] = None
        insecure: bool = False
        fallback_enabled: bool = False
        auto_refresh_lease: bool = True
        disable_lease_disk_cache: bool = False

        # HTTP/WebSocket (Play3.0-mini-http, Play3.0-mini-ws)
        inference_coordinates_options: InferenceCoordinatesOptions = field(default_factory=InferenceCoordinatesOptions)

    def __init__(
        self,
        user_id: str,
        api_key: str,
        auto_connect: bool = True,
        advanced: Optional["AsyncClient.AdvancedOptions"] = None,
    ):
        assert user_id, "user_id is required"
        assert api_key, "api_key is required"

        self._advanced = advanced or self.AdvancedOptions()

        async def lease_factory() -> Lease:
            _factory = LeaseFactory(user_id, api_key, self._advanced.api_url)
            if self._advanced.disable_lease_disk_cache:
                return await asyncio.to_thread(_factory)
            maybe_data = await self._lease_cache_read()
            if maybe_data is not None:
                lease = Lease(maybe_data)
                if lease.expires > datetime.now() + timedelta(minutes=5):
                    return lease
            lease = await asyncio.to_thread(_factory)
            await self._lease_cache_write(lease.data)
            return lease

        self._lease_factory = lease_factory
        self._lease: Optional[Lease] = None
        self._rpc: Optional[Tuple[str, Channel]] = None
        self._fallback_rpc: Optional[Tuple[str, Channel]] = None
        self._lock = asyncio.Lock()
        self._stop_lease_loop = asyncio.Event()
        if self._advanced.auto_refresh_lease:
            self._lease_loop_future = asyncio.ensure_future(self._lease_loop())
        else:
            self._lease_loop_future = asyncio.Future()
            self._lease_loop_future.set_result(None)
        self._telemetry = Telemetry(self._advanced.metrics_buffer_size)
        self._user_id = user_id
        self._api_key = api_key
        self._inference_coordinates: Optional[Dict[str, Any]] = None
        self._ws: Optional[ClientConnection] = None
        self._ws_requests_sent = 0
        self._ws_responses_received = 0

        if self._advanced.congestion_ctrl == CongestionCtrl.STATIC_MAR_2023:
            self._max_attempts = 3
            self._backoff = 0.05
        else:
            self._max_attempts = 1
            self._backoff = 0

        if auto_connect and not self._advanced.auto_refresh_lease:
            asyncio.ensure_future(self.refresh_lease())
        if auto_connect:
            asyncio.ensure_future(self.warmup())

    async def ensure_inference_coordinates(self, force: bool = False):
        if self._inference_coordinates is None or \
                self._inference_coordinates["refresh_at_ms"] < time.time_ns() // 1000000 or \
                force:
            if self._advanced.inference_coordinates_options.coordinates_generator_function_async is not None:
                self._inference_coordinates = await self._advanced.inference_coordinates_options.\
                        coordinates_generator_function_async(self._user_id, self._api_key,
                                                             self._advanced.inference_coordinates_options)
            else:
                self._inference_coordinates = await get_coordinates_async(self._user_id, self._api_key,
                                                                          self._advanced.inference_coordinates_options)

        assert self._inference_coordinates is not None, "No connection"

    async def warmup(self):
        await self.ensure_inference_coordinates()

        try:
            async with aiohttp.ClientSession() as session:
                assert self._inference_coordinates is not None, "No connection"
                async with session.options(self._inference_coordinates["Play3.0-mini"]["http_streaming_url"],
                                           headers={"Origin": "https://play.ht",
                                                    "Access-Control-Request-Method": "POST"}) as resp:
                    resp.raise_for_status()
        except Exception as e:
            logging.warning(f"Failed to warmup: {e}")

    @classmethod
    async def _lease_cache_read(cls) -> Optional[bytes]:
        def get_file():
            try:
                with filelock.FileLock(cls.LEASE_CACHE_PATH + '.lock'):
                    if not os.path.exists(cls.LEASE_CACHE_PATH):
                        return None
                    with open(cls.LEASE_CACHE_PATH, 'rb') as fp:
                        return fp.read()
            except IOError:
                return None

        async with cls.LEASE_LOCK:
            if cls.LEASE_DATA is None:
                cls.LEASE_DATA = await asyncio.to_thread(get_file)
            return cls.LEASE_DATA

    @classmethod
    async def _lease_cache_write(cls, data: bytes):
        def write_file():
            try:
                with filelock.FileLock(cls.LEASE_CACHE_PATH + '.lock'):
                    with open(cls.LEASE_CACHE_PATH, 'wb') as fp:
                        fp.write(data)
            except IOError:
                return

        async with cls.LEASE_LOCK:
            cls.LEASE_DATA = data
            await asyncio.to_thread(write_file)

    async def _lease_loop(self):
        refresh_time = timedelta(minutes=4, seconds=30)
        while not self._stop_lease_loop.is_set():
            await self.refresh_lease()
            await asyncio.sleep(refresh_time.total_seconds())

    async def refresh_lease(self):
        """Manually refresh credentials with Play."""
        async with self._lock:
            if self._lease and self._lease.expires > datetime.now() + timedelta(minutes=5):
                # Lease is still valid for at least the next 5 minutes.
                return
            self._lease = await self._lease_factory()

            grpc_addr = self._advanced.grpc_addr or self._lease.metadata["inference_address"]

            if self._rpc and self._rpc[0] != grpc_addr:
                await self._rpc[1].close()
                self._rpc = None
            if self._rpc is None:
                insecure = self._advanced.insecure or "on-prem.play.ht" in grpc_addr
                channel = (
                    insecure_channel(grpc_addr, options=CLIENT_RETRY_OPTIONS) if insecure
                    else secure_channel(grpc_addr, ssl_channel_credentials(), options=CLIENT_RETRY_OPTIONS)
                )
                self._rpc = (grpc_addr, channel)

            # Maybe set up a fallback grpc client
            if self._advanced.fallback_enabled:
                # Choose the fallback address
                # For now, this always is the inference address in the lease, but we can extend in the future
                fallback_addr = self._lease.metadata["inference_address"]

                # Only do fallback if the fallback address is not the same as the primary address
                if grpc_addr != fallback_addr:
                    if self._fallback_rpc and self._fallback_rpc[0] != fallback_addr:
                        await self._fallback_rpc[1].close()
                        self._fallback_rpc = None
                    if self._fallback_rpc is None:
                        channel = (
                            insecure_channel(fallback_addr, options=CLIENT_RETRY_OPTIONS) if self._advanced.insecure
                            else secure_channel(fallback_addr, ssl_channel_credentials(), options=CLIENT_RETRY_OPTIONS)
                        )
                        self._fallback_rpc = (fallback_addr, channel)

    async def stream_tts_input(
        self,
        text_stream: Union[AsyncGenerator[str, None], AsyncIterable[str]],
        options: TTSOptions,
        voice_engine: Optional[str] = None,
        protocol: Optional[str] = None,
        streaming: bool = True
    ):
        """Stream input to Play via the text_stream object."""
        buffer = io.StringIO()
        async for text in text_stream:
            t = text.strip()
            buffer.write(t)
            buffer.write(" ")  # normalize word spacing.
            if SENTENCE_END_REGEX.match(t) is None:
                continue
            async for data in self.tts(buffer.getvalue(), options, voice_engine, protocol, streaming):
                yield data
            buffer = io.StringIO()
        # If text_stream closes, send all remaining text, regardless of sentence structure.
        if buffer.tell() > 0:
            async for data in self.tts(buffer.getvalue(), options, voice_engine, protocol, streaming):
                yield data

    def tts(
        self,
        text: Union[str, list[str]],
        options: TTSOptions,
        voice_engine: Optional[str] = None,
        protocol: Optional[str] = None,
        streaming: bool = True
    ) -> AsyncIterable[bytes]:
        metrics = self._telemetry.start("tts-request")
        try:
            voice_engine, protocol = get_voice_engine_and_protocol(voice_engine, protocol)

            if voice_engine == "PlayDialog-turbo":
                if not streaming:
                    raise ValueError("Non-streaming is not supported for PlayDialog-turbo")
                return self._tts_turbo_http(text, options, voice_engine, metrics)
            elif protocol == "http":
                return self._tts_http(text, options, voice_engine, metrics, streaming)
            elif protocol == "ws":
                if not streaming:
                    raise ValueError("Non-streaming is not supported for WebSocket API")
                return self._tts_ws(text, options, voice_engine, metrics)
            elif protocol == "grpc":
                if not streaming:
                    raise ValueError("Non-streaming is not supported for gRPC API")
                return self._tts_grpc(text, options, voice_engine, metrics)
            else:
                raise ValueError(f"Unknown protocol {protocol}")
        except Exception as e:
            metrics.finish_error(str(e))
            raise e

    async def _tts_grpc(
        self,
        text: Union[str, list[str]],
        options: TTSOptions,
        voice_engine: Optional[str],
        metrics: Metrics,
        context: Optional[AsyncContext] = None
    ) -> AsyncIterable[bytes]:

        supported_voice_engines = ["Play3.0-mini", "PlayHT2.0-turbo"]
        if voice_engine not in supported_voice_engines:
            raise ValueError(f"Only {supported_voice_engines} are supported in the gRPC API; got {voice_engine}")

        start = time.perf_counter()
        await self.refresh_lease()
        async with self._lock:
            assert self._lease is not None and self._rpc is not None, "No connection"
            lease_data = self._lease.data

        text = prepare_text(text, self._advanced.remove_ssml_tags)
        metrics.append("text", str(text)).append("endpoint", str(self._rpc[0]))

        if options.format == Format.FORMAT_PCM:
            raise ValueError("PCM format is not supported in the gRPC API")
        request = api_pb2.TtsRequest(params=options.tts_params(text, voice_engine), lease=lease_data)

        for attempt in range(1, self._max_attempts + 1):
            try:
                stub = api_pb2_grpc.TtsStub(self._rpc[1])
                stream: TtsUnaryStream = stub.Tts(request)
                chunk_idx = -1
                if context is not None:
                    context.assign(stream)
                async for chunk in stream:
                    chunk_idx += 1
                    if chunk_idx == _audio_begins_at(options.format):
                        metrics.set_timer("time-to-first-audio", time.perf_counter() - start)
                    yield chunk.data
                metrics.finish_ok()
                break
            except grpc.RpcError as e:
                error_code = getattr(e, "code")()
                logging.debug(f"Error: {error_code}")
                if error_code not in {StatusCode.RESOURCE_EXHAUSTED, StatusCode.UNAVAILABLE}:
                    raise

                if attempt < self._max_attempts:
                    logging.debug(f"Retrying in {self._backoff*1000} sec ({attempt} attempts so far); ({error_code})")
                    metrics.inc("retry").append("retry.reason", str(error_code))
                    metrics.start_timer("retry-backoff")
                    if self._backoff > 0:
                        await asyncio.sleep(self._backoff)
                    metrics.finish_timer("retry-backoff")
                    continue

                if self._fallback_rpc is None:
                    raise

                # We log fallbacks to give customers an extra signal that they should scale up their on-prem appliance
                # (e.g. by paying for more GPU quota)
                logging.info(f"Falling back to {self._fallback_rpc[0]} because {self._rpc[0]} threw: {error_code}")
                metrics.inc("fallback").append("fallback.reason", str(error_code))
                try:
                    metrics.append("text", str(request.params.text)).append("endpoint", str(self._fallback_rpc[0]))
                    metrics.start_timer("time-to-first-audio")
                    stub = api_pb2_grpc.TtsStub(self._fallback_rpc[1])
                    stream: TtsUnaryStream = stub.Tts(request)
                    chunk_idx = -1
                    if context is not None:
                        context.assign(stream)
                    async for chunk in stream:
                        chunk_idx += 1
                        if chunk_idx == _audio_begins_at(options.format):
                            metrics.set_timer("time-to-first-audio", time.perf_counter() - start)
                        yield chunk.data
                    metrics.finish_ok()
                    break
                except grpc.RpcError as fallback_e:
                    metrics.finish_error(str(fallback_e))
                    raise fallback_e from e

    async def _tts_http(
        self,
        text: Union[str, list[str]],
        options: TTSOptions,
        voice_engine: Optional[str],
        metrics: Metrics,
        streaming: bool = True,
        context: Optional[AsyncContext] = None
    ) -> AsyncIterable[bytes]:
        supported_voice_engines = ["Play3.0-mini", "PlayDialog", "PlayDialogMultilingual", "PlayDialogArabic"]
        if voice_engine not in supported_voice_engines:
            raise ValueError(f"Only {supported_voice_engines} are supported in the HTTP API; got {voice_engine}")

        start = time.perf_counter()
        await self.ensure_inference_coordinates()
        assert self._inference_coordinates is not None, "No connection"

        if streaming:
            url = self._inference_coordinates[voice_engine]["http_streaming_url"]
        else:
            url = self._inference_coordinates[voice_engine]["http_nonstreaming_url"]

        text = prepare_text(text, self._advanced.remove_ssml_tags)
        metrics.append("text", str(text)).append("endpoint", str(url))

        for attempt in range(1, self._max_attempts + 1):
            try:
                async with aiohttp.ClientSession() as session:
                    assert self._inference_coordinates is not None, "No connection"
                    async with session.post(
                            url,
                            headers={
                                "accept": output_format_to_mime_type(options.format),
                            },
                            json=http_prepare_dict(text, options, voice_engine),
                            chunked=True
                    ) as response:
                        if response.status != 200:
                            raise Exception(f"HTTP {response.status}: {await response.text()}", response.status)
                        chunk_idx = -1
                        async for chunk in response.content.iter_any():
                            chunk_idx += 1
                            if chunk_idx == _audio_begins_at(options.format):
                                metrics.set_timer("time-to-first-audio", time.perf_counter() - start)
                            yield chunk
                        metrics.finish_ok()
                        break
            except Exception as e:
                logging.debug(f"Error: {e}")
                if e.args[1] == "401":
                    await self.ensure_inference_coordinates()
                elif e.args[1] not in {429, 503}:  # HTTP equivalent to gRPC RESOURCE_EXHAUSTED, UNAVAILABLE
                    metrics.finish_error(str(e))
                    raise

                if attempt < self._max_attempts:
                    # It's poor customer experience to show internal details about retries, so we only debug log here.
                    logging.debug(f"Retrying in {self._backoff*1000} sec ({attempt} attempts so far); ({e.args[1]})")
                    metrics.inc("retry").append("retry.reason", str(e.args[1]))
                    metrics.start_timer("retry-backoff")
                    if self._backoff > 0:
                        await asyncio.sleep(self._backoff)
                    metrics.finish_timer("retry-backoff")
                    continue

                metrics.finish_error(str(e))
                raise

    async def _tts_ws(
        self,
        text: Union[str, list[str]],
        options: TTSOptions,
        voice_engine: Optional[str],
        metrics: Metrics,
        context: Optional[AsyncContext] = None
    ) -> AsyncIterable[bytes]:
        supported_voice_engines = ["Play3.0-mini", "PlayDialog", "PlayDialogMultilingual", "PlayDialogArabic"]
        if voice_engine not in supported_voice_engines:
            raise ValueError(f"Only {supported_voice_engines} are supported in the WebSocket API; got {voice_engine}")

        start = time.perf_counter()
        await self.ensure_inference_coordinates()

        text = prepare_text(text, self._advanced.remove_ssml_tags)
        assert self._inference_coordinates is not None, "No connection"
        metrics.append("text", str(text)).append("endpoint",
                                                 str(self._inference_coordinates[voice_engine]["websocket_url"]))
        json_data = http_prepare_dict(text, options, voice_engine)

        for attempt in range(1, self._max_attempts + 1):
            try:
                assert self._inference_coordinates is not None, "No connection"
                ws_address = self._inference_coordinates[voice_engine]["websocket_url"]
                if self._ws is None:
                    self._ws = await connect(ws_address)
                    self._ws_requests_sent = 0
                    self._ws_responses_received = 0
                try:
                    await self._ws.send(json.dumps(json_data))
                    self._ws_requests_sent += 1
                except ConnectionClosed as e:
                    logging.debug(f"Reconnecting websocket which closed unexpectedly: {e}")
                    self._ws = await connect(ws_address)
                    await self._ws.send(json.dumps(json_data))
                    self._ws_requests_sent = 1
                    self._ws_responses_received = 0
                chunk_idx = -1
                request_id = -1
                started = False
                async for chunk in self._ws:
                    if isinstance(chunk, str):
                        msg = json.loads(chunk)
                        if msg["type"] == "start":
                            self._ws_responses_received += 1
                            if self._ws_responses_received == self._ws_requests_sent:
                                started = True
                                request_id = msg["request_id"]
                            elif self._ws_responses_received > self._ws_requests_sent:
                                raise Exception("Received more responses than requests")
                        elif msg["type"] == "end" and msg["request_id"] == request_id:
                            break
                        else:
                            continue
                    elif started:
                        chunk_idx += 1
                        if chunk_idx == _audio_begins_at(options.format):
                            metrics.set_timer("time-to-first-audio", time.perf_counter() - start)
                        yield chunk
                metrics.finish_ok()
                break
            except Exception as e:
                logging.debug(f"Error: {e}")
                if attempt < self._max_attempts:
                    # It's poor customer experience to show internal details about retries, so we only debug log here.
                    logging.debug(f"Retrying in {self._backoff*1000} ms ({attempt} attempts so far); ({e.args[1]})")
                    metrics.inc("retry").append("retry.reason", str(e.args[1]))
                    metrics.start_timer("retry-backoff")
                    if self._backoff > 0:
                        await asyncio.sleep(self._backoff)
                    metrics.finish_timer("retry-backoff")
                    # In case it was an expired token, refresh it
                    await self.ensure_inference_coordinates(force=True)
                    continue

                metrics.finish_error(str(e))
                raise

    async def _tts_turbo_http(
        self,
        text: Union[str, list[str]],
        options: TTSOptions,
        voice_engine: Optional[str],
        metrics: Metrics,
        context: Optional[AsyncContext] = None
    ) -> AsyncIterable[bytes]:
        supported_voice_engines = ["PlayDialog-turbo"]
        if voice_engine not in supported_voice_engines:
            raise ValueError(f"Only {supported_voice_engines} are supported in the Turbo HTTP API; got {voice_engine}")

        if type(text) == list and len(text) > 1:
            raise ValueError("PlayDialog-turbo only supports single-line text")

        start = time.perf_counter()

        url = "https://api.play.ht/api/v2/tts/stream"

        text = prepare_text(text, self._advanced.remove_ssml_tags)
        text = text[0]
        metrics.append("text", str(text)).append("endpoint", str(url))

        for attempt in range(1, self._max_attempts + 1):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(
                            url,
                            headers={
                                "x-user-id": self._user_id,
                                "authorization": f"Bearer {self._api_key}",
                                "accept": output_format_to_mime_type(options.format),
                            },
                            json=http_prepare_dict(text, options, voice_engine),
                            chunked=True
                    ) as response:
                        if response.status != 200:
                            raise Exception(f"HTTP {response.status}: {await response.text()}", response.status)
                        chunk_idx = -1
                        async for chunk in response.content.iter_any():
                            chunk_idx += 1
                            if chunk_idx == _audio_begins_at(options.format):
                                metrics.set_timer("time-to-first-audio", time.perf_counter() - start)
                            yield chunk
                        metrics.finish_ok()
                        break
            except Exception as e:
                logging.debug(f"Error: {e}")
                if e.args[1] not in {429, 503}:  # HTTP equivalent to gRPC RESOURCE_EXHAUSTED, UNAVAILABLE
                    metrics.finish_error(str(e))
                    raise

                if attempt < self._max_attempts:
                    # It's poor customer experience to show internal details about retries, so we only debug log here.
                    logging.debug(f"Retrying in {self._backoff*1000} sec ({attempt} attempts so far); ({e.args[1]})")
                    metrics.inc("retry").append("retry.reason", str(e.args[1]))
                    metrics.start_timer("retry-backoff")
                    if self._backoff > 0:
                        await asyncio.sleep(self._backoff)
                    metrics.finish_timer("retry-backoff")
                    continue

                metrics.finish_error(str(e))
                raise

    def get_stream_pair(
        self,
        options: TTSOptions,
        voice_engine: Optional[str] = None,
        protocol: Optional[str] = None
    ) -> tuple['_InputStream', '_OutputStream']:
        """Get a linked pair of (input, output) streams.

        These stream objects ARE NOT thread-safe. Coroutines using these stream objects must
        run on the same thread.
        """
        shared_q = asyncio.Queue()
        return (
            _InputStream(self, options, shared_q, voice_engine, protocol),
            _OutputStream(shared_q)
        )

    async def close(self):
        self._stop_lease_loop.set()
        if not self._lease_loop_future.done():
            self._lease_loop_future.cancel()
        if self._rpc is not None:
            await self._rpc[1].close()
            self._rpc = None
        if self._fallback_rpc is not None:
            await self._fallback_rpc[1].close()
            self._fallback_rpc = None

    def __del__(self):
        try:
            asyncio.get_running_loop()
            asyncio.ensure_future(self.close())
        except RuntimeError:
            asyncio.run(self.close())

    def metrics(self) -> list[Metrics]:
        return self._telemetry.metrics()


class UnaryStreamRendezvous(AsyncIterator[api_pb2.TtsResponse], Call):
    pass


class AsyncContext:
    def __init__(self):
        self._stream: asyncio.Future[TtsUnaryStream] = asyncio.Future()

    def assign(self, stream: TtsUnaryStream):
        self._stream.set_result(stream)

    def cancel(self):
        self._stream.add_done_callback(lambda s: s.result().cancel())
        if not self._stream.cancel():
            self._stream.result().cancel()

    def cancelled(self) -> bool:
        if self._stream.done():
            return self._stream.result().cancelled()
        return False

    def done(self) -> bool:
        if self._stream.done():
            return self._stream.result().done()
        return False


class TextStream(AsyncIterator[str]):
    def __init__(self, q: Optional[asyncio.Queue[Optional[str]]] = None):
        super().__init__()
        self._q = q or asyncio.Queue()
        self._futures = []

    def __aiter__(self) -> AsyncIterator[str]:
        return self

    async def __anext__(self) -> str:
        value = await self._q.get()
        if value is None:
            raise StopAsyncIteration()
        return value

    async def __call__(self, *args: str):
        await asyncio.gather(*(self._q.put(a) for a in args))

    async def close(self):
        await self._q.put(None)


class _InputStream:
    """Input stream handler for text.

    usage:
       input_stream('send', 'multiple', 'words', 'in', 'one', 'call.')
       input_stream += 'Add another sentence to the stream.'
       input_stream.done()
    """
    def __init__(
        self,
        client: AsyncClient,
        options: TTSOptions,
        q: asyncio.Queue[Optional[bytes]],
        voice_engine: Optional[str],
        protocol: Optional[str] = None
    ):
        self._input = TextStream()

        async def listen():
            async for output in client.stream_tts_input(self._input, options, voice_engine, protocol):
                await q.put(output)
            await q.put(None)

        self._listener = asyncio.ensure_future(listen())

    def __call__(self, *args: str) -> Coroutine[Any, Any, None]:
        return self._input(*args)

    def __iadd__(self, input: str) -> Coroutine[Any, Any, None]:
        return self._input(input)

    async def done(self):
        await self._input.close()
        await asyncio.wait_for(self._listener, 10)


class _OutputStream(AsyncIterator[bytes]):
    """Iterator for output audio.

    usage:
       for audio in output_stream:
           <do stuff with audio bytes>
        output_stream.close()
    """
    def __init__(self, q: asyncio.Queue[Optional[bytes]]):
        self._close = asyncio.Event()
        self._q = q

    def __aiter__(self) -> AsyncIterator[bytes]:
        return self

    async def __anext__(self) -> bytes:
        while True:
            try:
                value = await asyncio.wait_for(self._q.get(), timeout=0.05)
                break
            except asyncio.TimeoutError as e:
                if self._close.is_set():
                    raise StopAsyncIteration() from e
                continue
        if value is None:
            raise StopAsyncIteration()
        else:
            return value

    def close(self):
        self._close.set()
