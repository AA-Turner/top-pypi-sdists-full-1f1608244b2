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

class V1OrgMembershipRoleBinding(object):
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
        'org_id': 'str',
        'role_id': 'str',
        'updated_at': 'datetime',
        'user_id': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'org_id': 'orgId',
        'role_id': 'roleId',
        'updated_at': 'updatedAt',
        'user_id': 'userId'
    }

    def __init__(self, created_at: 'datetime' =None, org_id: 'str' =None, role_id: 'str' =None, updated_at: 'datetime' =None, user_id: 'str' =None):  # noqa: E501
        """V1OrgMembershipRoleBinding - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._org_id = None
        self._role_id = None
        self._updated_at = None
        self._user_id = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if org_id is not None:
            self.org_id = org_id
        if role_id is not None:
            self.role_id = role_id
        if updated_at is not None:
            self.updated_at = updated_at
        if user_id is not None:
            self.user_id = user_id

    @property
    def created_at(self) -> 'datetime':
        """Gets the created_at of this V1OrgMembershipRoleBinding.  # noqa: E501


        :return: The created_at of this V1OrgMembershipRoleBinding.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: 'datetime'):
        """Sets the created_at of this V1OrgMembershipRoleBinding.


        :param created_at: The created_at of this V1OrgMembershipRoleBinding.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def org_id(self) -> 'str':
        """Gets the org_id of this V1OrgMembershipRoleBinding.  # noqa: E501


        :return: The org_id of this V1OrgMembershipRoleBinding.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id: 'str'):
        """Sets the org_id of this V1OrgMembershipRoleBinding.


        :param org_id: The org_id of this V1OrgMembershipRoleBinding.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

    @property
    def role_id(self) -> 'str':
        """Gets the role_id of this V1OrgMembershipRoleBinding.  # noqa: E501


        :return: The role_id of this V1OrgMembershipRoleBinding.  # noqa: E501
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id: 'str'):
        """Sets the role_id of this V1OrgMembershipRoleBinding.


        :param role_id: The role_id of this V1OrgMembershipRoleBinding.  # noqa: E501
        :type: str
        """

        self._role_id = role_id

    @property
    def updated_at(self) -> 'datetime':
        """Gets the updated_at of this V1OrgMembershipRoleBinding.  # noqa: E501


        :return: The updated_at of this V1OrgMembershipRoleBinding.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at: 'datetime'):
        """Sets the updated_at of this V1OrgMembershipRoleBinding.


        :param updated_at: The updated_at of this V1OrgMembershipRoleBinding.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def user_id(self) -> 'str':
        """Gets the user_id of this V1OrgMembershipRoleBinding.  # noqa: E501


        :return: The user_id of this V1OrgMembershipRoleBinding.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: 'str'):
        """Sets the user_id of this V1OrgMembershipRoleBinding.


        :param user_id: The user_id of this V1OrgMembershipRoleBinding.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

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
        if issubclass(V1OrgMembershipRoleBinding, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: 'V1OrgMembershipRoleBinding') -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, V1OrgMembershipRoleBinding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V1OrgMembershipRoleBinding') -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
