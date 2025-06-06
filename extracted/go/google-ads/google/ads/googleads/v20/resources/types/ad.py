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

from google.ads.googleads.v20.common.types import ad_type_infos
from google.ads.googleads.v20.common.types import custom_parameter
from google.ads.googleads.v20.common.types import final_app_url
from google.ads.googleads.v20.common.types import url_collection
from google.ads.googleads.v20.enums.types import ad_type
from google.ads.googleads.v20.enums.types import device
from google.ads.googleads.v20.enums.types import system_managed_entity_source


__protobuf__ = proto.module(
    package="google.ads.googleads.v20.resources",
    marshal="google.ads.googleads.v20",
    manifest={
        "Ad",
    },
)


class Ad(proto.Message):
    r"""An ad.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        resource_name (str):
            Immutable. The resource name of the ad. Ad resource names
            have the form:

            ``customers/{customer_id}/ads/{ad_id}``
        id (int):
            Output only. The ID of the ad.

            This field is a member of `oneof`_ ``_id``.
        final_urls (MutableSequence[str]):
            The list of possible final URLs after all
            cross-domain redirects for the ad.
        final_app_urls (MutableSequence[google.ads.googleads.v20.common.types.FinalAppUrl]):
            A list of final app URLs that will be used on
            mobile if the user has the specific app
            installed.
        final_mobile_urls (MutableSequence[str]):
            The list of possible final mobile URLs after
            all cross-domain redirects for the ad.
        tracking_url_template (str):
            The URL template for constructing a tracking
            URL.

            This field is a member of `oneof`_ ``_tracking_url_template``.
        final_url_suffix (str):
            The suffix to use when constructing a final
            URL.

            This field is a member of `oneof`_ ``_final_url_suffix``.
        url_custom_parameters (MutableSequence[google.ads.googleads.v20.common.types.CustomParameter]):
            The list of mappings that can be used to substitute custom
            parameter tags in a ``tracking_url_template``,
            ``final_urls``, or ``mobile_final_urls``. For mutates, use
            url custom parameter operations.
        display_url (str):
            The URL that appears in the ad description
            for some ad formats.

            This field is a member of `oneof`_ ``_display_url``.
        type_ (google.ads.googleads.v20.enums.types.AdTypeEnum.AdType):
            Output only. The type of ad.
        added_by_google_ads (bool):
            Output only. Indicates if this ad was
            automatically added by Google Ads and not by a
            user. For example, this could happen when ads
            are automatically created as suggestions for new
            ads based on knowledge of how existing ads are
            performing.

            This field is a member of `oneof`_ ``_added_by_google_ads``.
        device_preference (google.ads.googleads.v20.enums.types.DeviceEnum.Device):
            The device preference for the ad. You can
            only specify a preference for mobile devices.
            When this preference is set the ad will be
            preferred over other ads when being displayed on
            a mobile device. The ad can still be displayed
            on other device types, for example, if no other
            ads are available. If unspecified (no device
            preference), all devices are targeted. This is
            only supported by some ad types.
        url_collections (MutableSequence[google.ads.googleads.v20.common.types.UrlCollection]):
            Additional URLs for the ad that are tagged
            with a unique identifier that can be referenced
            from other fields in the ad.
        name (str):
            Immutable. The name of the ad. This is only
            used to be able to identify the ad. It does not
            need to be unique and does not affect the served
            ad. The name field is currently only supported
            for DisplayUploadAd, ImageAd,
            ShoppingComparisonListingAd and VideoAd.

            This field is a member of `oneof`_ ``_name``.
        system_managed_resource_source (google.ads.googleads.v20.enums.types.SystemManagedResourceSourceEnum.SystemManagedResourceSource):
            Output only. If this ad is system managed,
            then this field will indicate the source. This
            field is read-only.
        text_ad (google.ads.googleads.v20.common.types.TextAdInfo):
            Immutable. Details pertaining to a text ad.

            This field is a member of `oneof`_ ``ad_data``.
        expanded_text_ad (google.ads.googleads.v20.common.types.ExpandedTextAdInfo):
            Details pertaining to an expanded text ad.

            This field is a member of `oneof`_ ``ad_data``.
        call_ad (google.ads.googleads.v20.common.types.CallAdInfo):
            Details pertaining to a call ad.

            This field is a member of `oneof`_ ``ad_data``.
        expanded_dynamic_search_ad (google.ads.googleads.v20.common.types.ExpandedDynamicSearchAdInfo):
            Immutable. Details pertaining to an Expanded Dynamic Search
            Ad. This type of ad has its headline, final URLs, and
            display URL auto-generated at serving time according to
            domain name specific information provided by
            ``dynamic_search_ads_setting`` linked at the campaign level.

            This field is a member of `oneof`_ ``ad_data``.
        hotel_ad (google.ads.googleads.v20.common.types.HotelAdInfo):
            Details pertaining to a hotel ad.

            This field is a member of `oneof`_ ``ad_data``.
        shopping_smart_ad (google.ads.googleads.v20.common.types.ShoppingSmartAdInfo):
            Details pertaining to a Smart Shopping ad.

            This field is a member of `oneof`_ ``ad_data``.
        shopping_product_ad (google.ads.googleads.v20.common.types.ShoppingProductAdInfo):
            Details pertaining to a Shopping product ad.

            This field is a member of `oneof`_ ``ad_data``.
        image_ad (google.ads.googleads.v20.common.types.ImageAdInfo):
            Immutable. Details pertaining to an Image ad.

            This field is a member of `oneof`_ ``ad_data``.
        video_ad (google.ads.googleads.v20.common.types.VideoAdInfo):
            Details pertaining to a Video ad.

            This field is a member of `oneof`_ ``ad_data``.
        video_responsive_ad (google.ads.googleads.v20.common.types.VideoResponsiveAdInfo):
            Details pertaining to a Video responsive ad.

            This field is a member of `oneof`_ ``ad_data``.
        responsive_search_ad (google.ads.googleads.v20.common.types.ResponsiveSearchAdInfo):
            Details pertaining to a responsive search ad.

            This field is a member of `oneof`_ ``ad_data``.
        legacy_responsive_display_ad (google.ads.googleads.v20.common.types.LegacyResponsiveDisplayAdInfo):
            Details pertaining to a legacy responsive
            display ad.

            This field is a member of `oneof`_ ``ad_data``.
        app_ad (google.ads.googleads.v20.common.types.AppAdInfo):
            Details pertaining to an app ad.

            This field is a member of `oneof`_ ``ad_data``.
        legacy_app_install_ad (google.ads.googleads.v20.common.types.LegacyAppInstallAdInfo):
            Immutable. Details pertaining to a legacy app
            install ad.

            This field is a member of `oneof`_ ``ad_data``.
        responsive_display_ad (google.ads.googleads.v20.common.types.ResponsiveDisplayAdInfo):
            Details pertaining to a responsive display
            ad.

            This field is a member of `oneof`_ ``ad_data``.
        local_ad (google.ads.googleads.v20.common.types.LocalAdInfo):
            Details pertaining to a local ad.

            This field is a member of `oneof`_ ``ad_data``.
        display_upload_ad (google.ads.googleads.v20.common.types.DisplayUploadAdInfo):
            Details pertaining to a display upload ad.

            This field is a member of `oneof`_ ``ad_data``.
        app_engagement_ad (google.ads.googleads.v20.common.types.AppEngagementAdInfo):
            Details pertaining to an app engagement ad.

            This field is a member of `oneof`_ ``ad_data``.
        shopping_comparison_listing_ad (google.ads.googleads.v20.common.types.ShoppingComparisonListingAdInfo):
            Details pertaining to a Shopping Comparison
            Listing ad.

            This field is a member of `oneof`_ ``ad_data``.
        smart_campaign_ad (google.ads.googleads.v20.common.types.SmartCampaignAdInfo):
            Details pertaining to a Smart campaign ad.

            This field is a member of `oneof`_ ``ad_data``.
        app_pre_registration_ad (google.ads.googleads.v20.common.types.AppPreRegistrationAdInfo):
            Details pertaining to an app pre-registration
            ad.

            This field is a member of `oneof`_ ``ad_data``.
        demand_gen_multi_asset_ad (google.ads.googleads.v20.common.types.DemandGenMultiAssetAdInfo):
            Details pertaining to a Demand Gen multi
            asset ad.

            This field is a member of `oneof`_ ``ad_data``.
        demand_gen_carousel_ad (google.ads.googleads.v20.common.types.DemandGenCarouselAdInfo):
            Details pertaining to a Demand Gen carousel
            ad.

            This field is a member of `oneof`_ ``ad_data``.
        demand_gen_video_responsive_ad (google.ads.googleads.v20.common.types.DemandGenVideoResponsiveAdInfo):
            Details pertaining to a Demand Gen video
            responsive ad.

            This field is a member of `oneof`_ ``ad_data``.
        demand_gen_product_ad (google.ads.googleads.v20.common.types.DemandGenProductAdInfo):
            Details pertaining to a Demand Gen product
            ad.

            This field is a member of `oneof`_ ``ad_data``.
        travel_ad (google.ads.googleads.v20.common.types.TravelAdInfo):
            Details pertaining to a travel ad.

            This field is a member of `oneof`_ ``ad_data``.
    """

    resource_name: str = proto.Field(
        proto.STRING,
        number=37,
    )
    id: int = proto.Field(
        proto.INT64,
        number=40,
        optional=True,
    )
    final_urls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=41,
    )
    final_app_urls: MutableSequence[final_app_url.FinalAppUrl] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=35,
            message=final_app_url.FinalAppUrl,
        )
    )
    final_mobile_urls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=42,
    )
    tracking_url_template: str = proto.Field(
        proto.STRING,
        number=43,
        optional=True,
    )
    final_url_suffix: str = proto.Field(
        proto.STRING,
        number=44,
        optional=True,
    )
    url_custom_parameters: MutableSequence[custom_parameter.CustomParameter] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=10,
            message=custom_parameter.CustomParameter,
        )
    )
    display_url: str = proto.Field(
        proto.STRING,
        number=45,
        optional=True,
    )
    type_: ad_type.AdTypeEnum.AdType = proto.Field(
        proto.ENUM,
        number=5,
        enum=ad_type.AdTypeEnum.AdType,
    )
    added_by_google_ads: bool = proto.Field(
        proto.BOOL,
        number=46,
        optional=True,
    )
    device_preference: device.DeviceEnum.Device = proto.Field(
        proto.ENUM,
        number=20,
        enum=device.DeviceEnum.Device,
    )
    url_collections: MutableSequence[url_collection.UrlCollection] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=26,
            message=url_collection.UrlCollection,
        )
    )
    name: str = proto.Field(
        proto.STRING,
        number=47,
        optional=True,
    )
    system_managed_resource_source: (
        system_managed_entity_source.SystemManagedResourceSourceEnum.SystemManagedResourceSource
    ) = proto.Field(
        proto.ENUM,
        number=27,
        enum=system_managed_entity_source.SystemManagedResourceSourceEnum.SystemManagedResourceSource,
    )
    text_ad: ad_type_infos.TextAdInfo = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="ad_data",
        message=ad_type_infos.TextAdInfo,
    )
    expanded_text_ad: ad_type_infos.ExpandedTextAdInfo = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="ad_data",
        message=ad_type_infos.ExpandedTextAdInfo,
    )
    call_ad: ad_type_infos.CallAdInfo = proto.Field(
        proto.MESSAGE,
        number=49,
        oneof="ad_data",
        message=ad_type_infos.CallAdInfo,
    )
    expanded_dynamic_search_ad: ad_type_infos.ExpandedDynamicSearchAdInfo = (
        proto.Field(
            proto.MESSAGE,
            number=14,
            oneof="ad_data",
            message=ad_type_infos.ExpandedDynamicSearchAdInfo,
        )
    )
    hotel_ad: ad_type_infos.HotelAdInfo = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="ad_data",
        message=ad_type_infos.HotelAdInfo,
    )
    shopping_smart_ad: ad_type_infos.ShoppingSmartAdInfo = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="ad_data",
        message=ad_type_infos.ShoppingSmartAdInfo,
    )
    shopping_product_ad: ad_type_infos.ShoppingProductAdInfo = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="ad_data",
        message=ad_type_infos.ShoppingProductAdInfo,
    )
    image_ad: ad_type_infos.ImageAdInfo = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="ad_data",
        message=ad_type_infos.ImageAdInfo,
    )
    video_ad: ad_type_infos.VideoAdInfo = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="ad_data",
        message=ad_type_infos.VideoAdInfo,
    )
    video_responsive_ad: ad_type_infos.VideoResponsiveAdInfo = proto.Field(
        proto.MESSAGE,
        number=39,
        oneof="ad_data",
        message=ad_type_infos.VideoResponsiveAdInfo,
    )
    responsive_search_ad: ad_type_infos.ResponsiveSearchAdInfo = proto.Field(
        proto.MESSAGE,
        number=25,
        oneof="ad_data",
        message=ad_type_infos.ResponsiveSearchAdInfo,
    )
    legacy_responsive_display_ad: (
        ad_type_infos.LegacyResponsiveDisplayAdInfo
    ) = proto.Field(
        proto.MESSAGE,
        number=28,
        oneof="ad_data",
        message=ad_type_infos.LegacyResponsiveDisplayAdInfo,
    )
    app_ad: ad_type_infos.AppAdInfo = proto.Field(
        proto.MESSAGE,
        number=29,
        oneof="ad_data",
        message=ad_type_infos.AppAdInfo,
    )
    legacy_app_install_ad: ad_type_infos.LegacyAppInstallAdInfo = proto.Field(
        proto.MESSAGE,
        number=30,
        oneof="ad_data",
        message=ad_type_infos.LegacyAppInstallAdInfo,
    )
    responsive_display_ad: ad_type_infos.ResponsiveDisplayAdInfo = proto.Field(
        proto.MESSAGE,
        number=31,
        oneof="ad_data",
        message=ad_type_infos.ResponsiveDisplayAdInfo,
    )
    local_ad: ad_type_infos.LocalAdInfo = proto.Field(
        proto.MESSAGE,
        number=32,
        oneof="ad_data",
        message=ad_type_infos.LocalAdInfo,
    )
    display_upload_ad: ad_type_infos.DisplayUploadAdInfo = proto.Field(
        proto.MESSAGE,
        number=33,
        oneof="ad_data",
        message=ad_type_infos.DisplayUploadAdInfo,
    )
    app_engagement_ad: ad_type_infos.AppEngagementAdInfo = proto.Field(
        proto.MESSAGE,
        number=34,
        oneof="ad_data",
        message=ad_type_infos.AppEngagementAdInfo,
    )
    shopping_comparison_listing_ad: (
        ad_type_infos.ShoppingComparisonListingAdInfo
    ) = proto.Field(
        proto.MESSAGE,
        number=36,
        oneof="ad_data",
        message=ad_type_infos.ShoppingComparisonListingAdInfo,
    )
    smart_campaign_ad: ad_type_infos.SmartCampaignAdInfo = proto.Field(
        proto.MESSAGE,
        number=48,
        oneof="ad_data",
        message=ad_type_infos.SmartCampaignAdInfo,
    )
    app_pre_registration_ad: ad_type_infos.AppPreRegistrationAdInfo = (
        proto.Field(
            proto.MESSAGE,
            number=50,
            oneof="ad_data",
            message=ad_type_infos.AppPreRegistrationAdInfo,
        )
    )
    demand_gen_multi_asset_ad: ad_type_infos.DemandGenMultiAssetAdInfo = (
        proto.Field(
            proto.MESSAGE,
            number=62,
            oneof="ad_data",
            message=ad_type_infos.DemandGenMultiAssetAdInfo,
        )
    )
    demand_gen_carousel_ad: ad_type_infos.DemandGenCarouselAdInfo = proto.Field(
        proto.MESSAGE,
        number=63,
        oneof="ad_data",
        message=ad_type_infos.DemandGenCarouselAdInfo,
    )
    demand_gen_video_responsive_ad: (
        ad_type_infos.DemandGenVideoResponsiveAdInfo
    ) = proto.Field(
        proto.MESSAGE,
        number=64,
        oneof="ad_data",
        message=ad_type_infos.DemandGenVideoResponsiveAdInfo,
    )
    demand_gen_product_ad: ad_type_infos.DemandGenProductAdInfo = proto.Field(
        proto.MESSAGE,
        number=61,
        oneof="ad_data",
        message=ad_type_infos.DemandGenProductAdInfo,
    )
    travel_ad: ad_type_infos.TravelAdInfo = proto.Field(
        proto.MESSAGE,
        number=54,
        oneof="ad_data",
        message=ad_type_infos.TravelAdInfo,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
