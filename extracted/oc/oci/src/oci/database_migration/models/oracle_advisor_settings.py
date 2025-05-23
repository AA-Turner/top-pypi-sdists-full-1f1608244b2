# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OracleAdvisorSettings(object):
    """
    Details about Oracle Advisor Settings.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OracleAdvisorSettings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_skip_advisor:
            The value to assign to the is_skip_advisor property of this OracleAdvisorSettings.
        :type is_skip_advisor: bool

        :param is_ignore_errors:
            The value to assign to the is_ignore_errors property of this OracleAdvisorSettings.
        :type is_ignore_errors: bool

        """
        self.swagger_types = {
            'is_skip_advisor': 'bool',
            'is_ignore_errors': 'bool'
        }
        self.attribute_map = {
            'is_skip_advisor': 'isSkipAdvisor',
            'is_ignore_errors': 'isIgnoreErrors'
        }
        self._is_skip_advisor = None
        self._is_ignore_errors = None

    @property
    def is_skip_advisor(self):
        """
        Gets the is_skip_advisor of this OracleAdvisorSettings.
        True to skip the Pre-Migration Advisor execution. Default is false.


        :return: The is_skip_advisor of this OracleAdvisorSettings.
        :rtype: bool
        """
        return self._is_skip_advisor

    @is_skip_advisor.setter
    def is_skip_advisor(self, is_skip_advisor):
        """
        Sets the is_skip_advisor of this OracleAdvisorSettings.
        True to skip the Pre-Migration Advisor execution. Default is false.


        :param is_skip_advisor: The is_skip_advisor of this OracleAdvisorSettings.
        :type: bool
        """
        self._is_skip_advisor = is_skip_advisor

    @property
    def is_ignore_errors(self):
        """
        Gets the is_ignore_errors of this OracleAdvisorSettings.
        True to not interrupt migration execution due to Pre-Migration Advisor errors. Default is false.


        :return: The is_ignore_errors of this OracleAdvisorSettings.
        :rtype: bool
        """
        return self._is_ignore_errors

    @is_ignore_errors.setter
    def is_ignore_errors(self, is_ignore_errors):
        """
        Sets the is_ignore_errors of this OracleAdvisorSettings.
        True to not interrupt migration execution due to Pre-Migration Advisor errors. Default is false.


        :param is_ignore_errors: The is_ignore_errors of this OracleAdvisorSettings.
        :type: bool
        """
        self._is_ignore_errors = is_ignore_errors

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
