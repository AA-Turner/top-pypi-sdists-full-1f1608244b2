# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import make_request_options
from .....types.radar.http.locations import device_type_get_params
from .....types.radar.http.locations.device_type_get_response import DeviceTypeGetResponse

__all__ = ["DeviceTypeResource", "AsyncDeviceTypeResource"]


class DeviceTypeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeviceTypeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DeviceTypeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeviceTypeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DeviceTypeResourceWithStreamingResponse(self)

    def get(
        self,
        device_type: Literal["DESKTOP", "MOBILE", "OTHER"],
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
        browser_family: List[Literal["CHROME", "EDGE", "FIREFOX", "SAFARI"]] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]]
        | NotGiven = NOT_GIVEN,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeviceTypeGetResponse:
        """
        Retrieves the top locations, by HTTP requests, of the requested device type.

        Args:
          device_type: Device type.

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          bot_class: Filters results by bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          browser_family: Filters results by browser family.

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          http_protocol: Filters results by HTTP protocol (HTTP vs. HTTPS).

          http_version: Filters results by HTTP version.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          limit: Limits the number of objects returned in the response.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          os: Filters results by operating system.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_type:
            raise ValueError(f"Expected a non-empty value for `device_type` but received {device_type!r}")
        return self._get(
            f"/radar/http/top/locations/device_type/{device_type}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "bot_class": bot_class,
                        "browser_family": browser_family,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "http_protocol": http_protocol,
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "limit": limit,
                        "location": location,
                        "name": name,
                        "os": os,
                        "tls_version": tls_version,
                    },
                    device_type_get_params.DeviceTypeGetParams,
                ),
                post_parser=ResultWrapper[DeviceTypeGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[DeviceTypeGetResponse], ResultWrapper[DeviceTypeGetResponse]),
        )


class AsyncDeviceTypeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeviceTypeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeviceTypeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeviceTypeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDeviceTypeResourceWithStreamingResponse(self)

    async def get(
        self,
        device_type: Literal["DESKTOP", "MOBILE", "OTHER"],
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        bot_class: List[Literal["LIKELY_AUTOMATED", "LIKELY_HUMAN"]] | NotGiven = NOT_GIVEN,
        browser_family: List[Literal["CHROME", "EDGE", "FIREFOX", "SAFARI"]] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        http_protocol: List[Literal["HTTP", "HTTPS"]] | NotGiven = NOT_GIVEN,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        os: List[Literal["WINDOWS", "MACOSX", "IOS", "ANDROID", "CHROMEOS", "LINUX", "SMART_TV"]]
        | NotGiven = NOT_GIVEN,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3", "TLSvQUIC"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeviceTypeGetResponse:
        """
        Retrieves the top locations, by HTTP requests, of the requested device type.

        Args:
          device_type: Device type.

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          bot_class: Filters results by bot class. Refer to
              [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).

          browser_family: Filters results by browser family.

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          http_protocol: Filters results by HTTP protocol (HTTP vs. HTTPS).

          http_version: Filters results by HTTP version.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          limit: Limits the number of objects returned in the response.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          os: Filters results by operating system.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_type:
            raise ValueError(f"Expected a non-empty value for `device_type` but received {device_type!r}")
        return await self._get(
            f"/radar/http/top/locations/device_type/{device_type}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asn": asn,
                        "bot_class": bot_class,
                        "browser_family": browser_family,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "http_protocol": http_protocol,
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "limit": limit,
                        "location": location,
                        "name": name,
                        "os": os,
                        "tls_version": tls_version,
                    },
                    device_type_get_params.DeviceTypeGetParams,
                ),
                post_parser=ResultWrapper[DeviceTypeGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[DeviceTypeGetResponse], ResultWrapper[DeviceTypeGetResponse]),
        )


class DeviceTypeResourceWithRawResponse:
    def __init__(self, device_type: DeviceTypeResource) -> None:
        self._device_type = device_type

        self.get = to_raw_response_wrapper(
            device_type.get,
        )


class AsyncDeviceTypeResourceWithRawResponse:
    def __init__(self, device_type: AsyncDeviceTypeResource) -> None:
        self._device_type = device_type

        self.get = async_to_raw_response_wrapper(
            device_type.get,
        )


class DeviceTypeResourceWithStreamingResponse:
    def __init__(self, device_type: DeviceTypeResource) -> None:
        self._device_type = device_type

        self.get = to_streamed_response_wrapper(
            device_type.get,
        )


class AsyncDeviceTypeResourceWithStreamingResponse:
    def __init__(self, device_type: AsyncDeviceTypeResource) -> None:
        self._device_type = device_type

        self.get = async_to_streamed_response_wrapper(
            device_type.get,
        )
