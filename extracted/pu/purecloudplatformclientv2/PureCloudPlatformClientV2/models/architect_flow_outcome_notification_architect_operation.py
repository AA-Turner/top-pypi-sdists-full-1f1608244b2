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
    from . import ArchitectFlowOutcomeNotificationClient
    from . import ArchitectFlowOutcomeNotificationErrorDetail
    from . import ArchitectFlowOutcomeNotificationErrorMessageParams
    from . import ArchitectFlowOutcomeNotificationUser

class ArchitectFlowOutcomeNotificationArchitectOperation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ArchitectFlowOutcomeNotificationArchitectOperation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'complete': 'bool',
            'user': 'ArchitectFlowOutcomeNotificationUser',
            'client': 'ArchitectFlowOutcomeNotificationClient',
            'action_name': 'str',
            'action_status': 'str',
            'error_message': 'str',
            'error_code': 'str',
            'error_message_params': 'ArchitectFlowOutcomeNotificationErrorMessageParams',
            'error_details': 'list[ArchitectFlowOutcomeNotificationErrorDetail]'
        }

        self.attribute_map = {
            'id': 'id',
            'complete': 'complete',
            'user': 'user',
            'client': 'client',
            'action_name': 'actionName',
            'action_status': 'actionStatus',
            'error_message': 'errorMessage',
            'error_code': 'errorCode',
            'error_message_params': 'errorMessageParams',
            'error_details': 'errorDetails'
        }

        self._id = None
        self._complete = None
        self._user = None
        self._client = None
        self._action_name = None
        self._action_status = None
        self._error_message = None
        self._error_code = None
        self._error_message_params = None
        self._error_details = None

    @property
    def id(self) -> str:
        """
        Gets the id of this ArchitectFlowOutcomeNotificationArchitectOperation.
        A unique identifier for this operation, as generated by the initiating client

        :return: The id of this ArchitectFlowOutcomeNotificationArchitectOperation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this ArchitectFlowOutcomeNotificationArchitectOperation.
        A unique identifier for this operation, as generated by the initiating client

        :param id: The id of this ArchitectFlowOutcomeNotificationArchitectOperation.
        :type: str
        """
        

        self._id = id

    @property
    def complete(self) -> bool:
        """
        Gets the complete of this ArchitectFlowOutcomeNotificationArchitectOperation.
        Indicates if the operation is complete

        :return: The complete of this ArchitectFlowOutcomeNotificationArchitectOperation.
        :rtype: bool
        """
        return self._complete

    @complete.setter
    def complete(self, complete: bool) -> None:
        """
        Sets the complete of this ArchitectFlowOutcomeNotificationArchitectOperation.
        Indicates if the operation is complete

        :param complete: The complete of this ArchitectFlowOutcomeNotificationArchitectOperation.
        :type: bool
        """
        

        self._complete = complete

    @property
    def user(self) -> 'ArchitectFlowOutcomeNotificationUser':
        """
        Gets the user of this ArchitectFlowOutcomeNotificationArchitectOperation.


        :return: The user of this ArchitectFlowOutcomeNotificationArchitectOperation.
        :rtype: ArchitectFlowOutcomeNotificationUser
        """
        return self._user

    @user.setter
    def user(self, user: 'ArchitectFlowOutcomeNotificationUser') -> None:
        """
        Sets the user of this ArchitectFlowOutcomeNotificationArchitectOperation.


        :param user: The user of this ArchitectFlowOutcomeNotificationArchitectOperation.
        :type: ArchitectFlowOutcomeNotificationUser
        """
        

        self._user = user

    @property
    def client(self) -> 'ArchitectFlowOutcomeNotificationClient':
        """
        Gets the client of this ArchitectFlowOutcomeNotificationArchitectOperation.


        :return: The client of this ArchitectFlowOutcomeNotificationArchitectOperation.
        :rtype: ArchitectFlowOutcomeNotificationClient
        """
        return self._client

    @client.setter
    def client(self, client: 'ArchitectFlowOutcomeNotificationClient') -> None:
        """
        Sets the client of this ArchitectFlowOutcomeNotificationArchitectOperation.


        :param client: The client of this ArchitectFlowOutcomeNotificationArchitectOperation.
        :type: ArchitectFlowOutcomeNotificationClient
        """
        

        self._client = client

    @property
    def action_name(self) -> str:
        """
        Gets the action_name of this ArchitectFlowOutcomeNotificationArchitectOperation.
        The action being performed

        :return: The action_name of this ArchitectFlowOutcomeNotificationArchitectOperation.
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name: str) -> None:
        """
        Sets the action_name of this ArchitectFlowOutcomeNotificationArchitectOperation.
        The action being performed

        :param action_name: The action_name of this ArchitectFlowOutcomeNotificationArchitectOperation.
        :type: str
        """
        if isinstance(action_name, int):
            action_name = str(action_name)
        allowed_values = ["CREATE", "CHECKIN", "CHECKOUT", "DEACTIVATE", "DEBUG", "DELETE", "HISTORY", "PUBLISH", "REVERT", "SAVE", "STATE_CHANGE", "UPDATE", "VALIDATE"]
        if action_name.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for action_name -> " + action_name)
            self._action_name = "outdated_sdk_version"
        else:
            self._action_name = action_name

    @property
    def action_status(self) -> str:
        """
        Gets the action_status of this ArchitectFlowOutcomeNotificationArchitectOperation.
        The action status

        :return: The action_status of this ArchitectFlowOutcomeNotificationArchitectOperation.
        :rtype: str
        """
        return self._action_status

    @action_status.setter
    def action_status(self, action_status: str) -> None:
        """
        Sets the action_status of this ArchitectFlowOutcomeNotificationArchitectOperation.
        The action status

        :param action_status: The action_status of this ArchitectFlowOutcomeNotificationArchitectOperation.
        :type: str
        """
        if isinstance(action_status, int):
            action_status = str(action_status)
        allowed_values = ["LOCKED", "UNLOCKED", "STARTED", "PENDING_GENERATION", "PENDING_BACKEND_NOTIFICATION", "SUCCESS", "FAILURE"]
        if action_status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for action_status -> " + action_status)
            self._action_status = "outdated_sdk_version"
        else:
            self._action_status = action_status

    @property
    def error_message(self) -> str:
        """
        Gets the error_message of this ArchitectFlowOutcomeNotificationArchitectOperation.
        The error message, if the action failed

        :return: The error_message of this ArchitectFlowOutcomeNotificationArchitectOperation.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message: str) -> None:
        """
        Sets the error_message of this ArchitectFlowOutcomeNotificationArchitectOperation.
        The error message, if the action failed

        :param error_message: The error_message of this ArchitectFlowOutcomeNotificationArchitectOperation.
        :type: str
        """
        

        self._error_message = error_message

    @property
    def error_code(self) -> str:
        """
        Gets the error_code of this ArchitectFlowOutcomeNotificationArchitectOperation.
        The error code, if the action failed

        :return: The error_code of this ArchitectFlowOutcomeNotificationArchitectOperation.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code: str) -> None:
        """
        Sets the error_code of this ArchitectFlowOutcomeNotificationArchitectOperation.
        The error code, if the action failed

        :param error_code: The error_code of this ArchitectFlowOutcomeNotificationArchitectOperation.
        :type: str
        """
        

        self._error_code = error_code

    @property
    def error_message_params(self) -> 'ArchitectFlowOutcomeNotificationErrorMessageParams':
        """
        Gets the error_message_params of this ArchitectFlowOutcomeNotificationArchitectOperation.


        :return: The error_message_params of this ArchitectFlowOutcomeNotificationArchitectOperation.
        :rtype: ArchitectFlowOutcomeNotificationErrorMessageParams
        """
        return self._error_message_params

    @error_message_params.setter
    def error_message_params(self, error_message_params: 'ArchitectFlowOutcomeNotificationErrorMessageParams') -> None:
        """
        Sets the error_message_params of this ArchitectFlowOutcomeNotificationArchitectOperation.


        :param error_message_params: The error_message_params of this ArchitectFlowOutcomeNotificationArchitectOperation.
        :type: ArchitectFlowOutcomeNotificationErrorMessageParams
        """
        

        self._error_message_params = error_message_params

    @property
    def error_details(self) -> List['ArchitectFlowOutcomeNotificationErrorDetail']:
        """
        Gets the error_details of this ArchitectFlowOutcomeNotificationArchitectOperation.
        The error details, if the action failed

        :return: The error_details of this ArchitectFlowOutcomeNotificationArchitectOperation.
        :rtype: list[ArchitectFlowOutcomeNotificationErrorDetail]
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details: List['ArchitectFlowOutcomeNotificationErrorDetail']) -> None:
        """
        Sets the error_details of this ArchitectFlowOutcomeNotificationArchitectOperation.
        The error details, if the action failed

        :param error_details: The error_details of this ArchitectFlowOutcomeNotificationArchitectOperation.
        :type: list[ArchitectFlowOutcomeNotificationErrorDetail]
        """
        

        self._error_details = error_details

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

