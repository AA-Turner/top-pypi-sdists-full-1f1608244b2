"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Generated by https://github.com/foxglove/schemas"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class KeyValuePair(google.protobuf.message.Message):
    """A key with its associated value"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    key: builtins.str
    """Key"""
    value: builtins.str
    """Value"""
    def __init__(
        self,
        *,
        key: builtins.str = ...,
        value: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

global___KeyValuePair = KeyValuePair
