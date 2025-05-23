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
    FHIRSubstanceStatusCode as proto___google___fhir___proto___r4___core___codes_pb2___FHIRSubstanceStatusCode,
)

from proto.google.fhir.proto.r4.core.datatypes_pb2 import (
    Code as proto___google___fhir___proto___r4___core___datatypes_pb2___Code,
    CodeableConcept as proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept,
    DateTime as proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime,
    Extension as proto___google___fhir___proto___r4___core___datatypes_pb2___Extension,
    Id as proto___google___fhir___proto___r4___core___datatypes_pb2___Id,
    Identifier as proto___google___fhir___proto___r4___core___datatypes_pb2___Identifier,
    Meta as proto___google___fhir___proto___r4___core___datatypes_pb2___Meta,
    Narrative as proto___google___fhir___proto___r4___core___datatypes_pb2___Narrative,
    Ratio as proto___google___fhir___proto___r4___core___datatypes_pb2___Ratio,
    Reference as proto___google___fhir___proto___r4___core___datatypes_pb2___Reference,
    SimpleQuantity as proto___google___fhir___proto___r4___core___datatypes_pb2___SimpleQuantity,
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

class Substance(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class StatusCode(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        value: proto___google___fhir___proto___r4___core___codes_pb2___FHIRSubstanceStatusCode.ValueValue = ...

        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        def __init__(self,
            *,
            value : typing___Optional[proto___google___fhir___proto___r4___core___codes_pb2___FHIRSubstanceStatusCode.ValueValue] = None,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"id",b"id"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"extension",b"extension",u"id",b"id",u"value",b"value"]) -> None: ...
    type___StatusCode = StatusCode

    class Instance(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def modifier_extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def identifier(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Identifier: ...

        @property
        def expiry(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime: ...

        @property
        def quantity(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___SimpleQuantity: ...

        def __init__(self,
            *,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            modifier_extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            identifier : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Identifier] = None,
            expiry : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime] = None,
            quantity : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___SimpleQuantity] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"expiry",b"expiry",u"id",b"id",u"identifier",b"identifier",u"quantity",b"quantity"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"expiry",b"expiry",u"extension",b"extension",u"id",b"id",u"identifier",b"identifier",u"modifier_extension",b"modifier_extension",u"quantity",b"quantity"]) -> None: ...
    type___Instance = Instance

    class Ingredient(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class SubstanceX(google___protobuf___message___Message):
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
        type___SubstanceX = SubstanceX


        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def modifier_extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def quantity(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Ratio: ...

        @property
        def substance(self) -> type___Substance.Ingredient.SubstanceX: ...

        def __init__(self,
            *,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            modifier_extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            quantity : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Ratio] = None,
            substance : typing___Optional[type___Substance.Ingredient.SubstanceX] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"id",b"id",u"quantity",b"quantity",u"substance",b"substance"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"extension",b"extension",u"id",b"id",u"modifier_extension",b"modifier_extension",u"quantity",b"quantity",u"substance",b"substance"]) -> None: ...
    type___Ingredient = Ingredient


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
    def status(self) -> type___Substance.StatusCode: ...

    @property
    def category(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]: ...

    @property
    def code(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

    @property
    def description(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

    @property
    def instance(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___Substance.Instance]: ...

    @property
    def ingredient(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___Substance.Ingredient]: ...

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
        status : typing___Optional[type___Substance.StatusCode] = None,
        category : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]] = None,
        code : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
        description : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
        instance : typing___Optional[typing___Iterable[type___Substance.Instance]] = None,
        ingredient : typing___Optional[typing___Iterable[type___Substance.Ingredient]] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"code",b"code",u"description",b"description",u"id",b"id",u"implicit_rules",b"implicit_rules",u"language",b"language",u"meta",b"meta",u"status",b"status",u"text",b"text"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"category",b"category",u"code",b"code",u"contained",b"contained",u"description",b"description",u"extension",b"extension",u"id",b"id",u"identifier",b"identifier",u"implicit_rules",b"implicit_rules",u"ingredient",b"ingredient",u"instance",b"instance",u"language",b"language",u"meta",b"meta",u"modifier_extension",b"modifier_extension",u"status",b"status",u"text",b"text"]) -> None: ...
type___Substance = Substance
