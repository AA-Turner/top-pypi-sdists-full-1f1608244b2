# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .out_record import OutRecord


class CreateBpmOutRecord(object):
    _types = {
        "user_id": str,
        "out_record": OutRecord,
        "out_reason": str,
        "custom_form_data": str,
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        self.out_record: Optional[OutRecord] = None
        self.out_reason: Optional[str] = None
        self.custom_form_data: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateBpmOutRecordBuilder":
        return CreateBpmOutRecordBuilder()


class CreateBpmOutRecordBuilder(object):
    def __init__(self) -> None:
        self._create_bpm_out_record = CreateBpmOutRecord()

    def user_id(self, user_id: str) -> "CreateBpmOutRecordBuilder":
        self._create_bpm_out_record.user_id = user_id
        return self

    def out_record(self, out_record: OutRecord) -> "CreateBpmOutRecordBuilder":
        self._create_bpm_out_record.out_record = out_record
        return self

    def out_reason(self, out_reason: str) -> "CreateBpmOutRecordBuilder":
        self._create_bpm_out_record.out_reason = out_reason
        return self

    def custom_form_data(self, custom_form_data: str) -> "CreateBpmOutRecordBuilder":
        self._create_bpm_out_record.custom_form_data = custom_form_data
        return self

    def build(self) -> "CreateBpmOutRecord":
        return self._create_bpm_out_record
