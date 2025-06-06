import av
import av.audio
import av.container
import av.stream
from . import redact_credentials as redact_credentials
from .const import AUDIO_CODECS as AUDIO_CODECS, HLS_PROVIDER as HLS_PROVIDER, MAX_MISSING_DTS as MAX_MISSING_DTS, MAX_TIMESTAMP_GAP as MAX_TIMESTAMP_GAP, PACKETS_TO_WAIT_FOR_AUDIO as PACKETS_TO_WAIT_FOR_AUDIO, SEGMENT_CONTAINER_FORMAT as SEGMENT_CONTAINER_FORMAT, SOURCE_TIMEOUT as SOURCE_TIMEOUT, StreamClientError as StreamClientError
from .core import KeyFrameConverter as KeyFrameConverter, Part as Part, STREAM_SETTINGS_NON_LL_HLS as STREAM_SETTINGS_NON_LL_HLS, Segment as Segment, StreamOutput as StreamOutput, StreamSettings as StreamSettings
from .diagnostics import Diagnostics as Diagnostics
from .exceptions import StreamEndedError as StreamEndedError, StreamWorkerError as StreamWorkerError
from .fmp4utils import read_init as read_init
from .hls import HlsStreamOutput as HlsStreamOutput
from _typeshed import Incomplete
from av.container import InputContainer as InputContainer
from collections import deque
from collections.abc import Callable as Callable, Generator, Iterator, Mapping
from homeassistant.core import HomeAssistant as HomeAssistant
from io import BytesIO
from threading import Event
from typing import Any, Self

_LOGGER: Incomplete
NEGATIVE_INF: Incomplete

def redact_av_error_string(err: av.FFmpegError) -> str: ...

class StreamState:
    _stream_id: int
    hass: Incomplete
    _outputs_callback: Callable[[], Mapping[str, StreamOutput]]
    _sequence: int
    _diagnostics: Incomplete
    def __init__(self, hass: HomeAssistant, outputs_callback: Callable[[], Mapping[str, StreamOutput]], diagnostics: Diagnostics) -> None: ...
    @property
    def sequence(self) -> int: ...
    def next_sequence(self) -> int: ...
    @property
    def stream_id(self) -> int: ...
    def discontinuity(self) -> None: ...
    @property
    def outputs(self) -> list[StreamOutput]: ...
    @property
    def diagnostics(self) -> Diagnostics: ...

class StreamMuxer:
    _segment_start_dts: int
    _memory_file: BytesIO
    _av_output: av.container.OutputContainer
    _output_video_stream: av.VideoStream
    _output_audio_stream: av.audio.AudioStream | None
    _segment: Segment | None
    _memory_file_pos: int
    _part_start_dts: float
    _hass: Incomplete
    _input_video_stream: Incomplete
    _input_audio_stream: Incomplete
    _audio_bsf: Incomplete
    _audio_bsf_context: av.BitStreamFilterContext | None
    _part_has_keyframe: bool
    _stream_settings: Incomplete
    _stream_state: Incomplete
    _start_time: Incomplete
    def __init__(self, hass: HomeAssistant, video_stream: av.VideoStream, audio_stream: av.audio.AudioStream | None, audio_bsf: str | None, stream_state: StreamState, stream_settings: StreamSettings) -> None: ...
    def make_new_av(self, memory_file: BytesIO, sequence: int, input_vstream: av.VideoStream, input_astream: av.audio.AudioStream | None) -> tuple[av.container.OutputContainer, av.VideoStream, av.audio.AudioStream | None]: ...
    def reset(self, video_dts: int) -> None: ...
    def mux_packet(self, packet: av.Packet) -> None: ...
    def create_segment(self) -> None: ...
    def check_flush_part(self, packet: av.Packet) -> None: ...
    def flush(self, packet: av.Packet, last_part: bool) -> None: ...
    def close(self) -> None: ...

class PeekIterator(Iterator[av.Packet]):
    _iterator: Incomplete
    _buffer: deque[av.Packet]
    _next: Incomplete
    def __init__(self, iterator: Iterator[av.Packet]) -> None: ...
    def __iter__(self) -> Self: ...
    def __next__(self) -> av.Packet: ...
    def _pop_buffer(self) -> av.Packet: ...
    def peek(self) -> Generator[av.Packet]: ...

class TimestampValidator:
    _last_dts: dict[av.stream.Stream, int | float]
    _missing_dts: int
    _max_dts_gap: Incomplete
    def __init__(self, inv_video_time_base: int, inv_audio_time_base: int) -> None: ...
    def is_valid(self, packet: av.Packet) -> bool: ...

def is_keyframe(packet: av.Packet) -> Any: ...
def get_audio_bitstream_filter(packets: Iterator[av.Packet], audio_stream: Any) -> str | None: ...
def try_open_stream(source: str, pyav_options: dict[str, str]) -> InputContainer: ...
def stream_worker(source: str, pyav_options: dict[str, str], stream_settings: StreamSettings, stream_state: StreamState, keyframe_converter: KeyFrameConverter, quit_event: Event) -> None: ...
