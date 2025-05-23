"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from .vdc_template_specification_type import VdcTemplateSpecificationType


class ReservationPoolVdcTemplateSpecificationType(VdcTemplateSpecificationType):
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
        'cpu_allocation_mhz': 'int',
        'cpu_limit_mhz': 'int',
        'memory_allocation_mb': 'int'
    }

    attribute_map = {
        'cpu_allocation_mhz': 'cpuAllocationMhz',
        'cpu_limit_mhz': 'cpuLimitMhz',
        'memory_allocation_mb': 'memoryAllocationMB'
    }

    def __init__(self, cpu_allocation_mhz=None,cpu_limit_mhz=None,memory_allocation_mb=None):
        self._cpu_allocation_mhz = None
        self._cpu_limit_mhz = None
        self._memory_allocation_mb = None

        if cpu_allocation_mhz is not None:
            self.cpu_allocation_mhz = cpu_allocation_mhz
        if cpu_limit_mhz is not None:
            self.cpu_limit_mhz = cpu_limit_mhz
        if memory_allocation_mb is not None:
            self.memory_allocation_mb = memory_allocation_mb

    @property
    def cpu_allocation_mhz(self):
        return self._cpu_allocation_mhz
    
    @cpu_allocation_mhz.setter
    def cpu_allocation_mhz(self, cpu_allocation_mhz):
        self._cpu_allocation_mhz = cpu_allocation_mhz

    @property
    def cpu_limit_mhz(self):
        return self._cpu_limit_mhz
    
    @cpu_limit_mhz.setter
    def cpu_limit_mhz(self, cpu_limit_mhz):
        self._cpu_limit_mhz = cpu_limit_mhz

    @property
    def memory_allocation_mb(self):
        return self._memory_allocation_mb
    
    @memory_allocation_mb.setter
    def memory_allocation_mb(self, memory_allocation_mb):
        self._memory_allocation_mb = memory_allocation_mb


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
        if not isinstance(other, ReservationPoolVdcTemplateSpecificationType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
