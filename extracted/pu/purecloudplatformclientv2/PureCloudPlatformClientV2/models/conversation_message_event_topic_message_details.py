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
    from . import ConversationMessageEventTopicErrorDetails
    from . import ConversationMessageEventTopicMessageMedia
    from . import ConversationMessageEventTopicMessageMetadata
    from . import ConversationMessageEventTopicMessageSticker
    from . import ConversationMessageEventTopicUriReference

class ConversationMessageEventTopicMessageDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ConversationMessageEventTopicMessageDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'message': 'ConversationMessageEventTopicUriReference',
            'message_time': 'datetime',
            'message_segment_count': 'int',
            'message_status': 'str',
            'media': 'list[ConversationMessageEventTopicMessageMedia]',
            'stickers': 'list[ConversationMessageEventTopicMessageSticker]',
            'error_info': 'ConversationMessageEventTopicErrorDetails',
            'message_metadata': 'ConversationMessageEventTopicMessageMetadata',
            'social_visibility': 'str'
        }

        self.attribute_map = {
            'message': 'message',
            'message_time': 'messageTime',
            'message_segment_count': 'messageSegmentCount',
            'message_status': 'messageStatus',
            'media': 'media',
            'stickers': 'stickers',
            'error_info': 'errorInfo',
            'message_metadata': 'messageMetadata',
            'social_visibility': 'socialVisibility'
        }

        self._message = None
        self._message_time = None
        self._message_segment_count = None
        self._message_status = None
        self._media = None
        self._stickers = None
        self._error_info = None
        self._message_metadata = None
        self._social_visibility = None

    @property
    def message(self) -> 'ConversationMessageEventTopicUriReference':
        """
        Gets the message of this ConversationMessageEventTopicMessageDetails.


        :return: The message of this ConversationMessageEventTopicMessageDetails.
        :rtype: ConversationMessageEventTopicUriReference
        """
        return self._message

    @message.setter
    def message(self, message: 'ConversationMessageEventTopicUriReference') -> None:
        """
        Sets the message of this ConversationMessageEventTopicMessageDetails.


        :param message: The message of this ConversationMessageEventTopicMessageDetails.
        :type: ConversationMessageEventTopicUriReference
        """
        

        self._message = message

    @property
    def message_time(self) -> datetime:
        """
        Gets the message_time of this ConversationMessageEventTopicMessageDetails.


        :return: The message_time of this ConversationMessageEventTopicMessageDetails.
        :rtype: datetime
        """
        return self._message_time

    @message_time.setter
    def message_time(self, message_time: datetime) -> None:
        """
        Sets the message_time of this ConversationMessageEventTopicMessageDetails.


        :param message_time: The message_time of this ConversationMessageEventTopicMessageDetails.
        :type: datetime
        """
        

        self._message_time = message_time

    @property
    def message_segment_count(self) -> int:
        """
        Gets the message_segment_count of this ConversationMessageEventTopicMessageDetails.


        :return: The message_segment_count of this ConversationMessageEventTopicMessageDetails.
        :rtype: int
        """
        return self._message_segment_count

    @message_segment_count.setter
    def message_segment_count(self, message_segment_count: int) -> None:
        """
        Sets the message_segment_count of this ConversationMessageEventTopicMessageDetails.


        :param message_segment_count: The message_segment_count of this ConversationMessageEventTopicMessageDetails.
        :type: int
        """
        

        self._message_segment_count = message_segment_count

    @property
    def message_status(self) -> str:
        """
        Gets the message_status of this ConversationMessageEventTopicMessageDetails.


        :return: The message_status of this ConversationMessageEventTopicMessageDetails.
        :rtype: str
        """
        return self._message_status

    @message_status.setter
    def message_status(self, message_status: str) -> None:
        """
        Sets the message_status of this ConversationMessageEventTopicMessageDetails.


        :param message_status: The message_status of this ConversationMessageEventTopicMessageDetails.
        :type: str
        """
        if isinstance(message_status, int):
            message_status = str(message_status)
        allowed_values = ["queued", "sent", "failed", "received", "delivery-success", "delivery-failed", "read", "removed", "published"]
        if message_status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for message_status -> " + message_status)
            self._message_status = "outdated_sdk_version"
        else:
            self._message_status = message_status

    @property
    def media(self) -> List['ConversationMessageEventTopicMessageMedia']:
        """
        Gets the media of this ConversationMessageEventTopicMessageDetails.


        :return: The media of this ConversationMessageEventTopicMessageDetails.
        :rtype: list[ConversationMessageEventTopicMessageMedia]
        """
        return self._media

    @media.setter
    def media(self, media: List['ConversationMessageEventTopicMessageMedia']) -> None:
        """
        Sets the media of this ConversationMessageEventTopicMessageDetails.


        :param media: The media of this ConversationMessageEventTopicMessageDetails.
        :type: list[ConversationMessageEventTopicMessageMedia]
        """
        

        self._media = media

    @property
    def stickers(self) -> List['ConversationMessageEventTopicMessageSticker']:
        """
        Gets the stickers of this ConversationMessageEventTopicMessageDetails.


        :return: The stickers of this ConversationMessageEventTopicMessageDetails.
        :rtype: list[ConversationMessageEventTopicMessageSticker]
        """
        return self._stickers

    @stickers.setter
    def stickers(self, stickers: List['ConversationMessageEventTopicMessageSticker']) -> None:
        """
        Sets the stickers of this ConversationMessageEventTopicMessageDetails.


        :param stickers: The stickers of this ConversationMessageEventTopicMessageDetails.
        :type: list[ConversationMessageEventTopicMessageSticker]
        """
        

        self._stickers = stickers

    @property
    def error_info(self) -> 'ConversationMessageEventTopicErrorDetails':
        """
        Gets the error_info of this ConversationMessageEventTopicMessageDetails.


        :return: The error_info of this ConversationMessageEventTopicMessageDetails.
        :rtype: ConversationMessageEventTopicErrorDetails
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info: 'ConversationMessageEventTopicErrorDetails') -> None:
        """
        Sets the error_info of this ConversationMessageEventTopicMessageDetails.


        :param error_info: The error_info of this ConversationMessageEventTopicMessageDetails.
        :type: ConversationMessageEventTopicErrorDetails
        """
        

        self._error_info = error_info

    @property
    def message_metadata(self) -> 'ConversationMessageEventTopicMessageMetadata':
        """
        Gets the message_metadata of this ConversationMessageEventTopicMessageDetails.


        :return: The message_metadata of this ConversationMessageEventTopicMessageDetails.
        :rtype: ConversationMessageEventTopicMessageMetadata
        """
        return self._message_metadata

    @message_metadata.setter
    def message_metadata(self, message_metadata: 'ConversationMessageEventTopicMessageMetadata') -> None:
        """
        Sets the message_metadata of this ConversationMessageEventTopicMessageDetails.


        :param message_metadata: The message_metadata of this ConversationMessageEventTopicMessageDetails.
        :type: ConversationMessageEventTopicMessageMetadata
        """
        

        self._message_metadata = message_metadata

    @property
    def social_visibility(self) -> str:
        """
        Gets the social_visibility of this ConversationMessageEventTopicMessageDetails.


        :return: The social_visibility of this ConversationMessageEventTopicMessageDetails.
        :rtype: str
        """
        return self._social_visibility

    @social_visibility.setter
    def social_visibility(self, social_visibility: str) -> None:
        """
        Sets the social_visibility of this ConversationMessageEventTopicMessageDetails.


        :param social_visibility: The social_visibility of this ConversationMessageEventTopicMessageDetails.
        :type: str
        """
        if isinstance(social_visibility, int):
            social_visibility = str(social_visibility)
        allowed_values = ["private", "public"]
        if social_visibility.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for social_visibility -> " + social_visibility)
            self._social_visibility = "outdated_sdk_version"
        else:
            self._social_visibility = social_visibility

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

