from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.not_found_error import NotFoundError
from ...models.plate_schema import PlateSchema
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    schema_id: str,
) -> Dict[str, Any]:
    url = "{}/plate-schemas/{schema_id}".format(client.base_url, schema_id=schema_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[PlateSchema, None, NotFoundError]]:
    if response.status_code == 200:
        response_200 = PlateSchema.from_dict(response.json(), strict=False)

        return response_200
    if response.status_code == 400:
        response_400 = None

        return response_400
    if response.status_code == 404:
        response_404 = NotFoundError.from_dict(response.json(), strict=False)

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[PlateSchema, None, NotFoundError]]:
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
) -> Response[Union[PlateSchema, None, NotFoundError]]:
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
) -> Optional[Union[PlateSchema, None, NotFoundError]]:
    """ Get a plate schema by ID """

    return sync_detailed(
        client=client,
        schema_id=schema_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    schema_id: str,
) -> Response[Union[PlateSchema, None, NotFoundError]]:
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
) -> Optional[Union[PlateSchema, None, NotFoundError]]:
    """ Get a plate schema by ID """

    return (
        await asyncio_detailed(
            client=client,
            schema_id=schema_id,
        )
    ).parsed
