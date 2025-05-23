# coding: utf-8
"""
    Snowflake Iceberg Table API.

    The Snowflake Iceberg Table API is a REST API that you can use to access, update, and perform certain actions on Iceberg Table resource in a Snowflake database.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: support@snowflake.com
    Generated by: https://openapi-generator.tech

    Do not edit this file manually.
"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from typing import Union

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr

from typing import Any, ClassVar, Dict, List, Optional


class IcebergTableFromIcebergFiles(BaseModel):
    """A model object representing the IcebergTableFromIcebergFiles resource.

    Constructs an object of type IcebergTableFromIcebergFiles with the provided properties.

    Parameters
    __________
    name : str
        Specifies the name for the table, must be unique for the schema in which the table is created
    metadata_file_path : str
        Specifies the relative path of the Iceberg metadata file to use for column definitions.
    external_volume : str, optional
        Specifies the name of the external volume to use for the table
    replace_invalid_characters : bool, optional
        Specifies whether to replace invalid characters in the column names
    catalog : str, optional
        Specifies the name of the catalog integration to use for the table
    comment : str, optional
        Specifies a comment for the table
    """

    name: StrictStr

    external_volume: Optional[StrictStr] = None

    replace_invalid_characters: Optional[StrictBool] = None

    metadata_file_path: StrictStr

    catalog: Optional[StrictStr] = None

    comment: Optional[StrictStr] = None

    __properties = [
        "name", "external_volume", "replace_invalid_characters",
        "metadata_file_path", "catalog", "comment"
    ]

    class Config:
        populate_by_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias."""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias."""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> IcebergTableFromIcebergFiles:
        """Create an instance of IcebergTableFromIcebergFiles from a JSON string."""
        return cls.from_dict(json.loads(json_str))

    def to_dict(
        self,
        hide_readonly_properties: bool = False,
    ) -> dict[str, Any]:
        """Returns the dictionary representation of the model using alias."""

        exclude_properties = set()

        if hide_readonly_properties:
            exclude_properties.update({})

        _dict = dict(
            self._iter(to_dict=True,
                       by_alias=True,
                       exclude=exclude_properties,
                       exclude_none=True))

        return _dict

    def to_dict_without_readonly_properties(self) -> dict[str, Any]:
        """Return the dictionary representation of the model without readonly properties."""
        return self.to_dict(hide_readonly_properties=True)

    @classmethod
    def from_dict(cls, obj: dict) -> IcebergTableFromIcebergFiles:
        """Create an instance of IcebergTableFromIcebergFiles from a dict."""

        if obj is None:
            return None

        if type(obj) is not dict:
            return IcebergTableFromIcebergFiles.parse_obj(obj)

        _obj = IcebergTableFromIcebergFiles.parse_obj({
            "name":
            obj.get("name"),
            "external_volume":
            obj.get("external_volume"),
            "replace_invalid_characters":
            obj.get("replace_invalid_characters"),
            "metadata_file_path":
            obj.get("metadata_file_path"),
            "catalog":
            obj.get("catalog"),
            "comment":
            obj.get("comment"),
        })

        return _obj


from typing import Optional, List, Dict


class IcebergTableFromIcebergFilesModel():

    def __init__(
        self,
        name: str,
        metadata_file_path: str,
        # optional properties
        external_volume: Optional[str] = None,
        replace_invalid_characters: Optional[bool] = None,
        catalog: Optional[str] = None,
        comment: Optional[str] = None,
    ):
        """A model object representing the IcebergTableFromIcebergFiles resource.

        Constructs an object of type IcebergTableFromIcebergFiles with the provided properties.

        Parameters
        __________
        name : str
            Specifies the name for the table, must be unique for the schema in which the table is created
        metadata_file_path : str
            Specifies the relative path of the Iceberg metadata file to use for column definitions.
        external_volume : str, optional
            Specifies the name of the external volume to use for the table
        replace_invalid_characters : bool, optional
            Specifies whether to replace invalid characters in the column names
        catalog : str, optional
            Specifies the name of the catalog integration to use for the table
        comment : str, optional
            Specifies a comment for the table
        """

        self.name = name
        self.external_volume = external_volume
        self.replace_invalid_characters = replace_invalid_characters
        self.metadata_file_path = metadata_file_path
        self.catalog = catalog
        self.comment = comment

    __properties = [
        "name", "external_volume", "replace_invalid_characters",
        "metadata_file_path", "catalog", "comment"
    ]

    def __repr__(self) -> str:
        return repr(self._to_model())

    def _to_model(self):
        return IcebergTableFromIcebergFiles(
            name=self.name,
            external_volume=self.external_volume,
            replace_invalid_characters=self.replace_invalid_characters,
            metadata_file_path=self.metadata_file_path,
            catalog=self.catalog,
            comment=self.comment,
        )

    @classmethod
    def _from_model(cls, model) -> IcebergTableFromIcebergFilesModel:
        return IcebergTableFromIcebergFilesModel(
            name=model.name,
            external_volume=model.external_volume,
            replace_invalid_characters=model.replace_invalid_characters,
            metadata_file_path=model.metadata_file_path,
            catalog=model.catalog,
            comment=model.comment,
        )

    def to_dict(self):
        """Creates a dictionary of the properties from a IcebergTableFromIcebergFiles.

        This method constructs a dictionary with the key-value entries corresponding to the properties of the IcebergTableFromIcebergFiles object.

        Returns
        _______
        dict
            A dictionary object created using the input model.
        """
        return self._to_model().to_dict()

    @classmethod
    def from_dict(cls, obj: dict) -> IcebergTableFromIcebergFilesModel:
        """Creates an instance of IcebergTableFromIcebergFiles from a dict.

        This method constructs a IcebergTableFromIcebergFiles object from a dictionary with the key-value pairs of its properties.

        Parameters
        ----------
        obj : dict
            A dictionary whose keys and values correspond to the properties of the resource object.

        Returns
        _______
        IcebergTableFromIcebergFiles
            A IcebergTableFromIcebergFiles object created using the input dictionary; this will fail if the required properties are missing.
        """
        return cls._from_model(IcebergTableFromIcebergFiles.from_dict(obj))


IcebergTableFromIcebergFiles._model_class = IcebergTableFromIcebergFilesModel
