from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.bad_request_error import BadRequestError
from ...models.dna_oligo_helm import DnaOligoHelm
from ...models.oligo_create_helm import OligoCreateHelm
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: OligoCreateHelm,
) -> Dict[str, Any]:
    url = "{}/dna-oligos".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[DnaOligoHelm, BadRequestError]]:
    if response.status_code == 201:
        response_201 = DnaOligoHelm.from_dict(response.json(), strict=False)

        return response_201
    if response.status_code == 400:
        response_400 = BadRequestError.from_dict(response.json(), strict=False)

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[DnaOligoHelm, BadRequestError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: OligoCreateHelm,
) -> Response[Union[DnaOligoHelm, BadRequestError]]:
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
    json_body: OligoCreateHelm,
) -> Optional[Union[DnaOligoHelm, BadRequestError]]:
    """Create a DNA Oligo with optional HELM Deprecated as HELM support is now in stable."""

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: OligoCreateHelm,
) -> Response[Union[DnaOligoHelm, BadRequestError]]:
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
    json_body: OligoCreateHelm,
) -> Optional[Union[DnaOligoHelm, BadRequestError]]:
    """Create a DNA Oligo with optional HELM Deprecated as HELM support is now in stable."""

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
