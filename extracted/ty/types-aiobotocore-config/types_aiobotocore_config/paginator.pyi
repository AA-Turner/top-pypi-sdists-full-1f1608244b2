"""
Type annotations for config service client paginators.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_config.client import ConfigServiceClient
    from types_aiobotocore_config.paginator import (
        DescribeAggregateComplianceByConfigRulesPaginator,
        DescribeAggregateComplianceByConformancePacksPaginator,
        DescribeAggregationAuthorizationsPaginator,
        DescribeComplianceByConfigRulePaginator,
        DescribeComplianceByResourcePaginator,
        DescribeConfigRuleEvaluationStatusPaginator,
        DescribeConfigRulesPaginator,
        DescribeConfigurationAggregatorSourcesStatusPaginator,
        DescribeConfigurationAggregatorsPaginator,
        DescribeConformancePackStatusPaginator,
        DescribeConformancePacksPaginator,
        DescribeOrganizationConfigRuleStatusesPaginator,
        DescribeOrganizationConfigRulesPaginator,
        DescribeOrganizationConformancePackStatusesPaginator,
        DescribeOrganizationConformancePacksPaginator,
        DescribePendingAggregationRequestsPaginator,
        DescribeRemediationExecutionStatusPaginator,
        DescribeRetentionConfigurationsPaginator,
        GetAggregateComplianceDetailsByConfigRulePaginator,
        GetComplianceDetailsByConfigRulePaginator,
        GetComplianceDetailsByResourcePaginator,
        GetConformancePackComplianceSummaryPaginator,
        GetOrganizationConfigRuleDetailedStatusPaginator,
        GetOrganizationConformancePackDetailedStatusPaginator,
        GetResourceConfigHistoryPaginator,
        ListAggregateDiscoveredResourcesPaginator,
        ListConfigurationRecordersPaginator,
        ListDiscoveredResourcesPaginator,
        ListResourceEvaluationsPaginator,
        ListTagsForResourcePaginator,
        SelectAggregateResourceConfigPaginator,
        SelectResourceConfigPaginator,
    )

    session = get_session()
    with session.create_client("config") as client:
        client: ConfigServiceClient

        describe_aggregate_compliance_by_config_rules_paginator: DescribeAggregateComplianceByConfigRulesPaginator = client.get_paginator("describe_aggregate_compliance_by_config_rules")
        describe_aggregate_compliance_by_conformance_packs_paginator: DescribeAggregateComplianceByConformancePacksPaginator = client.get_paginator("describe_aggregate_compliance_by_conformance_packs")
        describe_aggregation_authorizations_paginator: DescribeAggregationAuthorizationsPaginator = client.get_paginator("describe_aggregation_authorizations")
        describe_compliance_by_config_rule_paginator: DescribeComplianceByConfigRulePaginator = client.get_paginator("describe_compliance_by_config_rule")
        describe_compliance_by_resource_paginator: DescribeComplianceByResourcePaginator = client.get_paginator("describe_compliance_by_resource")
        describe_config_rule_evaluation_status_paginator: DescribeConfigRuleEvaluationStatusPaginator = client.get_paginator("describe_config_rule_evaluation_status")
        describe_config_rules_paginator: DescribeConfigRulesPaginator = client.get_paginator("describe_config_rules")
        describe_configuration_aggregator_sources_status_paginator: DescribeConfigurationAggregatorSourcesStatusPaginator = client.get_paginator("describe_configuration_aggregator_sources_status")
        describe_configuration_aggregators_paginator: DescribeConfigurationAggregatorsPaginator = client.get_paginator("describe_configuration_aggregators")
        describe_conformance_pack_status_paginator: DescribeConformancePackStatusPaginator = client.get_paginator("describe_conformance_pack_status")
        describe_conformance_packs_paginator: DescribeConformancePacksPaginator = client.get_paginator("describe_conformance_packs")
        describe_organization_config_rule_statuses_paginator: DescribeOrganizationConfigRuleStatusesPaginator = client.get_paginator("describe_organization_config_rule_statuses")
        describe_organization_config_rules_paginator: DescribeOrganizationConfigRulesPaginator = client.get_paginator("describe_organization_config_rules")
        describe_organization_conformance_pack_statuses_paginator: DescribeOrganizationConformancePackStatusesPaginator = client.get_paginator("describe_organization_conformance_pack_statuses")
        describe_organization_conformance_packs_paginator: DescribeOrganizationConformancePacksPaginator = client.get_paginator("describe_organization_conformance_packs")
        describe_pending_aggregation_requests_paginator: DescribePendingAggregationRequestsPaginator = client.get_paginator("describe_pending_aggregation_requests")
        describe_remediation_execution_status_paginator: DescribeRemediationExecutionStatusPaginator = client.get_paginator("describe_remediation_execution_status")
        describe_retention_configurations_paginator: DescribeRetentionConfigurationsPaginator = client.get_paginator("describe_retention_configurations")
        get_aggregate_compliance_details_by_config_rule_paginator: GetAggregateComplianceDetailsByConfigRulePaginator = client.get_paginator("get_aggregate_compliance_details_by_config_rule")
        get_compliance_details_by_config_rule_paginator: GetComplianceDetailsByConfigRulePaginator = client.get_paginator("get_compliance_details_by_config_rule")
        get_compliance_details_by_resource_paginator: GetComplianceDetailsByResourcePaginator = client.get_paginator("get_compliance_details_by_resource")
        get_conformance_pack_compliance_summary_paginator: GetConformancePackComplianceSummaryPaginator = client.get_paginator("get_conformance_pack_compliance_summary")
        get_organization_config_rule_detailed_status_paginator: GetOrganizationConfigRuleDetailedStatusPaginator = client.get_paginator("get_organization_config_rule_detailed_status")
        get_organization_conformance_pack_detailed_status_paginator: GetOrganizationConformancePackDetailedStatusPaginator = client.get_paginator("get_organization_conformance_pack_detailed_status")
        get_resource_config_history_paginator: GetResourceConfigHistoryPaginator = client.get_paginator("get_resource_config_history")
        list_aggregate_discovered_resources_paginator: ListAggregateDiscoveredResourcesPaginator = client.get_paginator("list_aggregate_discovered_resources")
        list_configuration_recorders_paginator: ListConfigurationRecordersPaginator = client.get_paginator("list_configuration_recorders")
        list_discovered_resources_paginator: ListDiscoveredResourcesPaginator = client.get_paginator("list_discovered_resources")
        list_resource_evaluations_paginator: ListResourceEvaluationsPaginator = client.get_paginator("list_resource_evaluations")
        list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
        select_aggregate_resource_config_paginator: SelectAggregateResourceConfigPaginator = client.get_paginator("select_aggregate_resource_config")
        select_resource_config_paginator: SelectResourceConfigPaginator = client.get_paginator("select_resource_config")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from aiobotocore.paginate import AioPageIterator, AioPaginator

from .type_defs import (
    DescribeAggregateComplianceByConfigRulesRequestPaginateTypeDef,
    DescribeAggregateComplianceByConfigRulesResponseTypeDef,
    DescribeAggregateComplianceByConformancePacksRequestPaginateTypeDef,
    DescribeAggregateComplianceByConformancePacksResponseTypeDef,
    DescribeAggregationAuthorizationsRequestPaginateTypeDef,
    DescribeAggregationAuthorizationsResponseTypeDef,
    DescribeComplianceByConfigRuleRequestPaginateTypeDef,
    DescribeComplianceByConfigRuleResponseTypeDef,
    DescribeComplianceByResourceRequestPaginateTypeDef,
    DescribeComplianceByResourceResponseTypeDef,
    DescribeConfigRuleEvaluationStatusRequestPaginateTypeDef,
    DescribeConfigRuleEvaluationStatusResponseTypeDef,
    DescribeConfigRulesRequestPaginateTypeDef,
    DescribeConfigRulesResponseTypeDef,
    DescribeConfigurationAggregatorSourcesStatusRequestPaginateTypeDef,
    DescribeConfigurationAggregatorSourcesStatusResponseTypeDef,
    DescribeConfigurationAggregatorsRequestPaginateTypeDef,
    DescribeConfigurationAggregatorsResponseTypeDef,
    DescribeConformancePacksRequestPaginateTypeDef,
    DescribeConformancePacksResponseTypeDef,
    DescribeConformancePackStatusRequestPaginateTypeDef,
    DescribeConformancePackStatusResponseTypeDef,
    DescribeOrganizationConfigRulesRequestPaginateTypeDef,
    DescribeOrganizationConfigRulesResponseTypeDef,
    DescribeOrganizationConfigRuleStatusesRequestPaginateTypeDef,
    DescribeOrganizationConfigRuleStatusesResponseTypeDef,
    DescribeOrganizationConformancePacksRequestPaginateTypeDef,
    DescribeOrganizationConformancePacksResponseTypeDef,
    DescribeOrganizationConformancePackStatusesRequestPaginateTypeDef,
    DescribeOrganizationConformancePackStatusesResponseTypeDef,
    DescribePendingAggregationRequestsRequestPaginateTypeDef,
    DescribePendingAggregationRequestsResponseTypeDef,
    DescribeRemediationExecutionStatusRequestPaginateTypeDef,
    DescribeRemediationExecutionStatusResponseTypeDef,
    DescribeRetentionConfigurationsRequestPaginateTypeDef,
    DescribeRetentionConfigurationsResponseTypeDef,
    GetAggregateComplianceDetailsByConfigRuleRequestPaginateTypeDef,
    GetAggregateComplianceDetailsByConfigRuleResponseTypeDef,
    GetComplianceDetailsByConfigRuleRequestPaginateTypeDef,
    GetComplianceDetailsByConfigRuleResponseTypeDef,
    GetComplianceDetailsByResourceRequestPaginateTypeDef,
    GetComplianceDetailsByResourceResponseTypeDef,
    GetConformancePackComplianceSummaryRequestPaginateTypeDef,
    GetConformancePackComplianceSummaryResponseTypeDef,
    GetOrganizationConfigRuleDetailedStatusRequestPaginateTypeDef,
    GetOrganizationConfigRuleDetailedStatusResponseTypeDef,
    GetOrganizationConformancePackDetailedStatusRequestPaginateTypeDef,
    GetOrganizationConformancePackDetailedStatusResponseTypeDef,
    GetResourceConfigHistoryRequestPaginateTypeDef,
    GetResourceConfigHistoryResponseTypeDef,
    ListAggregateDiscoveredResourcesRequestPaginateTypeDef,
    ListAggregateDiscoveredResourcesResponseTypeDef,
    ListConfigurationRecordersRequestPaginateTypeDef,
    ListConfigurationRecordersResponseTypeDef,
    ListDiscoveredResourcesRequestPaginateTypeDef,
    ListDiscoveredResourcesResponseTypeDef,
    ListResourceEvaluationsRequestPaginateTypeDef,
    ListResourceEvaluationsResponseTypeDef,
    ListTagsForResourceRequestPaginateTypeDef,
    ListTagsForResourceResponseTypeDef,
    SelectAggregateResourceConfigRequestPaginateTypeDef,
    SelectAggregateResourceConfigResponseTypeDef,
    SelectResourceConfigRequestPaginateTypeDef,
    SelectResourceConfigResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeAggregateComplianceByConfigRulesPaginator",
    "DescribeAggregateComplianceByConformancePacksPaginator",
    "DescribeAggregationAuthorizationsPaginator",
    "DescribeComplianceByConfigRulePaginator",
    "DescribeComplianceByResourcePaginator",
    "DescribeConfigRuleEvaluationStatusPaginator",
    "DescribeConfigRulesPaginator",
    "DescribeConfigurationAggregatorSourcesStatusPaginator",
    "DescribeConfigurationAggregatorsPaginator",
    "DescribeConformancePackStatusPaginator",
    "DescribeConformancePacksPaginator",
    "DescribeOrganizationConfigRuleStatusesPaginator",
    "DescribeOrganizationConfigRulesPaginator",
    "DescribeOrganizationConformancePackStatusesPaginator",
    "DescribeOrganizationConformancePacksPaginator",
    "DescribePendingAggregationRequestsPaginator",
    "DescribeRemediationExecutionStatusPaginator",
    "DescribeRetentionConfigurationsPaginator",
    "GetAggregateComplianceDetailsByConfigRulePaginator",
    "GetComplianceDetailsByConfigRulePaginator",
    "GetComplianceDetailsByResourcePaginator",
    "GetConformancePackComplianceSummaryPaginator",
    "GetOrganizationConfigRuleDetailedStatusPaginator",
    "GetOrganizationConformancePackDetailedStatusPaginator",
    "GetResourceConfigHistoryPaginator",
    "ListAggregateDiscoveredResourcesPaginator",
    "ListConfigurationRecordersPaginator",
    "ListDiscoveredResourcesPaginator",
    "ListResourceEvaluationsPaginator",
    "ListTagsForResourcePaginator",
    "SelectAggregateResourceConfigPaginator",
    "SelectResourceConfigPaginator",
)

if TYPE_CHECKING:
    _DescribeAggregateComplianceByConfigRulesPaginatorBase = AioPaginator[
        DescribeAggregateComplianceByConfigRulesResponseTypeDef
    ]
else:
    _DescribeAggregateComplianceByConfigRulesPaginatorBase = AioPaginator  # type: ignore[assignment]

class DescribeAggregateComplianceByConfigRulesPaginator(
    _DescribeAggregateComplianceByConfigRulesPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeAggregateComplianceByConfigRules.html#ConfigService.Paginator.DescribeAggregateComplianceByConfigRules)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeaggregatecompliancebyconfigrulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAggregateComplianceByConfigRulesRequestPaginateTypeDef]
    ) -> AioPageIterator[DescribeAggregateComplianceByConfigRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeAggregateComplianceByConfigRules.html#ConfigService.Paginator.DescribeAggregateComplianceByConfigRules.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeaggregatecompliancebyconfigrulespaginator)
        """

if TYPE_CHECKING:
    _DescribeAggregateComplianceByConformancePacksPaginatorBase = AioPaginator[
        DescribeAggregateComplianceByConformancePacksResponseTypeDef
    ]
else:
    _DescribeAggregateComplianceByConformancePacksPaginatorBase = AioPaginator  # type: ignore[assignment]

class DescribeAggregateComplianceByConformancePacksPaginator(
    _DescribeAggregateComplianceByConformancePacksPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeAggregateComplianceByConformancePacks.html#ConfigService.Paginator.DescribeAggregateComplianceByConformancePacks)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeaggregatecompliancebyconformancepackspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAggregateComplianceByConformancePacksRequestPaginateTypeDef]
    ) -> AioPageIterator[DescribeAggregateComplianceByConformancePacksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeAggregateComplianceByConformancePacks.html#ConfigService.Paginator.DescribeAggregateComplianceByConformancePacks.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeaggregatecompliancebyconformancepackspaginator)
        """

if TYPE_CHECKING:
    _DescribeAggregationAuthorizationsPaginatorBase = AioPaginator[
        DescribeAggregationAuthorizationsResponseTypeDef
    ]
else:
    _DescribeAggregationAuthorizationsPaginatorBase = AioPaginator  # type: ignore[assignment]

class DescribeAggregationAuthorizationsPaginator(_DescribeAggregationAuthorizationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeAggregationAuthorizations.html#ConfigService.Paginator.DescribeAggregationAuthorizations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeaggregationauthorizationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAggregationAuthorizationsRequestPaginateTypeDef]
    ) -> AioPageIterator[DescribeAggregationAuthorizationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeAggregationAuthorizations.html#ConfigService.Paginator.DescribeAggregationAuthorizations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeaggregationauthorizationspaginator)
        """

if TYPE_CHECKING:
    _DescribeComplianceByConfigRulePaginatorBase = AioPaginator[
        DescribeComplianceByConfigRuleResponseTypeDef
    ]
else:
    _DescribeComplianceByConfigRulePaginatorBase = AioPaginator  # type: ignore[assignment]

class DescribeComplianceByConfigRulePaginator(_DescribeComplianceByConfigRulePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeComplianceByConfigRule.html#ConfigService.Paginator.DescribeComplianceByConfigRule)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describecompliancebyconfigrulepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeComplianceByConfigRuleRequestPaginateTypeDef]
    ) -> AioPageIterator[DescribeComplianceByConfigRuleResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeComplianceByConfigRule.html#ConfigService.Paginator.DescribeComplianceByConfigRule.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describecompliancebyconfigrulepaginator)
        """

if TYPE_CHECKING:
    _DescribeComplianceByResourcePaginatorBase = AioPaginator[
        DescribeComplianceByResourceResponseTypeDef
    ]
else:
    _DescribeComplianceByResourcePaginatorBase = AioPaginator  # type: ignore[assignment]

class DescribeComplianceByResourcePaginator(_DescribeComplianceByResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeComplianceByResource.html#ConfigService.Paginator.DescribeComplianceByResource)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describecompliancebyresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeComplianceByResourceRequestPaginateTypeDef]
    ) -> AioPageIterator[DescribeComplianceByResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeComplianceByResource.html#ConfigService.Paginator.DescribeComplianceByResource.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describecompliancebyresourcepaginator)
        """

if TYPE_CHECKING:
    _DescribeConfigRuleEvaluationStatusPaginatorBase = AioPaginator[
        DescribeConfigRuleEvaluationStatusResponseTypeDef
    ]
else:
    _DescribeConfigRuleEvaluationStatusPaginatorBase = AioPaginator  # type: ignore[assignment]

class DescribeConfigRuleEvaluationStatusPaginator(_DescribeConfigRuleEvaluationStatusPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeConfigRuleEvaluationStatus.html#ConfigService.Paginator.DescribeConfigRuleEvaluationStatus)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeconfigruleevaluationstatuspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeConfigRuleEvaluationStatusRequestPaginateTypeDef]
    ) -> AioPageIterator[DescribeConfigRuleEvaluationStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeConfigRuleEvaluationStatus.html#ConfigService.Paginator.DescribeConfigRuleEvaluationStatus.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeconfigruleevaluationstatuspaginator)
        """

if TYPE_CHECKING:
    _DescribeConfigRulesPaginatorBase = AioPaginator[DescribeConfigRulesResponseTypeDef]
else:
    _DescribeConfigRulesPaginatorBase = AioPaginator  # type: ignore[assignment]

class DescribeConfigRulesPaginator(_DescribeConfigRulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeConfigRules.html#ConfigService.Paginator.DescribeConfigRules)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeconfigrulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeConfigRulesRequestPaginateTypeDef]
    ) -> AioPageIterator[DescribeConfigRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeConfigRules.html#ConfigService.Paginator.DescribeConfigRules.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeconfigrulespaginator)
        """

if TYPE_CHECKING:
    _DescribeConfigurationAggregatorSourcesStatusPaginatorBase = AioPaginator[
        DescribeConfigurationAggregatorSourcesStatusResponseTypeDef
    ]
else:
    _DescribeConfigurationAggregatorSourcesStatusPaginatorBase = AioPaginator  # type: ignore[assignment]

class DescribeConfigurationAggregatorSourcesStatusPaginator(
    _DescribeConfigurationAggregatorSourcesStatusPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeConfigurationAggregatorSourcesStatus.html#ConfigService.Paginator.DescribeConfigurationAggregatorSourcesStatus)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeconfigurationaggregatorsourcesstatuspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeConfigurationAggregatorSourcesStatusRequestPaginateTypeDef]
    ) -> AioPageIterator[DescribeConfigurationAggregatorSourcesStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeConfigurationAggregatorSourcesStatus.html#ConfigService.Paginator.DescribeConfigurationAggregatorSourcesStatus.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeconfigurationaggregatorsourcesstatuspaginator)
        """

if TYPE_CHECKING:
    _DescribeConfigurationAggregatorsPaginatorBase = AioPaginator[
        DescribeConfigurationAggregatorsResponseTypeDef
    ]
else:
    _DescribeConfigurationAggregatorsPaginatorBase = AioPaginator  # type: ignore[assignment]

class DescribeConfigurationAggregatorsPaginator(_DescribeConfigurationAggregatorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeConfigurationAggregators.html#ConfigService.Paginator.DescribeConfigurationAggregators)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeconfigurationaggregatorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeConfigurationAggregatorsRequestPaginateTypeDef]
    ) -> AioPageIterator[DescribeConfigurationAggregatorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeConfigurationAggregators.html#ConfigService.Paginator.DescribeConfigurationAggregators.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeconfigurationaggregatorspaginator)
        """

if TYPE_CHECKING:
    _DescribeConformancePackStatusPaginatorBase = AioPaginator[
        DescribeConformancePackStatusResponseTypeDef
    ]
else:
    _DescribeConformancePackStatusPaginatorBase = AioPaginator  # type: ignore[assignment]

class DescribeConformancePackStatusPaginator(_DescribeConformancePackStatusPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeConformancePackStatus.html#ConfigService.Paginator.DescribeConformancePackStatus)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeconformancepackstatuspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeConformancePackStatusRequestPaginateTypeDef]
    ) -> AioPageIterator[DescribeConformancePackStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeConformancePackStatus.html#ConfigService.Paginator.DescribeConformancePackStatus.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeconformancepackstatuspaginator)
        """

if TYPE_CHECKING:
    _DescribeConformancePacksPaginatorBase = AioPaginator[DescribeConformancePacksResponseTypeDef]
else:
    _DescribeConformancePacksPaginatorBase = AioPaginator  # type: ignore[assignment]

class DescribeConformancePacksPaginator(_DescribeConformancePacksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeConformancePacks.html#ConfigService.Paginator.DescribeConformancePacks)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeconformancepackspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeConformancePacksRequestPaginateTypeDef]
    ) -> AioPageIterator[DescribeConformancePacksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeConformancePacks.html#ConfigService.Paginator.DescribeConformancePacks.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeconformancepackspaginator)
        """

if TYPE_CHECKING:
    _DescribeOrganizationConfigRuleStatusesPaginatorBase = AioPaginator[
        DescribeOrganizationConfigRuleStatusesResponseTypeDef
    ]
else:
    _DescribeOrganizationConfigRuleStatusesPaginatorBase = AioPaginator  # type: ignore[assignment]

class DescribeOrganizationConfigRuleStatusesPaginator(
    _DescribeOrganizationConfigRuleStatusesPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeOrganizationConfigRuleStatuses.html#ConfigService.Paginator.DescribeOrganizationConfigRuleStatuses)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeorganizationconfigrulestatusespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeOrganizationConfigRuleStatusesRequestPaginateTypeDef]
    ) -> AioPageIterator[DescribeOrganizationConfigRuleStatusesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeOrganizationConfigRuleStatuses.html#ConfigService.Paginator.DescribeOrganizationConfigRuleStatuses.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeorganizationconfigrulestatusespaginator)
        """

if TYPE_CHECKING:
    _DescribeOrganizationConfigRulesPaginatorBase = AioPaginator[
        DescribeOrganizationConfigRulesResponseTypeDef
    ]
else:
    _DescribeOrganizationConfigRulesPaginatorBase = AioPaginator  # type: ignore[assignment]

class DescribeOrganizationConfigRulesPaginator(_DescribeOrganizationConfigRulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeOrganizationConfigRules.html#ConfigService.Paginator.DescribeOrganizationConfigRules)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeorganizationconfigrulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeOrganizationConfigRulesRequestPaginateTypeDef]
    ) -> AioPageIterator[DescribeOrganizationConfigRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeOrganizationConfigRules.html#ConfigService.Paginator.DescribeOrganizationConfigRules.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeorganizationconfigrulespaginator)
        """

if TYPE_CHECKING:
    _DescribeOrganizationConformancePackStatusesPaginatorBase = AioPaginator[
        DescribeOrganizationConformancePackStatusesResponseTypeDef
    ]
else:
    _DescribeOrganizationConformancePackStatusesPaginatorBase = AioPaginator  # type: ignore[assignment]

class DescribeOrganizationConformancePackStatusesPaginator(
    _DescribeOrganizationConformancePackStatusesPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeOrganizationConformancePackStatuses.html#ConfigService.Paginator.DescribeOrganizationConformancePackStatuses)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeorganizationconformancepackstatusespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeOrganizationConformancePackStatusesRequestPaginateTypeDef]
    ) -> AioPageIterator[DescribeOrganizationConformancePackStatusesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeOrganizationConformancePackStatuses.html#ConfigService.Paginator.DescribeOrganizationConformancePackStatuses.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeorganizationconformancepackstatusespaginator)
        """

if TYPE_CHECKING:
    _DescribeOrganizationConformancePacksPaginatorBase = AioPaginator[
        DescribeOrganizationConformancePacksResponseTypeDef
    ]
else:
    _DescribeOrganizationConformancePacksPaginatorBase = AioPaginator  # type: ignore[assignment]

class DescribeOrganizationConformancePacksPaginator(
    _DescribeOrganizationConformancePacksPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeOrganizationConformancePacks.html#ConfigService.Paginator.DescribeOrganizationConformancePacks)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeorganizationconformancepackspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeOrganizationConformancePacksRequestPaginateTypeDef]
    ) -> AioPageIterator[DescribeOrganizationConformancePacksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeOrganizationConformancePacks.html#ConfigService.Paginator.DescribeOrganizationConformancePacks.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeorganizationconformancepackspaginator)
        """

if TYPE_CHECKING:
    _DescribePendingAggregationRequestsPaginatorBase = AioPaginator[
        DescribePendingAggregationRequestsResponseTypeDef
    ]
else:
    _DescribePendingAggregationRequestsPaginatorBase = AioPaginator  # type: ignore[assignment]

class DescribePendingAggregationRequestsPaginator(_DescribePendingAggregationRequestsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribePendingAggregationRequests.html#ConfigService.Paginator.DescribePendingAggregationRequests)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describependingaggregationrequestspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribePendingAggregationRequestsRequestPaginateTypeDef]
    ) -> AioPageIterator[DescribePendingAggregationRequestsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribePendingAggregationRequests.html#ConfigService.Paginator.DescribePendingAggregationRequests.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describependingaggregationrequestspaginator)
        """

if TYPE_CHECKING:
    _DescribeRemediationExecutionStatusPaginatorBase = AioPaginator[
        DescribeRemediationExecutionStatusResponseTypeDef
    ]
else:
    _DescribeRemediationExecutionStatusPaginatorBase = AioPaginator  # type: ignore[assignment]

class DescribeRemediationExecutionStatusPaginator(_DescribeRemediationExecutionStatusPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeRemediationExecutionStatus.html#ConfigService.Paginator.DescribeRemediationExecutionStatus)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeremediationexecutionstatuspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeRemediationExecutionStatusRequestPaginateTypeDef]
    ) -> AioPageIterator[DescribeRemediationExecutionStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeRemediationExecutionStatus.html#ConfigService.Paginator.DescribeRemediationExecutionStatus.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeremediationexecutionstatuspaginator)
        """

if TYPE_CHECKING:
    _DescribeRetentionConfigurationsPaginatorBase = AioPaginator[
        DescribeRetentionConfigurationsResponseTypeDef
    ]
else:
    _DescribeRetentionConfigurationsPaginatorBase = AioPaginator  # type: ignore[assignment]

class DescribeRetentionConfigurationsPaginator(_DescribeRetentionConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeRetentionConfigurations.html#ConfigService.Paginator.DescribeRetentionConfigurations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeretentionconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeRetentionConfigurationsRequestPaginateTypeDef]
    ) -> AioPageIterator[DescribeRetentionConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/DescribeRetentionConfigurations.html#ConfigService.Paginator.DescribeRetentionConfigurations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#describeretentionconfigurationspaginator)
        """

if TYPE_CHECKING:
    _GetAggregateComplianceDetailsByConfigRulePaginatorBase = AioPaginator[
        GetAggregateComplianceDetailsByConfigRuleResponseTypeDef
    ]
else:
    _GetAggregateComplianceDetailsByConfigRulePaginatorBase = AioPaginator  # type: ignore[assignment]

class GetAggregateComplianceDetailsByConfigRulePaginator(
    _GetAggregateComplianceDetailsByConfigRulePaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/GetAggregateComplianceDetailsByConfigRule.html#ConfigService.Paginator.GetAggregateComplianceDetailsByConfigRule)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#getaggregatecompliancedetailsbyconfigrulepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetAggregateComplianceDetailsByConfigRuleRequestPaginateTypeDef]
    ) -> AioPageIterator[GetAggregateComplianceDetailsByConfigRuleResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/GetAggregateComplianceDetailsByConfigRule.html#ConfigService.Paginator.GetAggregateComplianceDetailsByConfigRule.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#getaggregatecompliancedetailsbyconfigrulepaginator)
        """

if TYPE_CHECKING:
    _GetComplianceDetailsByConfigRulePaginatorBase = AioPaginator[
        GetComplianceDetailsByConfigRuleResponseTypeDef
    ]
else:
    _GetComplianceDetailsByConfigRulePaginatorBase = AioPaginator  # type: ignore[assignment]

class GetComplianceDetailsByConfigRulePaginator(_GetComplianceDetailsByConfigRulePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/GetComplianceDetailsByConfigRule.html#ConfigService.Paginator.GetComplianceDetailsByConfigRule)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#getcompliancedetailsbyconfigrulepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetComplianceDetailsByConfigRuleRequestPaginateTypeDef]
    ) -> AioPageIterator[GetComplianceDetailsByConfigRuleResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/GetComplianceDetailsByConfigRule.html#ConfigService.Paginator.GetComplianceDetailsByConfigRule.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#getcompliancedetailsbyconfigrulepaginator)
        """

if TYPE_CHECKING:
    _GetComplianceDetailsByResourcePaginatorBase = AioPaginator[
        GetComplianceDetailsByResourceResponseTypeDef
    ]
else:
    _GetComplianceDetailsByResourcePaginatorBase = AioPaginator  # type: ignore[assignment]

class GetComplianceDetailsByResourcePaginator(_GetComplianceDetailsByResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/GetComplianceDetailsByResource.html#ConfigService.Paginator.GetComplianceDetailsByResource)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#getcompliancedetailsbyresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetComplianceDetailsByResourceRequestPaginateTypeDef]
    ) -> AioPageIterator[GetComplianceDetailsByResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/GetComplianceDetailsByResource.html#ConfigService.Paginator.GetComplianceDetailsByResource.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#getcompliancedetailsbyresourcepaginator)
        """

if TYPE_CHECKING:
    _GetConformancePackComplianceSummaryPaginatorBase = AioPaginator[
        GetConformancePackComplianceSummaryResponseTypeDef
    ]
else:
    _GetConformancePackComplianceSummaryPaginatorBase = AioPaginator  # type: ignore[assignment]

class GetConformancePackComplianceSummaryPaginator(
    _GetConformancePackComplianceSummaryPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/GetConformancePackComplianceSummary.html#ConfigService.Paginator.GetConformancePackComplianceSummary)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#getconformancepackcompliancesummarypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetConformancePackComplianceSummaryRequestPaginateTypeDef]
    ) -> AioPageIterator[GetConformancePackComplianceSummaryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/GetConformancePackComplianceSummary.html#ConfigService.Paginator.GetConformancePackComplianceSummary.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#getconformancepackcompliancesummarypaginator)
        """

if TYPE_CHECKING:
    _GetOrganizationConfigRuleDetailedStatusPaginatorBase = AioPaginator[
        GetOrganizationConfigRuleDetailedStatusResponseTypeDef
    ]
else:
    _GetOrganizationConfigRuleDetailedStatusPaginatorBase = AioPaginator  # type: ignore[assignment]

class GetOrganizationConfigRuleDetailedStatusPaginator(
    _GetOrganizationConfigRuleDetailedStatusPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/GetOrganizationConfigRuleDetailedStatus.html#ConfigService.Paginator.GetOrganizationConfigRuleDetailedStatus)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#getorganizationconfigruledetailedstatuspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetOrganizationConfigRuleDetailedStatusRequestPaginateTypeDef]
    ) -> AioPageIterator[GetOrganizationConfigRuleDetailedStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/GetOrganizationConfigRuleDetailedStatus.html#ConfigService.Paginator.GetOrganizationConfigRuleDetailedStatus.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#getorganizationconfigruledetailedstatuspaginator)
        """

if TYPE_CHECKING:
    _GetOrganizationConformancePackDetailedStatusPaginatorBase = AioPaginator[
        GetOrganizationConformancePackDetailedStatusResponseTypeDef
    ]
else:
    _GetOrganizationConformancePackDetailedStatusPaginatorBase = AioPaginator  # type: ignore[assignment]

class GetOrganizationConformancePackDetailedStatusPaginator(
    _GetOrganizationConformancePackDetailedStatusPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/GetOrganizationConformancePackDetailedStatus.html#ConfigService.Paginator.GetOrganizationConformancePackDetailedStatus)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#getorganizationconformancepackdetailedstatuspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetOrganizationConformancePackDetailedStatusRequestPaginateTypeDef]
    ) -> AioPageIterator[GetOrganizationConformancePackDetailedStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/GetOrganizationConformancePackDetailedStatus.html#ConfigService.Paginator.GetOrganizationConformancePackDetailedStatus.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#getorganizationconformancepackdetailedstatuspaginator)
        """

if TYPE_CHECKING:
    _GetResourceConfigHistoryPaginatorBase = AioPaginator[GetResourceConfigHistoryResponseTypeDef]
else:
    _GetResourceConfigHistoryPaginatorBase = AioPaginator  # type: ignore[assignment]

class GetResourceConfigHistoryPaginator(_GetResourceConfigHistoryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/GetResourceConfigHistory.html#ConfigService.Paginator.GetResourceConfigHistory)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#getresourceconfighistorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetResourceConfigHistoryRequestPaginateTypeDef]
    ) -> AioPageIterator[GetResourceConfigHistoryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/GetResourceConfigHistory.html#ConfigService.Paginator.GetResourceConfigHistory.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#getresourceconfighistorypaginator)
        """

if TYPE_CHECKING:
    _ListAggregateDiscoveredResourcesPaginatorBase = AioPaginator[
        ListAggregateDiscoveredResourcesResponseTypeDef
    ]
else:
    _ListAggregateDiscoveredResourcesPaginatorBase = AioPaginator  # type: ignore[assignment]

class ListAggregateDiscoveredResourcesPaginator(_ListAggregateDiscoveredResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/ListAggregateDiscoveredResources.html#ConfigService.Paginator.ListAggregateDiscoveredResources)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#listaggregatediscoveredresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAggregateDiscoveredResourcesRequestPaginateTypeDef]
    ) -> AioPageIterator[ListAggregateDiscoveredResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/ListAggregateDiscoveredResources.html#ConfigService.Paginator.ListAggregateDiscoveredResources.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#listaggregatediscoveredresourcespaginator)
        """

if TYPE_CHECKING:
    _ListConfigurationRecordersPaginatorBase = AioPaginator[
        ListConfigurationRecordersResponseTypeDef
    ]
else:
    _ListConfigurationRecordersPaginatorBase = AioPaginator  # type: ignore[assignment]

class ListConfigurationRecordersPaginator(_ListConfigurationRecordersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/ListConfigurationRecorders.html#ConfigService.Paginator.ListConfigurationRecorders)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#listconfigurationrecorderspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConfigurationRecordersRequestPaginateTypeDef]
    ) -> AioPageIterator[ListConfigurationRecordersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/ListConfigurationRecorders.html#ConfigService.Paginator.ListConfigurationRecorders.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#listconfigurationrecorderspaginator)
        """

if TYPE_CHECKING:
    _ListDiscoveredResourcesPaginatorBase = AioPaginator[ListDiscoveredResourcesResponseTypeDef]
else:
    _ListDiscoveredResourcesPaginatorBase = AioPaginator  # type: ignore[assignment]

class ListDiscoveredResourcesPaginator(_ListDiscoveredResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/ListDiscoveredResources.html#ConfigService.Paginator.ListDiscoveredResources)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#listdiscoveredresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDiscoveredResourcesRequestPaginateTypeDef]
    ) -> AioPageIterator[ListDiscoveredResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/ListDiscoveredResources.html#ConfigService.Paginator.ListDiscoveredResources.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#listdiscoveredresourcespaginator)
        """

if TYPE_CHECKING:
    _ListResourceEvaluationsPaginatorBase = AioPaginator[ListResourceEvaluationsResponseTypeDef]
else:
    _ListResourceEvaluationsPaginatorBase = AioPaginator  # type: ignore[assignment]

class ListResourceEvaluationsPaginator(_ListResourceEvaluationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/ListResourceEvaluations.html#ConfigService.Paginator.ListResourceEvaluations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#listresourceevaluationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourceEvaluationsRequestPaginateTypeDef]
    ) -> AioPageIterator[ListResourceEvaluationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/ListResourceEvaluations.html#ConfigService.Paginator.ListResourceEvaluations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#listresourceevaluationspaginator)
        """

if TYPE_CHECKING:
    _ListTagsForResourcePaginatorBase = AioPaginator[ListTagsForResourceResponseTypeDef]
else:
    _ListTagsForResourcePaginatorBase = AioPaginator  # type: ignore[assignment]

class ListTagsForResourcePaginator(_ListTagsForResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/ListTagsForResource.html#ConfigService.Paginator.ListTagsForResource)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#listtagsforresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsForResourceRequestPaginateTypeDef]
    ) -> AioPageIterator[ListTagsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/ListTagsForResource.html#ConfigService.Paginator.ListTagsForResource.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#listtagsforresourcepaginator)
        """

if TYPE_CHECKING:
    _SelectAggregateResourceConfigPaginatorBase = AioPaginator[
        SelectAggregateResourceConfigResponseTypeDef
    ]
else:
    _SelectAggregateResourceConfigPaginatorBase = AioPaginator  # type: ignore[assignment]

class SelectAggregateResourceConfigPaginator(_SelectAggregateResourceConfigPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/SelectAggregateResourceConfig.html#ConfigService.Paginator.SelectAggregateResourceConfig)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#selectaggregateresourceconfigpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SelectAggregateResourceConfigRequestPaginateTypeDef]
    ) -> AioPageIterator[SelectAggregateResourceConfigResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/SelectAggregateResourceConfig.html#ConfigService.Paginator.SelectAggregateResourceConfig.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#selectaggregateresourceconfigpaginator)
        """

if TYPE_CHECKING:
    _SelectResourceConfigPaginatorBase = AioPaginator[SelectResourceConfigResponseTypeDef]
else:
    _SelectResourceConfigPaginatorBase = AioPaginator  # type: ignore[assignment]

class SelectResourceConfigPaginator(_SelectResourceConfigPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/SelectResourceConfig.html#ConfigService.Paginator.SelectResourceConfig)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#selectresourceconfigpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SelectResourceConfigRequestPaginateTypeDef]
    ) -> AioPageIterator[SelectResourceConfigResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config/paginator/SelectResourceConfig.html#ConfigService.Paginator.SelectResourceConfig.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/paginators/#selectresourceconfigpaginator)
        """
