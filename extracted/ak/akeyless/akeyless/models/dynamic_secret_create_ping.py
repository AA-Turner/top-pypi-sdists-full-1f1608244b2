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


class DynamicSecretCreatePing(object):
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
        'delete_protection': 'str',
        'description': 'str',
        'json': 'bool',
        'name': 'str',
        'ping_administrative_port': 'str',
        'ping_atm_id': 'str',
        'ping_authorization_port': 'str',
        'ping_cert_subject_dn': 'str',
        'ping_client_authentication_type': 'str',
        'ping_enforce_replay_prevention': 'str',
        'ping_grant_types': 'list[str]',
        'ping_issuer_dn': 'str',
        'ping_jwks': 'str',
        'ping_jwks_url': 'str',
        'ping_password': 'str',
        'ping_privileged_user': 'str',
        'ping_redirect_uris': 'list[str]',
        'ping_restricted_scopes': 'list[str]',
        'ping_signing_algo': 'str',
        'ping_url': 'str',
        'producer_encryption_key_name': 'str',
        'tags': 'list[str]',
        'target_name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'user_ttl': 'str'
    }

    attribute_map = {
        'delete_protection': 'delete_protection',
        'description': 'description',
        'json': 'json',
        'name': 'name',
        'ping_administrative_port': 'ping-administrative-port',
        'ping_atm_id': 'ping-atm-id',
        'ping_authorization_port': 'ping-authorization-port',
        'ping_cert_subject_dn': 'ping-cert-subject-dn',
        'ping_client_authentication_type': 'ping-client-authentication-type',
        'ping_enforce_replay_prevention': 'ping-enforce-replay-prevention',
        'ping_grant_types': 'ping-grant-types',
        'ping_issuer_dn': 'ping-issuer-dn',
        'ping_jwks': 'ping-jwks',
        'ping_jwks_url': 'ping-jwks-url',
        'ping_password': 'ping-password',
        'ping_privileged_user': 'ping-privileged-user',
        'ping_redirect_uris': 'ping-redirect-uris',
        'ping_restricted_scopes': 'ping-restricted-scopes',
        'ping_signing_algo': 'ping-signing-algo',
        'ping_url': 'ping-url',
        'producer_encryption_key_name': 'producer-encryption-key-name',
        'tags': 'tags',
        'target_name': 'target-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'user_ttl': 'user-ttl'
    }

    def __init__(self, delete_protection=None, description=None, json=False, name=None, ping_administrative_port='9999', ping_atm_id=None, ping_authorization_port='9031', ping_cert_subject_dn=None, ping_client_authentication_type='CLIENT_SECRET', ping_enforce_replay_prevention='false', ping_grant_types=None, ping_issuer_dn=None, ping_jwks=None, ping_jwks_url=None, ping_password=None, ping_privileged_user=None, ping_redirect_uris=None, ping_restricted_scopes=None, ping_signing_algo=None, ping_url=None, producer_encryption_key_name=None, tags=None, target_name=None, token=None, uid_token=None, user_ttl='60m', local_vars_configuration=None):  # noqa: E501
        """DynamicSecretCreatePing - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._delete_protection = None
        self._description = None
        self._json = None
        self._name = None
        self._ping_administrative_port = None
        self._ping_atm_id = None
        self._ping_authorization_port = None
        self._ping_cert_subject_dn = None
        self._ping_client_authentication_type = None
        self._ping_enforce_replay_prevention = None
        self._ping_grant_types = None
        self._ping_issuer_dn = None
        self._ping_jwks = None
        self._ping_jwks_url = None
        self._ping_password = None
        self._ping_privileged_user = None
        self._ping_redirect_uris = None
        self._ping_restricted_scopes = None
        self._ping_signing_algo = None
        self._ping_url = None
        self._producer_encryption_key_name = None
        self._tags = None
        self._target_name = None
        self._token = None
        self._uid_token = None
        self._user_ttl = None
        self.discriminator = None

        if delete_protection is not None:
            self.delete_protection = delete_protection
        if description is not None:
            self.description = description
        if json is not None:
            self.json = json
        self.name = name
        if ping_administrative_port is not None:
            self.ping_administrative_port = ping_administrative_port
        if ping_atm_id is not None:
            self.ping_atm_id = ping_atm_id
        if ping_authorization_port is not None:
            self.ping_authorization_port = ping_authorization_port
        if ping_cert_subject_dn is not None:
            self.ping_cert_subject_dn = ping_cert_subject_dn
        if ping_client_authentication_type is not None:
            self.ping_client_authentication_type = ping_client_authentication_type
        if ping_enforce_replay_prevention is not None:
            self.ping_enforce_replay_prevention = ping_enforce_replay_prevention
        if ping_grant_types is not None:
            self.ping_grant_types = ping_grant_types
        if ping_issuer_dn is not None:
            self.ping_issuer_dn = ping_issuer_dn
        if ping_jwks is not None:
            self.ping_jwks = ping_jwks
        if ping_jwks_url is not None:
            self.ping_jwks_url = ping_jwks_url
        if ping_password is not None:
            self.ping_password = ping_password
        if ping_privileged_user is not None:
            self.ping_privileged_user = ping_privileged_user
        if ping_redirect_uris is not None:
            self.ping_redirect_uris = ping_redirect_uris
        if ping_restricted_scopes is not None:
            self.ping_restricted_scopes = ping_restricted_scopes
        if ping_signing_algo is not None:
            self.ping_signing_algo = ping_signing_algo
        if ping_url is not None:
            self.ping_url = ping_url
        if producer_encryption_key_name is not None:
            self.producer_encryption_key_name = producer_encryption_key_name
        if tags is not None:
            self.tags = tags
        if target_name is not None:
            self.target_name = target_name
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if user_ttl is not None:
            self.user_ttl = user_ttl

    @property
    def delete_protection(self):
        """Gets the delete_protection of this DynamicSecretCreatePing.  # noqa: E501

        Protection from accidental deletion of this object [true/false]  # noqa: E501

        :return: The delete_protection of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: str
        """
        return self._delete_protection

    @delete_protection.setter
    def delete_protection(self, delete_protection):
        """Sets the delete_protection of this DynamicSecretCreatePing.

        Protection from accidental deletion of this object [true/false]  # noqa: E501

        :param delete_protection: The delete_protection of this DynamicSecretCreatePing.  # noqa: E501
        :type: str
        """

        self._delete_protection = delete_protection

    @property
    def description(self):
        """Gets the description of this DynamicSecretCreatePing.  # noqa: E501

        Description of the object  # noqa: E501

        :return: The description of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DynamicSecretCreatePing.

        Description of the object  # noqa: E501

        :param description: The description of this DynamicSecretCreatePing.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def json(self):
        """Gets the json of this DynamicSecretCreatePing.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this DynamicSecretCreatePing.

        Set output format to JSON  # noqa: E501

        :param json: The json of this DynamicSecretCreatePing.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def name(self):
        """Gets the name of this DynamicSecretCreatePing.  # noqa: E501

        Dynamic secret name  # noqa: E501

        :return: The name of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DynamicSecretCreatePing.

        Dynamic secret name  # noqa: E501

        :param name: The name of this DynamicSecretCreatePing.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def ping_administrative_port(self):
        """Gets the ping_administrative_port of this DynamicSecretCreatePing.  # noqa: E501

        Ping Federate administrative port  # noqa: E501

        :return: The ping_administrative_port of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: str
        """
        return self._ping_administrative_port

    @ping_administrative_port.setter
    def ping_administrative_port(self, ping_administrative_port):
        """Sets the ping_administrative_port of this DynamicSecretCreatePing.

        Ping Federate administrative port  # noqa: E501

        :param ping_administrative_port: The ping_administrative_port of this DynamicSecretCreatePing.  # noqa: E501
        :type: str
        """

        self._ping_administrative_port = ping_administrative_port

    @property
    def ping_atm_id(self):
        """Gets the ping_atm_id of this DynamicSecretCreatePing.  # noqa: E501

        Set a specific Access Token Management (ATM) instance for the created OAuth Client by providing the ATM Id. If no explicit value is given, the default pingfederate server ATM will be set.  # noqa: E501

        :return: The ping_atm_id of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: str
        """
        return self._ping_atm_id

    @ping_atm_id.setter
    def ping_atm_id(self, ping_atm_id):
        """Sets the ping_atm_id of this DynamicSecretCreatePing.

        Set a specific Access Token Management (ATM) instance for the created OAuth Client by providing the ATM Id. If no explicit value is given, the default pingfederate server ATM will be set.  # noqa: E501

        :param ping_atm_id: The ping_atm_id of this DynamicSecretCreatePing.  # noqa: E501
        :type: str
        """

        self._ping_atm_id = ping_atm_id

    @property
    def ping_authorization_port(self):
        """Gets the ping_authorization_port of this DynamicSecretCreatePing.  # noqa: E501

        Ping Federate authorization port  # noqa: E501

        :return: The ping_authorization_port of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: str
        """
        return self._ping_authorization_port

    @ping_authorization_port.setter
    def ping_authorization_port(self, ping_authorization_port):
        """Sets the ping_authorization_port of this DynamicSecretCreatePing.

        Ping Federate authorization port  # noqa: E501

        :param ping_authorization_port: The ping_authorization_port of this DynamicSecretCreatePing.  # noqa: E501
        :type: str
        """

        self._ping_authorization_port = ping_authorization_port

    @property
    def ping_cert_subject_dn(self):
        """Gets the ping_cert_subject_dn of this DynamicSecretCreatePing.  # noqa: E501

        The subject DN of the client certificate. If no explicit value is given, the producer will create CA certificate and matched client certificate and return it as value. Used in conjunction with ping-issuer-dn (relevant for CLIENT_TLS_CERTIFICATE authentication method)  # noqa: E501

        :return: The ping_cert_subject_dn of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: str
        """
        return self._ping_cert_subject_dn

    @ping_cert_subject_dn.setter
    def ping_cert_subject_dn(self, ping_cert_subject_dn):
        """Sets the ping_cert_subject_dn of this DynamicSecretCreatePing.

        The subject DN of the client certificate. If no explicit value is given, the producer will create CA certificate and matched client certificate and return it as value. Used in conjunction with ping-issuer-dn (relevant for CLIENT_TLS_CERTIFICATE authentication method)  # noqa: E501

        :param ping_cert_subject_dn: The ping_cert_subject_dn of this DynamicSecretCreatePing.  # noqa: E501
        :type: str
        """

        self._ping_cert_subject_dn = ping_cert_subject_dn

    @property
    def ping_client_authentication_type(self):
        """Gets the ping_client_authentication_type of this DynamicSecretCreatePing.  # noqa: E501

        OAuth Client Authentication Type [CLIENT_SECRET, PRIVATE_KEY_JWT, CLIENT_TLS_CERTIFICATE]  # noqa: E501

        :return: The ping_client_authentication_type of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: str
        """
        return self._ping_client_authentication_type

    @ping_client_authentication_type.setter
    def ping_client_authentication_type(self, ping_client_authentication_type):
        """Sets the ping_client_authentication_type of this DynamicSecretCreatePing.

        OAuth Client Authentication Type [CLIENT_SECRET, PRIVATE_KEY_JWT, CLIENT_TLS_CERTIFICATE]  # noqa: E501

        :param ping_client_authentication_type: The ping_client_authentication_type of this DynamicSecretCreatePing.  # noqa: E501
        :type: str
        """

        self._ping_client_authentication_type = ping_client_authentication_type

    @property
    def ping_enforce_replay_prevention(self):
        """Gets the ping_enforce_replay_prevention of this DynamicSecretCreatePing.  # noqa: E501

        Determines whether PingFederate requires a unique signed JWT from the client for each action (relevant for PRIVATE_KEY_JWT authentication method) [true/false]  # noqa: E501

        :return: The ping_enforce_replay_prevention of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: str
        """
        return self._ping_enforce_replay_prevention

    @ping_enforce_replay_prevention.setter
    def ping_enforce_replay_prevention(self, ping_enforce_replay_prevention):
        """Sets the ping_enforce_replay_prevention of this DynamicSecretCreatePing.

        Determines whether PingFederate requires a unique signed JWT from the client for each action (relevant for PRIVATE_KEY_JWT authentication method) [true/false]  # noqa: E501

        :param ping_enforce_replay_prevention: The ping_enforce_replay_prevention of this DynamicSecretCreatePing.  # noqa: E501
        :type: str
        """

        self._ping_enforce_replay_prevention = ping_enforce_replay_prevention

    @property
    def ping_grant_types(self):
        """Gets the ping_grant_types of this DynamicSecretCreatePing.  # noqa: E501

        List of OAuth client grant types [IMPLICIT, AUTHORIZATION_CODE, CLIENT_CREDENTIALS, TOKEN_EXCHANGE, REFRESH_TOKEN, ASSERTION_GRANTS, PASSWORD, RESOURCE_OWNER_CREDENTIALS]. If no explicit value is given, AUTHORIZATION_CODE will be selected as default.  # noqa: E501

        :return: The ping_grant_types of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: list[str]
        """
        return self._ping_grant_types

    @ping_grant_types.setter
    def ping_grant_types(self, ping_grant_types):
        """Sets the ping_grant_types of this DynamicSecretCreatePing.

        List of OAuth client grant types [IMPLICIT, AUTHORIZATION_CODE, CLIENT_CREDENTIALS, TOKEN_EXCHANGE, REFRESH_TOKEN, ASSERTION_GRANTS, PASSWORD, RESOURCE_OWNER_CREDENTIALS]. If no explicit value is given, AUTHORIZATION_CODE will be selected as default.  # noqa: E501

        :param ping_grant_types: The ping_grant_types of this DynamicSecretCreatePing.  # noqa: E501
        :type: list[str]
        """

        self._ping_grant_types = ping_grant_types

    @property
    def ping_issuer_dn(self):
        """Gets the ping_issuer_dn of this DynamicSecretCreatePing.  # noqa: E501

        Issuer DN of trusted CA certificate that imported into Ping Federate server. You may select \\\"Trust Any\\\" to trust all the existing issuers in Ping Federate server. Used in conjunction with ping-cert-subject-dn (relevant for CLIENT_TLS_CERTIFICATE authentication method)  # noqa: E501

        :return: The ping_issuer_dn of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: str
        """
        return self._ping_issuer_dn

    @ping_issuer_dn.setter
    def ping_issuer_dn(self, ping_issuer_dn):
        """Sets the ping_issuer_dn of this DynamicSecretCreatePing.

        Issuer DN of trusted CA certificate that imported into Ping Federate server. You may select \\\"Trust Any\\\" to trust all the existing issuers in Ping Federate server. Used in conjunction with ping-cert-subject-dn (relevant for CLIENT_TLS_CERTIFICATE authentication method)  # noqa: E501

        :param ping_issuer_dn: The ping_issuer_dn of this DynamicSecretCreatePing.  # noqa: E501
        :type: str
        """

        self._ping_issuer_dn = ping_issuer_dn

    @property
    def ping_jwks(self):
        """Gets the ping_jwks of this DynamicSecretCreatePing.  # noqa: E501

        Base64-encoded JSON Web Key Set (JWKS). If no explicit value is given, the producer will create JWKs and matched signed JWT (Sign Algo: RS256) and return it as value (relevant for PRIVATE_KEY_JWT authentication method)  # noqa: E501

        :return: The ping_jwks of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: str
        """
        return self._ping_jwks

    @ping_jwks.setter
    def ping_jwks(self, ping_jwks):
        """Sets the ping_jwks of this DynamicSecretCreatePing.

        Base64-encoded JSON Web Key Set (JWKS). If no explicit value is given, the producer will create JWKs and matched signed JWT (Sign Algo: RS256) and return it as value (relevant for PRIVATE_KEY_JWT authentication method)  # noqa: E501

        :param ping_jwks: The ping_jwks of this DynamicSecretCreatePing.  # noqa: E501
        :type: str
        """

        self._ping_jwks = ping_jwks

    @property
    def ping_jwks_url(self):
        """Gets the ping_jwks_url of this DynamicSecretCreatePing.  # noqa: E501

        The URL of the JSON Web Key Set (JWKS). If no explicit value is given, the producer will create JWKs and matched signed JWT and return it as value (relevant for PRIVATE_KEY_JWT authentication method)  # noqa: E501

        :return: The ping_jwks_url of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: str
        """
        return self._ping_jwks_url

    @ping_jwks_url.setter
    def ping_jwks_url(self, ping_jwks_url):
        """Sets the ping_jwks_url of this DynamicSecretCreatePing.

        The URL of the JSON Web Key Set (JWKS). If no explicit value is given, the producer will create JWKs and matched signed JWT and return it as value (relevant for PRIVATE_KEY_JWT authentication method)  # noqa: E501

        :param ping_jwks_url: The ping_jwks_url of this DynamicSecretCreatePing.  # noqa: E501
        :type: str
        """

        self._ping_jwks_url = ping_jwks_url

    @property
    def ping_password(self):
        """Gets the ping_password of this DynamicSecretCreatePing.  # noqa: E501

        Ping Federate privileged user password  # noqa: E501

        :return: The ping_password of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: str
        """
        return self._ping_password

    @ping_password.setter
    def ping_password(self, ping_password):
        """Sets the ping_password of this DynamicSecretCreatePing.

        Ping Federate privileged user password  # noqa: E501

        :param ping_password: The ping_password of this DynamicSecretCreatePing.  # noqa: E501
        :type: str
        """

        self._ping_password = ping_password

    @property
    def ping_privileged_user(self):
        """Gets the ping_privileged_user of this DynamicSecretCreatePing.  # noqa: E501

        Ping Federate privileged user  # noqa: E501

        :return: The ping_privileged_user of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: str
        """
        return self._ping_privileged_user

    @ping_privileged_user.setter
    def ping_privileged_user(self, ping_privileged_user):
        """Sets the ping_privileged_user of this DynamicSecretCreatePing.

        Ping Federate privileged user  # noqa: E501

        :param ping_privileged_user: The ping_privileged_user of this DynamicSecretCreatePing.  # noqa: E501
        :type: str
        """

        self._ping_privileged_user = ping_privileged_user

    @property
    def ping_redirect_uris(self):
        """Gets the ping_redirect_uris of this DynamicSecretCreatePing.  # noqa: E501

        List of URIs to which the OAuth authorization server may redirect the resource owner's user agent after authorization is obtained. At least one redirection URI is required for the AUTHORIZATION_CODE and IMPLICIT grant types.  # noqa: E501

        :return: The ping_redirect_uris of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: list[str]
        """
        return self._ping_redirect_uris

    @ping_redirect_uris.setter
    def ping_redirect_uris(self, ping_redirect_uris):
        """Sets the ping_redirect_uris of this DynamicSecretCreatePing.

        List of URIs to which the OAuth authorization server may redirect the resource owner's user agent after authorization is obtained. At least one redirection URI is required for the AUTHORIZATION_CODE and IMPLICIT grant types.  # noqa: E501

        :param ping_redirect_uris: The ping_redirect_uris of this DynamicSecretCreatePing.  # noqa: E501
        :type: list[str]
        """

        self._ping_redirect_uris = ping_redirect_uris

    @property
    def ping_restricted_scopes(self):
        """Gets the ping_restricted_scopes of this DynamicSecretCreatePing.  # noqa: E501

        Limit the OAuth client to specific scopes list  # noqa: E501

        :return: The ping_restricted_scopes of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: list[str]
        """
        return self._ping_restricted_scopes

    @ping_restricted_scopes.setter
    def ping_restricted_scopes(self, ping_restricted_scopes):
        """Sets the ping_restricted_scopes of this DynamicSecretCreatePing.

        Limit the OAuth client to specific scopes list  # noqa: E501

        :param ping_restricted_scopes: The ping_restricted_scopes of this DynamicSecretCreatePing.  # noqa: E501
        :type: list[str]
        """

        self._ping_restricted_scopes = ping_restricted_scopes

    @property
    def ping_signing_algo(self):
        """Gets the ping_signing_algo of this DynamicSecretCreatePing.  # noqa: E501

        The signing algorithm that the client must use to sign its request objects [RS256,RS384,RS512,ES256,ES384,ES512,PS256,PS384,PS512] If no explicit value is given, the client can use any of the supported signing algorithms (relevant for PRIVATE_KEY_JWT authentication method)  # noqa: E501

        :return: The ping_signing_algo of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: str
        """
        return self._ping_signing_algo

    @ping_signing_algo.setter
    def ping_signing_algo(self, ping_signing_algo):
        """Sets the ping_signing_algo of this DynamicSecretCreatePing.

        The signing algorithm that the client must use to sign its request objects [RS256,RS384,RS512,ES256,ES384,ES512,PS256,PS384,PS512] If no explicit value is given, the client can use any of the supported signing algorithms (relevant for PRIVATE_KEY_JWT authentication method)  # noqa: E501

        :param ping_signing_algo: The ping_signing_algo of this DynamicSecretCreatePing.  # noqa: E501
        :type: str
        """

        self._ping_signing_algo = ping_signing_algo

    @property
    def ping_url(self):
        """Gets the ping_url of this DynamicSecretCreatePing.  # noqa: E501

        Ping URL  # noqa: E501

        :return: The ping_url of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: str
        """
        return self._ping_url

    @ping_url.setter
    def ping_url(self, ping_url):
        """Sets the ping_url of this DynamicSecretCreatePing.

        Ping URL  # noqa: E501

        :param ping_url: The ping_url of this DynamicSecretCreatePing.  # noqa: E501
        :type: str
        """

        self._ping_url = ping_url

    @property
    def producer_encryption_key_name(self):
        """Gets the producer_encryption_key_name of this DynamicSecretCreatePing.  # noqa: E501

        Dynamic producer encryption key  # noqa: E501

        :return: The producer_encryption_key_name of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: str
        """
        return self._producer_encryption_key_name

    @producer_encryption_key_name.setter
    def producer_encryption_key_name(self, producer_encryption_key_name):
        """Sets the producer_encryption_key_name of this DynamicSecretCreatePing.

        Dynamic producer encryption key  # noqa: E501

        :param producer_encryption_key_name: The producer_encryption_key_name of this DynamicSecretCreatePing.  # noqa: E501
        :type: str
        """

        self._producer_encryption_key_name = producer_encryption_key_name

    @property
    def tags(self):
        """Gets the tags of this DynamicSecretCreatePing.  # noqa: E501

        Add tags attached to this object  # noqa: E501

        :return: The tags of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DynamicSecretCreatePing.

        Add tags attached to this object  # noqa: E501

        :param tags: The tags of this DynamicSecretCreatePing.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def target_name(self):
        """Gets the target_name of this DynamicSecretCreatePing.  # noqa: E501

        Target name  # noqa: E501

        :return: The target_name of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this DynamicSecretCreatePing.

        Target name  # noqa: E501

        :param target_name: The target_name of this DynamicSecretCreatePing.  # noqa: E501
        :type: str
        """

        self._target_name = target_name

    @property
    def token(self):
        """Gets the token of this DynamicSecretCreatePing.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this DynamicSecretCreatePing.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this DynamicSecretCreatePing.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this DynamicSecretCreatePing.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this DynamicSecretCreatePing.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this DynamicSecretCreatePing.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def user_ttl(self):
        """Gets the user_ttl of this DynamicSecretCreatePing.  # noqa: E501

        The time from dynamic secret creation to expiration.  # noqa: E501

        :return: The user_ttl of this DynamicSecretCreatePing.  # noqa: E501
        :rtype: str
        """
        return self._user_ttl

    @user_ttl.setter
    def user_ttl(self, user_ttl):
        """Sets the user_ttl of this DynamicSecretCreatePing.

        The time from dynamic secret creation to expiration.  # noqa: E501

        :param user_ttl: The user_ttl of this DynamicSecretCreatePing.  # noqa: E501
        :type: str
        """

        self._user_ttl = user_ttl

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
        if not isinstance(other, DynamicSecretCreatePing):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DynamicSecretCreatePing):
            return True

        return self.to_dict() != other.to_dict()
