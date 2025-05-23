from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    workspace: Union[Unset, None, str] = UNSET,
    show_workspace_restriction: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["workspace"] = workspace

    params["show_workspace_restriction"] = show_workspace_restriction

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/workers/custom_tags",
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[List[str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(List[str], response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[List[str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    workspace: Union[Unset, None, str] = UNSET,
    show_workspace_restriction: Union[Unset, None, bool] = UNSET,
) -> Response[List[str]]:
    """get all instance custom tags (tags are used to dispatch jobs to different worker groups)

    Args:
        workspace (Union[Unset, None, str]):
        show_workspace_restriction (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[str]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        show_workspace_restriction=show_workspace_restriction,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    workspace: Union[Unset, None, str] = UNSET,
    show_workspace_restriction: Union[Unset, None, bool] = UNSET,
) -> Optional[List[str]]:
    """get all instance custom tags (tags are used to dispatch jobs to different worker groups)

    Args:
        workspace (Union[Unset, None, str]):
        show_workspace_restriction (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List[str]
    """

    return sync_detailed(
        client=client,
        workspace=workspace,
        show_workspace_restriction=show_workspace_restriction,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    workspace: Union[Unset, None, str] = UNSET,
    show_workspace_restriction: Union[Unset, None, bool] = UNSET,
) -> Response[List[str]]:
    """get all instance custom tags (tags are used to dispatch jobs to different worker groups)

    Args:
        workspace (Union[Unset, None, str]):
        show_workspace_restriction (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[str]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        show_workspace_restriction=show_workspace_restriction,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    workspace: Union[Unset, None, str] = UNSET,
    show_workspace_restriction: Union[Unset, None, bool] = UNSET,
) -> Optional[List[str]]:
    """get all instance custom tags (tags are used to dispatch jobs to different worker groups)

    Args:
        workspace (Union[Unset, None, str]):
        show_workspace_restriction (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List[str]
    """

    return (
        await asyncio_detailed(
            client=client,
            workspace=workspace,
            show_workspace_restriction=show_workspace_restriction,
        )
    ).parsed
