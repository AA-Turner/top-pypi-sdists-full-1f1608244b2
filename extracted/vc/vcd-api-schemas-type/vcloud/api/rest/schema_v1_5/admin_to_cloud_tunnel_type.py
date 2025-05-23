"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from .to_cloud_tunnel_type import ToCloudTunnelType


class AdminToCloudTunnelType(ToCloudTunnelType):
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
        'destination_ip_address': 'str',
        'destination_port': 'int',
        'use_ssl': 'bool'
    }

    attribute_map = {
        'destination_ip_address': 'destinationIpAddress',
        'destination_port': 'destinationPort',
        'use_ssl': 'useSsl'
    }

    def __init__(self, destination_ip_address=None,destination_port=None,use_ssl=None):
        self._destination_ip_address = None
        self._destination_port = None
        self._use_ssl = None

        if destination_ip_address is not None:
            self.destination_ip_address = destination_ip_address
        if destination_port is not None:
            self.destination_port = destination_port
        if use_ssl is not None:
            self.use_ssl = use_ssl

    @property
    def destination_ip_address(self):
        return self._destination_ip_address
    
    @destination_ip_address.setter
    def destination_ip_address(self, destination_ip_address):
        self._destination_ip_address = destination_ip_address

    @property
    def destination_port(self):
        return self._destination_port
    
    @destination_port.setter
    def destination_port(self, destination_port):
        self._destination_port = destination_port

    @property
    def use_ssl(self):
        return self._use_ssl
    
    @use_ssl.setter
    def use_ssl(self, use_ssl):
        self._use_ssl = use_ssl


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
        """Returns the string representation of the model"""
        return pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AdminToCloudTunnelType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
