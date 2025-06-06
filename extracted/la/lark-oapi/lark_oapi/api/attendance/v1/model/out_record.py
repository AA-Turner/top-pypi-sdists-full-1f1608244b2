# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .out_time import OutTime
from .out_time import OutTime


class OutRecord(object):
    _types = {
        "duration_unit": str,
        "start_time": OutTime,
        "end_time": OutTime,
    }

    def __init__(self, d=None):
        self.duration_unit: Optional[str] = None
        self.start_time: Optional[OutTime] = None
        self.end_time: Optional[OutTime] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OutRecordBuilder":
        return OutRecordBuilder()


class OutRecordBuilder(object):
    def __init__(self) -> None:
        self._out_record = OutRecord()

    def duration_unit(self, duration_unit: str) -> "OutRecordBuilder":
        self._out_record.duration_unit = duration_unit
        return self

    def start_time(self, start_time: OutTime) -> "OutRecordBuilder":
        self._out_record.start_time = start_time
        return self

    def end_time(self, end_time: OutTime) -> "OutRecordBuilder":
        self._out_record.end_time = end_time
        return self

    def build(self) -> "OutRecord":
        return self._out_record
