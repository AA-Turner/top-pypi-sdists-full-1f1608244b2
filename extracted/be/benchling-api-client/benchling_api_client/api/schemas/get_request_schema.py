from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.not_found_error import NotFoundError
from ...models.request_schema import RequestSchema
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    schema_id: str,
) -> Dict[str, Any]:
    url = "{}/request-schemas/{schema_id}".format(client.base_url, schema_id=schema_id)

    headers: Dict[str, Any] = client.httpx_client.headers
    headers.update(client.get_headers())

    cookies: Dict[str, Any] = client.httpx_client.cookies
    cookies.update(client.get_cookies())

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[RequestSchema, None, NotFoundError]]:
    if response.status_code == 200:
        response_200 = RequestSchema.from_dict(response.json(), strict=False)

        return response_200
    if response.status_code == 400:
        response_400 = None

        return response_400
    if response.status_code == 404:
        response_404 = NotFoundError.from_dict(response.json(), strict=False)

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[RequestSchema, None, NotFoundError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    schema_id: str,
) -> Response[Union[RequestSchema, None, NotFoundError]]:
    kwargs = _get_kwargs(
        client=client,
        schema_id=schema_id,
    )

    response = client.httpx_client.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    schema_id: str,
) -> Optional[Union[RequestSchema, None, NotFoundError]]:
    """ Get a Legacy Request schema by ID """

    return sync_detailed(
        client=client,
        schema_id=schema_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    schema_id: str,
) -> Response[Union[RequestSchema, None, NotFoundError]]:
    kwargs = _get_kwargs(
        client=client,
        schema_id=schema_id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    schema_id: str,
) -> Optional[Union[RequestSchema, None, NotFoundError]]:
    """ Get a Legacy Request schema by ID """

    return (
        await asyncio_detailed(
            client=client,
            schema_id=schema_id,
        )
    ).parsed
