# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from akeyless.configuration import Configuration


class RotatedSecretDetailsInfo(object):
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
        'delete_previous_version_in_days': 'int',
        'enable_custom_password_policy': 'bool',
        'grace_rotation': 'bool',
        'grace_rotation_hour': 'int',
        'grace_rotation_interval': 'int',
        'gw_cluster_id': 'int',
        'last_rotation_error': 'str',
        'managed_by_akeyless': 'bool',
        'max_versions': 'int',
        'next_auto_rotate_type': 'str',
        'number_of_versions_to_save': 'int',
        'rotation_hour': 'int',
        'rotation_interval_min': 'bool',
        'rotation_statement': 'str',
        'rotator_creds_type': 'str',
        'rotator_status': 'str',
        'rotator_type': 'str',
        'same_password': 'bool',
        'services_details': 'list[WindowsService]',
        'timeout_seconds': 'int'
    }

    attribute_map = {
        'delete_previous_version_in_days': 'delete_previous_version_in_days',
        'enable_custom_password_policy': 'enable_custom_password_policy',
        'grace_rotation': 'grace_rotation',
        'grace_rotation_hour': 'grace_rotation_hour',
        'grace_rotation_interval': 'grace_rotation_interval',
        'gw_cluster_id': 'gw_cluster_id',
        'last_rotation_error': 'last_rotation_error',
        'managed_by_akeyless': 'managed_by_akeyless',
        'max_versions': 'max_versions',
        'next_auto_rotate_type': 'next_auto_rotate_type',
        'number_of_versions_to_save': 'number_of_versions_to_save',
        'rotation_hour': 'rotation_hour',
        'rotation_interval_min': 'rotation_interval_min',
        'rotation_statement': 'rotation_statement',
        'rotator_creds_type': 'rotator_creds_type',
        'rotator_status': 'rotator_status',
        'rotator_type': 'rotator_type',
        'same_password': 'same_password',
        'services_details': 'services_details',
        'timeout_seconds': 'timeout_seconds'
    }

    def __init__(self, delete_previous_version_in_days=None, enable_custom_password_policy=None, grace_rotation=None, grace_rotation_hour=None, grace_rotation_interval=None, gw_cluster_id=None, last_rotation_error=None, managed_by_akeyless=None, max_versions=None, next_auto_rotate_type=None, number_of_versions_to_save=None, rotation_hour=None, rotation_interval_min=None, rotation_statement=None, rotator_creds_type=None, rotator_status=None, rotator_type=None, same_password=None, services_details=None, timeout_seconds=None, local_vars_configuration=None):  # noqa: E501
        """RotatedSecretDetailsInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._delete_previous_version_in_days = None
        self._enable_custom_password_policy = None
        self._grace_rotation = None
        self._grace_rotation_hour = None
        self._grace_rotation_interval = None
        self._gw_cluster_id = None
        self._last_rotation_error = None
        self._managed_by_akeyless = None
        self._max_versions = None
        self._next_auto_rotate_type = None
        self._number_of_versions_to_save = None
        self._rotation_hour = None
        self._rotation_interval_min = None
        self._rotation_statement = None
        self._rotator_creds_type = None
        self._rotator_status = None
        self._rotator_type = None
        self._same_password = None
        self._services_details = None
        self._timeout_seconds = None
        self.discriminator = None

        if delete_previous_version_in_days is not None:
            self.delete_previous_version_in_days = delete_previous_version_in_days
        if enable_custom_password_policy is not None:
            self.enable_custom_password_policy = enable_custom_password_policy
        if grace_rotation is not None:
            self.grace_rotation = grace_rotation
        if grace_rotation_hour is not None:
            self.grace_rotation_hour = grace_rotation_hour
        if grace_rotation_interval is not None:
            self.grace_rotation_interval = grace_rotation_interval
        if gw_cluster_id is not None:
            self.gw_cluster_id = gw_cluster_id
        if last_rotation_error is not None:
            self.last_rotation_error = last_rotation_error
        if managed_by_akeyless is not None:
            self.managed_by_akeyless = managed_by_akeyless
        if max_versions is not None:
            self.max_versions = max_versions
        if next_auto_rotate_type is not None:
            self.next_auto_rotate_type = next_auto_rotate_type
        if number_of_versions_to_save is not None:
            self.number_of_versions_to_save = number_of_versions_to_save
        if rotation_hour is not None:
            self.rotation_hour = rotation_hour
        if rotation_interval_min is not None:
            self.rotation_interval_min = rotation_interval_min
        if rotation_statement is not None:
            self.rotation_statement = rotation_statement
        if rotator_creds_type is not None:
            self.rotator_creds_type = rotator_creds_type
        if rotator_status is not None:
            self.rotator_status = rotator_status
        if rotator_type is not None:
            self.rotator_type = rotator_type
        if same_password is not None:
            self.same_password = same_password
        if services_details is not None:
            self.services_details = services_details
        if timeout_seconds is not None:
            self.timeout_seconds = timeout_seconds

    @property
    def delete_previous_version_in_days(self):
        """Gets the delete_previous_version_in_days of this RotatedSecretDetailsInfo.  # noqa: E501


        :return: The delete_previous_version_in_days of this RotatedSecretDetailsInfo.  # noqa: E501
        :rtype: int
        """
        return self._delete_previous_version_in_days

    @delete_previous_version_in_days.setter
    def delete_previous_version_in_days(self, delete_previous_version_in_days):
        """Sets the delete_previous_version_in_days of this RotatedSecretDetailsInfo.


        :param delete_previous_version_in_days: The delete_previous_version_in_days of this RotatedSecretDetailsInfo.  # noqa: E501
        :type: int
        """

        self._delete_previous_version_in_days = delete_previous_version_in_days

    @property
    def enable_custom_password_policy(self):
        """Gets the enable_custom_password_policy of this RotatedSecretDetailsInfo.  # noqa: E501


        :return: The enable_custom_password_policy of this RotatedSecretDetailsInfo.  # noqa: E501
        :rtype: bool
        """
        return self._enable_custom_password_policy

    @enable_custom_password_policy.setter
    def enable_custom_password_policy(self, enable_custom_password_policy):
        """Sets the enable_custom_password_policy of this RotatedSecretDetailsInfo.


        :param enable_custom_password_policy: The enable_custom_password_policy of this RotatedSecretDetailsInfo.  # noqa: E501
        :type: bool
        """

        self._enable_custom_password_policy = enable_custom_password_policy

    @property
    def grace_rotation(self):
        """Gets the grace_rotation of this RotatedSecretDetailsInfo.  # noqa: E501


        :return: The grace_rotation of this RotatedSecretDetailsInfo.  # noqa: E501
        :rtype: bool
        """
        return self._grace_rotation

    @grace_rotation.setter
    def grace_rotation(self, grace_rotation):
        """Sets the grace_rotation of this RotatedSecretDetailsInfo.


        :param grace_rotation: The grace_rotation of this RotatedSecretDetailsInfo.  # noqa: E501
        :type: bool
        """

        self._grace_rotation = grace_rotation

    @property
    def grace_rotation_hour(self):
        """Gets the grace_rotation_hour of this RotatedSecretDetailsInfo.  # noqa: E501


        :return: The grace_rotation_hour of this RotatedSecretDetailsInfo.  # noqa: E501
        :rtype: int
        """
        return self._grace_rotation_hour

    @grace_rotation_hour.setter
    def grace_rotation_hour(self, grace_rotation_hour):
        """Sets the grace_rotation_hour of this RotatedSecretDetailsInfo.


        :param grace_rotation_hour: The grace_rotation_hour of this RotatedSecretDetailsInfo.  # noqa: E501
        :type: int
        """

        self._grace_rotation_hour = grace_rotation_hour

    @property
    def grace_rotation_interval(self):
        """Gets the grace_rotation_interval of this RotatedSecretDetailsInfo.  # noqa: E501


        :return: The grace_rotation_interval of this RotatedSecretDetailsInfo.  # noqa: E501
        :rtype: int
        """
        return self._grace_rotation_interval

    @grace_rotation_interval.setter
    def grace_rotation_interval(self, grace_rotation_interval):
        """Sets the grace_rotation_interval of this RotatedSecretDetailsInfo.


        :param grace_rotation_interval: The grace_rotation_interval of this RotatedSecretDetailsInfo.  # noqa: E501
        :type: int
        """

        self._grace_rotation_interval = grace_rotation_interval

    @property
    def gw_cluster_id(self):
        """Gets the gw_cluster_id of this RotatedSecretDetailsInfo.  # noqa: E501


        :return: The gw_cluster_id of this RotatedSecretDetailsInfo.  # noqa: E501
        :rtype: int
        """
        return self._gw_cluster_id

    @gw_cluster_id.setter
    def gw_cluster_id(self, gw_cluster_id):
        """Sets the gw_cluster_id of this RotatedSecretDetailsInfo.


        :param gw_cluster_id: The gw_cluster_id of this RotatedSecretDetailsInfo.  # noqa: E501
        :type: int
        """

        self._gw_cluster_id = gw_cluster_id

    @property
    def last_rotation_error(self):
        """Gets the last_rotation_error of this RotatedSecretDetailsInfo.  # noqa: E501


        :return: The last_rotation_error of this RotatedSecretDetailsInfo.  # noqa: E501
        :rtype: str
        """
        return self._last_rotation_error

    @last_rotation_error.setter
    def last_rotation_error(self, last_rotation_error):
        """Sets the last_rotation_error of this RotatedSecretDetailsInfo.


        :param last_rotation_error: The last_rotation_error of this RotatedSecretDetailsInfo.  # noqa: E501
        :type: str
        """

        self._last_rotation_error = last_rotation_error

    @property
    def managed_by_akeyless(self):
        """Gets the managed_by_akeyless of this RotatedSecretDetailsInfo.  # noqa: E501


        :return: The managed_by_akeyless of this RotatedSecretDetailsInfo.  # noqa: E501
        :rtype: bool
        """
        return self._managed_by_akeyless

    @managed_by_akeyless.setter
    def managed_by_akeyless(self, managed_by_akeyless):
        """Sets the managed_by_akeyless of this RotatedSecretDetailsInfo.


        :param managed_by_akeyless: The managed_by_akeyless of this RotatedSecretDetailsInfo.  # noqa: E501
        :type: bool
        """

        self._managed_by_akeyless = managed_by_akeyless

    @property
    def max_versions(self):
        """Gets the max_versions of this RotatedSecretDetailsInfo.  # noqa: E501


        :return: The max_versions of this RotatedSecretDetailsInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_versions

    @max_versions.setter
    def max_versions(self, max_versions):
        """Sets the max_versions of this RotatedSecretDetailsInfo.


        :param max_versions: The max_versions of this RotatedSecretDetailsInfo.  # noqa: E501
        :type: int
        """

        self._max_versions = max_versions

    @property
    def next_auto_rotate_type(self):
        """Gets the next_auto_rotate_type of this RotatedSecretDetailsInfo.  # noqa: E501


        :return: The next_auto_rotate_type of this RotatedSecretDetailsInfo.  # noqa: E501
        :rtype: str
        """
        return self._next_auto_rotate_type

    @next_auto_rotate_type.setter
    def next_auto_rotate_type(self, next_auto_rotate_type):
        """Sets the next_auto_rotate_type of this RotatedSecretDetailsInfo.


        :param next_auto_rotate_type: The next_auto_rotate_type of this RotatedSecretDetailsInfo.  # noqa: E501
        :type: str
        """

        self._next_auto_rotate_type = next_auto_rotate_type

    @property
    def number_of_versions_to_save(self):
        """Gets the number_of_versions_to_save of this RotatedSecretDetailsInfo.  # noqa: E501


        :return: The number_of_versions_to_save of this RotatedSecretDetailsInfo.  # noqa: E501
        :rtype: int
        """
        return self._number_of_versions_to_save

    @number_of_versions_to_save.setter
    def number_of_versions_to_save(self, number_of_versions_to_save):
        """Sets the number_of_versions_to_save of this RotatedSecretDetailsInfo.


        :param number_of_versions_to_save: The number_of_versions_to_save of this RotatedSecretDetailsInfo.  # noqa: E501
        :type: int
        """

        self._number_of_versions_to_save = number_of_versions_to_save

    @property
    def rotation_hour(self):
        """Gets the rotation_hour of this RotatedSecretDetailsInfo.  # noqa: E501


        :return: The rotation_hour of this RotatedSecretDetailsInfo.  # noqa: E501
        :rtype: int
        """
        return self._rotation_hour

    @rotation_hour.setter
    def rotation_hour(self, rotation_hour):
        """Sets the rotation_hour of this RotatedSecretDetailsInfo.


        :param rotation_hour: The rotation_hour of this RotatedSecretDetailsInfo.  # noqa: E501
        :type: int
        """

        self._rotation_hour = rotation_hour

    @property
    def rotation_interval_min(self):
        """Gets the rotation_interval_min of this RotatedSecretDetailsInfo.  # noqa: E501


        :return: The rotation_interval_min of this RotatedSecretDetailsInfo.  # noqa: E501
        :rtype: bool
        """
        return self._rotation_interval_min

    @rotation_interval_min.setter
    def rotation_interval_min(self, rotation_interval_min):
        """Sets the rotation_interval_min of this RotatedSecretDetailsInfo.


        :param rotation_interval_min: The rotation_interval_min of this RotatedSecretDetailsInfo.  # noqa: E501
        :type: bool
        """

        self._rotation_interval_min = rotation_interval_min

    @property
    def rotation_statement(self):
        """Gets the rotation_statement of this RotatedSecretDetailsInfo.  # noqa: E501


        :return: The rotation_statement of this RotatedSecretDetailsInfo.  # noqa: E501
        :rtype: str
        """
        return self._rotation_statement

    @rotation_statement.setter
    def rotation_statement(self, rotation_statement):
        """Sets the rotation_statement of this RotatedSecretDetailsInfo.


        :param rotation_statement: The rotation_statement of this RotatedSecretDetailsInfo.  # noqa: E501
        :type: str
        """

        self._rotation_statement = rotation_statement

    @property
    def rotator_creds_type(self):
        """Gets the rotator_creds_type of this RotatedSecretDetailsInfo.  # noqa: E501


        :return: The rotator_creds_type of this RotatedSecretDetailsInfo.  # noqa: E501
        :rtype: str
        """
        return self._rotator_creds_type

    @rotator_creds_type.setter
    def rotator_creds_type(self, rotator_creds_type):
        """Sets the rotator_creds_type of this RotatedSecretDetailsInfo.


        :param rotator_creds_type: The rotator_creds_type of this RotatedSecretDetailsInfo.  # noqa: E501
        :type: str
        """

        self._rotator_creds_type = rotator_creds_type

    @property
    def rotator_status(self):
        """Gets the rotator_status of this RotatedSecretDetailsInfo.  # noqa: E501

        RotationStatus defines types of rotation Status  # noqa: E501

        :return: The rotator_status of this RotatedSecretDetailsInfo.  # noqa: E501
        :rtype: str
        """
        return self._rotator_status

    @rotator_status.setter
    def rotator_status(self, rotator_status):
        """Sets the rotator_status of this RotatedSecretDetailsInfo.

        RotationStatus defines types of rotation Status  # noqa: E501

        :param rotator_status: The rotator_status of this RotatedSecretDetailsInfo.  # noqa: E501
        :type: str
        """

        self._rotator_status = rotator_status

    @property
    def rotator_type(self):
        """Gets the rotator_type of this RotatedSecretDetailsInfo.  # noqa: E501


        :return: The rotator_type of this RotatedSecretDetailsInfo.  # noqa: E501
        :rtype: str
        """
        return self._rotator_type

    @rotator_type.setter
    def rotator_type(self, rotator_type):
        """Sets the rotator_type of this RotatedSecretDetailsInfo.


        :param rotator_type: The rotator_type of this RotatedSecretDetailsInfo.  # noqa: E501
        :type: str
        """

        self._rotator_type = rotator_type

    @property
    def same_password(self):
        """Gets the same_password of this RotatedSecretDetailsInfo.  # noqa: E501


        :return: The same_password of this RotatedSecretDetailsInfo.  # noqa: E501
        :rtype: bool
        """
        return self._same_password

    @same_password.setter
    def same_password(self, same_password):
        """Sets the same_password of this RotatedSecretDetailsInfo.


        :param same_password: The same_password of this RotatedSecretDetailsInfo.  # noqa: E501
        :type: bool
        """

        self._same_password = same_password

    @property
    def services_details(self):
        """Gets the services_details of this RotatedSecretDetailsInfo.  # noqa: E501


        :return: The services_details of this RotatedSecretDetailsInfo.  # noqa: E501
        :rtype: list[WindowsService]
        """
        return self._services_details

    @services_details.setter
    def services_details(self, services_details):
        """Sets the services_details of this RotatedSecretDetailsInfo.


        :param services_details: The services_details of this RotatedSecretDetailsInfo.  # noqa: E501
        :type: list[WindowsService]
        """

        self._services_details = services_details

    @property
    def timeout_seconds(self):
        """Gets the timeout_seconds of this RotatedSecretDetailsInfo.  # noqa: E501


        :return: The timeout_seconds of this RotatedSecretDetailsInfo.  # noqa: E501
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        """Sets the timeout_seconds of this RotatedSecretDetailsInfo.


        :param timeout_seconds: The timeout_seconds of this RotatedSecretDetailsInfo.  # noqa: E501
        :type: int
        """

        self._timeout_seconds = timeout_seconds

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
        if not isinstance(other, RotatedSecretDetailsInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RotatedSecretDetailsInfo):
            return True

        return self.to_dict() != other.to_dict()
