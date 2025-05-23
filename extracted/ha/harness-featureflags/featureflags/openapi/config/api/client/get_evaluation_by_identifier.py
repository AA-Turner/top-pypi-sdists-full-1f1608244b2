from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.evaluation import Evaluation
from ...types import UNSET, Response, Unset


def _get_kwargs(
    environment_uuid: str,
    target: str,
    feature: str,
    *,
    cluster: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["cluster"] = cluster

    params = {k: v for k, v in params.items(
    ) if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/client/env/{environment_uuid}/target/{target}/evaluations/{feature}".format(
            environment_uuid=environment_uuid,
            target=target,
            feature=feature,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Evaluation]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Evaluation.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Evaluation]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_uuid: str,
    target: str,
    feature: str,
    *,
    client: AuthenticatedClient,
    cluster: Union[Unset, str] = UNSET,
) -> Response[Evaluation]:
    """Get feature evaluations for target

    Args:
        environment_uuid (str):
        target (str):
        feature (str):
        cluster (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Evaluation]
    """

    kwargs = _get_kwargs(
        environment_uuid=environment_uuid,
        target=target,
        feature=feature,
        cluster=cluster,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_uuid: str,
    target: str,
    feature: str,
    *,
    client: AuthenticatedClient,
    cluster: Union[Unset, str] = UNSET,
) -> Optional[Evaluation]:
    """Get feature evaluations for target

    Args:
        environment_uuid (str):
        target (str):
        feature (str):
        cluster (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Evaluation
    """

    return sync_detailed(
        environment_uuid=environment_uuid,
        target=target,
        feature=feature,
        client=client,
        cluster=cluster,
    ).parsed


async def asyncio_detailed(
    environment_uuid: str,
    target: str,
    feature: str,
    *,
    client: AuthenticatedClient,
    cluster: Union[Unset, str] = UNSET,
) -> Response[Evaluation]:
    """Get feature evaluations for target

    Args:
        environment_uuid (str):
        target (str):
        feature (str):
        cluster (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Evaluation]
    """

    kwargs = _get_kwargs(
        environment_uuid=environment_uuid,
        target=target,
        feature=feature,
        cluster=cluster,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_uuid: str,
    target: str,
    feature: str,
    *,
    client: AuthenticatedClient,
    cluster: Union[Unset, str] = UNSET,
) -> Optional[Evaluation]:
    """Get feature evaluations for target

    Args:
        environment_uuid (str):
        target (str):
        feature (str):
        cluster (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Evaluation
    """

    return (
        await asyncio_detailed(
            environment_uuid=environment_uuid,
            target=target,
            feature=feature,
            client=client,
            cluster=cluster,
        )
    ).parsed
