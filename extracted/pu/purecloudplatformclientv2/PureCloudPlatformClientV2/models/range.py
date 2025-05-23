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


class Range(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Range - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'end': 'str',
            'number_of_occurrences': 'int'
        }

        self.attribute_map = {
            'type': 'type',
            'end': 'end',
            'number_of_occurrences': 'numberOfOccurrences'
        }

        self._type = None
        self._end = None
        self._number_of_occurrences = None

    @property
    def type(self) -> str:
        """
        Gets the type of this Range.
        Range type (NoEnd: without an end date. EndDate: with an end date. Numbered: with a specific number of occurrences)

        :return: The type of this Range.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this Range.
        Range type (NoEnd: without an end date. EndDate: with an end date. Numbered: with a specific number of occurrences)

        :param type: The type of this Range.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["NoEnd", "EndDate", "Numbered"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def end(self) -> str:
        """
        Gets the end of this Range.
        The end date time of the last occurrence of the range as an ISO-8601 string. Required for EndDate range type.

        :return: The end of this Range.
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end: str) -> None:
        """
        Sets the end of this Range.
        The end date time of the last occurrence of the range as an ISO-8601 string. Required for EndDate range type.

        :param end: The end of this Range.
        :type: str
        """
        

        self._end = end

    @property
    def number_of_occurrences(self) -> int:
        """
        Gets the number_of_occurrences of this Range.
        The number of times the schedule will be repeated, e.g: 2. Required to set for Numbered range type.

        :return: The number_of_occurrences of this Range.
        :rtype: int
        """
        return self._number_of_occurrences

    @number_of_occurrences.setter
    def number_of_occurrences(self, number_of_occurrences: int) -> None:
        """
        Sets the number_of_occurrences of this Range.
        The number of times the schedule will be repeated, e.g: 2. Required to set for Numbered range type.

        :param number_of_occurrences: The number_of_occurrences of this Range.
        :type: int
        """
        

        self._number_of_occurrences = number_of_occurrences

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

