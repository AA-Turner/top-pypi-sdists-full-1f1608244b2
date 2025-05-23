# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20250228

from .user_action_details import UserActionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ActionGroupBasedUserActionDetails(UserActionDetails):
    """
    Details for a user action to be performed on an action group.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ActionGroupBasedUserActionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_apps_management.models.ActionGroupBasedUserActionDetails.level` attribute
        of this class is ``ACTION_GROUP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param level:
            The value to assign to the level property of this ActionGroupBasedUserActionDetails.
            Allowed values for this property are: "ACTION_GROUP", "STEP_NAME"
        :type level: str

        :param action:
            The value to assign to the action property of this ActionGroupBasedUserActionDetails.
            Allowed values for this property are: "RETRY", "RESUME", "IGNORE", "ABORT"
        :type action: str

        :param action_group_id:
            The value to assign to the action_group_id property of this ActionGroupBasedUserActionDetails.
        :type action_group_id: str

        """
        self.swagger_types = {
            'level': 'str',
            'action': 'str',
            'action_group_id': 'str'
        }
        self.attribute_map = {
            'level': 'level',
            'action': 'action',
            'action_group_id': 'actionGroupId'
        }
        self._level = None
        self._action = None
        self._action_group_id = None
        self._level = 'ACTION_GROUP'

    @property
    def action_group_id(self):
        """
        **[Required]** Gets the action_group_id of this ActionGroupBasedUserActionDetails.
        Unique identifier for the action group.


        :return: The action_group_id of this ActionGroupBasedUserActionDetails.
        :rtype: str
        """
        return self._action_group_id

    @action_group_id.setter
    def action_group_id(self, action_group_id):
        """
        Sets the action_group_id of this ActionGroupBasedUserActionDetails.
        Unique identifier for the action group.


        :param action_group_id: The action_group_id of this ActionGroupBasedUserActionDetails.
        :type: str
        """
        self._action_group_id = action_group_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
