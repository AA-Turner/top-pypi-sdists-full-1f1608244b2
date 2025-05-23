# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20250228


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Task(object):
    """
    The details of the task
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Task object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param step_name:
            The value to assign to the step_name property of this Task.
        :type step_name: str

        :param task_record_details:
            The value to assign to the task_record_details property of this Task.
        :type task_record_details: oci.fleet_apps_management.models.AssociatedTaskDetails

        :param step_properties:
            The value to assign to the step_properties property of this Task.
        :type step_properties: oci.fleet_apps_management.models.ComponentProperties

        :param output_variable_mappings:
            The value to assign to the output_variable_mappings property of this Task.
        :type output_variable_mappings: list[oci.fleet_apps_management.models.OutputVariableMapping]

        """
        self.swagger_types = {
            'step_name': 'str',
            'task_record_details': 'AssociatedTaskDetails',
            'step_properties': 'ComponentProperties',
            'output_variable_mappings': 'list[OutputVariableMapping]'
        }
        self.attribute_map = {
            'step_name': 'stepName',
            'task_record_details': 'taskRecordDetails',
            'step_properties': 'stepProperties',
            'output_variable_mappings': 'outputVariableMappings'
        }
        self._step_name = None
        self._task_record_details = None
        self._step_properties = None
        self._output_variable_mappings = None

    @property
    def step_name(self):
        """
        **[Required]** Gets the step_name of this Task.
        The name of the task step.


        :return: The step_name of this Task.
        :rtype: str
        """
        return self._step_name

    @step_name.setter
    def step_name(self, step_name):
        """
        Sets the step_name of this Task.
        The name of the task step.


        :param step_name: The step_name of this Task.
        :type: str
        """
        self._step_name = step_name

    @property
    def task_record_details(self):
        """
        **[Required]** Gets the task_record_details of this Task.

        :return: The task_record_details of this Task.
        :rtype: oci.fleet_apps_management.models.AssociatedTaskDetails
        """
        return self._task_record_details

    @task_record_details.setter
    def task_record_details(self, task_record_details):
        """
        Sets the task_record_details of this Task.

        :param task_record_details: The task_record_details of this Task.
        :type: oci.fleet_apps_management.models.AssociatedTaskDetails
        """
        self._task_record_details = task_record_details

    @property
    def step_properties(self):
        """
        Gets the step_properties of this Task.

        :return: The step_properties of this Task.
        :rtype: oci.fleet_apps_management.models.ComponentProperties
        """
        return self._step_properties

    @step_properties.setter
    def step_properties(self, step_properties):
        """
        Sets the step_properties of this Task.

        :param step_properties: The step_properties of this Task.
        :type: oci.fleet_apps_management.models.ComponentProperties
        """
        self._step_properties = step_properties

    @property
    def output_variable_mappings(self):
        """
        Gets the output_variable_mappings of this Task.
        Mapping output variables of previous tasks to the input variables of the current task.


        :return: The output_variable_mappings of this Task.
        :rtype: list[oci.fleet_apps_management.models.OutputVariableMapping]
        """
        return self._output_variable_mappings

    @output_variable_mappings.setter
    def output_variable_mappings(self, output_variable_mappings):
        """
        Sets the output_variable_mappings of this Task.
        Mapping output variables of previous tasks to the input variables of the current task.


        :param output_variable_mappings: The output_variable_mappings of this Task.
        :type: list[oci.fleet_apps_management.models.OutputVariableMapping]
        """
        self._output_variable_mappings = output_variable_mappings

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
