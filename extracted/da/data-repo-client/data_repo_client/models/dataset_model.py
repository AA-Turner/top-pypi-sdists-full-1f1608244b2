# coding: utf-8

"""
    Data Repository API

    <details><summary>This document defines the REST API for the Terra Data Repository.</summary> <p> **Status: design in progress** There are a few top-level endpoints (besides some used by swagger):  * / - generated by swagger: swagger API page that provides this documentation and a live UI for submitting REST requests  * /status - provides the operational status of the service  * /configuration - provides the basic configuration and information about the service  * /api - is the authenticated and authorized Data Repository API  * /ga4gh/drs/v1 - is a transcription of the Data Repository Service API  The API endpoints are organized by interface. Each interface is separately versioned. <p> **Notes on Naming** <p> All of the reference items are suffixed with \\\"Model\\\". Those names are used as the class names in the generated Java code. It is helpful to distinguish these model classes from other related classes, like the DAO classes and the operation classes. </details>   # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from data_repo_client.configuration import Configuration


class DatasetModel(object):
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
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'default_profile_id': 'str',
        'data_project': 'str',
        'default_snapshot_id': 'str',
        'schema': 'DatasetSpecificationModel',
        'created_date': 'str',
        'storage': 'list[StorageResourceModel]',
        'secure_monitoring_enabled': 'bool',
        'phs_id': 'str',
        'access_information': 'AccessInfoModel',
        'cloud_platform': 'CloudPlatform',
        'self_hosted': 'bool',
        'properties': 'object',
        'ingest_service_account': 'str',
        'predictable_file_ids': 'bool',
        'tags': 'list[str]',
        'resource_locks': 'ResourceLocks',
        'inherit_steward': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'default_profile_id': 'defaultProfileId',
        'data_project': 'dataProject',
        'default_snapshot_id': 'defaultSnapshotId',
        'schema': 'schema',
        'created_date': 'createdDate',
        'storage': 'storage',
        'secure_monitoring_enabled': 'secureMonitoringEnabled',
        'phs_id': 'phsId',
        'access_information': 'accessInformation',
        'cloud_platform': 'cloudPlatform',
        'self_hosted': 'selfHosted',
        'properties': 'properties',
        'ingest_service_account': 'ingestServiceAccount',
        'predictable_file_ids': 'predictableFileIds',
        'tags': 'tags',
        'resource_locks': 'resourceLocks',
        'inherit_steward': 'inheritSteward'
    }

    def __init__(self, id=None, name=None, description=None, default_profile_id=None, data_project=None, default_snapshot_id=None, schema=None, created_date=None, storage=None, secure_monitoring_enabled=False, phs_id=None, access_information=None, cloud_platform=None, self_hosted=False, properties=None, ingest_service_account=None, predictable_file_ids=False, tags=None, resource_locks=None, inherit_steward=False, local_vars_configuration=None):  # noqa: E501
        """DatasetModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._description = None
        self._default_profile_id = None
        self._data_project = None
        self._default_snapshot_id = None
        self._schema = None
        self._created_date = None
        self._storage = None
        self._secure_monitoring_enabled = None
        self._phs_id = None
        self._access_information = None
        self._cloud_platform = None
        self._self_hosted = None
        self._properties = None
        self._ingest_service_account = None
        self._predictable_file_ids = None
        self._tags = None
        self._resource_locks = None
        self._inherit_steward = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if default_profile_id is not None:
            self.default_profile_id = default_profile_id
        if data_project is not None:
            self.data_project = data_project
        if default_snapshot_id is not None:
            self.default_snapshot_id = default_snapshot_id
        if schema is not None:
            self.schema = schema
        if created_date is not None:
            self.created_date = created_date
        if storage is not None:
            self.storage = storage
        if secure_monitoring_enabled is not None:
            self.secure_monitoring_enabled = secure_monitoring_enabled
        if phs_id is not None:
            self.phs_id = phs_id
        if access_information is not None:
            self.access_information = access_information
        if cloud_platform is not None:
            self.cloud_platform = cloud_platform
        if self_hosted is not None:
            self.self_hosted = self_hosted
        if properties is not None:
            self.properties = properties
        if ingest_service_account is not None:
            self.ingest_service_account = ingest_service_account
        if predictable_file_ids is not None:
            self.predictable_file_ids = predictable_file_ids
        if tags is not None:
            self.tags = tags
        if resource_locks is not None:
            self.resource_locks = resource_locks
        if inherit_steward is not None:
            self.inherit_steward = inherit_steward

    @property
    def id(self):
        """Gets the id of this DatasetModel.  # noqa: E501

        Unique identifier for a dataset, snapshot, etc.   # noqa: E501

        :return: The id of this DatasetModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatasetModel.

        Unique identifier for a dataset, snapshot, etc.   # noqa: E501

        :param id: The id of this DatasetModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DatasetModel.  # noqa: E501

        Dataset and snapshot names follow this pattern. It is the same as ObjectNameProperty, but has a greater maxLength.   # noqa: E501

        :return: The name of this DatasetModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatasetModel.

        Dataset and snapshot names follow this pattern. It is the same as ObjectNameProperty, but has a greater maxLength.   # noqa: E501

        :param name: The name of this DatasetModel.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 511):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `511`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[a-zA-Z0-9][_a-zA-Z0-9]*$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z0-9][_a-zA-Z0-9]*$/`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this DatasetModel.  # noqa: E501

        Description of the dataset  # noqa: E501

        :return: The description of this DatasetModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DatasetModel.

        Description of the dataset  # noqa: E501

        :param description: The description of this DatasetModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def default_profile_id(self):
        """Gets the default_profile_id of this DatasetModel.  # noqa: E501

        Unique identifier for a dataset, snapshot, etc.   # noqa: E501

        :return: The default_profile_id of this DatasetModel.  # noqa: E501
        :rtype: str
        """
        return self._default_profile_id

    @default_profile_id.setter
    def default_profile_id(self, default_profile_id):
        """Sets the default_profile_id of this DatasetModel.

        Unique identifier for a dataset, snapshot, etc.   # noqa: E501

        :param default_profile_id: The default_profile_id of this DatasetModel.  # noqa: E501
        :type: str
        """

        self._default_profile_id = default_profile_id

    @property
    def data_project(self):
        """Gets the data_project of this DatasetModel.  # noqa: E501

        Project id of the project where tabular data in BigQuery lives  # noqa: E501

        :return: The data_project of this DatasetModel.  # noqa: E501
        :rtype: str
        """
        return self._data_project

    @data_project.setter
    def data_project(self, data_project):
        """Sets the data_project of this DatasetModel.

        Project id of the project where tabular data in BigQuery lives  # noqa: E501

        :param data_project: The data_project of this DatasetModel.  # noqa: E501
        :type: str
        """

        self._data_project = data_project

    @property
    def default_snapshot_id(self):
        """Gets the default_snapshot_id of this DatasetModel.  # noqa: E501

        Id of the auto-generated default passthru snapshot  # noqa: E501

        :return: The default_snapshot_id of this DatasetModel.  # noqa: E501
        :rtype: str
        """
        return self._default_snapshot_id

    @default_snapshot_id.setter
    def default_snapshot_id(self, default_snapshot_id):
        """Sets the default_snapshot_id of this DatasetModel.

        Id of the auto-generated default passthru snapshot  # noqa: E501

        :param default_snapshot_id: The default_snapshot_id of this DatasetModel.  # noqa: E501
        :type: str
        """

        self._default_snapshot_id = default_snapshot_id

    @property
    def schema(self):
        """Gets the schema of this DatasetModel.  # noqa: E501


        :return: The schema of this DatasetModel.  # noqa: E501
        :rtype: DatasetSpecificationModel
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this DatasetModel.


        :param schema: The schema of this DatasetModel.  # noqa: E501
        :type: DatasetSpecificationModel
        """

        self._schema = schema

    @property
    def created_date(self):
        """Gets the created_date of this DatasetModel.  # noqa: E501

        Date the dataset was created  # noqa: E501

        :return: The created_date of this DatasetModel.  # noqa: E501
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this DatasetModel.

        Date the dataset was created  # noqa: E501

        :param created_date: The created_date of this DatasetModel.  # noqa: E501
        :type: str
        """

        self._created_date = created_date

    @property
    def storage(self):
        """Gets the storage of this DatasetModel.  # noqa: E501


        :return: The storage of this DatasetModel.  # noqa: E501
        :rtype: list[StorageResourceModel]
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this DatasetModel.


        :param storage: The storage of this DatasetModel.  # noqa: E501
        :type: list[StorageResourceModel]
        """

        self._storage = storage

    @property
    def secure_monitoring_enabled(self):
        """Gets the secure_monitoring_enabled of this DatasetModel.  # noqa: E501


        :return: The secure_monitoring_enabled of this DatasetModel.  # noqa: E501
        :rtype: bool
        """
        return self._secure_monitoring_enabled

    @secure_monitoring_enabled.setter
    def secure_monitoring_enabled(self, secure_monitoring_enabled):
        """Sets the secure_monitoring_enabled of this DatasetModel.


        :param secure_monitoring_enabled: The secure_monitoring_enabled of this DatasetModel.  # noqa: E501
        :type: bool
        """

        self._secure_monitoring_enabled = secure_monitoring_enabled

    @property
    def phs_id(self):
        """Gets the phs_id of this DatasetModel.  # noqa: E501

        PHS ID (DbGap Phenotype Study Identifer) associated with dataset  # noqa: E501

        :return: The phs_id of this DatasetModel.  # noqa: E501
        :rtype: str
        """
        return self._phs_id

    @phs_id.setter
    def phs_id(self, phs_id):
        """Sets the phs_id of this DatasetModel.

        PHS ID (DbGap Phenotype Study Identifer) associated with dataset  # noqa: E501

        :param phs_id: The phs_id of this DatasetModel.  # noqa: E501
        :type: str
        """

        self._phs_id = phs_id

    @property
    def access_information(self):
        """Gets the access_information of this DatasetModel.  # noqa: E501


        :return: The access_information of this DatasetModel.  # noqa: E501
        :rtype: AccessInfoModel
        """
        return self._access_information

    @access_information.setter
    def access_information(self, access_information):
        """Sets the access_information of this DatasetModel.


        :param access_information: The access_information of this DatasetModel.  # noqa: E501
        :type: AccessInfoModel
        """

        self._access_information = access_information

    @property
    def cloud_platform(self):
        """Gets the cloud_platform of this DatasetModel.  # noqa: E501


        :return: The cloud_platform of this DatasetModel.  # noqa: E501
        :rtype: CloudPlatform
        """
        return self._cloud_platform

    @cloud_platform.setter
    def cloud_platform(self, cloud_platform):
        """Sets the cloud_platform of this DatasetModel.


        :param cloud_platform: The cloud_platform of this DatasetModel.  # noqa: E501
        :type: CloudPlatform
        """

        self._cloud_platform = cloud_platform

    @property
    def self_hosted(self):
        """Gets the self_hosted of this DatasetModel.  # noqa: E501

        denotes whether data files in the dataset are self-hosted or not  # noqa: E501

        :return: The self_hosted of this DatasetModel.  # noqa: E501
        :rtype: bool
        """
        return self._self_hosted

    @self_hosted.setter
    def self_hosted(self, self_hosted):
        """Sets the self_hosted of this DatasetModel.

        denotes whether data files in the dataset are self-hosted or not  # noqa: E501

        :param self_hosted: The self_hosted of this DatasetModel.  # noqa: E501
        :type: bool
        """

        self._self_hosted = self_hosted

    @property
    def properties(self):
        """Gets the properties of this DatasetModel.  # noqa: E501

        Additional JSON metadata about the dataset (this does not need to adhere to a particular schema)  # noqa: E501

        :return: The properties of this DatasetModel.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this DatasetModel.

        Additional JSON metadata about the dataset (this does not need to adhere to a particular schema)  # noqa: E501

        :param properties: The properties of this DatasetModel.  # noqa: E501
        :type: object
        """

        self._properties = properties

    @property
    def ingest_service_account(self):
        """Gets the ingest_service_account of this DatasetModel.  # noqa: E501

        Google service account which must be granted `storage.objects.get` permissions on any source buckets that TDR will ingest data from.   # noqa: E501

        :return: The ingest_service_account of this DatasetModel.  # noqa: E501
        :rtype: str
        """
        return self._ingest_service_account

    @ingest_service_account.setter
    def ingest_service_account(self, ingest_service_account):
        """Sets the ingest_service_account of this DatasetModel.

        Google service account which must be granted `storage.objects.get` permissions on any source buckets that TDR will ingest data from.   # noqa: E501

        :param ingest_service_account: The ingest_service_account of this DatasetModel.  # noqa: E501
        :type: str
        """

        self._ingest_service_account = ingest_service_account

    @property
    def predictable_file_ids(self):
        """Gets the predictable_file_ids of this DatasetModel.  # noqa: E501

        If false, random ids will be created. If true, full target path (e.g. path + name), size and md5 hash will be used Note: this only applies to files.  Directories still have random ids regardless of this value   # noqa: E501

        :return: The predictable_file_ids of this DatasetModel.  # noqa: E501
        :rtype: bool
        """
        return self._predictable_file_ids

    @predictable_file_ids.setter
    def predictable_file_ids(self, predictable_file_ids):
        """Sets the predictable_file_ids of this DatasetModel.

        If false, random ids will be created. If true, full target path (e.g. path + name), size and md5 hash will be used Note: this only applies to files.  Directories still have random ids regardless of this value   # noqa: E501

        :param predictable_file_ids: The predictable_file_ids of this DatasetModel.  # noqa: E501
        :type: bool
        """

        self._predictable_file_ids = predictable_file_ids

    @property
    def tags(self):
        """Gets the tags of this DatasetModel.  # noqa: E501


        :return: The tags of this DatasetModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DatasetModel.


        :param tags: The tags of this DatasetModel.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def resource_locks(self):
        """Gets the resource_locks of this DatasetModel.  # noqa: E501


        :return: The resource_locks of this DatasetModel.  # noqa: E501
        :rtype: ResourceLocks
        """
        return self._resource_locks

    @resource_locks.setter
    def resource_locks(self, resource_locks):
        """Sets the resource_locks of this DatasetModel.


        :param resource_locks: The resource_locks of this DatasetModel.  # noqa: E501
        :type: ResourceLocks
        """

        self._resource_locks = resource_locks

    @property
    def inherit_steward(self):
        """Gets the inherit_steward of this DatasetModel.  # noqa: E501

        If true, all snapshots created from this dataset will grant dataset custodians the steward (owner) role on the snapshots.   # noqa: E501

        :return: The inherit_steward of this DatasetModel.  # noqa: E501
        :rtype: bool
        """
        return self._inherit_steward

    @inherit_steward.setter
    def inherit_steward(self, inherit_steward):
        """Sets the inherit_steward of this DatasetModel.

        If true, all snapshots created from this dataset will grant dataset custodians the steward (owner) role on the snapshots.   # noqa: E501

        :param inherit_steward: The inherit_steward of this DatasetModel.  # noqa: E501
        :type: bool
        """

        self._inherit_steward = inherit_steward

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
        if not isinstance(other, DatasetModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DatasetModel):
            return True

        return self.to_dict() != other.to_dict()
