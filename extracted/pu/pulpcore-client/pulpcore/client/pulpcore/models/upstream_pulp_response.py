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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pulpcore.client.pulpcore.models.generic_remote_response_hidden_fields_inner import GenericRemoteResponseHiddenFieldsInner
from pulpcore.client.pulpcore.models.policy357_enum import Policy357Enum
from typing import Optional, Set
from typing_extensions import Self

class UpstreamPulpResponse(BaseModel):
    """
    Serializer for a Server.
    """ # noqa: E501
    pulp_href: Optional[StrictStr] = None
    prn: Optional[StrictStr] = Field(default=None, description="The Pulp Resource Name (PRN).")
    pulp_created: Optional[datetime] = Field(default=None, description="Timestamp of creation.")
    pulp_last_updated: Optional[datetime] = Field(default=None, description="Timestamp of the most recent update of the remote.")
    name: StrictStr = Field(description="A unique name for this Pulp server.")
    base_url: StrictStr = Field(description="The transport, hostname, and an optional port of the Pulp server. e.g. https://example.com")
    api_root: StrictStr = Field(description="The API root. Defaults to '/pulp/'.")
    domain: Optional[StrictStr] = Field(default=None, description="The domain of the Pulp server if enabled.")
    ca_cert: Optional[StrictStr] = Field(default=None, description="A PEM encoded CA certificate used to validate the server certificate presented by the remote server.")
    client_cert: Optional[StrictStr] = Field(default=None, description="A PEM encoded client certificate used for authentication.")
    tls_validation: Optional[StrictBool] = Field(default=None, description="If True, TLS peer validation must be performed.")
    hidden_fields: Optional[List[GenericRemoteResponseHiddenFieldsInner]] = Field(default=None, description="List of hidden (write only) fields")
    q_select: Optional[StrictStr] = Field(default=None, description="Filter distributions on the upstream Pulp using complex filtering. E.g. pulp_label_select=\"foo\" OR pulp_label_select=\"key=val\"")
    last_replication: Optional[datetime] = Field(default=None, description="Timestamp of the last replication that occurred. Equals to 'null' if no replication task has been executed.")
    policy: Optional[Policy357Enum] = Field(default=None, description="Policy for how replicate will manage the local objects within the domain.  * `all` - Replicate manages ALL local objects within the domain. * `labeled` - Replicate will only manage the objects created from a previous replication, unlabled local objects will be untouched. * `nodelete` - Replicate will not delete any local object whether they were created by replication or not.")
    __properties: ClassVar[List[str]] = ["pulp_href", "prn", "pulp_created", "pulp_last_updated", "name", "base_url", "api_root", "domain", "ca_cert", "client_cert", "tls_validation", "hidden_fields", "q_select", "last_replication", "policy"]

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
        """Create an instance of UpstreamPulpResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "pulp_href",
            "prn",
            "pulp_created",
            "pulp_last_updated",
            "hidden_fields",
            "last_replication",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in hidden_fields (list)
        _items = []
        if self.hidden_fields:
            for _item_hidden_fields in self.hidden_fields:
                if _item_hidden_fields:
                    _items.append(_item_hidden_fields.to_dict())
            _dict['hidden_fields'] = _items
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

        # set to None if q_select (nullable) is None
        # and model_fields_set contains the field
        if self.q_select is None and "q_select" in self.model_fields_set:
            _dict['q_select'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpstreamPulpResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pulp_href": obj.get("pulp_href"),
            "prn": obj.get("prn"),
            "pulp_created": obj.get("pulp_created"),
            "pulp_last_updated": obj.get("pulp_last_updated"),
            "name": obj.get("name"),
            "base_url": obj.get("base_url"),
            "api_root": obj.get("api_root"),
            "domain": obj.get("domain"),
            "ca_cert": obj.get("ca_cert"),
            "client_cert": obj.get("client_cert"),
            "tls_validation": obj.get("tls_validation"),
            "hidden_fields": [GenericRemoteResponseHiddenFieldsInner.from_dict(_item) for _item in obj["hidden_fields"]] if obj.get("hidden_fields") is not None else None,
            "q_select": obj.get("q_select"),
            "last_replication": obj.get("last_replication"),
            "policy": obj.get("policy")
        })
        return _obj


