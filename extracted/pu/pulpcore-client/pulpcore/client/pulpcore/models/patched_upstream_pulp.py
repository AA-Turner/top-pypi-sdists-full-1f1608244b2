# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from pulpcore.client.pulpcore.models.policy357_enum import Policy357Enum
from typing import Optional, Set
from typing_extensions import Self

class PatchedUpstreamPulp(BaseModel):
    """
    Serializer for a Server.
    """ # noqa: E501
    name: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="A unique name for this Pulp server.")
    base_url: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="The transport, hostname, and an optional port of the Pulp server. e.g. https://example.com")
    api_root: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="The API root. Defaults to '/pulp/'.")
    domain: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="The domain of the Pulp server if enabled.")
    ca_cert: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="A PEM encoded CA certificate used to validate the server certificate presented by the remote server.")
    client_cert: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="A PEM encoded client certificate used for authentication.")
    client_key: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="A PEM encoded private key used for authentication.")
    tls_validation: Optional[StrictBool] = Field(default=None, description="If True, TLS peer validation must be performed.")
    username: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="The username to be used for authentication when syncing.")
    password: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="The password to be used for authentication when syncing. Extra leading and trailing whitespace characters are not trimmed.")
    q_select: Optional[StrictStr] = Field(default=None, description="Filter distributions on the upstream Pulp using complex filtering. E.g. pulp_label_select=\"foo\" OR pulp_label_select=\"key=val\"")
    policy: Optional[Policy357Enum] = Field(default=None, description="Policy for how replicate will manage the local objects within the domain.  * `all` - Replicate manages ALL local objects within the domain. * `labeled` - Replicate will only manage the objects created from a previous replication, unlabled local objects will be untouched. * `nodelete` - Replicate will not delete any local object whether they were created by replication or not.")
    __properties: ClassVar[List[str]] = ["name", "base_url", "api_root", "domain", "ca_cert", "client_cert", "client_key", "tls_validation", "username", "password", "q_select", "policy"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PatchedUpstreamPulp from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if ca_cert (nullable) is None
        # and model_fields_set contains the field
        if self.ca_cert is None and "ca_cert" in self.model_fields_set:
            _dict['ca_cert'] = None

        # set to None if client_cert (nullable) is None
        # and model_fields_set contains the field
        if self.client_cert is None and "client_cert" in self.model_fields_set:
            _dict['client_cert'] = None

        # set to None if client_key (nullable) is None
        # and model_fields_set contains the field
        if self.client_key is None and "client_key" in self.model_fields_set:
            _dict['client_key'] = None

        # set to None if username (nullable) is None
        # and model_fields_set contains the field
        if self.username is None and "username" in self.model_fields_set:
            _dict['username'] = None

        # set to None if password (nullable) is None
        # and model_fields_set contains the field
        if self.password is None and "password" in self.model_fields_set:
            _dict['password'] = None

        # set to None if q_select (nullable) is None
        # and model_fields_set contains the field
        if self.q_select is None and "q_select" in self.model_fields_set:
            _dict['q_select'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedUpstreamPulp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "base_url": obj.get("base_url"),
            "api_root": obj.get("api_root"),
            "domain": obj.get("domain"),
            "ca_cert": obj.get("ca_cert"),
            "client_cert": obj.get("client_cert"),
            "client_key": obj.get("client_key"),
            "tls_validation": obj.get("tls_validation"),
            "username": obj.get("username"),
            "password": obj.get("password"),
            "q_select": obj.get("q_select"),
            "policy": obj.get("policy")
        })
        return _obj


