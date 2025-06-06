# coding: utf-8

"""
    Anyscale API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from anyscale_client.configuration import Configuration


class ProductionJobStateTransition(object):
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
        'state_transitioned_at': 'datetime',
        'current_state': 'HaJobStates',
        'goal_state': 'HaJobGoalStates',
        'error': 'str',
        'operation_message': 'str',
        'cluster_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'state_transitioned_at': 'state_transitioned_at',
        'current_state': 'current_state',
        'goal_state': 'goal_state',
        'error': 'error',
        'operation_message': 'operation_message',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, id=None, state_transitioned_at=None, current_state=None, goal_state=None, error=None, operation_message=None, cluster_id=None, local_vars_configuration=None):  # noqa: E501
        """ProductionJobStateTransition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._state_transitioned_at = None
        self._current_state = None
        self._goal_state = None
        self._error = None
        self._operation_message = None
        self._cluster_id = None
        self.discriminator = None

        self.id = id
        self.state_transitioned_at = state_transitioned_at
        self.current_state = current_state
        if goal_state is not None:
            self.goal_state = goal_state
        if error is not None:
            self.error = error
        if operation_message is not None:
            self.operation_message = operation_message
        if cluster_id is not None:
            self.cluster_id = cluster_id

    @property
    def id(self):
        """Gets the id of this ProductionJobStateTransition.  # noqa: E501

        The id of this job state transition  # noqa: E501

        :return: The id of this ProductionJobStateTransition.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProductionJobStateTransition.

        The id of this job state transition  # noqa: E501

        :param id: The id of this ProductionJobStateTransition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def state_transitioned_at(self):
        """Gets the state_transitioned_at of this ProductionJobStateTransition.  # noqa: E501

        The last time the state of this job was updated  # noqa: E501

        :return: The state_transitioned_at of this ProductionJobStateTransition.  # noqa: E501
        :rtype: datetime
        """
        return self._state_transitioned_at

    @state_transitioned_at.setter
    def state_transitioned_at(self, state_transitioned_at):
        """Sets the state_transitioned_at of this ProductionJobStateTransition.

        The last time the state of this job was updated  # noqa: E501

        :param state_transitioned_at: The state_transitioned_at of this ProductionJobStateTransition.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and state_transitioned_at is None:  # noqa: E501
            raise ValueError("Invalid value for `state_transitioned_at`, must not be `None`")  # noqa: E501

        self._state_transitioned_at = state_transitioned_at

    @property
    def current_state(self):
        """Gets the current_state of this ProductionJobStateTransition.  # noqa: E501

        The current state of the job  # noqa: E501

        :return: The current_state of this ProductionJobStateTransition.  # noqa: E501
        :rtype: HaJobStates
        """
        return self._current_state

    @current_state.setter
    def current_state(self, current_state):
        """Sets the current_state of this ProductionJobStateTransition.

        The current state of the job  # noqa: E501

        :param current_state: The current_state of this ProductionJobStateTransition.  # noqa: E501
        :type: HaJobStates
        """
        if self.local_vars_configuration.client_side_validation and current_state is None:  # noqa: E501
            raise ValueError("Invalid value for `current_state`, must not be `None`")  # noqa: E501

        self._current_state = current_state

    @property
    def goal_state(self):
        """Gets the goal_state of this ProductionJobStateTransition.  # noqa: E501

        The goal state of the job  # noqa: E501

        :return: The goal_state of this ProductionJobStateTransition.  # noqa: E501
        :rtype: HaJobGoalStates
        """
        return self._goal_state

    @goal_state.setter
    def goal_state(self, goal_state):
        """Sets the goal_state of this ProductionJobStateTransition.

        The goal state of the job  # noqa: E501

        :param goal_state: The goal_state of this ProductionJobStateTransition.  # noqa: E501
        :type: HaJobGoalStates
        """

        self._goal_state = goal_state

    @property
    def error(self):
        """Gets the error of this ProductionJobStateTransition.  # noqa: E501

        An error message that occurred in this job state transition  # noqa: E501

        :return: The error of this ProductionJobStateTransition.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ProductionJobStateTransition.

        An error message that occurred in this job state transition  # noqa: E501

        :param error: The error of this ProductionJobStateTransition.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def operation_message(self):
        """Gets the operation_message of this ProductionJobStateTransition.  # noqa: E501

        The logging message for this job state transition  # noqa: E501

        :return: The operation_message of this ProductionJobStateTransition.  # noqa: E501
        :rtype: str
        """
        return self._operation_message

    @operation_message.setter
    def operation_message(self, operation_message):
        """Sets the operation_message of this ProductionJobStateTransition.

        The logging message for this job state transition  # noqa: E501

        :param operation_message: The operation_message of this ProductionJobStateTransition.  # noqa: E501
        :type: str
        """

        self._operation_message = operation_message

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ProductionJobStateTransition.  # noqa: E501

        The id of the cluster the job is running on  # noqa: E501

        :return: The cluster_id of this ProductionJobStateTransition.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ProductionJobStateTransition.

        The id of the cluster the job is running on  # noqa: E501

        :param cluster_id: The cluster_id of this ProductionJobStateTransition.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

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
        if not isinstance(other, ProductionJobStateTransition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductionJobStateTransition):
            return True

        return self.to_dict() != other.to_dict()
