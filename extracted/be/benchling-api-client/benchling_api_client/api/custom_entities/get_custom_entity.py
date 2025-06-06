from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.bad_request_error import BadRequestError
from ...models.custom_entity import CustomEntity
from ...types import Response, UNSET, Unset


def _get_kwargs(
    *,
    client: Client,
    custom_entity_id: str,
    returning: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/custom-entities/{custom_entity_id}".format(client.base_url, custom_entity_id=custom_entity_id)

    headers: Dict[str, Any] = client.httpx_client.headers
    headers.update(client.get_headers())

    cookies: Dict[str, Any] = client.httpx_client.cookies
    cookies.update(client.get_cookies())

    params: Dict[str, Any] = {}
    if not isinstance(returning, Unset) and returning is not None:
        params["returning"] = returning

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[CustomEntity, BadRequestError]]:
    if response.status_code == 200:
        response_200 = CustomEntity.from_dict(response.json(), strict=False)

        return response_200
    if response.status_code == 400:
        response_400 = BadRequestError.from_dict(response.json(), strict=False)

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[CustomEntity, BadRequestError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    custom_entity_id: str,
    returning: Union[Unset, str] = UNSET,
) -> Response[Union[CustomEntity, BadRequestError]]:
    kwargs = _get_kwargs(
        client=client,
        custom_entity_id=custom_entity_id,
        returning=returning,
    )

    response = client.httpx_client.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    custom_entity_id: str,
    returning: Union[Unset, str] = UNSET,
) -> Optional[Union[CustomEntity, BadRequestError]]:
    """ Get a custom entity """

    return sync_detailed(
        client=client,
        custom_entity_id=custom_entity_id,
        returning=returning,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    custom_entity_id: str,
    returning: Union[Unset, str] = UNSET,
) -> Response[Union[CustomEntity, BadRequestError]]:
    kwargs = _get_kwargs(
        client=client,
        custom_entity_id=custom_entity_id,
        returning=returning,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    custom_entity_id: str,
    returning: Union[Unset, str] = UNSET,
) -> Optional[Union[CustomEntity, BadRequestError]]:
    """ Get a custom entity """

    return (
        await asyncio_detailed(
            client=client,
            custom_entity_id=custom_entity_id,
            returning=returning,
        )
    ).parsed
