from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.bad_request_error import BadRequestError
from ...models.box_schemas_list import BoxSchemasList
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    registry_id: str,
) -> Dict[str, Any]:
    url = "{}/registries/{registry_id}/box-schemas".format(client.base_url, registry_id=registry_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[BoxSchemasList, BadRequestError]]:
    if response.status_code == 200:
        response_200 = BoxSchemasList.from_dict(response.json(), strict=False)

        return response_200
    if response.status_code == 400:
        response_400 = BadRequestError.from_dict(response.json(), strict=False)

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[BoxSchemasList, BadRequestError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    registry_id: str,
) -> Response[Union[BoxSchemasList, BadRequestError]]:
    kwargs = _get_kwargs(
        client=client,
        registry_id=registry_id,
    )

    response = client.httpx_client.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    registry_id: str,
) -> Optional[Union[BoxSchemasList, BadRequestError]]:
    """ List box schemas by registry. Deprecated - use Schemas endpoints instead. """

    return sync_detailed(
        client=client,
        registry_id=registry_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    registry_id: str,
) -> Response[Union[BoxSchemasList, BadRequestError]]:
    kwargs = _get_kwargs(
        client=client,
        registry_id=registry_id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    registry_id: str,
) -> Optional[Union[BoxSchemasList, BadRequestError]]:
    """ List box schemas by registry. Deprecated - use Schemas endpoints instead. """

    return (
        await asyncio_detailed(
            client=client,
            registry_id=registry_id,
        )
    ).parsed
