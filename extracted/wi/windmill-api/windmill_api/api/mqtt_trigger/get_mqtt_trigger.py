from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_mqtt_trigger_response_200 import GetMqttTriggerResponse200
from ...types import Response


def _get_kwargs(
    workspace: str,
    path: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/w/{workspace}/mqtt_triggers/get/{path}".format(
            workspace=workspace,
            path=path,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetMqttTriggerResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetMqttTriggerResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetMqttTriggerResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: str,
    path: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetMqttTriggerResponse200]:
    """get mqtt trigger

    Args:
        workspace (str):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMqttTriggerResponse200]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        path=path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    path: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetMqttTriggerResponse200]:
    """get mqtt trigger

    Args:
        workspace (str):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMqttTriggerResponse200
    """

    return sync_detailed(
        workspace=workspace,
        path=path,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    path: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetMqttTriggerResponse200]:
    """get mqtt trigger

    Args:
        workspace (str):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMqttTriggerResponse200]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        path=path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    path: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetMqttTriggerResponse200]:
    """get mqtt trigger

    Args:
        workspace (str):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMqttTriggerResponse200
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            path=path,
            client=client,
        )
    ).parsed
