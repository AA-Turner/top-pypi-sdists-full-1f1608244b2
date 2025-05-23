# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.email.security.top.tlds import SpoofGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpoof:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        spoof = client.radar.email.security.top.tlds.spoof.get(
            spoof="SPOOF",
        )
        assert_matches_type(SpoofGetResponse, spoof, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        spoof = client.radar.email.security.top.tlds.spoof.get(
            spoof="SPOOF",
            arc=["PASS"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            dkim=["PASS"],
            dmarc=["PASS"],
            format="JSON",
            limit=5,
            name=["main_series"],
            spf=["PASS"],
            tld_category="CLASSIC",
            tls_version=["TLSv1_0"],
        )
        assert_matches_type(SpoofGetResponse, spoof, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.radar.email.security.top.tlds.spoof.with_raw_response.get(
            spoof="SPOOF",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spoof = response.parse()
        assert_matches_type(SpoofGetResponse, spoof, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.radar.email.security.top.tlds.spoof.with_streaming_response.get(
            spoof="SPOOF",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spoof = response.parse()
            assert_matches_type(SpoofGetResponse, spoof, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSpoof:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        spoof = await async_client.radar.email.security.top.tlds.spoof.get(
            spoof="SPOOF",
        )
        assert_matches_type(SpoofGetResponse, spoof, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        spoof = await async_client.radar.email.security.top.tlds.spoof.get(
            spoof="SPOOF",
            arc=["PASS"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            dkim=["PASS"],
            dmarc=["PASS"],
            format="JSON",
            limit=5,
            name=["main_series"],
            spf=["PASS"],
            tld_category="CLASSIC",
            tls_version=["TLSv1_0"],
        )
        assert_matches_type(SpoofGetResponse, spoof, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.email.security.top.tlds.spoof.with_raw_response.get(
            spoof="SPOOF",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spoof = await response.parse()
        assert_matches_type(SpoofGetResponse, spoof, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.email.security.top.tlds.spoof.with_streaming_response.get(
            spoof="SPOOF",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spoof = await response.parse()
            assert_matches_type(SpoofGetResponse, spoof, path=["response"])

        assert cast(Any, response.is_closed) is True
