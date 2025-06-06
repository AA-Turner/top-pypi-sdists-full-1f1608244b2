from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.bad_request_error import BadRequestError
from ...models.forbidden_error import ForbiddenError
from ...models.monomer import Monomer
from ...models.monomer_create import MonomerCreate
from ...types import Response, UNSET, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: MonomerCreate,
    returning: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/monomers".format(client.base_url)

    headers: Dict[str, Any] = client.httpx_client.headers
    headers.update(client.get_headers())

    cookies: Dict[str, Any] = client.httpx_client.cookies
    cookies.update(client.get_cookies())

    params: Dict[str, Any] = {}
    if not isinstance(returning, Unset) and returning is not None:
        params["returning"] = returning

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Monomer, BadRequestError, ForbiddenError]]:
    if response.status_code == 201:
        response_201 = Monomer.from_dict(response.json(), strict=False)

        return response_201
    if response.status_code == 400:
        response_400 = BadRequestError.from_dict(response.json(), strict=False)

        return response_400
    if response.status_code == 403:
        response_403 = ForbiddenError.from_dict(response.json(), strict=False)

        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Monomer, BadRequestError, ForbiddenError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: MonomerCreate,
    returning: Union[Unset, str] = UNSET,
) -> Response[Union[Monomer, BadRequestError, ForbiddenError]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        returning=returning,
    )

    response = client.httpx_client.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: MonomerCreate,
    returning: Union[Unset, str] = UNSET,
) -> Optional[Union[Monomer, BadRequestError, ForbiddenError]]:
    """ Create a monomer. """

    return sync_detailed(
        client=client,
        json_body=json_body,
        returning=returning,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: MonomerCreate,
    returning: Union[Unset, str] = UNSET,
) -> Response[Union[Monomer, BadRequestError, ForbiddenError]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        returning=returning,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: MonomerCreate,
    returning: Union[Unset, str] = UNSET,
) -> Optional[Union[Monomer, BadRequestError, ForbiddenError]]:
    """ Create a monomer. """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            returning=returning,
        )
    ).parsed
