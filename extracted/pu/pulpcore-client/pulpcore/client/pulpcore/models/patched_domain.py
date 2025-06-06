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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from pulpcore.client.pulpcore.models.storage_class_enum import StorageClassEnum
from typing import Optional, Set
from typing_extensions import Self

class PatchedDomain(BaseModel):
    """
    Serializer for Domain.
    """ # noqa: E501
    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=50)]] = Field(default=None, description="A name for this domain.")
    description: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="An optional description.")
    pulp_labels: Optional[Dict[str, Optional[StrictStr]]] = None
    storage_class: Optional[StorageClassEnum] = Field(default=None, description="Backend storage class for domain.  * `pulpcore.app.models.storage.FileSystem` - Use local filesystem as storage * `storages.backends.s3boto3.S3Boto3Storage` - Use Amazon S3 as storage * `storages.backends.azure_storage.AzureStorage` - Use Azure Blob as storage")
    storage_settings: Optional[Dict[str, Any]] = Field(default=None, description="Settings for storage class.")
    redirect_to_object_storage: Optional[StrictBool] = Field(default=True, description="Boolean to have the content app redirect to object storage.")
    hide_guarded_distributions: Optional[StrictBool] = Field(default=False, description="Boolean to hide distributions with a content guard in the content app.")
    __properties: ClassVar[List[str]] = ["name", "description", "pulp_labels", "storage_class", "storage_settings", "redirect_to_object_storage", "hide_guarded_distributions"]

    @field_validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[-a-zA-Z0-9_]+$", value):
            raise ValueError(r"must validate the regular expression /^[-a-zA-Z0-9_]+$/")
        return value

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
        """Create an instance of PatchedDomain from a JSON string"""
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
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedDomain from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "pulp_labels": obj.get("pulp_labels"),
            "storage_class": obj.get("storage_class"),
            "storage_settings": obj.get("storage_settings"),
            "redirect_to_object_storage": obj.get("redirect_to_object_storage") if obj.get("redirect_to_object_storage") is not None else True,
            "hide_guarded_distributions": obj.get("hide_guarded_distributions") if obj.get("hide_guarded_distributions") is not None else False
        })
        return _obj


