# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations


import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v20.errors",
    marshal="google.ads.googleads.v20",
    manifest={
        "CustomerLifecycleGoalErrorEnum",
    },
)


class CustomerLifecycleGoalErrorEnum(proto.Message):
    r"""Container for enum describing possible customer lifecycle
    goal errors.

    """

    class CustomerLifecycleGoalError(proto.Enum):
        r"""Enum describing possible customer lifecycle goal errors.

        Values:
            UNSPECIFIED (0):
                Enum unspecified.
            UNKNOWN (1):
                The received error code is not known in this
                version.
            CUSTOMER_ACQUISITION_VALUE_MISSING (2):
                CustomerLifecycleGoal.customer_acquisition_goal_value_settings.value
                must be set.
            CUSTOMER_ACQUISITION_INVALID_VALUE (3):
                CustomerLifecycleGoal.customer_acquisition_goal_value_settings.value
                must be no less than 0.01.
            CUSTOMER_ACQUISITION_INVALID_HIGH_LIFETIME_VALUE (4):
                CustomerLifecycleGoal.customer_acquisition_goal_value_settings.high_lifetime_value
                must be no less than 0.01. Also, to set this field,
                CustomerLifecycleGoal.customer_acquisition_goal_value_settings.value
                must also be present, and high_lifetime_value must be
                greater than value.
            CUSTOMER_ACQUISITION_VALUE_CANNOT_BE_CLEARED (5):
                CustomerLifecycleGoal.customer_acquisition_goal_value_settings.value
                cannot be cleared. This value would have no effect as long
                as none of your campaigns adopt the customer acquisitiong
                goal.
            CUSTOMER_ACQUISITION_HIGH_LIFETIME_VALUE_CANNOT_BE_CLEARED (6):
                CustomerLifecycleGoal.customer_acquisition_goal_value_settings.high_lifetime_value
                cannot be cleared. This value would have no effect as long
                as none of your campaigns adopt the high value optimization
                of customer acquisitiong goal.
            INVALID_EXISTING_USER_LIST (7):
                Found invalid value in
                CustomerLifecycleGoal.lifecycle_goal_customer_definition_settings.existing_user_lists.
                The userlist must be accessible, active and belong to one of
                the following types: CRM_BASED, RULE_BASED, REMARKETING.
            INVALID_HIGH_LIFETIME_VALUE_USER_LIST (8):
                Found invalid value in
                CustomerLifecycleGoal.lifecycle_goal_customer_definition_settings.high_lifetime_value_user_lists.
                The userlist must be accessible, active and belong to one of
                the following types: CRM_BASED, RULE_BASED, REMARKETING.
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        CUSTOMER_ACQUISITION_VALUE_MISSING = 2
        CUSTOMER_ACQUISITION_INVALID_VALUE = 3
        CUSTOMER_ACQUISITION_INVALID_HIGH_LIFETIME_VALUE = 4
        CUSTOMER_ACQUISITION_VALUE_CANNOT_BE_CLEARED = 5
        CUSTOMER_ACQUISITION_HIGH_LIFETIME_VALUE_CANNOT_BE_CLEARED = 6
        INVALID_EXISTING_USER_LIST = 7
        INVALID_HIGH_LIFETIME_VALUE_USER_LIST = 8


__all__ = tuple(sorted(__protobuf__.manifest))
