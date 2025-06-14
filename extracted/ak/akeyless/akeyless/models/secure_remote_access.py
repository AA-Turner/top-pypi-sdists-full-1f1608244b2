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


class SecureRemoteAccess(object):
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
        'account_id': 'str',
        'allow_port_forwarding': 'bool',
        'allow_providing_external_username': 'bool',
        'bastion_api': 'str',
        'bastion_issuer': 'str',
        'bastion_issuer_id': 'int',
        'bastion_ssh': 'str',
        'block_concurrent_connections': 'bool',
        'block_concurrent_connections_level': 'str',
        'category': 'str',
        'connection_delay_seconds': 'int',
        'dashboard_url': 'str',
        'db_name': 'str',
        'domain': 'str',
        'enable': 'bool',
        'endpoint': 'str',
        'enforce_hosts_restriction': 'bool',
        'gw_cluster_id': 'int',
        'host': 'list[str]',
        'host_provider_type': 'str',
        'is_cli': 'bool',
        'is_desktop_app': 'bool',
        'is_web': 'bool',
        'isolated': 'bool',
        'native': 'bool',
        'rd_gateway_server': 'str',
        'rdp_user': 'str',
        'region': 'str',
        'rotate_after_disconnect': 'bool',
        'schema': 'str',
        'ssh_password': 'bool',
        'ssh_private_key': 'bool',
        'ssh_user': 'str',
        'status_info': 'ItemSraStatus',
        'target_hosts': 'list[TargetNameWithHosts]',
        'targets': 'list[str]',
        'url': 'str',
        'use_internal_bastion': 'bool',
        'web_proxy': 'bool'
    }

    attribute_map = {
        'account_id': 'account_id',
        'allow_port_forwarding': 'allow_port_forwarding',
        'allow_providing_external_username': 'allow_providing_external_username',
        'bastion_api': 'bastion_api',
        'bastion_issuer': 'bastion_issuer',
        'bastion_issuer_id': 'bastion_issuer_id',
        'bastion_ssh': 'bastion_ssh',
        'block_concurrent_connections': 'block_concurrent_connections',
        'block_concurrent_connections_level': 'block_concurrent_connections_level',
        'category': 'category',
        'connection_delay_seconds': 'connection_delay_seconds',
        'dashboard_url': 'dashboard_url',
        'db_name': 'db_name',
        'domain': 'domain',
        'enable': 'enable',
        'endpoint': 'endpoint',
        'enforce_hosts_restriction': 'enforce_hosts_restriction',
        'gw_cluster_id': 'gw_cluster_id',
        'host': 'host',
        'host_provider_type': 'host_provider_type',
        'is_cli': 'is_cli',
        'is_desktop_app': 'is_desktop_app',
        'is_web': 'is_web',
        'isolated': 'isolated',
        'native': 'native',
        'rd_gateway_server': 'rd_gateway_server',
        'rdp_user': 'rdp_user',
        'region': 'region',
        'rotate_after_disconnect': 'rotate_after_disconnect',
        'schema': 'schema',
        'ssh_password': 'ssh_password',
        'ssh_private_key': 'ssh_private_key',
        'ssh_user': 'ssh_user',
        'status_info': 'status_info',
        'target_hosts': 'target_hosts',
        'targets': 'targets',
        'url': 'url',
        'use_internal_bastion': 'use_internal_bastion',
        'web_proxy': 'web_proxy'
    }

    def __init__(self, account_id=None, allow_port_forwarding=None, allow_providing_external_username=None, bastion_api=None, bastion_issuer=None, bastion_issuer_id=None, bastion_ssh=None, block_concurrent_connections=None, block_concurrent_connections_level=None, category=None, connection_delay_seconds=None, dashboard_url=None, db_name=None, domain=None, enable=None, endpoint=None, enforce_hosts_restriction=None, gw_cluster_id=None, host=None, host_provider_type=None, is_cli=None, is_desktop_app=None, is_web=None, isolated=None, native=None, rd_gateway_server=None, rdp_user=None, region=None, rotate_after_disconnect=None, schema=None, ssh_password=None, ssh_private_key=None, ssh_user=None, status_info=None, target_hosts=None, targets=None, url=None, use_internal_bastion=None, web_proxy=None, local_vars_configuration=None):  # noqa: E501
        """SecureRemoteAccess - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._allow_port_forwarding = None
        self._allow_providing_external_username = None
        self._bastion_api = None
        self._bastion_issuer = None
        self._bastion_issuer_id = None
        self._bastion_ssh = None
        self._block_concurrent_connections = None
        self._block_concurrent_connections_level = None
        self._category = None
        self._connection_delay_seconds = None
        self._dashboard_url = None
        self._db_name = None
        self._domain = None
        self._enable = None
        self._endpoint = None
        self._enforce_hosts_restriction = None
        self._gw_cluster_id = None
        self._host = None
        self._host_provider_type = None
        self._is_cli = None
        self._is_desktop_app = None
        self._is_web = None
        self._isolated = None
        self._native = None
        self._rd_gateway_server = None
        self._rdp_user = None
        self._region = None
        self._rotate_after_disconnect = None
        self._schema = None
        self._ssh_password = None
        self._ssh_private_key = None
        self._ssh_user = None
        self._status_info = None
        self._target_hosts = None
        self._targets = None
        self._url = None
        self._use_internal_bastion = None
        self._web_proxy = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if allow_port_forwarding is not None:
            self.allow_port_forwarding = allow_port_forwarding
        if allow_providing_external_username is not None:
            self.allow_providing_external_username = allow_providing_external_username
        if bastion_api is not None:
            self.bastion_api = bastion_api
        if bastion_issuer is not None:
            self.bastion_issuer = bastion_issuer
        if bastion_issuer_id is not None:
            self.bastion_issuer_id = bastion_issuer_id
        if bastion_ssh is not None:
            self.bastion_ssh = bastion_ssh
        if block_concurrent_connections is not None:
            self.block_concurrent_connections = block_concurrent_connections
        if block_concurrent_connections_level is not None:
            self.block_concurrent_connections_level = block_concurrent_connections_level
        if category is not None:
            self.category = category
        if connection_delay_seconds is not None:
            self.connection_delay_seconds = connection_delay_seconds
        if dashboard_url is not None:
            self.dashboard_url = dashboard_url
        if db_name is not None:
            self.db_name = db_name
        if domain is not None:
            self.domain = domain
        if enable is not None:
            self.enable = enable
        if endpoint is not None:
            self.endpoint = endpoint
        if enforce_hosts_restriction is not None:
            self.enforce_hosts_restriction = enforce_hosts_restriction
        if gw_cluster_id is not None:
            self.gw_cluster_id = gw_cluster_id
        if host is not None:
            self.host = host
        if host_provider_type is not None:
            self.host_provider_type = host_provider_type
        if is_cli is not None:
            self.is_cli = is_cli
        if is_desktop_app is not None:
            self.is_desktop_app = is_desktop_app
        if is_web is not None:
            self.is_web = is_web
        if isolated is not None:
            self.isolated = isolated
        if native is not None:
            self.native = native
        if rd_gateway_server is not None:
            self.rd_gateway_server = rd_gateway_server
        if rdp_user is not None:
            self.rdp_user = rdp_user
        if region is not None:
            self.region = region
        if rotate_after_disconnect is not None:
            self.rotate_after_disconnect = rotate_after_disconnect
        if schema is not None:
            self.schema = schema
        if ssh_password is not None:
            self.ssh_password = ssh_password
        if ssh_private_key is not None:
            self.ssh_private_key = ssh_private_key
        if ssh_user is not None:
            self.ssh_user = ssh_user
        if status_info is not None:
            self.status_info = status_info
        if target_hosts is not None:
            self.target_hosts = target_hosts
        if targets is not None:
            self.targets = targets
        if url is not None:
            self.url = url
        if use_internal_bastion is not None:
            self.use_internal_bastion = use_internal_bastion
        if web_proxy is not None:
            self.web_proxy = web_proxy

    @property
    def account_id(self):
        """Gets the account_id of this SecureRemoteAccess.  # noqa: E501


        :return: The account_id of this SecureRemoteAccess.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this SecureRemoteAccess.


        :param account_id: The account_id of this SecureRemoteAccess.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def allow_port_forwarding(self):
        """Gets the allow_port_forwarding of this SecureRemoteAccess.  # noqa: E501


        :return: The allow_port_forwarding of this SecureRemoteAccess.  # noqa: E501
        :rtype: bool
        """
        return self._allow_port_forwarding

    @allow_port_forwarding.setter
    def allow_port_forwarding(self, allow_port_forwarding):
        """Sets the allow_port_forwarding of this SecureRemoteAccess.


        :param allow_port_forwarding: The allow_port_forwarding of this SecureRemoteAccess.  # noqa: E501
        :type: bool
        """

        self._allow_port_forwarding = allow_port_forwarding

    @property
    def allow_providing_external_username(self):
        """Gets the allow_providing_external_username of this SecureRemoteAccess.  # noqa: E501


        :return: The allow_providing_external_username of this SecureRemoteAccess.  # noqa: E501
        :rtype: bool
        """
        return self._allow_providing_external_username

    @allow_providing_external_username.setter
    def allow_providing_external_username(self, allow_providing_external_username):
        """Sets the allow_providing_external_username of this SecureRemoteAccess.


        :param allow_providing_external_username: The allow_providing_external_username of this SecureRemoteAccess.  # noqa: E501
        :type: bool
        """

        self._allow_providing_external_username = allow_providing_external_username

    @property
    def bastion_api(self):
        """Gets the bastion_api of this SecureRemoteAccess.  # noqa: E501


        :return: The bastion_api of this SecureRemoteAccess.  # noqa: E501
        :rtype: str
        """
        return self._bastion_api

    @bastion_api.setter
    def bastion_api(self, bastion_api):
        """Sets the bastion_api of this SecureRemoteAccess.


        :param bastion_api: The bastion_api of this SecureRemoteAccess.  # noqa: E501
        :type: str
        """

        self._bastion_api = bastion_api

    @property
    def bastion_issuer(self):
        """Gets the bastion_issuer of this SecureRemoteAccess.  # noqa: E501


        :return: The bastion_issuer of this SecureRemoteAccess.  # noqa: E501
        :rtype: str
        """
        return self._bastion_issuer

    @bastion_issuer.setter
    def bastion_issuer(self, bastion_issuer):
        """Sets the bastion_issuer of this SecureRemoteAccess.


        :param bastion_issuer: The bastion_issuer of this SecureRemoteAccess.  # noqa: E501
        :type: str
        """

        self._bastion_issuer = bastion_issuer

    @property
    def bastion_issuer_id(self):
        """Gets the bastion_issuer_id of this SecureRemoteAccess.  # noqa: E501


        :return: The bastion_issuer_id of this SecureRemoteAccess.  # noqa: E501
        :rtype: int
        """
        return self._bastion_issuer_id

    @bastion_issuer_id.setter
    def bastion_issuer_id(self, bastion_issuer_id):
        """Sets the bastion_issuer_id of this SecureRemoteAccess.


        :param bastion_issuer_id: The bastion_issuer_id of this SecureRemoteAccess.  # noqa: E501
        :type: int
        """

        self._bastion_issuer_id = bastion_issuer_id

    @property
    def bastion_ssh(self):
        """Gets the bastion_ssh of this SecureRemoteAccess.  # noqa: E501


        :return: The bastion_ssh of this SecureRemoteAccess.  # noqa: E501
        :rtype: str
        """
        return self._bastion_ssh

    @bastion_ssh.setter
    def bastion_ssh(self, bastion_ssh):
        """Sets the bastion_ssh of this SecureRemoteAccess.


        :param bastion_ssh: The bastion_ssh of this SecureRemoteAccess.  # noqa: E501
        :type: str
        """

        self._bastion_ssh = bastion_ssh

    @property
    def block_concurrent_connections(self):
        """Gets the block_concurrent_connections of this SecureRemoteAccess.  # noqa: E501


        :return: The block_concurrent_connections of this SecureRemoteAccess.  # noqa: E501
        :rtype: bool
        """
        return self._block_concurrent_connections

    @block_concurrent_connections.setter
    def block_concurrent_connections(self, block_concurrent_connections):
        """Sets the block_concurrent_connections of this SecureRemoteAccess.


        :param block_concurrent_connections: The block_concurrent_connections of this SecureRemoteAccess.  # noqa: E501
        :type: bool
        """

        self._block_concurrent_connections = block_concurrent_connections

    @property
    def block_concurrent_connections_level(self):
        """Gets the block_concurrent_connections_level of this SecureRemoteAccess.  # noqa: E501


        :return: The block_concurrent_connections_level of this SecureRemoteAccess.  # noqa: E501
        :rtype: str
        """
        return self._block_concurrent_connections_level

    @block_concurrent_connections_level.setter
    def block_concurrent_connections_level(self, block_concurrent_connections_level):
        """Sets the block_concurrent_connections_level of this SecureRemoteAccess.


        :param block_concurrent_connections_level: The block_concurrent_connections_level of this SecureRemoteAccess.  # noqa: E501
        :type: str
        """

        self._block_concurrent_connections_level = block_concurrent_connections_level

    @property
    def category(self):
        """Gets the category of this SecureRemoteAccess.  # noqa: E501


        :return: The category of this SecureRemoteAccess.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this SecureRemoteAccess.


        :param category: The category of this SecureRemoteAccess.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def connection_delay_seconds(self):
        """Gets the connection_delay_seconds of this SecureRemoteAccess.  # noqa: E501


        :return: The connection_delay_seconds of this SecureRemoteAccess.  # noqa: E501
        :rtype: int
        """
        return self._connection_delay_seconds

    @connection_delay_seconds.setter
    def connection_delay_seconds(self, connection_delay_seconds):
        """Sets the connection_delay_seconds of this SecureRemoteAccess.


        :param connection_delay_seconds: The connection_delay_seconds of this SecureRemoteAccess.  # noqa: E501
        :type: int
        """

        self._connection_delay_seconds = connection_delay_seconds

    @property
    def dashboard_url(self):
        """Gets the dashboard_url of this SecureRemoteAccess.  # noqa: E501


        :return: The dashboard_url of this SecureRemoteAccess.  # noqa: E501
        :rtype: str
        """
        return self._dashboard_url

    @dashboard_url.setter
    def dashboard_url(self, dashboard_url):
        """Sets the dashboard_url of this SecureRemoteAccess.


        :param dashboard_url: The dashboard_url of this SecureRemoteAccess.  # noqa: E501
        :type: str
        """

        self._dashboard_url = dashboard_url

    @property
    def db_name(self):
        """Gets the db_name of this SecureRemoteAccess.  # noqa: E501


        :return: The db_name of this SecureRemoteAccess.  # noqa: E501
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this SecureRemoteAccess.


        :param db_name: The db_name of this SecureRemoteAccess.  # noqa: E501
        :type: str
        """

        self._db_name = db_name

    @property
    def domain(self):
        """Gets the domain of this SecureRemoteAccess.  # noqa: E501


        :return: The domain of this SecureRemoteAccess.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this SecureRemoteAccess.


        :param domain: The domain of this SecureRemoteAccess.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def enable(self):
        """Gets the enable of this SecureRemoteAccess.  # noqa: E501


        :return: The enable of this SecureRemoteAccess.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this SecureRemoteAccess.


        :param enable: The enable of this SecureRemoteAccess.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def endpoint(self):
        """Gets the endpoint of this SecureRemoteAccess.  # noqa: E501


        :return: The endpoint of this SecureRemoteAccess.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this SecureRemoteAccess.


        :param endpoint: The endpoint of this SecureRemoteAccess.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def enforce_hosts_restriction(self):
        """Gets the enforce_hosts_restriction of this SecureRemoteAccess.  # noqa: E501


        :return: The enforce_hosts_restriction of this SecureRemoteAccess.  # noqa: E501
        :rtype: bool
        """
        return self._enforce_hosts_restriction

    @enforce_hosts_restriction.setter
    def enforce_hosts_restriction(self, enforce_hosts_restriction):
        """Sets the enforce_hosts_restriction of this SecureRemoteAccess.


        :param enforce_hosts_restriction: The enforce_hosts_restriction of this SecureRemoteAccess.  # noqa: E501
        :type: bool
        """

        self._enforce_hosts_restriction = enforce_hosts_restriction

    @property
    def gw_cluster_id(self):
        """Gets the gw_cluster_id of this SecureRemoteAccess.  # noqa: E501


        :return: The gw_cluster_id of this SecureRemoteAccess.  # noqa: E501
        :rtype: int
        """
        return self._gw_cluster_id

    @gw_cluster_id.setter
    def gw_cluster_id(self, gw_cluster_id):
        """Sets the gw_cluster_id of this SecureRemoteAccess.


        :param gw_cluster_id: The gw_cluster_id of this SecureRemoteAccess.  # noqa: E501
        :type: int
        """

        self._gw_cluster_id = gw_cluster_id

    @property
    def host(self):
        """Gets the host of this SecureRemoteAccess.  # noqa: E501


        :return: The host of this SecureRemoteAccess.  # noqa: E501
        :rtype: list[str]
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this SecureRemoteAccess.


        :param host: The host of this SecureRemoteAccess.  # noqa: E501
        :type: list[str]
        """

        self._host = host

    @property
    def host_provider_type(self):
        """Gets the host_provider_type of this SecureRemoteAccess.  # noqa: E501


        :return: The host_provider_type of this SecureRemoteAccess.  # noqa: E501
        :rtype: str
        """
        return self._host_provider_type

    @host_provider_type.setter
    def host_provider_type(self, host_provider_type):
        """Sets the host_provider_type of this SecureRemoteAccess.


        :param host_provider_type: The host_provider_type of this SecureRemoteAccess.  # noqa: E501
        :type: str
        """

        self._host_provider_type = host_provider_type

    @property
    def is_cli(self):
        """Gets the is_cli of this SecureRemoteAccess.  # noqa: E501


        :return: The is_cli of this SecureRemoteAccess.  # noqa: E501
        :rtype: bool
        """
        return self._is_cli

    @is_cli.setter
    def is_cli(self, is_cli):
        """Sets the is_cli of this SecureRemoteAccess.


        :param is_cli: The is_cli of this SecureRemoteAccess.  # noqa: E501
        :type: bool
        """

        self._is_cli = is_cli

    @property
    def is_desktop_app(self):
        """Gets the is_desktop_app of this SecureRemoteAccess.  # noqa: E501


        :return: The is_desktop_app of this SecureRemoteAccess.  # noqa: E501
        :rtype: bool
        """
        return self._is_desktop_app

    @is_desktop_app.setter
    def is_desktop_app(self, is_desktop_app):
        """Sets the is_desktop_app of this SecureRemoteAccess.


        :param is_desktop_app: The is_desktop_app of this SecureRemoteAccess.  # noqa: E501
        :type: bool
        """

        self._is_desktop_app = is_desktop_app

    @property
    def is_web(self):
        """Gets the is_web of this SecureRemoteAccess.  # noqa: E501


        :return: The is_web of this SecureRemoteAccess.  # noqa: E501
        :rtype: bool
        """
        return self._is_web

    @is_web.setter
    def is_web(self, is_web):
        """Sets the is_web of this SecureRemoteAccess.


        :param is_web: The is_web of this SecureRemoteAccess.  # noqa: E501
        :type: bool
        """

        self._is_web = is_web

    @property
    def isolated(self):
        """Gets the isolated of this SecureRemoteAccess.  # noqa: E501


        :return: The isolated of this SecureRemoteAccess.  # noqa: E501
        :rtype: bool
        """
        return self._isolated

    @isolated.setter
    def isolated(self, isolated):
        """Sets the isolated of this SecureRemoteAccess.


        :param isolated: The isolated of this SecureRemoteAccess.  # noqa: E501
        :type: bool
        """

        self._isolated = isolated

    @property
    def native(self):
        """Gets the native of this SecureRemoteAccess.  # noqa: E501


        :return: The native of this SecureRemoteAccess.  # noqa: E501
        :rtype: bool
        """
        return self._native

    @native.setter
    def native(self, native):
        """Sets the native of this SecureRemoteAccess.


        :param native: The native of this SecureRemoteAccess.  # noqa: E501
        :type: bool
        """

        self._native = native

    @property
    def rd_gateway_server(self):
        """Gets the rd_gateway_server of this SecureRemoteAccess.  # noqa: E501


        :return: The rd_gateway_server of this SecureRemoteAccess.  # noqa: E501
        :rtype: str
        """
        return self._rd_gateway_server

    @rd_gateway_server.setter
    def rd_gateway_server(self, rd_gateway_server):
        """Sets the rd_gateway_server of this SecureRemoteAccess.


        :param rd_gateway_server: The rd_gateway_server of this SecureRemoteAccess.  # noqa: E501
        :type: str
        """

        self._rd_gateway_server = rd_gateway_server

    @property
    def rdp_user(self):
        """Gets the rdp_user of this SecureRemoteAccess.  # noqa: E501


        :return: The rdp_user of this SecureRemoteAccess.  # noqa: E501
        :rtype: str
        """
        return self._rdp_user

    @rdp_user.setter
    def rdp_user(self, rdp_user):
        """Sets the rdp_user of this SecureRemoteAccess.


        :param rdp_user: The rdp_user of this SecureRemoteAccess.  # noqa: E501
        :type: str
        """

        self._rdp_user = rdp_user

    @property
    def region(self):
        """Gets the region of this SecureRemoteAccess.  # noqa: E501


        :return: The region of this SecureRemoteAccess.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this SecureRemoteAccess.


        :param region: The region of this SecureRemoteAccess.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def rotate_after_disconnect(self):
        """Gets the rotate_after_disconnect of this SecureRemoteAccess.  # noqa: E501


        :return: The rotate_after_disconnect of this SecureRemoteAccess.  # noqa: E501
        :rtype: bool
        """
        return self._rotate_after_disconnect

    @rotate_after_disconnect.setter
    def rotate_after_disconnect(self, rotate_after_disconnect):
        """Sets the rotate_after_disconnect of this SecureRemoteAccess.


        :param rotate_after_disconnect: The rotate_after_disconnect of this SecureRemoteAccess.  # noqa: E501
        :type: bool
        """

        self._rotate_after_disconnect = rotate_after_disconnect

    @property
    def schema(self):
        """Gets the schema of this SecureRemoteAccess.  # noqa: E501


        :return: The schema of this SecureRemoteAccess.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this SecureRemoteAccess.


        :param schema: The schema of this SecureRemoteAccess.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def ssh_password(self):
        """Gets the ssh_password of this SecureRemoteAccess.  # noqa: E501


        :return: The ssh_password of this SecureRemoteAccess.  # noqa: E501
        :rtype: bool
        """
        return self._ssh_password

    @ssh_password.setter
    def ssh_password(self, ssh_password):
        """Sets the ssh_password of this SecureRemoteAccess.


        :param ssh_password: The ssh_password of this SecureRemoteAccess.  # noqa: E501
        :type: bool
        """

        self._ssh_password = ssh_password

    @property
    def ssh_private_key(self):
        """Gets the ssh_private_key of this SecureRemoteAccess.  # noqa: E501


        :return: The ssh_private_key of this SecureRemoteAccess.  # noqa: E501
        :rtype: bool
        """
        return self._ssh_private_key

    @ssh_private_key.setter
    def ssh_private_key(self, ssh_private_key):
        """Sets the ssh_private_key of this SecureRemoteAccess.


        :param ssh_private_key: The ssh_private_key of this SecureRemoteAccess.  # noqa: E501
        :type: bool
        """

        self._ssh_private_key = ssh_private_key

    @property
    def ssh_user(self):
        """Gets the ssh_user of this SecureRemoteAccess.  # noqa: E501


        :return: The ssh_user of this SecureRemoteAccess.  # noqa: E501
        :rtype: str
        """
        return self._ssh_user

    @ssh_user.setter
    def ssh_user(self, ssh_user):
        """Sets the ssh_user of this SecureRemoteAccess.


        :param ssh_user: The ssh_user of this SecureRemoteAccess.  # noqa: E501
        :type: str
        """

        self._ssh_user = ssh_user

    @property
    def status_info(self):
        """Gets the status_info of this SecureRemoteAccess.  # noqa: E501


        :return: The status_info of this SecureRemoteAccess.  # noqa: E501
        :rtype: ItemSraStatus
        """
        return self._status_info

    @status_info.setter
    def status_info(self, status_info):
        """Sets the status_info of this SecureRemoteAccess.


        :param status_info: The status_info of this SecureRemoteAccess.  # noqa: E501
        :type: ItemSraStatus
        """

        self._status_info = status_info

    @property
    def target_hosts(self):
        """Gets the target_hosts of this SecureRemoteAccess.  # noqa: E501


        :return: The target_hosts of this SecureRemoteAccess.  # noqa: E501
        :rtype: list[TargetNameWithHosts]
        """
        return self._target_hosts

    @target_hosts.setter
    def target_hosts(self, target_hosts):
        """Sets the target_hosts of this SecureRemoteAccess.


        :param target_hosts: The target_hosts of this SecureRemoteAccess.  # noqa: E501
        :type: list[TargetNameWithHosts]
        """

        self._target_hosts = target_hosts

    @property
    def targets(self):
        """Gets the targets of this SecureRemoteAccess.  # noqa: E501


        :return: The targets of this SecureRemoteAccess.  # noqa: E501
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this SecureRemoteAccess.


        :param targets: The targets of this SecureRemoteAccess.  # noqa: E501
        :type: list[str]
        """

        self._targets = targets

    @property
    def url(self):
        """Gets the url of this SecureRemoteAccess.  # noqa: E501


        :return: The url of this SecureRemoteAccess.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SecureRemoteAccess.


        :param url: The url of this SecureRemoteAccess.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def use_internal_bastion(self):
        """Gets the use_internal_bastion of this SecureRemoteAccess.  # noqa: E501


        :return: The use_internal_bastion of this SecureRemoteAccess.  # noqa: E501
        :rtype: bool
        """
        return self._use_internal_bastion

    @use_internal_bastion.setter
    def use_internal_bastion(self, use_internal_bastion):
        """Sets the use_internal_bastion of this SecureRemoteAccess.


        :param use_internal_bastion: The use_internal_bastion of this SecureRemoteAccess.  # noqa: E501
        :type: bool
        """

        self._use_internal_bastion = use_internal_bastion

    @property
    def web_proxy(self):
        """Gets the web_proxy of this SecureRemoteAccess.  # noqa: E501


        :return: The web_proxy of this SecureRemoteAccess.  # noqa: E501
        :rtype: bool
        """
        return self._web_proxy

    @web_proxy.setter
    def web_proxy(self, web_proxy):
        """Sets the web_proxy of this SecureRemoteAccess.


        :param web_proxy: The web_proxy of this SecureRemoteAccess.  # noqa: E501
        :type: bool
        """

        self._web_proxy = web_proxy

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
        if not isinstance(other, SecureRemoteAccess):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SecureRemoteAccess):
            return True

        return self.to_dict() != other.to_dict()
