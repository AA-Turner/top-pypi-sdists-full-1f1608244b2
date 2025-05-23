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
    from . import ConversationNotificationTemplateBody
    from . import ConversationNotificationTemplateButton
    from . import ConversationNotificationTemplateFooter
    from . import ConversationNotificationTemplateHeader

class ConversationContentNotificationTemplate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ConversationContentNotificationTemplate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'language': 'str',
            'header': 'ConversationNotificationTemplateHeader',
            'body': 'ConversationNotificationTemplateBody',
            'buttons': 'list[ConversationNotificationTemplateButton]',
            'footer': 'ConversationNotificationTemplateFooter'
        }

        self.attribute_map = {
            'id': 'id',
            'language': 'language',
            'header': 'header',
            'body': 'body',
            'buttons': 'buttons',
            'footer': 'footer'
        }

        self._id = None
        self._language = None
        self._header = None
        self._body = None
        self._buttons = None
        self._footer = None

    @property
    def id(self) -> str:
        """
        Gets the id of this ConversationContentNotificationTemplate.
        The identifier of the message template in 'your-namespace@your-template-id/name' format. For External vendor (e.g WhatsApp), 'your-namespace@your-template-name'. For GenesysCloud canned response message template use 'cannedresponse' as your-namespace and use response ID as your-template-id (e.g. response ID=1234 then 'cannedresponse@1234')

        :return: The id of this ConversationContentNotificationTemplate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this ConversationContentNotificationTemplate.
        The identifier of the message template in 'your-namespace@your-template-id/name' format. For External vendor (e.g WhatsApp), 'your-namespace@your-template-name'. For GenesysCloud canned response message template use 'cannedresponse' as your-namespace and use response ID as your-template-id (e.g. response ID=1234 then 'cannedresponse@1234')

        :param id: The id of this ConversationContentNotificationTemplate.
        :type: str
        """
        

        self._id = id

    @property
    def language(self) -> str:
        """
        Gets the language of this ConversationContentNotificationTemplate.
        Template language.

        :return: The language of this ConversationContentNotificationTemplate.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language: str) -> None:
        """
        Sets the language of this ConversationContentNotificationTemplate.
        Template language.

        :param language: The language of this ConversationContentNotificationTemplate.
        :type: str
        """
        

        self._language = language

    @property
    def header(self) -> 'ConversationNotificationTemplateHeader':
        """
        Gets the header of this ConversationContentNotificationTemplate.
        The template header.

        :return: The header of this ConversationContentNotificationTemplate.
        :rtype: ConversationNotificationTemplateHeader
        """
        return self._header

    @header.setter
    def header(self, header: 'ConversationNotificationTemplateHeader') -> None:
        """
        Sets the header of this ConversationContentNotificationTemplate.
        The template header.

        :param header: The header of this ConversationContentNotificationTemplate.
        :type: ConversationNotificationTemplateHeader
        """
        

        self._header = header

    @property
    def body(self) -> 'ConversationNotificationTemplateBody':
        """
        Gets the body of this ConversationContentNotificationTemplate.
        The template body.

        :return: The body of this ConversationContentNotificationTemplate.
        :rtype: ConversationNotificationTemplateBody
        """
        return self._body

    @body.setter
    def body(self, body: 'ConversationNotificationTemplateBody') -> None:
        """
        Sets the body of this ConversationContentNotificationTemplate.
        The template body.

        :param body: The body of this ConversationContentNotificationTemplate.
        :type: ConversationNotificationTemplateBody
        """
        

        self._body = body

    @property
    def buttons(self) -> List['ConversationNotificationTemplateButton']:
        """
        Gets the buttons of this ConversationContentNotificationTemplate.
        Template buttons

        :return: The buttons of this ConversationContentNotificationTemplate.
        :rtype: list[ConversationNotificationTemplateButton]
        """
        return self._buttons

    @buttons.setter
    def buttons(self, buttons: List['ConversationNotificationTemplateButton']) -> None:
        """
        Sets the buttons of this ConversationContentNotificationTemplate.
        Template buttons

        :param buttons: The buttons of this ConversationContentNotificationTemplate.
        :type: list[ConversationNotificationTemplateButton]
        """
        

        self._buttons = buttons

    @property
    def footer(self) -> 'ConversationNotificationTemplateFooter':
        """
        Gets the footer of this ConversationContentNotificationTemplate.
        The template footer.

        :return: The footer of this ConversationContentNotificationTemplate.
        :rtype: ConversationNotificationTemplateFooter
        """
        return self._footer

    @footer.setter
    def footer(self, footer: 'ConversationNotificationTemplateFooter') -> None:
        """
        Sets the footer of this ConversationContentNotificationTemplate.
        The template footer.

        :param footer: The footer of this ConversationContentNotificationTemplate.
        :type: ConversationNotificationTemplateFooter
        """
        

        self._footer = footer

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

