# coding: utf-8
"""
    Snowflake Database Role API.

    The Snowflake Database Role API is a REST API that you can use to access, update, and perform certain actions on Database Role resource in a Snowflake database.  # noqa: E501

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

from pydantic import BaseModel, ConfigDict, Field, field_validator

from typing import Any, ClassVar, Dict, List, Optional

from typing_extensions import Annotated


class ContainingScope(BaseModel):
    """A model object representing the ContainingScope resource.

    Constructs an object of type ContainingScope with the provided properties.

    Parameters
    __________
    database : str
        Database name of the securable scope if applicable.
    var_schema : str, optional
        Schema name of the securable scope if applicable.
    """

    database: Annotated[str, Field(strict=True)]

    var_schema: Optional[Annotated[str,
                                   Field(strict=True)]] = Field(default=None,
                                                                alias="schema")

    __properties = ["database", "schema"]

    @field_validator('database')
    def database_validate_regular_expression(cls, v):

        if not re.match(r"""^\"([^\"]|\"\")+\"|[a-zA-Z_][a-zA-Z0-9_$]*$""", v):
            raise ValueError(
                r"""must validate the regular expression /^"([^"]|"")+"|[a-zA-Z_][a-zA-Z0-9_$]*$/"""
            )
        return v

    @field_validator('var_schema')
    def var_schema_validate_regular_expression(cls, v):

        if v is None:
            return v
        if not re.match(r"""^\"([^\"]|\"\")+\"|[a-zA-Z_][a-zA-Z0-9_$]*$""", v):
            raise ValueError(
                r"""must validate the regular expression /^"([^"]|"")+"|[a-zA-Z_][a-zA-Z0-9_$]*$/"""
            )
        return v

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
    def from_json(cls, json_str: str) -> ContainingScope:
        """Create an instance of ContainingScope from a JSON string."""
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
    def from_dict(cls, obj: dict) -> ContainingScope:
        """Create an instance of ContainingScope from a dict."""

        if obj is None:
            return None

        if type(obj) is not dict:
            return ContainingScope.parse_obj(obj)

        _obj = ContainingScope.parse_obj({
            "database": obj.get("database"),
            "var_schema": obj.get("schema"),
        })

        return _obj


from typing import Optional, List, Dict


class ContainingScopeModel():

    def __init__(
        self,
        database: str,
        # optional properties
        var_schema: Optional[str] = None,
    ):
        """A model object representing the ContainingScope resource.

        Constructs an object of type ContainingScope with the provided properties.

        Parameters
        __________
        database : str
            Database name of the securable scope if applicable.
        var_schema : str, optional
            Schema name of the securable scope if applicable.
        """

        self.database = database
        self.var_schema = var_schema

    __properties = ["database", "schema"]

    def __repr__(self) -> str:
        return repr(self._to_model())

    def _to_model(self):
        return ContainingScope(
            database=self.database,
            var_schema=self.var_schema,
        )

    @classmethod
    def _from_model(cls, model) -> ContainingScopeModel:
        return ContainingScopeModel(
            database=model.database,
            var_schema=model.var_schema,
        )

    def to_dict(self):
        """Creates a dictionary of the properties from a ContainingScope.

        This method constructs a dictionary with the key-value entries corresponding to the properties of the ContainingScope object.

        Returns
        _______
        dict
            A dictionary object created using the input model.
        """
        return self._to_model().to_dict()

    @classmethod
    def from_dict(cls, obj: dict) -> ContainingScopeModel:
        """Creates an instance of ContainingScope from a dict.

        This method constructs a ContainingScope object from a dictionary with the key-value pairs of its properties.

        Parameters
        ----------
        obj : dict
            A dictionary whose keys and values correspond to the properties of the resource object.

        Returns
        _______
        ContainingScope
            A ContainingScope object created using the input dictionary; this will fail if the required properties are missing.
        """
        return cls._from_model(ContainingScope.from_dict(obj))


ContainingScope._model_class = ContainingScopeModel
