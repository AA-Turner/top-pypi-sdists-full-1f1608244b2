from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class PubKey(_message.Message):
    __slots__ = ['key']
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: bytes

    def __init__(self, key: _Optional[bytes]=...) -> None:
        ...

class PrivKey(_message.Message):
    __slots__ = ['secret']
    SECRET_FIELD_NUMBER: _ClassVar[int]
    secret: bytes

    def __init__(self, secret: _Optional[bytes]=...) -> None:
        ...