# coding: utf-8

"""
    Managed Ray API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class OrganizationCollaborator(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'permission_level': 'OrganizationPermissionLevel',
        'id': 'str',
        'name': 'str',
        'created_at': 'datetime',
        'email': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'permission_level': 'permission_level',
        'id': 'id',
        'name': 'name',
        'created_at': 'created_at',
        'email': 'email',
        'user_id': 'user_id'
    }

    def __init__(self, permission_level=None, id=None, name=None, created_at=None, email=None, user_id=None, local_vars_configuration=None):  # noqa: E501
        """OrganizationCollaborator - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._permission_level = None
        self._id = None
        self._name = None
        self._created_at = None
        self._email = None
        self._user_id = None
        self.discriminator = None

        self.permission_level = permission_level
        self.id = id
        self.name = name
        self.created_at = created_at
        self.email = email
        if user_id is not None:
            self.user_id = user_id

    @property
    def permission_level(self):
        """Gets the permission_level of this OrganizationCollaborator.  # noqa: E501


        :return: The permission_level of this OrganizationCollaborator.  # noqa: E501
        :rtype: OrganizationPermissionLevel
        """
        return self._permission_level

    @permission_level.setter
    def permission_level(self, permission_level):
        """Sets the permission_level of this OrganizationCollaborator.


        :param permission_level: The permission_level of this OrganizationCollaborator.  # noqa: E501
        :type: OrganizationPermissionLevel
        """
        if self.local_vars_configuration.client_side_validation and permission_level is None:  # noqa: E501
            raise ValueError("Invalid value for `permission_level`, must not be `None`")  # noqa: E501

        self._permission_level = permission_level

    @property
    def id(self):
        """Gets the id of this OrganizationCollaborator.  # noqa: E501

        The identity id of the organization collaborator  # noqa: E501

        :return: The id of this OrganizationCollaborator.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrganizationCollaborator.

        The identity id of the organization collaborator  # noqa: E501

        :param id: The id of this OrganizationCollaborator.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this OrganizationCollaborator.  # noqa: E501


        :return: The name of this OrganizationCollaborator.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationCollaborator.


        :param name: The name of this OrganizationCollaborator.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this OrganizationCollaborator.  # noqa: E501


        :return: The created_at of this OrganizationCollaborator.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this OrganizationCollaborator.


        :param created_at: The created_at of this OrganizationCollaborator.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def email(self):
        """Gets the email of this OrganizationCollaborator.  # noqa: E501


        :return: The email of this OrganizationCollaborator.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this OrganizationCollaborator.


        :param email: The email of this OrganizationCollaborator.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def user_id(self):
        """Gets the user_id of this OrganizationCollaborator.  # noqa: E501

        The user id of the organization collaborator  # noqa: E501

        :return: The user_id of this OrganizationCollaborator.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this OrganizationCollaborator.

        The user id of the organization collaborator  # noqa: E501

        :param user_id: The user_id of this OrganizationCollaborator.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OrganizationCollaborator):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganizationCollaborator):
            return True

        return self.to_dict() != other.to_dict()
