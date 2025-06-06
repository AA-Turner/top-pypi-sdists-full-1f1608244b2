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
    from . import MessagingInitialConfiguration
    from . import SourceConfiguration

class MessagingExternalEstablishedEvent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        MessagingExternalEstablishedEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'event_id': 'str',
            'event_date_time': 'datetime',
            'conversation_id': 'str',
            'communication_id': 'str',
            'display_name': 'str',
            'initial_configuration': 'MessagingInitialConfiguration',
            'source_configuration': 'SourceConfiguration'
        }

        self.attribute_map = {
            'event_id': 'eventId',
            'event_date_time': 'eventDateTime',
            'conversation_id': 'conversationId',
            'communication_id': 'communicationId',
            'display_name': 'displayName',
            'initial_configuration': 'initialConfiguration',
            'source_configuration': 'sourceConfiguration'
        }

        self._event_id = None
        self._event_date_time = None
        self._conversation_id = None
        self._communication_id = None
        self._display_name = None
        self._initial_configuration = None
        self._source_configuration = None

    @property
    def event_id(self) -> str:
        """
        Gets the event_id of this MessagingExternalEstablishedEvent.
        A unique (V4 UUID) eventId for this event

        :return: The event_id of this MessagingExternalEstablishedEvent.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id: str) -> None:
        """
        Sets the event_id of this MessagingExternalEstablishedEvent.
        A unique (V4 UUID) eventId for this event

        :param event_id: The event_id of this MessagingExternalEstablishedEvent.
        :type: str
        """
        

        self._event_id = event_id

    @property
    def event_date_time(self) -> datetime:
        """
        Gets the event_date_time of this MessagingExternalEstablishedEvent.
        A Date Time representing the time this event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The event_date_time of this MessagingExternalEstablishedEvent.
        :rtype: datetime
        """
        return self._event_date_time

    @event_date_time.setter
    def event_date_time(self, event_date_time: datetime) -> None:
        """
        Sets the event_date_time of this MessagingExternalEstablishedEvent.
        A Date Time representing the time this event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param event_date_time: The event_date_time of this MessagingExternalEstablishedEvent.
        :type: datetime
        """
        

        self._event_date_time = event_date_time

    @property
    def conversation_id(self) -> str:
        """
        Gets the conversation_id of this MessagingExternalEstablishedEvent.
        A unique Id (V4 UUID) identifying this conversation

        :return: The conversation_id of this MessagingExternalEstablishedEvent.
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id: str) -> None:
        """
        Sets the conversation_id of this MessagingExternalEstablishedEvent.
        A unique Id (V4 UUID) identifying this conversation

        :param conversation_id: The conversation_id of this MessagingExternalEstablishedEvent.
        :type: str
        """
        

        self._conversation_id = conversation_id

    @property
    def communication_id(self) -> str:
        """
        Gets the communication_id of this MessagingExternalEstablishedEvent.
        A unique Id (V4 UUID) identifying this communication.

        :return: The communication_id of this MessagingExternalEstablishedEvent.
        :rtype: str
        """
        return self._communication_id

    @communication_id.setter
    def communication_id(self, communication_id: str) -> None:
        """
        Sets the communication_id of this MessagingExternalEstablishedEvent.
        A unique Id (V4 UUID) identifying this communication.

        :param communication_id: The communication_id of this MessagingExternalEstablishedEvent.
        :type: str
        """
        

        self._communication_id = communication_id

    @property
    def display_name(self) -> str:
        """
        Gets the display_name of this MessagingExternalEstablishedEvent.
        A name for the participant if it is available for this conversation.

        :return: The display_name of this MessagingExternalEstablishedEvent.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: str) -> None:
        """
        Sets the display_name of this MessagingExternalEstablishedEvent.
        A name for the participant if it is available for this conversation.

        :param display_name: The display_name of this MessagingExternalEstablishedEvent.
        :type: str
        """
        

        self._display_name = display_name

    @property
    def initial_configuration(self) -> 'MessagingInitialConfiguration':
        """
        Gets the initial_configuration of this MessagingExternalEstablishedEvent.
        Metadata about this communication.

        :return: The initial_configuration of this MessagingExternalEstablishedEvent.
        :rtype: MessagingInitialConfiguration
        """
        return self._initial_configuration

    @initial_configuration.setter
    def initial_configuration(self, initial_configuration: 'MessagingInitialConfiguration') -> None:
        """
        Sets the initial_configuration of this MessagingExternalEstablishedEvent.
        Metadata about this communication.

        :param initial_configuration: The initial_configuration of this MessagingExternalEstablishedEvent.
        :type: MessagingInitialConfiguration
        """
        

        self._initial_configuration = initial_configuration

    @property
    def source_configuration(self) -> 'SourceConfiguration':
        """
        Gets the source_configuration of this MessagingExternalEstablishedEvent.
        Metadata about the source of this communication's interaction.

        :return: The source_configuration of this MessagingExternalEstablishedEvent.
        :rtype: SourceConfiguration
        """
        return self._source_configuration

    @source_configuration.setter
    def source_configuration(self, source_configuration: 'SourceConfiguration') -> None:
        """
        Sets the source_configuration of this MessagingExternalEstablishedEvent.
        Metadata about the source of this communication's interaction.

        :param source_configuration: The source_configuration of this MessagingExternalEstablishedEvent.
        :type: SourceConfiguration
        """
        

        self._source_configuration = source_configuration

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

