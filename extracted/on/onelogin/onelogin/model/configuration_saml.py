# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from onelogin import schemas  # noqa: F401


class ConfigurationSaml(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            signature_algorithm = schemas.StrSchema
            certificate_id = schemas.IntSchema
            __annotations__ = {
                "signature_algorithm": signature_algorithm,
                "certificate_id": certificate_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signature_algorithm"]) -> MetaOapg.properties.signature_algorithm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["certificate_id"]) -> MetaOapg.properties.certificate_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["signature_algorithm", "certificate_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signature_algorithm"]) -> typing.Union[MetaOapg.properties.signature_algorithm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["certificate_id"]) -> typing.Union[MetaOapg.properties.certificate_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["signature_algorithm", "certificate_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        signature_algorithm: typing.Union[MetaOapg.properties.signature_algorithm, str, schemas.Unset] = schemas.unset,
        certificate_id: typing.Union[MetaOapg.properties.certificate_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConfigurationSaml':
        return super().__new__(
            cls,
            *_args,
            signature_algorithm=signature_algorithm,
            certificate_id=certificate_id,
            _configuration=_configuration,
            **kwargs,
        )
