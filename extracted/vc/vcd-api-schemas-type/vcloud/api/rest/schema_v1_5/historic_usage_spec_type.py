"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re


class HistoricUsageSpecType(object):
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
        'absolute_start_time': 'AbsoluteTimeType',
        'relative_start_time': 'RelativeTimeType',
        'absolute_end_time': 'AbsoluteTimeType',
        'relative_end_time': 'RelativeTimeType',
        'metric_pattern': 'list[str]'
    }

    attribute_map = {
        'absolute_start_time': 'absoluteStartTime',
        'relative_start_time': 'relativeStartTime',
        'absolute_end_time': 'absoluteEndTime',
        'relative_end_time': 'relativeEndTime',
        'metric_pattern': 'metricPattern'
    }

    def __init__(self, absolute_start_time=None,relative_start_time=None,absolute_end_time=None,relative_end_time=None,metric_pattern=None):
        self._absolute_start_time = None
        self._relative_start_time = None
        self._absolute_end_time = None
        self._relative_end_time = None
        self._metric_pattern = None

        if absolute_start_time is not None:
            self.absolute_start_time = absolute_start_time
        if relative_start_time is not None:
            self.relative_start_time = relative_start_time
        if absolute_end_time is not None:
            self.absolute_end_time = absolute_end_time
        if relative_end_time is not None:
            self.relative_end_time = relative_end_time
        if metric_pattern is not None:
            self.metric_pattern = metric_pattern

    @property
    def absolute_start_time(self):
        return self._absolute_start_time
    
    @absolute_start_time.setter
    def absolute_start_time(self, absolute_start_time):
        self._absolute_start_time = absolute_start_time

    @property
    def relative_start_time(self):
        return self._relative_start_time
    
    @relative_start_time.setter
    def relative_start_time(self, relative_start_time):
        self._relative_start_time = relative_start_time

    @property
    def absolute_end_time(self):
        return self._absolute_end_time
    
    @absolute_end_time.setter
    def absolute_end_time(self, absolute_end_time):
        self._absolute_end_time = absolute_end_time

    @property
    def relative_end_time(self):
        return self._relative_end_time
    
    @relative_end_time.setter
    def relative_end_time(self, relative_end_time):
        self._relative_end_time = relative_end_time

    @property
    def metric_pattern(self):
        return self._metric_pattern
    
    @metric_pattern.setter
    def metric_pattern(self, metric_pattern):
        self._metric_pattern = metric_pattern


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
        if not isinstance(other, HistoricUsageSpecType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
