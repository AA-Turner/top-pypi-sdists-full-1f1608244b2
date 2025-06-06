# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from braintrust_api import Braintrust, AsyncBraintrust
from braintrust_api.pagination import SyncListObjects, AsyncListObjects
from braintrust_api.types.shared import Role

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Braintrust) -> None:
        role = client.roles.create(
            name="x",
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Braintrust) -> None:
        role = client.roles.create(
            name="x",
            description="description",
            member_permissions=[
                {
                    "permission": "create",
                    "restrict_object_type": "organization",
                }
            ],
            member_roles=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            org_name="org_name",
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Braintrust) -> None:
        response = client.roles.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = response.parse()
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Braintrust) -> None:
        with client.roles.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = response.parse()
            assert_matches_type(Role, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Braintrust) -> None:
        role = client.roles.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Braintrust) -> None:
        response = client.roles.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = response.parse()
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Braintrust) -> None:
        with client.roles.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = response.parse()
            assert_matches_type(Role, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role_id` but received ''"):
            client.roles.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Braintrust) -> None:
        role = client.roles.update(
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Braintrust) -> None:
        role = client.roles.update(
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            add_member_permissions=[
                {
                    "permission": "create",
                    "restrict_object_type": "organization",
                }
            ],
            add_member_roles=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            description="description",
            name="x",
            remove_member_permissions=[
                {
                    "permission": "create",
                    "restrict_object_type": "organization",
                }
            ],
            remove_member_roles=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Braintrust) -> None:
        response = client.roles.with_raw_response.update(
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = response.parse()
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Braintrust) -> None:
        with client.roles.with_streaming_response.update(
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = response.parse()
            assert_matches_type(Role, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role_id` but received ''"):
            client.roles.with_raw_response.update(
                role_id="",
            )

    @parametrize
    def test_method_list(self, client: Braintrust) -> None:
        role = client.roles.list()
        assert_matches_type(SyncListObjects[Role], role, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Braintrust) -> None:
        role = client.roles.list(
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            org_name="org_name",
            role_name="role_name",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncListObjects[Role], role, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Braintrust) -> None:
        response = client.roles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = response.parse()
        assert_matches_type(SyncListObjects[Role], role, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Braintrust) -> None:
        with client.roles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = response.parse()
            assert_matches_type(SyncListObjects[Role], role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Braintrust) -> None:
        role = client.roles.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Braintrust) -> None:
        response = client.roles.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = response.parse()
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Braintrust) -> None:
        with client.roles.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = response.parse()
            assert_matches_type(Role, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role_id` but received ''"):
            client.roles.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_replace(self, client: Braintrust) -> None:
        role = client.roles.replace(
            name="x",
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Braintrust) -> None:
        role = client.roles.replace(
            name="x",
            description="description",
            member_permissions=[
                {
                    "permission": "create",
                    "restrict_object_type": "organization",
                }
            ],
            member_roles=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            org_name="org_name",
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Braintrust) -> None:
        response = client.roles.with_raw_response.replace(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = response.parse()
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Braintrust) -> None:
        with client.roles.with_streaming_response.replace(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = response.parse()
            assert_matches_type(Role, role, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRoles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncBraintrust) -> None:
        role = await async_client.roles.create(
            name="x",
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBraintrust) -> None:
        role = await async_client.roles.create(
            name="x",
            description="description",
            member_permissions=[
                {
                    "permission": "create",
                    "restrict_object_type": "organization",
                }
            ],
            member_roles=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            org_name="org_name",
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.roles.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = await response.parse()
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBraintrust) -> None:
        async with async_client.roles.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = await response.parse()
            assert_matches_type(Role, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBraintrust) -> None:
        role = await async_client.roles.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.roles.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = await response.parse()
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        async with async_client.roles.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = await response.parse()
            assert_matches_type(Role, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role_id` but received ''"):
            await async_client.roles.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncBraintrust) -> None:
        role = await async_client.roles.update(
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBraintrust) -> None:
        role = await async_client.roles.update(
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            add_member_permissions=[
                {
                    "permission": "create",
                    "restrict_object_type": "organization",
                }
            ],
            add_member_roles=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            description="description",
            name="x",
            remove_member_permissions=[
                {
                    "permission": "create",
                    "restrict_object_type": "organization",
                }
            ],
            remove_member_roles=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.roles.with_raw_response.update(
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = await response.parse()
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBraintrust) -> None:
        async with async_client.roles.with_streaming_response.update(
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = await response.parse()
            assert_matches_type(Role, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role_id` but received ''"):
            await async_client.roles.with_raw_response.update(
                role_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBraintrust) -> None:
        role = await async_client.roles.list()
        assert_matches_type(AsyncListObjects[Role], role, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBraintrust) -> None:
        role = await async_client.roles.list(
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            org_name="org_name",
            role_name="role_name",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncListObjects[Role], role, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.roles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = await response.parse()
        assert_matches_type(AsyncListObjects[Role], role, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBraintrust) -> None:
        async with async_client.roles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = await response.parse()
            assert_matches_type(AsyncListObjects[Role], role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncBraintrust) -> None:
        role = await async_client.roles.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.roles.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = await response.parse()
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBraintrust) -> None:
        async with async_client.roles.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = await response.parse()
            assert_matches_type(Role, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role_id` but received ''"):
            await async_client.roles.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_replace(self, async_client: AsyncBraintrust) -> None:
        role = await async_client.roles.replace(
            name="x",
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncBraintrust) -> None:
        role = await async_client.roles.replace(
            name="x",
            description="description",
            member_permissions=[
                {
                    "permission": "create",
                    "restrict_object_type": "organization",
                }
            ],
            member_roles=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            org_name="org_name",
        )
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.roles.with_raw_response.replace(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = await response.parse()
        assert_matches_type(Role, role, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncBraintrust) -> None:
        async with async_client.roles.with_streaming_response.replace(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = await response.parse()
            assert_matches_type(Role, role, path=["response"])

        assert cast(Any, response.is_closed) is True
