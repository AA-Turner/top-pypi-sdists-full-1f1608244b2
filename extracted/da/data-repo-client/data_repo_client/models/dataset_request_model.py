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


class DatasetRequestModel(object):
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
        'name': 'str',
        'description': 'str',
        'default_profile_id': 'str',
        'schema': 'DatasetSpecificationModel',
        'region': 'str',
        'cloud_platform': 'CloudPlatform',
        'enable_secure_monitoring': 'bool',
        'phs_id': 'str',
        'experimental_self_hosted': 'bool',
        'properties': 'object',
        'dedicated_ingest_service_account': 'bool',
        'experimental_predictable_file_ids': 'bool',
        'policies': 'DatasetRequestModelPolicies',
        'inherit_steward': 'bool',
        'tags': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'default_profile_id': 'defaultProfileId',
        'schema': 'schema',
        'region': 'region',
        'cloud_platform': 'cloudPlatform',
        'enable_secure_monitoring': 'enableSecureMonitoring',
        'phs_id': 'phsId',
        'experimental_self_hosted': 'experimentalSelfHosted',
        'properties': 'properties',
        'dedicated_ingest_service_account': 'dedicatedIngestServiceAccount',
        'experimental_predictable_file_ids': 'experimentalPredictableFileIds',
        'policies': 'policies',
        'inherit_steward': 'inheritSteward',
        'tags': 'tags'
    }

    def __init__(self, name=None, description=None, default_profile_id=None, schema=None, region=None, cloud_platform=None, enable_secure_monitoring=False, phs_id=None, experimental_self_hosted=False, properties=None, dedicated_ingest_service_account=True, experimental_predictable_file_ids=False, policies=None, inherit_steward=False, tags=None, local_vars_configuration=None):  # noqa: E501
        """DatasetRequestModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._default_profile_id = None
        self._schema = None
        self._region = None
        self._cloud_platform = None
        self._enable_secure_monitoring = None
        self._phs_id = None
        self._experimental_self_hosted = None
        self._properties = None
        self._dedicated_ingest_service_account = None
        self._experimental_predictable_file_ids = None
        self._policies = None
        self._inherit_steward = None
        self._tags = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.default_profile_id = default_profile_id
        self.schema = schema
        if region is not None:
            self.region = region
        if cloud_platform is not None:
            self.cloud_platform = cloud_platform
        if enable_secure_monitoring is not None:
            self.enable_secure_monitoring = enable_secure_monitoring
        if phs_id is not None:
            self.phs_id = phs_id
        if experimental_self_hosted is not None:
            self.experimental_self_hosted = experimental_self_hosted
        if properties is not None:
            self.properties = properties
        if dedicated_ingest_service_account is not None:
            self.dedicated_ingest_service_account = dedicated_ingest_service_account
        if experimental_predictable_file_ids is not None:
            self.experimental_predictable_file_ids = experimental_predictable_file_ids
        if policies is not None:
            self.policies = policies
        if inherit_steward is not None:
            self.inherit_steward = inherit_steward
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this DatasetRequestModel.  # noqa: E501

        Dataset and snapshot names follow this pattern. It is the same as ObjectNameProperty, but has a greater maxLength.   # noqa: E501

        :return: The name of this DatasetRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatasetRequestModel.

        Dataset and snapshot names follow this pattern. It is the same as ObjectNameProperty, but has a greater maxLength.   # noqa: E501

        :param name: The name of this DatasetRequestModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
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
        """Gets the description of this DatasetRequestModel.  # noqa: E501

        Description of the dataset  # noqa: E501

        :return: The description of this DatasetRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DatasetRequestModel.

        Description of the dataset  # noqa: E501

        :param description: The description of this DatasetRequestModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def default_profile_id(self):
        """Gets the default_profile_id of this DatasetRequestModel.  # noqa: E501

        Unique identifier for a dataset, snapshot, etc.   # noqa: E501

        :return: The default_profile_id of this DatasetRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._default_profile_id

    @default_profile_id.setter
    def default_profile_id(self, default_profile_id):
        """Sets the default_profile_id of this DatasetRequestModel.

        Unique identifier for a dataset, snapshot, etc.   # noqa: E501

        :param default_profile_id: The default_profile_id of this DatasetRequestModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and default_profile_id is None:  # noqa: E501
            raise ValueError("Invalid value for `default_profile_id`, must not be `None`")  # noqa: E501

        self._default_profile_id = default_profile_id

    @property
    def schema(self):
        """Gets the schema of this DatasetRequestModel.  # noqa: E501


        :return: The schema of this DatasetRequestModel.  # noqa: E501
        :rtype: DatasetSpecificationModel
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this DatasetRequestModel.


        :param schema: The schema of this DatasetRequestModel.  # noqa: E501
        :type: DatasetSpecificationModel
        """
        if self.local_vars_configuration.client_side_validation and schema is None:  # noqa: E501
            raise ValueError("Invalid value for `schema`, must not be `None`")  # noqa: E501

        self._schema = schema

    @property
    def region(self):
        """Gets the region of this DatasetRequestModel.  # noqa: E501


        :return: The region of this DatasetRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this DatasetRequestModel.


        :param region: The region of this DatasetRequestModel.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def cloud_platform(self):
        """Gets the cloud_platform of this DatasetRequestModel.  # noqa: E501


        :return: The cloud_platform of this DatasetRequestModel.  # noqa: E501
        :rtype: CloudPlatform
        """
        return self._cloud_platform

    @cloud_platform.setter
    def cloud_platform(self, cloud_platform):
        """Sets the cloud_platform of this DatasetRequestModel.


        :param cloud_platform: The cloud_platform of this DatasetRequestModel.  # noqa: E501
        :type: CloudPlatform
        """

        self._cloud_platform = cloud_platform

    @property
    def enable_secure_monitoring(self):
        """Gets the enable_secure_monitoring of this DatasetRequestModel.  # noqa: E501


        :return: The enable_secure_monitoring of this DatasetRequestModel.  # noqa: E501
        :rtype: bool
        """
        return self._enable_secure_monitoring

    @enable_secure_monitoring.setter
    def enable_secure_monitoring(self, enable_secure_monitoring):
        """Sets the enable_secure_monitoring of this DatasetRequestModel.


        :param enable_secure_monitoring: The enable_secure_monitoring of this DatasetRequestModel.  # noqa: E501
        :type: bool
        """

        self._enable_secure_monitoring = enable_secure_monitoring

    @property
    def phs_id(self):
        """Gets the phs_id of this DatasetRequestModel.  # noqa: E501

        PHS ID (DbGap Phenotype Study Identifer) associated with dataset  # noqa: E501

        :return: The phs_id of this DatasetRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._phs_id

    @phs_id.setter
    def phs_id(self, phs_id):
        """Sets the phs_id of this DatasetRequestModel.

        PHS ID (DbGap Phenotype Study Identifer) associated with dataset  # noqa: E501

        :param phs_id: The phs_id of this DatasetRequestModel.  # noqa: E501
        :type: str
        """

        self._phs_id = phs_id

    @property
    def experimental_self_hosted(self):
        """Gets the experimental_self_hosted of this DatasetRequestModel.  # noqa: E501

        Create the dataset in self-hosted mode, where TDR does not ingest files, but rather points to files in their original location.  # noqa: E501

        :return: The experimental_self_hosted of this DatasetRequestModel.  # noqa: E501
        :rtype: bool
        """
        return self._experimental_self_hosted

    @experimental_self_hosted.setter
    def experimental_self_hosted(self, experimental_self_hosted):
        """Sets the experimental_self_hosted of this DatasetRequestModel.

        Create the dataset in self-hosted mode, where TDR does not ingest files, but rather points to files in their original location.  # noqa: E501

        :param experimental_self_hosted: The experimental_self_hosted of this DatasetRequestModel.  # noqa: E501
        :type: bool
        """

        self._experimental_self_hosted = experimental_self_hosted

    @property
    def properties(self):
        """Gets the properties of this DatasetRequestModel.  # noqa: E501

        Additional JSON metadata about the dataset (this does not need to adhere to a particular schema)  # noqa: E501

        :return: The properties of this DatasetRequestModel.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this DatasetRequestModel.

        Additional JSON metadata about the dataset (this does not need to adhere to a particular schema)  # noqa: E501

        :param properties: The properties of this DatasetRequestModel.  # noqa: E501
        :type: object
        """

        self._properties = properties

    @property
    def dedicated_ingest_service_account(self):
        """Gets the dedicated_ingest_service_account of this DatasetRequestModel.  # noqa: E501

        This field is only relevant for GCP-backed datasets. If true, a unique service account will be created in the dataset's primary GCP project, registered in Terra, and used to facilitate ingests. If false, TDR's general service account will be used.  The dataset's service account can be found when retrieving the dataset.  Whether it is dedicated or general, it must be granted `storage.objects.get` permissions on any source buckets that TDR will ingest data from. This can be done by giving the service account the \"Storage Object Viewer\", \"Storage Legacy Object Reader\", or \"Storage Legacy Object Owner\" role on the source buckets.  TDR recommends that this be set to true:  - A dedicated account that explicitly does not have access to other buckets is more   secure and isolated from issues that could impact the general account. - Up to 2.5x speed improvements when ingesting files. TDR can bypass the costly   permission checking of all user-specified GCP files to ingest if the dataset has a   dedicated service account. Such accounts are unique to the dataset and ingests will   correctly fail if they lack needed permission on the files. Otherwise, we must   perform this check to ensure that a user cannot ingest files inaccessible to them, but   accessible to the general TDR service account. - Only the dataset's dedicated account must be granted permissions on source ingest   buckets.  When using the general account, you must also grant permissions to the Terra   proxy user groups for any users triggering ingests. - A dedicated service account is less likely to encounter Google group membership quota   violations, which is relevant if you need to authorize a large number of buckets.   # noqa: E501

        :return: The dedicated_ingest_service_account of this DatasetRequestModel.  # noqa: E501
        :rtype: bool
        """
        return self._dedicated_ingest_service_account

    @dedicated_ingest_service_account.setter
    def dedicated_ingest_service_account(self, dedicated_ingest_service_account):
        """Sets the dedicated_ingest_service_account of this DatasetRequestModel.

        This field is only relevant for GCP-backed datasets. If true, a unique service account will be created in the dataset's primary GCP project, registered in Terra, and used to facilitate ingests. If false, TDR's general service account will be used.  The dataset's service account can be found when retrieving the dataset.  Whether it is dedicated or general, it must be granted `storage.objects.get` permissions on any source buckets that TDR will ingest data from. This can be done by giving the service account the \"Storage Object Viewer\", \"Storage Legacy Object Reader\", or \"Storage Legacy Object Owner\" role on the source buckets.  TDR recommends that this be set to true:  - A dedicated account that explicitly does not have access to other buckets is more   secure and isolated from issues that could impact the general account. - Up to 2.5x speed improvements when ingesting files. TDR can bypass the costly   permission checking of all user-specified GCP files to ingest if the dataset has a   dedicated service account. Such accounts are unique to the dataset and ingests will   correctly fail if they lack needed permission on the files. Otherwise, we must   perform this check to ensure that a user cannot ingest files inaccessible to them, but   accessible to the general TDR service account. - Only the dataset's dedicated account must be granted permissions on source ingest   buckets.  When using the general account, you must also grant permissions to the Terra   proxy user groups for any users triggering ingests. - A dedicated service account is less likely to encounter Google group membership quota   violations, which is relevant if you need to authorize a large number of buckets.   # noqa: E501

        :param dedicated_ingest_service_account: The dedicated_ingest_service_account of this DatasetRequestModel.  # noqa: E501
        :type: bool
        """

        self._dedicated_ingest_service_account = dedicated_ingest_service_account

    @property
    def experimental_predictable_file_ids(self):
        """Gets the experimental_predictable_file_ids of this DatasetRequestModel.  # noqa: E501

        If false, random ids will be created. If true, full target path (e.g. path + name), size and md5 hash will be used Note: this only applies to files.  Directories still have random ids regardless of this value   # noqa: E501

        :return: The experimental_predictable_file_ids of this DatasetRequestModel.  # noqa: E501
        :rtype: bool
        """
        return self._experimental_predictable_file_ids

    @experimental_predictable_file_ids.setter
    def experimental_predictable_file_ids(self, experimental_predictable_file_ids):
        """Sets the experimental_predictable_file_ids of this DatasetRequestModel.

        If false, random ids will be created. If true, full target path (e.g. path + name), size and md5 hash will be used Note: this only applies to files.  Directories still have random ids regardless of this value   # noqa: E501

        :param experimental_predictable_file_ids: The experimental_predictable_file_ids of this DatasetRequestModel.  # noqa: E501
        :type: bool
        """

        self._experimental_predictable_file_ids = experimental_predictable_file_ids

    @property
    def policies(self):
        """Gets the policies of this DatasetRequestModel.  # noqa: E501


        :return: The policies of this DatasetRequestModel.  # noqa: E501
        :rtype: DatasetRequestModelPolicies
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this DatasetRequestModel.


        :param policies: The policies of this DatasetRequestModel.  # noqa: E501
        :type: DatasetRequestModelPolicies
        """

        self._policies = policies

    @property
    def inherit_steward(self):
        """Gets the inherit_steward of this DatasetRequestModel.  # noqa: E501

        If true, all snapshots created from this dataset will grant dataset custodians the steward (owner) role on the snapshots. This is intended to be used in cases where a dataset will have many (> 1000) snapshots and the user wants all dataset custodians to have this role on all snapshots. Using this flag is a more efficient way to grant this role, and will avoid using up google resource quotas.   # noqa: E501

        :return: The inherit_steward of this DatasetRequestModel.  # noqa: E501
        :rtype: bool
        """
        return self._inherit_steward

    @inherit_steward.setter
    def inherit_steward(self, inherit_steward):
        """Sets the inherit_steward of this DatasetRequestModel.

        If true, all snapshots created from this dataset will grant dataset custodians the steward (owner) role on the snapshots. This is intended to be used in cases where a dataset will have many (> 1000) snapshots and the user wants all dataset custodians to have this role on all snapshots. Using this flag is a more efficient way to grant this role, and will avoid using up google resource quotas.   # noqa: E501

        :param inherit_steward: The inherit_steward of this DatasetRequestModel.  # noqa: E501
        :type: bool
        """

        self._inherit_steward = inherit_steward

    @property
    def tags(self):
        """Gets the tags of this DatasetRequestModel.  # noqa: E501

        Tags to add to the resource on its creation.  User-inputted tags will be stripped of leading and trailing whitespace, filtered of empty elements, and deduplicated.   # noqa: E501

        :return: The tags of this DatasetRequestModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DatasetRequestModel.

        Tags to add to the resource on its creation.  User-inputted tags will be stripped of leading and trailing whitespace, filtered of empty elements, and deduplicated.   # noqa: E501

        :param tags: The tags of this DatasetRequestModel.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

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
        if not isinstance(other, DatasetRequestModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DatasetRequestModel):
            return True

        return self.to_dict() != other.to_dict()
