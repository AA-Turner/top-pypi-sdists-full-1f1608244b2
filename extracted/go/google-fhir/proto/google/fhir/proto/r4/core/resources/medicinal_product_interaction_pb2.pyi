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

from proto.google.fhir.proto.r4.core.datatypes_pb2 import (
    Code as proto___google___fhir___proto___r4___core___datatypes_pb2___Code,
    CodeableConcept as proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept,
    Extension as proto___google___fhir___proto___r4___core___datatypes_pb2___Extension,
    Id as proto___google___fhir___proto___r4___core___datatypes_pb2___Id,
    Meta as proto___google___fhir___proto___r4___core___datatypes_pb2___Meta,
    Narrative as proto___google___fhir___proto___r4___core___datatypes_pb2___Narrative,
    Reference as proto___google___fhir___proto___r4___core___datatypes_pb2___Reference,
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

class MedicinalProductInteraction(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Interactant(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class ItemX(google___protobuf___message___Message):
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
        type___ItemX = ItemX


        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def modifier_extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def item(self) -> type___MedicinalProductInteraction.Interactant.ItemX: ...

        def __init__(self,
            *,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            modifier_extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            item : typing___Optional[type___MedicinalProductInteraction.Interactant.ItemX] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"id",b"id",u"item",b"item"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"extension",b"extension",u"id",b"id",u"item",b"item",u"modifier_extension",b"modifier_extension"]) -> None: ...
    type___Interactant = Interactant


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
    def subject(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]: ...

    @property
    def description(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

    @property
    def interactant(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___MedicinalProductInteraction.Interactant]: ...

    @property
    def type(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

    @property
    def effect(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

    @property
    def incidence(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

    @property
    def management(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

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
        subject : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]] = None,
        description : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
        interactant : typing___Optional[typing___Iterable[type___MedicinalProductInteraction.Interactant]] = None,
        type : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
        effect : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
        incidence : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
        management : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"description",b"description",u"effect",b"effect",u"id",b"id",u"implicit_rules",b"implicit_rules",u"incidence",b"incidence",u"language",b"language",u"management",b"management",u"meta",b"meta",u"text",b"text",u"type",b"type"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"contained",b"contained",u"description",b"description",u"effect",b"effect",u"extension",b"extension",u"id",b"id",u"implicit_rules",b"implicit_rules",u"incidence",b"incidence",u"interactant",b"interactant",u"language",b"language",u"management",b"management",u"meta",b"meta",u"modifier_extension",b"modifier_extension",u"subject",b"subject",u"text",b"text",u"type",b"type"]) -> None: ...
type___MedicinalProductInteraction = MedicinalProductInteraction
