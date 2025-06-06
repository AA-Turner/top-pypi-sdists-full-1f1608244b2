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


class GatewayUpdateLdapAuthConfig(object):
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
        'access_id': 'str',
        'bind_dn': 'str',
        'bind_dn_password': 'str',
        'group_attr': 'str',
        'group_dn': 'str',
        'group_filter': 'str',
        'json': 'bool',
        'ldap_ca_cert': 'str',
        'ldap_enable': 'str',
        'ldap_url': 'str',
        'signing_key_data': 'str',
        'token': 'str',
        'uid_token': 'str',
        'user_attribute': 'str',
        'user_dn': 'str'
    }

    attribute_map = {
        'access_id': 'access-id',
        'bind_dn': 'bind-dn',
        'bind_dn_password': 'bind-dn-password',
        'group_attr': 'group-attr',
        'group_dn': 'group-dn',
        'group_filter': 'group-filter',
        'json': 'json',
        'ldap_ca_cert': 'ldap-ca-cert',
        'ldap_enable': 'ldap-enable',
        'ldap_url': 'ldap-url',
        'signing_key_data': 'signing-key-data',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_attribute': 'user-attribute',
        'user_dn': 'user-dn'
    }

    def __init__(self, access_id=None, bind_dn=None, bind_dn_password=None, group_attr=None, group_dn=None, group_filter=None, json=False, ldap_ca_cert=None, ldap_enable=None, ldap_url=None, signing_key_data=None, token=None, uid_token=None, user_attribute=None, user_dn=None, local_vars_configuration=None):  # noqa: E501
        """GatewayUpdateLdapAuthConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_id = None
        self._bind_dn = None
        self._bind_dn_password = None
        self._group_attr = None
        self._group_dn = None
        self._group_filter = None
        self._json = None
        self._ldap_ca_cert = None
        self._ldap_enable = None
        self._ldap_url = None
        self._signing_key_data = None
        self._token = None
        self._uid_token = None
        self._user_attribute = None
        self._user_dn = None
        self.discriminator = None

        if access_id is not None:
            self.access_id = access_id
        if bind_dn is not None:
            self.bind_dn = bind_dn
        if bind_dn_password is not None:
            self.bind_dn_password = bind_dn_password
        if group_attr is not None:
            self.group_attr = group_attr
        if group_dn is not None:
            self.group_dn = group_dn
        if group_filter is not None:
            self.group_filter = group_filter
        if json is not None:
            self.json = json
        if ldap_ca_cert is not None:
            self.ldap_ca_cert = ldap_ca_cert
        if ldap_enable is not None:
            self.ldap_enable = ldap_enable
        if ldap_url is not None:
            self.ldap_url = ldap_url
        if signing_key_data is not None:
            self.signing_key_data = signing_key_data
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if user_attribute is not None:
            self.user_attribute = user_attribute
        if user_dn is not None:
            self.user_dn = user_dn

    @property
    def access_id(self):
        """Gets the access_id of this GatewayUpdateLdapAuthConfig.  # noqa: E501

        The access ID of the Ldap auth method  # noqa: E501

        :return: The access_id of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._access_id

    @access_id.setter
    def access_id(self, access_id):
        """Sets the access_id of this GatewayUpdateLdapAuthConfig.

        The access ID of the Ldap auth method  # noqa: E501

        :param access_id: The access_id of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :type: str
        """

        self._access_id = access_id

    @property
    def bind_dn(self):
        """Gets the bind_dn of this GatewayUpdateLdapAuthConfig.  # noqa: E501

        Bind DN  # noqa: E501

        :return: The bind_dn of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._bind_dn

    @bind_dn.setter
    def bind_dn(self, bind_dn):
        """Sets the bind_dn of this GatewayUpdateLdapAuthConfig.

        Bind DN  # noqa: E501

        :param bind_dn: The bind_dn of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :type: str
        """

        self._bind_dn = bind_dn

    @property
    def bind_dn_password(self):
        """Gets the bind_dn_password of this GatewayUpdateLdapAuthConfig.  # noqa: E501

        Bind DN Password  # noqa: E501

        :return: The bind_dn_password of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._bind_dn_password

    @bind_dn_password.setter
    def bind_dn_password(self, bind_dn_password):
        """Sets the bind_dn_password of this GatewayUpdateLdapAuthConfig.

        Bind DN Password  # noqa: E501

        :param bind_dn_password: The bind_dn_password of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :type: str
        """

        self._bind_dn_password = bind_dn_password

    @property
    def group_attr(self):
        """Gets the group_attr of this GatewayUpdateLdapAuthConfig.  # noqa: E501

        Group Attr  # noqa: E501

        :return: The group_attr of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._group_attr

    @group_attr.setter
    def group_attr(self, group_attr):
        """Sets the group_attr of this GatewayUpdateLdapAuthConfig.

        Group Attr  # noqa: E501

        :param group_attr: The group_attr of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :type: str
        """

        self._group_attr = group_attr

    @property
    def group_dn(self):
        """Gets the group_dn of this GatewayUpdateLdapAuthConfig.  # noqa: E501

        Group Dn  # noqa: E501

        :return: The group_dn of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._group_dn

    @group_dn.setter
    def group_dn(self, group_dn):
        """Sets the group_dn of this GatewayUpdateLdapAuthConfig.

        Group Dn  # noqa: E501

        :param group_dn: The group_dn of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :type: str
        """

        self._group_dn = group_dn

    @property
    def group_filter(self):
        """Gets the group_filter of this GatewayUpdateLdapAuthConfig.  # noqa: E501

        Group Filter  # noqa: E501

        :return: The group_filter of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._group_filter

    @group_filter.setter
    def group_filter(self, group_filter):
        """Sets the group_filter of this GatewayUpdateLdapAuthConfig.

        Group Filter  # noqa: E501

        :param group_filter: The group_filter of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :type: str
        """

        self._group_filter = group_filter

    @property
    def json(self):
        """Gets the json of this GatewayUpdateLdapAuthConfig.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this GatewayUpdateLdapAuthConfig.

        Set output format to JSON  # noqa: E501

        :param json: The json of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def ldap_ca_cert(self):
        """Gets the ldap_ca_cert of this GatewayUpdateLdapAuthConfig.  # noqa: E501

        LDAP CA Certificate (base64 encoded)  # noqa: E501

        :return: The ldap_ca_cert of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._ldap_ca_cert

    @ldap_ca_cert.setter
    def ldap_ca_cert(self, ldap_ca_cert):
        """Sets the ldap_ca_cert of this GatewayUpdateLdapAuthConfig.

        LDAP CA Certificate (base64 encoded)  # noqa: E501

        :param ldap_ca_cert: The ldap_ca_cert of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :type: str
        """

        self._ldap_ca_cert = ldap_ca_cert

    @property
    def ldap_enable(self):
        """Gets the ldap_enable of this GatewayUpdateLdapAuthConfig.  # noqa: E501

        Enable Ldap [true/false]  # noqa: E501

        :return: The ldap_enable of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._ldap_enable

    @ldap_enable.setter
    def ldap_enable(self, ldap_enable):
        """Sets the ldap_enable of this GatewayUpdateLdapAuthConfig.

        Enable Ldap [true/false]  # noqa: E501

        :param ldap_enable: The ldap_enable of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :type: str
        """

        self._ldap_enable = ldap_enable

    @property
    def ldap_url(self):
        """Gets the ldap_url of this GatewayUpdateLdapAuthConfig.  # noqa: E501

        LDAP Server URL, e.g. ldap://planetexpress.com:389  # noqa: E501

        :return: The ldap_url of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._ldap_url

    @ldap_url.setter
    def ldap_url(self, ldap_url):
        """Sets the ldap_url of this GatewayUpdateLdapAuthConfig.

        LDAP Server URL, e.g. ldap://planetexpress.com:389  # noqa: E501

        :param ldap_url: The ldap_url of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :type: str
        """

        self._ldap_url = ldap_url

    @property
    def signing_key_data(self):
        """Gets the signing_key_data of this GatewayUpdateLdapAuthConfig.  # noqa: E501

        The private key (base64 encoded), associated with the public key defined in the Ldap auth  # noqa: E501

        :return: The signing_key_data of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._signing_key_data

    @signing_key_data.setter
    def signing_key_data(self, signing_key_data):
        """Sets the signing_key_data of this GatewayUpdateLdapAuthConfig.

        The private key (base64 encoded), associated with the public key defined in the Ldap auth  # noqa: E501

        :param signing_key_data: The signing_key_data of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :type: str
        """

        self._signing_key_data = signing_key_data

    @property
    def token(self):
        """Gets the token of this GatewayUpdateLdapAuthConfig.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayUpdateLdapAuthConfig.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayUpdateLdapAuthConfig.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayUpdateLdapAuthConfig.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_attribute(self):
        """Gets the user_attribute of this GatewayUpdateLdapAuthConfig.  # noqa: E501

        User Attribute  # noqa: E501

        :return: The user_attribute of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._user_attribute

    @user_attribute.setter
    def user_attribute(self, user_attribute):
        """Sets the user_attribute of this GatewayUpdateLdapAuthConfig.

        User Attribute  # noqa: E501

        :param user_attribute: The user_attribute of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :type: str
        """

        self._user_attribute = user_attribute

    @property
    def user_dn(self):
        """Gets the user_dn of this GatewayUpdateLdapAuthConfig.  # noqa: E501

        User DN  # noqa: E501

        :return: The user_dn of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._user_dn

    @user_dn.setter
    def user_dn(self, user_dn):
        """Sets the user_dn of this GatewayUpdateLdapAuthConfig.

        User DN  # noqa: E501

        :param user_dn: The user_dn of this GatewayUpdateLdapAuthConfig.  # noqa: E501
        :type: str
        """

        self._user_dn = user_dn

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
        if not isinstance(other, GatewayUpdateLdapAuthConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayUpdateLdapAuthConfig):
            return True

        return self.to_dict() != other.to_dict()
