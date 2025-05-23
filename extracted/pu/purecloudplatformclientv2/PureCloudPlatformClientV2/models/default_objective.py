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
    from . import AddressableEntityRef
    from . import ObjectiveZone

class DefaultObjective(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        DefaultObjective - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'template_id': 'str',
            'zones': 'list[ObjectiveZone]',
            'enabled': 'bool',
            'media_types': 'list[str]',
            'queues': 'list[AddressableEntityRef]',
            'topics': 'list[AddressableEntityRef]',
            'topic_ids_filter_type': 'str',
            'evaluation_form_context_ids': 'list[str]',
            'initial_direction': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'template_id': 'templateId',
            'zones': 'zones',
            'enabled': 'enabled',
            'media_types': 'mediaTypes',
            'queues': 'queues',
            'topics': 'topics',
            'topic_ids_filter_type': 'topicIdsFilterType',
            'evaluation_form_context_ids': 'evaluationFormContextIds',
            'initial_direction': 'initialDirection'
        }

        self._id = None
        self._template_id = None
        self._zones = None
        self._enabled = None
        self._media_types = None
        self._queues = None
        self._topics = None
        self._topic_ids_filter_type = None
        self._evaluation_form_context_ids = None
        self._initial_direction = None

    @property
    def id(self) -> str:
        """
        Gets the id of this DefaultObjective.
        The globally unique identifier for the object.

        :return: The id of this DefaultObjective.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this DefaultObjective.
        The globally unique identifier for the object.

        :param id: The id of this DefaultObjective.
        :type: str
        """
        

        self._id = id

    @property
    def template_id(self) -> str:
        """
        Gets the template_id of this DefaultObjective.
        The id of this objective's base template

        :return: The template_id of this DefaultObjective.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id: str) -> None:
        """
        Sets the template_id of this DefaultObjective.
        The id of this objective's base template

        :param template_id: The template_id of this DefaultObjective.
        :type: str
        """
        

        self._template_id = template_id

    @property
    def zones(self) -> List['ObjectiveZone']:
        """
        Gets the zones of this DefaultObjective.
        Objective zone specifies min,max points and values for the associated metric

        :return: The zones of this DefaultObjective.
        :rtype: list[ObjectiveZone]
        """
        return self._zones

    @zones.setter
    def zones(self, zones: List['ObjectiveZone']) -> None:
        """
        Sets the zones of this DefaultObjective.
        Objective zone specifies min,max points and values for the associated metric

        :param zones: The zones of this DefaultObjective.
        :type: list[ObjectiveZone]
        """
        

        self._zones = zones

    @property
    def enabled(self) -> bool:
        """
        Gets the enabled of this DefaultObjective.
        A flag for whether this objective is enabled for the related metric

        :return: The enabled of this DefaultObjective.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool) -> None:
        """
        Sets the enabled of this DefaultObjective.
        A flag for whether this objective is enabled for the related metric

        :param enabled: The enabled of this DefaultObjective.
        :type: bool
        """
        

        self._enabled = enabled

    @property
    def media_types(self) -> List[str]:
        """
        Gets the media_types of this DefaultObjective.
        A list of media types for the metric

        :return: The media_types of this DefaultObjective.
        :rtype: list[str]
        """
        return self._media_types

    @media_types.setter
    def media_types(self, media_types: List[str]) -> None:
        """
        Sets the media_types of this DefaultObjective.
        A list of media types for the metric

        :param media_types: The media_types of this DefaultObjective.
        :type: list[str]
        """
        

        self._media_types = media_types

    @property
    def queues(self) -> List['AddressableEntityRef']:
        """
        Gets the queues of this DefaultObjective.
        A list of queues for the metric

        :return: The queues of this DefaultObjective.
        :rtype: list[AddressableEntityRef]
        """
        return self._queues

    @queues.setter
    def queues(self, queues: List['AddressableEntityRef']) -> None:
        """
        Sets the queues of this DefaultObjective.
        A list of queues for the metric

        :param queues: The queues of this DefaultObjective.
        :type: list[AddressableEntityRef]
        """
        

        self._queues = queues

    @property
    def topics(self) -> List['AddressableEntityRef']:
        """
        Gets the topics of this DefaultObjective.
        A list of topic ids for detected topic metrics

        :return: The topics of this DefaultObjective.
        :rtype: list[AddressableEntityRef]
        """
        return self._topics

    @topics.setter
    def topics(self, topics: List['AddressableEntityRef']) -> None:
        """
        Sets the topics of this DefaultObjective.
        A list of topic ids for detected topic metrics

        :param topics: The topics of this DefaultObjective.
        :type: list[AddressableEntityRef]
        """
        

        self._topics = topics

    @property
    def topic_ids_filter_type(self) -> str:
        """
        Gets the topic_ids_filter_type of this DefaultObjective.
        A filter type for topic Ids. It's only used for objectives with topicIds. Default filter behavior is \"or\".

        :return: The topic_ids_filter_type of this DefaultObjective.
        :rtype: str
        """
        return self._topic_ids_filter_type

    @topic_ids_filter_type.setter
    def topic_ids_filter_type(self, topic_ids_filter_type: str) -> None:
        """
        Sets the topic_ids_filter_type of this DefaultObjective.
        A filter type for topic Ids. It's only used for objectives with topicIds. Default filter behavior is \"or\".

        :param topic_ids_filter_type: The topic_ids_filter_type of this DefaultObjective.
        :type: str
        """
        if isinstance(topic_ids_filter_type, int):
            topic_ids_filter_type = str(topic_ids_filter_type)
        allowed_values = ["and", "or"]
        if topic_ids_filter_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for topic_ids_filter_type -> " + topic_ids_filter_type)
            self._topic_ids_filter_type = "outdated_sdk_version"
        else:
            self._topic_ids_filter_type = topic_ids_filter_type

    @property
    def evaluation_form_context_ids(self) -> List[str]:
        """
        Gets the evaluation_form_context_ids of this DefaultObjective.
        The ids of associated evaluation form context, for Quality Evaluation Score metrics

        :return: The evaluation_form_context_ids of this DefaultObjective.
        :rtype: list[str]
        """
        return self._evaluation_form_context_ids

    @evaluation_form_context_ids.setter
    def evaluation_form_context_ids(self, evaluation_form_context_ids: List[str]) -> None:
        """
        Sets the evaluation_form_context_ids of this DefaultObjective.
        The ids of associated evaluation form context, for Quality Evaluation Score metrics

        :param evaluation_form_context_ids: The evaluation_form_context_ids of this DefaultObjective.
        :type: list[str]
        """
        

        self._evaluation_form_context_ids = evaluation_form_context_ids

    @property
    def initial_direction(self) -> str:
        """
        Gets the initial_direction of this DefaultObjective.
        The initial direction to filter on

        :return: The initial_direction of this DefaultObjective.
        :rtype: str
        """
        return self._initial_direction

    @initial_direction.setter
    def initial_direction(self, initial_direction: str) -> None:
        """
        Sets the initial_direction of this DefaultObjective.
        The initial direction to filter on

        :param initial_direction: The initial_direction of this DefaultObjective.
        :type: str
        """
        if isinstance(initial_direction, int):
            initial_direction = str(initial_direction)
        allowed_values = ["inbound", "outbound"]
        if initial_direction.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for initial_direction -> " + initial_direction)
            self._initial_direction = "outdated_sdk_version"
        else:
            self._initial_direction = initial_direction

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

