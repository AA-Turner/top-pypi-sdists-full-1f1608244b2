# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from akeyless.configuration import Configuration


class ListItemsOutput(object):
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
        'has_next': 'bool',
        'items': 'list[Item]',
        'next_page': 'str'
    }

    attribute_map = {
        'has_next': 'has_next',
        'items': 'items',
        'next_page': 'next_page'
    }

    def __init__(self, has_next=None, items=None, next_page=None, local_vars_configuration=None):  # noqa: E501
        """ListItemsOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._has_next = None
        self._items = None
        self._next_page = None
        self.discriminator = None

        if has_next is not None:
            self.has_next = has_next
        if items is not None:
            self.items = items
        if next_page is not None:
            self.next_page = next_page

    @property
    def has_next(self):
        """Gets the has_next of this ListItemsOutput.  # noqa: E501


        :return: The has_next of this ListItemsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._has_next

    @has_next.setter
    def has_next(self, has_next):
        """Sets the has_next of this ListItemsOutput.


        :param has_next: The has_next of this ListItemsOutput.  # noqa: E501
        :type: bool
        """

        self._has_next = has_next

    @property
    def items(self):
        """Gets the items of this ListItemsOutput.  # noqa: E501


        :return: The items of this ListItemsOutput.  # noqa: E501
        :rtype: list[Item]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ListItemsOutput.


        :param items: The items of this ListItemsOutput.  # noqa: E501
        :type: list[Item]
        """

        self._items = items

    @property
    def next_page(self):
        """Gets the next_page of this ListItemsOutput.  # noqa: E501


        :return: The next_page of this ListItemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this ListItemsOutput.


        :param next_page: The next_page of this ListItemsOutput.  # noqa: E501
        :type: str
        """

        self._next_page = next_page

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
        if not isinstance(other, ListItemsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListItemsOutput):
            return True

        return self.to_dict() != other.to_dict()
