# coding: utf-8

"""
    Cudo Compute service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cudo_compute.configuration import Configuration


class CreateNetworkBody(object):
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
        'data_center_id': 'str',
        'id': 'str',
        'cidr_prefix': 'str',
        'vrouter_size': 'V1VRouterSize'
    }

    attribute_map = {
        'data_center_id': 'dataCenterId',
        'id': 'id',
        'cidr_prefix': 'cidrPrefix',
        'vrouter_size': 'vrouterSize'
    }

    def __init__(self, data_center_id=None, id=None, cidr_prefix=None, vrouter_size=None, _configuration=None):  # noqa: E501
        """CreateNetworkBody - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._data_center_id = None
        self._id = None
        self._cidr_prefix = None
        self._vrouter_size = None
        self.discriminator = None

        self.data_center_id = data_center_id
        self.id = id
        self.cidr_prefix = cidr_prefix
        if vrouter_size is not None:
            self.vrouter_size = vrouter_size

    @property
    def data_center_id(self):
        """Gets the data_center_id of this CreateNetworkBody.  # noqa: E501


        :return: The data_center_id of this CreateNetworkBody.  # noqa: E501
        :rtype: str
        """
        return self._data_center_id

    @data_center_id.setter
    def data_center_id(self, data_center_id):
        """Sets the data_center_id of this CreateNetworkBody.


        :param data_center_id: The data_center_id of this CreateNetworkBody.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and data_center_id is None:
            raise ValueError("Invalid value for `data_center_id`, must not be `None`")  # noqa: E501

        self._data_center_id = data_center_id

    @property
    def id(self):
        """Gets the id of this CreateNetworkBody.  # noqa: E501


        :return: The id of this CreateNetworkBody.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateNetworkBody.


        :param id: The id of this CreateNetworkBody.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def cidr_prefix(self):
        """Gets the cidr_prefix of this CreateNetworkBody.  # noqa: E501


        :return: The cidr_prefix of this CreateNetworkBody.  # noqa: E501
        :rtype: str
        """
        return self._cidr_prefix

    @cidr_prefix.setter
    def cidr_prefix(self, cidr_prefix):
        """Sets the cidr_prefix of this CreateNetworkBody.


        :param cidr_prefix: The cidr_prefix of this CreateNetworkBody.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cidr_prefix is None:
            raise ValueError("Invalid value for `cidr_prefix`, must not be `None`")  # noqa: E501

        self._cidr_prefix = cidr_prefix

    @property
    def vrouter_size(self):
        """Gets the vrouter_size of this CreateNetworkBody.  # noqa: E501


        :return: The vrouter_size of this CreateNetworkBody.  # noqa: E501
        :rtype: V1VRouterSize
        """
        return self._vrouter_size

    @vrouter_size.setter
    def vrouter_size(self, vrouter_size):
        """Sets the vrouter_size of this CreateNetworkBody.


        :param vrouter_size: The vrouter_size of this CreateNetworkBody.  # noqa: E501
        :type: V1VRouterSize
        """

        self._vrouter_size = vrouter_size

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
        if issubclass(CreateNetworkBody, dict):
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
        if not isinstance(other, CreateNetworkBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateNetworkBody):
            return True

        return self.to_dict() != other.to_dict()
