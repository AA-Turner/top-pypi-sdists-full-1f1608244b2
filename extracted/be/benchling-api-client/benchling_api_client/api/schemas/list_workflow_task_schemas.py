from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.not_found_error import NotFoundError
from ...models.workflow_task_schemas_paginated_list import WorkflowTaskSchemasPaginatedList
from ...types import Response, UNSET, Unset


def _get_kwargs(
    *,
    client: Client,
    next_token: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 50,
    modified_at: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/workflow-task-schemas".format(client.base_url)

    headers: Dict[str, Any] = client.httpx_client.headers
    headers.update(client.get_headers())

    cookies: Dict[str, Any] = client.httpx_client.cookies
    cookies.update(client.get_cookies())

    params: Dict[str, Any] = {}
    if not isinstance(next_token, Unset) and next_token is not None:
        params["nextToken"] = next_token
    if not isinstance(page_size, Unset) and page_size is not None:
        params["pageSize"] = page_size
    if not isinstance(modified_at, Unset) and modified_at is not None:
        params["modifiedAt"] = modified_at

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[WorkflowTaskSchemasPaginatedList, NotFoundError]]:
    if response.status_code == 200:
        response_200 = WorkflowTaskSchemasPaginatedList.from_dict(response.json(), strict=False)

        return response_200
    if response.status_code == 404:
        response_404 = NotFoundError.from_dict(response.json(), strict=False)

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[WorkflowTaskSchemasPaginatedList, NotFoundError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    next_token: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 50,
    modified_at: Union[Unset, str] = UNSET,
) -> Response[Union[WorkflowTaskSchemasPaginatedList, NotFoundError]]:
    kwargs = _get_kwargs(
        client=client,
        next_token=next_token,
        page_size=page_size,
        modified_at=modified_at,
    )

    response = client.httpx_client.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    next_token: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 50,
    modified_at: Union[Unset, str] = UNSET,
) -> Optional[Union[WorkflowTaskSchemasPaginatedList, NotFoundError]]:
    """ List workflow task schemas """

    return sync_detailed(
        client=client,
        next_token=next_token,
        page_size=page_size,
        modified_at=modified_at,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    next_token: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 50,
    modified_at: Union[Unset, str] = UNSET,
) -> Response[Union[WorkflowTaskSchemasPaginatedList, NotFoundError]]:
    kwargs = _get_kwargs(
        client=client,
        next_token=next_token,
        page_size=page_size,
        modified_at=modified_at,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    next_token: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 50,
    modified_at: Union[Unset, str] = UNSET,
) -> Optional[Union[WorkflowTaskSchemasPaginatedList, NotFoundError]]:
    """ List workflow task schemas """

    return (
        await asyncio_detailed(
            client=client,
            next_token=next_token,
            page_size=page_size,
            modified_at=modified_at,
        )
    ).parsed
