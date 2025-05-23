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

class V1Membership(object):
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
        'balance': 'float',
        'created_at': 'datetime',
        'creator_id': 'str',
        'datastore_count': 'str',
        'description': 'str',
        'display_name': 'str',
        'free_credits_enabled': 'bool',
        'is_default': 'bool',
        'job_count': 'str',
        'membership_count': 'str',
        'name': 'str',
        'owner_id': 'str',
        'owner_type': 'V1OwnerType',
        'project_id': 'str',
        'quotas': 'V1Quotas',
        'roles': 'list[V1Role]',
        'updated_at': 'datetime',
        'user_id': 'str'
    }

    attribute_map = {
        'balance': 'balance',
        'created_at': 'createdAt',
        'creator_id': 'creatorId',
        'datastore_count': 'datastoreCount',
        'description': 'description',
        'display_name': 'displayName',
        'free_credits_enabled': 'freeCreditsEnabled',
        'is_default': 'isDefault',
        'job_count': 'jobCount',
        'membership_count': 'membershipCount',
        'name': 'name',
        'owner_id': 'ownerId',
        'owner_type': 'ownerType',
        'project_id': 'projectId',
        'quotas': 'quotas',
        'roles': 'roles',
        'updated_at': 'updatedAt',
        'user_id': 'userId'
    }

    def __init__(self, balance: 'float' =None, created_at: 'datetime' =None, creator_id: 'str' =None, datastore_count: 'str' =None, description: 'str' =None, display_name: 'str' =None, free_credits_enabled: 'bool' =None, is_default: 'bool' =None, job_count: 'str' =None, membership_count: 'str' =None, name: 'str' =None, owner_id: 'str' =None, owner_type: 'V1OwnerType' =None, project_id: 'str' =None, quotas: 'V1Quotas' =None, roles: 'list[V1Role]' =None, updated_at: 'datetime' =None, user_id: 'str' =None):  # noqa: E501
        """V1Membership - a model defined in Swagger"""  # noqa: E501
        self._balance = None
        self._created_at = None
        self._creator_id = None
        self._datastore_count = None
        self._description = None
        self._display_name = None
        self._free_credits_enabled = None
        self._is_default = None
        self._job_count = None
        self._membership_count = None
        self._name = None
        self._owner_id = None
        self._owner_type = None
        self._project_id = None
        self._quotas = None
        self._roles = None
        self._updated_at = None
        self._user_id = None
        self.discriminator = None
        if balance is not None:
            self.balance = balance
        if created_at is not None:
            self.created_at = created_at
        if creator_id is not None:
            self.creator_id = creator_id
        if datastore_count is not None:
            self.datastore_count = datastore_count
        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if free_credits_enabled is not None:
            self.free_credits_enabled = free_credits_enabled
        if is_default is not None:
            self.is_default = is_default
        if job_count is not None:
            self.job_count = job_count
        if membership_count is not None:
            self.membership_count = membership_count
        if name is not None:
            self.name = name
        if owner_id is not None:
            self.owner_id = owner_id
        if owner_type is not None:
            self.owner_type = owner_type
        if project_id is not None:
            self.project_id = project_id
        if quotas is not None:
            self.quotas = quotas
        if roles is not None:
            self.roles = roles
        if updated_at is not None:
            self.updated_at = updated_at
        if user_id is not None:
            self.user_id = user_id

    @property
    def balance(self) -> 'float':
        """Gets the balance of this V1Membership.  # noqa: E501


        :return: The balance of this V1Membership.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance: 'float'):
        """Sets the balance of this V1Membership.


        :param balance: The balance of this V1Membership.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def created_at(self) -> 'datetime':
        """Gets the created_at of this V1Membership.  # noqa: E501


        :return: The created_at of this V1Membership.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: 'datetime'):
        """Sets the created_at of this V1Membership.


        :param created_at: The created_at of this V1Membership.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def creator_id(self) -> 'str':
        """Gets the creator_id of this V1Membership.  # noqa: E501


        :return: The creator_id of this V1Membership.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id: 'str'):
        """Sets the creator_id of this V1Membership.


        :param creator_id: The creator_id of this V1Membership.  # noqa: E501
        :type: str
        """

        self._creator_id = creator_id

    @property
    def datastore_count(self) -> 'str':
        """Gets the datastore_count of this V1Membership.  # noqa: E501


        :return: The datastore_count of this V1Membership.  # noqa: E501
        :rtype: str
        """
        return self._datastore_count

    @datastore_count.setter
    def datastore_count(self, datastore_count: 'str'):
        """Sets the datastore_count of this V1Membership.


        :param datastore_count: The datastore_count of this V1Membership.  # noqa: E501
        :type: str
        """

        self._datastore_count = datastore_count

    @property
    def description(self) -> 'str':
        """Gets the description of this V1Membership.  # noqa: E501


        :return: The description of this V1Membership.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: 'str'):
        """Sets the description of this V1Membership.


        :param description: The description of this V1Membership.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def display_name(self) -> 'str':
        """Gets the display_name of this V1Membership.  # noqa: E501


        :return: The display_name of this V1Membership.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: 'str'):
        """Sets the display_name of this V1Membership.


        :param display_name: The display_name of this V1Membership.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def free_credits_enabled(self) -> 'bool':
        """Gets the free_credits_enabled of this V1Membership.  # noqa: E501


        :return: The free_credits_enabled of this V1Membership.  # noqa: E501
        :rtype: bool
        """
        return self._free_credits_enabled

    @free_credits_enabled.setter
    def free_credits_enabled(self, free_credits_enabled: 'bool'):
        """Sets the free_credits_enabled of this V1Membership.


        :param free_credits_enabled: The free_credits_enabled of this V1Membership.  # noqa: E501
        :type: bool
        """

        self._free_credits_enabled = free_credits_enabled

    @property
    def is_default(self) -> 'bool':
        """Gets the is_default of this V1Membership.  # noqa: E501


        :return: The is_default of this V1Membership.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default: 'bool'):
        """Sets the is_default of this V1Membership.


        :param is_default: The is_default of this V1Membership.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def job_count(self) -> 'str':
        """Gets the job_count of this V1Membership.  # noqa: E501


        :return: The job_count of this V1Membership.  # noqa: E501
        :rtype: str
        """
        return self._job_count

    @job_count.setter
    def job_count(self, job_count: 'str'):
        """Sets the job_count of this V1Membership.


        :param job_count: The job_count of this V1Membership.  # noqa: E501
        :type: str
        """

        self._job_count = job_count

    @property
    def membership_count(self) -> 'str':
        """Gets the membership_count of this V1Membership.  # noqa: E501


        :return: The membership_count of this V1Membership.  # noqa: E501
        :rtype: str
        """
        return self._membership_count

    @membership_count.setter
    def membership_count(self, membership_count: 'str'):
        """Sets the membership_count of this V1Membership.


        :param membership_count: The membership_count of this V1Membership.  # noqa: E501
        :type: str
        """

        self._membership_count = membership_count

    @property
    def name(self) -> 'str':
        """Gets the name of this V1Membership.  # noqa: E501


        :return: The name of this V1Membership.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: 'str'):
        """Sets the name of this V1Membership.


        :param name: The name of this V1Membership.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def owner_id(self) -> 'str':
        """Gets the owner_id of this V1Membership.  # noqa: E501


        :return: The owner_id of this V1Membership.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: 'str'):
        """Sets the owner_id of this V1Membership.


        :param owner_id: The owner_id of this V1Membership.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def owner_type(self) -> 'V1OwnerType':
        """Gets the owner_type of this V1Membership.  # noqa: E501


        :return: The owner_type of this V1Membership.  # noqa: E501
        :rtype: V1OwnerType
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type: 'V1OwnerType'):
        """Sets the owner_type of this V1Membership.


        :param owner_type: The owner_type of this V1Membership.  # noqa: E501
        :type: V1OwnerType
        """

        self._owner_type = owner_type

    @property
    def project_id(self) -> 'str':
        """Gets the project_id of this V1Membership.  # noqa: E501


        :return: The project_id of this V1Membership.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id: 'str'):
        """Sets the project_id of this V1Membership.


        :param project_id: The project_id of this V1Membership.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def quotas(self) -> 'V1Quotas':
        """Gets the quotas of this V1Membership.  # noqa: E501


        :return: The quotas of this V1Membership.  # noqa: E501
        :rtype: V1Quotas
        """
        return self._quotas

    @quotas.setter
    def quotas(self, quotas: 'V1Quotas'):
        """Sets the quotas of this V1Membership.


        :param quotas: The quotas of this V1Membership.  # noqa: E501
        :type: V1Quotas
        """

        self._quotas = quotas

    @property
    def roles(self) -> 'list[V1Role]':
        """Gets the roles of this V1Membership.  # noqa: E501


        :return: The roles of this V1Membership.  # noqa: E501
        :rtype: list[V1Role]
        """
        return self._roles

    @roles.setter
    def roles(self, roles: 'list[V1Role]'):
        """Sets the roles of this V1Membership.


        :param roles: The roles of this V1Membership.  # noqa: E501
        :type: list[V1Role]
        """

        self._roles = roles

    @property
    def updated_at(self) -> 'datetime':
        """Gets the updated_at of this V1Membership.  # noqa: E501


        :return: The updated_at of this V1Membership.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at: 'datetime'):
        """Sets the updated_at of this V1Membership.


        :param updated_at: The updated_at of this V1Membership.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def user_id(self) -> 'str':
        """Gets the user_id of this V1Membership.  # noqa: E501


        :return: The user_id of this V1Membership.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: 'str'):
        """Sets the user_id of this V1Membership.


        :param user_id: The user_id of this V1Membership.  # noqa: E501
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
        if issubclass(V1Membership, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: 'V1Membership') -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, V1Membership):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V1Membership') -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
