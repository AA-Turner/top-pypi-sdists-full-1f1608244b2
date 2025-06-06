# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from datetime import datetime
from datetime import date
from pprint import pformat
import re
import json

from ..utils import sanitize_for_serialization

# type hinting support
from typing import TYPE_CHECKING
from typing import List
from typing import Dict

if TYPE_CHECKING:
    from . import AgentWorkPlanShift
    from . import SetWrapperDayOfWeek

class AgentWorkPlan(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        AgentWorkPlan - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'constrain_weekly_paid_time': 'bool',
            'flexible_weekly_paid_time': 'bool',
            'weekly_exact_paid_minutes': 'int',
            'weekly_minimum_paid_minutes': 'int',
            'weekly_maximum_paid_minutes': 'int',
            'optional_days': 'SetWrapperDayOfWeek',
            'shifts': 'list[AgentWorkPlanShift]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'constrain_weekly_paid_time': 'constrainWeeklyPaidTime',
            'flexible_weekly_paid_time': 'flexibleWeeklyPaidTime',
            'weekly_exact_paid_minutes': 'weeklyExactPaidMinutes',
            'weekly_minimum_paid_minutes': 'weeklyMinimumPaidMinutes',
            'weekly_maximum_paid_minutes': 'weeklyMaximumPaidMinutes',
            'optional_days': 'optionalDays',
            'shifts': 'shifts',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._constrain_weekly_paid_time = None
        self._flexible_weekly_paid_time = None
        self._weekly_exact_paid_minutes = None
        self._weekly_minimum_paid_minutes = None
        self._weekly_maximum_paid_minutes = None
        self._optional_days = None
        self._shifts = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this AgentWorkPlan.
        The globally unique identifier for the object.

        :return: The id of this AgentWorkPlan.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this AgentWorkPlan.
        The globally unique identifier for the object.

        :param id: The id of this AgentWorkPlan.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this AgentWorkPlan.


        :return: The name of this AgentWorkPlan.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this AgentWorkPlan.


        :param name: The name of this AgentWorkPlan.
        :type: str
        """
        

        self._name = name

    @property
    def constrain_weekly_paid_time(self) -> bool:
        """
        Gets the constrain_weekly_paid_time of this AgentWorkPlan.
        Whether the weekly paid time constraint is enabled for this work plan

        :return: The constrain_weekly_paid_time of this AgentWorkPlan.
        :rtype: bool
        """
        return self._constrain_weekly_paid_time

    @constrain_weekly_paid_time.setter
    def constrain_weekly_paid_time(self, constrain_weekly_paid_time: bool) -> None:
        """
        Sets the constrain_weekly_paid_time of this AgentWorkPlan.
        Whether the weekly paid time constraint is enabled for this work plan

        :param constrain_weekly_paid_time: The constrain_weekly_paid_time of this AgentWorkPlan.
        :type: bool
        """
        

        self._constrain_weekly_paid_time = constrain_weekly_paid_time

    @property
    def flexible_weekly_paid_time(self) -> bool:
        """
        Gets the flexible_weekly_paid_time of this AgentWorkPlan.
        Whether the weekly paid time constraint is flexible for this work plan

        :return: The flexible_weekly_paid_time of this AgentWorkPlan.
        :rtype: bool
        """
        return self._flexible_weekly_paid_time

    @flexible_weekly_paid_time.setter
    def flexible_weekly_paid_time(self, flexible_weekly_paid_time: bool) -> None:
        """
        Sets the flexible_weekly_paid_time of this AgentWorkPlan.
        Whether the weekly paid time constraint is flexible for this work plan

        :param flexible_weekly_paid_time: The flexible_weekly_paid_time of this AgentWorkPlan.
        :type: bool
        """
        

        self._flexible_weekly_paid_time = flexible_weekly_paid_time

    @property
    def weekly_exact_paid_minutes(self) -> int:
        """
        Gets the weekly_exact_paid_minutes of this AgentWorkPlan.
        Exact weekly paid time in minutes for this work plan. Used if flexibleWeeklyPaidTime == false

        :return: The weekly_exact_paid_minutes of this AgentWorkPlan.
        :rtype: int
        """
        return self._weekly_exact_paid_minutes

    @weekly_exact_paid_minutes.setter
    def weekly_exact_paid_minutes(self, weekly_exact_paid_minutes: int) -> None:
        """
        Sets the weekly_exact_paid_minutes of this AgentWorkPlan.
        Exact weekly paid time in minutes for this work plan. Used if flexibleWeeklyPaidTime == false

        :param weekly_exact_paid_minutes: The weekly_exact_paid_minutes of this AgentWorkPlan.
        :type: int
        """
        

        self._weekly_exact_paid_minutes = weekly_exact_paid_minutes

    @property
    def weekly_minimum_paid_minutes(self) -> int:
        """
        Gets the weekly_minimum_paid_minutes of this AgentWorkPlan.
        Minimum weekly paid time in minutes for this work plan. Used if flexibleWeeklyPaidTime == true

        :return: The weekly_minimum_paid_minutes of this AgentWorkPlan.
        :rtype: int
        """
        return self._weekly_minimum_paid_minutes

    @weekly_minimum_paid_minutes.setter
    def weekly_minimum_paid_minutes(self, weekly_minimum_paid_minutes: int) -> None:
        """
        Sets the weekly_minimum_paid_minutes of this AgentWorkPlan.
        Minimum weekly paid time in minutes for this work plan. Used if flexibleWeeklyPaidTime == true

        :param weekly_minimum_paid_minutes: The weekly_minimum_paid_minutes of this AgentWorkPlan.
        :type: int
        """
        

        self._weekly_minimum_paid_minutes = weekly_minimum_paid_minutes

    @property
    def weekly_maximum_paid_minutes(self) -> int:
        """
        Gets the weekly_maximum_paid_minutes of this AgentWorkPlan.
        Maximum weekly paid time in minutes for this work plan. Used if flexibleWeeklyPaidTime == true

        :return: The weekly_maximum_paid_minutes of this AgentWorkPlan.
        :rtype: int
        """
        return self._weekly_maximum_paid_minutes

    @weekly_maximum_paid_minutes.setter
    def weekly_maximum_paid_minutes(self, weekly_maximum_paid_minutes: int) -> None:
        """
        Sets the weekly_maximum_paid_minutes of this AgentWorkPlan.
        Maximum weekly paid time in minutes for this work plan. Used if flexibleWeeklyPaidTime == true

        :param weekly_maximum_paid_minutes: The weekly_maximum_paid_minutes of this AgentWorkPlan.
        :type: int
        """
        

        self._weekly_maximum_paid_minutes = weekly_maximum_paid_minutes

    @property
    def optional_days(self) -> 'SetWrapperDayOfWeek':
        """
        Gets the optional_days of this AgentWorkPlan.
        Optional days to schedule for this work plan

        :return: The optional_days of this AgentWorkPlan.
        :rtype: SetWrapperDayOfWeek
        """
        return self._optional_days

    @optional_days.setter
    def optional_days(self, optional_days: 'SetWrapperDayOfWeek') -> None:
        """
        Sets the optional_days of this AgentWorkPlan.
        Optional days to schedule for this work plan

        :param optional_days: The optional_days of this AgentWorkPlan.
        :type: SetWrapperDayOfWeek
        """
        

        self._optional_days = optional_days

    @property
    def shifts(self) -> List['AgentWorkPlanShift']:
        """
        Gets the shifts of this AgentWorkPlan.
        Shifts in this work plan

        :return: The shifts of this AgentWorkPlan.
        :rtype: list[AgentWorkPlanShift]
        """
        return self._shifts

    @shifts.setter
    def shifts(self, shifts: List['AgentWorkPlanShift']) -> None:
        """
        Sets the shifts of this AgentWorkPlan.
        Shifts in this work plan

        :param shifts: The shifts of this AgentWorkPlan.
        :type: list[AgentWorkPlanShift]
        """
        

        self._shifts = shifts

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this AgentWorkPlan.
        The URI for this object

        :return: The self_uri of this AgentWorkPlan.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this AgentWorkPlan.
        The URI for this object

        :param self_uri: The self_uri of this AgentWorkPlan.
        :type: str
        """
        

        self._self_uri = self_uri

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in self.swagger_types.items():
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

    def to_json(self):
        """
        Returns the model as raw JSON
        """
        return json.dumps(sanitize_for_serialization(self.to_dict()))

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

