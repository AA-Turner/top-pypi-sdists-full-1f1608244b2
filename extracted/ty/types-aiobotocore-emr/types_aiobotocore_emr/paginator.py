"""
Type annotations for emr service client paginators.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_emr.client import EMRClient
    from types_aiobotocore_emr.paginator import (
        ListBootstrapActionsPaginator,
        ListClustersPaginator,
        ListInstanceFleetsPaginator,
        ListInstanceGroupsPaginator,
        ListInstancesPaginator,
        ListNotebookExecutionsPaginator,
        ListSecurityConfigurationsPaginator,
        ListStepsPaginator,
        ListStudioSessionMappingsPaginator,
        ListStudiosPaginator,
    )

    session = get_session()
    with session.create_client("emr") as client:
        client: EMRClient

        list_bootstrap_actions_paginator: ListBootstrapActionsPaginator = client.get_paginator("list_bootstrap_actions")
        list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
        list_instance_fleets_paginator: ListInstanceFleetsPaginator = client.get_paginator("list_instance_fleets")
        list_instance_groups_paginator: ListInstanceGroupsPaginator = client.get_paginator("list_instance_groups")
        list_instances_paginator: ListInstancesPaginator = client.get_paginator("list_instances")
        list_notebook_executions_paginator: ListNotebookExecutionsPaginator = client.get_paginator("list_notebook_executions")
        list_security_configurations_paginator: ListSecurityConfigurationsPaginator = client.get_paginator("list_security_configurations")
        list_steps_paginator: ListStepsPaginator = client.get_paginator("list_steps")
        list_studio_session_mappings_paginator: ListStudioSessionMappingsPaginator = client.get_paginator("list_studio_session_mappings")
        list_studios_paginator: ListStudiosPaginator = client.get_paginator("list_studios")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from aiobotocore.paginate import AioPageIterator, AioPaginator

from .type_defs import (
    ListBootstrapActionsInputPaginateTypeDef,
    ListBootstrapActionsOutputTypeDef,
    ListClustersInputPaginateTypeDef,
    ListClustersOutputTypeDef,
    ListInstanceFleetsInputPaginateTypeDef,
    ListInstanceFleetsOutputPaginatorTypeDef,
    ListInstanceGroupsInputPaginateTypeDef,
    ListInstanceGroupsOutputPaginatorTypeDef,
    ListInstancesInputPaginateTypeDef,
    ListInstancesOutputTypeDef,
    ListNotebookExecutionsInputPaginateTypeDef,
    ListNotebookExecutionsOutputTypeDef,
    ListSecurityConfigurationsInputPaginateTypeDef,
    ListSecurityConfigurationsOutputTypeDef,
    ListStepsInputPaginateTypeDef,
    ListStepsOutputTypeDef,
    ListStudioSessionMappingsInputPaginateTypeDef,
    ListStudioSessionMappingsOutputTypeDef,
    ListStudiosInputPaginateTypeDef,
    ListStudiosOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = (
    "ListBootstrapActionsPaginator",
    "ListClustersPaginator",
    "ListInstanceFleetsPaginator",
    "ListInstanceGroupsPaginator",
    "ListInstancesPaginator",
    "ListNotebookExecutionsPaginator",
    "ListSecurityConfigurationsPaginator",
    "ListStepsPaginator",
    "ListStudioSessionMappingsPaginator",
    "ListStudiosPaginator",
)


if TYPE_CHECKING:
    _ListBootstrapActionsPaginatorBase = AioPaginator[ListBootstrapActionsOutputTypeDef]
else:
    _ListBootstrapActionsPaginatorBase = AioPaginator  # type: ignore[assignment]


class ListBootstrapActionsPaginator(_ListBootstrapActionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr/paginator/ListBootstrapActions.html#EMR.Paginator.ListBootstrapActions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr/paginators/#listbootstrapactionspaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBootstrapActionsInputPaginateTypeDef]
    ) -> AioPageIterator[ListBootstrapActionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr/paginator/ListBootstrapActions.html#EMR.Paginator.ListBootstrapActions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr/paginators/#listbootstrapactionspaginator)
        """


if TYPE_CHECKING:
    _ListClustersPaginatorBase = AioPaginator[ListClustersOutputTypeDef]
else:
    _ListClustersPaginatorBase = AioPaginator  # type: ignore[assignment]


class ListClustersPaginator(_ListClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr/paginator/ListClusters.html#EMR.Paginator.ListClusters)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr/paginators/#listclusterspaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListClustersInputPaginateTypeDef]
    ) -> AioPageIterator[ListClustersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr/paginator/ListClusters.html#EMR.Paginator.ListClusters.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr/paginators/#listclusterspaginator)
        """


if TYPE_CHECKING:
    _ListInstanceFleetsPaginatorBase = AioPaginator[ListInstanceFleetsOutputPaginatorTypeDef]
else:
    _ListInstanceFleetsPaginatorBase = AioPaginator  # type: ignore[assignment]


class ListInstanceFleetsPaginator(_ListInstanceFleetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr/paginator/ListInstanceFleets.html#EMR.Paginator.ListInstanceFleets)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr/paginators/#listinstancefleetspaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInstanceFleetsInputPaginateTypeDef]
    ) -> AioPageIterator[ListInstanceFleetsOutputPaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr/paginator/ListInstanceFleets.html#EMR.Paginator.ListInstanceFleets.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr/paginators/#listinstancefleetspaginator)
        """


if TYPE_CHECKING:
    _ListInstanceGroupsPaginatorBase = AioPaginator[ListInstanceGroupsOutputPaginatorTypeDef]
else:
    _ListInstanceGroupsPaginatorBase = AioPaginator  # type: ignore[assignment]


class ListInstanceGroupsPaginator(_ListInstanceGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr/paginator/ListInstanceGroups.html#EMR.Paginator.ListInstanceGroups)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr/paginators/#listinstancegroupspaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInstanceGroupsInputPaginateTypeDef]
    ) -> AioPageIterator[ListInstanceGroupsOutputPaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr/paginator/ListInstanceGroups.html#EMR.Paginator.ListInstanceGroups.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr/paginators/#listinstancegroupspaginator)
        """


if TYPE_CHECKING:
    _ListInstancesPaginatorBase = AioPaginator[ListInstancesOutputTypeDef]
else:
    _ListInstancesPaginatorBase = AioPaginator  # type: ignore[assignment]


class ListInstancesPaginator(_ListInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr/paginator/ListInstances.html#EMR.Paginator.ListInstances)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr/paginators/#listinstancespaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInstancesInputPaginateTypeDef]
    ) -> AioPageIterator[ListInstancesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr/paginator/ListInstances.html#EMR.Paginator.ListInstances.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr/paginators/#listinstancespaginator)
        """


if TYPE_CHECKING:
    _ListNotebookExecutionsPaginatorBase = AioPaginator[ListNotebookExecutionsOutputTypeDef]
else:
    _ListNotebookExecutionsPaginatorBase = AioPaginator  # type: ignore[assignment]


class ListNotebookExecutionsPaginator(_ListNotebookExecutionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr/paginator/ListNotebookExecutions.html#EMR.Paginator.ListNotebookExecutions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr/paginators/#listnotebookexecutionspaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListNotebookExecutionsInputPaginateTypeDef]
    ) -> AioPageIterator[ListNotebookExecutionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr/paginator/ListNotebookExecutions.html#EMR.Paginator.ListNotebookExecutions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr/paginators/#listnotebookexecutionspaginator)
        """


if TYPE_CHECKING:
    _ListSecurityConfigurationsPaginatorBase = AioPaginator[ListSecurityConfigurationsOutputTypeDef]
else:
    _ListSecurityConfigurationsPaginatorBase = AioPaginator  # type: ignore[assignment]


class ListSecurityConfigurationsPaginator(_ListSecurityConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr/paginator/ListSecurityConfigurations.html#EMR.Paginator.ListSecurityConfigurations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr/paginators/#listsecurityconfigurationspaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSecurityConfigurationsInputPaginateTypeDef]
    ) -> AioPageIterator[ListSecurityConfigurationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr/paginator/ListSecurityConfigurations.html#EMR.Paginator.ListSecurityConfigurations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr/paginators/#listsecurityconfigurationspaginator)
        """


if TYPE_CHECKING:
    _ListStepsPaginatorBase = AioPaginator[ListStepsOutputTypeDef]
else:
    _ListStepsPaginatorBase = AioPaginator  # type: ignore[assignment]


class ListStepsPaginator(_ListStepsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr/paginator/ListSteps.html#EMR.Paginator.ListSteps)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr/paginators/#liststepspaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStepsInputPaginateTypeDef]
    ) -> AioPageIterator[ListStepsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr/paginator/ListSteps.html#EMR.Paginator.ListSteps.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr/paginators/#liststepspaginator)
        """


if TYPE_CHECKING:
    _ListStudioSessionMappingsPaginatorBase = AioPaginator[ListStudioSessionMappingsOutputTypeDef]
else:
    _ListStudioSessionMappingsPaginatorBase = AioPaginator  # type: ignore[assignment]


class ListStudioSessionMappingsPaginator(_ListStudioSessionMappingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr/paginator/ListStudioSessionMappings.html#EMR.Paginator.ListStudioSessionMappings)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr/paginators/#liststudiosessionmappingspaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStudioSessionMappingsInputPaginateTypeDef]
    ) -> AioPageIterator[ListStudioSessionMappingsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr/paginator/ListStudioSessionMappings.html#EMR.Paginator.ListStudioSessionMappings.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr/paginators/#liststudiosessionmappingspaginator)
        """


if TYPE_CHECKING:
    _ListStudiosPaginatorBase = AioPaginator[ListStudiosOutputTypeDef]
else:
    _ListStudiosPaginatorBase = AioPaginator  # type: ignore[assignment]


class ListStudiosPaginator(_ListStudiosPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr/paginator/ListStudios.html#EMR.Paginator.ListStudios)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr/paginators/#liststudiospaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStudiosInputPaginateTypeDef]
    ) -> AioPageIterator[ListStudiosOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr/paginator/ListStudios.html#EMR.Paginator.ListStudios.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr/paginators/#liststudiospaginator)
        """
