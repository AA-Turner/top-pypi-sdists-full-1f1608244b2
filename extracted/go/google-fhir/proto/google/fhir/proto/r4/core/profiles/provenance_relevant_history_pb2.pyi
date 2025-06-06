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
    ProvenanceEntityRoleCode as proto___google___fhir___proto___r4___core___codes_pb2___ProvenanceEntityRoleCode,
)

from proto.google.fhir.proto.r4.core.datatypes_pb2 import (
    Code as proto___google___fhir___proto___r4___core___datatypes_pb2___Code,
    CodeableConcept as proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept,
    DateTime as proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime,
    Extension as proto___google___fhir___proto___r4___core___datatypes_pb2___Extension,
    Id as proto___google___fhir___proto___r4___core___datatypes_pb2___Id,
    Instant as proto___google___fhir___proto___r4___core___datatypes_pb2___Instant,
    Meta as proto___google___fhir___proto___r4___core___datatypes_pb2___Meta,
    Narrative as proto___google___fhir___proto___r4___core___datatypes_pb2___Narrative,
    Reference as proto___google___fhir___proto___r4___core___datatypes_pb2___Reference,
    Signature as proto___google___fhir___proto___r4___core___datatypes_pb2___Signature,
    String as proto___google___fhir___proto___r4___core___datatypes_pb2___String,
    Uri as proto___google___fhir___proto___r4___core___datatypes_pb2___Uri,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class ProvenanceRelevantHistory(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class OccurredX(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def date_time(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime: ...

        def __init__(self,
            *,
            date_time : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"choice",b"choice",u"date_time",b"date_time"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"choice",b"choice",u"date_time",b"date_time"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions___Literal[u"choice",b"choice"]) -> typing_extensions___Literal["date_time"]: ...
    type___OccurredX = OccurredX

    class Agent(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def modifier_extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def type(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

        @property
        def role(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]: ...

        @property
        def who(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Reference: ...

        @property
        def on_behalf_of(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Reference: ...

        def __init__(self,
            *,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            modifier_extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            type : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
            role : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]] = None,
            who : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference] = None,
            on_behalf_of : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"id",b"id",u"on_behalf_of",b"on_behalf_of",u"type",b"type",u"who",b"who"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"extension",b"extension",u"id",b"id",u"modifier_extension",b"modifier_extension",u"on_behalf_of",b"on_behalf_of",u"role",b"role",u"type",b"type",u"who",b"who"]) -> None: ...
    type___Agent = Agent

    class Entity(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class RoleCode(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            value: proto___google___fhir___proto___r4___core___codes_pb2___ProvenanceEntityRoleCode.ValueValue = ...

            @property
            def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

            @property
            def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

            def __init__(self,
                *,
                value : typing___Optional[proto___google___fhir___proto___r4___core___codes_pb2___ProvenanceEntityRoleCode.ValueValue] = None,
                id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
                extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions___Literal[u"id",b"id"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"extension",b"extension",u"id",b"id",u"value",b"value"]) -> None: ...
        type___RoleCode = RoleCode


        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def modifier_extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def role(self) -> type___ProvenanceRelevantHistory.Entity.RoleCode: ...

        @property
        def what(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Reference: ...

        @property
        def agent(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___ProvenanceRelevantHistory.Agent]: ...

        def __init__(self,
            *,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            modifier_extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            role : typing___Optional[type___ProvenanceRelevantHistory.Entity.RoleCode] = None,
            what : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference] = None,
            agent : typing___Optional[typing___Iterable[type___ProvenanceRelevantHistory.Agent]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"id",b"id",u"role",b"role",u"what",b"what"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"agent",b"agent",u"extension",b"extension",u"id",b"id",u"modifier_extension",b"modifier_extension",u"role",b"role",u"what",b"what"]) -> None: ...
    type___Entity = Entity


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
    def target(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]: ...

    @property
    def occurred(self) -> type___ProvenanceRelevantHistory.OccurredX: ...

    @property
    def recorded(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Instant: ...

    @property
    def policy(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Uri]: ...

    @property
    def location(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Reference: ...

    @property
    def reason(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]: ...

    @property
    def activity(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

    @property
    def agent(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___ProvenanceRelevantHistory.Agent]: ...

    @property
    def entity(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___ProvenanceRelevantHistory.Entity]: ...

    @property
    def signature(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Signature]: ...

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
        target : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]] = None,
        occurred : typing___Optional[type___ProvenanceRelevantHistory.OccurredX] = None,
        recorded : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Instant] = None,
        policy : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Uri]] = None,
        location : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference] = None,
        reason : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]] = None,
        activity : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
        agent : typing___Optional[typing___Iterable[type___ProvenanceRelevantHistory.Agent]] = None,
        entity : typing___Optional[typing___Iterable[type___ProvenanceRelevantHistory.Entity]] = None,
        signature : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Signature]] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"activity",b"activity",u"id",b"id",u"implicit_rules",b"implicit_rules",u"language",b"language",u"location",b"location",u"meta",b"meta",u"occurred",b"occurred",u"recorded",b"recorded",u"text",b"text"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"activity",b"activity",u"agent",b"agent",u"contained",b"contained",u"entity",b"entity",u"extension",b"extension",u"id",b"id",u"implicit_rules",b"implicit_rules",u"language",b"language",u"location",b"location",u"meta",b"meta",u"modifier_extension",b"modifier_extension",u"occurred",b"occurred",u"policy",b"policy",u"reason",b"reason",u"recorded",b"recorded",u"signature",b"signature",u"target",b"target",u"text",b"text"]) -> None: ...
type___ProvenanceRelevantHistory = ProvenanceRelevantHistory
