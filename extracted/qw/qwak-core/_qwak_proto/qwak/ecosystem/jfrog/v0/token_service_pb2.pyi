"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import qwak.ecosystem.jfrog.v0.token_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GenerateTokenRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOKEN_SPEC_FIELD_NUMBER: builtins.int
    @property
    def token_spec(self) -> qwak.ecosystem.jfrog.v0.token_pb2.JFrogTokenSpec:
        """Token spec"""
    def __init__(
        self,
        *,
        token_spec: qwak.ecosystem.jfrog.v0.token_pb2.JFrogTokenSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["token_spec", b"token_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["token_spec", b"token_spec"]) -> None: ...

global___GenerateTokenRequest = GenerateTokenRequest

class GenerateTokenResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOKEN_FIELD_NUMBER: builtins.int
    @property
    def token(self) -> qwak.ecosystem.jfrog.v0.token_pb2.JFrogToken:
        """Generated token"""
    def __init__(
        self,
        *,
        token: qwak.ecosystem.jfrog.v0.token_pb2.JFrogToken | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["token", b"token"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["token", b"token"]) -> None: ...

global___GenerateTokenResponse = GenerateTokenResponse

class GenerateArtifactoryImagePullTokenRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOKEN_SPEC_FIELD_NUMBER: builtins.int
    @property
    def token_spec(self) -> qwak.ecosystem.jfrog.v0.token_pb2.ArtifactoryImagePullTokenSpec:
        """Artifactory Image pull token spec"""
    def __init__(
        self,
        *,
        token_spec: qwak.ecosystem.jfrog.v0.token_pb2.ArtifactoryImagePullTokenSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["token_spec", b"token_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["token_spec", b"token_spec"]) -> None: ...

global___GenerateArtifactoryImagePullTokenRequest = GenerateArtifactoryImagePullTokenRequest

class GenerateArtifactoryImagePullTokenResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOKEN_FIELD_NUMBER: builtins.int
    @property
    def token(self) -> qwak.ecosystem.jfrog.v0.token_pb2.JFrogToken:
        """Generated token"""
    def __init__(
        self,
        *,
        token: qwak.ecosystem.jfrog.v0.token_pb2.JFrogToken | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["token", b"token"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["token", b"token"]) -> None: ...

global___GenerateArtifactoryImagePullTokenResponse = GenerateArtifactoryImagePullTokenResponse

class PersistTokenClaimsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SPEC_FIELD_NUMBER: builtins.int
    @property
    def spec(self) -> qwak.ecosystem.jfrog.v0.token_pb2.PersistTokenClaimsSpec:
        """Persist token claims spec"""
    def __init__(
        self,
        *,
        spec: qwak.ecosystem.jfrog.v0.token_pb2.PersistTokenClaimsSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["spec", b"spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["spec", b"spec"]) -> None: ...

global___PersistTokenClaimsRequest = PersistTokenClaimsRequest

class PersistTokenClaimsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOKEN_ID_FIELD_NUMBER: builtins.int
    token_id: builtins.str
    """The persisted token id.
    Used for later retrieval
    """
    def __init__(
        self,
        *,
        token_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["token_id", b"token_id"]) -> None: ...

global___PersistTokenClaimsResponse = PersistTokenClaimsResponse

class RevokeTokenRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOKEN_REVOKE_SPEC_FIELD_NUMBER: builtins.int
    @property
    def token_revoke_spec(self) -> qwak.ecosystem.jfrog.v0.token_pb2.JFrogTokenRevokeSpec:
        """Revoke token spec"""
    def __init__(
        self,
        *,
        token_revoke_spec: qwak.ecosystem.jfrog.v0.token_pb2.JFrogTokenRevokeSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["token_revoke_spec", b"token_revoke_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["token_revoke_spec", b"token_revoke_spec"]) -> None: ...

global___RevokeTokenRequest = RevokeTokenRequest

class RevokeTokenRequestResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___RevokeTokenRequestResponse = RevokeTokenRequestResponse
