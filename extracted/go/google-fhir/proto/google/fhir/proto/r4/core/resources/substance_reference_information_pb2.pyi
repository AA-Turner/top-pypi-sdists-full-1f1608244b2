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
    Identifier as proto___google___fhir___proto___r4___core___datatypes_pb2___Identifier,
    Meta as proto___google___fhir___proto___r4___core___datatypes_pb2___Meta,
    Narrative as proto___google___fhir___proto___r4___core___datatypes_pb2___Narrative,
    Quantity as proto___google___fhir___proto___r4___core___datatypes_pb2___Quantity,
    Range as proto___google___fhir___proto___r4___core___datatypes_pb2___Range,
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

class SubstanceReferenceInformation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Gene(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def modifier_extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def gene_sequence_origin(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

        @property
        def gene(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

        @property
        def source(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]: ...

        def __init__(self,
            *,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            modifier_extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            gene_sequence_origin : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
            gene : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
            source : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"gene",b"gene",u"gene_sequence_origin",b"gene_sequence_origin",u"id",b"id"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"extension",b"extension",u"gene",b"gene",u"gene_sequence_origin",b"gene_sequence_origin",u"id",b"id",u"modifier_extension",b"modifier_extension",u"source",b"source"]) -> None: ...
    type___Gene = Gene

    class GeneElement(google___protobuf___message___Message):
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
        def element(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Identifier: ...

        @property
        def source(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]: ...

        def __init__(self,
            *,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            modifier_extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            type : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
            element : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Identifier] = None,
            source : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"element",b"element",u"id",b"id",u"type",b"type"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"element",b"element",u"extension",b"extension",u"id",b"id",u"modifier_extension",b"modifier_extension",u"source",b"source",u"type",b"type"]) -> None: ...
    type___GeneElement = GeneElement

    class Classification(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def modifier_extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def domain(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

        @property
        def classification(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

        @property
        def subtype(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]: ...

        @property
        def source(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]: ...

        def __init__(self,
            *,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            modifier_extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            domain : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
            classification : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
            subtype : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]] = None,
            source : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"classification",b"classification",u"domain",b"domain",u"id",b"id"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"classification",b"classification",u"domain",b"domain",u"extension",b"extension",u"id",b"id",u"modifier_extension",b"modifier_extension",u"source",b"source",u"subtype",b"subtype"]) -> None: ...
    type___Classification = Classification

    class Target(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class AmountX(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

            @property
            def quantity(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Quantity: ...

            @property
            def range(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Range: ...

            @property
            def string_value(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

            def __init__(self,
                *,
                quantity : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Quantity] = None,
                range : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Range] = None,
                string_value : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions___Literal[u"choice",b"choice",u"quantity",b"quantity",u"range",b"range",u"string_value",b"string_value"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"choice",b"choice",u"quantity",b"quantity",u"range",b"range",u"string_value",b"string_value"]) -> None: ...
            def WhichOneof(self, oneof_group: typing_extensions___Literal[u"choice",b"choice"]) -> typing_extensions___Literal["quantity","range","string_value"]: ...
        type___AmountX = AmountX


        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def modifier_extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def target(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Identifier: ...

        @property
        def type(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

        @property
        def interaction(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

        @property
        def organism(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

        @property
        def organism_type(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

        @property
        def amount(self) -> type___SubstanceReferenceInformation.Target.AmountX: ...

        @property
        def amount_type(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

        @property
        def source(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]: ...

        def __init__(self,
            *,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            modifier_extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            target : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Identifier] = None,
            type : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
            interaction : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
            organism : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
            organism_type : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
            amount : typing___Optional[type___SubstanceReferenceInformation.Target.AmountX] = None,
            amount_type : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
            source : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"amount",b"amount",u"amount_type",b"amount_type",u"id",b"id",u"interaction",b"interaction",u"organism",b"organism",u"organism_type",b"organism_type",u"target",b"target",u"type",b"type"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"amount",b"amount",u"amount_type",b"amount_type",u"extension",b"extension",u"id",b"id",u"interaction",b"interaction",u"modifier_extension",b"modifier_extension",u"organism",b"organism",u"organism_type",b"organism_type",u"source",b"source",u"target",b"target",u"type",b"type"]) -> None: ...
    type___Target = Target


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
    def comment(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

    @property
    def gene(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___SubstanceReferenceInformation.Gene]: ...

    @property
    def gene_element(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___SubstanceReferenceInformation.GeneElement]: ...

    @property
    def classification(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___SubstanceReferenceInformation.Classification]: ...

    @property
    def target(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___SubstanceReferenceInformation.Target]: ...

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
        comment : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
        gene : typing___Optional[typing___Iterable[type___SubstanceReferenceInformation.Gene]] = None,
        gene_element : typing___Optional[typing___Iterable[type___SubstanceReferenceInformation.GeneElement]] = None,
        classification : typing___Optional[typing___Iterable[type___SubstanceReferenceInformation.Classification]] = None,
        target : typing___Optional[typing___Iterable[type___SubstanceReferenceInformation.Target]] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"comment",b"comment",u"id",b"id",u"implicit_rules",b"implicit_rules",u"language",b"language",u"meta",b"meta",u"text",b"text"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"classification",b"classification",u"comment",b"comment",u"contained",b"contained",u"extension",b"extension",u"gene",b"gene",u"gene_element",b"gene_element",u"id",b"id",u"implicit_rules",b"implicit_rules",u"language",b"language",u"meta",b"meta",u"modifier_extension",b"modifier_extension",u"target",b"target",u"text",b"text"]) -> None: ...
type___SubstanceReferenceInformation = SubstanceReferenceInformation
