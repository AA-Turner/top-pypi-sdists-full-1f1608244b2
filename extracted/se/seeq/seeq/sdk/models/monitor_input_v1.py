# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 66.26.0-v202506111109-CD
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class MonitorInputV1(object):
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
        'gauges': 'list[GaugeDatumV1]',
        'meters': 'list[MeterDatumV1]',
        'timers': 'list[TimerDatumV1]'
    }

    attribute_map = {
        'gauges': 'gauges',
        'meters': 'meters',
        'timers': 'timers'
    }

    def __init__(self, gauges=None, meters=None, timers=None):
        """
        MonitorInputV1 - a model defined in Swagger
        """

        self._gauges = None
        self._meters = None
        self._timers = None

        if gauges is not None:
          self.gauges = gauges
        if meters is not None:
          self.meters = meters
        if timers is not None:
          self.timers = timers

    @property
    def gauges(self):
        """
        Gets the gauges of this MonitorInputV1.
        List of gauges to update

        :return: The gauges of this MonitorInputV1.
        :rtype: list[GaugeDatumV1]
        """
        return self._gauges

    @gauges.setter
    def gauges(self, gauges):
        """
        Sets the gauges of this MonitorInputV1.
        List of gauges to update

        :param gauges: The gauges of this MonitorInputV1.
        :type: list[GaugeDatumV1]
        """

        self._gauges = gauges

    @property
    def meters(self):
        """
        Gets the meters of this MonitorInputV1.
        List of meters to update

        :return: The meters of this MonitorInputV1.
        :rtype: list[MeterDatumV1]
        """
        return self._meters

    @meters.setter
    def meters(self, meters):
        """
        Sets the meters of this MonitorInputV1.
        List of meters to update

        :param meters: The meters of this MonitorInputV1.
        :type: list[MeterDatumV1]
        """

        self._meters = meters

    @property
    def timers(self):
        """
        Gets the timers of this MonitorInputV1.
        List of timers to update

        :return: The timers of this MonitorInputV1.
        :rtype: list[TimerDatumV1]
        """
        return self._timers

    @timers.setter
    def timers(self, timers):
        """
        Sets the timers of this MonitorInputV1.
        List of timers to update

        :param timers: The timers of this MonitorInputV1.
        :type: list[TimerDatumV1]
        """

        self._timers = timers

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
        if not isinstance(other, MonitorInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
