# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConnectionSummary(object):
    """
    Summary of the Connection.
    """

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "GOLDENGATE"
    CONNECTION_TYPE_GOLDENGATE = "GOLDENGATE"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "KAFKA"
    CONNECTION_TYPE_KAFKA = "KAFKA"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "KAFKA_SCHEMA_REGISTRY"
    CONNECTION_TYPE_KAFKA_SCHEMA_REGISTRY = "KAFKA_SCHEMA_REGISTRY"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "MYSQL"
    CONNECTION_TYPE_MYSQL = "MYSQL"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "JAVA_MESSAGE_SERVICE"
    CONNECTION_TYPE_JAVA_MESSAGE_SERVICE = "JAVA_MESSAGE_SERVICE"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "MICROSOFT_SQLSERVER"
    CONNECTION_TYPE_MICROSOFT_SQLSERVER = "MICROSOFT_SQLSERVER"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "OCI_OBJECT_STORAGE"
    CONNECTION_TYPE_OCI_OBJECT_STORAGE = "OCI_OBJECT_STORAGE"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "ORACLE"
    CONNECTION_TYPE_ORACLE = "ORACLE"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "AZURE_DATA_LAKE_STORAGE"
    CONNECTION_TYPE_AZURE_DATA_LAKE_STORAGE = "AZURE_DATA_LAKE_STORAGE"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "POSTGRESQL"
    CONNECTION_TYPE_POSTGRESQL = "POSTGRESQL"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "AZURE_SYNAPSE_ANALYTICS"
    CONNECTION_TYPE_AZURE_SYNAPSE_ANALYTICS = "AZURE_SYNAPSE_ANALYTICS"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "SNOWFLAKE"
    CONNECTION_TYPE_SNOWFLAKE = "SNOWFLAKE"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "AMAZON_S3"
    CONNECTION_TYPE_AMAZON_S3 = "AMAZON_S3"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "HDFS"
    CONNECTION_TYPE_HDFS = "HDFS"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "ORACLE_NOSQL"
    CONNECTION_TYPE_ORACLE_NOSQL = "ORACLE_NOSQL"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "MONGODB"
    CONNECTION_TYPE_MONGODB = "MONGODB"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "AMAZON_KINESIS"
    CONNECTION_TYPE_AMAZON_KINESIS = "AMAZON_KINESIS"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "AMAZON_REDSHIFT"
    CONNECTION_TYPE_AMAZON_REDSHIFT = "AMAZON_REDSHIFT"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "DB2"
    CONNECTION_TYPE_DB2 = "DB2"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "REDIS"
    CONNECTION_TYPE_REDIS = "REDIS"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "ELASTICSEARCH"
    CONNECTION_TYPE_ELASTICSEARCH = "ELASTICSEARCH"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "GENERIC"
    CONNECTION_TYPE_GENERIC = "GENERIC"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "GOOGLE_CLOUD_STORAGE"
    CONNECTION_TYPE_GOOGLE_CLOUD_STORAGE = "GOOGLE_CLOUD_STORAGE"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "GOOGLE_BIGQUERY"
    CONNECTION_TYPE_GOOGLE_BIGQUERY = "GOOGLE_BIGQUERY"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "DATABRICKS"
    CONNECTION_TYPE_DATABRICKS = "DATABRICKS"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "GOOGLE_PUBSUB"
    CONNECTION_TYPE_GOOGLE_PUBSUB = "GOOGLE_PUBSUB"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "MICROSOFT_FABRIC"
    CONNECTION_TYPE_MICROSOFT_FABRIC = "MICROSOFT_FABRIC"

    #: A constant which can be used with the connection_type property of a ConnectionSummary.
    #: This constant has a value of "ICEBERG"
    CONNECTION_TYPE_ICEBERG = "ICEBERG"

    #: A constant which can be used with the routing_method property of a ConnectionSummary.
    #: This constant has a value of "SHARED_SERVICE_ENDPOINT"
    ROUTING_METHOD_SHARED_SERVICE_ENDPOINT = "SHARED_SERVICE_ENDPOINT"

    #: A constant which can be used with the routing_method property of a ConnectionSummary.
    #: This constant has a value of "SHARED_DEPLOYMENT_ENDPOINT"
    ROUTING_METHOD_SHARED_DEPLOYMENT_ENDPOINT = "SHARED_DEPLOYMENT_ENDPOINT"

    #: A constant which can be used with the routing_method property of a ConnectionSummary.
    #: This constant has a value of "DEDICATED_ENDPOINT"
    ROUTING_METHOD_DEDICATED_ENDPOINT = "DEDICATED_ENDPOINT"

    def __init__(self, **kwargs):
        """
        Initializes a new ConnectionSummary object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.golden_gate.models.MicrosoftFabricConnectionSummary`
        * :class:`~oci.golden_gate.models.KafkaSchemaRegistryConnectionSummary`
        * :class:`~oci.golden_gate.models.MicrosoftSqlserverConnectionSummary`
        * :class:`~oci.golden_gate.models.OracleNosqlConnectionSummary`
        * :class:`~oci.golden_gate.models.OracleConnectionSummary`
        * :class:`~oci.golden_gate.models.OciObjectStorageConnectionSummary`
        * :class:`~oci.golden_gate.models.AzureSynapseConnectionSummary`
        * :class:`~oci.golden_gate.models.MongoDbConnectionSummary`
        * :class:`~oci.golden_gate.models.AmazonS3ConnectionSummary`
        * :class:`~oci.golden_gate.models.MysqlConnectionSummary`
        * :class:`~oci.golden_gate.models.ElasticsearchConnectionSummary`
        * :class:`~oci.golden_gate.models.GooglePubSubConnectionSummary`
        * :class:`~oci.golden_gate.models.GoogleCloudStorageConnectionSummary`
        * :class:`~oci.golden_gate.models.GoldenGateConnectionSummary`
        * :class:`~oci.golden_gate.models.JavaMessageServiceConnectionSummary`
        * :class:`~oci.golden_gate.models.SnowflakeConnectionSummary`
        * :class:`~oci.golden_gate.models.AmazonKinesisConnectionSummary`
        * :class:`~oci.golden_gate.models.RedisConnectionSummary`
        * :class:`~oci.golden_gate.models.AzureDataLakeStorageConnectionSummary`
        * :class:`~oci.golden_gate.models.GoogleBigQueryConnectionSummary`
        * :class:`~oci.golden_gate.models.IcebergConnectionSummary`
        * :class:`~oci.golden_gate.models.PostgresqlConnectionSummary`
        * :class:`~oci.golden_gate.models.GenericConnectionSummary`
        * :class:`~oci.golden_gate.models.KafkaConnectionSummary`
        * :class:`~oci.golden_gate.models.Db2ConnectionSummary`
        * :class:`~oci.golden_gate.models.AmazonRedshiftConnectionSummary`
        * :class:`~oci.golden_gate.models.DatabricksConnectionSummary`
        * :class:`~oci.golden_gate.models.HdfsConnectionSummary`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this ConnectionSummary.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "DB2", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY", "DATABRICKS", "GOOGLE_PUBSUB", "MICROSOFT_FABRIC", "ICEBERG", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type connection_type: str

        :param id:
            The value to assign to the id property of this ConnectionSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ConnectionSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ConnectionSummary.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ConnectionSummary.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ConnectionSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ConnectionSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ConnectionSummary.
        :type system_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ConnectionSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ConnectionSummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this ConnectionSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ConnectionSummary.
        :type time_updated: datetime

        :param vault_id:
            The value to assign to the vault_id property of this ConnectionSummary.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this ConnectionSummary.
        :type key_id: str

        :param ingress_ips:
            The value to assign to the ingress_ips property of this ConnectionSummary.
        :type ingress_ips: list[oci.golden_gate.models.IngressIpDetails]

        :param nsg_ids:
            The value to assign to the nsg_ids property of this ConnectionSummary.
        :type nsg_ids: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this ConnectionSummary.
        :type subnet_id: str

        :param routing_method:
            The value to assign to the routing_method property of this ConnectionSummary.
            Allowed values for this property are: "SHARED_SERVICE_ENDPOINT", "SHARED_DEPLOYMENT_ENDPOINT", "DEDICATED_ENDPOINT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type routing_method: str

        :param locks:
            The value to assign to the locks property of this ConnectionSummary.
        :type locks: list[oci.golden_gate.models.ResourceLock]

        :param does_use_secret_ids:
            The value to assign to the does_use_secret_ids property of this ConnectionSummary.
        :type does_use_secret_ids: bool

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
            'vault_id': 'str',
            'key_id': 'str',
            'ingress_ips': 'list[IngressIpDetails]',
            'nsg_ids': 'list[str]',
            'subnet_id': 'str',
            'routing_method': 'str',
            'locks': 'list[ResourceLock]',
            'does_use_secret_ids': 'bool'
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
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'ingress_ips': 'ingressIps',
            'nsg_ids': 'nsgIds',
            'subnet_id': 'subnetId',
            'routing_method': 'routingMethod',
            'locks': 'locks',
            'does_use_secret_ids': 'doesUseSecretIds'
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
        self._vault_id = None
        self._key_id = None
        self._ingress_ips = None
        self._nsg_ids = None
        self._subnet_id = None
        self._routing_method = None
        self._locks = None
        self._does_use_secret_ids = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['connectionType']

        if type == 'MICROSOFT_FABRIC':
            return 'MicrosoftFabricConnectionSummary'

        if type == 'KAFKA_SCHEMA_REGISTRY':
            return 'KafkaSchemaRegistryConnectionSummary'

        if type == 'MICROSOFT_SQLSERVER':
            return 'MicrosoftSqlserverConnectionSummary'

        if type == 'ORACLE_NOSQL':
            return 'OracleNosqlConnectionSummary'

        if type == 'ORACLE':
            return 'OracleConnectionSummary'

        if type == 'OCI_OBJECT_STORAGE':
            return 'OciObjectStorageConnectionSummary'

        if type == 'AZURE_SYNAPSE_ANALYTICS':
            return 'AzureSynapseConnectionSummary'

        if type == 'MONGODB':
            return 'MongoDbConnectionSummary'

        if type == 'AMAZON_S3':
            return 'AmazonS3ConnectionSummary'

        if type == 'MYSQL':
            return 'MysqlConnectionSummary'

        if type == 'ELASTICSEARCH':
            return 'ElasticsearchConnectionSummary'

        if type == 'GOOGLE_PUBSUB':
            return 'GooglePubSubConnectionSummary'

        if type == 'GOOGLE_CLOUD_STORAGE':
            return 'GoogleCloudStorageConnectionSummary'

        if type == 'GOLDENGATE':
            return 'GoldenGateConnectionSummary'

        if type == 'JAVA_MESSAGE_SERVICE':
            return 'JavaMessageServiceConnectionSummary'

        if type == 'SNOWFLAKE':
            return 'SnowflakeConnectionSummary'

        if type == 'AMAZON_KINESIS':
            return 'AmazonKinesisConnectionSummary'

        if type == 'REDIS':
            return 'RedisConnectionSummary'

        if type == 'AZURE_DATA_LAKE_STORAGE':
            return 'AzureDataLakeStorageConnectionSummary'

        if type == 'GOOGLE_BIGQUERY':
            return 'GoogleBigQueryConnectionSummary'

        if type == 'ICEBERG':
            return 'IcebergConnectionSummary'

        if type == 'POSTGRESQL':
            return 'PostgresqlConnectionSummary'

        if type == 'GENERIC':
            return 'GenericConnectionSummary'

        if type == 'KAFKA':
            return 'KafkaConnectionSummary'

        if type == 'DB2':
            return 'Db2ConnectionSummary'

        if type == 'AMAZON_REDSHIFT':
            return 'AmazonRedshiftConnectionSummary'

        if type == 'DATABRICKS':
            return 'DatabricksConnectionSummary'

        if type == 'HDFS':
            return 'HdfsConnectionSummary'
        else:
            return 'ConnectionSummary'

    @property
    def connection_type(self):
        """
        **[Required]** Gets the connection_type of this ConnectionSummary.
        The connection type.

        Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "DB2", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY", "DATABRICKS", "GOOGLE_PUBSUB", "MICROSOFT_FABRIC", "ICEBERG", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The connection_type of this ConnectionSummary.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """
        Sets the connection_type of this ConnectionSummary.
        The connection type.


        :param connection_type: The connection_type of this ConnectionSummary.
        :type: str
        """
        allowed_values = ["GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "DB2", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY", "DATABRICKS", "GOOGLE_PUBSUB", "MICROSOFT_FABRIC", "ICEBERG"]
        if not value_allowed_none_or_none_sentinel(connection_type, allowed_values):
            connection_type = 'UNKNOWN_ENUM_VALUE'
        self._connection_type = connection_type

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ConnectionSummary.
        The `OCID`__ of the connection being
        referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ConnectionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConnectionSummary.
        The `OCID`__ of the connection being
        referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ConnectionSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ConnectionSummary.
        An object's Display Name.


        :return: The display_name of this ConnectionSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ConnectionSummary.
        An object's Display Name.


        :param display_name: The display_name of this ConnectionSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this ConnectionSummary.
        Metadata about this specific object.


        :return: The description of this ConnectionSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ConnectionSummary.
        Metadata about this specific object.


        :param description: The description of this ConnectionSummary.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ConnectionSummary.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ConnectionSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ConnectionSummary.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ConnectionSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ConnectionSummary.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists
        for cross-compatibility only.

        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ConnectionSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ConnectionSummary.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists
        for cross-compatibility only.

        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ConnectionSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ConnectionSummary.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ConnectionSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ConnectionSummary.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ConnectionSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ConnectionSummary.
        The system tags associated with this resource, if any. The system tags are set by Oracle
        Cloud Infrastructure services. Each key is predefined and scoped to namespaces.  For more
        information, see `Resource Tags`__.

        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this ConnectionSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ConnectionSummary.
        The system tags associated with this resource, if any. The system tags are set by Oracle
        Cloud Infrastructure services. Each key is predefined and scoped to namespaces.  For more
        information, see `Resource Tags`__.

        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this ConnectionSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ConnectionSummary.
        Possible lifecycle states for connection.


        :return: The lifecycle_state of this ConnectionSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ConnectionSummary.
        Possible lifecycle states for connection.


        :param lifecycle_state: The lifecycle_state of this ConnectionSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ConnectionSummary.
        Describes the object's current state in detail. For example, it can be used to provide
        actionable information for a resource in a Failed state.


        :return: The lifecycle_details of this ConnectionSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ConnectionSummary.
        Describes the object's current state in detail. For example, it can be used to provide
        actionable information for a resource in a Failed state.


        :param lifecycle_details: The lifecycle_details of this ConnectionSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ConnectionSummary.
        The time the resource was created. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ConnectionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ConnectionSummary.
        The time the resource was created. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ConnectionSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ConnectionSummary.
        The time the resource was last updated. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this ConnectionSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ConnectionSummary.
        The time the resource was last updated. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this ConnectionSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def vault_id(self):
        """
        Gets the vault_id of this ConnectionSummary.
        Refers to the customer's vault OCID.
        If provided, it references a vault where GoldenGate can manage secrets. Customers must add policies to permit GoldenGate
        to manage secrets contained within this vault.


        :return: The vault_id of this ConnectionSummary.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """
        Sets the vault_id of this ConnectionSummary.
        Refers to the customer's vault OCID.
        If provided, it references a vault where GoldenGate can manage secrets. Customers must add policies to permit GoldenGate
        to manage secrets contained within this vault.


        :param vault_id: The vault_id of this ConnectionSummary.
        :type: str
        """
        self._vault_id = vault_id

    @property
    def key_id(self):
        """
        Gets the key_id of this ConnectionSummary.
        Refers to the customer's master key OCID.
        If provided, it references a key to manage secrets. Customers must add policies to permit GoldenGate to use this key.


        :return: The key_id of this ConnectionSummary.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this ConnectionSummary.
        Refers to the customer's master key OCID.
        If provided, it references a key to manage secrets. Customers must add policies to permit GoldenGate to use this key.


        :param key_id: The key_id of this ConnectionSummary.
        :type: str
        """
        self._key_id = key_id

    @property
    def ingress_ips(self):
        """
        Gets the ingress_ips of this ConnectionSummary.
        List of ingress IP addresses from where the GoldenGate deployment connects to this connection's privateIp.
        Customers may optionally set up ingress security rules to restrict traffic from these IP addresses.


        :return: The ingress_ips of this ConnectionSummary.
        :rtype: list[oci.golden_gate.models.IngressIpDetails]
        """
        return self._ingress_ips

    @ingress_ips.setter
    def ingress_ips(self, ingress_ips):
        """
        Sets the ingress_ips of this ConnectionSummary.
        List of ingress IP addresses from where the GoldenGate deployment connects to this connection's privateIp.
        Customers may optionally set up ingress security rules to restrict traffic from these IP addresses.


        :param ingress_ips: The ingress_ips of this ConnectionSummary.
        :type: list[oci.golden_gate.models.IngressIpDetails]
        """
        self._ingress_ips = ingress_ips

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this ConnectionSummary.
        An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.


        :return: The nsg_ids of this ConnectionSummary.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this ConnectionSummary.
        An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.


        :param nsg_ids: The nsg_ids of this ConnectionSummary.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this ConnectionSummary.
        The `OCID`__ of the target subnet of the dedicated connection.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this ConnectionSummary.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this ConnectionSummary.
        The `OCID`__ of the target subnet of the dedicated connection.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this ConnectionSummary.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def routing_method(self):
        """
        Gets the routing_method of this ConnectionSummary.
        Controls the network traffic direction to the target:
        SHARED_SERVICE_ENDPOINT: Traffic flows through the Goldengate Service's network to public hosts. Cannot be used for private targets.
        SHARED_DEPLOYMENT_ENDPOINT: Network traffic flows from the assigned deployment's private endpoint through the deployment's subnet.
        DEDICATED_ENDPOINT: A dedicated private endpoint is created in the target VCN subnet for the connection. The subnetId is required when DEDICATED_ENDPOINT networking is selected.

        Allowed values for this property are: "SHARED_SERVICE_ENDPOINT", "SHARED_DEPLOYMENT_ENDPOINT", "DEDICATED_ENDPOINT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The routing_method of this ConnectionSummary.
        :rtype: str
        """
        return self._routing_method

    @routing_method.setter
    def routing_method(self, routing_method):
        """
        Sets the routing_method of this ConnectionSummary.
        Controls the network traffic direction to the target:
        SHARED_SERVICE_ENDPOINT: Traffic flows through the Goldengate Service's network to public hosts. Cannot be used for private targets.
        SHARED_DEPLOYMENT_ENDPOINT: Network traffic flows from the assigned deployment's private endpoint through the deployment's subnet.
        DEDICATED_ENDPOINT: A dedicated private endpoint is created in the target VCN subnet for the connection. The subnetId is required when DEDICATED_ENDPOINT networking is selected.


        :param routing_method: The routing_method of this ConnectionSummary.
        :type: str
        """
        allowed_values = ["SHARED_SERVICE_ENDPOINT", "SHARED_DEPLOYMENT_ENDPOINT", "DEDICATED_ENDPOINT"]
        if not value_allowed_none_or_none_sentinel(routing_method, allowed_values):
            routing_method = 'UNKNOWN_ENUM_VALUE'
        self._routing_method = routing_method

    @property
    def locks(self):
        """
        Gets the locks of this ConnectionSummary.
        Locks associated with this resource.


        :return: The locks of this ConnectionSummary.
        :rtype: list[oci.golden_gate.models.ResourceLock]
        """
        return self._locks

    @locks.setter
    def locks(self, locks):
        """
        Sets the locks of this ConnectionSummary.
        Locks associated with this resource.


        :param locks: The locks of this ConnectionSummary.
        :type: list[oci.golden_gate.models.ResourceLock]
        """
        self._locks = locks

    @property
    def does_use_secret_ids(self):
        """
        Gets the does_use_secret_ids of this ConnectionSummary.
        Indicates that sensitive attributes are provided via Secrets.


        :return: The does_use_secret_ids of this ConnectionSummary.
        :rtype: bool
        """
        return self._does_use_secret_ids

    @does_use_secret_ids.setter
    def does_use_secret_ids(self, does_use_secret_ids):
        """
        Sets the does_use_secret_ids of this ConnectionSummary.
        Indicates that sensitive attributes are provided via Secrets.


        :param does_use_secret_ids: The does_use_secret_ids of this ConnectionSummary.
        :type: bool
        """
        self._does_use_secret_ids = does_use_secret_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
