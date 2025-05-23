# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.any_pb2 import (
    Any as google___protobuf___any_pb2___Any,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from proto.google.fhir.proto.r4.core.codes_pb2 import (
    SubscriptionChannelTypeCode as proto___google___fhir___proto___r4___core___codes_pb2___SubscriptionChannelTypeCode,
    SubscriptionStatusCode as proto___google___fhir___proto___r4___core___codes_pb2___SubscriptionStatusCode,
)

from proto.google.fhir.proto.r4.core.datatypes_pb2 import (
    Code as proto___google___fhir___proto___r4___core___datatypes_pb2___Code,
    ContactPoint as proto___google___fhir___proto___r4___core___datatypes_pb2___ContactPoint,
    Extension as proto___google___fhir___proto___r4___core___datatypes_pb2___Extension,
    Id as proto___google___fhir___proto___r4___core___datatypes_pb2___Id,
    Instant as proto___google___fhir___proto___r4___core___datatypes_pb2___Instant,
    Meta as proto___google___fhir___proto___r4___core___datatypes_pb2___Meta,
    Narrative as proto___google___fhir___proto___r4___core___datatypes_pb2___Narrative,
    String as proto___google___fhir___proto___r4___core___datatypes_pb2___String,
    Uri as proto___google___fhir___proto___r4___core___datatypes_pb2___Uri,
    Url as proto___google___fhir___proto___r4___core___datatypes_pb2___Url,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class Subscription(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class StatusCode(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        value: proto___google___fhir___proto___r4___core___codes_pb2___SubscriptionStatusCode.ValueValue = ...

        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        def __init__(self,
            *,
            value : typing___Optional[proto___google___fhir___proto___r4___core___codes_pb2___SubscriptionStatusCode.ValueValue] = None,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"id",b"id"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"extension",b"extension",u"id",b"id",u"value",b"value"]) -> None: ...
    type___StatusCode = StatusCode

    class Channel(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class TypeCode(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            value: proto___google___fhir___proto___r4___core___codes_pb2___SubscriptionChannelTypeCode.ValueValue = ...

            @property
            def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

            @property
            def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

            def __init__(self,
                *,
                value : typing___Optional[proto___google___fhir___proto___r4___core___codes_pb2___SubscriptionChannelTypeCode.ValueValue] = None,
                id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
                extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions___Literal[u"id",b"id"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"extension",b"extension",u"id",b"id",u"value",b"value"]) -> None: ...
        type___TypeCode = TypeCode

        class PayloadCode(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            value: typing___Text = ...

            @property
            def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

            @property
            def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

            def __init__(self,
                *,
                id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
                extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
                value : typing___Optional[typing___Text] = None,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions___Literal[u"id",b"id"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"extension",b"extension",u"id",b"id",u"value",b"value"]) -> None: ...
        type___PayloadCode = PayloadCode


        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def modifier_extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def type(self) -> type___Subscription.Channel.TypeCode: ...

        @property
        def endpoint(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Url: ...

        @property
        def payload(self) -> type___Subscription.Channel.PayloadCode: ...

        @property
        def header(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___String]: ...

        def __init__(self,
            *,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            modifier_extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            type : typing___Optional[type___Subscription.Channel.TypeCode] = None,
            endpoint : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Url] = None,
            payload : typing___Optional[type___Subscription.Channel.PayloadCode] = None,
            header : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___String]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"endpoint",b"endpoint",u"id",b"id",u"payload",b"payload",u"type",b"type"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"endpoint",b"endpoint",u"extension",b"extension",u"header",b"header",u"id",b"id",u"modifier_extension",b"modifier_extension",u"payload",b"payload",u"type",b"type"]) -> None: ...
    type___Channel = Channel


    @property
    def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Id: ...

    @property
    def meta(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Meta: ...

    @property
    def implicit_rules(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Uri: ...

    @property
    def language(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Code: ...

    @property
    def text(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Narrative: ...

    @property
    def contained(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___any_pb2___Any]: ...

    @property
    def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

    @property
    def modifier_extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

    @property
    def status(self) -> type___Subscription.StatusCode: ...

    @property
    def contact(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___ContactPoint]: ...

    @property
    def end(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Instant: ...

    @property
    def reason(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

    @property
    def criteria(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

    @property
    def error(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

    @property
    def channel(self) -> type___Subscription.Channel: ...

    def __init__(self,
        *,
        id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Id] = None,
        meta : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Meta] = None,
        implicit_rules : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Uri] = None,
        language : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Code] = None,
        text : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Narrative] = None,
        contained : typing___Optional[typing___Iterable[google___protobuf___any_pb2___Any]] = None,
        extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
        modifier_extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
        status : typing___Optional[type___Subscription.StatusCode] = None,
        contact : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___ContactPoint]] = None,
        end : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Instant] = None,
        reason : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
        criteria : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
        error : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
        channel : typing___Optional[type___Subscription.Channel] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"channel",b"channel",u"criteria",b"criteria",u"end",b"end",u"error",b"error",u"id",b"id",u"implicit_rules",b"implicit_rules",u"language",b"language",u"meta",b"meta",u"reason",b"reason",u"status",b"status",u"text",b"text"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"channel",b"channel",u"contact",b"contact",u"contained",b"contained",u"criteria",b"criteria",u"end",b"end",u"error",b"error",u"extension",b"extension",u"id",b"id",u"implicit_rules",b"implicit_rules",u"language",b"language",u"meta",b"meta",u"modifier_extension",b"modifier_extension",u"reason",b"reason",u"status",b"status",u"text",b"text"]) -> None: ...
type___Subscription = Subscription
