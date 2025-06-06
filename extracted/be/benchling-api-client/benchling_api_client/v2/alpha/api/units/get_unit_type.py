from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.unit_type import UnitType
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    unit_type_id: str,
) -> Dict[str, Any]:
    url = "{}/unit-types/{unit_type_id}".format(client.base_url, unit_type_id=unit_type_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[UnitType, None]]:
    if response.status_code == 200:
        response_200 = UnitType.from_dict(response.json(), strict=False)

        return response_200
    if response.status_code == 404:
        response_404 = None

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[UnitType, None]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    unit_type_id: str,
) -> Response[Union[UnitType, None]]:
    kwargs = _get_kwargs(
        client=client,
        unit_type_id=unit_type_id,
    )

    response = client.httpx_client.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    unit_type_id: str,
) -> Optional[Union[UnitType, None]]:
    """Get a specific unit type, including constituent units."""

    return sync_detailed(
        client=client,
        unit_type_id=unit_type_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    unit_type_id: str,
) -> Response[Union[UnitType, None]]:
    kwargs = _get_kwargs(
        client=client,
        unit_type_id=unit_type_id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    unit_type_id: str,
) -> Optional[Union[UnitType, None]]:
    """Get a specific unit type, including constituent units."""

    return (
        await asyncio_detailed(
            client=client,
            unit_type_id=unit_type_id,
        )
    ).parsed
