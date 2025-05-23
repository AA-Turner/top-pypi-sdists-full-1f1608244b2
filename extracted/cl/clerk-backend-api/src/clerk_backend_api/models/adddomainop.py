"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class AddDomainRequestBodyTypedDict(TypedDict):
    name: str
    r"""The new domain name. Can contain the port for development instances."""
    is_satellite: bool
    r"""Marks the new domain as satellite. Only `true` is accepted at the moment."""
    proxy_url: NotRequired[Nullable[str]]
    r"""The full URL of the proxy which will forward requests to the Clerk Frontend API for this domain. Applicable only to production instances."""


class AddDomainRequestBody(BaseModel):
    name: str
    r"""The new domain name. Can contain the port for development instances."""

    is_satellite: bool
    r"""Marks the new domain as satellite. Only `true` is accepted at the moment."""

    proxy_url: OptionalNullable[str] = UNSET
    r"""The full URL of the proxy which will forward requests to the Clerk Frontend API for this domain. Applicable only to production instances."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["proxy_url"]
        nullable_fields = ["proxy_url"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
