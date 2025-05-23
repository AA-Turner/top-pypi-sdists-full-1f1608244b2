"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from .network_service_type import NetworkServiceType


class NatServiceType(NetworkServiceType):
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
        'nat_type': 'str',
        'policy': 'str',
        'nat_rule': 'list[NatRuleType]',
        'external_ip': 'str'
    }

    attribute_map = {
        'nat_type': 'natType',
        'policy': 'policy',
        'nat_rule': 'natRule',
        'external_ip': 'externalIp'
    }

    def __init__(self, nat_type=None,policy=None,nat_rule=None,external_ip=None):
        self._nat_type = None
        self._policy = None
        self._nat_rule = None
        self._external_ip = None

        if nat_type is not None:
            self.nat_type = nat_type
        if policy is not None:
            self.policy = policy
        if nat_rule is not None:
            self.nat_rule = nat_rule
        if external_ip is not None:
            self.external_ip = external_ip

    @property
    def nat_type(self):
        return self._nat_type
    
    @nat_type.setter
    def nat_type(self, nat_type):
        self._nat_type = nat_type

    @property
    def policy(self):
        return self._policy
    
    @policy.setter
    def policy(self, policy):
        self._policy = policy

    @property
    def nat_rule(self):
        return self._nat_rule
    
    @nat_rule.setter
    def nat_rule(self, nat_rule):
        self._nat_rule = nat_rule

    @property
    def external_ip(self):
        return self._external_ip
    
    @external_ip.setter
    def external_ip(self, external_ip):
        self._external_ip = external_ip


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
        if not isinstance(other, NatServiceType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
