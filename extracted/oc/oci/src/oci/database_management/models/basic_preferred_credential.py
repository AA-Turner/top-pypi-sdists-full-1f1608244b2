# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101

from .preferred_credential import PreferredCredential
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BasicPreferredCredential(PreferredCredential):
    """
    The details of the 'BASIC' preferred credential.
    """

    #: A constant which can be used with the role property of a BasicPreferredCredential.
    #: This constant has a value of "NORMAL"
    ROLE_NORMAL = "NORMAL"

    #: A constant which can be used with the role property of a BasicPreferredCredential.
    #: This constant has a value of "SYSDBA"
    ROLE_SYSDBA = "SYSDBA"

    #: A constant which can be used with the role property of a BasicPreferredCredential.
    #: This constant has a value of "SYSDG"
    ROLE_SYSDG = "SYSDG"

    def __init__(self, **kwargs):
        """
        Initializes a new BasicPreferredCredential object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.BasicPreferredCredential.type` attribute
        of this class is ``BASIC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this BasicPreferredCredential.
            Allowed values for this property are: "BASIC", "NAMED_CREDENTIAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param credential_name:
            The value to assign to the credential_name property of this BasicPreferredCredential.
        :type credential_name: str

        :param status:
            The value to assign to the status property of this BasicPreferredCredential.
            Allowed values for this property are: "SET", "NOT_SET", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param is_accessible:
            The value to assign to the is_accessible property of this BasicPreferredCredential.
        :type is_accessible: bool

        :param user_name:
            The value to assign to the user_name property of this BasicPreferredCredential.
        :type user_name: str

        :param role:
            The value to assign to the role property of this BasicPreferredCredential.
            Allowed values for this property are: "NORMAL", "SYSDBA", "SYSDG", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type role: str

        :param password_secret_id:
            The value to assign to the password_secret_id property of this BasicPreferredCredential.
        :type password_secret_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'credential_name': 'str',
            'status': 'str',
            'is_accessible': 'bool',
            'user_name': 'str',
            'role': 'str',
            'password_secret_id': 'str'
        }
        self.attribute_map = {
            'type': 'type',
            'credential_name': 'credentialName',
            'status': 'status',
            'is_accessible': 'isAccessible',
            'user_name': 'userName',
            'role': 'role',
            'password_secret_id': 'passwordSecretId'
        }
        self._type = None
        self._credential_name = None
        self._status = None
        self._is_accessible = None
        self._user_name = None
        self._role = None
        self._password_secret_id = None
        self._type = 'BASIC'

    @property
    def user_name(self):
        """
        Gets the user_name of this BasicPreferredCredential.
        The user name used to connect to the database.


        :return: The user_name of this BasicPreferredCredential.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this BasicPreferredCredential.
        The user name used to connect to the database.


        :param user_name: The user_name of this BasicPreferredCredential.
        :type: str
        """
        self._user_name = user_name

    @property
    def role(self):
        """
        Gets the role of this BasicPreferredCredential.
        The role of the database user.

        Allowed values for this property are: "NORMAL", "SYSDBA", "SYSDG", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The role of this BasicPreferredCredential.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this BasicPreferredCredential.
        The role of the database user.


        :param role: The role of this BasicPreferredCredential.
        :type: str
        """
        allowed_values = ["NORMAL", "SYSDBA", "SYSDG"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            role = 'UNKNOWN_ENUM_VALUE'
        self._role = role

    @property
    def password_secret_id(self):
        """
        Gets the password_secret_id of this BasicPreferredCredential.
        The `OCID`__ of the Vault service secret that contains the database user password.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The password_secret_id of this BasicPreferredCredential.
        :rtype: str
        """
        return self._password_secret_id

    @password_secret_id.setter
    def password_secret_id(self, password_secret_id):
        """
        Sets the password_secret_id of this BasicPreferredCredential.
        The `OCID`__ of the Vault service secret that contains the database user password.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param password_secret_id: The password_secret_id of this BasicPreferredCredential.
        :type: str
        """
        self._password_secret_id = password_secret_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
