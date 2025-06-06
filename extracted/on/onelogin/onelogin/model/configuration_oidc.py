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


class ConfigurationOidc(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "login_url",
            "access_token_expiration_minutes",
            "refresh_token_expiration_minutes",
            "redirect_uri",
            "oidc_application_type",
            "token_endpoint_auth_method",
        }
        
        class properties:
            login_url = schemas.StrSchema
            redirect_uri = schemas.StrSchema
            access_token_expiration_minutes = schemas.IntSchema
            refresh_token_expiration_minutes = schemas.IntSchema
            
            
            class token_endpoint_auth_method(
                schemas.EnumBase,
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        0: "POSITIVE_0",
                        1: "POSITIVE_1",
                        2: "POSITIVE_2",
                    }
                
                @schemas.classproperty
                def POSITIVE_0(cls):
                    return cls(0)
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
                
                @schemas.classproperty
                def POSITIVE_2(cls):
                    return cls(2)
            
            
            class oidc_application_type(
                schemas.EnumBase,
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        0: "POSITIVE_0",
                        1: "POSITIVE_1",
                    }
                
                @schemas.classproperty
                def POSITIVE_0(cls):
                    return cls(0)
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
            __annotations__ = {
                "login_url": login_url,
                "redirect_uri": redirect_uri,
                "access_token_expiration_minutes": access_token_expiration_minutes,
                "refresh_token_expiration_minutes": refresh_token_expiration_minutes,
                "token_endpoint_auth_method": token_endpoint_auth_method,
                "oidc_application_type": oidc_application_type,
            }
    
    login_url: MetaOapg.properties.login_url
    access_token_expiration_minutes: MetaOapg.properties.access_token_expiration_minutes
    refresh_token_expiration_minutes: MetaOapg.properties.refresh_token_expiration_minutes
    redirect_uri: MetaOapg.properties.redirect_uri
    oidc_application_type: MetaOapg.properties.oidc_application_type
    token_endpoint_auth_method: MetaOapg.properties.token_endpoint_auth_method
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["login_url"]) -> MetaOapg.properties.login_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redirect_uri"]) -> MetaOapg.properties.redirect_uri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access_token_expiration_minutes"]) -> MetaOapg.properties.access_token_expiration_minutes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refresh_token_expiration_minutes"]) -> MetaOapg.properties.refresh_token_expiration_minutes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_endpoint_auth_method"]) -> MetaOapg.properties.token_endpoint_auth_method: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["oidc_application_type"]) -> MetaOapg.properties.oidc_application_type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["login_url", "redirect_uri", "access_token_expiration_minutes", "refresh_token_expiration_minutes", "token_endpoint_auth_method", "oidc_application_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["login_url"]) -> MetaOapg.properties.login_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redirect_uri"]) -> MetaOapg.properties.redirect_uri: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access_token_expiration_minutes"]) -> MetaOapg.properties.access_token_expiration_minutes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refresh_token_expiration_minutes"]) -> MetaOapg.properties.refresh_token_expiration_minutes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_endpoint_auth_method"]) -> MetaOapg.properties.token_endpoint_auth_method: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["oidc_application_type"]) -> MetaOapg.properties.oidc_application_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["login_url", "redirect_uri", "access_token_expiration_minutes", "refresh_token_expiration_minutes", "token_endpoint_auth_method", "oidc_application_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        login_url: typing.Union[MetaOapg.properties.login_url, str, ],
        access_token_expiration_minutes: typing.Union[MetaOapg.properties.access_token_expiration_minutes, decimal.Decimal, int, ],
        refresh_token_expiration_minutes: typing.Union[MetaOapg.properties.refresh_token_expiration_minutes, decimal.Decimal, int, ],
        redirect_uri: typing.Union[MetaOapg.properties.redirect_uri, str, ],
        oidc_application_type: typing.Union[MetaOapg.properties.oidc_application_type, decimal.Decimal, int, ],
        token_endpoint_auth_method: typing.Union[MetaOapg.properties.token_endpoint_auth_method, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConfigurationOidc':
        return super().__new__(
            cls,
            *_args,
            login_url=login_url,
            access_token_expiration_minutes=access_token_expiration_minutes,
            refresh_token_expiration_minutes=refresh_token_expiration_minutes,
            redirect_uri=redirect_uri,
            oidc_application_type=oidc_application_type,
            token_endpoint_auth_method=token_endpoint_auth_method,
            _configuration=_configuration,
            **kwargs,
        )
