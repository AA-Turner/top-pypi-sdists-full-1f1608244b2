"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ObjectStorageConfiguration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    S3_FIELD_NUMBER: builtins.int
    GS_FIELD_NUMBER: builtins.int
    @property
    def s3(self) -> global___S3Configuration: ...
    @property
    def gs(self) -> global___GSConfiguration: ...
    def __init__(
        self,
        *,
        s3: global___S3Configuration | None = ...,
        gs: global___GSConfiguration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["gs", b"gs", "s3", b"s3", "type", b"type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["gs", b"gs", "s3", b"s3", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["type", b"type"]) -> typing_extensions.Literal["s3", "gs"] | None: ...

global___ObjectStorageConfiguration = ObjectStorageConfiguration

class S3Configuration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUCKET_FIELD_NUMBER: builtins.int
    bucket: builtins.str
    """This proto does not contain auth configuration, as by default it gets is auth from the hosting configuration.
    This is an extensible behaviour if needed (e.g: running on OpenShift while using S3 as and Object Storage)
    """
    def __init__(
        self,
        *,
        bucket: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["bucket", b"bucket"]) -> None: ...

global___S3Configuration = S3Configuration

class GSConfiguration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUCKET_FIELD_NUMBER: builtins.int
    bucket: builtins.str
    """This proto does not contain auth configuration, as by default it gets is auth from the hosting configuration.
    This is an extensible behaviour if needed (e.g: running on OpenShift while using S3 as and Object Storage)
    """
    def __init__(
        self,
        *,
        bucket: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["bucket", b"bucket"]) -> None: ...

global___GSConfiguration = GSConfiguration
