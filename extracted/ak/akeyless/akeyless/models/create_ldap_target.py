# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from akeyless.configuration import Configuration


class CreateLdapTarget(object):
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
        'bind_dn': 'str',
        'bind_dn_password': 'str',
        'comment': 'str',
        'description': 'str',
        'json': 'bool',
        'key': 'str',
        'ldap_ca_cert': 'str',
        'ldap_url': 'str',
        'max_versions': 'str',
        'name': 'str',
        'server_type': 'str',
        'token': 'str',
        'token_expiration': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'bind_dn': 'bind-dn',
        'bind_dn_password': 'bind-dn-password',
        'comment': 'comment',
        'description': 'description',
        'json': 'json',
        'key': 'key',
        'ldap_ca_cert': 'ldap-ca-cert',
        'ldap_url': 'ldap-url',
        'max_versions': 'max-versions',
        'name': 'name',
        'server_type': 'server-type',
        'token': 'token',
        'token_expiration': 'token-expiration',
        'uid_token': 'uid-token'
    }

    def __init__(self, bind_dn=None, bind_dn_password=None, comment=None, description=None, json=False, key=None, ldap_ca_cert=None, ldap_url=None, max_versions=None, name=None, server_type='OpenLDAP', token=None, token_expiration=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """CreateLdapTarget - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bind_dn = None
        self._bind_dn_password = None
        self._comment = None
        self._description = None
        self._json = None
        self._key = None
        self._ldap_ca_cert = None
        self._ldap_url = None
        self._max_versions = None
        self._name = None
        self._server_type = None
        self._token = None
        self._token_expiration = None
        self._uid_token = None
        self.discriminator = None

        self.bind_dn = bind_dn
        self.bind_dn_password = bind_dn_password
        if comment is not None:
            self.comment = comment
        if description is not None:
            self.description = description
        if json is not None:
            self.json = json
        if key is not None:
            self.key = key
        if ldap_ca_cert is not None:
            self.ldap_ca_cert = ldap_ca_cert
        self.ldap_url = ldap_url
        if max_versions is not None:
            self.max_versions = max_versions
        self.name = name
        if server_type is not None:
            self.server_type = server_type
        if token is not None:
            self.token = token
        if token_expiration is not None:
            self.token_expiration = token_expiration
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def bind_dn(self):
        """Gets the bind_dn of this CreateLdapTarget.  # noqa: E501

        Bind DN  # noqa: E501

        :return: The bind_dn of this CreateLdapTarget.  # noqa: E501
        :rtype: str
        """
        return self._bind_dn

    @bind_dn.setter
    def bind_dn(self, bind_dn):
        """Sets the bind_dn of this CreateLdapTarget.

        Bind DN  # noqa: E501

        :param bind_dn: The bind_dn of this CreateLdapTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and bind_dn is None:  # noqa: E501
            raise ValueError("Invalid value for `bind_dn`, must not be `None`")  # noqa: E501

        self._bind_dn = bind_dn

    @property
    def bind_dn_password(self):
        """Gets the bind_dn_password of this CreateLdapTarget.  # noqa: E501

        Bind DN Password  # noqa: E501

        :return: The bind_dn_password of this CreateLdapTarget.  # noqa: E501
        :rtype: str
        """
        return self._bind_dn_password

    @bind_dn_password.setter
    def bind_dn_password(self, bind_dn_password):
        """Sets the bind_dn_password of this CreateLdapTarget.

        Bind DN Password  # noqa: E501

        :param bind_dn_password: The bind_dn_password of this CreateLdapTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and bind_dn_password is None:  # noqa: E501
            raise ValueError("Invalid value for `bind_dn_password`, must not be `None`")  # noqa: E501

        self._bind_dn_password = bind_dn_password

    @property
    def comment(self):
        """Gets the comment of this CreateLdapTarget.  # noqa: E501

        Deprecated - use description  # noqa: E501

        :return: The comment of this CreateLdapTarget.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CreateLdapTarget.

        Deprecated - use description  # noqa: E501

        :param comment: The comment of this CreateLdapTarget.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def description(self):
        """Gets the description of this CreateLdapTarget.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this CreateLdapTarget.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateLdapTarget.

        Description of the object  # noqa: E501

        :param description: The description of this CreateLdapTarget.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def json(self):
        """Gets the json of this CreateLdapTarget.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this CreateLdapTarget.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this CreateLdapTarget.

        Set output format to JSON  # noqa: E501

        :param json: The json of this CreateLdapTarget.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def key(self):
        """Gets the key of this CreateLdapTarget.  # noqa: E501

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this CreateLdapTarget.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CreateLdapTarget.

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this CreateLdapTarget.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def ldap_ca_cert(self):
        """Gets the ldap_ca_cert of this CreateLdapTarget.  # noqa: E501

        CA Certificate File Content  # noqa: E501

        :return: The ldap_ca_cert of this CreateLdapTarget.  # noqa: E501
        :rtype: str
        """
        return self._ldap_ca_cert

    @ldap_ca_cert.setter
    def ldap_ca_cert(self, ldap_ca_cert):
        """Sets the ldap_ca_cert of this CreateLdapTarget.

        CA Certificate File Content  # noqa: E501

        :param ldap_ca_cert: The ldap_ca_cert of this CreateLdapTarget.  # noqa: E501
        :type: str
        """

        self._ldap_ca_cert = ldap_ca_cert

    @property
    def ldap_url(self):
        """Gets the ldap_url of this CreateLdapTarget.  # noqa: E501

        LDAP Server URL  # noqa: E501

        :return: The ldap_url of this CreateLdapTarget.  # noqa: E501
        :rtype: str
        """
        return self._ldap_url

    @ldap_url.setter
    def ldap_url(self, ldap_url):
        """Sets the ldap_url of this CreateLdapTarget.

        LDAP Server URL  # noqa: E501

        :param ldap_url: The ldap_url of this CreateLdapTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ldap_url is None:  # noqa: E501
            raise ValueError("Invalid value for `ldap_url`, must not be `None`")  # noqa: E501

        self._ldap_url = ldap_url

    @property
    def max_versions(self):
        """Gets the max_versions of this CreateLdapTarget.  # noqa: E501

        Set the maximum number of versions, limited by the account settings defaults.  # noqa: E501

        :return: The max_versions of this CreateLdapTarget.  # noqa: E501
        :rtype: str
        """
        return self._max_versions

    @max_versions.setter
    def max_versions(self, max_versions):
        """Sets the max_versions of this CreateLdapTarget.

        Set the maximum number of versions, limited by the account settings defaults.  # noqa: E501

        :param max_versions: The max_versions of this CreateLdapTarget.  # noqa: E501
        :type: str
        """

        self._max_versions = max_versions

    @property
    def name(self):
        """Gets the name of this CreateLdapTarget.  # noqa: E501

        Target name  # noqa: E501

        :return: The name of this CreateLdapTarget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateLdapTarget.

        Target name  # noqa: E501

        :param name: The name of this CreateLdapTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def server_type(self):
        """Gets the server_type of this CreateLdapTarget.  # noqa: E501

        Set Ldap server type, Options:[OpenLDAP, ActiveDirectory]. Default is OpenLDAP  # noqa: E501

        :return: The server_type of this CreateLdapTarget.  # noqa: E501
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        """Sets the server_type of this CreateLdapTarget.

        Set Ldap server type, Options:[OpenLDAP, ActiveDirectory]. Default is OpenLDAP  # noqa: E501

        :param server_type: The server_type of this CreateLdapTarget.  # noqa: E501
        :type: str
        """

        self._server_type = server_type

    @property
    def token(self):
        """Gets the token of this CreateLdapTarget.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this CreateLdapTarget.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CreateLdapTarget.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this CreateLdapTarget.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def token_expiration(self):
        """Gets the token_expiration of this CreateLdapTarget.  # noqa: E501

        Token expiration  # noqa: E501

        :return: The token_expiration of this CreateLdapTarget.  # noqa: E501
        :rtype: str
        """
        return self._token_expiration

    @token_expiration.setter
    def token_expiration(self, token_expiration):
        """Sets the token_expiration of this CreateLdapTarget.

        Token expiration  # noqa: E501

        :param token_expiration: The token_expiration of this CreateLdapTarget.  # noqa: E501
        :type: str
        """

        self._token_expiration = token_expiration

    @property
    def uid_token(self):
        """Gets the uid_token of this CreateLdapTarget.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this CreateLdapTarget.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this CreateLdapTarget.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this CreateLdapTarget.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

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
        if not isinstance(other, CreateLdapTarget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateLdapTarget):
            return True

        return self.to_dict() != other.to_dict()
