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
    ObservationStatusCode as proto___google___fhir___proto___r4___core___codes_pb2___ObservationStatusCode,
)

from proto.google.fhir.proto.r4.core.datatypes_pb2 import (
    Annotation as proto___google___fhir___proto___r4___core___datatypes_pb2___Annotation,
    Boolean as proto___google___fhir___proto___r4___core___datatypes_pb2___Boolean,
    Code as proto___google___fhir___proto___r4___core___datatypes_pb2___Code,
    CodeableConcept as proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept,
    DateTime as proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime,
    Extension as proto___google___fhir___proto___r4___core___datatypes_pb2___Extension,
    Id as proto___google___fhir___proto___r4___core___datatypes_pb2___Id,
    Identifier as proto___google___fhir___proto___r4___core___datatypes_pb2___Identifier,
    Instant as proto___google___fhir___proto___r4___core___datatypes_pb2___Instant,
    Integer as proto___google___fhir___proto___r4___core___datatypes_pb2___Integer,
    Meta as proto___google___fhir___proto___r4___core___datatypes_pb2___Meta,
    Narrative as proto___google___fhir___proto___r4___core___datatypes_pb2___Narrative,
    Period as proto___google___fhir___proto___r4___core___datatypes_pb2___Period,
    Quantity as proto___google___fhir___proto___r4___core___datatypes_pb2___Quantity,
    Range as proto___google___fhir___proto___r4___core___datatypes_pb2___Range,
    Ratio as proto___google___fhir___proto___r4___core___datatypes_pb2___Ratio,
    Reference as proto___google___fhir___proto___r4___core___datatypes_pb2___Reference,
    SampledData as proto___google___fhir___proto___r4___core___datatypes_pb2___SampledData,
    SimpleQuantity as proto___google___fhir___proto___r4___core___datatypes_pb2___SimpleQuantity,
    String as proto___google___fhir___proto___r4___core___datatypes_pb2___String,
    Time as proto___google___fhir___proto___r4___core___datatypes_pb2___Time,
    Timing as proto___google___fhir___proto___r4___core___datatypes_pb2___Timing,
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

class Cholesterol(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class StatusCode(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        value: proto___google___fhir___proto___r4___core___codes_pb2___ObservationStatusCode.ValueValue = ...

        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        def __init__(self,
            *,
            value : typing___Optional[proto___google___fhir___proto___r4___core___codes_pb2___ObservationStatusCode.ValueValue] = None,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"id",b"id"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"extension",b"extension",u"id",b"id",u"value",b"value"]) -> None: ...
    type___StatusCode = StatusCode

    class EffectiveX(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def date_time(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime: ...

        @property
        def period(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Period: ...

        @property
        def timing(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Timing: ...

        @property
        def instant(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Instant: ...

        def __init__(self,
            *,
            date_time : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime] = None,
            period : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Period] = None,
            timing : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Timing] = None,
            instant : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Instant] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"choice",b"choice",u"date_time",b"date_time",u"instant",b"instant",u"period",b"period",u"timing",b"timing"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"choice",b"choice",u"date_time",b"date_time",u"instant",b"instant",u"period",b"period",u"timing",b"timing"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions___Literal[u"choice",b"choice"]) -> typing_extensions___Literal["date_time","period","timing","instant"]: ...
    type___EffectiveX = EffectiveX

    class ValueX(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def quantity(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Quantity: ...

        def __init__(self,
            *,
            quantity : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Quantity] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"choice",b"choice",u"quantity",b"quantity"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"choice",b"choice",u"quantity",b"quantity"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions___Literal[u"choice",b"choice"]) -> typing_extensions___Literal["quantity"]: ...
    type___ValueX = ValueX

    class ReferenceRange(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def modifier_extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def high(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___SimpleQuantity: ...

        @property
        def text(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        def __init__(self,
            *,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            modifier_extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            high : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___SimpleQuantity] = None,
            text : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"high",b"high",u"id",b"id",u"text",b"text"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"extension",b"extension",u"high",b"high",u"id",b"id",u"modifier_extension",b"modifier_extension",u"text",b"text"]) -> None: ...
    type___ReferenceRange = ReferenceRange

    class Component(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class ValueX(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

            @property
            def quantity(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Quantity: ...

            @property
            def codeable_concept(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

            @property
            def string_value(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

            @property
            def boolean(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Boolean: ...

            @property
            def integer(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Integer: ...

            @property
            def range(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Range: ...

            @property
            def ratio(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Ratio: ...

            @property
            def sampled_data(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___SampledData: ...

            @property
            def time(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Time: ...

            @property
            def date_time(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime: ...

            @property
            def period(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Period: ...

            def __init__(self,
                *,
                quantity : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Quantity] = None,
                codeable_concept : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
                string_value : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
                boolean : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Boolean] = None,
                integer : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Integer] = None,
                range : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Range] = None,
                ratio : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Ratio] = None,
                sampled_data : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___SampledData] = None,
                time : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Time] = None,
                date_time : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime] = None,
                period : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Period] = None,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions___Literal[u"boolean",b"boolean",u"choice",b"choice",u"codeable_concept",b"codeable_concept",u"date_time",b"date_time",u"integer",b"integer",u"period",b"period",u"quantity",b"quantity",u"range",b"range",u"ratio",b"ratio",u"sampled_data",b"sampled_data",u"string_value",b"string_value",u"time",b"time"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"boolean",b"boolean",u"choice",b"choice",u"codeable_concept",b"codeable_concept",u"date_time",b"date_time",u"integer",b"integer",u"period",b"period",u"quantity",b"quantity",u"range",b"range",u"ratio",b"ratio",u"sampled_data",b"sampled_data",u"string_value",b"string_value",u"time",b"time"]) -> None: ...
            def WhichOneof(self, oneof_group: typing_extensions___Literal[u"choice",b"choice"]) -> typing_extensions___Literal["quantity","codeable_concept","string_value","boolean","integer","range","ratio","sampled_data","time","date_time","period"]: ...
        type___ValueX = ValueX


        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def modifier_extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def code(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

        @property
        def value(self) -> type___Cholesterol.Component.ValueX: ...

        @property
        def data_absent_reason(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

        @property
        def interpretation(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]: ...

        @property
        def reference_range(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___Cholesterol.ReferenceRange]: ...

        def __init__(self,
            *,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            modifier_extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            code : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
            value : typing___Optional[type___Cholesterol.Component.ValueX] = None,
            data_absent_reason : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
            interpretation : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]] = None,
            reference_range : typing___Optional[typing___Iterable[type___Cholesterol.ReferenceRange]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"code",b"code",u"data_absent_reason",b"data_absent_reason",u"id",b"id",u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"data_absent_reason",b"data_absent_reason",u"extension",b"extension",u"id",b"id",u"interpretation",b"interpretation",u"modifier_extension",b"modifier_extension",u"reference_range",b"reference_range",u"value",b"value"]) -> None: ...
    type___Component = Component


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
    def identifier(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Identifier]: ...

    @property
    def based_on(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]: ...

    @property
    def part_of(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]: ...

    @property
    def status(self) -> type___Cholesterol.StatusCode: ...

    @property
    def category(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]: ...

    @property
    def code(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

    @property
    def subject(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Reference: ...

    @property
    def focus(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]: ...

    @property
    def encounter(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Reference: ...

    @property
    def effective(self) -> type___Cholesterol.EffectiveX: ...

    @property
    def issued(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Instant: ...

    @property
    def performer(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]: ...

    @property
    def value(self) -> type___Cholesterol.ValueX: ...

    @property
    def data_absent_reason(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

    @property
    def interpretation(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

    @property
    def note(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Annotation]: ...

    @property
    def body_site(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

    @property
    def method(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

    @property
    def specimen(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Reference: ...

    @property
    def device(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Reference: ...

    @property
    def reference_range(self) -> type___Cholesterol.ReferenceRange: ...

    @property
    def component(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___Cholesterol.Component]: ...

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
        identifier : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Identifier]] = None,
        based_on : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]] = None,
        part_of : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]] = None,
        status : typing___Optional[type___Cholesterol.StatusCode] = None,
        category : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]] = None,
        code : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
        subject : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference] = None,
        focus : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]] = None,
        encounter : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference] = None,
        effective : typing___Optional[type___Cholesterol.EffectiveX] = None,
        issued : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Instant] = None,
        performer : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]] = None,
        value : typing___Optional[type___Cholesterol.ValueX] = None,
        data_absent_reason : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
        interpretation : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
        note : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Annotation]] = None,
        body_site : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
        method : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
        specimen : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference] = None,
        device : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference] = None,
        reference_range : typing___Optional[type___Cholesterol.ReferenceRange] = None,
        component : typing___Optional[typing___Iterable[type___Cholesterol.Component]] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"body_site",b"body_site",u"code",b"code",u"data_absent_reason",b"data_absent_reason",u"device",b"device",u"effective",b"effective",u"encounter",b"encounter",u"id",b"id",u"implicit_rules",b"implicit_rules",u"interpretation",b"interpretation",u"issued",b"issued",u"language",b"language",u"meta",b"meta",u"method",b"method",u"reference_range",b"reference_range",u"specimen",b"specimen",u"status",b"status",u"subject",b"subject",u"text",b"text",u"value",b"value"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"based_on",b"based_on",u"body_site",b"body_site",u"category",b"category",u"code",b"code",u"component",b"component",u"contained",b"contained",u"data_absent_reason",b"data_absent_reason",u"device",b"device",u"effective",b"effective",u"encounter",b"encounter",u"extension",b"extension",u"focus",b"focus",u"id",b"id",u"identifier",b"identifier",u"implicit_rules",b"implicit_rules",u"interpretation",b"interpretation",u"issued",b"issued",u"language",b"language",u"meta",b"meta",u"method",b"method",u"modifier_extension",b"modifier_extension",u"note",b"note",u"part_of",b"part_of",u"performer",b"performer",u"reference_range",b"reference_range",u"specimen",b"specimen",u"status",b"status",u"subject",b"subject",u"text",b"text",u"value",b"value"]) -> None: ...
type___Cholesterol = Cholesterol
