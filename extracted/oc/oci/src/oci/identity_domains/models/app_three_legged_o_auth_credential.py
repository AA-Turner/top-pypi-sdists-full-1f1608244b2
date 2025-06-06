# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppThreeLeggedOAuthCredential(object):
    """
    The value of this attribute persists any OAuth access token that the system uses to connect to this ManagedApp. The system obtains this access token using an OAuth protocol flow that could be two-legged or three-legged. A two-legged flow involves only the requester and the server. A three-legged flow also requires the consent of a user -- in this case the consent of an administrator.

    **SCIM++ Properties:**
    - idcsSearchable: true
    - multiValued: false
    - mutability: readWrite
    - required: false
    - returned: default
    - type: complex
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AppThreeLeggedOAuthCredential object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param access_token:
            The value to assign to the access_token property of this AppThreeLeggedOAuthCredential.
        :type access_token: str

        :param refresh_token:
            The value to assign to the refresh_token property of this AppThreeLeggedOAuthCredential.
        :type refresh_token: str

        :param access_token_expiry:
            The value to assign to the access_token_expiry property of this AppThreeLeggedOAuthCredential.
        :type access_token_expiry: str

        """
        self.swagger_types = {
            'access_token': 'str',
            'refresh_token': 'str',
            'access_token_expiry': 'str'
        }
        self.attribute_map = {
            'access_token': 'accessToken',
            'refresh_token': 'refreshToken',
            'access_token_expiry': 'accessTokenExpiry'
        }
        self._access_token = None
        self._refresh_token = None
        self._access_token_expiry = None

    @property
    def access_token(self):
        """
        Gets the access_token of this AppThreeLeggedOAuthCredential.
        Access Token

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - idcsSensitive: encrypt
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The access_token of this AppThreeLeggedOAuthCredential.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """
        Sets the access_token of this AppThreeLeggedOAuthCredential.
        Access Token

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - idcsSensitive: encrypt
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param access_token: The access_token of this AppThreeLeggedOAuthCredential.
        :type: str
        """
        self._access_token = access_token

    @property
    def refresh_token(self):
        """
        Gets the refresh_token of this AppThreeLeggedOAuthCredential.
        Refresh Token

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - idcsSensitive: encrypt
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The refresh_token of this AppThreeLeggedOAuthCredential.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """
        Sets the refresh_token of this AppThreeLeggedOAuthCredential.
        Refresh Token

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - idcsSensitive: encrypt
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param refresh_token: The refresh_token of this AppThreeLeggedOAuthCredential.
        :type: str
        """
        self._refresh_token = refresh_token

    @property
    def access_token_expiry(self):
        """
        Gets the access_token_expiry of this AppThreeLeggedOAuthCredential.
        Access token expiry

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: dateTime
         - uniqueness: none


        :return: The access_token_expiry of this AppThreeLeggedOAuthCredential.
        :rtype: str
        """
        return self._access_token_expiry

    @access_token_expiry.setter
    def access_token_expiry(self, access_token_expiry):
        """
        Sets the access_token_expiry of this AppThreeLeggedOAuthCredential.
        Access token expiry

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: dateTime
         - uniqueness: none


        :param access_token_expiry: The access_token_expiry of this AppThreeLeggedOAuthCredential.
        :type: str
        """
        self._access_token_expiry = access_token_expiry

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
