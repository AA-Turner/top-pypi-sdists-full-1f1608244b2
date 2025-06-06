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
    from . import BuAbandonRate
    from . import BuAverageSpeedOfAnswer
    from . import BuServiceLevel
    from . import ServiceGoalTemplateImpactOverride

class CreateServiceGoalTemplate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CreateServiceGoalTemplate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'service_level': 'BuServiceLevel',
            'average_speed_of_answer': 'BuAverageSpeedOfAnswer',
            'abandon_rate': 'BuAbandonRate',
            'impact_override': 'ServiceGoalTemplateImpactOverride'
        }

        self.attribute_map = {
            'name': 'name',
            'service_level': 'serviceLevel',
            'average_speed_of_answer': 'averageSpeedOfAnswer',
            'abandon_rate': 'abandonRate',
            'impact_override': 'impactOverride'
        }

        self._name = None
        self._service_level = None
        self._average_speed_of_answer = None
        self._abandon_rate = None
        self._impact_override = None

    @property
    def name(self) -> str:
        """
        Gets the name of this CreateServiceGoalTemplate.
        The name of the service goal template.

        :return: The name of this CreateServiceGoalTemplate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this CreateServiceGoalTemplate.
        The name of the service goal template.

        :param name: The name of this CreateServiceGoalTemplate.
        :type: str
        """
        

        self._name = name

    @property
    def service_level(self) -> 'BuServiceLevel':
        """
        Gets the service_level of this CreateServiceGoalTemplate.
        Service level targets for this service goal template

        :return: The service_level of this CreateServiceGoalTemplate.
        :rtype: BuServiceLevel
        """
        return self._service_level

    @service_level.setter
    def service_level(self, service_level: 'BuServiceLevel') -> None:
        """
        Sets the service_level of this CreateServiceGoalTemplate.
        Service level targets for this service goal template

        :param service_level: The service_level of this CreateServiceGoalTemplate.
        :type: BuServiceLevel
        """
        

        self._service_level = service_level

    @property
    def average_speed_of_answer(self) -> 'BuAverageSpeedOfAnswer':
        """
        Gets the average_speed_of_answer of this CreateServiceGoalTemplate.
        Average speed of answer targets for this service goal template

        :return: The average_speed_of_answer of this CreateServiceGoalTemplate.
        :rtype: BuAverageSpeedOfAnswer
        """
        return self._average_speed_of_answer

    @average_speed_of_answer.setter
    def average_speed_of_answer(self, average_speed_of_answer: 'BuAverageSpeedOfAnswer') -> None:
        """
        Sets the average_speed_of_answer of this CreateServiceGoalTemplate.
        Average speed of answer targets for this service goal template

        :param average_speed_of_answer: The average_speed_of_answer of this CreateServiceGoalTemplate.
        :type: BuAverageSpeedOfAnswer
        """
        

        self._average_speed_of_answer = average_speed_of_answer

    @property
    def abandon_rate(self) -> 'BuAbandonRate':
        """
        Gets the abandon_rate of this CreateServiceGoalTemplate.
        Abandon rate targets for this service goal template

        :return: The abandon_rate of this CreateServiceGoalTemplate.
        :rtype: BuAbandonRate
        """
        return self._abandon_rate

    @abandon_rate.setter
    def abandon_rate(self, abandon_rate: 'BuAbandonRate') -> None:
        """
        Sets the abandon_rate of this CreateServiceGoalTemplate.
        Abandon rate targets for this service goal template

        :param abandon_rate: The abandon_rate of this CreateServiceGoalTemplate.
        :type: BuAbandonRate
        """
        

        self._abandon_rate = abandon_rate

    @property
    def impact_override(self) -> 'ServiceGoalTemplateImpactOverride':
        """
        Gets the impact_override of this CreateServiceGoalTemplate.
        Settings controlling max percent increase and decrease of service goals for this service goal template

        :return: The impact_override of this CreateServiceGoalTemplate.
        :rtype: ServiceGoalTemplateImpactOverride
        """
        return self._impact_override

    @impact_override.setter
    def impact_override(self, impact_override: 'ServiceGoalTemplateImpactOverride') -> None:
        """
        Sets the impact_override of this CreateServiceGoalTemplate.
        Settings controlling max percent increase and decrease of service goals for this service goal template

        :param impact_override: The impact_override of this CreateServiceGoalTemplate.
        :type: ServiceGoalTemplateImpactOverride
        """
        

        self._impact_override = impact_override

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

