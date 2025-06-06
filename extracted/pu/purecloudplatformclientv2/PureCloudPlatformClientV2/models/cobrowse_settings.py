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
    from . import PauseCriteria

class CobrowseSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CobrowseSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'enabled': 'bool',
            'allow_agent_control': 'bool',
            'allow_agent_navigation': 'bool',
            'allow_draw': 'bool',
            'mask_selectors': 'list[str]',
            'channels': 'list[str]',
            'readonly_selectors': 'list[str]',
            'pause_criteria': 'list[PauseCriteria]'
        }

        self.attribute_map = {
            'enabled': 'enabled',
            'allow_agent_control': 'allowAgentControl',
            'allow_agent_navigation': 'allowAgentNavigation',
            'allow_draw': 'allowDraw',
            'mask_selectors': 'maskSelectors',
            'channels': 'channels',
            'readonly_selectors': 'readonlySelectors',
            'pause_criteria': 'pauseCriteria'
        }

        self._enabled = None
        self._allow_agent_control = None
        self._allow_agent_navigation = None
        self._allow_draw = None
        self._mask_selectors = None
        self._channels = None
        self._readonly_selectors = None
        self._pause_criteria = None

    @property
    def enabled(self) -> bool:
        """
        Gets the enabled of this CobrowseSettings.
        Whether or not cobrowse is enabled

        :return: The enabled of this CobrowseSettings.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool) -> None:
        """
        Sets the enabled of this CobrowseSettings.
        Whether or not cobrowse is enabled

        :param enabled: The enabled of this CobrowseSettings.
        :type: bool
        """
        

        self._enabled = enabled

    @property
    def allow_agent_control(self) -> bool:
        """
        Gets the allow_agent_control of this CobrowseSettings.
        Whether the viewer should have option to request control

        :return: The allow_agent_control of this CobrowseSettings.
        :rtype: bool
        """
        return self._allow_agent_control

    @allow_agent_control.setter
    def allow_agent_control(self, allow_agent_control: bool) -> None:
        """
        Sets the allow_agent_control of this CobrowseSettings.
        Whether the viewer should have option to request control

        :param allow_agent_control: The allow_agent_control of this CobrowseSettings.
        :type: bool
        """
        

        self._allow_agent_control = allow_agent_control

    @property
    def allow_agent_navigation(self) -> bool:
        """
        Gets the allow_agent_navigation of this CobrowseSettings.
        Whether the viewer should have option to request navigation

        :return: The allow_agent_navigation of this CobrowseSettings.
        :rtype: bool
        """
        return self._allow_agent_navigation

    @allow_agent_navigation.setter
    def allow_agent_navigation(self, allow_agent_navigation: bool) -> None:
        """
        Sets the allow_agent_navigation of this CobrowseSettings.
        Whether the viewer should have option to request navigation

        :param allow_agent_navigation: The allow_agent_navigation of this CobrowseSettings.
        :type: bool
        """
        

        self._allow_agent_navigation = allow_agent_navigation

    @property
    def allow_draw(self) -> bool:
        """
        Gets the allow_draw of this CobrowseSettings.
        Should cobrowse draw be enabled

        :return: The allow_draw of this CobrowseSettings.
        :rtype: bool
        """
        return self._allow_draw

    @allow_draw.setter
    def allow_draw(self, allow_draw: bool) -> None:
        """
        Sets the allow_draw of this CobrowseSettings.
        Should cobrowse draw be enabled

        :param allow_draw: The allow_draw of this CobrowseSettings.
        :type: bool
        """
        

        self._allow_draw = allow_draw

    @property
    def mask_selectors(self) -> List[str]:
        """
        Gets the mask_selectors of this CobrowseSettings.
        Mask patterns that will apply to pages being shared

        :return: The mask_selectors of this CobrowseSettings.
        :rtype: list[str]
        """
        return self._mask_selectors

    @mask_selectors.setter
    def mask_selectors(self, mask_selectors: List[str]) -> None:
        """
        Sets the mask_selectors of this CobrowseSettings.
        Mask patterns that will apply to pages being shared

        :param mask_selectors: The mask_selectors of this CobrowseSettings.
        :type: list[str]
        """
        

        self._mask_selectors = mask_selectors

    @property
    def channels(self) -> List[str]:
        """
        Gets the channels of this CobrowseSettings.
        Cobrowse channels for web messenger

        :return: The channels of this CobrowseSettings.
        :rtype: list[str]
        """
        return self._channels

    @channels.setter
    def channels(self, channels: List[str]) -> None:
        """
        Sets the channels of this CobrowseSettings.
        Cobrowse channels for web messenger

        :param channels: The channels of this CobrowseSettings.
        :type: list[str]
        """
        

        self._channels = channels

    @property
    def readonly_selectors(self) -> List[str]:
        """
        Gets the readonly_selectors of this CobrowseSettings.
        Readonly patterns that will apply to pages being shared

        :return: The readonly_selectors of this CobrowseSettings.
        :rtype: list[str]
        """
        return self._readonly_selectors

    @readonly_selectors.setter
    def readonly_selectors(self, readonly_selectors: List[str]) -> None:
        """
        Sets the readonly_selectors of this CobrowseSettings.
        Readonly patterns that will apply to pages being shared

        :param readonly_selectors: The readonly_selectors of this CobrowseSettings.
        :type: list[str]
        """
        

        self._readonly_selectors = readonly_selectors

    @property
    def pause_criteria(self) -> List['PauseCriteria']:
        """
        Gets the pause_criteria of this CobrowseSettings.
        Pause criteria that will pause cobrowse if some of them are met in the user's URL

        :return: The pause_criteria of this CobrowseSettings.
        :rtype: list[PauseCriteria]
        """
        return self._pause_criteria

    @pause_criteria.setter
    def pause_criteria(self, pause_criteria: List['PauseCriteria']) -> None:
        """
        Sets the pause_criteria of this CobrowseSettings.
        Pause criteria that will pause cobrowse if some of them are met in the user's URL

        :param pause_criteria: The pause_criteria of this CobrowseSettings.
        :type: list[PauseCriteria]
        """
        

        self._pause_criteria = pause_criteria

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

