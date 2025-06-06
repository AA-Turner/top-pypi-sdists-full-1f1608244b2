# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeHostGroupSummary(object):
    """
    Summary information for a compute host group.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeHostGroupSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this ComputeHostGroupSummary.
        :type availability_domain: str

        :param id:
            The value to assign to the id property of this ComputeHostGroupSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ComputeHostGroupSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ComputeHostGroupSummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this ComputeHostGroupSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ComputeHostGroupSummary.
        :type time_updated: datetime

        :param defined_tags:
            The value to assign to the defined_tags property of this ComputeHostGroupSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ComputeHostGroupSummary.
        :type freeform_tags: dict(str, str)

        :param system_tags:
            The value to assign to the system_tags property of this ComputeHostGroupSummary.
        :type system_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ComputeHostGroupSummary.
        :type lifecycle_state: str

        :param is_targeted_placement_required:
            The value to assign to the is_targeted_placement_required property of this ComputeHostGroupSummary.
        :type is_targeted_placement_required: bool

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'system_tags': 'dict(str, dict(str, object))',
            'lifecycle_state': 'str',
            'is_targeted_placement_required': 'bool'
        }
        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'system_tags': 'systemTags',
            'lifecycle_state': 'lifecycleState',
            'is_targeted_placement_required': 'isTargetedPlacementRequired'
        }
        self._availability_domain = None
        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._defined_tags = None
        self._freeform_tags = None
        self._system_tags = None
        self._lifecycle_state = None
        self._is_targeted_placement_required = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this ComputeHostGroupSummary.
        The availability domain of a host group.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this ComputeHostGroupSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this ComputeHostGroupSummary.
        The availability domain of a host group.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this ComputeHostGroupSummary.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ComputeHostGroupSummary.
        The `OCID`__ for the Customer-unique host group

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ComputeHostGroupSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ComputeHostGroupSummary.
        The `OCID`__ for the Customer-unique host group

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ComputeHostGroupSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ComputeHostGroupSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this ComputeHostGroupSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ComputeHostGroupSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this ComputeHostGroupSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ComputeHostGroupSummary.
        The OCID of the compartment that contains host group.


        :return: The compartment_id of this ComputeHostGroupSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ComputeHostGroupSummary.
        The OCID of the compartment that contains host group.


        :param compartment_id: The compartment_id of this ComputeHostGroupSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ComputeHostGroupSummary.
        The date and time the host group was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ComputeHostGroupSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ComputeHostGroupSummary.
        The date and time the host group was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ComputeHostGroupSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ComputeHostGroupSummary.
        The date and time the host group was updated, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this ComputeHostGroupSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ComputeHostGroupSummary.
        The date and time the host group was updated, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this ComputeHostGroupSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ComputeHostGroupSummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ComputeHostGroupSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ComputeHostGroupSummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ComputeHostGroupSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ComputeHostGroupSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ComputeHostGroupSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ComputeHostGroupSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ComputeHostGroupSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ComputeHostGroupSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The system_tags of this ComputeHostGroupSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ComputeHostGroupSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param system_tags: The system_tags of this ComputeHostGroupSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ComputeHostGroupSummary.
        The current state of the compute host group


        :return: The lifecycle_state of this ComputeHostGroupSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ComputeHostGroupSummary.
        The current state of the compute host group


        :param lifecycle_state: The lifecycle_state of this ComputeHostGroupSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def is_targeted_placement_required(self):
        """
        **[Required]** Gets the is_targeted_placement_required of this ComputeHostGroupSummary.
        A flag that allows customers to restrict placement for hosts attached to the group. If true, the only way to place on hosts is to target the specific host group.


        :return: The is_targeted_placement_required of this ComputeHostGroupSummary.
        :rtype: bool
        """
        return self._is_targeted_placement_required

    @is_targeted_placement_required.setter
    def is_targeted_placement_required(self, is_targeted_placement_required):
        """
        Sets the is_targeted_placement_required of this ComputeHostGroupSummary.
        A flag that allows customers to restrict placement for hosts attached to the group. If true, the only way to place on hosts is to target the specific host group.


        :param is_targeted_placement_required: The is_targeted_placement_required of this ComputeHostGroupSummary.
        :type: bool
        """
        self._is_targeted_placement_required = is_targeted_placement_required

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
