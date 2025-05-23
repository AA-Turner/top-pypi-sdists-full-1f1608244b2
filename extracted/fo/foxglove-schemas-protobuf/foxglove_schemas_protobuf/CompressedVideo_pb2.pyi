"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Generated by https://github.com/foxglove/schemas"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class CompressedVideo(google.protobuf.message.Message):
    """A single frame of a compressed video bitstream"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIMESTAMP_FIELD_NUMBER: builtins.int
    FRAME_ID_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    FORMAT_FIELD_NUMBER: builtins.int
    frame_id: builtins.str
    """Frame of reference for the video.

    The origin of the frame is the optical center of the camera. +x points to the right in the video, +y points down, and +z points into the plane of the video.
    """
    data: builtins.bytes
    """Compressed video frame data.

    For packet-based video codecs this data must begin and end on packet boundaries (no partial packets), and must contain enough video packets to decode exactly one image (either a keyframe or delta frame). Note: Foxglove does not support video streams that include B frames because they require lookahead.

    Specifically, the requirements for different `format` values are:

    - `h264`
      - Use Annex B formatted data
      - Each CompressedVideo message should contain enough NAL units to decode exactly one video frame
      - Each message containing a key frame (IDR) must also include a SPS NAL unit

    - `h265` (HEVC)
      - Use Annex B formatted data
      - Each CompressedVideo message should contain enough NAL units to decode exactly one video frame
      - Each message containing a key frame (IRAP) must also include relevant VPS/SPS/PPS NAL units

    - `vp9`
      - Each CompressedVideo message should contain exactly one video frame

    - `av1`
      - Use the "Low overhead bitstream format" (section 5.2)
      - Each CompressedVideo message should contain enough OBUs to decode exactly one video frame
      - Each message containing a key frame must also include a Sequence Header OBU
    """
    format: builtins.str
    """Video format.

    Supported values: `h264`, `h265`, `vp9`, `av1`.

    Note: compressed video support is subject to hardware limitations and patent licensing, so not all encodings may be supported on all platforms. See more about [H.265 support](https://caniuse.com/hevc), [VP9 support](https://caniuse.com/webm), and [AV1 support](https://caniuse.com/av1).
    """
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Timestamp of video frame"""

    def __init__(
        self,
        *,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        frame_id: builtins.str = ...,
        data: builtins.bytes = ...,
        format: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["data", b"data", "format", b"format", "frame_id", b"frame_id", "timestamp", b"timestamp"]) -> None: ...

global___CompressedVideo = CompressedVideo
