# Generated by https://github.com/foxglove/foxglove-sdk
from enum import Enum
from typing import List, Optional, Union

from . import Schema
from .schemas_wkt import Duration as Duration
from .schemas_wkt import Timestamp as Timestamp

#
# Enums
#

class LinePrimitiveLineType(Enum):
    """
    An enumeration indicating how input points should be interpreted to create lines
    """

    LineStrip = 0
    LineLoop = 1
    LineList = 2

class LocationFixPositionCovarianceType(Enum):
    """
    Type of position covariance
    """

    Unknown = 0
    Approximated = 1
    DiagonalKnown = 2
    Known = 3

class LogLevel(Enum):
    """
    Log level
    """

    Unknown = 0
    Debug = 1
    Info = 2
    Warning = 3
    Error = 4
    Fatal = 5

class PackedElementFieldNumericType(Enum):
    """
    Numeric type
    """

    Unknown = 0
    Uint8 = 1
    Int8 = 2
    Uint16 = 3
    Int16 = 4
    Uint32 = 5
    Int32 = 6
    Float32 = 7
    Float64 = 8

class PointsAnnotationType(Enum):
    """
    Type of points annotation
    """

    Unknown = 0
    Points = 1
    LineLoop = 2
    LineStrip = 3
    LineList = 4

class SceneEntityDeletionType(Enum):
    """
    An enumeration indicating which entities should match a SceneEntityDeletion command
    """

    MatchingId = 0
    All = 1

#
# Classes
#

class ArrowPrimitive:
    """
    A primitive representing an arrow
    """

    def __new__(
        cls,
        *,
        pose: "Optional[Pose]" = None,
        shaft_length: "Optional[float]" = 0.0,
        shaft_diameter: "Optional[float]" = 0.0,
        head_length: "Optional[float]" = 0.0,
        head_diameter: "Optional[float]" = 0.0,
        color: "Optional[Color]" = None,
    ) -> "ArrowPrimitive": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the ArrowPrimitive schema"""
        ...

class CameraCalibration:
    """
    Camera calibration parameters
    """

    def __new__(
        cls,
        *,
        timestamp: "Optional[Timestamp]" = None,
        frame_id: "Optional[str]" = "",
        width: "Optional[int]" = 0,
        height: "Optional[int]" = 0,
        distortion_model: "Optional[str]" = "",
        D: "Optional[List[float]]" = [],
        K: "Optional[List[float]]" = [],
        R: "Optional[List[float]]" = [],
        P: "Optional[List[float]]" = [],
    ) -> "CameraCalibration": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the CameraCalibration schema"""
        ...

class CircleAnnotation:
    """
    A circle annotation on a 2D image
    """

    def __new__(
        cls,
        *,
        timestamp: "Optional[Timestamp]" = None,
        position: "Optional[Point2]" = None,
        diameter: "Optional[float]" = 0.0,
        thickness: "Optional[float]" = 0.0,
        fill_color: "Optional[Color]" = None,
        outline_color: "Optional[Color]" = None,
    ) -> "CircleAnnotation": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the CircleAnnotation schema"""
        ...

class Color:
    """
    A color in RGBA format
    """

    def __new__(
        cls,
        *,
        r: "Optional[float]" = 0.0,
        g: "Optional[float]" = 0.0,
        b: "Optional[float]" = 0.0,
        a: "Optional[float]" = 0.0,
    ) -> "Color": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the Color schema"""
        ...

class CompressedImage:
    """
    A compressed image
    """

    def __new__(
        cls,
        *,
        timestamp: "Optional[Timestamp]" = None,
        frame_id: "Optional[str]" = "",
        data: "Optional[bytes]" = b"",
        format: "Optional[str]" = "",
    ) -> "CompressedImage": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the CompressedImage schema"""
        ...

class CompressedVideo:
    """
    A single frame of a compressed video bitstream
    """

    def __new__(
        cls,
        *,
        timestamp: "Optional[Timestamp]" = None,
        frame_id: "Optional[str]" = "",
        data: "Optional[bytes]" = b"",
        format: "Optional[str]" = "",
    ) -> "CompressedVideo": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the CompressedVideo schema"""
        ...

class CubePrimitive:
    """
    A primitive representing a cube or rectangular prism
    """

    def __new__(
        cls,
        *,
        pose: "Optional[Pose]" = None,
        size: "Optional[Vector3]" = None,
        color: "Optional[Color]" = None,
    ) -> "CubePrimitive": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the CubePrimitive schema"""
        ...

class CylinderPrimitive:
    """
    A primitive representing a cylinder, elliptic cylinder, or truncated cone
    """

    def __new__(
        cls,
        *,
        pose: "Optional[Pose]" = None,
        size: "Optional[Vector3]" = None,
        bottom_scale: "Optional[float]" = 0.0,
        top_scale: "Optional[float]" = 0.0,
        color: "Optional[Color]" = None,
    ) -> "CylinderPrimitive": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the CylinderPrimitive schema"""
        ...

class FrameTransform:
    """
    A transform between two reference frames in 3D space
    """

    def __new__(
        cls,
        *,
        timestamp: "Optional[Timestamp]" = None,
        parent_frame_id: "Optional[str]" = "",
        child_frame_id: "Optional[str]" = "",
        translation: "Optional[Vector3]" = None,
        rotation: "Optional[Quaternion]" = None,
    ) -> "FrameTransform": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the FrameTransform schema"""
        ...

class FrameTransforms:
    """
    An array of FrameTransform messages
    """

    def __new__(
        cls, *, transforms: "Optional[List[FrameTransform]]" = []
    ) -> "FrameTransforms": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the FrameTransforms schema"""
        ...

class GeoJson:
    """
    GeoJSON data for annotating maps
    """

    def __new__(cls, *, geojson: "Optional[str]" = "") -> "GeoJson": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the GeoJson schema"""
        ...

class Grid:
    """
    A 2D grid of data
    """

    def __new__(
        cls,
        *,
        timestamp: "Optional[Timestamp]" = None,
        frame_id: "Optional[str]" = "",
        pose: "Optional[Pose]" = None,
        column_count: "Optional[int]" = 0,
        cell_size: "Optional[Vector2]" = None,
        row_stride: "Optional[int]" = 0,
        cell_stride: "Optional[int]" = 0,
        fields: "Optional[List[PackedElementField]]" = [],
        data: "Optional[bytes]" = b"",
    ) -> "Grid": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the Grid schema"""
        ...

class ImageAnnotations:
    """
    Array of annotations for a 2D image
    """

    def __new__(
        cls,
        *,
        circles: "Optional[List[CircleAnnotation]]" = [],
        points: "Optional[List[PointsAnnotation]]" = [],
        texts: "Optional[List[TextAnnotation]]" = [],
    ) -> "ImageAnnotations": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the ImageAnnotations schema"""
        ...

class KeyValuePair:
    """
    A key with its associated value
    """

    def __new__(
        cls, *, key: "Optional[str]" = "", value: "Optional[str]" = ""
    ) -> "KeyValuePair": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the KeyValuePair schema"""
        ...

class LaserScan:
    """
    A single scan from a planar laser range-finder
    """

    def __new__(
        cls,
        *,
        timestamp: "Optional[Timestamp]" = None,
        frame_id: "Optional[str]" = "",
        pose: "Optional[Pose]" = None,
        start_angle: "Optional[float]" = 0.0,
        end_angle: "Optional[float]" = 0.0,
        ranges: "Optional[List[float]]" = [],
        intensities: "Optional[List[float]]" = [],
    ) -> "LaserScan": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the LaserScan schema"""
        ...

class LinePrimitive:
    """
    A primitive representing a series of points connected by lines
    """

    def __new__(
        cls,
        *,
        type: "Optional[LinePrimitiveLineType]" = LinePrimitiveLineType.LineStrip,
        pose: "Optional[Pose]" = None,
        thickness: "Optional[float]" = 0.0,
        scale_invariant: "Optional[bool]" = False,
        points: "Optional[List[Point3]]" = [],
        color: "Optional[Color]" = None,
        colors: "Optional[List[Color]]" = [],
        indices: "Optional[List[int]]" = [],
    ) -> "LinePrimitive": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the LinePrimitive schema"""
        ...

class LocationFix:
    """
    A navigation satellite fix for any Global Navigation Satellite System
    """

    def __new__(
        cls,
        *,
        timestamp: "Optional[Timestamp]" = None,
        frame_id: "Optional[str]" = "",
        latitude: "Optional[float]" = 0.0,
        longitude: "Optional[float]" = 0.0,
        altitude: "Optional[float]" = 0.0,
        position_covariance: "Optional[List[float]]" = [],
        position_covariance_type: "Optional[LocationFixPositionCovarianceType]" = LocationFixPositionCovarianceType.Unknown,
    ) -> "LocationFix": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the LocationFix schema"""
        ...

class Log:
    """
    A log message
    """

    def __new__(
        cls,
        *,
        timestamp: "Optional[Timestamp]" = None,
        level: "Optional[LogLevel]" = LogLevel.Unknown,
        message: "Optional[str]" = "",
        name: "Optional[str]" = "",
        file: "Optional[str]" = "",
        line: "Optional[int]" = 0,
    ) -> "Log": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the Log schema"""
        ...

class ModelPrimitive:
    """
    A primitive representing a 3D model file loaded from an external URL or embedded data
    """

    def __new__(
        cls,
        *,
        pose: "Optional[Pose]" = None,
        scale: "Optional[Vector3]" = None,
        color: "Optional[Color]" = None,
        override_color: "Optional[bool]" = False,
        url: "Optional[str]" = "",
        media_type: "Optional[str]" = "",
        data: "Optional[bytes]" = b"",
    ) -> "ModelPrimitive": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the ModelPrimitive schema"""
        ...

class PackedElementField:
    """
    A field present within each element in a byte array of packed elements.
    """

    def __new__(
        cls,
        *,
        name: "Optional[str]" = "",
        offset: "Optional[int]" = 0,
        type: "Optional[PackedElementFieldNumericType]" = PackedElementFieldNumericType.Unknown,
    ) -> "PackedElementField": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the PackedElementField schema"""
        ...

class Point2:
    """
    A point representing a position in 2D space
    """

    def __new__(
        cls, *, x: "Optional[float]" = 0.0, y: "Optional[float]" = 0.0
    ) -> "Point2": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the Point2 schema"""
        ...

class Point3:
    """
    A point representing a position in 3D space
    """

    def __new__(
        cls,
        *,
        x: "Optional[float]" = 0.0,
        y: "Optional[float]" = 0.0,
        z: "Optional[float]" = 0.0,
    ) -> "Point3": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the Point3 schema"""
        ...

class PointCloud:
    """
    A collection of N-dimensional points, which may contain additional fields with information like normals, intensity, etc.
    """

    def __new__(
        cls,
        *,
        timestamp: "Optional[Timestamp]" = None,
        frame_id: "Optional[str]" = "",
        pose: "Optional[Pose]" = None,
        point_stride: "Optional[int]" = 0,
        fields: "Optional[List[PackedElementField]]" = [],
        data: "Optional[bytes]" = b"",
    ) -> "PointCloud": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the PointCloud schema"""
        ...

class PointsAnnotation:
    """
    An array of points on a 2D image
    """

    def __new__(
        cls,
        *,
        timestamp: "Optional[Timestamp]" = None,
        type: "Optional[PointsAnnotationType]" = PointsAnnotationType.Unknown,
        points: "Optional[List[Point2]]" = [],
        outline_color: "Optional[Color]" = None,
        outline_colors: "Optional[List[Color]]" = [],
        fill_color: "Optional[Color]" = None,
        thickness: "Optional[float]" = 0.0,
    ) -> "PointsAnnotation": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the PointsAnnotation schema"""
        ...

class Pose:
    """
    A position and orientation for an object or reference frame in 3D space
    """

    def __new__(
        cls,
        *,
        position: "Optional[Vector3]" = None,
        orientation: "Optional[Quaternion]" = None,
    ) -> "Pose": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the Pose schema"""
        ...

class PoseInFrame:
    """
    A timestamped pose for an object or reference frame in 3D space
    """

    def __new__(
        cls,
        *,
        timestamp: "Optional[Timestamp]" = None,
        frame_id: "Optional[str]" = "",
        pose: "Optional[Pose]" = None,
    ) -> "PoseInFrame": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the PoseInFrame schema"""
        ...

class PosesInFrame:
    """
    An array of timestamped poses for an object or reference frame in 3D space
    """

    def __new__(
        cls,
        *,
        timestamp: "Optional[Timestamp]" = None,
        frame_id: "Optional[str]" = "",
        poses: "Optional[List[Pose]]" = [],
    ) -> "PosesInFrame": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the PosesInFrame schema"""
        ...

class Quaternion:
    """
    A [quaternion](https://eater.net/quaternions) representing a rotation in 3D space
    """

    def __new__(
        cls,
        *,
        x: "Optional[float]" = 0.0,
        y: "Optional[float]" = 0.0,
        z: "Optional[float]" = 0.0,
        w: "Optional[float]" = 0.0,
    ) -> "Quaternion": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the Quaternion schema"""
        ...

class RawAudio:
    """
    A single block of an audio bitstream
    """

    def __new__(
        cls,
        *,
        timestamp: "Optional[Timestamp]" = None,
        data: "Optional[bytes]" = b"",
        format: "Optional[str]" = "",
        sample_rate: "Optional[int]" = 0,
        number_of_channels: "Optional[int]" = 0,
    ) -> "RawAudio": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the RawAudio schema"""
        ...

class RawImage:
    """
    A raw image
    """

    def __new__(
        cls,
        *,
        timestamp: "Optional[Timestamp]" = None,
        frame_id: "Optional[str]" = "",
        width: "Optional[int]" = 0,
        height: "Optional[int]" = 0,
        encoding: "Optional[str]" = "",
        step: "Optional[int]" = 0,
        data: "Optional[bytes]" = b"",
    ) -> "RawImage": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the RawImage schema"""
        ...

class SceneEntity:
    """
    A visual element in a 3D scene. An entity may be composed of multiple primitives which all share the same frame of reference.
    """

    def __new__(
        cls,
        *,
        timestamp: "Optional[Timestamp]" = None,
        frame_id: "Optional[str]" = "",
        id: "Optional[str]" = "",
        lifetime: "Optional[Duration]" = None,
        frame_locked: "Optional[bool]" = False,
        metadata: "Optional[List[KeyValuePair]]" = [],
        arrows: "Optional[List[ArrowPrimitive]]" = [],
        cubes: "Optional[List[CubePrimitive]]" = [],
        spheres: "Optional[List[SpherePrimitive]]" = [],
        cylinders: "Optional[List[CylinderPrimitive]]" = [],
        lines: "Optional[List[LinePrimitive]]" = [],
        triangles: "Optional[List[TriangleListPrimitive]]" = [],
        texts: "Optional[List[TextPrimitive]]" = [],
        models: "Optional[List[ModelPrimitive]]" = [],
    ) -> "SceneEntity": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the SceneEntity schema"""
        ...

class SceneEntityDeletion:
    """
    Command to remove previously published entities
    """

    def __new__(
        cls,
        *,
        timestamp: "Optional[Timestamp]" = None,
        type: "Optional[SceneEntityDeletionType]" = SceneEntityDeletionType.MatchingId,
        id: "Optional[str]" = "",
    ) -> "SceneEntityDeletion": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the SceneEntityDeletion schema"""
        ...

class SceneUpdate:
    """
    An update to the entities displayed in a 3D scene
    """

    def __new__(
        cls,
        *,
        deletions: "Optional[List[SceneEntityDeletion]]" = [],
        entities: "Optional[List[SceneEntity]]" = [],
    ) -> "SceneUpdate": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the SceneUpdate schema"""
        ...

class SpherePrimitive:
    """
    A primitive representing a sphere or ellipsoid
    """

    def __new__(
        cls,
        *,
        pose: "Optional[Pose]" = None,
        size: "Optional[Vector3]" = None,
        color: "Optional[Color]" = None,
    ) -> "SpherePrimitive": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the SpherePrimitive schema"""
        ...

class TextAnnotation:
    """
    A text label on a 2D image
    """

    def __new__(
        cls,
        *,
        timestamp: "Optional[Timestamp]" = None,
        position: "Optional[Point2]" = None,
        text: "Optional[str]" = "",
        font_size: "Optional[float]" = 0.0,
        text_color: "Optional[Color]" = None,
        background_color: "Optional[Color]" = None,
    ) -> "TextAnnotation": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the TextAnnotation schema"""
        ...

class TextPrimitive:
    """
    A primitive representing a text label
    """

    def __new__(
        cls,
        *,
        pose: "Optional[Pose]" = None,
        billboard: "Optional[bool]" = False,
        font_size: "Optional[float]" = 0.0,
        scale_invariant: "Optional[bool]" = False,
        color: "Optional[Color]" = None,
        text: "Optional[str]" = "",
    ) -> "TextPrimitive": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the TextPrimitive schema"""
        ...

class TriangleListPrimitive:
    """
    A primitive representing a set of triangles or a surface tiled by triangles
    """

    def __new__(
        cls,
        *,
        pose: "Optional[Pose]" = None,
        points: "Optional[List[Point3]]" = [],
        color: "Optional[Color]" = None,
        colors: "Optional[List[Color]]" = [],
        indices: "Optional[List[int]]" = [],
    ) -> "TriangleListPrimitive": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the TriangleListPrimitive schema"""
        ...

class Vector2:
    """
    A vector in 2D space that represents a direction only
    """

    def __new__(
        cls, *, x: "Optional[float]" = 0.0, y: "Optional[float]" = 0.0
    ) -> "Vector2": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the Vector2 schema"""
        ...

class Vector3:
    """
    A vector in 3D space that represents a direction only
    """

    def __new__(
        cls,
        *,
        x: "Optional[float]" = 0.0,
        y: "Optional[float]" = 0.0,
        z: "Optional[float]" = 0.0,
    ) -> "Vector3": ...
    @staticmethod
    def get_schema() -> Schema:
        """Returns the Vector3 schema"""
        ...

FoxgloveSchema = Union[
    ArrowPrimitive,
    CameraCalibration,
    CircleAnnotation,
    Color,
    CompressedImage,
    CompressedVideo,
    CylinderPrimitive,
    CubePrimitive,
    FrameTransform,
    FrameTransforms,
    GeoJson,
    Grid,
    ImageAnnotations,
    KeyValuePair,
    LaserScan,
    LinePrimitive,
    LocationFix,
    Log,
    SceneEntityDeletion,
    SceneEntity,
    SceneUpdate,
    ModelPrimitive,
    PackedElementField,
    Point2,
    Point3,
    PointCloud,
    PointsAnnotation,
    Pose,
    PoseInFrame,
    PosesInFrame,
    Quaternion,
    RawAudio,
    RawImage,
    SpherePrimitive,
    TextAnnotation,
    TextPrimitive,
    TriangleListPrimitive,
    Vector2,
    Vector3,
]
