import datetime as dt
import sys

from collections.abc import Callable
from decimal import Decimal

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self
from typing import (
    Any,
    Generic,
    Iterable,
    Iterator,
    Literal,
    TypeVar,
    overload,
)

import numpy as np
import pandas as pd

from pandas.core.dtypes.base import ExtensionDtype
from pyarrow._compute import CastOptions
from pyarrow._stubs_typing import (
    ArrayLike,
    Indices,
    Mask,
    Order,
    SupportArrowArray,
    SupportArrowDeviceArray,
)
from pyarrow.lib import (
    Buffer,
    Device,
    MemoryManager,
    MemoryPool,
    MonthDayNano,
    Tensor,
    _Weakrefable,
)

from . import scalar, types
from .device import DeviceAllocationType
from .scalar import NullableCollection, Scalar
from .types import (
    DataType,
    Field,
    MapType,
    _AsPyType,
    _BasicDataType,
    _BasicValueT,
    _DataTypeT,
    _IndexT,
    _RunEndType,
    _Size,
)

@overload
def array(
    values: NullableCollection[bool],
    type: None = None,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> BooleanArray: ...
@overload
def array(
    values: NullableCollection[int],
    type: None = None,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> Int64Array: ...
@overload
def array(
    values: NullableCollection[float],
    type: None = None,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> DoubleArray: ...
@overload
def array(
    values: NullableCollection[Decimal],
    type: None = None,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> Decimal128Array: ...
@overload
def array(
    values: NullableCollection[dict[str, Any]],
    type: None = None,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> StructArray: ...
@overload
def array(
    values: NullableCollection[dt.date],
    type: None = None,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> Date32Array: ...
@overload
def array(
    values: NullableCollection[dt.time],
    type: None = None,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> Time64Array[Literal["us"]]: ...
@overload
def array(
    values: NullableCollection[dt.timedelta],
    type: None = None,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> DurationArray[Literal["us"]]: ...
@overload
def array(
    values: NullableCollection[MonthDayNano],
    type: None = None,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> MonthDayNanoIntervalArray: ...
@overload
def array(
    values: NullableCollection[str],
    type: None = None,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> StringArray: ...
@overload
def array(
    values: NullableCollection[bytes],
    type: None = None,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> BinaryArray: ...
@overload
def array(
    values: NullableCollection[list[Any]],
    type: None = None,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> ListArray[Any]: ...
@overload
def array(
    values: NullableCollection[_ScalarT],
    type: None = None,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> Array[_ScalarT]: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["null"] | types.NullType,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> NullArray: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["bool", "boolean"] | types.BoolType,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> BooleanArray: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["i1", "int8"] | types.Int8Type,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> Int8Array: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["i2", "int16"] | types.Int16Type,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> Int16Array: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["i4", "int32"] | types.Int32Type,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> Int32Array: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["i8", "int64"] | types.Int64Type,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> Int64Array: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["u1", "uint8"] | types.UInt8Type,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> UInt8Array: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["u2", "uint16"] | types.UInt16Type,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> UInt16Array: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["u4", "uint32"] | types.Uint32Type,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> UInt32Array: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["u8", "uint64"] | types.UInt64Type,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> UInt64Array: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["f2", "halffloat", "float16"] | types.Float16Type,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> HalfFloatArray: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["f4", "float", "float32"] | types.Float32Type,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> FloatArray: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["f8", "double", "float64"] | types.Float64Type,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> DoubleArray: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["string", "str", "utf8"] | types.StringType,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> StringArray: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["binary"] | types.BinaryType,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> BinaryArray: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["large_string", "large_str", "large_utf8"] | types.LargeStringType,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> LargeStringArray: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["large_binary"] | types.LargeBinaryType,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> LargeBinaryArray: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["binary_view"] | types.BinaryViewType,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> BinaryViewArray: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["string_view"] | types.StringViewType,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> StringViewArray: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["date32", "date32[day]"] | types.Date32Type,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> Date32Array: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["date64", "date64[ms]"] | types.Date64Type,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> Date64Array: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["time32[s]"] | types.Time32Type[Literal["s"]],
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> Time32Array[Literal["s"]]: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["time32[ms]"] | types.Time32Type[Literal["ms"]],
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> Time32Array[Literal["ms"]]: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["time64[us]"] | types.Time64Type[Literal["us"]],
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> Time64Array[Literal["us"]]: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["time64[ns]"] | types.Time64Type[Literal["ns"]],
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> Time64Array[Literal["ns"]]: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["timestamp[s]"] | types.TimestampType[Literal["s"]],
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> TimestampArray[Literal["s"]]: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["timestamp[ms]"] | types.TimestampType[Literal["ms"]],
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> TimestampArray[Literal["ms"]]: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["timestamp[us]"] | types.TimestampType[Literal["us"]],
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> TimestampArray[Literal["us"]]: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["duration[s]"] | types.DurationType[Literal["s"]],
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> DurationArray[Literal["s"]]: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["duration[ms]"] | types.DurationType[Literal["ms"]],
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> DurationArray[Literal["ms"]]: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["duration[us]"] | types.DurationType[Literal["us"]],
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> DurationArray[Literal["us"]]: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["duration[ns]"] | types.DurationType[Literal["ns"]],
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> DurationArray[Literal["ns"]]: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["month_day_nano_interval"] | types.MonthDayNanoIntervalType,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> MonthDayNanoIntervalArray: ...
@overload
def array(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: _DataTypeT,
    mask: Mask | None = None,
    size: int | None = None,
    from_pandas: bool | None = None,
    safe: bool = True,
    memory_pool: MemoryPool | None = None,
) -> Array[Scalar[_DataTypeT]]: ...
@overload
def asarray(values: NullableCollection[bool]) -> BooleanArray: ...
@overload
def asarray(values: NullableCollection[int]) -> Int64Array: ...
@overload
def asarray(values: NullableCollection[float]) -> DoubleArray: ...
@overload
def asarray(values: NullableCollection[Decimal]) -> Decimal128Array: ...
@overload
def asarray(values: NullableCollection[dict[str, Any]]) -> StructArray: ...
@overload
def asarray(values: NullableCollection[dt.date]) -> Date32Array: ...
@overload
def asarray(values: NullableCollection[dt.time]) -> Time64Array: ...
@overload
def asarray(values: NullableCollection[dt.timedelta]) -> DurationArray: ...
@overload
def asarray(values: NullableCollection[MonthDayNano]) -> MonthDayNanoIntervalArray: ...
@overload
def asarray(values: NullableCollection[list[Any]]) -> ListArray[Any]: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["null"] | types.NullType,
) -> NullArray: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["bool", "boolean"] | types.BoolType,
) -> BooleanArray: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["i1", "int8"] | types.Int8Type,
) -> Int8Array: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["i2", "int16"] | types.Int16Type,
) -> Int16Array: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["i4", "int32"] | types.Int32Type,
) -> Int32Array: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["i8", "int64"] | types.Int64Type,
) -> Int64Array: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["u1", "uint8"] | types.UInt8Type,
) -> UInt8Array: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["u2", "uint16"] | types.UInt16Type,
) -> UInt16Array: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["u4", "uint32"] | types.Uint32Type,
) -> UInt32Array: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["u8", "uint64"] | types.UInt64Type,
) -> UInt64Array: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["f2", "halffloat", "float16"] | types.Float16Type,
) -> HalfFloatArray: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["f4", "float", "float32"] | types.Float32Type,
) -> FloatArray: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["f8", "double", "float64"] | types.Float64Type,
) -> DoubleArray: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["string", "str", "utf8"] | types.StringType,
) -> StringArray: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["binary"] | types.BinaryType,
) -> BinaryArray: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["large_string", "large_str", "large_utf8"] | types.LargeStringType,
) -> LargeStringArray: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["large_binary"] | types.LargeBinaryType,
) -> LargeBinaryArray: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["binary_view"] | types.BinaryViewType,
) -> BinaryViewArray: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["string_view"] | types.StringViewType,
) -> StringViewArray: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["date32", "date32[day]"] | types.Date32Type,
) -> Date32Array: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["date64", "date64[ms]"] | types.Date64Type,
) -> Date64Array: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["time32[s]"] | types.Time32Type[Literal["s"]],
) -> Time32Array[Literal["s"]]: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["time32[ms]"] | types.Time32Type[Literal["ms"]],
) -> Time32Array[Literal["ms"]]: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["time64[us]"] | types.Time64Type[Literal["us"]],
) -> Time64Array[Literal["us"]]: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["time64[ns]"] | types.Time64Type[Literal["ns"]],
) -> Time64Array[Literal["ns"]]: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["timestamp[s]"] | types.TimestampType[Literal["s"]],
) -> TimestampArray[Literal["s"]]: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["timestamp[ms]"] | types.TimestampType[Literal["ms"]],
) -> TimestampArray[Literal["ms"]]: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["timestamp[us]"] | types.TimestampType[Literal["us"]],
) -> TimestampArray[Literal["us"]]: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["timestamp[ns]"] | types.TimestampType[Literal["ns"]],
) -> TimestampArray[Literal["ns"]]: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["duration[s]"] | types.DurationType[Literal["s"]],
) -> DurationArray[Literal["s"]]: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["duration[ms]"] | types.DurationType[Literal["ms"]],
) -> DurationArray[Literal["ms"]]: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["duration[us]"] | types.DurationType[Literal["us"]],
) -> DurationArray[Literal["us"]]: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["duration[ns]"] | types.DurationType[Literal["ns"]],
) -> DurationArray[Literal["ns"]]: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: Literal["month_day_nano_interval"] | types.MonthDayNanoIntervalType,
) -> MonthDayNanoIntervalArray: ...
@overload
def asarray(
    values: Iterable[Any] | SupportArrowArray | SupportArrowDeviceArray,
    type: _DataTypeT,
) -> Array[Scalar[_DataTypeT]]: ...
@overload
def nulls(size: int, memory_pool: MemoryPool | None = None) -> NullArray: ...
@overload
def nulls(
    size: int, type: types.NullType | None, memory_pool: MemoryPool | None = None
) -> NullArray: ...
@overload
def nulls(
    size: int, type: types.BoolType, memory_pool: MemoryPool | None = None
) -> BooleanArray: ...
@overload
def nulls(size: int, type: types.Int8Type, memory_pool: MemoryPool | None = None) -> Int8Array: ...
@overload
def nulls(
    size: int, type: types.Int16Type, memory_pool: MemoryPool | None = None
) -> Int16Array: ...
@overload
def nulls(
    size: int, type: types.Int32Type, memory_pool: MemoryPool | None = None
) -> Int32Array: ...
@overload
def nulls(
    size: int, type: types.Int64Type, memory_pool: MemoryPool | None = None
) -> Int64Array: ...
@overload
def nulls(
    size: int, type: types.UInt8Type, memory_pool: MemoryPool | None = None
) -> UInt8Array: ...
@overload
def nulls(
    size: int, type: types.UInt16Type, memory_pool: MemoryPool | None = None
) -> UInt16Array: ...
@overload
def nulls(
    size: int, type: types.Uint32Type, memory_pool: MemoryPool | None = None
) -> UInt32Array: ...
@overload
def nulls(
    size: int, type: types.UInt64Type, memory_pool: MemoryPool | None = None
) -> UInt64Array: ...
@overload
def nulls(
    size: int, type: types.Float16Type, memory_pool: MemoryPool | None = None
) -> HalfFloatArray: ...
@overload
def nulls(
    size: int, type: types.Float32Type, memory_pool: MemoryPool | None = None
) -> FloatArray: ...
@overload
def nulls(
    size: int, type: types.Float64Type, memory_pool: MemoryPool | None = None
) -> DoubleArray: ...
@overload
def nulls(
    size: int, type: types.Decimal32Type, memory_pool: MemoryPool | None = None
) -> Decimal128Array: ...
@overload
def nulls(
    size: int, type: types.Decimal64Type, memory_pool: MemoryPool | None = None
) -> Decimal128Array: ...
@overload
def nulls(
    size: int, type: types.Decimal128Type, memory_pool: MemoryPool | None = None
) -> Decimal128Array: ...
@overload
def nulls(
    size: int, type: types.Decimal256Type, memory_pool: MemoryPool | None = None
) -> Decimal256Array: ...
@overload
def nulls(
    size: int, type: types.Date32Type, memory_pool: MemoryPool | None = None
) -> Date32Array: ...
@overload
def nulls(
    size: int, type: types.Date64Type, memory_pool: MemoryPool | None = None
) -> Date64Array: ...
@overload
def nulls(
    size: int, type: types.Time32Type[types._Time32Unit], memory_pool: MemoryPool | None = None
) -> Time32Array[types._Time32Unit]: ...
@overload
def nulls(
    size: int, type: types.Time64Type[types._Time64Unit], memory_pool: MemoryPool | None = None
) -> Time64Array[types._Time64Unit]: ...
@overload
def nulls(
    size: int,
    type: types.TimestampType[types._Unit, types._Tz],
    memory_pool: MemoryPool | None = None,
) -> TimestampArray[types._Unit, types._Tz]: ...
@overload
def nulls(
    size: int, type: types.DurationType[types._Unit], memory_pool: MemoryPool | None = None
) -> DurationArray[types._Unit]: ...
@overload
def nulls(
    size: int, type: types.MonthDayNanoIntervalType, memory_pool: MemoryPool | None = None
) -> MonthDayNanoIntervalArray: ...
@overload
def nulls(
    size: int,
    type: types.BinaryType,
    memory_pool: MemoryPool | None = None,
) -> BinaryArray: ...
@overload
def nulls(
    size: int,
    type: types.LargeBinaryType,
    memory_pool: MemoryPool | None = None,
) -> LargeBinaryArray: ...
@overload
def nulls(
    size: int,
    type: types.FixedSizeBinaryType,
    memory_pool: MemoryPool | None = None,
) -> FixedSizeBinaryArray: ...
@overload
def nulls(
    size: int,
    type: types.StringType,
    memory_pool: MemoryPool | None = None,
) -> StringArray: ...
@overload
def nulls(
    size: int,
    type: types.LargeStringType,
    memory_pool: MemoryPool | None = None,
) -> LargeStringArray: ...
@overload
def nulls(
    size: int,
    type: types.BinaryViewType,
    memory_pool: MemoryPool | None = None,
) -> BinaryViewArray: ...
@overload
def nulls(
    size: int,
    type: types.StringViewType,
    memory_pool: MemoryPool | None = None,
) -> StringViewArray: ...
@overload
def nulls(
    size: int,
    type: types.LargeListType[_DataTypeT],
    memory_pool: MemoryPool | None = None,
) -> LargeListArray[_DataTypeT]: ...
@overload
def nulls(
    size: int,
    type: types.ListViewType[_DataTypeT],
    memory_pool: MemoryPool | None = None,
) -> ListViewArray[_DataTypeT]: ...
@overload
def nulls(
    size: int,
    type: types.LargeListViewType[_DataTypeT],
    memory_pool: MemoryPool | None = None,
) -> LargeListViewArray[_DataTypeT]: ...
@overload
def nulls(
    size: int,
    type: types.FixedSizeListType[_DataTypeT, _Size],
    memory_pool: MemoryPool | None = None,
) -> FixedSizeListArray[_DataTypeT, _Size]: ...
@overload
def nulls(
    size: int,
    type: types.ListType[_DataTypeT],
    memory_pool: MemoryPool | None = None,
) -> ListArray[scalar.ListScalar[_DataTypeT]]: ...
@overload
def nulls(
    size: int,
    type: types.StructType,
    memory_pool: MemoryPool | None = None,
) -> StructArray: ...
@overload
def nulls(
    size: int,
    type: types.MapType[_MapKeyT, _MapItemT],
    memory_pool: MemoryPool | None = None,
) -> MapArray[_MapKeyT, _MapItemT]: ...
@overload
def nulls(
    size: int,
    type: types.DictionaryType[_IndexT, _BasicValueT],
    memory_pool: MemoryPool | None = None,
) -> DictionaryArray[_IndexT, _BasicValueT]: ...
@overload
def nulls(
    size: int,
    type: types.RunEndEncodedType[_RunEndType, _BasicValueT],
    memory_pool: MemoryPool | None = None,
) -> RunEndEncodedArray[_RunEndType, _BasicValueT]: ...
@overload
def nulls(
    size: int,
    type: types.UnionType,
    memory_pool: MemoryPool | None = None,
) -> UnionArray: ...
@overload
def nulls(
    size: int,
    type: types.FixedShapeTensorType[types._ValueT],
    memory_pool: MemoryPool | None = None,
) -> FixedShapeTensorArray[Any]: ...
@overload
def nulls(
    size: int,
    type: types.Bool8Type,
    memory_pool: MemoryPool | None = None,
) -> Bool8Array: ...
@overload
def nulls(
    size: int,
    type: types.UuidType,
    memory_pool: MemoryPool | None = None,
) -> UuidArray[Any]: ...
@overload
def nulls(
    size: int,
    type: types.JsonType,
    memory_pool: MemoryPool | None = None,
) -> JsonArray[Any]: ...
@overload
def nulls(
    size: int,
    type: types.OpaqueType,
    memory_pool: MemoryPool | None = None,
) -> OpaqueArray[Any]: ...
@overload
def nulls(
    size: int,
    type: types.ExtensionType,
    memory_pool: MemoryPool | None = None,
) -> ExtensionArray[Any]: ...
@overload
def repeat(
    value: None | scalar.NullScalar, size: int, memory_pool: MemoryPool | None = None
) -> NullArray: ...
@overload
def repeat(  # type: ignore[overload-overlap]
    value: bool | scalar.BooleanScalar, size: int, memory_pool: MemoryPool | None = None
) -> BooleanArray: ...
@overload
def repeat(
    value: scalar.Int8Scalar, size: int, memory_pool: MemoryPool | None = None
) -> Int8Array: ...
@overload
def repeat(
    value: scalar.Int16Scalar, size: int, memory_pool: MemoryPool | None = None
) -> Int16Array: ...
@overload
def repeat(
    value: scalar.Int32Scalar, size: int, memory_pool: MemoryPool | None = None
) -> Int32Array: ...
@overload
def repeat(
    value: int | scalar.Int64Scalar, size: int, memory_pool: MemoryPool | None = None
) -> Int64Array: ...
@overload
def repeat(
    value: scalar.UInt8Scalar, size: int, memory_pool: MemoryPool | None = None
) -> UInt8Array: ...
@overload
def repeat(
    value: scalar.UInt16Scalar, size: int, memory_pool: MemoryPool | None = None
) -> UInt16Array: ...
@overload
def repeat(
    value: scalar.UInt32Scalar, size: int, memory_pool: MemoryPool | None = None
) -> UInt32Array: ...
@overload
def repeat(
    value: scalar.UInt64Scalar, size: int, memory_pool: MemoryPool | None = None
) -> UInt64Array: ...
@overload
def repeat(
    value: scalar.HalfFloatScalar, size: int, memory_pool: MemoryPool | None = None
) -> HalfFloatArray: ...
@overload
def repeat(
    value: scalar.FloatScalar, size: int, memory_pool: MemoryPool | None = None
) -> FloatArray: ...
@overload
def repeat(
    value: float | scalar.DoubleScalar, size: int, memory_pool: MemoryPool | None = None
) -> DoubleArray: ...
@overload
def repeat(
    value: Decimal | scalar.Decimal32Scalar, size: int, memory_pool: MemoryPool | None = None
) -> Decimal32Array: ...
@overload
def repeat(
    value: scalar.Decimal64Scalar, size: int, memory_pool: MemoryPool | None = None
) -> Decimal64Array: ...
@overload
def repeat(
    value: scalar.Decimal128Scalar, size: int, memory_pool: MemoryPool | None = None
) -> Decimal128Array: ...
@overload
def repeat(
    value: scalar.Decimal256Scalar, size: int, memory_pool: MemoryPool | None = None
) -> Decimal256Array: ...
@overload
def repeat(
    value: dt.date | scalar.Date32Scalar, size: int, memory_pool: MemoryPool | None = None
) -> Date32Array: ...
@overload
def repeat(
    value: scalar.Date64Scalar, size: int, memory_pool: MemoryPool | None = None
) -> Date64Array: ...
@overload
def repeat(
    value: scalar.Time32Scalar[types._Time32Unit], size: int, memory_pool: MemoryPool | None = None
) -> Time32Array[types._Time32Unit]: ...
@overload
def repeat(
    value: dt.time | scalar.Time64Scalar[types._Time64Unit],
    size: int,
    memory_pool: MemoryPool | None = None,
) -> Time64Array[types._Time64Unit]: ...
@overload
def repeat(
    value: scalar.TimestampScalar[types._Unit, types._Tz],
    size: int,
    memory_pool: MemoryPool | None = None,
) -> TimestampArray[types._Unit, types._Tz]: ...
@overload
def repeat(
    value: dt.timedelta | scalar.DurationScalar[types._Unit],
    size: int,
    memory_pool: MemoryPool | None = None,
) -> DurationArray[types._Unit]: ...
@overload
def repeat(  # pyright: ignore[reportOverlappingOverload]
    value: MonthDayNano | scalar.MonthDayNanoIntervalScalar,
    size: int,
    memory_pool: MemoryPool | None = None,
) -> MonthDayNanoIntervalArray: ...
@overload
def repeat(
    value: bytes | scalar.BinaryScalar,
    size: int,
    memory_pool: MemoryPool | None = None,
) -> BinaryArray: ...
@overload
def repeat(
    value: scalar.LargeBinaryScalar,
    size: int,
    memory_pool: MemoryPool | None = None,
) -> LargeBinaryArray: ...
@overload
def repeat(
    value: scalar.FixedSizeBinaryScalar,
    size: int,
    memory_pool: MemoryPool | None = None,
) -> FixedSizeBinaryArray: ...
@overload
def repeat(
    value: str | scalar.StringScalar,
    size: int,
    memory_pool: MemoryPool | None = None,
) -> StringArray: ...
@overload
def repeat(
    value: scalar.LargeStringScalar,
    size: int,
    memory_pool: MemoryPool | None = None,
) -> LargeStringArray: ...
@overload
def repeat(
    value: scalar.BinaryViewScalar,
    size: int,
    memory_pool: MemoryPool | None = None,
) -> BinaryViewArray: ...
@overload
def repeat(
    value: scalar.StringViewScalar,
    size: int,
    memory_pool: MemoryPool | None = None,
) -> StringViewArray: ...
@overload
def repeat(
    value: list[Any] | tuple[Any] | scalar.ListScalar[_DataTypeT],
    size: int,
    memory_pool: MemoryPool | None = None,
) -> ListArray[scalar.ListScalar[_DataTypeT]]: ...
@overload
def repeat(
    value: scalar.FixedSizeListScalar[_DataTypeT, _Size],
    size: int,
    memory_pool: MemoryPool | None = None,
) -> FixedSizeListArray[_DataTypeT, _Size]: ...
@overload
def repeat(
    value: scalar.LargeListScalar[_DataTypeT],
    size: int,
    memory_pool: MemoryPool | None = None,
) -> LargeListArray[_DataTypeT]: ...
@overload
def repeat(
    value: scalar.ListViewScalar[_DataTypeT],
    size: int,
    memory_pool: MemoryPool | None = None,
) -> ListViewArray[_DataTypeT]: ...
@overload
def repeat(
    value: scalar.LargeListViewScalar[_DataTypeT],
    size: int,
    memory_pool: MemoryPool | None = None,
) -> LargeListViewArray[_DataTypeT]: ...
@overload
def repeat(
    value: dict[str, Any] | scalar.StructScalar,
    size: int,
    memory_pool: MemoryPool | None = None,
) -> StructArray: ...
@overload
def repeat(
    value: scalar.MapScalar[_MapKeyT, _MapItemT],
    size: int,
    memory_pool: MemoryPool | None = None,
) -> MapArray[_MapKeyT, _MapItemT]: ...
@overload
def repeat(
    value: scalar.DictionaryScalar[_IndexT, _BasicValueT],
    size: int,
    memory_pool: MemoryPool | None = None,
) -> DictionaryArray[_IndexT, _BasicValueT]: ...
@overload
def repeat(
    value: scalar.RunEndEncodedScalar[_RunEndType, _BasicValueT],
    size: int,
    memory_pool: MemoryPool | None = None,
) -> RunEndEncodedArray[_RunEndType, _BasicValueT]: ...
@overload
def repeat(
    value: scalar.UnionScalar,
    size: int,
    memory_pool: MemoryPool | None = None,
) -> UnionArray: ...
@overload
def repeat(
    value: scalar.FixedShapeTensorScalar,
    size: int,
    memory_pool: MemoryPool | None = None,
) -> FixedShapeTensorArray[Any]: ...
@overload
def repeat(
    value: scalar.Bool8Scalar,
    size: int,
    memory_pool: MemoryPool | None = None,
) -> Bool8Array: ...
@overload
def repeat(
    value: scalar.UuidScalar,
    size: int,
    memory_pool: MemoryPool | None = None,
) -> UuidArray[Any]: ...
@overload
def repeat(
    value: scalar.JsonScalar,
    size: int,
    memory_pool: MemoryPool | None = None,
) -> JsonArray[Any]: ...
@overload
def repeat(
    value: scalar.OpaqueScalar,
    size: int,
    memory_pool: MemoryPool | None = None,
) -> OpaqueArray[Any]: ...
@overload
def repeat(
    value: scalar.ExtensionScalar,
    size: int,
    memory_pool: MemoryPool | None = None,
) -> ExtensionArray[Any]: ...
def infer_type(values: Iterable[Any], mask: Mask, from_pandas: bool = False) -> DataType: ...

_ConvertAs = TypeVar("_ConvertAs", pd.DataFrame, pd.Series)

class _PandasConvertible(_Weakrefable, Generic[_ConvertAs]):
    def to_pandas(
        self,
        memory_pool: MemoryPool | None = None,
        categories: list | None = None,
        strings_to_categorical: bool = False,
        zero_copy_only: bool = False,
        integer_object_nulls: bool = False,
        date_as_object: bool = True,
        timestamp_as_object: bool = False,
        use_threads: bool = True,
        deduplicate_objects: bool = True,
        ignore_metadata: bool = False,
        safe: bool = True,
        split_blocks: bool = False,
        self_destruct: bool = False,
        maps_as_pydicts: Literal["None", "lossy", "strict"] | None = None,
        types_mapper: Callable[[DataType], ExtensionDtype | None] | None = None,
        coerce_temporal_nanoseconds: bool = False,
    ) -> _ConvertAs: ...

_CastAs = TypeVar("_CastAs", bound=DataType)
_ScalarT = TypeVar("_ScalarT", bound=Scalar)

class Array(_PandasConvertible[pd.Series], Generic[_ScalarT]):
    def diff(self, other: Self) -> str: ...
    def cast(
        self,
        target_type: _CastAs,
        safe: bool = True,
        options: CastOptions | None = None,
        memory_pool: MemoryPool | None = None,
    ) -> Array[Scalar[_CastAs]]: ...
    def view(self, target_type: _CastAs) -> Array[Scalar[_CastAs]]: ...
    def sum(self, **kwargs) -> _ScalarT: ...
    @property
    def type(self: Array[Scalar[_DataTypeT]]) -> _DataTypeT: ...
    def unique(self) -> Self: ...
    def dictionary_encode(self, null_encoding: str = "mask") -> DictionaryArray: ...
    @overload
    @staticmethod
    def from_pandas(
        obj: pd.Series | np.ndarray | ArrayLike,
        *,
        mask: Mask | None = None,
        type: _DataTypeT,
        safe: bool = True,
        memory_pool: MemoryPool | None = None,
    ) -> Array[Scalar[_DataTypeT]]: ...
    @overload
    @staticmethod
    def from_pandas(
        obj: pd.Series | np.ndarray | ArrayLike,
        *,
        mask: Mask | None = None,
        safe: bool = True,
        memory_pool: MemoryPool | None = None,
    ) -> Array[Scalar]: ...
    @staticmethod
    def from_buffers(
        type: _DataTypeT,
        length: int,
        buffers: list[Buffer],
        null_count: int = -1,
        offset=0,
        children: NullableCollection[Array[Scalar[_DataTypeT]]] | None = None,
    ) -> Array[Scalar[_DataTypeT]]: ...
    @property
    def null_count(self) -> int: ...
    @property
    def nbytes(self) -> int: ...
    def get_total_buffer_size(self) -> int: ...
    def __sizeof__(self) -> int: ...
    def __iter__(self) -> Iterator[_ScalarT]: ...
    def to_string(
        self,
        *,
        indent: int = 2,
        top_level_indent: int = 0,
        window: int = 10,
        container_window: int = 2,
        skip_new_lines: bool = False,
    ) -> str: ...
    format = to_string
    def equals(self, other: Self) -> bool: ...
    def __len__(self) -> int: ...
    def is_null(self, *, nan_is_null: bool = False) -> BooleanArray: ...
    def is_nan(self) -> BooleanArray: ...
    def is_valid(self) -> BooleanArray: ...
    def fill_null(
        self: Array[Scalar[_BasicDataType[_AsPyType]]], fill_value: _AsPyType
    ) -> Array[Scalar[_BasicDataType[_AsPyType]]]: ...
    @overload
    def __getitem__(self, key: int) -> _ScalarT: ...
    @overload
    def __getitem__(self, key: slice) -> Self: ...
    def slice(self, offset: int = 0, length: int | None = None) -> Self: ...
    def take(self, indices: Indices) -> Self: ...
    def drop_null(self) -> Self: ...
    def filter(
        self,
        mask: Mask,
        *,
        null_selection_behavior: Literal["drop", "emit_null"] = "drop",
    ) -> Self: ...
    @overload
    def index(
        self: Array[_ScalarT],
        value: _ScalarT,
        start: int | None = None,
        end: int | None = None,
        *,
        memory_pool: MemoryPool | None = None,
    ) -> scalar.Int64Scalar: ...
    @overload
    def index(
        self: Array[Scalar[_BasicDataType[_AsPyType]]],
        value: _AsPyType,
        start: int | None = None,
        end: int | None = None,
        *,
        memory_pool: MemoryPool | None = None,
    ) -> scalar.Int64Scalar: ...
    def sort(self, order: Order = "ascending", **kwargs) -> Self: ...
    def __array__(self, dtype: np.dtype | None = None, copy: bool | None = None) -> np.ndarray: ...
    def to_numpy(self, zero_copy_only: bool = True, writable: bool = False) -> np.ndarray: ...
    def to_pylist(
        self: Array[Scalar[_BasicDataType[_AsPyType]]],
    ) -> list[_AsPyType | None]: ...
    tolist = to_pylist
    def validate(self, *, full: bool = False) -> None: ...
    @property
    def offset(self) -> int: ...
    def buffers(self) -> list[Buffer | None]: ...
    def copy_to(self, destination: MemoryManager | Device) -> Self: ...
    def _export_to_c(self, out_ptr: int, out_schema_ptr: int = 0) -> None: ...
    @classmethod
    def _import_from_c(cls, in_ptr: int, type: int | DataType) -> Self: ...
    def __arrow_c_array__(self, requested_schema=None) -> Any: ...
    @classmethod
    def _import_from_c_capsule(cls, schema_capsule, array_capsule) -> Self: ...
    def _export_to_c_device(self, out_ptr: int, out_schema_ptr: int = 0) -> None: ...
    @classmethod
    def _import_from_c_device(cls, in_ptr: int, type: DataType | int) -> Self: ...
    def __arrow_c_device_array__(self, requested_schema=None, **kwargs) -> Any: ...
    @classmethod
    def _import_from_c_device_capsule(cls, schema_capsule, array_capsule) -> Self: ...
    def __dlpack__(self, stream: int | None = None) -> Any: ...
    def __dlpack_device__(self) -> tuple[int, int]: ...
    @property
    def device_type(self) -> DeviceAllocationType: ...
    @property
    def is_cpu(self) -> bool: ...

class NullArray(Array[scalar.NullScalar]): ...

class BooleanArray(Array[scalar.BooleanScalar]):
    @property
    def false_count(self) -> int: ...
    @property
    def true_count(self) -> int: ...

class NumericArray(Array[_ScalarT]): ...
class IntegerArray(NumericArray[_ScalarT]): ...
class FloatingPointArray(NumericArray[_ScalarT]): ...
class Int8Array(IntegerArray[scalar.Int8Scalar]): ...
class UInt8Array(IntegerArray[scalar.UInt8Scalar]): ...
class Int16Array(IntegerArray[scalar.Int16Scalar]): ...
class UInt16Array(IntegerArray[scalar.UInt16Scalar]): ...
class Int32Array(IntegerArray[scalar.Int32Scalar]): ...
class UInt32Array(IntegerArray[scalar.UInt32Scalar]): ...
class Int64Array(IntegerArray[scalar.Int64Scalar]): ...
class UInt64Array(IntegerArray[scalar.UInt64Scalar]): ...
class Date32Array(NumericArray[scalar.Date32Scalar]): ...
class Date64Array(NumericArray[scalar.Date64Scalar]): ...
class TimestampArray(NumericArray[scalar.TimestampScalar[types._Unit, types._Tz]]): ...
class Time32Array(NumericArray[scalar.Time32Scalar[types._Time32Unit]]): ...
class Time64Array(NumericArray[scalar.Time64Scalar[types._Time64Unit]]): ...
class DurationArray(NumericArray[scalar.DurationScalar[types._Unit]]): ...
class MonthDayNanoIntervalArray(Array[scalar.MonthDayNanoIntervalScalar]): ...
class HalfFloatArray(FloatingPointArray[scalar.HalfFloatScalar]): ...
class FloatArray(FloatingPointArray[scalar.FloatScalar]): ...
class DoubleArray(FloatingPointArray[scalar.DoubleScalar]): ...
class FixedSizeBinaryArray(Array[scalar.FixedSizeBinaryScalar]): ...
class Decimal32Array(FixedSizeBinaryArray): ...
class Decimal64Array(FixedSizeBinaryArray): ...
class Decimal128Array(FixedSizeBinaryArray): ...
class Decimal256Array(FixedSizeBinaryArray): ...

class BaseListArray(Array[_ScalarT]):
    def flatten(self, recursive: bool = False) -> Array: ...
    def value_parent_indices(self) -> Int64Array: ...
    def value_lengths(self) -> Int32Array: ...

class ListArray(BaseListArray[_ScalarT]):
    @overload
    @classmethod
    def from_arrays(
        cls,
        offsets: Int32Array | list[int],
        values: Array[Scalar[_DataTypeT]],
        *,
        type: None = None,
        pool: MemoryPool | None = None,
        mask: Mask | None = None,
    ) -> ListArray[scalar.ListScalar[_DataTypeT]]: ...
    @overload
    @classmethod
    def from_arrays(
        cls,
        offsets: Int32Array | list[int],
        values: list[int],
        *,
        type: None = None,
        pool: MemoryPool | None = None,
        mask: Mask | None = None,
    ) -> ListArray[scalar.ListScalar[types.Int64Type]]: ...
    @overload
    @classmethod
    def from_arrays(
        cls,
        offsets: Int32Array | list[int],
        values: list[float],
        *,
        type: None = None,
        pool: MemoryPool | None = None,
        mask: Mask | None = None,
    ) -> ListArray[scalar.ListScalar[types.Float64Type]]: ...
    @overload
    @classmethod
    def from_arrays(
        cls,
        offsets: Int32Array | list[int],
        values: list[str],
        *,
        type: None = None,
        pool: MemoryPool | None = None,
        mask: Mask | None = None,
    ) -> ListArray[scalar.ListScalar[types.StringType]]: ...
    @overload
    @classmethod
    def from_arrays(
        cls,
        offsets: Int32Array | list[int],
        values: list[bytes],
        *,
        type: None = None,
        pool: MemoryPool | None = None,
        mask: Mask | None = None,
    ) -> ListArray[scalar.ListScalar[types.BinaryType]]: ...
    @overload
    @classmethod
    def from_arrays(
        cls,
        offsets: Int32Array | list[int],
        values: list,
        *,
        type: None = None,
        pool: MemoryPool | None = None,
        mask: Mask | None = None,
    ) -> ListArray: ...
    @overload
    @classmethod
    def from_arrays(
        cls,
        offsets: Int32Array | list[int],
        values: Array | list,
        *,
        type: _DataTypeT,
        pool: MemoryPool | None = None,
        mask: Mask | None = None,
    ) -> ListArray[scalar.ListScalar[_DataTypeT]]: ...
    @property
    def values(self) -> Array: ...
    @property
    def offsets(self) -> Int32Array: ...

class LargeListArray(BaseListArray[scalar.LargeListScalar[_DataTypeT]]):
    @overload
    @classmethod
    def from_arrays(
        cls,
        offsets: Int64Array,
        values: Array[Scalar[_DataTypeT]],
        *,
        type: None = None,
        pool: MemoryPool | None = None,
        mask: Mask | None = None,
    ) -> LargeListArray[_DataTypeT]: ...
    @overload
    @classmethod
    def from_arrays(
        cls,
        offsets: Int64Array,
        values: Array,
        *,
        type: _DataTypeT,
        pool: MemoryPool | None = None,
        mask: Mask | None = None,
    ) -> LargeListArray[_DataTypeT]: ...
    @property
    def values(self) -> Array: ...
    @property
    def offsets(self) -> Int64Array: ...

class ListViewArray(BaseListArray[scalar.ListViewScalar[_DataTypeT]]):
    @overload
    @classmethod
    def from_arrays(
        cls,
        offsets: Int32Array,
        values: Array[Scalar[_DataTypeT]],
        *,
        type: None = None,
        pool: MemoryPool | None = None,
        mask: Mask | None = None,
    ) -> ListViewArray[_DataTypeT]: ...
    @overload
    @classmethod
    def from_arrays(
        cls,
        offsets: Int32Array,
        values: Array,
        *,
        type: _DataTypeT,
        pool: MemoryPool | None = None,
        mask: Mask | None = None,
    ) -> ListViewArray[_DataTypeT]: ...
    @property
    def values(self) -> Array: ...
    @property
    def offsets(self) -> Int32Array: ...
    @property
    def sizes(self) -> Int32Array: ...

class LargeListViewArray(BaseListArray[scalar.LargeListScalar[_DataTypeT]]):
    @overload
    @classmethod
    def from_arrays(
        cls,
        offsets: Int64Array,
        values: Array[Scalar[_DataTypeT]],
        *,
        type: None = None,
        pool: MemoryPool | None = None,
        mask: Mask | None = None,
    ) -> LargeListViewArray[_DataTypeT]: ...
    @overload
    @classmethod
    def from_arrays(
        cls,
        offsets: Int64Array,
        values: Array,
        *,
        type: _DataTypeT,
        pool: MemoryPool | None = None,
        mask: Mask | None = None,
    ) -> LargeListViewArray[_DataTypeT]: ...
    @property
    def values(self) -> Array: ...
    @property
    def offsets(self) -> Int64Array: ...
    @property
    def sizes(self) -> Int64Array: ...

class FixedSizeListArray(BaseListArray[scalar.FixedSizeListScalar[_DataTypeT, _Size]]):
    @overload
    @classmethod
    def from_arrays(
        cls,
        values: Array[Scalar[_DataTypeT]],
        *,
        type: None = None,
        mask: Mask | None = None,
    ) -> FixedSizeListArray[_DataTypeT, None]: ...
    @overload
    @classmethod
    def from_arrays(
        cls,
        values: Array[Scalar[_DataTypeT]],
        limit_size: _Size,
        *,
        type: None = None,
        mask: Mask | None = None,
    ) -> FixedSizeListArray[_DataTypeT, _Size]: ...
    @property
    def values(self) -> BaseListArray[scalar.ListScalar[_DataTypeT]]: ...

_MapKeyT = TypeVar("_MapKeyT", bound=_BasicDataType)
_MapItemT = TypeVar("_MapItemT", bound=_BasicDataType)

class MapArray(ListArray[scalar.MapScalar[_MapKeyT, _MapItemT]]):
    @overload
    @classmethod
    def from_arrays(
        cls,
        offsets: Int64Array,
        keys: Array[Scalar[_MapKeyT]],
        items: Array[Scalar[_MapItemT]],
        *,
        type: None = None,
        pool: MemoryPool | None = None,
        mask: Mask | None = None,
    ) -> MapArray[_MapKeyT, _MapItemT]: ...
    @overload
    @classmethod
    def from_arrays(  # pyright: ignore[reportIncompatibleMethodOverride]
        cls,
        offsets: Int64Array,
        values: Array,
        *,
        type: MapType[_MapKeyT, _MapItemT],
        pool: MemoryPool | None = None,
        mask: Mask | None = None,
    ) -> MapArray[_MapKeyT, _MapItemT]: ...
    @property
    def keys(self) -> Array: ...
    @property
    def items(self) -> Array: ...

class UnionArray(Array[scalar.UnionScalar]):
    def child(self, pos: int) -> Field: ...
    def field(self, pos: int) -> Array: ...
    @property
    def type_codes(self) -> Int8Array: ...
    @property
    def offsets(self) -> Int32Array: ...
    @staticmethod
    def from_dense(
        type: Int8Array,
        value_offsets: Int32Array,
        children: NullableCollection[Array],
        field_names: list[str] | None = None,
        type_codes: Int8Array | None = None,
    ) -> UnionArray: ...
    @staticmethod
    def from_sparse(
        types: Int8Array,
        children: NullableCollection[Array],
        field_names: list[str] | None = None,
        type_codes: Int8Array | None = None,
    ) -> UnionArray: ...

class StringArray(Array[scalar.StringScalar]):
    @staticmethod
    def from_buffers(  # type: ignore[override]
        length: int,
        value_offsets: Buffer,
        data: Buffer,
        null_bitmap: Buffer | None = None,
        null_count: int | None = -1,
        offset: int | None = 0,
    ) -> StringArray: ...

class LargeStringArray(Array[scalar.LargeStringScalar]):
    @staticmethod
    def from_buffers(  # type: ignore[override]
        length: int,
        value_offsets: Buffer,
        data: Buffer,
        null_bitmap: Buffer | None = None,
        null_count: int | None = -1,
        offset: int | None = 0,
    ) -> StringArray: ...

class StringViewArray(Array[scalar.StringViewScalar]): ...

class BinaryArray(Array[scalar.BinaryScalar]):
    @property
    def total_values_length(self) -> int: ...

class LargeBinaryArray(Array[scalar.LargeBinaryScalar]):
    @property
    def total_values_length(self) -> int: ...

class BinaryViewArray(Array[scalar.BinaryViewScalar]): ...

class DictionaryArray(Array[scalar.DictionaryScalar[_IndexT, _BasicValueT]]):
    def dictionary_encode(self) -> Self: ...  # type: ignore[override]
    def dictionary_decode(self) -> Array[Scalar[_BasicValueT]]: ...
    @property
    def indices(self) -> Array[Scalar[_IndexT]]: ...
    @property
    def dictionary(self) -> Array[Scalar[_BasicValueT]]: ...
    @staticmethod
    def from_buffers(  # type: ignore[override]
        type: _BasicValueT,
        length: int,
        buffers: list[Buffer],
        dictionary: Array | np.ndarray | pd.Series,
        null_count: int = -1,
        offset: int = 0,
    ) -> DictionaryArray[Any, _BasicValueT]: ...
    @staticmethod
    def from_arrays(
        indices: Indices,
        dictionary: Array | np.ndarray | pd.Series,
        mask: np.ndarray | pd.Series | BooleanArray | None = None,
        ordered: bool = False,
        from_pandas: bool = False,
        safe: bool = True,
        memory_pool: MemoryPool | None = None,
    ) -> DictionaryArray: ...

class StructArray(Array[scalar.StructScalar]):
    def field(self, index: int | str) -> Array: ...
    def flatten(self, memory_pool: MemoryPool | None = None) -> list[Array]: ...
    @staticmethod
    def from_arrays(
        arrays: Iterable[Array],
        names: list[str] | None = None,
        fields: list[Field] | None = None,
        mask=None,
        memory_pool: MemoryPool | None = None,
        type: types.StructType | None = None,
    ) -> StructArray: ...
    def sort(self, order: Order = "ascending", by: str | None = None, **kwargs) -> StructArray: ...

class RunEndEncodedArray(Array[scalar.RunEndEncodedScalar[_RunEndType, _BasicValueT]]):
    @overload
    @staticmethod
    def from_arrays(
        run_ends: Int16Array,
        values: Array,
        type: DataType | None = None,
    ) -> RunEndEncodedArray[types.Int16Type, _BasicValueT]: ...
    @overload
    @staticmethod
    def from_arrays(
        run_ends: Int32Array,
        values: Array,
        type: DataType | None = None,
    ) -> RunEndEncodedArray[types.Int32Type, _BasicValueT]: ...
    @overload
    @staticmethod
    def from_arrays(
        run_ends: Int64Array,
        values: Array,
        type: DataType | None = None,
    ) -> RunEndEncodedArray[types.Int64Type, _BasicValueT]: ...
    @staticmethod
    def from_buffers(  # pyright: ignore[reportIncompatibleMethodOverride]
        type: DataType,
        length: int,
        buffers: list[Buffer],
        null_count: int = -1,
        offset=0,
        children: tuple[Array, Array] | None = None,
    ) -> RunEndEncodedArray[Any, _BasicValueT]: ...
    @property
    def run_ends(self) -> Array[scalar.Scalar[_RunEndType]]: ...
    @property
    def values(self) -> Array[scalar.Scalar[_BasicValueT]]: ...
    def find_physical_offset(self) -> int: ...
    def find_physical_length(self) -> int: ...

_ArrayT = TypeVar("_ArrayT", bound=Array)

class ExtensionArray(Array[scalar.ExtensionScalar], Generic[_ArrayT]):
    @property
    def storage(self) -> Any: ...
    @staticmethod
    def from_storage(
        typ: types.BaseExtensionType, storage: _ArrayT
    ) -> ExtensionArray[_ArrayT]: ...

class JsonArray(ExtensionArray[_ArrayT]): ...
class UuidArray(ExtensionArray[_ArrayT]): ...

class FixedShapeTensorArray(ExtensionArray[_ArrayT]):
    def to_numpy_ndarray(self) -> np.ndarray: ...
    def to_tensor(self) -> Tensor: ...
    @classmethod
    def from_numpy_ndarray(cls, obj: np.ndarray) -> Self: ...

class OpaqueArray(ExtensionArray[_ArrayT]): ...

class Bool8Array(ExtensionArray):
    def to_numpy(self, zero_copy_only: bool = ..., writable: bool = ...) -> np.ndarray: ...
    @classmethod
    def from_storage(cls, storage: Int8Array) -> Self: ...  # type: ignore[override]
    @classmethod
    def from_numpy(cls, obj: np.ndarray) -> Self: ...

def concat_arrays(arrays: Iterable[_ArrayT], memory_pool: MemoryPool | None = None) -> _ArrayT: ...
def _empty_array(type: _DataTypeT) -> Array[scalar.Scalar[_DataTypeT]]: ...

__all__ = [
    "array",
    "asarray",
    "nulls",
    "repeat",
    "infer_type",
    "_PandasConvertible",
    "Array",
    "NullArray",
    "BooleanArray",
    "NumericArray",
    "IntegerArray",
    "FloatingPointArray",
    "Int8Array",
    "UInt8Array",
    "Int16Array",
    "UInt16Array",
    "Int32Array",
    "UInt32Array",
    "Int64Array",
    "UInt64Array",
    "Date32Array",
    "Date64Array",
    "TimestampArray",
    "Time32Array",
    "Time64Array",
    "DurationArray",
    "MonthDayNanoIntervalArray",
    "HalfFloatArray",
    "FloatArray",
    "DoubleArray",
    "FixedSizeBinaryArray",
    "Decimal32Array",
    "Decimal64Array",
    "Decimal128Array",
    "Decimal256Array",
    "BaseListArray",
    "ListArray",
    "LargeListArray",
    "ListViewArray",
    "LargeListViewArray",
    "FixedSizeListArray",
    "MapArray",
    "UnionArray",
    "StringArray",
    "LargeStringArray",
    "StringViewArray",
    "BinaryArray",
    "LargeBinaryArray",
    "BinaryViewArray",
    "DictionaryArray",
    "StructArray",
    "RunEndEncodedArray",
    "ExtensionArray",
    "Bool8Array",
    "UuidArray",
    "JsonArray",
    "OpaqueArray",
    "FixedShapeTensorArray",
    "concat_arrays",
    "_empty_array",
]
