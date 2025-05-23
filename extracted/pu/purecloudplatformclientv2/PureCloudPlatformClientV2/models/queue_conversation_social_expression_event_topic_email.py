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
    from . import QueueConversationSocialExpressionEventTopicAfterCallWork
    from . import QueueConversationSocialExpressionEventTopicAttachment
    from . import QueueConversationSocialExpressionEventTopicErrorDetails
    from . import QueueConversationSocialExpressionEventTopicQueueMediaSettings
    from . import QueueConversationSocialExpressionEventTopicWrapup

class QueueConversationSocialExpressionEventTopicEmail(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        QueueConversationSocialExpressionEventTopicEmail - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'state': 'str',
            'initial_state': 'str',
            'held': 'bool',
            'auto_generated': 'bool',
            'subject': 'str',
            'provider': 'str',
            'script_id': 'str',
            'peer_id': 'str',
            'messages_sent': 'int',
            'error_info': 'QueueConversationSocialExpressionEventTopicErrorDetails',
            'disconnect_type': 'str',
            'start_hold_time': 'datetime',
            'connected_time': 'datetime',
            'disconnected_time': 'datetime',
            'message_id': 'str',
            'direction': 'str',
            'draft_attachments': 'list[QueueConversationSocialExpressionEventTopicAttachment]',
            'spam': 'bool',
            'wrapup': 'QueueConversationSocialExpressionEventTopicWrapup',
            'after_call_work': 'QueueConversationSocialExpressionEventTopicAfterCallWork',
            'after_call_work_required': 'bool',
            'queue_media_settings': 'QueueConversationSocialExpressionEventTopicQueueMediaSettings',
            'resume_time': 'datetime',
            'park_time': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'state': 'state',
            'initial_state': 'initialState',
            'held': 'held',
            'auto_generated': 'autoGenerated',
            'subject': 'subject',
            'provider': 'provider',
            'script_id': 'scriptId',
            'peer_id': 'peerId',
            'messages_sent': 'messagesSent',
            'error_info': 'errorInfo',
            'disconnect_type': 'disconnectType',
            'start_hold_time': 'startHoldTime',
            'connected_time': 'connectedTime',
            'disconnected_time': 'disconnectedTime',
            'message_id': 'messageId',
            'direction': 'direction',
            'draft_attachments': 'draftAttachments',
            'spam': 'spam',
            'wrapup': 'wrapup',
            'after_call_work': 'afterCallWork',
            'after_call_work_required': 'afterCallWorkRequired',
            'queue_media_settings': 'queueMediaSettings',
            'resume_time': 'resumeTime',
            'park_time': 'parkTime'
        }

        self._id = None
        self._state = None
        self._initial_state = None
        self._held = None
        self._auto_generated = None
        self._subject = None
        self._provider = None
        self._script_id = None
        self._peer_id = None
        self._messages_sent = None
        self._error_info = None
        self._disconnect_type = None
        self._start_hold_time = None
        self._connected_time = None
        self._disconnected_time = None
        self._message_id = None
        self._direction = None
        self._draft_attachments = None
        self._spam = None
        self._wrapup = None
        self._after_call_work = None
        self._after_call_work_required = None
        self._queue_media_settings = None
        self._resume_time = None
        self._park_time = None

    @property
    def id(self) -> str:
        """
        Gets the id of this QueueConversationSocialExpressionEventTopicEmail.
        A globally unique identifier for this communication.

        :return: The id of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this QueueConversationSocialExpressionEventTopicEmail.
        A globally unique identifier for this communication.

        :param id: The id of this QueueConversationSocialExpressionEventTopicEmail.
        :type: str
        """
        

        self._id = id

    @property
    def state(self) -> str:
        """
        Gets the state of this QueueConversationSocialExpressionEventTopicEmail.


        :return: The state of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this QueueConversationSocialExpressionEventTopicEmail.


        :param state: The state of this QueueConversationSocialExpressionEventTopicEmail.
        :type: str
        """
        if isinstance(state, int):
            state = str(state)
        allowed_values = ["alerting", "connected", "disconnected", "none", "transmitting", "parked"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def initial_state(self) -> str:
        """
        Gets the initial_state of this QueueConversationSocialExpressionEventTopicEmail.


        :return: The initial_state of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: str
        """
        return self._initial_state

    @initial_state.setter
    def initial_state(self, initial_state: str) -> None:
        """
        Sets the initial_state of this QueueConversationSocialExpressionEventTopicEmail.


        :param initial_state: The initial_state of this QueueConversationSocialExpressionEventTopicEmail.
        :type: str
        """
        if isinstance(initial_state, int):
            initial_state = str(initial_state)
        allowed_values = ["alerting", "connected", "disconnected", "none", "transmitting", "parked"]
        if initial_state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for initial_state -> " + initial_state)
            self._initial_state = "outdated_sdk_version"
        else:
            self._initial_state = initial_state

    @property
    def held(self) -> bool:
        """
        Gets the held of this QueueConversationSocialExpressionEventTopicEmail.
        True if this call is held and the person on this side hears silence.

        :return: The held of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: bool
        """
        return self._held

    @held.setter
    def held(self, held: bool) -> None:
        """
        Sets the held of this QueueConversationSocialExpressionEventTopicEmail.
        True if this call is held and the person on this side hears silence.

        :param held: The held of this QueueConversationSocialExpressionEventTopicEmail.
        :type: bool
        """
        

        self._held = held

    @property
    def auto_generated(self) -> bool:
        """
        Gets the auto_generated of this QueueConversationSocialExpressionEventTopicEmail.
        Indicates that the email was auto-generated like an Out of Office reply.

        :return: The auto_generated of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: bool
        """
        return self._auto_generated

    @auto_generated.setter
    def auto_generated(self, auto_generated: bool) -> None:
        """
        Sets the auto_generated of this QueueConversationSocialExpressionEventTopicEmail.
        Indicates that the email was auto-generated like an Out of Office reply.

        :param auto_generated: The auto_generated of this QueueConversationSocialExpressionEventTopicEmail.
        :type: bool
        """
        

        self._auto_generated = auto_generated

    @property
    def subject(self) -> str:
        """
        Gets the subject of this QueueConversationSocialExpressionEventTopicEmail.
        The subject for the initial email that started this conversation.

        :return: The subject of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject: str) -> None:
        """
        Sets the subject of this QueueConversationSocialExpressionEventTopicEmail.
        The subject for the initial email that started this conversation.

        :param subject: The subject of this QueueConversationSocialExpressionEventTopicEmail.
        :type: str
        """
        

        self._subject = subject

    @property
    def provider(self) -> str:
        """
        Gets the provider of this QueueConversationSocialExpressionEventTopicEmail.
        The source provider of the email.

        :return: The provider of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider: str) -> None:
        """
        Sets the provider of this QueueConversationSocialExpressionEventTopicEmail.
        The source provider of the email.

        :param provider: The provider of this QueueConversationSocialExpressionEventTopicEmail.
        :type: str
        """
        

        self._provider = provider

    @property
    def script_id(self) -> str:
        """
        Gets the script_id of this QueueConversationSocialExpressionEventTopicEmail.
        The UUID of the script to use.

        :return: The script_id of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id: str) -> None:
        """
        Sets the script_id of this QueueConversationSocialExpressionEventTopicEmail.
        The UUID of the script to use.

        :param script_id: The script_id of this QueueConversationSocialExpressionEventTopicEmail.
        :type: str
        """
        

        self._script_id = script_id

    @property
    def peer_id(self) -> str:
        """
        Gets the peer_id of this QueueConversationSocialExpressionEventTopicEmail.
        The id of the peer communication corresponding to a matching leg for this communication.

        :return: The peer_id of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id: str) -> None:
        """
        Sets the peer_id of this QueueConversationSocialExpressionEventTopicEmail.
        The id of the peer communication corresponding to a matching leg for this communication.

        :param peer_id: The peer_id of this QueueConversationSocialExpressionEventTopicEmail.
        :type: str
        """
        

        self._peer_id = peer_id

    @property
    def messages_sent(self) -> int:
        """
        Gets the messages_sent of this QueueConversationSocialExpressionEventTopicEmail.
        The number of email messages sent by this participant.

        :return: The messages_sent of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: int
        """
        return self._messages_sent

    @messages_sent.setter
    def messages_sent(self, messages_sent: int) -> None:
        """
        Sets the messages_sent of this QueueConversationSocialExpressionEventTopicEmail.
        The number of email messages sent by this participant.

        :param messages_sent: The messages_sent of this QueueConversationSocialExpressionEventTopicEmail.
        :type: int
        """
        

        self._messages_sent = messages_sent

    @property
    def error_info(self) -> 'QueueConversationSocialExpressionEventTopicErrorDetails':
        """
        Gets the error_info of this QueueConversationSocialExpressionEventTopicEmail.
        Detailed information about an error response.

        :return: The error_info of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: QueueConversationSocialExpressionEventTopicErrorDetails
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info: 'QueueConversationSocialExpressionEventTopicErrorDetails') -> None:
        """
        Sets the error_info of this QueueConversationSocialExpressionEventTopicEmail.
        Detailed information about an error response.

        :param error_info: The error_info of this QueueConversationSocialExpressionEventTopicEmail.
        :type: QueueConversationSocialExpressionEventTopicErrorDetails
        """
        

        self._error_info = error_info

    @property
    def disconnect_type(self) -> str:
        """
        Gets the disconnect_type of this QueueConversationSocialExpressionEventTopicEmail.
        System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects.

        :return: The disconnect_type of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: str
        """
        return self._disconnect_type

    @disconnect_type.setter
    def disconnect_type(self, disconnect_type: str) -> None:
        """
        Sets the disconnect_type of this QueueConversationSocialExpressionEventTopicEmail.
        System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects.

        :param disconnect_type: The disconnect_type of this QueueConversationSocialExpressionEventTopicEmail.
        :type: str
        """
        if isinstance(disconnect_type, int):
            disconnect_type = str(disconnect_type)
        allowed_values = ["endpoint", "client", "system", "timeout", "transfer", "transfer.conference", "transfer.consult", "transfer.forward", "transfer.noanswer", "transfer.notavailable", "transport.failure", "error", "peer", "other", "spam", "uncallable"]
        if disconnect_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for disconnect_type -> " + disconnect_type)
            self._disconnect_type = "outdated_sdk_version"
        else:
            self._disconnect_type = disconnect_type

    @property
    def start_hold_time(self) -> datetime:
        """
        Gets the start_hold_time of this QueueConversationSocialExpressionEventTopicEmail.
        The timestamp the email was placed on hold in the cloud clock if the email is currently on hold.

        :return: The start_hold_time of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: datetime
        """
        return self._start_hold_time

    @start_hold_time.setter
    def start_hold_time(self, start_hold_time: datetime) -> None:
        """
        Sets the start_hold_time of this QueueConversationSocialExpressionEventTopicEmail.
        The timestamp the email was placed on hold in the cloud clock if the email is currently on hold.

        :param start_hold_time: The start_hold_time of this QueueConversationSocialExpressionEventTopicEmail.
        :type: datetime
        """
        

        self._start_hold_time = start_hold_time

    @property
    def connected_time(self) -> datetime:
        """
        Gets the connected_time of this QueueConversationSocialExpressionEventTopicEmail.
        The timestamp when this communication was connected in the cloud clock.

        :return: The connected_time of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: datetime
        """
        return self._connected_time

    @connected_time.setter
    def connected_time(self, connected_time: datetime) -> None:
        """
        Sets the connected_time of this QueueConversationSocialExpressionEventTopicEmail.
        The timestamp when this communication was connected in the cloud clock.

        :param connected_time: The connected_time of this QueueConversationSocialExpressionEventTopicEmail.
        :type: datetime
        """
        

        self._connected_time = connected_time

    @property
    def disconnected_time(self) -> datetime:
        """
        Gets the disconnected_time of this QueueConversationSocialExpressionEventTopicEmail.
        The timestamp when this communication disconnected from the conversation in the provider clock.

        :return: The disconnected_time of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: datetime
        """
        return self._disconnected_time

    @disconnected_time.setter
    def disconnected_time(self, disconnected_time: datetime) -> None:
        """
        Sets the disconnected_time of this QueueConversationSocialExpressionEventTopicEmail.
        The timestamp when this communication disconnected from the conversation in the provider clock.

        :param disconnected_time: The disconnected_time of this QueueConversationSocialExpressionEventTopicEmail.
        :type: datetime
        """
        

        self._disconnected_time = disconnected_time

    @property
    def message_id(self) -> str:
        """
        Gets the message_id of this QueueConversationSocialExpressionEventTopicEmail.
        A globally unique identifier for the stored content of this communication.

        :return: The message_id of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id: str) -> None:
        """
        Sets the message_id of this QueueConversationSocialExpressionEventTopicEmail.
        A globally unique identifier for the stored content of this communication.

        :param message_id: The message_id of this QueueConversationSocialExpressionEventTopicEmail.
        :type: str
        """
        

        self._message_id = message_id

    @property
    def direction(self) -> str:
        """
        Gets the direction of this QueueConversationSocialExpressionEventTopicEmail.
        Whether an email is inbound or outbound.

        :return: The direction of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction: str) -> None:
        """
        Sets the direction of this QueueConversationSocialExpressionEventTopicEmail.
        Whether an email is inbound or outbound.

        :param direction: The direction of this QueueConversationSocialExpressionEventTopicEmail.
        :type: str
        """
        if isinstance(direction, int):
            direction = str(direction)
        allowed_values = ["outbound", "inbound"]
        if direction.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for direction -> " + direction)
            self._direction = "outdated_sdk_version"
        else:
            self._direction = direction

    @property
    def draft_attachments(self) -> List['QueueConversationSocialExpressionEventTopicAttachment']:
        """
        Gets the draft_attachments of this QueueConversationSocialExpressionEventTopicEmail.
        A list of uploaded attachments on the email draft.

        :return: The draft_attachments of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: list[QueueConversationSocialExpressionEventTopicAttachment]
        """
        return self._draft_attachments

    @draft_attachments.setter
    def draft_attachments(self, draft_attachments: List['QueueConversationSocialExpressionEventTopicAttachment']) -> None:
        """
        Sets the draft_attachments of this QueueConversationSocialExpressionEventTopicEmail.
        A list of uploaded attachments on the email draft.

        :param draft_attachments: The draft_attachments of this QueueConversationSocialExpressionEventTopicEmail.
        :type: list[QueueConversationSocialExpressionEventTopicAttachment]
        """
        

        self._draft_attachments = draft_attachments

    @property
    def spam(self) -> bool:
        """
        Gets the spam of this QueueConversationSocialExpressionEventTopicEmail.
        Indicates if the inbound email was marked as spam.

        :return: The spam of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: bool
        """
        return self._spam

    @spam.setter
    def spam(self, spam: bool) -> None:
        """
        Sets the spam of this QueueConversationSocialExpressionEventTopicEmail.
        Indicates if the inbound email was marked as spam.

        :param spam: The spam of this QueueConversationSocialExpressionEventTopicEmail.
        :type: bool
        """
        

        self._spam = spam

    @property
    def wrapup(self) -> 'QueueConversationSocialExpressionEventTopicWrapup':
        """
        Gets the wrapup of this QueueConversationSocialExpressionEventTopicEmail.
        Call wrap up or disposition data.

        :return: The wrapup of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: QueueConversationSocialExpressionEventTopicWrapup
        """
        return self._wrapup

    @wrapup.setter
    def wrapup(self, wrapup: 'QueueConversationSocialExpressionEventTopicWrapup') -> None:
        """
        Sets the wrapup of this QueueConversationSocialExpressionEventTopicEmail.
        Call wrap up or disposition data.

        :param wrapup: The wrapup of this QueueConversationSocialExpressionEventTopicEmail.
        :type: QueueConversationSocialExpressionEventTopicWrapup
        """
        

        self._wrapup = wrapup

    @property
    def after_call_work(self) -> 'QueueConversationSocialExpressionEventTopicAfterCallWork':
        """
        Gets the after_call_work of this QueueConversationSocialExpressionEventTopicEmail.
        A communication's after-call work data.

        :return: The after_call_work of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: QueueConversationSocialExpressionEventTopicAfterCallWork
        """
        return self._after_call_work

    @after_call_work.setter
    def after_call_work(self, after_call_work: 'QueueConversationSocialExpressionEventTopicAfterCallWork') -> None:
        """
        Sets the after_call_work of this QueueConversationSocialExpressionEventTopicEmail.
        A communication's after-call work data.

        :param after_call_work: The after_call_work of this QueueConversationSocialExpressionEventTopicEmail.
        :type: QueueConversationSocialExpressionEventTopicAfterCallWork
        """
        

        self._after_call_work = after_call_work

    @property
    def after_call_work_required(self) -> bool:
        """
        Gets the after_call_work_required of this QueueConversationSocialExpressionEventTopicEmail.
        Indicates if after-call is required for a communication. Only used when the ACW Setting is Agent Requested.

        :return: The after_call_work_required of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: bool
        """
        return self._after_call_work_required

    @after_call_work_required.setter
    def after_call_work_required(self, after_call_work_required: bool) -> None:
        """
        Sets the after_call_work_required of this QueueConversationSocialExpressionEventTopicEmail.
        Indicates if after-call is required for a communication. Only used when the ACW Setting is Agent Requested.

        :param after_call_work_required: The after_call_work_required of this QueueConversationSocialExpressionEventTopicEmail.
        :type: bool
        """
        

        self._after_call_work_required = after_call_work_required

    @property
    def queue_media_settings(self) -> 'QueueConversationSocialExpressionEventTopicQueueMediaSettings':
        """
        Gets the queue_media_settings of this QueueConversationSocialExpressionEventTopicEmail.
        Represents the queue setting for this media.

        :return: The queue_media_settings of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: QueueConversationSocialExpressionEventTopicQueueMediaSettings
        """
        return self._queue_media_settings

    @queue_media_settings.setter
    def queue_media_settings(self, queue_media_settings: 'QueueConversationSocialExpressionEventTopicQueueMediaSettings') -> None:
        """
        Sets the queue_media_settings of this QueueConversationSocialExpressionEventTopicEmail.
        Represents the queue setting for this media.

        :param queue_media_settings: The queue_media_settings of this QueueConversationSocialExpressionEventTopicEmail.
        :type: QueueConversationSocialExpressionEventTopicQueueMediaSettings
        """
        

        self._queue_media_settings = queue_media_settings

    @property
    def resume_time(self) -> datetime:
        """
        Gets the resume_time of this QueueConversationSocialExpressionEventTopicEmail.
        The time when a parked email should resume.

        :return: The resume_time of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: datetime
        """
        return self._resume_time

    @resume_time.setter
    def resume_time(self, resume_time: datetime) -> None:
        """
        Sets the resume_time of this QueueConversationSocialExpressionEventTopicEmail.
        The time when a parked email should resume.

        :param resume_time: The resume_time of this QueueConversationSocialExpressionEventTopicEmail.
        :type: datetime
        """
        

        self._resume_time = resume_time

    @property
    def park_time(self) -> datetime:
        """
        Gets the park_time of this QueueConversationSocialExpressionEventTopicEmail.
        The time when an  parked email was parked.

        :return: The park_time of this QueueConversationSocialExpressionEventTopicEmail.
        :rtype: datetime
        """
        return self._park_time

    @park_time.setter
    def park_time(self, park_time: datetime) -> None:
        """
        Sets the park_time of this QueueConversationSocialExpressionEventTopicEmail.
        The time when an  parked email was parked.

        :param park_time: The park_time of this QueueConversationSocialExpressionEventTopicEmail.
        :type: datetime
        """
        

        self._park_time = park_time

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

