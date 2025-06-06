# coding: utf-8

"""
    external/v1/auth_service.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    NOTE
    ----
    standard swagger-codegen-cli for this python client has been modified
    by custom templates. The purpose of these templates is to include
    typing information in the API and Model code. Please refer to the
    main grid repository for more info
"""

import pprint
import re  # noqa: F401

from typing import TYPE_CHECKING

import six

if TYPE_CHECKING:
    from datetime import datetime
    from lightning_cloud.openapi.models import *

class Externalv1Lightningwork(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'created_at': 'datetime',
        'display_name': 'str',
        'id': 'str',
        'name': 'str',
        'project_id': 'str',
        'spec': 'V1LightningworkSpec',
        'status': 'V1LightningworkStatus',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'display_name': 'displayName',
        'id': 'id',
        'name': 'name',
        'project_id': 'projectId',
        'spec': 'spec',
        'status': 'status',
        'updated_at': 'updatedAt'
    }

    def __init__(self, created_at: 'datetime' =None, display_name: 'str' =None, id: 'str' =None, name: 'str' =None, project_id: 'str' =None, spec: 'V1LightningworkSpec' =None, status: 'V1LightningworkStatus' =None, updated_at: 'datetime' =None):  # noqa: E501
        """Externalv1Lightningwork - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._display_name = None
        self._id = None
        self._name = None
        self._project_id = None
        self._spec = None
        self._status = None
        self._updated_at = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if spec is not None:
            self.spec = spec
        if status is not None:
            self.status = status
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def created_at(self) -> 'datetime':
        """Gets the created_at of this Externalv1Lightningwork.  # noqa: E501


        :return: The created_at of this Externalv1Lightningwork.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: 'datetime'):
        """Sets the created_at of this Externalv1Lightningwork.


        :param created_at: The created_at of this Externalv1Lightningwork.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def display_name(self) -> 'str':
        """Gets the display_name of this Externalv1Lightningwork.  # noqa: E501


        :return: The display_name of this Externalv1Lightningwork.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: 'str'):
        """Sets the display_name of this Externalv1Lightningwork.


        :param display_name: The display_name of this Externalv1Lightningwork.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self) -> 'str':
        """Gets the id of this Externalv1Lightningwork.  # noqa: E501


        :return: The id of this Externalv1Lightningwork.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: 'str'):
        """Sets the id of this Externalv1Lightningwork.


        :param id: The id of this Externalv1Lightningwork.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self) -> 'str':
        """Gets the name of this Externalv1Lightningwork.  # noqa: E501


        :return: The name of this Externalv1Lightningwork.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: 'str'):
        """Sets the name of this Externalv1Lightningwork.


        :param name: The name of this Externalv1Lightningwork.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def project_id(self) -> 'str':
        """Gets the project_id of this Externalv1Lightningwork.  # noqa: E501


        :return: The project_id of this Externalv1Lightningwork.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id: 'str'):
        """Sets the project_id of this Externalv1Lightningwork.


        :param project_id: The project_id of this Externalv1Lightningwork.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def spec(self) -> 'V1LightningworkSpec':
        """Gets the spec of this Externalv1Lightningwork.  # noqa: E501


        :return: The spec of this Externalv1Lightningwork.  # noqa: E501
        :rtype: V1LightningworkSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec: 'V1LightningworkSpec'):
        """Sets the spec of this Externalv1Lightningwork.


        :param spec: The spec of this Externalv1Lightningwork.  # noqa: E501
        :type: V1LightningworkSpec
        """

        self._spec = spec

    @property
    def status(self) -> 'V1LightningworkStatus':
        """Gets the status of this Externalv1Lightningwork.  # noqa: E501


        :return: The status of this Externalv1Lightningwork.  # noqa: E501
        :rtype: V1LightningworkStatus
        """
        return self._status

    @status.setter
    def status(self, status: 'V1LightningworkStatus'):
        """Sets the status of this Externalv1Lightningwork.


        :param status: The status of this Externalv1Lightningwork.  # noqa: E501
        :type: V1LightningworkStatus
        """

        self._status = status

    @property
    def updated_at(self) -> 'datetime':
        """Gets the updated_at of this Externalv1Lightningwork.  # noqa: E501


        :return: The updated_at of this Externalv1Lightningwork.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at: 'datetime'):
        """Sets the updated_at of this Externalv1Lightningwork.


        :param updated_at: The updated_at of this Externalv1Lightningwork.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    def to_dict(self) -> dict:
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Externalv1Lightningwork, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: 'Externalv1Lightningwork') -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, Externalv1Lightningwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Externalv1Lightningwork') -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
