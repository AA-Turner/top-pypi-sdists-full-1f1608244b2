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
    package="google.ads.googleads.v20.enums",
    marshal="google.ads.googleads.v20",
    manifest={
        "ClickTypeEnum",
    },
)


class ClickTypeEnum(proto.Message):
    r"""Container for enumeration of Google Ads click types."""

    class ClickType(proto.Enum):
        r"""Enumerates Google Ads click types.

        Values:
            UNSPECIFIED (0):
                Not specified.
            UNKNOWN (1):
                The value is unknown in this version.
            APP_DEEPLINK (2):
                App engagement ad deep link.
            BREADCRUMBS (3):
                Breadcrumbs.
            BROADBAND_PLAN (4):
                Broadband Plan.
            CALL_TRACKING (5):
                Manually dialed phone calls.
            CALLS (6):
                Phone calls.
            CLICK_ON_ENGAGEMENT_AD (7):
                Click on engagement ad.
            GET_DIRECTIONS (8):
                Driving direction.
            LOCATION_EXPANSION (9):
                Get location details.
            LOCATION_FORMAT_CALL (10):
                Call.
            LOCATION_FORMAT_DIRECTIONS (11):
                Directions.
            LOCATION_FORMAT_IMAGE (12):
                Image(s).
            LOCATION_FORMAT_LANDING_PAGE (13):
                Go to landing page.
            LOCATION_FORMAT_MAP (14):
                Map.
            LOCATION_FORMAT_STORE_INFO (15):
                Go to store info.
            LOCATION_FORMAT_TEXT (16):
                Text.
            MOBILE_CALL_TRACKING (17):
                Mobile phone calls.
            OFFER_PRINTS (18):
                Print offer.
            OTHER (19):
                Other.
            PRODUCT_EXTENSION_CLICKS (20):
                Product plusbox offer.
            PRODUCT_LISTING_AD_CLICKS (21):
                Shopping - Product - Online.
            SITELINKS (22):
                Sitelink.
            STORE_LOCATOR (23):
                Show nearby locations.
            URL_CLICKS (25):
                Headline.
            VIDEO_APP_STORE_CLICKS (26):
                App store.
            VIDEO_CALL_TO_ACTION_CLICKS (27):
                Call-to-Action overlay.
            VIDEO_CARD_ACTION_HEADLINE_CLICKS (28):
                Cards.
            VIDEO_END_CAP_CLICKS (29):
                End cap.
            VIDEO_WEBSITE_CLICKS (30):
                Website.
            VISUAL_SITELINKS (31):
                Visual Sitelinks.
            WIRELESS_PLAN (32):
                Wireless Plan.
            PRODUCT_LISTING_AD_LOCAL (33):
                Shopping - Product - Local.
            PRODUCT_LISTING_AD_MULTICHANNEL_LOCAL (34):
                Shopping - Product - MultiChannel Local.
            PRODUCT_LISTING_AD_MULTICHANNEL_ONLINE (35):
                Shopping - Product - MultiChannel Online.
            PRODUCT_LISTING_ADS_COUPON (36):
                Shopping - Product - Coupon.
            PRODUCT_LISTING_AD_TRANSACTABLE (37):
                Shopping - Product - Sell on Google.
            PRODUCT_AD_APP_DEEPLINK (38):
                Shopping - Product - App engagement ad deep
                link.
            SHOWCASE_AD_CATEGORY_LINK (39):
                Shopping - Showcase - Category.
            SHOWCASE_AD_LOCAL_STOREFRONT_LINK (40):
                Shopping - Showcase - Local storefront.
            SHOWCASE_AD_ONLINE_PRODUCT_LINK (42):
                Shopping - Showcase - Online product.
            SHOWCASE_AD_LOCAL_PRODUCT_LINK (43):
                Shopping - Showcase - Local product.
            PROMOTION_EXTENSION (44):
                Promotion Extension.
            SWIPEABLE_GALLERY_AD_HEADLINE (45):
                Ad Headline.
            SWIPEABLE_GALLERY_AD_SWIPES (46):
                Swipes.
            SWIPEABLE_GALLERY_AD_SEE_MORE (47):
                See More.
            SWIPEABLE_GALLERY_AD_SITELINK_ONE (48):
                Sitelink 1.
            SWIPEABLE_GALLERY_AD_SITELINK_TWO (49):
                Sitelink 2.
            SWIPEABLE_GALLERY_AD_SITELINK_THREE (50):
                Sitelink 3.
            SWIPEABLE_GALLERY_AD_SITELINK_FOUR (51):
                Sitelink 4.
            SWIPEABLE_GALLERY_AD_SITELINK_FIVE (52):
                Sitelink 5.
            HOTEL_PRICE (53):
                Hotel price.
            PRICE_EXTENSION (54):
                Price Extension.
            HOTEL_BOOK_ON_GOOGLE_ROOM_SELECTION (55):
                Book on Google hotel room selection.
            SHOPPING_COMPARISON_LISTING (56):
                Shopping - Comparison Listing.
            CROSS_NETWORK (57):
                Cross-network. From Performance Max and
                Discovery Campaigns.
            AD_IMAGE (58):
                AD Images.
            TRAVEL_ASSETS (59):
                Travel Feed Assets.
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        APP_DEEPLINK = 2
        BREADCRUMBS = 3
        BROADBAND_PLAN = 4
        CALL_TRACKING = 5
        CALLS = 6
        CLICK_ON_ENGAGEMENT_AD = 7
        GET_DIRECTIONS = 8
        LOCATION_EXPANSION = 9
        LOCATION_FORMAT_CALL = 10
        LOCATION_FORMAT_DIRECTIONS = 11
        LOCATION_FORMAT_IMAGE = 12
        LOCATION_FORMAT_LANDING_PAGE = 13
        LOCATION_FORMAT_MAP = 14
        LOCATION_FORMAT_STORE_INFO = 15
        LOCATION_FORMAT_TEXT = 16
        MOBILE_CALL_TRACKING = 17
        OFFER_PRINTS = 18
        OTHER = 19
        PRODUCT_EXTENSION_CLICKS = 20
        PRODUCT_LISTING_AD_CLICKS = 21
        SITELINKS = 22
        STORE_LOCATOR = 23
        URL_CLICKS = 25
        VIDEO_APP_STORE_CLICKS = 26
        VIDEO_CALL_TO_ACTION_CLICKS = 27
        VIDEO_CARD_ACTION_HEADLINE_CLICKS = 28
        VIDEO_END_CAP_CLICKS = 29
        VIDEO_WEBSITE_CLICKS = 30
        VISUAL_SITELINKS = 31
        WIRELESS_PLAN = 32
        PRODUCT_LISTING_AD_LOCAL = 33
        PRODUCT_LISTING_AD_MULTICHANNEL_LOCAL = 34
        PRODUCT_LISTING_AD_MULTICHANNEL_ONLINE = 35
        PRODUCT_LISTING_ADS_COUPON = 36
        PRODUCT_LISTING_AD_TRANSACTABLE = 37
        PRODUCT_AD_APP_DEEPLINK = 38
        SHOWCASE_AD_CATEGORY_LINK = 39
        SHOWCASE_AD_LOCAL_STOREFRONT_LINK = 40
        SHOWCASE_AD_ONLINE_PRODUCT_LINK = 42
        SHOWCASE_AD_LOCAL_PRODUCT_LINK = 43
        PROMOTION_EXTENSION = 44
        SWIPEABLE_GALLERY_AD_HEADLINE = 45
        SWIPEABLE_GALLERY_AD_SWIPES = 46
        SWIPEABLE_GALLERY_AD_SEE_MORE = 47
        SWIPEABLE_GALLERY_AD_SITELINK_ONE = 48
        SWIPEABLE_GALLERY_AD_SITELINK_TWO = 49
        SWIPEABLE_GALLERY_AD_SITELINK_THREE = 50
        SWIPEABLE_GALLERY_AD_SITELINK_FOUR = 51
        SWIPEABLE_GALLERY_AD_SITELINK_FIVE = 52
        HOTEL_PRICE = 53
        PRICE_EXTENSION = 54
        HOTEL_BOOK_ON_GOOGLE_ROOM_SELECTION = 55
        SHOPPING_COMPARISON_LISTING = 56
        CROSS_NETWORK = 57
        AD_IMAGE = 58
        TRAVEL_ASSETS = 59


__all__ = tuple(sorted(__protobuf__.manifest))
