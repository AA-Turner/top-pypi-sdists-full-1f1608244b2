from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.not_found_error import NotFoundError
from ...models.request_response import RequestResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    request_id: str,
) -> Dict[str, Any]:
    url = "{}/requests/{request_id}/response".format(client.base_url, request_id=request_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[RequestResponse, NotFoundError]]:
    if response.status_code == 200:
        response_200 = RequestResponse.from_dict(response.json(), strict=False)

        return response_200
    if response.status_code == 404:
        response_404 = NotFoundError.from_dict(response.json(), strict=False)

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[RequestResponse, NotFoundError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    request_id: str,
) -> Response[Union[RequestResponse, NotFoundError]]:
    kwargs = _get_kwargs(
        client=client,
        request_id=request_id,
    )

    response = client.httpx_client.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    request_id: str,
) -> Optional[Union[RequestResponse, NotFoundError]]:
    """ Get a Legacy Request's response """

    return sync_detailed(
        client=client,
        request_id=request_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    request_id: str,
) -> Response[Union[RequestResponse, NotFoundError]]:
    kwargs = _get_kwargs(
        client=client,
        request_id=request_id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    request_id: str,
) -> Optional[Union[RequestResponse, NotFoundError]]:
    """ Get a Legacy Request's response """

    return (
        await asyncio_detailed(
            client=client,
            request_id=request_id,
        )
    ).parsed
