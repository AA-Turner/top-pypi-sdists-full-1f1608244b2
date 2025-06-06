# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 66.25.0-v202506042330-CD
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class EnumConfigFieldV1(object):
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
        'enum_fully_qualified_name': 'str',
        'valid_options': 'list[str]'
    }

    attribute_map = {
        'enum_fully_qualified_name': 'enumFullyQualifiedName',
        'valid_options': 'validOptions'
    }

    def __init__(self, enum_fully_qualified_name=None, valid_options=None):
        """
        EnumConfigFieldV1 - a model defined in Swagger
        """

        self._enum_fully_qualified_name = None
        self._valid_options = None

        if enum_fully_qualified_name is not None:
          self.enum_fully_qualified_name = enum_fully_qualified_name
        if valid_options is not None:
          self.valid_options = valid_options

    @property
    def enum_fully_qualified_name(self):
        """
        Gets the enum_fully_qualified_name of this EnumConfigFieldV1.

        :return: The enum_fully_qualified_name of this EnumConfigFieldV1.
        :rtype: str
        """
        return self._enum_fully_qualified_name

    @enum_fully_qualified_name.setter
    def enum_fully_qualified_name(self, enum_fully_qualified_name):
        """
        Sets the enum_fully_qualified_name of this EnumConfigFieldV1.

        :param enum_fully_qualified_name: The enum_fully_qualified_name of this EnumConfigFieldV1.
        :type: str
        """

        self._enum_fully_qualified_name = enum_fully_qualified_name

    @property
    def valid_options(self):
        """
        Gets the valid_options of this EnumConfigFieldV1.
        The list of valid options allowed for the value field

        :return: The valid_options of this EnumConfigFieldV1.
        :rtype: list[str]
        """
        return self._valid_options

    @valid_options.setter
    def valid_options(self, valid_options):
        """
        Sets the valid_options of this EnumConfigFieldV1.
        The list of valid options allowed for the value field

        :param valid_options: The valid_options of this EnumConfigFieldV1.
        :type: list[str]
        """

        self._valid_options = valid_options

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
        if not isinstance(other, EnumConfigFieldV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
