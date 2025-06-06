# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407

from .update_connection_details import UpdateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMicrosoftSqlserverConnectionDetails(UpdateConnectionDetails):
    """
    The information to update a Microsoft SQL Server Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMicrosoftSqlserverConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.UpdateMicrosoftSqlserverConnectionDetails.connection_type` attribute
        of this class is ``MICROSOFT_SQLSERVER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this UpdateMicrosoftSqlserverConnectionDetails.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "DB2", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY", "DATABRICKS", "GOOGLE_PUBSUB", "MICROSOFT_FABRIC", "ICEBERG"
        :type connection_type: str

        :param display_name:
            The value to assign to the display_name property of this UpdateMicrosoftSqlserverConnectionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateMicrosoftSqlserverConnectionDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateMicrosoftSqlserverConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateMicrosoftSqlserverConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param vault_id:
            The value to assign to the vault_id property of this UpdateMicrosoftSqlserverConnectionDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this UpdateMicrosoftSqlserverConnectionDetails.
        :type key_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateMicrosoftSqlserverConnectionDetails.
        :type nsg_ids: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this UpdateMicrosoftSqlserverConnectionDetails.
        :type subnet_id: str

        :param routing_method:
            The value to assign to the routing_method property of this UpdateMicrosoftSqlserverConnectionDetails.
            Allowed values for this property are: "SHARED_SERVICE_ENDPOINT", "SHARED_DEPLOYMENT_ENDPOINT", "DEDICATED_ENDPOINT"
        :type routing_method: str

        :param does_use_secret_ids:
            The value to assign to the does_use_secret_ids property of this UpdateMicrosoftSqlserverConnectionDetails.
        :type does_use_secret_ids: bool

        :param database_name:
            The value to assign to the database_name property of this UpdateMicrosoftSqlserverConnectionDetails.
        :type database_name: str

        :param host:
            The value to assign to the host property of this UpdateMicrosoftSqlserverConnectionDetails.
        :type host: str

        :param port:
            The value to assign to the port property of this UpdateMicrosoftSqlserverConnectionDetails.
        :type port: int

        :param username:
            The value to assign to the username property of this UpdateMicrosoftSqlserverConnectionDetails.
        :type username: str

        :param password:
            The value to assign to the password property of this UpdateMicrosoftSqlserverConnectionDetails.
        :type password: str

        :param password_secret_id:
            The value to assign to the password_secret_id property of this UpdateMicrosoftSqlserverConnectionDetails.
        :type password_secret_id: str

        :param additional_attributes:
            The value to assign to the additional_attributes property of this UpdateMicrosoftSqlserverConnectionDetails.
        :type additional_attributes: list[oci.golden_gate.models.NameValuePair]

        :param security_protocol:
            The value to assign to the security_protocol property of this UpdateMicrosoftSqlserverConnectionDetails.
        :type security_protocol: str

        :param ssl_ca:
            The value to assign to the ssl_ca property of this UpdateMicrosoftSqlserverConnectionDetails.
        :type ssl_ca: str

        :param should_validate_server_certificate:
            The value to assign to the should_validate_server_certificate property of this UpdateMicrosoftSqlserverConnectionDetails.
        :type should_validate_server_certificate: bool

        :param private_ip:
            The value to assign to the private_ip property of this UpdateMicrosoftSqlserverConnectionDetails.
        :type private_ip: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'vault_id': 'str',
            'key_id': 'str',
            'nsg_ids': 'list[str]',
            'subnet_id': 'str',
            'routing_method': 'str',
            'does_use_secret_ids': 'bool',
            'database_name': 'str',
            'host': 'str',
            'port': 'int',
            'username': 'str',
            'password': 'str',
            'password_secret_id': 'str',
            'additional_attributes': 'list[NameValuePair]',
            'security_protocol': 'str',
            'ssl_ca': 'str',
            'should_validate_server_certificate': 'bool',
            'private_ip': 'str'
        }
        self.attribute_map = {
            'connection_type': 'connectionType',
            'display_name': 'displayName',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'nsg_ids': 'nsgIds',
            'subnet_id': 'subnetId',
            'routing_method': 'routingMethod',
            'does_use_secret_ids': 'doesUseSecretIds',
            'database_name': 'databaseName',
            'host': 'host',
            'port': 'port',
            'username': 'username',
            'password': 'password',
            'password_secret_id': 'passwordSecretId',
            'additional_attributes': 'additionalAttributes',
            'security_protocol': 'securityProtocol',
            'ssl_ca': 'sslCa',
            'should_validate_server_certificate': 'shouldValidateServerCertificate',
            'private_ip': 'privateIp'
        }
        self._connection_type = None
        self._display_name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._vault_id = None
        self._key_id = None
        self._nsg_ids = None
        self._subnet_id = None
        self._routing_method = None
        self._does_use_secret_ids = None
        self._database_name = None
        self._host = None
        self._port = None
        self._username = None
        self._password = None
        self._password_secret_id = None
        self._additional_attributes = None
        self._security_protocol = None
        self._ssl_ca = None
        self._should_validate_server_certificate = None
        self._private_ip = None
        self._connection_type = 'MICROSOFT_SQLSERVER'

    @property
    def database_name(self):
        """
        Gets the database_name of this UpdateMicrosoftSqlserverConnectionDetails.
        The name of the database.


        :return: The database_name of this UpdateMicrosoftSqlserverConnectionDetails.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """
        Sets the database_name of this UpdateMicrosoftSqlserverConnectionDetails.
        The name of the database.


        :param database_name: The database_name of this UpdateMicrosoftSqlserverConnectionDetails.
        :type: str
        """
        self._database_name = database_name

    @property
    def host(self):
        """
        Gets the host of this UpdateMicrosoftSqlserverConnectionDetails.
        The name or address of a host.


        :return: The host of this UpdateMicrosoftSqlserverConnectionDetails.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this UpdateMicrosoftSqlserverConnectionDetails.
        The name or address of a host.


        :param host: The host of this UpdateMicrosoftSqlserverConnectionDetails.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """
        Gets the port of this UpdateMicrosoftSqlserverConnectionDetails.
        The port of an endpoint usually specified for a connection.


        :return: The port of this UpdateMicrosoftSqlserverConnectionDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this UpdateMicrosoftSqlserverConnectionDetails.
        The port of an endpoint usually specified for a connection.


        :param port: The port of this UpdateMicrosoftSqlserverConnectionDetails.
        :type: int
        """
        self._port = port

    @property
    def username(self):
        """
        Gets the username of this UpdateMicrosoftSqlserverConnectionDetails.
        The username Oracle GoldenGate uses to connect to the Microsoft SQL Server.
        This username must already exist and be available by the Microsoft SQL Server to be connected to.


        :return: The username of this UpdateMicrosoftSqlserverConnectionDetails.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this UpdateMicrosoftSqlserverConnectionDetails.
        The username Oracle GoldenGate uses to connect to the Microsoft SQL Server.
        This username must already exist and be available by the Microsoft SQL Server to be connected to.


        :param username: The username of this UpdateMicrosoftSqlserverConnectionDetails.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """
        Gets the password of this UpdateMicrosoftSqlserverConnectionDetails.
        The password Oracle GoldenGate uses to connect the associated Microsoft SQL Server.
        Deprecated: This field is deprecated and replaced by \"passwordSecretId\". This field will be removed after February 15 2026.


        :return: The password of this UpdateMicrosoftSqlserverConnectionDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UpdateMicrosoftSqlserverConnectionDetails.
        The password Oracle GoldenGate uses to connect the associated Microsoft SQL Server.
        Deprecated: This field is deprecated and replaced by \"passwordSecretId\". This field will be removed after February 15 2026.


        :param password: The password of this UpdateMicrosoftSqlserverConnectionDetails.
        :type: str
        """
        self._password = password

    @property
    def password_secret_id(self):
        """
        Gets the password_secret_id of this UpdateMicrosoftSqlserverConnectionDetails.
        The `OCID`__ of the Secret that stores the password Oracle GoldenGate uses to connect the associated Microsoft SQL Server.
        Note: When provided, 'password' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The password_secret_id of this UpdateMicrosoftSqlserverConnectionDetails.
        :rtype: str
        """
        return self._password_secret_id

    @password_secret_id.setter
    def password_secret_id(self, password_secret_id):
        """
        Sets the password_secret_id of this UpdateMicrosoftSqlserverConnectionDetails.
        The `OCID`__ of the Secret that stores the password Oracle GoldenGate uses to connect the associated Microsoft SQL Server.
        Note: When provided, 'password' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param password_secret_id: The password_secret_id of this UpdateMicrosoftSqlserverConnectionDetails.
        :type: str
        """
        self._password_secret_id = password_secret_id

    @property
    def additional_attributes(self):
        """
        Gets the additional_attributes of this UpdateMicrosoftSqlserverConnectionDetails.
        An array of name-value pair attribute entries.
        Used as additional parameters in connection string.


        :return: The additional_attributes of this UpdateMicrosoftSqlserverConnectionDetails.
        :rtype: list[oci.golden_gate.models.NameValuePair]
        """
        return self._additional_attributes

    @additional_attributes.setter
    def additional_attributes(self, additional_attributes):
        """
        Sets the additional_attributes of this UpdateMicrosoftSqlserverConnectionDetails.
        An array of name-value pair attribute entries.
        Used as additional parameters in connection string.


        :param additional_attributes: The additional_attributes of this UpdateMicrosoftSqlserverConnectionDetails.
        :type: list[oci.golden_gate.models.NameValuePair]
        """
        self._additional_attributes = additional_attributes

    @property
    def security_protocol(self):
        """
        Gets the security_protocol of this UpdateMicrosoftSqlserverConnectionDetails.
        Security Type for Microsoft SQL Server.


        :return: The security_protocol of this UpdateMicrosoftSqlserverConnectionDetails.
        :rtype: str
        """
        return self._security_protocol

    @security_protocol.setter
    def security_protocol(self, security_protocol):
        """
        Sets the security_protocol of this UpdateMicrosoftSqlserverConnectionDetails.
        Security Type for Microsoft SQL Server.


        :param security_protocol: The security_protocol of this UpdateMicrosoftSqlserverConnectionDetails.
        :type: str
        """
        self._security_protocol = security_protocol

    @property
    def ssl_ca(self):
        """
        Gets the ssl_ca of this UpdateMicrosoftSqlserverConnectionDetails.
        Database Certificate - The base64 encoded content of a .pem or .crt file
        containing the server public key (for 1-way SSL).


        :return: The ssl_ca of this UpdateMicrosoftSqlserverConnectionDetails.
        :rtype: str
        """
        return self._ssl_ca

    @ssl_ca.setter
    def ssl_ca(self, ssl_ca):
        """
        Sets the ssl_ca of this UpdateMicrosoftSqlserverConnectionDetails.
        Database Certificate - The base64 encoded content of a .pem or .crt file
        containing the server public key (for 1-way SSL).


        :param ssl_ca: The ssl_ca of this UpdateMicrosoftSqlserverConnectionDetails.
        :type: str
        """
        self._ssl_ca = ssl_ca

    @property
    def should_validate_server_certificate(self):
        """
        Gets the should_validate_server_certificate of this UpdateMicrosoftSqlserverConnectionDetails.
        If set to true, the driver validates the certificate that is sent by the database server.


        :return: The should_validate_server_certificate of this UpdateMicrosoftSqlserverConnectionDetails.
        :rtype: bool
        """
        return self._should_validate_server_certificate

    @should_validate_server_certificate.setter
    def should_validate_server_certificate(self, should_validate_server_certificate):
        """
        Sets the should_validate_server_certificate of this UpdateMicrosoftSqlserverConnectionDetails.
        If set to true, the driver validates the certificate that is sent by the database server.


        :param should_validate_server_certificate: The should_validate_server_certificate of this UpdateMicrosoftSqlserverConnectionDetails.
        :type: bool
        """
        self._should_validate_server_certificate = should_validate_server_certificate

    @property
    def private_ip(self):
        """
        Gets the private_ip of this UpdateMicrosoftSqlserverConnectionDetails.
        Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host
        field, or make sure the host name is resolvable in the target VCN.

        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :return: The private_ip of this UpdateMicrosoftSqlserverConnectionDetails.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """
        Sets the private_ip of this UpdateMicrosoftSqlserverConnectionDetails.
        Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host
        field, or make sure the host name is resolvable in the target VCN.

        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :param private_ip: The private_ip of this UpdateMicrosoftSqlserverConnectionDetails.
        :type: str
        """
        self._private_ip = private_ip

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
