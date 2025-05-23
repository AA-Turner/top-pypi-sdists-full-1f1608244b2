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


class MaterializedTableV1(object):
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
        'headers': 'list[MaterializedTableHeaderV1]',
        'rows': 'list[list[object]]'
    }

    attribute_map = {
        'headers': 'headers',
        'rows': 'rows'
    }

    def __init__(self, headers=None, rows=None):
        """
        MaterializedTableV1 - a model defined in Swagger
        """

        self._headers = None
        self._rows = None

        if headers is not None:
          self.headers = headers
        if rows is not None:
          self.rows = rows

    @property
    def headers(self):
        """
        Gets the headers of this MaterializedTableV1.
        The headers for the returned rows. The order of the headers will match the order of the datums in the rows.

        :return: The headers of this MaterializedTableV1.
        :rtype: list[MaterializedTableHeaderV1]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """
        Sets the headers of this MaterializedTableV1.
        The headers for the returned rows. The order of the headers will match the order of the datums in the rows.

        :param headers: The headers of this MaterializedTableV1.
        :type: list[MaterializedTableHeaderV1]
        """
        if headers is None:
            raise ValueError("Invalid value for `headers`, must not be `None`")

        self._headers = headers

    @property
    def rows(self):
        """
        Gets the rows of this MaterializedTableV1.
        The list of all rows belonging to this table. Each row is a list where its index will correspond to the same index in the headers.

        :return: The rows of this MaterializedTableV1.
        :rtype: list[list[object]]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """
        Sets the rows of this MaterializedTableV1.
        The list of all rows belonging to this table. Each row is a list where its index will correspond to the same index in the headers.

        :param rows: The rows of this MaterializedTableV1.
        :type: list[list[object]]
        """
        if rows is None:
            raise ValueError("Invalid value for `rows`, must not be `None`")

        self._rows = rows

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
        if not isinstance(other, MaterializedTableV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
