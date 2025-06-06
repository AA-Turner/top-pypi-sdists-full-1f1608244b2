# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407

from .update_connection_details import UpdateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateIcebergConnectionDetails(UpdateConnectionDetails):
    """
    The information to update an Iceberg Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateIcebergConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.UpdateIcebergConnectionDetails.connection_type` attribute
        of this class is ``ICEBERG`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this UpdateIcebergConnectionDetails.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "DB2", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY", "DATABRICKS", "GOOGLE_PUBSUB", "MICROSOFT_FABRIC", "ICEBERG"
        :type connection_type: str

        :param display_name:
            The value to assign to the display_name property of this UpdateIcebergConnectionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateIcebergConnectionDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateIcebergConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateIcebergConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param vault_id:
            The value to assign to the vault_id property of this UpdateIcebergConnectionDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this UpdateIcebergConnectionDetails.
        :type key_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateIcebergConnectionDetails.
        :type nsg_ids: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this UpdateIcebergConnectionDetails.
        :type subnet_id: str

        :param routing_method:
            The value to assign to the routing_method property of this UpdateIcebergConnectionDetails.
            Allowed values for this property are: "SHARED_SERVICE_ENDPOINT", "SHARED_DEPLOYMENT_ENDPOINT", "DEDICATED_ENDPOINT"
        :type routing_method: str

        :param does_use_secret_ids:
            The value to assign to the does_use_secret_ids property of this UpdateIcebergConnectionDetails.
        :type does_use_secret_ids: bool

        :param catalog:
            The value to assign to the catalog property of this UpdateIcebergConnectionDetails.
        :type catalog: oci.golden_gate.models.UpdateIcebergCatalogDetails

        :param storage:
            The value to assign to the storage property of this UpdateIcebergConnectionDetails.
        :type storage: oci.golden_gate.models.UpdateIcebergStorageDetails

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
            'catalog': 'UpdateIcebergCatalogDetails',
            'storage': 'UpdateIcebergStorageDetails'
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
            'catalog': 'catalog',
            'storage': 'storage'
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
        self._catalog = None
        self._storage = None
        self._connection_type = 'ICEBERG'

    @property
    def catalog(self):
        """
        Gets the catalog of this UpdateIcebergConnectionDetails.

        :return: The catalog of this UpdateIcebergConnectionDetails.
        :rtype: oci.golden_gate.models.UpdateIcebergCatalogDetails
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        """
        Sets the catalog of this UpdateIcebergConnectionDetails.

        :param catalog: The catalog of this UpdateIcebergConnectionDetails.
        :type: oci.golden_gate.models.UpdateIcebergCatalogDetails
        """
        self._catalog = catalog

    @property
    def storage(self):
        """
        Gets the storage of this UpdateIcebergConnectionDetails.

        :return: The storage of this UpdateIcebergConnectionDetails.
        :rtype: oci.golden_gate.models.UpdateIcebergStorageDetails
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """
        Sets the storage of this UpdateIcebergConnectionDetails.

        :param storage: The storage of this UpdateIcebergConnectionDetails.
        :type: oci.golden_gate.models.UpdateIcebergStorageDetails
        """
        self._storage = storage

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
