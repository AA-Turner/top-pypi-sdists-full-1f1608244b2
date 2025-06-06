# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SkipBulkResponderExecutionDetails(object):
    """
    Details of responders to skip execution.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SkipBulkResponderExecutionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param responder_execution_ids:
            The value to assign to the responder_execution_ids property of this SkipBulkResponderExecutionDetails.
        :type responder_execution_ids: list[str]

        """
        self.swagger_types = {
            'responder_execution_ids': 'list[str]'
        }
        self.attribute_map = {
            'responder_execution_ids': 'responderExecutionIds'
        }
        self._responder_execution_ids = None

    @property
    def responder_execution_ids(self):
        """
        **[Required]** Gets the responder_execution_ids of this SkipBulkResponderExecutionDetails.
        List of responder execution IDs to skip execution


        :return: The responder_execution_ids of this SkipBulkResponderExecutionDetails.
        :rtype: list[str]
        """
        return self._responder_execution_ids

    @responder_execution_ids.setter
    def responder_execution_ids(self, responder_execution_ids):
        """
        Sets the responder_execution_ids of this SkipBulkResponderExecutionDetails.
        List of responder execution IDs to skip execution


        :param responder_execution_ids: The responder_execution_ids of this SkipBulkResponderExecutionDetails.
        :type: list[str]
        """
        self._responder_execution_ids = responder_execution_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
