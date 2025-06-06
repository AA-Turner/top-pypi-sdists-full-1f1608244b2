# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407

from .connection import Connection
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MongoDbConnection(Connection):
    """
    Represents the metadata of a MongoDB Connection.
    """

    #: A constant which can be used with the technology_type property of a MongoDbConnection.
    #: This constant has a value of "MONGODB"
    TECHNOLOGY_TYPE_MONGODB = "MONGODB"

    #: A constant which can be used with the technology_type property of a MongoDbConnection.
    #: This constant has a value of "OCI_AUTONOMOUS_JSON_DATABASE"
    TECHNOLOGY_TYPE_OCI_AUTONOMOUS_JSON_DATABASE = "OCI_AUTONOMOUS_JSON_DATABASE"

    #: A constant which can be used with the technology_type property of a MongoDbConnection.
    #: This constant has a value of "AZURE_COSMOS_DB_FOR_MONGODB"
    TECHNOLOGY_TYPE_AZURE_COSMOS_DB_FOR_MONGODB = "AZURE_COSMOS_DB_FOR_MONGODB"

    #: A constant which can be used with the technology_type property of a MongoDbConnection.
    #: This constant has a value of "AMAZON_DOCUMENT_DB"
    TECHNOLOGY_TYPE_AMAZON_DOCUMENT_DB = "AMAZON_DOCUMENT_DB"

    #: A constant which can be used with the technology_type property of a MongoDbConnection.
    #: This constant has a value of "ORACLE_JSON_COLLECTION"
    TECHNOLOGY_TYPE_ORACLE_JSON_COLLECTION = "ORACLE_JSON_COLLECTION"

    #: A constant which can be used with the technology_type property of a MongoDbConnection.
    #: This constant has a value of "ORACLE_REST_DATA_SERVICES"
    TECHNOLOGY_TYPE_ORACLE_REST_DATA_SERVICES = "ORACLE_REST_DATA_SERVICES"

    #: A constant which can be used with the security_protocol property of a MongoDbConnection.
    #: This constant has a value of "PLAIN"
    SECURITY_PROTOCOL_PLAIN = "PLAIN"

    #: A constant which can be used with the security_protocol property of a MongoDbConnection.
    #: This constant has a value of "TLS"
    SECURITY_PROTOCOL_TLS = "TLS"

    #: A constant which can be used with the security_protocol property of a MongoDbConnection.
    #: This constant has a value of "MTLS"
    SECURITY_PROTOCOL_MTLS = "MTLS"

    def __init__(self, **kwargs):
        """
        Initializes a new MongoDbConnection object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.MongoDbConnection.connection_type` attribute
        of this class is ``MONGODB`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this MongoDbConnection.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "DB2", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY", "DATABRICKS", "GOOGLE_PUBSUB", "MICROSOFT_FABRIC", "ICEBERG", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type connection_type: str

        :param id:
            The value to assign to the id property of this MongoDbConnection.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this MongoDbConnection.
        :type display_name: str

        :param description:
            The value to assign to the description property of this MongoDbConnection.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MongoDbConnection.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MongoDbConnection.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MongoDbConnection.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this MongoDbConnection.
        :type system_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MongoDbConnection.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this MongoDbConnection.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this MongoDbConnection.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MongoDbConnection.
        :type time_updated: datetime

        :param locks:
            The value to assign to the locks property of this MongoDbConnection.
        :type locks: list[oci.golden_gate.models.ResourceLock]

        :param vault_id:
            The value to assign to the vault_id property of this MongoDbConnection.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this MongoDbConnection.
        :type key_id: str

        :param ingress_ips:
            The value to assign to the ingress_ips property of this MongoDbConnection.
        :type ingress_ips: list[oci.golden_gate.models.IngressIpDetails]

        :param nsg_ids:
            The value to assign to the nsg_ids property of this MongoDbConnection.
        :type nsg_ids: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this MongoDbConnection.
        :type subnet_id: str

        :param routing_method:
            The value to assign to the routing_method property of this MongoDbConnection.
            Allowed values for this property are: "SHARED_SERVICE_ENDPOINT", "SHARED_DEPLOYMENT_ENDPOINT", "DEDICATED_ENDPOINT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type routing_method: str

        :param does_use_secret_ids:
            The value to assign to the does_use_secret_ids property of this MongoDbConnection.
        :type does_use_secret_ids: bool

        :param technology_type:
            The value to assign to the technology_type property of this MongoDbConnection.
            Allowed values for this property are: "MONGODB", "OCI_AUTONOMOUS_JSON_DATABASE", "AZURE_COSMOS_DB_FOR_MONGODB", "AMAZON_DOCUMENT_DB", "ORACLE_JSON_COLLECTION", "ORACLE_REST_DATA_SERVICES", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type technology_type: str

        :param connection_string:
            The value to assign to the connection_string property of this MongoDbConnection.
        :type connection_string: str

        :param username:
            The value to assign to the username property of this MongoDbConnection.
        :type username: str

        :param database_id:
            The value to assign to the database_id property of this MongoDbConnection.
        :type database_id: str

        :param security_protocol:
            The value to assign to the security_protocol property of this MongoDbConnection.
            Allowed values for this property are: "PLAIN", "TLS", "MTLS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type security_protocol: str

        :param password_secret_id:
            The value to assign to the password_secret_id property of this MongoDbConnection.
        :type password_secret_id: str

        :param tls_certificate_key_file_secret_id:
            The value to assign to the tls_certificate_key_file_secret_id property of this MongoDbConnection.
        :type tls_certificate_key_file_secret_id: str

        :param tls_certificate_key_file_password_secret_id:
            The value to assign to the tls_certificate_key_file_password_secret_id property of this MongoDbConnection.
        :type tls_certificate_key_file_password_secret_id: str

        :param tls_ca_file:
            The value to assign to the tls_ca_file property of this MongoDbConnection.
        :type tls_ca_file: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'locks': 'list[ResourceLock]',
            'vault_id': 'str',
            'key_id': 'str',
            'ingress_ips': 'list[IngressIpDetails]',
            'nsg_ids': 'list[str]',
            'subnet_id': 'str',
            'routing_method': 'str',
            'does_use_secret_ids': 'bool',
            'technology_type': 'str',
            'connection_string': 'str',
            'username': 'str',
            'database_id': 'str',
            'security_protocol': 'str',
            'password_secret_id': 'str',
            'tls_certificate_key_file_secret_id': 'str',
            'tls_certificate_key_file_password_secret_id': 'str',
            'tls_ca_file': 'str'
        }
        self.attribute_map = {
            'connection_type': 'connectionType',
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'locks': 'locks',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'ingress_ips': 'ingressIps',
            'nsg_ids': 'nsgIds',
            'subnet_id': 'subnetId',
            'routing_method': 'routingMethod',
            'does_use_secret_ids': 'doesUseSecretIds',
            'technology_type': 'technologyType',
            'connection_string': 'connectionString',
            'username': 'username',
            'database_id': 'databaseId',
            'security_protocol': 'securityProtocol',
            'password_secret_id': 'passwordSecretId',
            'tls_certificate_key_file_secret_id': 'tlsCertificateKeyFileSecretId',
            'tls_certificate_key_file_password_secret_id': 'tlsCertificateKeyFilePasswordSecretId',
            'tls_ca_file': 'tlsCaFile'
        }
        self._connection_type = None
        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._locks = None
        self._vault_id = None
        self._key_id = None
        self._ingress_ips = None
        self._nsg_ids = None
        self._subnet_id = None
        self._routing_method = None
        self._does_use_secret_ids = None
        self._technology_type = None
        self._connection_string = None
        self._username = None
        self._database_id = None
        self._security_protocol = None
        self._password_secret_id = None
        self._tls_certificate_key_file_secret_id = None
        self._tls_certificate_key_file_password_secret_id = None
        self._tls_ca_file = None
        self._connection_type = 'MONGODB'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this MongoDbConnection.
        The MongoDB technology type.

        Allowed values for this property are: "MONGODB", "OCI_AUTONOMOUS_JSON_DATABASE", "AZURE_COSMOS_DB_FOR_MONGODB", "AMAZON_DOCUMENT_DB", "ORACLE_JSON_COLLECTION", "ORACLE_REST_DATA_SERVICES", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The technology_type of this MongoDbConnection.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this MongoDbConnection.
        The MongoDB technology type.


        :param technology_type: The technology_type of this MongoDbConnection.
        :type: str
        """
        allowed_values = ["MONGODB", "OCI_AUTONOMOUS_JSON_DATABASE", "AZURE_COSMOS_DB_FOR_MONGODB", "AMAZON_DOCUMENT_DB", "ORACLE_JSON_COLLECTION", "ORACLE_REST_DATA_SERVICES"]
        if not value_allowed_none_or_none_sentinel(technology_type, allowed_values):
            technology_type = 'UNKNOWN_ENUM_VALUE'
        self._technology_type = technology_type

    @property
    def connection_string(self):
        """
        Gets the connection_string of this MongoDbConnection.
        MongoDB connection string.
        e.g.: 'mongodb://mongodb0.example.com:27017/recordsrecords'


        :return: The connection_string of this MongoDbConnection.
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """
        Sets the connection_string of this MongoDbConnection.
        MongoDB connection string.
        e.g.: 'mongodb://mongodb0.example.com:27017/recordsrecords'


        :param connection_string: The connection_string of this MongoDbConnection.
        :type: str
        """
        self._connection_string = connection_string

    @property
    def username(self):
        """
        Gets the username of this MongoDbConnection.
        The username Oracle GoldenGate uses to connect to the database.
        This username must already exist and be available by the database to be connected to.


        :return: The username of this MongoDbConnection.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this MongoDbConnection.
        The username Oracle GoldenGate uses to connect to the database.
        This username must already exist and be available by the database to be connected to.


        :param username: The username of this MongoDbConnection.
        :type: str
        """
        self._username = username

    @property
    def database_id(self):
        """
        Gets the database_id of this MongoDbConnection.
        The `OCID`__ of the Oracle Autonomous Json Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The database_id of this MongoDbConnection.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this MongoDbConnection.
        The `OCID`__ of the Oracle Autonomous Json Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param database_id: The database_id of this MongoDbConnection.
        :type: str
        """
        self._database_id = database_id

    @property
    def security_protocol(self):
        """
        Gets the security_protocol of this MongoDbConnection.
        Security Protocol for MongoDB.

        Allowed values for this property are: "PLAIN", "TLS", "MTLS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The security_protocol of this MongoDbConnection.
        :rtype: str
        """
        return self._security_protocol

    @security_protocol.setter
    def security_protocol(self, security_protocol):
        """
        Sets the security_protocol of this MongoDbConnection.
        Security Protocol for MongoDB.


        :param security_protocol: The security_protocol of this MongoDbConnection.
        :type: str
        """
        allowed_values = ["PLAIN", "TLS", "MTLS"]
        if not value_allowed_none_or_none_sentinel(security_protocol, allowed_values):
            security_protocol = 'UNKNOWN_ENUM_VALUE'
        self._security_protocol = security_protocol

    @property
    def password_secret_id(self):
        """
        Gets the password_secret_id of this MongoDbConnection.
        The `OCID`__ of the Secret that stores the password Oracle GoldenGate uses to connect the associated database.
        Note: When provided, 'password' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The password_secret_id of this MongoDbConnection.
        :rtype: str
        """
        return self._password_secret_id

    @password_secret_id.setter
    def password_secret_id(self, password_secret_id):
        """
        Sets the password_secret_id of this MongoDbConnection.
        The `OCID`__ of the Secret that stores the password Oracle GoldenGate uses to connect the associated database.
        Note: When provided, 'password' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param password_secret_id: The password_secret_id of this MongoDbConnection.
        :type: str
        """
        self._password_secret_id = password_secret_id

    @property
    def tls_certificate_key_file_secret_id(self):
        """
        Gets the tls_certificate_key_file_secret_id of this MongoDbConnection.
        The `OCID`__ of the Secret that stores the certificate key file of the mtls connection.
        - The content of a .pem file containing the client private key (for 2-way SSL).
        Note: When provided, 'tlsCertificateKeyFile' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The tls_certificate_key_file_secret_id of this MongoDbConnection.
        :rtype: str
        """
        return self._tls_certificate_key_file_secret_id

    @tls_certificate_key_file_secret_id.setter
    def tls_certificate_key_file_secret_id(self, tls_certificate_key_file_secret_id):
        """
        Sets the tls_certificate_key_file_secret_id of this MongoDbConnection.
        The `OCID`__ of the Secret that stores the certificate key file of the mtls connection.
        - The content of a .pem file containing the client private key (for 2-way SSL).
        Note: When provided, 'tlsCertificateKeyFile' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param tls_certificate_key_file_secret_id: The tls_certificate_key_file_secret_id of this MongoDbConnection.
        :type: str
        """
        self._tls_certificate_key_file_secret_id = tls_certificate_key_file_secret_id

    @property
    def tls_certificate_key_file_password_secret_id(self):
        """
        Gets the tls_certificate_key_file_password_secret_id of this MongoDbConnection.
        The `OCID`__ of the Secret that stores the password of the tls certificate key file.
        Note: When provided, 'tlsCertificateKeyFilePassword' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The tls_certificate_key_file_password_secret_id of this MongoDbConnection.
        :rtype: str
        """
        return self._tls_certificate_key_file_password_secret_id

    @tls_certificate_key_file_password_secret_id.setter
    def tls_certificate_key_file_password_secret_id(self, tls_certificate_key_file_password_secret_id):
        """
        Sets the tls_certificate_key_file_password_secret_id of this MongoDbConnection.
        The `OCID`__ of the Secret that stores the password of the tls certificate key file.
        Note: When provided, 'tlsCertificateKeyFilePassword' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param tls_certificate_key_file_password_secret_id: The tls_certificate_key_file_password_secret_id of this MongoDbConnection.
        :type: str
        """
        self._tls_certificate_key_file_password_secret_id = tls_certificate_key_file_password_secret_id

    @property
    def tls_ca_file(self):
        """
        Gets the tls_ca_file of this MongoDbConnection.
        Database Certificate - The base64 encoded content of a .pem file, containing the server public key (for 1 and 2-way SSL).
        It is not included in GET responses if the `view=COMPACT` query parameter is specified.


        :return: The tls_ca_file of this MongoDbConnection.
        :rtype: str
        """
        return self._tls_ca_file

    @tls_ca_file.setter
    def tls_ca_file(self, tls_ca_file):
        """
        Sets the tls_ca_file of this MongoDbConnection.
        Database Certificate - The base64 encoded content of a .pem file, containing the server public key (for 1 and 2-way SSL).
        It is not included in GET responses if the `view=COMPACT` query parameter is specified.


        :param tls_ca_file: The tls_ca_file of this MongoDbConnection.
        :type: str
        """
        self._tls_ca_file = tls_ca_file

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
