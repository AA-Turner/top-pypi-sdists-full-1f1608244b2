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
    ActionParticipantTypeCode as proto___google___fhir___proto___r4___core___codes_pb2___ActionParticipantTypeCode,
    PublicationStatusCode as proto___google___fhir___proto___r4___core___codes_pb2___PublicationStatusCode,
    RequestIntentCode as proto___google___fhir___proto___r4___core___codes_pb2___RequestIntentCode,
    RequestPriorityCode as proto___google___fhir___proto___r4___core___codes_pb2___RequestPriorityCode,
    RequestResourceTypeCode as proto___google___fhir___proto___r4___core___codes_pb2___RequestResourceTypeCode,
)

from proto.google.fhir.proto.r4.core.datatypes_pb2 import (
    Age as proto___google___fhir___proto___r4___core___datatypes_pb2___Age,
    Boolean as proto___google___fhir___proto___r4___core___datatypes_pb2___Boolean,
    Canonical as proto___google___fhir___proto___r4___core___datatypes_pb2___Canonical,
    Code as proto___google___fhir___proto___r4___core___datatypes_pb2___Code,
    CodeableConcept as proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept,
    ContactDetail as proto___google___fhir___proto___r4___core___datatypes_pb2___ContactDetail,
    Date as proto___google___fhir___proto___r4___core___datatypes_pb2___Date,
    DateTime as proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime,
    Dosage as proto___google___fhir___proto___r4___core___datatypes_pb2___Dosage,
    Duration as proto___google___fhir___proto___r4___core___datatypes_pb2___Duration,
    Expression as proto___google___fhir___proto___r4___core___datatypes_pb2___Expression,
    Extension as proto___google___fhir___proto___r4___core___datatypes_pb2___Extension,
    Id as proto___google___fhir___proto___r4___core___datatypes_pb2___Id,
    Identifier as proto___google___fhir___proto___r4___core___datatypes_pb2___Identifier,
    Markdown as proto___google___fhir___proto___r4___core___datatypes_pb2___Markdown,
    Meta as proto___google___fhir___proto___r4___core___datatypes_pb2___Meta,
    Narrative as proto___google___fhir___proto___r4___core___datatypes_pb2___Narrative,
    Period as proto___google___fhir___proto___r4___core___datatypes_pb2___Period,
    Range as proto___google___fhir___proto___r4___core___datatypes_pb2___Range,
    Reference as proto___google___fhir___proto___r4___core___datatypes_pb2___Reference,
    RelatedArtifact as proto___google___fhir___proto___r4___core___datatypes_pb2___RelatedArtifact,
    SimpleQuantity as proto___google___fhir___proto___r4___core___datatypes_pb2___SimpleQuantity,
    String as proto___google___fhir___proto___r4___core___datatypes_pb2___String,
    Timing as proto___google___fhir___proto___r4___core___datatypes_pb2___Timing,
    Uri as proto___google___fhir___proto___r4___core___datatypes_pb2___Uri,
    UsageContext as proto___google___fhir___proto___r4___core___datatypes_pb2___UsageContext,
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

class ActivityDefinition(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class StatusCode(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        value: proto___google___fhir___proto___r4___core___codes_pb2___PublicationStatusCode.ValueValue = ...

        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        def __init__(self,
            *,
            value : typing___Optional[proto___google___fhir___proto___r4___core___codes_pb2___PublicationStatusCode.ValueValue] = None,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"id",b"id"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"extension",b"extension",u"id",b"id",u"value",b"value"]) -> None: ...
    type___StatusCode = StatusCode

    class SubjectX(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def codeable_concept(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

        @property
        def reference(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Reference: ...

        def __init__(self,
            *,
            codeable_concept : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
            reference : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"choice",b"choice",u"codeable_concept",b"codeable_concept",u"reference",b"reference"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"choice",b"choice",u"codeable_concept",b"codeable_concept",u"reference",b"reference"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions___Literal[u"choice",b"choice"]) -> typing_extensions___Literal["codeable_concept","reference"]: ...
    type___SubjectX = SubjectX

    class KindCode(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        value: proto___google___fhir___proto___r4___core___codes_pb2___RequestResourceTypeCode.ValueValue = ...

        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        def __init__(self,
            *,
            value : typing___Optional[proto___google___fhir___proto___r4___core___codes_pb2___RequestResourceTypeCode.ValueValue] = None,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"id",b"id"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"extension",b"extension",u"id",b"id",u"value",b"value"]) -> None: ...
    type___KindCode = KindCode

    class IntentCode(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        value: proto___google___fhir___proto___r4___core___codes_pb2___RequestIntentCode.ValueValue = ...

        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        def __init__(self,
            *,
            value : typing___Optional[proto___google___fhir___proto___r4___core___codes_pb2___RequestIntentCode.ValueValue] = None,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"id",b"id"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"extension",b"extension",u"id",b"id",u"value",b"value"]) -> None: ...
    type___IntentCode = IntentCode

    class PriorityCode(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        value: proto___google___fhir___proto___r4___core___codes_pb2___RequestPriorityCode.ValueValue = ...

        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        def __init__(self,
            *,
            value : typing___Optional[proto___google___fhir___proto___r4___core___codes_pb2___RequestPriorityCode.ValueValue] = None,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"id",b"id"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"extension",b"extension",u"id",b"id",u"value",b"value"]) -> None: ...
    type___PriorityCode = PriorityCode

    class TimingX(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def timing(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Timing: ...

        @property
        def date_time(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime: ...

        @property
        def age(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Age: ...

        @property
        def period(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Period: ...

        @property
        def range(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Range: ...

        @property
        def duration(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Duration: ...

        def __init__(self,
            *,
            timing : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Timing] = None,
            date_time : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime] = None,
            age : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Age] = None,
            period : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Period] = None,
            range : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Range] = None,
            duration : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Duration] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"age",b"age",u"choice",b"choice",u"date_time",b"date_time",u"duration",b"duration",u"period",b"period",u"range",b"range",u"timing",b"timing"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"age",b"age",u"choice",b"choice",u"date_time",b"date_time",u"duration",b"duration",u"period",b"period",u"range",b"range",u"timing",b"timing"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions___Literal[u"choice",b"choice"]) -> typing_extensions___Literal["timing","date_time","age","period","range","duration"]: ...
    type___TimingX = TimingX

    class Participant(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class TypeCode(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            value: proto___google___fhir___proto___r4___core___codes_pb2___ActionParticipantTypeCode.ValueValue = ...

            @property
            def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

            @property
            def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

            def __init__(self,
                *,
                value : typing___Optional[proto___google___fhir___proto___r4___core___codes_pb2___ActionParticipantTypeCode.ValueValue] = None,
                id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
                extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions___Literal[u"id",b"id"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"extension",b"extension",u"id",b"id",u"value",b"value"]) -> None: ...
        type___TypeCode = TypeCode


        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def modifier_extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def type(self) -> type___ActivityDefinition.Participant.TypeCode: ...

        @property
        def role(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

        def __init__(self,
            *,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            modifier_extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            type : typing___Optional[type___ActivityDefinition.Participant.TypeCode] = None,
            role : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"id",b"id",u"role",b"role",u"type",b"type"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"extension",b"extension",u"id",b"id",u"modifier_extension",b"modifier_extension",u"role",b"role",u"type",b"type"]) -> None: ...
    type___Participant = Participant

    class ProductX(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def reference(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Reference: ...

        @property
        def codeable_concept(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

        def __init__(self,
            *,
            reference : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference] = None,
            codeable_concept : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"choice",b"choice",u"codeable_concept",b"codeable_concept",u"reference",b"reference"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"choice",b"choice",u"codeable_concept",b"codeable_concept",u"reference",b"reference"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions___Literal[u"choice",b"choice"]) -> typing_extensions___Literal["reference","codeable_concept"]: ...
    type___ProductX = ProductX

    class DynamicValue(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def modifier_extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def path(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def expression(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Expression: ...

        def __init__(self,
            *,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            modifier_extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            path : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            expression : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Expression] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"expression",b"expression",u"id",b"id",u"path",b"path"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"expression",b"expression",u"extension",b"extension",u"id",b"id",u"modifier_extension",b"modifier_extension",u"path",b"path"]) -> None: ...
    type___DynamicValue = DynamicValue


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
    def url(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Uri: ...

    @property
    def identifier(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Identifier]: ...

    @property
    def version(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

    @property
    def name(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

    @property
    def title(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

    @property
    def subtitle(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

    @property
    def status(self) -> type___ActivityDefinition.StatusCode: ...

    @property
    def experimental(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Boolean: ...

    @property
    def subject(self) -> type___ActivityDefinition.SubjectX: ...

    @property
    def date(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime: ...

    @property
    def publisher(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

    @property
    def contact(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___ContactDetail]: ...

    @property
    def description(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Markdown: ...

    @property
    def use_context(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___UsageContext]: ...

    @property
    def jurisdiction(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]: ...

    @property
    def purpose(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Markdown: ...

    @property
    def usage(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

    @property
    def copyright(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Markdown: ...

    @property
    def approval_date(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Date: ...

    @property
    def last_review_date(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Date: ...

    @property
    def effective_period(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Period: ...

    @property
    def topic(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]: ...

    @property
    def author(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___ContactDetail]: ...

    @property
    def editor(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___ContactDetail]: ...

    @property
    def reviewer(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___ContactDetail]: ...

    @property
    def endorser(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___ContactDetail]: ...

    @property
    def related_artifact(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___RelatedArtifact]: ...

    @property
    def library(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Canonical]: ...

    @property
    def kind(self) -> type___ActivityDefinition.KindCode: ...

    @property
    def profile(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Canonical: ...

    @property
    def code(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

    @property
    def intent(self) -> type___ActivityDefinition.IntentCode: ...

    @property
    def priority(self) -> type___ActivityDefinition.PriorityCode: ...

    @property
    def do_not_perform(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Boolean: ...

    @property
    def timing(self) -> type___ActivityDefinition.TimingX: ...

    @property
    def location(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Reference: ...

    @property
    def participant(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___ActivityDefinition.Participant]: ...

    @property
    def product(self) -> type___ActivityDefinition.ProductX: ...

    @property
    def quantity(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___SimpleQuantity: ...

    @property
    def dosage(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Dosage]: ...

    @property
    def body_site(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]: ...

    @property
    def specimen_requirement(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]: ...

    @property
    def observation_requirement(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]: ...

    @property
    def observation_result_requirement(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]: ...

    @property
    def transform(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Canonical: ...

    @property
    def dynamic_value(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___ActivityDefinition.DynamicValue]: ...

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
        url : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Uri] = None,
        identifier : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Identifier]] = None,
        version : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
        name : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
        title : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
        subtitle : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
        status : typing___Optional[type___ActivityDefinition.StatusCode] = None,
        experimental : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Boolean] = None,
        subject : typing___Optional[type___ActivityDefinition.SubjectX] = None,
        date : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime] = None,
        publisher : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
        contact : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___ContactDetail]] = None,
        description : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Markdown] = None,
        use_context : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___UsageContext]] = None,
        jurisdiction : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]] = None,
        purpose : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Markdown] = None,
        usage : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
        copyright : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Markdown] = None,
        approval_date : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Date] = None,
        last_review_date : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Date] = None,
        effective_period : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Period] = None,
        topic : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]] = None,
        author : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___ContactDetail]] = None,
        editor : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___ContactDetail]] = None,
        reviewer : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___ContactDetail]] = None,
        endorser : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___ContactDetail]] = None,
        related_artifact : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___RelatedArtifact]] = None,
        library : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Canonical]] = None,
        kind : typing___Optional[type___ActivityDefinition.KindCode] = None,
        profile : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Canonical] = None,
        code : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
        intent : typing___Optional[type___ActivityDefinition.IntentCode] = None,
        priority : typing___Optional[type___ActivityDefinition.PriorityCode] = None,
        do_not_perform : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Boolean] = None,
        timing : typing___Optional[type___ActivityDefinition.TimingX] = None,
        location : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference] = None,
        participant : typing___Optional[typing___Iterable[type___ActivityDefinition.Participant]] = None,
        product : typing___Optional[type___ActivityDefinition.ProductX] = None,
        quantity : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___SimpleQuantity] = None,
        dosage : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Dosage]] = None,
        body_site : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]] = None,
        specimen_requirement : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]] = None,
        observation_requirement : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]] = None,
        observation_result_requirement : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]] = None,
        transform : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Canonical] = None,
        dynamic_value : typing___Optional[typing___Iterable[type___ActivityDefinition.DynamicValue]] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"approval_date",b"approval_date",u"code",b"code",u"copyright",b"copyright",u"date",b"date",u"description",b"description",u"do_not_perform",b"do_not_perform",u"effective_period",b"effective_period",u"experimental",b"experimental",u"id",b"id",u"implicit_rules",b"implicit_rules",u"intent",b"intent",u"kind",b"kind",u"language",b"language",u"last_review_date",b"last_review_date",u"location",b"location",u"meta",b"meta",u"name",b"name",u"priority",b"priority",u"product",b"product",u"profile",b"profile",u"publisher",b"publisher",u"purpose",b"purpose",u"quantity",b"quantity",u"status",b"status",u"subject",b"subject",u"subtitle",b"subtitle",u"text",b"text",u"timing",b"timing",u"title",b"title",u"transform",b"transform",u"url",b"url",u"usage",b"usage",u"version",b"version"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"approval_date",b"approval_date",u"author",b"author",u"body_site",b"body_site",u"code",b"code",u"contact",b"contact",u"contained",b"contained",u"copyright",b"copyright",u"date",b"date",u"description",b"description",u"do_not_perform",b"do_not_perform",u"dosage",b"dosage",u"dynamic_value",b"dynamic_value",u"editor",b"editor",u"effective_period",b"effective_period",u"endorser",b"endorser",u"experimental",b"experimental",u"extension",b"extension",u"id",b"id",u"identifier",b"identifier",u"implicit_rules",b"implicit_rules",u"intent",b"intent",u"jurisdiction",b"jurisdiction",u"kind",b"kind",u"language",b"language",u"last_review_date",b"last_review_date",u"library",b"library",u"location",b"location",u"meta",b"meta",u"modifier_extension",b"modifier_extension",u"name",b"name",u"observation_requirement",b"observation_requirement",u"observation_result_requirement",b"observation_result_requirement",u"participant",b"participant",u"priority",b"priority",u"product",b"product",u"profile",b"profile",u"publisher",b"publisher",u"purpose",b"purpose",u"quantity",b"quantity",u"related_artifact",b"related_artifact",u"reviewer",b"reviewer",u"specimen_requirement",b"specimen_requirement",u"status",b"status",u"subject",b"subject",u"subtitle",b"subtitle",u"text",b"text",u"timing",b"timing",u"title",b"title",u"topic",b"topic",u"transform",b"transform",u"url",b"url",u"usage",b"usage",u"use_context",b"use_context",u"version",b"version"]) -> None: ...
type___ActivityDefinition = ActivityDefinition
