from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.assay_runs_bulk_create_error_response import AssayRunsBulkCreateErrorResponse
from ...models.assay_runs_bulk_create_request import AssayRunsBulkCreateRequest
from ...models.assay_runs_bulk_create_response import AssayRunsBulkCreateResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: AssayRunsBulkCreateRequest,
) -> Dict[str, Any]:
    url = "{}/assay-runs".format(client.base_url)

    headers: Dict[str, Any] = client.httpx_client.headers
    headers.update(client.get_headers())

    cookies: Dict[str, Any] = client.httpx_client.cookies
    cookies.update(client.get_cookies())

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[AssayRunsBulkCreateResponse, AssayRunsBulkCreateErrorResponse]]:
    if response.status_code == 200:
        response_200 = AssayRunsBulkCreateResponse.from_dict(response.json(), strict=False)

        return response_200
    if response.status_code == 400:
        response_400 = AssayRunsBulkCreateErrorResponse.from_dict(response.json(), strict=False)

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[AssayRunsBulkCreateResponse, AssayRunsBulkCreateErrorResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: AssayRunsBulkCreateRequest,
) -> Response[Union[AssayRunsBulkCreateResponse, AssayRunsBulkCreateErrorResponse]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = client.httpx_client.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: AssayRunsBulkCreateRequest,
) -> Optional[Union[AssayRunsBulkCreateResponse, AssayRunsBulkCreateErrorResponse]]:
    """ Create 1 or more runs. """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: AssayRunsBulkCreateRequest,
) -> Response[Union[AssayRunsBulkCreateResponse, AssayRunsBulkCreateErrorResponse]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: AssayRunsBulkCreateRequest,
) -> Optional[Union[AssayRunsBulkCreateResponse, AssayRunsBulkCreateErrorResponse]]:
    """ Create 1 or more runs. """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
