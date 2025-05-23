# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from datetime import datetime
from datetime import date
from pprint import pformat
import re
import json

from ..utils import sanitize_for_serialization

# type hinting support
from typing import TYPE_CHECKING
from typing import List
from typing import Dict

if TYPE_CHECKING:
    from . import ScimMetadata
    from . import ScimV2SchemaAttribute

class ScimV2SchemaDefinition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ScimV2SchemaDefinition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'attributes': 'list[ScimV2SchemaAttribute]',
            'meta': 'ScimMetadata'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'attributes': 'attributes',
            'meta': 'meta'
        }

        self._id = None
        self._name = None
        self._description = None
        self._attributes = None
        self._meta = None

    @property
    def id(self) -> str:
        """
        Gets the id of this ScimV2SchemaDefinition.
        The ID of the SCIM resource. Set by the service provider. \"caseExact\" is set to \"true\". \"mutability\" is set to \"readOnly\". \"returned\" is set to \"always\".

        :return: The id of this ScimV2SchemaDefinition.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this ScimV2SchemaDefinition.
        The ID of the SCIM resource. Set by the service provider. \"caseExact\" is set to \"true\". \"mutability\" is set to \"readOnly\". \"returned\" is set to \"always\".

        :param id: The id of this ScimV2SchemaDefinition.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this ScimV2SchemaDefinition.
        The name of the schema.

        :return: The name of this ScimV2SchemaDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this ScimV2SchemaDefinition.
        The name of the schema.

        :param name: The name of this ScimV2SchemaDefinition.
        :type: str
        """
        

        self._name = name

    @property
    def description(self) -> str:
        """
        Gets the description of this ScimV2SchemaDefinition.
        The description of the schema.

        :return: The description of this ScimV2SchemaDefinition.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this ScimV2SchemaDefinition.
        The description of the schema.

        :param description: The description of this ScimV2SchemaDefinition.
        :type: str
        """
        

        self._description = description

    @property
    def attributes(self) -> List['ScimV2SchemaAttribute']:
        """
        Gets the attributes of this ScimV2SchemaDefinition.
        The list of service provider attributes.

        :return: The attributes of this ScimV2SchemaDefinition.
        :rtype: list[ScimV2SchemaAttribute]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes: List['ScimV2SchemaAttribute']) -> None:
        """
        Sets the attributes of this ScimV2SchemaDefinition.
        The list of service provider attributes.

        :param attributes: The attributes of this ScimV2SchemaDefinition.
        :type: list[ScimV2SchemaAttribute]
        """
        

        self._attributes = attributes

    @property
    def meta(self) -> 'ScimMetadata':
        """
        Gets the meta of this ScimV2SchemaDefinition.
        The metadata of the SCIM resource. Only \"location\" and \"resourceType\" are set for \"Schema\" resources.

        :return: The meta of this ScimV2SchemaDefinition.
        :rtype: ScimMetadata
        """
        return self._meta

    @meta.setter
    def meta(self, meta: 'ScimMetadata') -> None:
        """
        Sets the meta of this ScimV2SchemaDefinition.
        The metadata of the SCIM resource. Only \"location\" and \"resourceType\" are set for \"Schema\" resources.

        :param meta: The meta of this ScimV2SchemaDefinition.
        :type: ScimMetadata
        """
        

        self._meta = meta

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in self.swagger_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_json(self):
        """
        Returns the model as raw JSON
        """
        return json.dumps(sanitize_for_serialization(self.to_dict()))

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

