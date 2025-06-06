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
    FinancialResourceStatusCode as proto___google___fhir___proto___r4___core___codes_pb2___FinancialResourceStatusCode,
    VisionBaseCode as proto___google___fhir___proto___r4___core___codes_pb2___VisionBaseCode,
    VisionEyesCode as proto___google___fhir___proto___r4___core___codes_pb2___VisionEyesCode,
)

from proto.google.fhir.proto.r4.core.datatypes_pb2 import (
    Annotation as proto___google___fhir___proto___r4___core___datatypes_pb2___Annotation,
    Code as proto___google___fhir___proto___r4___core___datatypes_pb2___Code,
    CodeableConcept as proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept,
    DateTime as proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime,
    Decimal as proto___google___fhir___proto___r4___core___datatypes_pb2___Decimal,
    Extension as proto___google___fhir___proto___r4___core___datatypes_pb2___Extension,
    Id as proto___google___fhir___proto___r4___core___datatypes_pb2___Id,
    Identifier as proto___google___fhir___proto___r4___core___datatypes_pb2___Identifier,
    Integer as proto___google___fhir___proto___r4___core___datatypes_pb2___Integer,
    Meta as proto___google___fhir___proto___r4___core___datatypes_pb2___Meta,
    Narrative as proto___google___fhir___proto___r4___core___datatypes_pb2___Narrative,
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

class VisionPrescription(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class StatusCode(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        value: proto___google___fhir___proto___r4___core___codes_pb2___FinancialResourceStatusCode.ValueValue = ...

        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        def __init__(self,
            *,
            value : typing___Optional[proto___google___fhir___proto___r4___core___codes_pb2___FinancialResourceStatusCode.ValueValue] = None,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"id",b"id"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"extension",b"extension",u"id",b"id",u"value",b"value"]) -> None: ...
    type___StatusCode = StatusCode

    class LensSpecification(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class EyeCode(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            value: proto___google___fhir___proto___r4___core___codes_pb2___VisionEyesCode.ValueValue = ...

            @property
            def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

            @property
            def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

            def __init__(self,
                *,
                value : typing___Optional[proto___google___fhir___proto___r4___core___codes_pb2___VisionEyesCode.ValueValue] = None,
                id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
                extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions___Literal[u"id",b"id"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"extension",b"extension",u"id",b"id",u"value",b"value"]) -> None: ...
        type___EyeCode = EyeCode

        class Prism(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            class BaseCode(google___protobuf___message___Message):
                DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
                value: proto___google___fhir___proto___r4___core___codes_pb2___VisionBaseCode.ValueValue = ...

                @property
                def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

                @property
                def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

                def __init__(self,
                    *,
                    value : typing___Optional[proto___google___fhir___proto___r4___core___codes_pb2___VisionBaseCode.ValueValue] = None,
                    id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
                    extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
                    ) -> None: ...
                def HasField(self, field_name: typing_extensions___Literal[u"id",b"id"]) -> builtin___bool: ...
                def ClearField(self, field_name: typing_extensions___Literal[u"extension",b"extension",u"id",b"id",u"value",b"value"]) -> None: ...
            type___BaseCode = BaseCode


            @property
            def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

            @property
            def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

            @property
            def modifier_extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

            @property
            def amount(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Decimal: ...

            @property
            def base(self) -> type___VisionPrescription.LensSpecification.Prism.BaseCode: ...

            def __init__(self,
                *,
                id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
                extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
                modifier_extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
                amount : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Decimal] = None,
                base : typing___Optional[type___VisionPrescription.LensSpecification.Prism.BaseCode] = None,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions___Literal[u"amount",b"amount",u"base",b"base",u"id",b"id"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"amount",b"amount",u"base",b"base",u"extension",b"extension",u"id",b"id",u"modifier_extension",b"modifier_extension"]) -> None: ...
        type___Prism = Prism


        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def modifier_extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def product(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

        @property
        def eye(self) -> type___VisionPrescription.LensSpecification.EyeCode: ...

        @property
        def sphere(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Decimal: ...

        @property
        def cylinder(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Decimal: ...

        @property
        def axis(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Integer: ...

        @property
        def prism(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___VisionPrescription.LensSpecification.Prism]: ...

        @property
        def add(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Decimal: ...

        @property
        def power(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Decimal: ...

        @property
        def back_curve(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Decimal: ...

        @property
        def diameter(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Decimal: ...

        @property
        def duration(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___SimpleQuantity: ...

        @property
        def color(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def brand(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def note(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Annotation]: ...

        def __init__(self,
            *,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            modifier_extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            product : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
            eye : typing___Optional[type___VisionPrescription.LensSpecification.EyeCode] = None,
            sphere : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Decimal] = None,
            cylinder : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Decimal] = None,
            axis : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Integer] = None,
            prism : typing___Optional[typing___Iterable[type___VisionPrescription.LensSpecification.Prism]] = None,
            add : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Decimal] = None,
            power : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Decimal] = None,
            back_curve : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Decimal] = None,
            diameter : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Decimal] = None,
            duration : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___SimpleQuantity] = None,
            color : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            brand : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            note : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Annotation]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"add",b"add",u"axis",b"axis",u"back_curve",b"back_curve",u"brand",b"brand",u"color",b"color",u"cylinder",b"cylinder",u"diameter",b"diameter",u"duration",b"duration",u"eye",b"eye",u"id",b"id",u"power",b"power",u"product",b"product",u"sphere",b"sphere"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"add",b"add",u"axis",b"axis",u"back_curve",b"back_curve",u"brand",b"brand",u"color",b"color",u"cylinder",b"cylinder",u"diameter",b"diameter",u"duration",b"duration",u"extension",b"extension",u"eye",b"eye",u"id",b"id",u"modifier_extension",b"modifier_extension",u"note",b"note",u"power",b"power",u"prism",b"prism",u"product",b"product",u"sphere",b"sphere"]) -> None: ...
    type___LensSpecification = LensSpecification


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
    def status(self) -> type___VisionPrescription.StatusCode: ...

    @property
    def created(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime: ...

    @property
    def patient(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Reference: ...

    @property
    def encounter(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Reference: ...

    @property
    def date_written(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime: ...

    @property
    def prescriber(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Reference: ...

    @property
    def lens_specification(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___VisionPrescription.LensSpecification]: ...

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
        status : typing___Optional[type___VisionPrescription.StatusCode] = None,
        created : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime] = None,
        patient : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference] = None,
        encounter : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference] = None,
        date_written : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime] = None,
        prescriber : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference] = None,
        lens_specification : typing___Optional[typing___Iterable[type___VisionPrescription.LensSpecification]] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"created",b"created",u"date_written",b"date_written",u"encounter",b"encounter",u"id",b"id",u"implicit_rules",b"implicit_rules",u"language",b"language",u"meta",b"meta",u"patient",b"patient",u"prescriber",b"prescriber",u"status",b"status",u"text",b"text"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"contained",b"contained",u"created",b"created",u"date_written",b"date_written",u"encounter",b"encounter",u"extension",b"extension",u"id",b"id",u"identifier",b"identifier",u"implicit_rules",b"implicit_rules",u"language",b"language",u"lens_specification",b"lens_specification",u"meta",b"meta",u"modifier_extension",b"modifier_extension",u"patient",b"patient",u"prescriber",b"prescriber",u"status",b"status",u"text",b"text"]) -> None: ...
type___VisionPrescription = VisionPrescription
