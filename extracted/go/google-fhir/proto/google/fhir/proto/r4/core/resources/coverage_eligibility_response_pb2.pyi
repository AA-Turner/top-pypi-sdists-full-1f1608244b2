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
    ClaimProcessingCode as proto___google___fhir___proto___r4___core___codes_pb2___ClaimProcessingCode,
    EligibilityResponsePurposeCode as proto___google___fhir___proto___r4___core___codes_pb2___EligibilityResponsePurposeCode,
    FinancialResourceStatusCode as proto___google___fhir___proto___r4___core___codes_pb2___FinancialResourceStatusCode,
)

from proto.google.fhir.proto.r4.core.datatypes_pb2 import (
    Boolean as proto___google___fhir___proto___r4___core___datatypes_pb2___Boolean,
    Code as proto___google___fhir___proto___r4___core___datatypes_pb2___Code,
    CodeableConcept as proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept,
    Date as proto___google___fhir___proto___r4___core___datatypes_pb2___Date,
    DateTime as proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime,
    Extension as proto___google___fhir___proto___r4___core___datatypes_pb2___Extension,
    Id as proto___google___fhir___proto___r4___core___datatypes_pb2___Id,
    Identifier as proto___google___fhir___proto___r4___core___datatypes_pb2___Identifier,
    Meta as proto___google___fhir___proto___r4___core___datatypes_pb2___Meta,
    Money as proto___google___fhir___proto___r4___core___datatypes_pb2___Money,
    Narrative as proto___google___fhir___proto___r4___core___datatypes_pb2___Narrative,
    Period as proto___google___fhir___proto___r4___core___datatypes_pb2___Period,
    Reference as proto___google___fhir___proto___r4___core___datatypes_pb2___Reference,
    String as proto___google___fhir___proto___r4___core___datatypes_pb2___String,
    UnsignedInt as proto___google___fhir___proto___r4___core___datatypes_pb2___UnsignedInt,
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

class CoverageEligibilityResponse(google___protobuf___message___Message):
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

    class PurposeCode(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        value: proto___google___fhir___proto___r4___core___codes_pb2___EligibilityResponsePurposeCode.ValueValue = ...

        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        def __init__(self,
            *,
            value : typing___Optional[proto___google___fhir___proto___r4___core___codes_pb2___EligibilityResponsePurposeCode.ValueValue] = None,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"id",b"id"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"extension",b"extension",u"id",b"id",u"value",b"value"]) -> None: ...
    type___PurposeCode = PurposeCode

    class ServicedX(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def date(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Date: ...

        @property
        def period(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Period: ...

        def __init__(self,
            *,
            date : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Date] = None,
            period : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Period] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"choice",b"choice",u"date",b"date",u"period",b"period"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"choice",b"choice",u"date",b"date",u"period",b"period"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions___Literal[u"choice",b"choice"]) -> typing_extensions___Literal["date","period"]: ...
    type___ServicedX = ServicedX

    class OutcomeCode(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        value: proto___google___fhir___proto___r4___core___codes_pb2___ClaimProcessingCode.ValueValue = ...

        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        def __init__(self,
            *,
            value : typing___Optional[proto___google___fhir___proto___r4___core___codes_pb2___ClaimProcessingCode.ValueValue] = None,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"id",b"id"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"extension",b"extension",u"id",b"id",u"value",b"value"]) -> None: ...
    type___OutcomeCode = OutcomeCode

    class Insurance(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class Items(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            class Benefit(google___protobuf___message___Message):
                DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
                class AllowedX(google___protobuf___message___Message):
                    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

                    @property
                    def unsigned_int(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___UnsignedInt: ...

                    @property
                    def string_value(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

                    @property
                    def money(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Money: ...

                    def __init__(self,
                        *,
                        unsigned_int : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___UnsignedInt] = None,
                        string_value : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
                        money : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Money] = None,
                        ) -> None: ...
                    def HasField(self, field_name: typing_extensions___Literal[u"choice",b"choice",u"money",b"money",u"string_value",b"string_value",u"unsigned_int",b"unsigned_int"]) -> builtin___bool: ...
                    def ClearField(self, field_name: typing_extensions___Literal[u"choice",b"choice",u"money",b"money",u"string_value",b"string_value",u"unsigned_int",b"unsigned_int"]) -> None: ...
                    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"choice",b"choice"]) -> typing_extensions___Literal["unsigned_int","string_value","money"]: ...
                type___AllowedX = AllowedX

                class UsedX(google___protobuf___message___Message):
                    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

                    @property
                    def unsigned_int(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___UnsignedInt: ...

                    @property
                    def string_value(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

                    @property
                    def money(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Money: ...

                    def __init__(self,
                        *,
                        unsigned_int : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___UnsignedInt] = None,
                        string_value : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
                        money : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Money] = None,
                        ) -> None: ...
                    def HasField(self, field_name: typing_extensions___Literal[u"choice",b"choice",u"money",b"money",u"string_value",b"string_value",u"unsigned_int",b"unsigned_int"]) -> builtin___bool: ...
                    def ClearField(self, field_name: typing_extensions___Literal[u"choice",b"choice",u"money",b"money",u"string_value",b"string_value",u"unsigned_int",b"unsigned_int"]) -> None: ...
                    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"choice",b"choice"]) -> typing_extensions___Literal["unsigned_int","string_value","money"]: ...
                type___UsedX = UsedX


                @property
                def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

                @property
                def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

                @property
                def modifier_extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

                @property
                def type(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

                @property
                def allowed(self) -> type___CoverageEligibilityResponse.Insurance.Items.Benefit.AllowedX: ...

                @property
                def used(self) -> type___CoverageEligibilityResponse.Insurance.Items.Benefit.UsedX: ...

                def __init__(self,
                    *,
                    id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
                    extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
                    modifier_extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
                    type : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
                    allowed : typing___Optional[type___CoverageEligibilityResponse.Insurance.Items.Benefit.AllowedX] = None,
                    used : typing___Optional[type___CoverageEligibilityResponse.Insurance.Items.Benefit.UsedX] = None,
                    ) -> None: ...
                def HasField(self, field_name: typing_extensions___Literal[u"allowed",b"allowed",u"id",b"id",u"type",b"type",u"used",b"used"]) -> builtin___bool: ...
                def ClearField(self, field_name: typing_extensions___Literal[u"allowed",b"allowed",u"extension",b"extension",u"id",b"id",u"modifier_extension",b"modifier_extension",u"type",b"type",u"used",b"used"]) -> None: ...
            type___Benefit = Benefit


            @property
            def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

            @property
            def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

            @property
            def modifier_extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

            @property
            def category(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

            @property
            def product_or_service(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

            @property
            def modifier(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]: ...

            @property
            def provider(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Reference: ...

            @property
            def excluded(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Boolean: ...

            @property
            def name(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

            @property
            def description(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

            @property
            def network(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

            @property
            def unit(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

            @property
            def term(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

            @property
            def benefit(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___CoverageEligibilityResponse.Insurance.Items.Benefit]: ...

            @property
            def authorization_required(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Boolean: ...

            @property
            def authorization_supporting(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]: ...

            @property
            def authorization_url(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Uri: ...

            def __init__(self,
                *,
                id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
                extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
                modifier_extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
                category : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
                product_or_service : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
                modifier : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]] = None,
                provider : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference] = None,
                excluded : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Boolean] = None,
                name : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
                description : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
                network : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
                unit : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
                term : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
                benefit : typing___Optional[typing___Iterable[type___CoverageEligibilityResponse.Insurance.Items.Benefit]] = None,
                authorization_required : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Boolean] = None,
                authorization_supporting : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept]] = None,
                authorization_url : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Uri] = None,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions___Literal[u"authorization_required",b"authorization_required",u"authorization_url",b"authorization_url",u"category",b"category",u"description",b"description",u"excluded",b"excluded",u"id",b"id",u"name",b"name",u"network",b"network",u"product_or_service",b"product_or_service",u"provider",b"provider",u"term",b"term",u"unit",b"unit"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"authorization_required",b"authorization_required",u"authorization_supporting",b"authorization_supporting",u"authorization_url",b"authorization_url",u"benefit",b"benefit",u"category",b"category",u"description",b"description",u"excluded",b"excluded",u"extension",b"extension",u"id",b"id",u"modifier",b"modifier",u"modifier_extension",b"modifier_extension",u"name",b"name",u"network",b"network",u"product_or_service",b"product_or_service",u"provider",b"provider",u"term",b"term",u"unit",b"unit"]) -> None: ...
        type___Items = Items


        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def modifier_extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def coverage(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Reference: ...

        @property
        def inforce(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Boolean: ...

        @property
        def benefit_period(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Period: ...

        @property
        def item(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___CoverageEligibilityResponse.Insurance.Items]: ...

        def __init__(self,
            *,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            modifier_extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            coverage : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference] = None,
            inforce : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Boolean] = None,
            benefit_period : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Period] = None,
            item : typing___Optional[typing___Iterable[type___CoverageEligibilityResponse.Insurance.Items]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"benefit_period",b"benefit_period",u"coverage",b"coverage",u"id",b"id",u"inforce",b"inforce"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"benefit_period",b"benefit_period",u"coverage",b"coverage",u"extension",b"extension",u"id",b"id",u"inforce",b"inforce",u"item",b"item",u"modifier_extension",b"modifier_extension"]) -> None: ...
    type___Insurance = Insurance

    class Errors(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def id(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

        @property
        def extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def modifier_extension(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]: ...

        @property
        def code(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

        def __init__(self,
            *,
            id : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
            extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            modifier_extension : typing___Optional[typing___Iterable[proto___google___fhir___proto___r4___core___datatypes_pb2___Extension]] = None,
            code : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"code",b"code",u"id",b"id"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"extension",b"extension",u"id",b"id",u"modifier_extension",b"modifier_extension"]) -> None: ...
    type___Errors = Errors


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
    def status(self) -> type___CoverageEligibilityResponse.StatusCode: ...

    @property
    def purpose(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___CoverageEligibilityResponse.PurposeCode]: ...

    @property
    def patient(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Reference: ...

    @property
    def serviced(self) -> type___CoverageEligibilityResponse.ServicedX: ...

    @property
    def created(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime: ...

    @property
    def requestor(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Reference: ...

    @property
    def request(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Reference: ...

    @property
    def outcome(self) -> type___CoverageEligibilityResponse.OutcomeCode: ...

    @property
    def disposition(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

    @property
    def insurer(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___Reference: ...

    @property
    def insurance(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___CoverageEligibilityResponse.Insurance]: ...

    @property
    def pre_auth_ref(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___String: ...

    @property
    def form(self) -> proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept: ...

    @property
    def error(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___CoverageEligibilityResponse.Errors]: ...

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
        status : typing___Optional[type___CoverageEligibilityResponse.StatusCode] = None,
        purpose : typing___Optional[typing___Iterable[type___CoverageEligibilityResponse.PurposeCode]] = None,
        patient : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference] = None,
        serviced : typing___Optional[type___CoverageEligibilityResponse.ServicedX] = None,
        created : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___DateTime] = None,
        requestor : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference] = None,
        request : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference] = None,
        outcome : typing___Optional[type___CoverageEligibilityResponse.OutcomeCode] = None,
        disposition : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
        insurer : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___Reference] = None,
        insurance : typing___Optional[typing___Iterable[type___CoverageEligibilityResponse.Insurance]] = None,
        pre_auth_ref : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___String] = None,
        form : typing___Optional[proto___google___fhir___proto___r4___core___datatypes_pb2___CodeableConcept] = None,
        error : typing___Optional[typing___Iterable[type___CoverageEligibilityResponse.Errors]] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"created",b"created",u"disposition",b"disposition",u"form",b"form",u"id",b"id",u"implicit_rules",b"implicit_rules",u"insurer",b"insurer",u"language",b"language",u"meta",b"meta",u"outcome",b"outcome",u"patient",b"patient",u"pre_auth_ref",b"pre_auth_ref",u"request",b"request",u"requestor",b"requestor",u"serviced",b"serviced",u"status",b"status",u"text",b"text"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"contained",b"contained",u"created",b"created",u"disposition",b"disposition",u"error",b"error",u"extension",b"extension",u"form",b"form",u"id",b"id",u"identifier",b"identifier",u"implicit_rules",b"implicit_rules",u"insurance",b"insurance",u"insurer",b"insurer",u"language",b"language",u"meta",b"meta",u"modifier_extension",b"modifier_extension",u"outcome",b"outcome",u"patient",b"patient",u"pre_auth_ref",b"pre_auth_ref",u"purpose",b"purpose",u"request",b"request",u"requestor",b"requestor",u"serviced",b"serviced",u"status",b"status",u"text",b"text"]) -> None: ...
type___CoverageEligibilityResponse = CoverageEligibilityResponse
