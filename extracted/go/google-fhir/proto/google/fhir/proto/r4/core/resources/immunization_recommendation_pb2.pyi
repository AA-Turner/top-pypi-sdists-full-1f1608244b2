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
    DateTime as proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime,
    Extension as proto___google___fhir___proto___r4___core___datatypes_pb2___Extension,
    Id as proto___google___fhir___proto___r4___core___datatypes_pb2___Id,
    Identifier as proto___google___fhir___proto___r4___core___datatypes_pb2___Identifier,
    Meta as proto___google___fhir___proto___r4___core___datatypes_pb2___Meta,
    Narrative as proto___google___fhir___proto___r4___core___datatypes_pb2___Narrative,
    PositiveInt as proto___google___fhir___proto___r4___core___datatypes_pb2___PositiveInt,
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

class ImmunizationRecommendation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Recommendation(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class DateCriterion(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

            @property
            def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

            @property
            def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

            @property
            def modifier_extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

            @property
            def code(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

            @property
            def value(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime: ...

            def __init__(self,
                *,
                id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
                extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
                modifier_extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
                code : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
                value : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime] = None,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions___Literal[u"code",b"code",u"id",b"id",u"value",b"value"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"extension",b"extension",u"id",b"id",u"modifier_extension",b"modifier_extension",u"value",b"value"]) -> None: ...
        type___DateCriterion = DateCriterion

        class DoseNumberX(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

            @property
            def positive_int(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___PositiveInt: ...

            @property
            def string_value(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

            def __init__(self,
                *,
                positive_int : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___PositiveInt] = None,
                string_value : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions___Literal[u"choice",b"choice",u"positive_int",b"positive_int",u"string_value",b"string_value"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"choice",b"choice",u"positive_int",b"positive_int",u"string_value",b"string_value"]) -> None: ...
            def WhichOneof(self, oneof_group: typing_extensions___Literal[u"choice",b"choice"]) -> typing_extensions___Literal["positive_int","string_value"]: ...
        type___DoseNumberX = DoseNumberX

        class SeriesDosesX(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

            @property
            def positive_int(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___PositiveInt: ...

            @property
            def string_value(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

            def __init__(self,
                *,
                positive_int : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___PositiveInt] = None,
                string_value : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions___Literal[u"choice",b"choice",u"positive_int",b"positive_int",u"string_value",b"string_value"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"choice",b"choice",u"positive_int",b"positive_int",u"string_value",b"string_value"]) -> None: ...
            def WhichOneof(self, oneof_group: typing_extensions___Literal[u"choice",b"choice"]) -> typing_extensions___Literal["positive_int","string_value"]: ...
        type___SeriesDosesX = SeriesDosesX


        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def modifier_extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def vaccine_code(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]: ...

        @property
        def target_disease(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

        @property
        def contraindicated_vaccine_code(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]: ...

        @property
        def forecast_status(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

        @property
        def forecast_reason(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]: ...

        @property
        def date_criterion(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___ImmunizationRecommendation.Recommendation.DateCriterion]: ...

        @property
        def description(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def series(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def dose_number(self) -> type___ImmunizationRecommendation.Recommendation.DoseNumberX: ...

        @property
        def series_doses(self) -> type___ImmunizationRecommendation.Recommendation.SeriesDosesX: ...

        @property
        def supporting_immunization(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]: ...

        @property
        def supporting_patient_information(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]: ...

        def __init__(self,
            *,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            modifier_extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            vaccine_code : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]] = None,
            target_disease : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
            contraindicated_vaccine_code : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]] = None,
            forecast_status : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
            forecast_reason : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]] = None,
            date_criterion : typing___Optional[typing___Iterable[type___ImmunizationRecommendation.Recommendation.DateCriterion]] = None,
            description : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            series : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            dose_number : typing___Optional[type___ImmunizationRecommendation.Recommendation.DoseNumberX] = None,
            series_doses : typing___Optional[type___ImmunizationRecommendation.Recommendation.SeriesDosesX] = None,
            supporting_immunization : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]] = None,
            supporting_patient_information : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"description",b"description",u"dose_number",b"dose_number",u"forecast_status",b"forecast_status",u"id",b"id",u"series",b"series",u"series_doses",b"series_doses",u"target_disease",b"target_disease"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"contraindicated_vaccine_code",b"contraindicated_vaccine_code",u"date_criterion",b"date_criterion",u"description",b"description",u"dose_number",b"dose_number",u"extension",b"extension",u"forecast_reason",b"forecast_reason",u"forecast_status",b"forecast_status",u"id",b"id",u"modifier_extension",b"modifier_extension",u"series",b"series",u"series_doses",b"series_doses",u"supporting_immunization",b"supporting_immunization",u"supporting_patient_information",b"supporting_patient_information",u"target_disease",b"target_disease",u"vaccine_code",b"vaccine_code"]) -> None: ...
    type___Recommendation = Recommendation


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
    def patient(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Reference: ...

    @property
    def date(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime: ...

    @property
    def authority(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Reference: ...

    @property
    def recommendation(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___ImmunizationRecommendation.Recommendation]: ...

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
        patient : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference] = None,
        date : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime] = None,
        authority : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference] = None,
        recommendation : typing___Optional[typing___Iterable[type___ImmunizationRecommendation.Recommendation]] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"authority",b"authority",u"date",b"date",u"id",b"id",u"implicit_rules",b"implicit_rules",u"language",b"language",u"meta",b"meta",u"patient",b"patient",u"text",b"text"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"authority",b"authority",u"contained",b"contained",u"date",b"date",u"extension",b"extension",u"id",b"id",u"identifier",b"identifier",u"implicit_rules",b"implicit_rules",u"language",b"language",u"meta",b"meta",u"modifier_extension",b"modifier_extension",u"patient",b"patient",u"recommendation",b"recommendation",u"text",b"text"]) -> None: ...
type___ImmunizationRecommendation = ImmunizationRecommendation
