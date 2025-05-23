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


class CreateGcpTarget(object):
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
        'comment': 'str',
        'description': 'str',
        'gcp_key': 'str',
        'json': 'bool',
        'key': 'str',
        'max_versions': 'str',
        'name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'use_gw_cloud_identity': 'bool'
    }

    attribute_map = {
        'comment': 'comment',
        'description': 'description',
        'gcp_key': 'gcp-key',
        'json': 'json',
        'key': 'key',
        'max_versions': 'max-versions',
        'name': 'name',
        'token': 'token',
        'uid_token': 'uid-token',
        'use_gw_cloud_identity': 'use-gw-cloud-identity'
    }

    def __init__(self, comment=None, description=None, gcp_key=None, json=False, key=None, max_versions=None, name=None, token=None, uid_token=None, use_gw_cloud_identity=None, local_vars_configuration=None):  # noqa: E501
        """CreateGcpTarget - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._comment = None
        self._description = None
        self._gcp_key = None
        self._json = None
        self._key = None
        self._max_versions = None
        self._name = None
        self._token = None
        self._uid_token = None
        self._use_gw_cloud_identity = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if description is not None:
            self.description = description
        if gcp_key is not None:
            self.gcp_key = gcp_key
        if json is not None:
            self.json = json
        if key is not None:
            self.key = key
        if max_versions is not None:
            self.max_versions = max_versions
        self.name = name
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if use_gw_cloud_identity is not None:
            self.use_gw_cloud_identity = use_gw_cloud_identity

    @property
    def comment(self):
        """Gets the comment of this CreateGcpTarget.  # noqa: E501

        Deprecated - use description  # noqa: E501

        :return: The comment of this CreateGcpTarget.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CreateGcpTarget.

        Deprecated - use description  # noqa: E501

        :param comment: The comment of this CreateGcpTarget.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def description(self):
        """Gets the description of this CreateGcpTarget.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this CreateGcpTarget.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateGcpTarget.

        Description of the object  # noqa: E501

        :param description: The description of this CreateGcpTarget.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def gcp_key(self):
        """Gets the gcp_key of this CreateGcpTarget.  # noqa: E501

        Base64-encoded service account private key text  # noqa: E501

        :return: The gcp_key of this CreateGcpTarget.  # noqa: E501
        :rtype: str
        """
        return self._gcp_key

    @gcp_key.setter
    def gcp_key(self, gcp_key):
        """Sets the gcp_key of this CreateGcpTarget.

        Base64-encoded service account private key text  # noqa: E501

        :param gcp_key: The gcp_key of this CreateGcpTarget.  # noqa: E501
        :type: str
        """

        self._gcp_key = gcp_key

    @property
    def json(self):
        """Gets the json of this CreateGcpTarget.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this CreateGcpTarget.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this CreateGcpTarget.

        Set output format to JSON  # noqa: E501

        :param json: The json of this CreateGcpTarget.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def key(self):
        """Gets the key of this CreateGcpTarget.  # noqa: E501

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The key of this CreateGcpTarget.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CreateGcpTarget.

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param key: The key of this CreateGcpTarget.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def max_versions(self):
        """Gets the max_versions of this CreateGcpTarget.  # noqa: E501

        Set the maximum number of versions, limited by the account settings defaults.  # noqa: E501

        :return: The max_versions of this CreateGcpTarget.  # noqa: E501
        :rtype: str
        """
        return self._max_versions

    @max_versions.setter
    def max_versions(self, max_versions):
        """Sets the max_versions of this CreateGcpTarget.

        Set the maximum number of versions, limited by the account settings defaults.  # noqa: E501

        :param max_versions: The max_versions of this CreateGcpTarget.  # noqa: E501
        :type: str
        """

        self._max_versions = max_versions

    @property
    def name(self):
        """Gets the name of this CreateGcpTarget.  # noqa: E501

        Target name  # noqa: E501

        :return: The name of this CreateGcpTarget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateGcpTarget.

        Target name  # noqa: E501

        :param name: The name of this CreateGcpTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def token(self):
        """Gets the token of this CreateGcpTarget.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this CreateGcpTarget.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CreateGcpTarget.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this CreateGcpTarget.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this CreateGcpTarget.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this CreateGcpTarget.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this CreateGcpTarget.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this CreateGcpTarget.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def use_gw_cloud_identity(self):
        """Gets the use_gw_cloud_identity of this CreateGcpTarget.  # noqa: E501


        :return: The use_gw_cloud_identity of this CreateGcpTarget.  # noqa: E501
        :rtype: bool
        """
        return self._use_gw_cloud_identity

    @use_gw_cloud_identity.setter
    def use_gw_cloud_identity(self, use_gw_cloud_identity):
        """Sets the use_gw_cloud_identity of this CreateGcpTarget.


        :param use_gw_cloud_identity: The use_gw_cloud_identity of this CreateGcpTarget.  # noqa: E501
        :type: bool
        """

        self._use_gw_cloud_identity = use_gw_cloud_identity

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
        if not isinstance(other, CreateGcpTarget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateGcpTarget):
            return True

        return self.to_dict() != other.to_dict()
