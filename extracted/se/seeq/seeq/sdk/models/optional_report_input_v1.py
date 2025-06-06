# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 66.25.0-v202506042330-CD
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class OptionalReportInputV1(object):
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
        'background': 'bool',
        'cron_schedule': 'list[str]',
        'enabled': 'bool',
        'step_to_now': 'bool'
    }

    attribute_map = {
        'background': 'background',
        'cron_schedule': 'cronSchedule',
        'enabled': 'enabled',
        'step_to_now': 'stepToNow'
    }

    def __init__(self, background=False, cron_schedule=None, enabled=True, step_to_now=False):
        """
        OptionalReportInputV1 - a model defined in Swagger
        """

        self._background = None
        self._cron_schedule = None
        self._enabled = None
        self._step_to_now = None

        if background is not None:
          self.background = background
        if cron_schedule is not None:
          self.cron_schedule = cron_schedule
        if enabled is not None:
          self.enabled = enabled
        if step_to_now is not None:
          self.step_to_now = step_to_now

    @property
    def background(self):
        """
        Gets the background of this OptionalReportInputV1.
        Whether the report, if scheduled, should continue to update if there are no subscribers(i.e. in the background)

        :return: The background of this OptionalReportInputV1.
        :rtype: bool
        """
        return self._background

    @background.setter
    def background(self, background):
        """
        Sets the background of this OptionalReportInputV1.
        Whether the report, if scheduled, should continue to update if there are no subscribers(i.e. in the background)

        :param background: The background of this OptionalReportInputV1.
        :type: bool
        """

        self._background = background

    @property
    def cron_schedule(self):
        """
        Gets the cron_schedule of this OptionalReportInputV1.
        The report's update schedule as a cron expression (see http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html)

        :return: The cron_schedule of this OptionalReportInputV1.
        :rtype: list[str]
        """
        return self._cron_schedule

    @cron_schedule.setter
    def cron_schedule(self, cron_schedule):
        """
        Sets the cron_schedule of this OptionalReportInputV1.
        The report's update schedule as a cron expression (see http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html)

        :param cron_schedule: The cron_schedule of this OptionalReportInputV1.
        :type: list[str]
        """

        self._cron_schedule = cron_schedule

    @property
    def enabled(self):
        """
        Gets the enabled of this OptionalReportInputV1.
        Whether the report is enabled to run jobs

        :return: The enabled of this OptionalReportInputV1.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this OptionalReportInputV1.
        Whether the report is enabled to run jobs

        :param enabled: The enabled of this OptionalReportInputV1.
        :type: bool
        """

        self._enabled = enabled

    @property
    def step_to_now(self):
        """
        Gets the step_to_now of this OptionalReportInputV1.
        Whether the scheduled report should update its value for 'now'

        :return: The step_to_now of this OptionalReportInputV1.
        :rtype: bool
        """
        return self._step_to_now

    @step_to_now.setter
    def step_to_now(self, step_to_now):
        """
        Sets the step_to_now of this OptionalReportInputV1.
        Whether the scheduled report should update its value for 'now'

        :param step_to_now: The step_to_now of this OptionalReportInputV1.
        :type: bool
        """

        self._step_to_now = step_to_now

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
        if not isinstance(other, OptionalReportInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
