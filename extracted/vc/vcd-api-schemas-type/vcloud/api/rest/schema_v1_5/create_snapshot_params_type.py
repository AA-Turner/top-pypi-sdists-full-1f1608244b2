"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from .params_type import ParamsType


class CreateSnapshotParamsType(ParamsType):
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
        'memory': 'bool',
        'quiesce': 'bool'
    }

    attribute_map = {
        'memory': 'memory',
        'quiesce': 'quiesce'
    }

    def __init__(self, memory=None,quiesce=None):
        self._memory = None
        self._quiesce = None

        if memory is not None:
            self.memory = memory
        if quiesce is not None:
            self.quiesce = quiesce

    @property
    def memory(self):
        return self._memory
    
    @memory.setter
    def memory(self, memory):
        self._memory = memory

    @property
    def quiesce(self):
        return self._quiesce
    
    @quiesce.setter
    def quiesce(self, quiesce):
        self._quiesce = quiesce


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
        if not isinstance(other, CreateSnapshotParamsType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
