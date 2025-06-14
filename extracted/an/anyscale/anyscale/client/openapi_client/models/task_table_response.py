# coding: utf-8

"""
    Managed Ray API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class TaskTableResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'results': 'list[TaskTableRow]',
        'next_offset': 'str',
        'total': 'int'
    }

    attribute_map = {
        'results': 'results',
        'next_offset': 'next_offset',
        'total': 'total'
    }

    def __init__(self, results=None, next_offset=None, total=None, local_vars_configuration=None):  # noqa: E501
        """TaskTableResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._results = None
        self._next_offset = None
        self._total = None
        self.discriminator = None

        self.results = results
        if next_offset is not None:
            self.next_offset = next_offset
        self.total = total

    @property
    def results(self):
        """Gets the results of this TaskTableResponse.  # noqa: E501


        :return: The results of this TaskTableResponse.  # noqa: E501
        :rtype: list[TaskTableRow]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this TaskTableResponse.


        :param results: The results of this TaskTableResponse.  # noqa: E501
        :type: list[TaskTableRow]
        """
        if self.local_vars_configuration.client_side_validation and results is None:  # noqa: E501
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

    @property
    def next_offset(self):
        """Gets the next_offset of this TaskTableResponse.  # noqa: E501


        :return: The next_offset of this TaskTableResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_offset

    @next_offset.setter
    def next_offset(self, next_offset):
        """Sets the next_offset of this TaskTableResponse.


        :param next_offset: The next_offset of this TaskTableResponse.  # noqa: E501
        :type: str
        """

        self._next_offset = next_offset

    @property
    def total(self):
        """Gets the total of this TaskTableResponse.  # noqa: E501


        :return: The total of this TaskTableResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this TaskTableResponse.


        :param total: The total of this TaskTableResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total is None:  # noqa: E501
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TaskTableResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskTableResponse):
            return True

        return self.to_dict() != other.to_dict()
