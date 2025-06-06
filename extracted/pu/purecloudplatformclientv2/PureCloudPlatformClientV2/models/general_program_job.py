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

class GeneralProgramJob(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        GeneralProgramJob - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'state': 'str',
            'created_by': 'AddressableEntityRef',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'state': 'state',
            'created_by': 'createdBy',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._state = None
        self._created_by = None
        self._date_created = None
        self._date_modified = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this GeneralProgramJob.
        The globally unique identifier for the object.

        :return: The id of this GeneralProgramJob.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this GeneralProgramJob.
        The globally unique identifier for the object.

        :param id: The id of this GeneralProgramJob.
        :type: str
        """
        

        self._id = id

    @property
    def state(self) -> str:
        """
        Gets the state of this GeneralProgramJob.


        :return: The state of this GeneralProgramJob.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this GeneralProgramJob.


        :param state: The state of this GeneralProgramJob.
        :type: str
        """
        if isinstance(state, int):
            state = str(state)
        allowed_values = ["Running", "Completed", "Failed"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def created_by(self) -> 'AddressableEntityRef':
        """
        Gets the created_by of this GeneralProgramJob.


        :return: The created_by of this GeneralProgramJob.
        :rtype: AddressableEntityRef
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by: 'AddressableEntityRef') -> None:
        """
        Sets the created_by of this GeneralProgramJob.


        :param created_by: The created_by of this GeneralProgramJob.
        :type: AddressableEntityRef
        """
        

        self._created_by = created_by

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this GeneralProgramJob.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this GeneralProgramJob.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this GeneralProgramJob.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this GeneralProgramJob.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this GeneralProgramJob.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this GeneralProgramJob.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this GeneralProgramJob.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this GeneralProgramJob.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this GeneralProgramJob.
        The URI for this object

        :return: The self_uri of this GeneralProgramJob.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this GeneralProgramJob.
        The URI for this object

        :param self_uri: The self_uri of this GeneralProgramJob.
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

