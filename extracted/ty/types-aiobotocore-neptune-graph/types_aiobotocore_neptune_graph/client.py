"""
Type annotations for neptune-graph service Client.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_neptune_graph.client import NeptuneGraphClient

    session = get_session()
    async with session.create_client("neptune-graph") as client:
        client: NeptuneGraphClient
    ```
"""

from __future__ import annotations

import sys
from types import TracebackType
from typing import Any, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListExportTasksPaginator,
    ListGraphSnapshotsPaginator,
    ListGraphsPaginator,
    ListImportTasksPaginator,
    ListPrivateGraphEndpointsPaginator,
)
from .type_defs import (
    CancelExportTaskInputTypeDef,
    CancelExportTaskOutputTypeDef,
    CancelImportTaskInputTypeDef,
    CancelImportTaskOutputTypeDef,
    CancelQueryInputTypeDef,
    CreateGraphInputTypeDef,
    CreateGraphOutputTypeDef,
    CreateGraphSnapshotInputTypeDef,
    CreateGraphSnapshotOutputTypeDef,
    CreateGraphUsingImportTaskInputTypeDef,
    CreateGraphUsingImportTaskOutputTypeDef,
    CreatePrivateGraphEndpointInputTypeDef,
    CreatePrivateGraphEndpointOutputTypeDef,
    DeleteGraphInputTypeDef,
    DeleteGraphOutputTypeDef,
    DeleteGraphSnapshotInputTypeDef,
    DeleteGraphSnapshotOutputTypeDef,
    DeletePrivateGraphEndpointInputTypeDef,
    DeletePrivateGraphEndpointOutputTypeDef,
    EmptyResponseMetadataTypeDef,
    ExecuteQueryInputTypeDef,
    ExecuteQueryOutputTypeDef,
    GetExportTaskInputTypeDef,
    GetExportTaskOutputTypeDef,
    GetGraphInputTypeDef,
    GetGraphOutputTypeDef,
    GetGraphSnapshotInputTypeDef,
    GetGraphSnapshotOutputTypeDef,
    GetGraphSummaryInputTypeDef,
    GetGraphSummaryOutputTypeDef,
    GetImportTaskInputTypeDef,
    GetImportTaskOutputTypeDef,
    GetPrivateGraphEndpointInputTypeDef,
    GetPrivateGraphEndpointOutputTypeDef,
    GetQueryInputTypeDef,
    GetQueryOutputTypeDef,
    ListExportTasksInputTypeDef,
    ListExportTasksOutputTypeDef,
    ListGraphsInputTypeDef,
    ListGraphSnapshotsInputTypeDef,
    ListGraphSnapshotsOutputTypeDef,
    ListGraphsOutputTypeDef,
    ListImportTasksInputTypeDef,
    ListImportTasksOutputTypeDef,
    ListPrivateGraphEndpointsInputTypeDef,
    ListPrivateGraphEndpointsOutputTypeDef,
    ListQueriesInputTypeDef,
    ListQueriesOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ResetGraphInputTypeDef,
    ResetGraphOutputTypeDef,
    RestoreGraphFromSnapshotInputTypeDef,
    RestoreGraphFromSnapshotOutputTypeDef,
    StartExportTaskInputTypeDef,
    StartExportTaskOutputTypeDef,
    StartImportTaskInputTypeDef,
    StartImportTaskOutputTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
    UpdateGraphInputTypeDef,
    UpdateGraphOutputTypeDef,
)
from .waiter import (
    ExportTaskCancelledWaiter,
    ExportTaskSuccessfulWaiter,
    GraphAvailableWaiter,
    GraphDeletedWaiter,
    GraphSnapshotAvailableWaiter,
    GraphSnapshotDeletedWaiter,
    ImportTaskCancelledWaiter,
    ImportTaskSuccessfulWaiter,
    PrivateGraphEndpointAvailableWaiter,
    PrivateGraphEndpointDeletedWaiter,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Self, Unpack
else:
    from typing_extensions import Literal, Self, Unpack


__all__ = ("NeptuneGraphClient",)


class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnprocessableException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class NeptuneGraphClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        NeptuneGraphClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/can_paginate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#can_paginate)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/generate_presigned_url.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#generate_presigned_url)
        """

    async def cancel_export_task(
        self, **kwargs: Unpack[CancelExportTaskInputTypeDef]
    ) -> CancelExportTaskOutputTypeDef:
        """
        Cancel the specified export task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/cancel_export_task.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#cancel_export_task)
        """

    async def cancel_import_task(
        self, **kwargs: Unpack[CancelImportTaskInputTypeDef]
    ) -> CancelImportTaskOutputTypeDef:
        """
        Deletes the specified import task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/cancel_import_task.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#cancel_import_task)
        """

    async def cancel_query(
        self, **kwargs: Unpack[CancelQueryInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Cancels a specified query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/cancel_query.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#cancel_query)
        """

    async def create_graph(
        self, **kwargs: Unpack[CreateGraphInputTypeDef]
    ) -> CreateGraphOutputTypeDef:
        """
        Creates a new Neptune Analytics graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/create_graph.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#create_graph)
        """

    async def create_graph_snapshot(
        self, **kwargs: Unpack[CreateGraphSnapshotInputTypeDef]
    ) -> CreateGraphSnapshotOutputTypeDef:
        """
        Creates a snapshot of the specific graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/create_graph_snapshot.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#create_graph_snapshot)
        """

    async def create_graph_using_import_task(
        self, **kwargs: Unpack[CreateGraphUsingImportTaskInputTypeDef]
    ) -> CreateGraphUsingImportTaskOutputTypeDef:
        """
        Creates a new Neptune Analytics graph and imports data into it, either from
        Amazon Simple Storage Service (S3) or from a Neptune database or a Neptune
        database snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/create_graph_using_import_task.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#create_graph_using_import_task)
        """

    async def create_private_graph_endpoint(
        self, **kwargs: Unpack[CreatePrivateGraphEndpointInputTypeDef]
    ) -> CreatePrivateGraphEndpointOutputTypeDef:
        """
        Create a private graph endpoint to allow private access from to the graph from
        within a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/create_private_graph_endpoint.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#create_private_graph_endpoint)
        """

    async def delete_graph(
        self, **kwargs: Unpack[DeleteGraphInputTypeDef]
    ) -> DeleteGraphOutputTypeDef:
        """
        Deletes the specified graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/delete_graph.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#delete_graph)
        """

    async def delete_graph_snapshot(
        self, **kwargs: Unpack[DeleteGraphSnapshotInputTypeDef]
    ) -> DeleteGraphSnapshotOutputTypeDef:
        """
        Deletes the specifed graph snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/delete_graph_snapshot.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#delete_graph_snapshot)
        """

    async def delete_private_graph_endpoint(
        self, **kwargs: Unpack[DeletePrivateGraphEndpointInputTypeDef]
    ) -> DeletePrivateGraphEndpointOutputTypeDef:
        """
        Deletes a private graph endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/delete_private_graph_endpoint.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#delete_private_graph_endpoint)
        """

    async def execute_query(
        self, **kwargs: Unpack[ExecuteQueryInputTypeDef]
    ) -> ExecuteQueryOutputTypeDef:
        """
        Execute an openCypher query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/execute_query.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#execute_query)
        """

    async def get_export_task(
        self, **kwargs: Unpack[GetExportTaskInputTypeDef]
    ) -> GetExportTaskOutputTypeDef:
        """
        Retrieves a specified export task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/get_export_task.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_export_task)
        """

    async def get_graph(self, **kwargs: Unpack[GetGraphInputTypeDef]) -> GetGraphOutputTypeDef:
        """
        Gets information about a specified graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/get_graph.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_graph)
        """

    async def get_graph_snapshot(
        self, **kwargs: Unpack[GetGraphSnapshotInputTypeDef]
    ) -> GetGraphSnapshotOutputTypeDef:
        """
        Retrieves a specified graph snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/get_graph_snapshot.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_graph_snapshot)
        """

    async def get_graph_summary(
        self, **kwargs: Unpack[GetGraphSummaryInputTypeDef]
    ) -> GetGraphSummaryOutputTypeDef:
        """
        Gets a graph summary for a property graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/get_graph_summary.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_graph_summary)
        """

    async def get_import_task(
        self, **kwargs: Unpack[GetImportTaskInputTypeDef]
    ) -> GetImportTaskOutputTypeDef:
        """
        Retrieves a specified import task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/get_import_task.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_import_task)
        """

    async def get_private_graph_endpoint(
        self, **kwargs: Unpack[GetPrivateGraphEndpointInputTypeDef]
    ) -> GetPrivateGraphEndpointOutputTypeDef:
        """
        Retrieves information about a specified private endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/get_private_graph_endpoint.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_private_graph_endpoint)
        """

    async def get_query(self, **kwargs: Unpack[GetQueryInputTypeDef]) -> GetQueryOutputTypeDef:
        """
        Retrieves the status of a specified query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/get_query.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_query)
        """

    async def list_export_tasks(
        self, **kwargs: Unpack[ListExportTasksInputTypeDef]
    ) -> ListExportTasksOutputTypeDef:
        """
        Retrieves a list of export tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/list_export_tasks.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#list_export_tasks)
        """

    async def list_graph_snapshots(
        self, **kwargs: Unpack[ListGraphSnapshotsInputTypeDef]
    ) -> ListGraphSnapshotsOutputTypeDef:
        """
        Lists available snapshots of a specified Neptune Analytics graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/list_graph_snapshots.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#list_graph_snapshots)
        """

    async def list_graphs(
        self, **kwargs: Unpack[ListGraphsInputTypeDef]
    ) -> ListGraphsOutputTypeDef:
        """
        Lists available Neptune Analytics graphs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/list_graphs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#list_graphs)
        """

    async def list_import_tasks(
        self, **kwargs: Unpack[ListImportTasksInputTypeDef]
    ) -> ListImportTasksOutputTypeDef:
        """
        Lists import tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/list_import_tasks.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#list_import_tasks)
        """

    async def list_private_graph_endpoints(
        self, **kwargs: Unpack[ListPrivateGraphEndpointsInputTypeDef]
    ) -> ListPrivateGraphEndpointsOutputTypeDef:
        """
        Lists private endpoints for a specified Neptune Analytics graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/list_private_graph_endpoints.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#list_private_graph_endpoints)
        """

    async def list_queries(
        self, **kwargs: Unpack[ListQueriesInputTypeDef]
    ) -> ListQueriesOutputTypeDef:
        """
        Lists active openCypher queries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/list_queries.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#list_queries)
        """

    async def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Lists tags associated with a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/list_tags_for_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#list_tags_for_resource)
        """

    async def reset_graph(
        self, **kwargs: Unpack[ResetGraphInputTypeDef]
    ) -> ResetGraphOutputTypeDef:
        """
        Empties the data from a specified Neptune Analytics graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/reset_graph.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#reset_graph)
        """

    async def restore_graph_from_snapshot(
        self, **kwargs: Unpack[RestoreGraphFromSnapshotInputTypeDef]
    ) -> RestoreGraphFromSnapshotOutputTypeDef:
        """
        Restores a graph from a snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/restore_graph_from_snapshot.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#restore_graph_from_snapshot)
        """

    async def start_export_task(
        self, **kwargs: Unpack[StartExportTaskInputTypeDef]
    ) -> StartExportTaskOutputTypeDef:
        """
        Export data from an existing Neptune Analytics graph to Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/start_export_task.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#start_export_task)
        """

    async def start_import_task(
        self, **kwargs: Unpack[StartImportTaskInputTypeDef]
    ) -> StartImportTaskOutputTypeDef:
        """
        Import data into existing Neptune Analytics graph from Amazon Simple Storage
        Service (S3).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/start_import_task.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#start_import_task)
        """

    async def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Adds tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/tag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#tag_resource)
        """

    async def untag_resource(self, **kwargs: Unpack[UntagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/untag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#untag_resource)
        """

    async def update_graph(
        self, **kwargs: Unpack[UpdateGraphInputTypeDef]
    ) -> UpdateGraphOutputTypeDef:
        """
        Updates the configuration of a specified Neptune Analytics graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/update_graph.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#update_graph)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_export_tasks"]
    ) -> ListExportTasksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_graph_snapshots"]
    ) -> ListGraphSnapshotsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_graphs"]
    ) -> ListGraphsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_import_tasks"]
    ) -> ListImportTasksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_private_graph_endpoints"]
    ) -> ListPrivateGraphEndpointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["export_task_cancelled"]
    ) -> ExportTaskCancelledWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["export_task_successful"]
    ) -> ExportTaskSuccessfulWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["graph_available"]
    ) -> GraphAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["graph_deleted"]
    ) -> GraphDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["graph_snapshot_available"]
    ) -> GraphSnapshotAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["graph_snapshot_deleted"]
    ) -> GraphSnapshotDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["import_task_cancelled"]
    ) -> ImportTaskCancelledWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["import_task_successful"]
    ) -> ImportTaskSuccessfulWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["private_graph_endpoint_available"]
    ) -> PrivateGraphEndpointAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["private_graph_endpoint_deleted"]
    ) -> PrivateGraphEndpointDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_waiter)
        """

    async def __aenter__(self) -> Self:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/)
        """

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/)
        """
