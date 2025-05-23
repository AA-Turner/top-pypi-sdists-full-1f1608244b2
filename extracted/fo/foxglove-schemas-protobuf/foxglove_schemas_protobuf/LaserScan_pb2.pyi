"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Generated by https://github.com/foxglove/schemas"""

import builtins
import collections.abc
from . import Pose_pb2 as foxglove_Pose_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class LaserScan(google.protobuf.message.Message):
    """A single scan from a planar laser range-finder"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIMESTAMP_FIELD_NUMBER: builtins.int
    FRAME_ID_FIELD_NUMBER: builtins.int
    POSE_FIELD_NUMBER: builtins.int
    START_ANGLE_FIELD_NUMBER: builtins.int
    END_ANGLE_FIELD_NUMBER: builtins.int
    RANGES_FIELD_NUMBER: builtins.int
    INTENSITIES_FIELD_NUMBER: builtins.int
    frame_id: builtins.str
    """Frame of reference"""
    start_angle: builtins.float
    """Bearing of first point, in radians"""
    end_angle: builtins.float
    """Bearing of last point, in radians"""
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Timestamp of scan"""

    @property
    def pose(self) -> foxglove_Pose_pb2.Pose:
        """Origin of scan relative to frame of reference; points are positioned in the x-y plane relative to this origin; angles are interpreted as counterclockwise rotations around the z axis with 0 rad being in the +x direction"""

    @property
    def ranges(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Distance of detections from origin; assumed to be at equally-spaced angles between `start_angle` and `end_angle`"""

    @property
    def intensities(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Intensity of detections"""

    def __init__(
        self,
        *,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        frame_id: builtins.str = ...,
        pose: foxglove_Pose_pb2.Pose | None = ...,
        start_angle: builtins.float = ...,
        end_angle: builtins.float = ...,
        ranges: collections.abc.Iterable[builtins.float] | None = ...,
        intensities: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["pose", b"pose", "timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["end_angle", b"end_angle", "frame_id", b"frame_id", "intensities", b"intensities", "pose", b"pose", "ranges", b"ranges", "start_angle", b"start_angle", "timestamp", b"timestamp"]) -> None: ...

global___LaserScan = LaserScan
