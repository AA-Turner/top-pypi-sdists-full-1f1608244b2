# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20250228


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExecutionSummary(object):
    """
    A task associated with the Job.
    """

    #: A constant which can be used with the status property of a ExecutionSummary.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a ExecutionSummary.
    #: This constant has a value of "WAITING"
    STATUS_WAITING = "WAITING"

    #: A constant which can be used with the status property of a ExecutionSummary.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a ExecutionSummary.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a ExecutionSummary.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a ExecutionSummary.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    #: A constant which can be used with the status property of a ExecutionSummary.
    #: This constant has a value of "SKIPPED"
    STATUS_SKIPPED = "SKIPPED"

    #: A constant which can be used with the status property of a ExecutionSummary.
    #: This constant has a value of "IGNORED"
    STATUS_IGNORED = "IGNORED"

    #: A constant which can be used with the status property of a ExecutionSummary.
    #: This constant has a value of "NOT_APPLICABLE"
    STATUS_NOT_APPLICABLE = "NOT_APPLICABLE"

    #: A constant which can be used with the status property of a ExecutionSummary.
    #: This constant has a value of "ABORTED"
    STATUS_ABORTED = "ABORTED"

    #: A constant which can be used with the status property of a ExecutionSummary.
    #: This constant has a value of "TIMED_OUT"
    STATUS_TIMED_OUT = "TIMED_OUT"

    #: A constant which can be used with the status property of a ExecutionSummary.
    #: This constant has a value of "PAUSED"
    STATUS_PAUSED = "PAUSED"

    def __init__(self, **kwargs):
        """
        Initializes a new ExecutionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ExecutionSummary.
        :type id: str

        :param task_record_id:
            The value to assign to the task_record_id property of this ExecutionSummary.
        :type task_record_id: str

        :param step_name:
            The value to assign to the step_name property of this ExecutionSummary.
        :type step_name: str

        :param process_reference_id:
            The value to assign to the process_reference_id property of this ExecutionSummary.
        :type process_reference_id: str

        :param sequence:
            The value to assign to the sequence property of this ExecutionSummary.
        :type sequence: str

        :param status:
            The value to assign to the status property of this ExecutionSummary.
            Allowed values for this property are: "ACCEPTED", "WAITING", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED", "SKIPPED", "IGNORED", "NOT_APPLICABLE", "ABORTED", "TIMED_OUT", "PAUSED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param target_id:
            The value to assign to the target_id property of this ExecutionSummary.
        :type target_id: str

        :param time_started:
            The value to assign to the time_started property of this ExecutionSummary.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this ExecutionSummary.
        :type time_ended: datetime

        :param is_rollback_task:
            The value to assign to the is_rollback_task property of this ExecutionSummary.
        :type is_rollback_task: bool

        :param description:
            The value to assign to the description property of this ExecutionSummary.
        :type description: str

        :param resource_id:
            The value to assign to the resource_id property of this ExecutionSummary.
        :type resource_id: str

        :param is_retry_exceeded:
            The value to assign to the is_retry_exceeded property of this ExecutionSummary.
        :type is_retry_exceeded: bool

        :param system_tags:
            The value to assign to the system_tags property of this ExecutionSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'task_record_id': 'str',
            'step_name': 'str',
            'process_reference_id': 'str',
            'sequence': 'str',
            'status': 'str',
            'target_id': 'str',
            'time_started': 'datetime',
            'time_ended': 'datetime',
            'is_rollback_task': 'bool',
            'description': 'str',
            'resource_id': 'str',
            'is_retry_exceeded': 'bool',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'task_record_id': 'taskRecordId',
            'step_name': 'stepName',
            'process_reference_id': 'processReferenceId',
            'sequence': 'sequence',
            'status': 'status',
            'target_id': 'targetId',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded',
            'is_rollback_task': 'isRollbackTask',
            'description': 'description',
            'resource_id': 'resourceId',
            'is_retry_exceeded': 'isRetryExceeded',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._task_record_id = None
        self._step_name = None
        self._process_reference_id = None
        self._sequence = None
        self._status = None
        self._target_id = None
        self._time_started = None
        self._time_ended = None
        self._is_rollback_task = None
        self._description = None
        self._resource_id = None
        self._is_retry_exceeded = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ExecutionSummary.
        Unique Id associated with the task execution.


        :return: The id of this ExecutionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExecutionSummary.
        Unique Id associated with the task execution.


        :param id: The id of this ExecutionSummary.
        :type: str
        """
        self._id = id

    @property
    def task_record_id(self):
        """
        Gets the task_record_id of this ExecutionSummary.
        The OCID of taskRecord.


        :return: The task_record_id of this ExecutionSummary.
        :rtype: str
        """
        return self._task_record_id

    @task_record_id.setter
    def task_record_id(self, task_record_id):
        """
        Sets the task_record_id of this ExecutionSummary.
        The OCID of taskRecord.


        :param task_record_id: The task_record_id of this ExecutionSummary.
        :type: str
        """
        self._task_record_id = task_record_id

    @property
    def step_name(self):
        """
        Gets the step_name of this ExecutionSummary.
        Name of the Step.


        :return: The step_name of this ExecutionSummary.
        :rtype: str
        """
        return self._step_name

    @step_name.setter
    def step_name(self, step_name):
        """
        Sets the step_name of this ExecutionSummary.
        Name of the Step.


        :param step_name: The step_name of this ExecutionSummary.
        :type: str
        """
        self._step_name = step_name

    @property
    def process_reference_id(self):
        """
        Gets the process_reference_id of this ExecutionSummary.
        Unique process-reference identifier returned by the execution client.
        In some cases, this can be a runcommand OCID.


        :return: The process_reference_id of this ExecutionSummary.
        :rtype: str
        """
        return self._process_reference_id

    @process_reference_id.setter
    def process_reference_id(self, process_reference_id):
        """
        Sets the process_reference_id of this ExecutionSummary.
        Unique process-reference identifier returned by the execution client.
        In some cases, this can be a runcommand OCID.


        :param process_reference_id: The process_reference_id of this ExecutionSummary.
        :type: str
        """
        self._process_reference_id = process_reference_id

    @property
    def sequence(self):
        """
        Gets the sequence of this ExecutionSummary.
        The sequence of the task.


        :return: The sequence of this ExecutionSummary.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """
        Sets the sequence of this ExecutionSummary.
        The sequence of the task.


        :param sequence: The sequence of this ExecutionSummary.
        :type: str
        """
        self._sequence = sequence

    @property
    def status(self):
        """
        **[Required]** Gets the status of this ExecutionSummary.
        Status of the Task.

        Allowed values for this property are: "ACCEPTED", "WAITING", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED", "SKIPPED", "IGNORED", "NOT_APPLICABLE", "ABORTED", "TIMED_OUT", "PAUSED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this ExecutionSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ExecutionSummary.
        Status of the Task.


        :param status: The status of this ExecutionSummary.
        :type: str
        """
        allowed_values = ["ACCEPTED", "WAITING", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED", "SKIPPED", "IGNORED", "NOT_APPLICABLE", "ABORTED", "TIMED_OUT", "PAUSED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def target_id(self):
        """
        Gets the target_id of this ExecutionSummary.
        Target associated with the execution.


        :return: The target_id of this ExecutionSummary.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this ExecutionSummary.
        Target associated with the execution.


        :param target_id: The target_id of this ExecutionSummary.
        :type: str
        """
        self._target_id = target_id

    @property
    def time_started(self):
        """
        Gets the time_started of this ExecutionSummary.
        The time the task started. An RFC3339 formatted datetime string.


        :return: The time_started of this ExecutionSummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this ExecutionSummary.
        The time the task started. An RFC3339 formatted datetime string.


        :param time_started: The time_started of this ExecutionSummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        Gets the time_ended of this ExecutionSummary.
        The time the task ended. An RFC3339 formatted datetime string.


        :return: The time_ended of this ExecutionSummary.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this ExecutionSummary.
        The time the task ended. An RFC3339 formatted datetime string.


        :param time_ended: The time_ended of this ExecutionSummary.
        :type: datetime
        """
        self._time_ended = time_ended

    @property
    def is_rollback_task(self):
        """
        Gets the is_rollback_task of this ExecutionSummary.
        Is this a rollback task?


        :return: The is_rollback_task of this ExecutionSummary.
        :rtype: bool
        """
        return self._is_rollback_task

    @is_rollback_task.setter
    def is_rollback_task(self, is_rollback_task):
        """
        Sets the is_rollback_task of this ExecutionSummary.
        Is this a rollback task?


        :param is_rollback_task: The is_rollback_task of this ExecutionSummary.
        :type: bool
        """
        self._is_rollback_task = is_rollback_task

    @property
    def description(self):
        """
        Gets the description of this ExecutionSummary.
        Description of the Execution status.
        If there are any errors, this can also include a short error message.


        :return: The description of this ExecutionSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ExecutionSummary.
        Description of the Execution status.
        If there are any errors, this can also include a short error message.


        :param description: The description of this ExecutionSummary.
        :type: str
        """
        self._description = description

    @property
    def resource_id(self):
        """
        Gets the resource_id of this ExecutionSummary.
        Resource Identifier associated with the Work Request.


        :return: The resource_id of this ExecutionSummary.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this ExecutionSummary.
        Resource Identifier associated with the Work Request.


        :param resource_id: The resource_id of this ExecutionSummary.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def is_retry_exceeded(self):
        """
        Gets the is_retry_exceeded of this ExecutionSummary.
        An attribute which tells if further retries are allowed for the task on failure.


        :return: The is_retry_exceeded of this ExecutionSummary.
        :rtype: bool
        """
        return self._is_retry_exceeded

    @is_retry_exceeded.setter
    def is_retry_exceeded(self, is_retry_exceeded):
        """
        Sets the is_retry_exceeded of this ExecutionSummary.
        An attribute which tells if further retries are allowed for the task on failure.


        :param is_retry_exceeded: The is_retry_exceeded of this ExecutionSummary.
        :type: bool
        """
        self._is_retry_exceeded = is_retry_exceeded

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ExecutionSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this ExecutionSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ExecutionSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this ExecutionSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
