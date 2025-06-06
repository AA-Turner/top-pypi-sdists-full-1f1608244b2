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

from typing import MutableSequence

import proto  # type: ignore

from google.ads.googleads.v20.enums.types import gender_type
from google.ads.googleads.v20.enums.types import income_range_type
from google.ads.googleads.v20.enums.types import parental_status_type


__protobuf__ = proto.module(
    package="google.ads.googleads.v20.common",
    marshal="google.ads.googleads.v20",
    manifest={
        "AudienceDimension",
        "AudienceExclusionDimension",
        "ExclusionSegment",
        "AgeDimension",
        "AgeSegment",
        "GenderDimension",
        "HouseholdIncomeDimension",
        "ParentalStatusDimension",
        "AudienceSegmentDimension",
        "AudienceSegment",
        "UserListSegment",
        "UserInterestSegment",
        "LifeEventSegment",
        "DetailedDemographicSegment",
        "CustomAudienceSegment",
    },
)


class AudienceDimension(proto.Message):
    r"""Positive dimension specifying user's audience.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        age (google.ads.googleads.v20.common.types.AgeDimension):
            Dimension specifying users by their age.

            This field is a member of `oneof`_ ``dimension``.
        gender (google.ads.googleads.v20.common.types.GenderDimension):
            Dimension specifying users by their gender.

            This field is a member of `oneof`_ ``dimension``.
        household_income (google.ads.googleads.v20.common.types.HouseholdIncomeDimension):
            Dimension specifying users by their household
            income.

            This field is a member of `oneof`_ ``dimension``.
        parental_status (google.ads.googleads.v20.common.types.ParentalStatusDimension):
            Dimension specifying users by their parental
            status.

            This field is a member of `oneof`_ ``dimension``.
        audience_segments (google.ads.googleads.v20.common.types.AudienceSegmentDimension):
            Dimension specifying users by their
            membership in other audience segments.

            This field is a member of `oneof`_ ``dimension``.
    """

    age: "AgeDimension" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="dimension",
        message="AgeDimension",
    )
    gender: "GenderDimension" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="dimension",
        message="GenderDimension",
    )
    household_income: "HouseholdIncomeDimension" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="dimension",
        message="HouseholdIncomeDimension",
    )
    parental_status: "ParentalStatusDimension" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="dimension",
        message="ParentalStatusDimension",
    )
    audience_segments: "AudienceSegmentDimension" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="dimension",
        message="AudienceSegmentDimension",
    )


class AudienceExclusionDimension(proto.Message):
    r"""Negative dimension specifying users to exclude from the
    audience.

    Attributes:
        exclusions (MutableSequence[google.ads.googleads.v20.common.types.ExclusionSegment]):
            Audience segment to be excluded.
    """

    exclusions: MutableSequence["ExclusionSegment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ExclusionSegment",
    )


class ExclusionSegment(proto.Message):
    r"""An audience segment to be excluded from an audience.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        user_list (google.ads.googleads.v20.common.types.UserListSegment):
            User list segment to be excluded.

            This field is a member of `oneof`_ ``segment``.
    """

    user_list: "UserListSegment" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="segment",
        message="UserListSegment",
    )


class AgeDimension(proto.Message):
    r"""Dimension specifying users by their age.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        age_ranges (MutableSequence[google.ads.googleads.v20.common.types.AgeSegment]):
            Contiguous age range to be included in the
            dimension.
        include_undetermined (bool):
            Include users whose age is not determined.

            This field is a member of `oneof`_ ``_include_undetermined``.
    """

    age_ranges: MutableSequence["AgeSegment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AgeSegment",
    )
    include_undetermined: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )


class AgeSegment(proto.Message):
    r"""Contiguous age range.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        min_age (int):
            Minimum age to include. A minimum age must be
            specified and must be at least 18. Allowed
            values are 18, 25, 35, 45, 55, and 65.

            This field is a member of `oneof`_ ``_min_age``.
        max_age (int):
            Maximum age to include. A maximum age need not be specified.
            If specified, max_age must be greater than min_age, and
            allowed values are 24, 34, 44, 54, and 64.

            This field is a member of `oneof`_ ``_max_age``.
    """

    min_age: int = proto.Field(
        proto.INT32,
        number=1,
        optional=True,
    )
    max_age: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )


class GenderDimension(proto.Message):
    r"""Dimension specifying users by their gender.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        genders (MutableSequence[google.ads.googleads.v20.enums.types.GenderTypeEnum.GenderType]):
            Included gender demographic segments.
        include_undetermined (bool):
            Include users whose gender is not determined.

            This field is a member of `oneof`_ ``_include_undetermined``.
    """

    genders: MutableSequence[gender_type.GenderTypeEnum.GenderType] = (
        proto.RepeatedField(
            proto.ENUM,
            number=1,
            enum=gender_type.GenderTypeEnum.GenderType,
        )
    )
    include_undetermined: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )


class HouseholdIncomeDimension(proto.Message):
    r"""Dimension specifying users by their household income.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        income_ranges (MutableSequence[google.ads.googleads.v20.enums.types.IncomeRangeTypeEnum.IncomeRangeType]):
            Included household income demographic
            segments.
        include_undetermined (bool):
            Include users whose household income is not
            determined.

            This field is a member of `oneof`_ ``_include_undetermined``.
    """

    income_ranges: MutableSequence[
        income_range_type.IncomeRangeTypeEnum.IncomeRangeType
    ] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum=income_range_type.IncomeRangeTypeEnum.IncomeRangeType,
    )
    include_undetermined: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )


class ParentalStatusDimension(proto.Message):
    r"""Dimension specifying users by their parental status.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parental_statuses (MutableSequence[google.ads.googleads.v20.enums.types.ParentalStatusTypeEnum.ParentalStatusType]):
            Included parental status demographic
            segments.
        include_undetermined (bool):
            Include users whose parental status is
            undetermined.

            This field is a member of `oneof`_ ``_include_undetermined``.
    """

    parental_statuses: MutableSequence[
        parental_status_type.ParentalStatusTypeEnum.ParentalStatusType
    ] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum=parental_status_type.ParentalStatusTypeEnum.ParentalStatusType,
    )
    include_undetermined: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )


class AudienceSegmentDimension(proto.Message):
    r"""Dimension specifying users by their membership in other
    audience segments.

    Attributes:
        segments (MutableSequence[google.ads.googleads.v20.common.types.AudienceSegment]):
            Included audience segments. Users are
            included if they belong to at least one segment.
    """

    segments: MutableSequence["AudienceSegment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AudienceSegment",
    )


class AudienceSegment(proto.Message):
    r"""Positive audience segment.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        user_list (google.ads.googleads.v20.common.types.UserListSegment):
            User list segment.

            This field is a member of `oneof`_ ``segment``.
        user_interest (google.ads.googleads.v20.common.types.UserInterestSegment):
            Affinity or In-market segment.

            This field is a member of `oneof`_ ``segment``.
        life_event (google.ads.googleads.v20.common.types.LifeEventSegment):
            Live-event audience segment.

            This field is a member of `oneof`_ ``segment``.
        detailed_demographic (google.ads.googleads.v20.common.types.DetailedDemographicSegment):
            Detailed demographic segment.

            This field is a member of `oneof`_ ``segment``.
        custom_audience (google.ads.googleads.v20.common.types.CustomAudienceSegment):
            Custom audience segment.

            This field is a member of `oneof`_ ``segment``.
    """

    user_list: "UserListSegment" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="segment",
        message="UserListSegment",
    )
    user_interest: "UserInterestSegment" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="segment",
        message="UserInterestSegment",
    )
    life_event: "LifeEventSegment" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="segment",
        message="LifeEventSegment",
    )
    detailed_demographic: "DetailedDemographicSegment" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="segment",
        message="DetailedDemographicSegment",
    )
    custom_audience: "CustomAudienceSegment" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="segment",
        message="CustomAudienceSegment",
    )


class UserListSegment(proto.Message):
    r"""User list segment.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        user_list (str):
            The user list resource.

            This field is a member of `oneof`_ ``_user_list``.
    """

    user_list: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )


class UserInterestSegment(proto.Message):
    r"""User interest segment.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        user_interest_category (str):
            The user interest resource.

            This field is a member of `oneof`_ ``_user_interest_category``.
    """

    user_interest_category: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )


class LifeEventSegment(proto.Message):
    r"""Live event segment.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        life_event (str):
            The life event resource.

            This field is a member of `oneof`_ ``_life_event``.
    """

    life_event: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )


class DetailedDemographicSegment(proto.Message):
    r"""Detailed demographic segment.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        detailed_demographic (str):
            The detailed demographic resource.

            This field is a member of `oneof`_ ``_detailed_demographic``.
    """

    detailed_demographic: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )


class CustomAudienceSegment(proto.Message):
    r"""Custom audience segment.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        custom_audience (str):
            The custom audience resource.

            This field is a member of `oneof`_ ``_custom_audience``.
    """

    custom_audience: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
