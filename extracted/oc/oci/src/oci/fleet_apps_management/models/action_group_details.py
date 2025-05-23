# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20250228


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ActionGroupDetails(object):
    """
    Action Group details.
    """

    #: A constant which can be used with the kind property of a ActionGroupDetails.
    #: This constant has a value of "FLEET_USING_RUNBOOK"
    KIND_FLEET_USING_RUNBOOK = "FLEET_USING_RUNBOOK"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "WAITING"
    STATUS_WAITING = "WAITING"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "SKIPPED"
    STATUS_SKIPPED = "SKIPPED"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "IGNORED"
    STATUS_IGNORED = "IGNORED"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "NOT_APPLICABLE"
    STATUS_NOT_APPLICABLE = "NOT_APPLICABLE"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "ABORTED"
    STATUS_ABORTED = "ABORTED"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "TIMED_OUT"
    STATUS_TIMED_OUT = "TIMED_OUT"

    #: A constant which can be used with the status property of a ActionGroupDetails.
    #: This constant has a value of "PAUSED"
    STATUS_PAUSED = "PAUSED"

    def __init__(self, **kwargs):
        """
        Initializes a new ActionGroupDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.fleet_apps_management.models.FleetBasedActionGroupDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this ActionGroupDetails.
        :type display_name: str

        :param kind:
            The value to assign to the kind property of this ActionGroupDetails.
            Allowed values for this property are: "FLEET_USING_RUNBOOK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type kind: str

        :param product:
            The value to assign to the product property of this ActionGroupDetails.
        :type product: str

        :param lifecycle_operation:
            The value to assign to the lifecycle_operation property of this ActionGroupDetails.
        :type lifecycle_operation: str

        :param activity_id:
            The value to assign to the activity_id property of this ActionGroupDetails.
        :type activity_id: str

        :param status:
            The value to assign to the status property of this ActionGroupDetails.
            Allowed values for this property are: "ACCEPTED", "WAITING", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED", "SKIPPED", "IGNORED", "NOT_APPLICABLE", "ABORTED", "TIMED_OUT", "PAUSED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param time_started:
            The value to assign to the time_started property of this ActionGroupDetails.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this ActionGroupDetails.
        :type time_ended: datetime

        """
        self.swagger_types = {
            'display_name': 'str',
            'kind': 'str',
            'product': 'str',
            'lifecycle_operation': 'str',
            'activity_id': 'str',
            'status': 'str',
            'time_started': 'datetime',
            'time_ended': 'datetime'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'kind': 'kind',
            'product': 'product',
            'lifecycle_operation': 'lifecycleOperation',
            'activity_id': 'activityId',
            'status': 'status',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded'
        }
        self._display_name = None
        self._kind = None
        self._product = None
        self._lifecycle_operation = None
        self._activity_id = None
        self._status = None
        self._time_started = None
        self._time_ended = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['kind']

        if type == 'FLEET_USING_RUNBOOK':
            return 'FleetBasedActionGroupDetails'
        else:
            return 'ActionGroupDetails'

    @property
    def display_name(self):
        """
        Gets the display_name of this ActionGroupDetails.
        Name of the ActionGroup.


        :return: The display_name of this ActionGroupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ActionGroupDetails.
        Name of the ActionGroup.


        :param display_name: The display_name of this ActionGroupDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def kind(self):
        """
        **[Required]** Gets the kind of this ActionGroupDetails.
        Action Group kind

        Allowed values for this property are: "FLEET_USING_RUNBOOK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The kind of this ActionGroupDetails.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this ActionGroupDetails.
        Action Group kind


        :param kind: The kind of this ActionGroupDetails.
        :type: str
        """
        allowed_values = ["FLEET_USING_RUNBOOK"]
        if not value_allowed_none_or_none_sentinel(kind, allowed_values):
            kind = 'UNKNOWN_ENUM_VALUE'
        self._kind = kind

    @property
    def product(self):
        """
        Gets the product of this ActionGroupDetails.
        Product associated.
        Only applicable if actionGroup type is PRODUCT.


        :return: The product of this ActionGroupDetails.
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this ActionGroupDetails.
        Product associated.
        Only applicable if actionGroup type is PRODUCT.


        :param product: The product of this ActionGroupDetails.
        :type: str
        """
        self._product = product

    @property
    def lifecycle_operation(self):
        """
        Gets the lifecycle_operation of this ActionGroupDetails.
        LifeCycle Operation.


        :return: The lifecycle_operation of this ActionGroupDetails.
        :rtype: str
        """
        return self._lifecycle_operation

    @lifecycle_operation.setter
    def lifecycle_operation(self, lifecycle_operation):
        """
        Sets the lifecycle_operation of this ActionGroupDetails.
        LifeCycle Operation.


        :param lifecycle_operation: The lifecycle_operation of this ActionGroupDetails.
        :type: str
        """
        self._lifecycle_operation = lifecycle_operation

    @property
    def activity_id(self):
        """
        Gets the activity_id of this ActionGroupDetails.
        Unique producer Id at Action Group Level


        :return: The activity_id of this ActionGroupDetails.
        :rtype: str
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """
        Sets the activity_id of this ActionGroupDetails.
        Unique producer Id at Action Group Level


        :param activity_id: The activity_id of this ActionGroupDetails.
        :type: str
        """
        self._activity_id = activity_id

    @property
    def status(self):
        """
        Gets the status of this ActionGroupDetails.
        Status of the Job at Action Group Level.

        Allowed values for this property are: "ACCEPTED", "WAITING", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED", "SKIPPED", "IGNORED", "NOT_APPLICABLE", "ABORTED", "TIMED_OUT", "PAUSED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this ActionGroupDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ActionGroupDetails.
        Status of the Job at Action Group Level.


        :param status: The status of this ActionGroupDetails.
        :type: str
        """
        allowed_values = ["ACCEPTED", "WAITING", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED", "SKIPPED", "IGNORED", "NOT_APPLICABLE", "ABORTED", "TIMED_OUT", "PAUSED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def time_started(self):
        """
        Gets the time_started of this ActionGroupDetails.
        The time the Scheduler Job started. An RFC3339 formatted datetime string.


        :return: The time_started of this ActionGroupDetails.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this ActionGroupDetails.
        The time the Scheduler Job started. An RFC3339 formatted datetime string.


        :param time_started: The time_started of this ActionGroupDetails.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        Gets the time_ended of this ActionGroupDetails.
        The time the Scheduler Job ended. An RFC3339 formatted datetime string.


        :return: The time_ended of this ActionGroupDetails.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this ActionGroupDetails.
        The time the Scheduler Job ended. An RFC3339 formatted datetime string.


        :param time_ended: The time_ended of this ActionGroupDetails.
        :type: datetime
        """
        self._time_ended = time_ended

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
