"""
Type annotations for datasync service Client.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_datasync.client import DataSyncClient

    session = get_session()
    async with session.create_client("datasync") as client:
        client: DataSyncClient
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
    ListAgentsPaginator,
    ListLocationsPaginator,
    ListTagsForResourcePaginator,
    ListTaskExecutionsPaginator,
    ListTasksPaginator,
)
from .type_defs import (
    CancelTaskExecutionRequestTypeDef,
    CreateAgentRequestTypeDef,
    CreateAgentResponseTypeDef,
    CreateLocationAzureBlobRequestTypeDef,
    CreateLocationAzureBlobResponseTypeDef,
    CreateLocationEfsRequestTypeDef,
    CreateLocationEfsResponseTypeDef,
    CreateLocationFsxLustreRequestTypeDef,
    CreateLocationFsxLustreResponseTypeDef,
    CreateLocationFsxOntapRequestTypeDef,
    CreateLocationFsxOntapResponseTypeDef,
    CreateLocationFsxOpenZfsRequestTypeDef,
    CreateLocationFsxOpenZfsResponseTypeDef,
    CreateLocationFsxWindowsRequestTypeDef,
    CreateLocationFsxWindowsResponseTypeDef,
    CreateLocationHdfsRequestTypeDef,
    CreateLocationHdfsResponseTypeDef,
    CreateLocationNfsRequestTypeDef,
    CreateLocationNfsResponseTypeDef,
    CreateLocationObjectStorageRequestTypeDef,
    CreateLocationObjectStorageResponseTypeDef,
    CreateLocationS3RequestTypeDef,
    CreateLocationS3ResponseTypeDef,
    CreateLocationSmbRequestTypeDef,
    CreateLocationSmbResponseTypeDef,
    CreateTaskRequestTypeDef,
    CreateTaskResponseTypeDef,
    DeleteAgentRequestTypeDef,
    DeleteLocationRequestTypeDef,
    DeleteTaskRequestTypeDef,
    DescribeAgentRequestTypeDef,
    DescribeAgentResponseTypeDef,
    DescribeLocationAzureBlobRequestTypeDef,
    DescribeLocationAzureBlobResponseTypeDef,
    DescribeLocationEfsRequestTypeDef,
    DescribeLocationEfsResponseTypeDef,
    DescribeLocationFsxLustreRequestTypeDef,
    DescribeLocationFsxLustreResponseTypeDef,
    DescribeLocationFsxOntapRequestTypeDef,
    DescribeLocationFsxOntapResponseTypeDef,
    DescribeLocationFsxOpenZfsRequestTypeDef,
    DescribeLocationFsxOpenZfsResponseTypeDef,
    DescribeLocationFsxWindowsRequestTypeDef,
    DescribeLocationFsxWindowsResponseTypeDef,
    DescribeLocationHdfsRequestTypeDef,
    DescribeLocationHdfsResponseTypeDef,
    DescribeLocationNfsRequestTypeDef,
    DescribeLocationNfsResponseTypeDef,
    DescribeLocationObjectStorageRequestTypeDef,
    DescribeLocationObjectStorageResponseTypeDef,
    DescribeLocationS3RequestTypeDef,
    DescribeLocationS3ResponseTypeDef,
    DescribeLocationSmbRequestTypeDef,
    DescribeLocationSmbResponseTypeDef,
    DescribeTaskExecutionRequestTypeDef,
    DescribeTaskExecutionResponseTypeDef,
    DescribeTaskRequestTypeDef,
    DescribeTaskResponseTypeDef,
    ListAgentsRequestTypeDef,
    ListAgentsResponseTypeDef,
    ListLocationsRequestTypeDef,
    ListLocationsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTaskExecutionsRequestTypeDef,
    ListTaskExecutionsResponseTypeDef,
    ListTasksRequestTypeDef,
    ListTasksResponseTypeDef,
    StartTaskExecutionRequestTypeDef,
    StartTaskExecutionResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAgentRequestTypeDef,
    UpdateLocationAzureBlobRequestTypeDef,
    UpdateLocationEfsRequestTypeDef,
    UpdateLocationFsxLustreRequestTypeDef,
    UpdateLocationFsxOntapRequestTypeDef,
    UpdateLocationFsxOpenZfsRequestTypeDef,
    UpdateLocationFsxWindowsRequestTypeDef,
    UpdateLocationHdfsRequestTypeDef,
    UpdateLocationNfsRequestTypeDef,
    UpdateLocationObjectStorageRequestTypeDef,
    UpdateLocationS3RequestTypeDef,
    UpdateLocationSmbRequestTypeDef,
    UpdateTaskExecutionRequestTypeDef,
    UpdateTaskRequestTypeDef,
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

__all__ = ("DataSyncClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InternalException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]

class DataSyncClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DataSyncClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/can_paginate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#can_paginate)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/generate_presigned_url.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#generate_presigned_url)
        """

    async def cancel_task_execution(
        self, **kwargs: Unpack[CancelTaskExecutionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Stops an DataSync task execution that's in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/cancel_task_execution.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#cancel_task_execution)
        """

    async def create_agent(
        self, **kwargs: Unpack[CreateAgentRequestTypeDef]
    ) -> CreateAgentResponseTypeDef:
        """
        Activates an DataSync agent that you deploy in your storage environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_agent.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#create_agent)
        """

    async def create_location_azure_blob(
        self, **kwargs: Unpack[CreateLocationAzureBlobRequestTypeDef]
    ) -> CreateLocationAzureBlobResponseTypeDef:
        """
        Creates a transfer <i>location</i> for a Microsoft Azure Blob Storage container.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_location_azure_blob.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#create_location_azure_blob)
        """

    async def create_location_efs(
        self, **kwargs: Unpack[CreateLocationEfsRequestTypeDef]
    ) -> CreateLocationEfsResponseTypeDef:
        """
        Creates a transfer <i>location</i> for an Amazon EFS file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_location_efs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#create_location_efs)
        """

    async def create_location_fsx_lustre(
        self, **kwargs: Unpack[CreateLocationFsxLustreRequestTypeDef]
    ) -> CreateLocationFsxLustreResponseTypeDef:
        """
        Creates a transfer <i>location</i> for an Amazon FSx for Lustre file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_location_fsx_lustre.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#create_location_fsx_lustre)
        """

    async def create_location_fsx_ontap(
        self, **kwargs: Unpack[CreateLocationFsxOntapRequestTypeDef]
    ) -> CreateLocationFsxOntapResponseTypeDef:
        """
        Creates a transfer <i>location</i> for an Amazon FSx for NetApp ONTAP file
        system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_location_fsx_ontap.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#create_location_fsx_ontap)
        """

    async def create_location_fsx_open_zfs(
        self, **kwargs: Unpack[CreateLocationFsxOpenZfsRequestTypeDef]
    ) -> CreateLocationFsxOpenZfsResponseTypeDef:
        """
        Creates a transfer <i>location</i> for an Amazon FSx for OpenZFS file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_location_fsx_open_zfs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#create_location_fsx_open_zfs)
        """

    async def create_location_fsx_windows(
        self, **kwargs: Unpack[CreateLocationFsxWindowsRequestTypeDef]
    ) -> CreateLocationFsxWindowsResponseTypeDef:
        """
        Creates a transfer <i>location</i> for an Amazon FSx for Windows File Server
        file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_location_fsx_windows.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#create_location_fsx_windows)
        """

    async def create_location_hdfs(
        self, **kwargs: Unpack[CreateLocationHdfsRequestTypeDef]
    ) -> CreateLocationHdfsResponseTypeDef:
        """
        Creates a transfer <i>location</i> for a Hadoop Distributed File System (HDFS).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_location_hdfs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#create_location_hdfs)
        """

    async def create_location_nfs(
        self, **kwargs: Unpack[CreateLocationNfsRequestTypeDef]
    ) -> CreateLocationNfsResponseTypeDef:
        """
        Creates a transfer <i>location</i> for a Network File System (NFS) file server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_location_nfs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#create_location_nfs)
        """

    async def create_location_object_storage(
        self, **kwargs: Unpack[CreateLocationObjectStorageRequestTypeDef]
    ) -> CreateLocationObjectStorageResponseTypeDef:
        """
        Creates a transfer <i>location</i> for an object storage system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_location_object_storage.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#create_location_object_storage)
        """

    async def create_location_s3(
        self, **kwargs: Unpack[CreateLocationS3RequestTypeDef]
    ) -> CreateLocationS3ResponseTypeDef:
        """
        Creates a transfer <i>location</i> for an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_location_s3.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#create_location_s3)
        """

    async def create_location_smb(
        self, **kwargs: Unpack[CreateLocationSmbRequestTypeDef]
    ) -> CreateLocationSmbResponseTypeDef:
        """
        Creates a transfer <i>location</i> for a Server Message Block (SMB) file server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_location_smb.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#create_location_smb)
        """

    async def create_task(
        self, **kwargs: Unpack[CreateTaskRequestTypeDef]
    ) -> CreateTaskResponseTypeDef:
        """
        Configures a <i>task</i>, which defines where and how DataSync transfers your
        data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/create_task.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#create_task)
        """

    async def delete_agent(self, **kwargs: Unpack[DeleteAgentRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes an DataSync agent resource from your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/delete_agent.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#delete_agent)
        """

    async def delete_location(
        self, **kwargs: Unpack[DeleteLocationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a transfer location resource from DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/delete_location.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#delete_location)
        """

    async def delete_task(self, **kwargs: Unpack[DeleteTaskRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a transfer task resource from DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/delete_task.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#delete_task)
        """

    async def describe_agent(
        self, **kwargs: Unpack[DescribeAgentRequestTypeDef]
    ) -> DescribeAgentResponseTypeDef:
        """
        Returns information about an DataSync agent, such as its name, service endpoint
        type, and status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_agent.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#describe_agent)
        """

    async def describe_location_azure_blob(
        self, **kwargs: Unpack[DescribeLocationAzureBlobRequestTypeDef]
    ) -> DescribeLocationAzureBlobResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for Microsoft Azure
        Blob Storage is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_location_azure_blob.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#describe_location_azure_blob)
        """

    async def describe_location_efs(
        self, **kwargs: Unpack[DescribeLocationEfsRequestTypeDef]
    ) -> DescribeLocationEfsResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for an Amazon EFS file
        system is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_location_efs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#describe_location_efs)
        """

    async def describe_location_fsx_lustre(
        self, **kwargs: Unpack[DescribeLocationFsxLustreRequestTypeDef]
    ) -> DescribeLocationFsxLustreResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for an Amazon FSx for
        Lustre file system is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_location_fsx_lustre.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#describe_location_fsx_lustre)
        """

    async def describe_location_fsx_ontap(
        self, **kwargs: Unpack[DescribeLocationFsxOntapRequestTypeDef]
    ) -> DescribeLocationFsxOntapResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for an Amazon FSx for
        NetApp ONTAP file system is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_location_fsx_ontap.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#describe_location_fsx_ontap)
        """

    async def describe_location_fsx_open_zfs(
        self, **kwargs: Unpack[DescribeLocationFsxOpenZfsRequestTypeDef]
    ) -> DescribeLocationFsxOpenZfsResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for an Amazon FSx for
        OpenZFS file system is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_location_fsx_open_zfs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#describe_location_fsx_open_zfs)
        """

    async def describe_location_fsx_windows(
        self, **kwargs: Unpack[DescribeLocationFsxWindowsRequestTypeDef]
    ) -> DescribeLocationFsxWindowsResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for an Amazon FSx for
        Windows File Server file system is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_location_fsx_windows.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#describe_location_fsx_windows)
        """

    async def describe_location_hdfs(
        self, **kwargs: Unpack[DescribeLocationHdfsRequestTypeDef]
    ) -> DescribeLocationHdfsResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for a Hadoop
        Distributed File System (HDFS) is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_location_hdfs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#describe_location_hdfs)
        """

    async def describe_location_nfs(
        self, **kwargs: Unpack[DescribeLocationNfsRequestTypeDef]
    ) -> DescribeLocationNfsResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for a Network File
        System (NFS) file server is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_location_nfs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#describe_location_nfs)
        """

    async def describe_location_object_storage(
        self, **kwargs: Unpack[DescribeLocationObjectStorageRequestTypeDef]
    ) -> DescribeLocationObjectStorageResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for an object storage
        system is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_location_object_storage.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#describe_location_object_storage)
        """

    async def describe_location_s3(
        self, **kwargs: Unpack[DescribeLocationS3RequestTypeDef]
    ) -> DescribeLocationS3ResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for an S3 bucket is
        configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_location_s3.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#describe_location_s3)
        """

    async def describe_location_smb(
        self, **kwargs: Unpack[DescribeLocationSmbRequestTypeDef]
    ) -> DescribeLocationSmbResponseTypeDef:
        """
        Provides details about how an DataSync transfer location for a Server Message
        Block (SMB) file server is configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_location_smb.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#describe_location_smb)
        """

    async def describe_task(
        self, **kwargs: Unpack[DescribeTaskRequestTypeDef]
    ) -> DescribeTaskResponseTypeDef:
        """
        Provides information about a <i>task</i>, which defines where and how DataSync
        transfers your data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_task.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#describe_task)
        """

    async def describe_task_execution(
        self, **kwargs: Unpack[DescribeTaskExecutionRequestTypeDef]
    ) -> DescribeTaskExecutionResponseTypeDef:
        """
        Provides information about an execution of your DataSync task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/describe_task_execution.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#describe_task_execution)
        """

    async def list_agents(
        self, **kwargs: Unpack[ListAgentsRequestTypeDef]
    ) -> ListAgentsResponseTypeDef:
        """
        Returns a list of DataSync agents that belong to an Amazon Web Services account
        in the Amazon Web Services Region specified in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/list_agents.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#list_agents)
        """

    async def list_locations(
        self, **kwargs: Unpack[ListLocationsRequestTypeDef]
    ) -> ListLocationsResponseTypeDef:
        """
        Returns a list of source and destination locations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/list_locations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#list_locations)
        """

    async def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns all the tags associated with an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/list_tags_for_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#list_tags_for_resource)
        """

    async def list_task_executions(
        self, **kwargs: Unpack[ListTaskExecutionsRequestTypeDef]
    ) -> ListTaskExecutionsResponseTypeDef:
        """
        Returns a list of executions for an DataSync transfer task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/list_task_executions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#list_task_executions)
        """

    async def list_tasks(
        self, **kwargs: Unpack[ListTasksRequestTypeDef]
    ) -> ListTasksResponseTypeDef:
        """
        Returns a list of the DataSync tasks you created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/list_tasks.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#list_tasks)
        """

    async def start_task_execution(
        self, **kwargs: Unpack[StartTaskExecutionRequestTypeDef]
    ) -> StartTaskExecutionResponseTypeDef:
        """
        Starts an DataSync transfer task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/start_task_execution.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#start_task_execution)
        """

    async def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Applies a <i>tag</i> to an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/tag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#tag_resource)
        """

    async def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/untag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#untag_resource)
        """

    async def update_agent(self, **kwargs: Unpack[UpdateAgentRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates the name of an DataSync agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_agent.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#update_agent)
        """

    async def update_location_azure_blob(
        self, **kwargs: Unpack[UpdateLocationAzureBlobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies the following configurations of the Microsoft Azure Blob Storage
        transfer location that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_location_azure_blob.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#update_location_azure_blob)
        """

    async def update_location_efs(
        self, **kwargs: Unpack[UpdateLocationEfsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies the following configuration parameters of the Amazon EFS transfer
        location that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_location_efs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#update_location_efs)
        """

    async def update_location_fsx_lustre(
        self, **kwargs: Unpack[UpdateLocationFsxLustreRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies the following configuration parameters of the Amazon FSx for Lustre
        transfer location that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_location_fsx_lustre.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#update_location_fsx_lustre)
        """

    async def update_location_fsx_ontap(
        self, **kwargs: Unpack[UpdateLocationFsxOntapRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies the following configuration parameters of the Amazon FSx for NetApp
        ONTAP transfer location that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_location_fsx_ontap.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#update_location_fsx_ontap)
        """

    async def update_location_fsx_open_zfs(
        self, **kwargs: Unpack[UpdateLocationFsxOpenZfsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies the following configuration parameters of the Amazon FSx for OpenZFS
        transfer location that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_location_fsx_open_zfs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#update_location_fsx_open_zfs)
        """

    async def update_location_fsx_windows(
        self, **kwargs: Unpack[UpdateLocationFsxWindowsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies the following configuration parameters of the Amazon FSx for Windows
        File Server transfer location that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_location_fsx_windows.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#update_location_fsx_windows)
        """

    async def update_location_hdfs(
        self, **kwargs: Unpack[UpdateLocationHdfsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies the following configuration parameters of the Hadoop Distributed File
        System (HDFS) transfer location that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_location_hdfs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#update_location_hdfs)
        """

    async def update_location_nfs(
        self, **kwargs: Unpack[UpdateLocationNfsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies the following configuration parameters of the Network File System
        (NFS) transfer location that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_location_nfs.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#update_location_nfs)
        """

    async def update_location_object_storage(
        self, **kwargs: Unpack[UpdateLocationObjectStorageRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies the following configuration parameters of the object storage transfer
        location that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_location_object_storage.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#update_location_object_storage)
        """

    async def update_location_s3(
        self, **kwargs: Unpack[UpdateLocationS3RequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies the following configuration parameters of the Amazon S3 transfer
        location that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_location_s3.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#update_location_s3)
        """

    async def update_location_smb(
        self, **kwargs: Unpack[UpdateLocationSmbRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies the following configuration parameters of the Server Message Block
        (SMB) transfer location that you're using with DataSync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_location_smb.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#update_location_smb)
        """

    async def update_task(self, **kwargs: Unpack[UpdateTaskRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates the configuration of a <i>task</i>, which defines where and how
        DataSync transfers your data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_task.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#update_task)
        """

    async def update_task_execution(
        self, **kwargs: Unpack[UpdateTaskExecutionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the configuration of a running DataSync task execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/update_task_execution.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#update_task_execution)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_agents"]
    ) -> ListAgentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_locations"]
    ) -> ListLocationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_task_executions"]
    ) -> ListTaskExecutionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tasks"]
    ) -> ListTasksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/#get_paginator)
        """

    async def __aenter__(self) -> Self:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/)
        """

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/client/)
        """
