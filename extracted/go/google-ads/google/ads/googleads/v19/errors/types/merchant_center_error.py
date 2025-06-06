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
    package="google.ads.googleads.v19.errors",
    marshal="google.ads.googleads.v19",
    manifest={
        "MerchantCenterErrorEnum",
    },
)


class MerchantCenterErrorEnum(proto.Message):
    r"""Container for enum describing possible merchant center
    errors.

    """

    class MerchantCenterError(proto.Enum):
        r"""Enum describing Merchant Center errors.

        Values:
            UNSPECIFIED (0):
                Enum unspecified.
            UNKNOWN (1):
                The received error code is not known in this
                version.
            MERCHANT_ID_CANNOT_BE_ACCESSED (2):
                Merchant ID is either not found or not linked
                to the Google Ads customer.
            CUSTOMER_NOT_ALLOWED_FOR_SHOPPING_PERFORMANCE_MAX (3):
                Customer not allowlisted for Shopping in
                Performance Max Campaign.
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        MERCHANT_ID_CANNOT_BE_ACCESSED = 2
        CUSTOMER_NOT_ALLOWED_FOR_SHOPPING_PERFORMANCE_MAX = 3


__all__ = tuple(sorted(__protobuf__.manifest))
