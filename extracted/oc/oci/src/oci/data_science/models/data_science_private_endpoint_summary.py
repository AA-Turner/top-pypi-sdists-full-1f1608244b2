# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataSciencePrivateEndpointSummary(object):
    """
    List of Data Science private endpoints.
    """

    #: A constant which can be used with the lifecycle_state property of a DataSciencePrivateEndpointSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DataSciencePrivateEndpointSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DataSciencePrivateEndpointSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DataSciencePrivateEndpointSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DataSciencePrivateEndpointSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DataSciencePrivateEndpointSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a DataSciencePrivateEndpointSummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the data_science_resource_type property of a DataSciencePrivateEndpointSummary.
    #: This constant has a value of "NOTEBOOK_SESSION"
    DATA_SCIENCE_RESOURCE_TYPE_NOTEBOOK_SESSION = "NOTEBOOK_SESSION"

    #: A constant which can be used with the data_science_resource_type property of a DataSciencePrivateEndpointSummary.
    #: This constant has a value of "MODEL_DEPLOYMENT"
    DATA_SCIENCE_RESOURCE_TYPE_MODEL_DEPLOYMENT = "MODEL_DEPLOYMENT"

    def __init__(self, **kwargs):
        """
        Initializes a new DataSciencePrivateEndpointSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this DataSciencePrivateEndpointSummary.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this DataSciencePrivateEndpointSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this DataSciencePrivateEndpointSummary.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DataSciencePrivateEndpointSummary.
        :type freeform_tags: dict(str, str)

        :param system_tags:
            The value to assign to the system_tags property of this DataSciencePrivateEndpointSummary.
        :type system_tags: dict(str, dict(str, object))

        :param id:
            The value to assign to the id property of this DataSciencePrivateEndpointSummary.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DataSciencePrivateEndpointSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DataSciencePrivateEndpointSummary.
        :type lifecycle_details: str

        :param data_science_resource_type:
            The value to assign to the data_science_resource_type property of this DataSciencePrivateEndpointSummary.
            Allowed values for this property are: "NOTEBOOK_SESSION", "MODEL_DEPLOYMENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_science_resource_type: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this DataSciencePrivateEndpointSummary.
        :type nsg_ids: list[str]

        :param created_by:
            The value to assign to the created_by property of this DataSciencePrivateEndpointSummary.
        :type created_by: str

        :param subnet_id:
            The value to assign to the subnet_id property of this DataSciencePrivateEndpointSummary.
        :type subnet_id: str

        :param fqdn:
            The value to assign to the fqdn property of this DataSciencePrivateEndpointSummary.
        :type fqdn: str

        :param time_created:
            The value to assign to the time_created property of this DataSciencePrivateEndpointSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DataSciencePrivateEndpointSummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'system_tags': 'dict(str, dict(str, object))',
            'id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'data_science_resource_type': 'str',
            'nsg_ids': 'list[str]',
            'created_by': 'str',
            'subnet_id': 'str',
            'fqdn': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }
        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'system_tags': 'systemTags',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'data_science_resource_type': 'dataScienceResourceType',
            'nsg_ids': 'nsgIds',
            'created_by': 'createdBy',
            'subnet_id': 'subnetId',
            'fqdn': 'fqdn',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }
        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._system_tags = None
        self._id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._data_science_resource_type = None
        self._nsg_ids = None
        self._created_by = None
        self._subnet_id = None
        self._fqdn = None
        self._time_created = None
        self._time_updated = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DataSciencePrivateEndpointSummary.
        The `OCID`__ of the compartment where you want to create private Endpoint.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DataSciencePrivateEndpointSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DataSciencePrivateEndpointSummary.
        The `OCID`__ of the compartment where you want to create private Endpoint.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DataSciencePrivateEndpointSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this DataSciencePrivateEndpointSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this DataSciencePrivateEndpointSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DataSciencePrivateEndpointSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this DataSciencePrivateEndpointSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DataSciencePrivateEndpointSummary.
        A user friendly name. It doesn't have to be unique. Avoid entering confidential information.


        :return: The display_name of this DataSciencePrivateEndpointSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DataSciencePrivateEndpointSummary.
        A user friendly name. It doesn't have to be unique. Avoid entering confidential information.


        :param display_name: The display_name of this DataSciencePrivateEndpointSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this DataSciencePrivateEndpointSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this DataSciencePrivateEndpointSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DataSciencePrivateEndpointSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this DataSciencePrivateEndpointSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DataSciencePrivateEndpointSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this DataSciencePrivateEndpointSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DataSciencePrivateEndpointSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this DataSciencePrivateEndpointSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DataSciencePrivateEndpointSummary.
        The OCID of a private endpoint.


        :return: The id of this DataSciencePrivateEndpointSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DataSciencePrivateEndpointSummary.
        The OCID of a private endpoint.


        :param id: The id of this DataSciencePrivateEndpointSummary.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DataSciencePrivateEndpointSummary.
        State of a private endpoint.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DataSciencePrivateEndpointSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DataSciencePrivateEndpointSummary.
        State of a private endpoint.


        :param lifecycle_state: The lifecycle_state of this DataSciencePrivateEndpointSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        **[Required]** Gets the lifecycle_details of this DataSciencePrivateEndpointSummary.
        Details of the state of a private endpoint.


        :return: The lifecycle_details of this DataSciencePrivateEndpointSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DataSciencePrivateEndpointSummary.
        Details of the state of a private endpoint.


        :param lifecycle_details: The lifecycle_details of this DataSciencePrivateEndpointSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def data_science_resource_type(self):
        """
        **[Required]** Gets the data_science_resource_type of this DataSciencePrivateEndpointSummary.
        Data Science resource type.

        Allowed values for this property are: "NOTEBOOK_SESSION", "MODEL_DEPLOYMENT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The data_science_resource_type of this DataSciencePrivateEndpointSummary.
        :rtype: str
        """
        return self._data_science_resource_type

    @data_science_resource_type.setter
    def data_science_resource_type(self, data_science_resource_type):
        """
        Sets the data_science_resource_type of this DataSciencePrivateEndpointSummary.
        Data Science resource type.


        :param data_science_resource_type: The data_science_resource_type of this DataSciencePrivateEndpointSummary.
        :type: str
        """
        allowed_values = ["NOTEBOOK_SESSION", "MODEL_DEPLOYMENT"]
        if not value_allowed_none_or_none_sentinel(data_science_resource_type, allowed_values):
            data_science_resource_type = 'UNKNOWN_ENUM_VALUE'
        self._data_science_resource_type = data_science_resource_type

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this DataSciencePrivateEndpointSummary.
        An array of network security group OCIDs.


        :return: The nsg_ids of this DataSciencePrivateEndpointSummary.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this DataSciencePrivateEndpointSummary.
        An array of network security group OCIDs.


        :param nsg_ids: The nsg_ids of this DataSciencePrivateEndpointSummary.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def created_by(self):
        """
        **[Required]** Gets the created_by of this DataSciencePrivateEndpointSummary.
        The `OCID`__ of the user that created the private endpoint.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The created_by of this DataSciencePrivateEndpointSummary.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this DataSciencePrivateEndpointSummary.
        The `OCID`__ of the user that created the private endpoint.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param created_by: The created_by of this DataSciencePrivateEndpointSummary.
        :type: str
        """
        self._created_by = created_by

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this DataSciencePrivateEndpointSummary.
        The OCID of a subnet.


        :return: The subnet_id of this DataSciencePrivateEndpointSummary.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this DataSciencePrivateEndpointSummary.
        The OCID of a subnet.


        :param subnet_id: The subnet_id of this DataSciencePrivateEndpointSummary.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def fqdn(self):
        """
        **[Required]** Gets the fqdn of this DataSciencePrivateEndpointSummary.
        Accesing Data Science resource using FQDN.


        :return: The fqdn of this DataSciencePrivateEndpointSummary.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """
        Sets the fqdn of this DataSciencePrivateEndpointSummary.
        Accesing Data Science resource using FQDN.


        :param fqdn: The fqdn of this DataSciencePrivateEndpointSummary.
        :type: str
        """
        self._fqdn = fqdn

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DataSciencePrivateEndpointSummary.
        The date and time that the Data Science private endpoint was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this DataSciencePrivateEndpointSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DataSciencePrivateEndpointSummary.
        The date and time that the Data Science private endpoint was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this DataSciencePrivateEndpointSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this DataSciencePrivateEndpointSummary.
        The date and time that the Data Science private endpoint was updated expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this DataSciencePrivateEndpointSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DataSciencePrivateEndpointSummary.
        The date and time that the Data Science private endpoint was updated expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this DataSciencePrivateEndpointSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
