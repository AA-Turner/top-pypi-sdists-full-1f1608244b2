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
    from . import FaxTopicLockData
    from . import FaxTopicUserData
    from . import FaxTopicWorkspaceData

class FaxTopicFaxDataV2(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        FaxTopicFaxDataV2 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'workspace': 'FaxTopicWorkspaceData',
            'created_by': 'FaxTopicUserData',
            'content_type': 'str',
            'content_length': 'int',
            'filename': 'str',
            'change_number': 'int',
            'date_uploaded': 'datetime',
            'uploaded_by': 'FaxTopicUserData',
            'lock_info': 'FaxTopicLockData',
            'self_uri': 'str',
            'caller_address': 'str',
            'receiver_address': 'str',
            'read': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'workspace': 'workspace',
            'created_by': 'createdBy',
            'content_type': 'contentType',
            'content_length': 'contentLength',
            'filename': 'filename',
            'change_number': 'changeNumber',
            'date_uploaded': 'dateUploaded',
            'uploaded_by': 'uploadedBy',
            'lock_info': 'lockInfo',
            'self_uri': 'selfUri',
            'caller_address': 'callerAddress',
            'receiver_address': 'receiverAddress',
            'read': 'read'
        }

        self._id = None
        self._name = None
        self._date_created = None
        self._date_modified = None
        self._workspace = None
        self._created_by = None
        self._content_type = None
        self._content_length = None
        self._filename = None
        self._change_number = None
        self._date_uploaded = None
        self._uploaded_by = None
        self._lock_info = None
        self._self_uri = None
        self._caller_address = None
        self._receiver_address = None
        self._read = None

    @property
    def id(self) -> str:
        """
        Gets the id of this FaxTopicFaxDataV2.


        :return: The id of this FaxTopicFaxDataV2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this FaxTopicFaxDataV2.


        :param id: The id of this FaxTopicFaxDataV2.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this FaxTopicFaxDataV2.


        :return: The name of this FaxTopicFaxDataV2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this FaxTopicFaxDataV2.


        :param name: The name of this FaxTopicFaxDataV2.
        :type: str
        """
        

        self._name = name

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this FaxTopicFaxDataV2.


        :return: The date_created of this FaxTopicFaxDataV2.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this FaxTopicFaxDataV2.


        :param date_created: The date_created of this FaxTopicFaxDataV2.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this FaxTopicFaxDataV2.


        :return: The date_modified of this FaxTopicFaxDataV2.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this FaxTopicFaxDataV2.


        :param date_modified: The date_modified of this FaxTopicFaxDataV2.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def workspace(self) -> 'FaxTopicWorkspaceData':
        """
        Gets the workspace of this FaxTopicFaxDataV2.


        :return: The workspace of this FaxTopicFaxDataV2.
        :rtype: FaxTopicWorkspaceData
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace: 'FaxTopicWorkspaceData') -> None:
        """
        Sets the workspace of this FaxTopicFaxDataV2.


        :param workspace: The workspace of this FaxTopicFaxDataV2.
        :type: FaxTopicWorkspaceData
        """
        

        self._workspace = workspace

    @property
    def created_by(self) -> 'FaxTopicUserData':
        """
        Gets the created_by of this FaxTopicFaxDataV2.


        :return: The created_by of this FaxTopicFaxDataV2.
        :rtype: FaxTopicUserData
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by: 'FaxTopicUserData') -> None:
        """
        Sets the created_by of this FaxTopicFaxDataV2.


        :param created_by: The created_by of this FaxTopicFaxDataV2.
        :type: FaxTopicUserData
        """
        

        self._created_by = created_by

    @property
    def content_type(self) -> str:
        """
        Gets the content_type of this FaxTopicFaxDataV2.


        :return: The content_type of this FaxTopicFaxDataV2.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type: str) -> None:
        """
        Sets the content_type of this FaxTopicFaxDataV2.


        :param content_type: The content_type of this FaxTopicFaxDataV2.
        :type: str
        """
        

        self._content_type = content_type

    @property
    def content_length(self) -> int:
        """
        Gets the content_length of this FaxTopicFaxDataV2.


        :return: The content_length of this FaxTopicFaxDataV2.
        :rtype: int
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length: int) -> None:
        """
        Sets the content_length of this FaxTopicFaxDataV2.


        :param content_length: The content_length of this FaxTopicFaxDataV2.
        :type: int
        """
        

        self._content_length = content_length

    @property
    def filename(self) -> str:
        """
        Gets the filename of this FaxTopicFaxDataV2.


        :return: The filename of this FaxTopicFaxDataV2.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename: str) -> None:
        """
        Sets the filename of this FaxTopicFaxDataV2.


        :param filename: The filename of this FaxTopicFaxDataV2.
        :type: str
        """
        

        self._filename = filename

    @property
    def change_number(self) -> int:
        """
        Gets the change_number of this FaxTopicFaxDataV2.


        :return: The change_number of this FaxTopicFaxDataV2.
        :rtype: int
        """
        return self._change_number

    @change_number.setter
    def change_number(self, change_number: int) -> None:
        """
        Sets the change_number of this FaxTopicFaxDataV2.


        :param change_number: The change_number of this FaxTopicFaxDataV2.
        :type: int
        """
        

        self._change_number = change_number

    @property
    def date_uploaded(self) -> datetime:
        """
        Gets the date_uploaded of this FaxTopicFaxDataV2.


        :return: The date_uploaded of this FaxTopicFaxDataV2.
        :rtype: datetime
        """
        return self._date_uploaded

    @date_uploaded.setter
    def date_uploaded(self, date_uploaded: datetime) -> None:
        """
        Sets the date_uploaded of this FaxTopicFaxDataV2.


        :param date_uploaded: The date_uploaded of this FaxTopicFaxDataV2.
        :type: datetime
        """
        

        self._date_uploaded = date_uploaded

    @property
    def uploaded_by(self) -> 'FaxTopicUserData':
        """
        Gets the uploaded_by of this FaxTopicFaxDataV2.


        :return: The uploaded_by of this FaxTopicFaxDataV2.
        :rtype: FaxTopicUserData
        """
        return self._uploaded_by

    @uploaded_by.setter
    def uploaded_by(self, uploaded_by: 'FaxTopicUserData') -> None:
        """
        Sets the uploaded_by of this FaxTopicFaxDataV2.


        :param uploaded_by: The uploaded_by of this FaxTopicFaxDataV2.
        :type: FaxTopicUserData
        """
        

        self._uploaded_by = uploaded_by

    @property
    def lock_info(self) -> 'FaxTopicLockData':
        """
        Gets the lock_info of this FaxTopicFaxDataV2.


        :return: The lock_info of this FaxTopicFaxDataV2.
        :rtype: FaxTopicLockData
        """
        return self._lock_info

    @lock_info.setter
    def lock_info(self, lock_info: 'FaxTopicLockData') -> None:
        """
        Sets the lock_info of this FaxTopicFaxDataV2.


        :param lock_info: The lock_info of this FaxTopicFaxDataV2.
        :type: FaxTopicLockData
        """
        

        self._lock_info = lock_info

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this FaxTopicFaxDataV2.


        :return: The self_uri of this FaxTopicFaxDataV2.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this FaxTopicFaxDataV2.


        :param self_uri: The self_uri of this FaxTopicFaxDataV2.
        :type: str
        """
        

        self._self_uri = self_uri

    @property
    def caller_address(self) -> str:
        """
        Gets the caller_address of this FaxTopicFaxDataV2.


        :return: The caller_address of this FaxTopicFaxDataV2.
        :rtype: str
        """
        return self._caller_address

    @caller_address.setter
    def caller_address(self, caller_address: str) -> None:
        """
        Sets the caller_address of this FaxTopicFaxDataV2.


        :param caller_address: The caller_address of this FaxTopicFaxDataV2.
        :type: str
        """
        

        self._caller_address = caller_address

    @property
    def receiver_address(self) -> str:
        """
        Gets the receiver_address of this FaxTopicFaxDataV2.


        :return: The receiver_address of this FaxTopicFaxDataV2.
        :rtype: str
        """
        return self._receiver_address

    @receiver_address.setter
    def receiver_address(self, receiver_address: str) -> None:
        """
        Sets the receiver_address of this FaxTopicFaxDataV2.


        :param receiver_address: The receiver_address of this FaxTopicFaxDataV2.
        :type: str
        """
        

        self._receiver_address = receiver_address

    @property
    def read(self) -> bool:
        """
        Gets the read of this FaxTopicFaxDataV2.


        :return: The read of this FaxTopicFaxDataV2.
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read: bool) -> None:
        """
        Sets the read of this FaxTopicFaxDataV2.


        :param read: The read of this FaxTopicFaxDataV2.
        :type: bool
        """
        

        self._read = read

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

