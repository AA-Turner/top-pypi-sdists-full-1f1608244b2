# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 66.22.1-v202505231115-CD
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class ColumnDefinitionInputListV1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'column_definitions': 'list[ColumnDefinitionInputV1]'
    }

    attribute_map = {
        'column_definitions': 'columnDefinitions'
    }

    def __init__(self, column_definitions=None):
        """
        ColumnDefinitionInputListV1 - a model defined in Swagger
        """

        self._column_definitions = None

        if column_definitions is not None:
          self.column_definitions = column_definitions

    @property
    def column_definitions(self):
        """
        Gets the column_definitions of this ColumnDefinitionInputListV1.
        Column definitions for the Table. A column definition contains all the properties that define each column in the table.

        :return: The column_definitions of this ColumnDefinitionInputListV1.
        :rtype: list[ColumnDefinitionInputV1]
        """
        return self._column_definitions

    @column_definitions.setter
    def column_definitions(self, column_definitions):
        """
        Sets the column_definitions of this ColumnDefinitionInputListV1.
        Column definitions for the Table. A column definition contains all the properties that define each column in the table.

        :param column_definitions: The column_definitions of this ColumnDefinitionInputListV1.
        :type: list[ColumnDefinitionInputV1]
        """
        if column_definitions is None:
            raise ValueError("Invalid value for `column_definitions`, must not be `None`")

        self._column_definitions = column_definitions

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        if not isinstance(other, ColumnDefinitionInputListV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
