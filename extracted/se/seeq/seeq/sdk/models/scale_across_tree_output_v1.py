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


class ScaleAcrossTreeOutputV1(object):
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
        'item_results': 'list[ItemSwapResultOutputV1]',
        'status_message': 'str'
    }

    attribute_map = {
        'item_results': 'itemResults',
        'status_message': 'statusMessage'
    }

    def __init__(self, item_results=None, status_message=None):
        """
        ScaleAcrossTreeOutputV1 - a model defined in Swagger
        """

        self._item_results = None
        self._status_message = None

        if item_results is not None:
          self.item_results = item_results
        if status_message is not None:
          self.status_message = status_message

    @property
    def item_results(self):
        """
        Gets the item_results of this ScaleAcrossTreeOutputV1.
        The list of results from new tree items that Seeq attempted to create.

        :return: The item_results of this ScaleAcrossTreeOutputV1.
        :rtype: list[ItemSwapResultOutputV1]
        """
        return self._item_results

    @item_results.setter
    def item_results(self, item_results):
        """
        Sets the item_results of this ScaleAcrossTreeOutputV1.
        The list of results from new tree items that Seeq attempted to create.

        :param item_results: The item_results of this ScaleAcrossTreeOutputV1.
        :type: list[ItemSwapResultOutputV1]
        """

        self._item_results = item_results

    @property
    def status_message(self):
        """
        Gets the status_message of this ScaleAcrossTreeOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :return: The status_message of this ScaleAcrossTreeOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this ScaleAcrossTreeOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :param status_message: The status_message of this ScaleAcrossTreeOutputV1.
        :type: str
        """

        self._status_message = status_message

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
        if not isinstance(other, ScaleAcrossTreeOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
