# coding: utf-8

"""
    seccenter20240508

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListAgentProxiesRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'address': 'str',
        'name': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'slim': 'bool',
        'sort_by': 'str',
        'sort_order': 'str'
    }

    attribute_map = {
        'address': 'Address',
        'name': 'Name',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'slim': 'Slim',
        'sort_by': 'SortBy',
        'sort_order': 'SortOrder'
    }

    def __init__(self, address=None, name=None, page_number=None, page_size=None, slim=None, sort_by=None, sort_order=None, _configuration=None):  # noqa: E501
        """ListAgentProxiesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address = None
        self._name = None
        self._page_number = None
        self._page_size = None
        self._slim = None
        self._sort_by = None
        self._sort_order = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if name is not None:
            self.name = name
        self.page_number = page_number
        self.page_size = page_size
        if slim is not None:
            self.slim = slim
        if sort_by is not None:
            self.sort_by = sort_by
        if sort_order is not None:
            self.sort_order = sort_order

    @property
    def address(self):
        """Gets the address of this ListAgentProxiesRequest.  # noqa: E501


        :return: The address of this ListAgentProxiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ListAgentProxiesRequest.


        :param address: The address of this ListAgentProxiesRequest.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def name(self):
        """Gets the name of this ListAgentProxiesRequest.  # noqa: E501


        :return: The name of this ListAgentProxiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAgentProxiesRequest.


        :param name: The name of this ListAgentProxiesRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def page_number(self):
        """Gets the page_number of this ListAgentProxiesRequest.  # noqa: E501


        :return: The page_number of this ListAgentProxiesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ListAgentProxiesRequest.


        :param page_number: The page_number of this ListAgentProxiesRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and page_number is None:
            raise ValueError("Invalid value for `page_number`, must not be `None`")  # noqa: E501

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this ListAgentProxiesRequest.  # noqa: E501


        :return: The page_size of this ListAgentProxiesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListAgentProxiesRequest.


        :param page_size: The page_size of this ListAgentProxiesRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and page_size is None:
            raise ValueError("Invalid value for `page_size`, must not be `None`")  # noqa: E501

        self._page_size = page_size

    @property
    def slim(self):
        """Gets the slim of this ListAgentProxiesRequest.  # noqa: E501


        :return: The slim of this ListAgentProxiesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._slim

    @slim.setter
    def slim(self, slim):
        """Sets the slim of this ListAgentProxiesRequest.


        :param slim: The slim of this ListAgentProxiesRequest.  # noqa: E501
        :type: bool
        """

        self._slim = slim

    @property
    def sort_by(self):
        """Gets the sort_by of this ListAgentProxiesRequest.  # noqa: E501


        :return: The sort_by of this ListAgentProxiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this ListAgentProxiesRequest.


        :param sort_by: The sort_by of this ListAgentProxiesRequest.  # noqa: E501
        :type: str
        """

        self._sort_by = sort_by

    @property
    def sort_order(self):
        """Gets the sort_order of this ListAgentProxiesRequest.  # noqa: E501


        :return: The sort_order of this ListAgentProxiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this ListAgentProxiesRequest.


        :param sort_order: The sort_order of this ListAgentProxiesRequest.  # noqa: E501
        :type: str
        """

        self._sort_order = sort_order

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ListAgentProxiesRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListAgentProxiesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListAgentProxiesRequest):
            return True

        return self.to_dict() != other.to_dict()
