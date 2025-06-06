from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Label(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class Sample(_message.Message):
    __slots__ = ["timestamp", "value"]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    value: float
    def __init__(self, value: _Optional[float] = ..., timestamp: _Optional[int] = ...) -> None: ...

class TimeSeries(_message.Message):
    __slots__ = ["labels", "samples"]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SAMPLES_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.RepeatedCompositeFieldContainer[Label]
    samples: _containers.RepeatedCompositeFieldContainer[Sample]
    def __init__(self, labels: _Optional[_Iterable[_Union[Label, _Mapping]]] = ..., samples: _Optional[_Iterable[_Union[Sample, _Mapping]]] = ...) -> None: ...

class WriteRequest(_message.Message):
    __slots__ = ["timeseries"]
    TIMESERIES_FIELD_NUMBER: _ClassVar[int]
    timeseries: _containers.RepeatedCompositeFieldContainer[TimeSeries]
    def __init__(self, timeseries: _Optional[_Iterable[_Union[TimeSeries, _Mapping]]] = ...) -> None: ...
