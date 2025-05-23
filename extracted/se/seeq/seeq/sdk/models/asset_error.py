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


class AssetError(object):
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
        'error': 'str',
        'id': 'str',
        'name': 'str',
        'parent_name': 'str'
    }

    attribute_map = {
        'error': 'error',
        'id': 'id',
        'name': 'name',
        'parent_name': 'parentName'
    }

    def __init__(self, error=None, id=None, name=None, parent_name=None):
        """
        AssetError - a model defined in Swagger
        """

        self._error = None
        self._id = None
        self._name = None
        self._parent_name = None

        if error is not None:
          self.error = error
        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if parent_name is not None:
          self.parent_name = parent_name

    @property
    def error(self):
        """
        Gets the error of this AssetError.

        :return: The error of this AssetError.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this AssetError.

        :param error: The error of this AssetError.
        :type: str
        """

        self._error = error

    @property
    def id(self):
        """
        Gets the id of this AssetError.

        :return: The id of this AssetError.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AssetError.

        :param id: The id of this AssetError.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this AssetError.

        :return: The name of this AssetError.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AssetError.

        :param name: The name of this AssetError.
        :type: str
        """

        self._name = name

    @property
    def parent_name(self):
        """
        Gets the parent_name of this AssetError.

        :return: The parent_name of this AssetError.
        :rtype: str
        """
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name):
        """
        Sets the parent_name of this AssetError.

        :param parent_name: The parent_name of this AssetError.
        :type: str
        """

        self._parent_name = parent_name

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
        if not isinstance(other, AssetError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
