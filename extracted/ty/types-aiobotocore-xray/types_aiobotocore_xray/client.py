"""
Type annotations for xray service Client.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_xray.client import XRayClient

    session = get_session()
    async with session.create_client("xray") as client:
        client: XRayClient
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
    BatchGetTracesPaginator,
    GetGroupsPaginator,
    GetSamplingRulesPaginator,
    GetSamplingStatisticSummariesPaginator,
    GetServiceGraphPaginator,
    GetTimeSeriesServiceStatisticsPaginator,
    GetTraceGraphPaginator,
    GetTraceSummariesPaginator,
    ListResourcePoliciesPaginator,
    ListTagsForResourcePaginator,
)
from .type_defs import (
    BatchGetTracesRequestTypeDef,
    BatchGetTracesResultTypeDef,
    CancelTraceRetrievalRequestTypeDef,
    CreateGroupRequestTypeDef,
    CreateGroupResultTypeDef,
    CreateSamplingRuleRequestTypeDef,
    CreateSamplingRuleResultTypeDef,
    DeleteGroupRequestTypeDef,
    DeleteResourcePolicyRequestTypeDef,
    DeleteSamplingRuleRequestTypeDef,
    DeleteSamplingRuleResultTypeDef,
    GetEncryptionConfigResultTypeDef,
    GetGroupRequestTypeDef,
    GetGroupResultTypeDef,
    GetGroupsRequestTypeDef,
    GetGroupsResultTypeDef,
    GetIndexingRulesRequestTypeDef,
    GetIndexingRulesResultTypeDef,
    GetInsightEventsRequestTypeDef,
    GetInsightEventsResultTypeDef,
    GetInsightImpactGraphRequestTypeDef,
    GetInsightImpactGraphResultTypeDef,
    GetInsightRequestTypeDef,
    GetInsightResultTypeDef,
    GetInsightSummariesRequestTypeDef,
    GetInsightSummariesResultTypeDef,
    GetRetrievedTracesGraphRequestTypeDef,
    GetRetrievedTracesGraphResultTypeDef,
    GetSamplingRulesRequestTypeDef,
    GetSamplingRulesResultTypeDef,
    GetSamplingStatisticSummariesRequestTypeDef,
    GetSamplingStatisticSummariesResultTypeDef,
    GetSamplingTargetsRequestTypeDef,
    GetSamplingTargetsResultTypeDef,
    GetServiceGraphRequestTypeDef,
    GetServiceGraphResultTypeDef,
    GetTimeSeriesServiceStatisticsRequestTypeDef,
    GetTimeSeriesServiceStatisticsResultTypeDef,
    GetTraceGraphRequestTypeDef,
    GetTraceGraphResultTypeDef,
    GetTraceSegmentDestinationResultTypeDef,
    GetTraceSummariesRequestTypeDef,
    GetTraceSummariesResultTypeDef,
    ListResourcePoliciesRequestTypeDef,
    ListResourcePoliciesResultTypeDef,
    ListRetrievedTracesRequestTypeDef,
    ListRetrievedTracesResultTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutEncryptionConfigRequestTypeDef,
    PutEncryptionConfigResultTypeDef,
    PutResourcePolicyRequestTypeDef,
    PutResourcePolicyResultTypeDef,
    PutTelemetryRecordsRequestTypeDef,
    PutTraceSegmentsRequestTypeDef,
    PutTraceSegmentsResultTypeDef,
    StartTraceRetrievalRequestTypeDef,
    StartTraceRetrievalResultTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateGroupRequestTypeDef,
    UpdateGroupResultTypeDef,
    UpdateIndexingRuleRequestTypeDef,
    UpdateIndexingRuleResultTypeDef,
    UpdateSamplingRuleRequestTypeDef,
    UpdateSamplingRuleResultTypeDef,
    UpdateTraceSegmentDestinationRequestTypeDef,
    UpdateTraceSegmentDestinationResultTypeDef,
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


__all__ = ("XRayClient",)


class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InvalidPolicyRevisionIdException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LockoutPreventionException: Type[BotocoreClientError]
    MalformedPolicyDocumentException: Type[BotocoreClientError]
    PolicyCountLimitExceededException: Type[BotocoreClientError]
    PolicySizeLimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    RuleLimitExceededException: Type[BotocoreClientError]
    ThrottledException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]


class XRayClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        XRayClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/can_paginate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#can_paginate)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/generate_presigned_url.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#generate_presigned_url)
        """

    async def batch_get_traces(
        self, **kwargs: Unpack[BatchGetTracesRequestTypeDef]
    ) -> BatchGetTracesResultTypeDef:
        """
        You cannot find traces through this API if Transaction Search is enabled since
        trace is not indexed in X-Ray.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/batch_get_traces.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#batch_get_traces)
        """

    async def cancel_trace_retrieval(
        self, **kwargs: Unpack[CancelTraceRetrievalRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Cancels an ongoing trace retrieval job initiated by
        <code>StartTraceRetrieval</code> using the provided
        <code>RetrievalToken</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/cancel_trace_retrieval.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#cancel_trace_retrieval)
        """

    async def create_group(
        self, **kwargs: Unpack[CreateGroupRequestTypeDef]
    ) -> CreateGroupResultTypeDef:
        """
        Creates a group resource with a name and a filter expression.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/create_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#create_group)
        """

    async def create_sampling_rule(
        self, **kwargs: Unpack[CreateSamplingRuleRequestTypeDef]
    ) -> CreateSamplingRuleResultTypeDef:
        """
        Creates a rule to control sampling behavior for instrumented applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/create_sampling_rule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#create_sampling_rule)
        """

    async def delete_group(self, **kwargs: Unpack[DeleteGroupRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a group resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/delete_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#delete_group)
        """

    async def delete_resource_policy(
        self, **kwargs: Unpack[DeleteResourcePolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a resource policy from the target Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/delete_resource_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#delete_resource_policy)
        """

    async def delete_sampling_rule(
        self, **kwargs: Unpack[DeleteSamplingRuleRequestTypeDef]
    ) -> DeleteSamplingRuleResultTypeDef:
        """
        Deletes a sampling rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/delete_sampling_rule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#delete_sampling_rule)
        """

    async def get_encryption_config(self) -> GetEncryptionConfigResultTypeDef:
        """
        Retrieves the current encryption configuration for X-Ray data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_encryption_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_encryption_config)
        """

    async def get_group(self, **kwargs: Unpack[GetGroupRequestTypeDef]) -> GetGroupResultTypeDef:
        """
        Retrieves group resource details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_group)
        """

    async def get_groups(self, **kwargs: Unpack[GetGroupsRequestTypeDef]) -> GetGroupsResultTypeDef:
        """
        Retrieves all active group details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_groups.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_groups)
        """

    async def get_indexing_rules(
        self, **kwargs: Unpack[GetIndexingRulesRequestTypeDef]
    ) -> GetIndexingRulesResultTypeDef:
        """
        Retrieves all indexing rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_indexing_rules.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_indexing_rules)
        """

    async def get_insight(
        self, **kwargs: Unpack[GetInsightRequestTypeDef]
    ) -> GetInsightResultTypeDef:
        """
        Retrieves the summary information of an insight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_insight.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_insight)
        """

    async def get_insight_events(
        self, **kwargs: Unpack[GetInsightEventsRequestTypeDef]
    ) -> GetInsightEventsResultTypeDef:
        """
        X-Ray reevaluates insights periodically until they're resolved, and records
        each intermediate state as an event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_insight_events.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_insight_events)
        """

    async def get_insight_impact_graph(
        self, **kwargs: Unpack[GetInsightImpactGraphRequestTypeDef]
    ) -> GetInsightImpactGraphResultTypeDef:
        """
        Retrieves a service graph structure filtered by the specified insight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_insight_impact_graph.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_insight_impact_graph)
        """

    async def get_insight_summaries(
        self, **kwargs: Unpack[GetInsightSummariesRequestTypeDef]
    ) -> GetInsightSummariesResultTypeDef:
        """
        Retrieves the summaries of all insights in the specified group matching the
        provided filter values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_insight_summaries.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_insight_summaries)
        """

    async def get_retrieved_traces_graph(
        self, **kwargs: Unpack[GetRetrievedTracesGraphRequestTypeDef]
    ) -> GetRetrievedTracesGraphResultTypeDef:
        """
        Retrieves a service graph for traces based on the specified
        <code>RetrievalToken</code> from the CloudWatch log group generated by
        Transaction Search.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_retrieved_traces_graph.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_retrieved_traces_graph)
        """

    async def get_sampling_rules(
        self, **kwargs: Unpack[GetSamplingRulesRequestTypeDef]
    ) -> GetSamplingRulesResultTypeDef:
        """
        Retrieves all sampling rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_sampling_rules.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_sampling_rules)
        """

    async def get_sampling_statistic_summaries(
        self, **kwargs: Unpack[GetSamplingStatisticSummariesRequestTypeDef]
    ) -> GetSamplingStatisticSummariesResultTypeDef:
        """
        Retrieves information about recent sampling results for all sampling rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_sampling_statistic_summaries.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_sampling_statistic_summaries)
        """

    async def get_sampling_targets(
        self, **kwargs: Unpack[GetSamplingTargetsRequestTypeDef]
    ) -> GetSamplingTargetsResultTypeDef:
        """
        Requests a sampling quota for rules that the service is using to sample
        requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_sampling_targets.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_sampling_targets)
        """

    async def get_service_graph(
        self, **kwargs: Unpack[GetServiceGraphRequestTypeDef]
    ) -> GetServiceGraphResultTypeDef:
        """
        Retrieves a document that describes services that process incoming requests,
        and downstream services that they call as a result.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_service_graph.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_service_graph)
        """

    async def get_time_series_service_statistics(
        self, **kwargs: Unpack[GetTimeSeriesServiceStatisticsRequestTypeDef]
    ) -> GetTimeSeriesServiceStatisticsResultTypeDef:
        """
        Get an aggregation of service statistics defined by a specific time range.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_time_series_service_statistics.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_time_series_service_statistics)
        """

    async def get_trace_graph(
        self, **kwargs: Unpack[GetTraceGraphRequestTypeDef]
    ) -> GetTraceGraphResultTypeDef:
        """
        Retrieves a service graph for one or more specific trace IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_trace_graph.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_trace_graph)
        """

    async def get_trace_segment_destination(self) -> GetTraceSegmentDestinationResultTypeDef:
        """
        Retrieves the current destination of data sent to <code>PutTraceSegments</code>
        and <i>OpenTelemetry</i> API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_trace_segment_destination.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_trace_segment_destination)
        """

    async def get_trace_summaries(
        self, **kwargs: Unpack[GetTraceSummariesRequestTypeDef]
    ) -> GetTraceSummariesResultTypeDef:
        """
        Retrieves IDs and annotations for traces available for a specified time frame
        using an optional filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_trace_summaries.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_trace_summaries)
        """

    async def list_resource_policies(
        self, **kwargs: Unpack[ListResourcePoliciesRequestTypeDef]
    ) -> ListResourcePoliciesResultTypeDef:
        """
        Returns the list of resource policies in the target Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/list_resource_policies.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#list_resource_policies)
        """

    async def list_retrieved_traces(
        self, **kwargs: Unpack[ListRetrievedTracesRequestTypeDef]
    ) -> ListRetrievedTracesResultTypeDef:
        """
        Retrieves a list of traces for a given <code>RetrievalToken</code> from the
        CloudWatch log group generated by Transaction Search.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/list_retrieved_traces.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#list_retrieved_traces)
        """

    async def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags that are applied to the specified Amazon Web Services
        X-Ray group or sampling rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/list_tags_for_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#list_tags_for_resource)
        """

    async def put_encryption_config(
        self, **kwargs: Unpack[PutEncryptionConfigRequestTypeDef]
    ) -> PutEncryptionConfigResultTypeDef:
        """
        Updates the encryption configuration for X-Ray data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/put_encryption_config.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#put_encryption_config)
        """

    async def put_resource_policy(
        self, **kwargs: Unpack[PutResourcePolicyRequestTypeDef]
    ) -> PutResourcePolicyResultTypeDef:
        """
        Sets the resource policy to grant one or more Amazon Web Services services and
        accounts permissions to access X-Ray.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/put_resource_policy.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#put_resource_policy)
        """

    async def put_telemetry_records(
        self, **kwargs: Unpack[PutTelemetryRecordsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Used by the Amazon Web Services X-Ray daemon to upload telemetry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/put_telemetry_records.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#put_telemetry_records)
        """

    async def put_trace_segments(
        self, **kwargs: Unpack[PutTraceSegmentsRequestTypeDef]
    ) -> PutTraceSegmentsResultTypeDef:
        """
        Uploads segment documents to Amazon Web Services X-Ray.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/put_trace_segments.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#put_trace_segments)
        """

    async def start_trace_retrieval(
        self, **kwargs: Unpack[StartTraceRetrievalRequestTypeDef]
    ) -> StartTraceRetrievalResultTypeDef:
        """
        Initiates a trace retrieval process using the specified time range and for the
        give trace IDs on Transaction Search generated by the CloudWatch log group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/start_trace_retrieval.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#start_trace_retrieval)
        """

    async def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Applies tags to an existing Amazon Web Services X-Ray group or sampling rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/tag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#tag_resource)
        """

    async def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from an Amazon Web Services X-Ray group or sampling rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/untag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#untag_resource)
        """

    async def update_group(
        self, **kwargs: Unpack[UpdateGroupRequestTypeDef]
    ) -> UpdateGroupResultTypeDef:
        """
        Updates a group resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/update_group.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#update_group)
        """

    async def update_indexing_rule(
        self, **kwargs: Unpack[UpdateIndexingRuleRequestTypeDef]
    ) -> UpdateIndexingRuleResultTypeDef:
        """
        Modifies an indexing rule's configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/update_indexing_rule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#update_indexing_rule)
        """

    async def update_sampling_rule(
        self, **kwargs: Unpack[UpdateSamplingRuleRequestTypeDef]
    ) -> UpdateSamplingRuleResultTypeDef:
        """
        Modifies a sampling rule's configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/update_sampling_rule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#update_sampling_rule)
        """

    async def update_trace_segment_destination(
        self, **kwargs: Unpack[UpdateTraceSegmentDestinationRequestTypeDef]
    ) -> UpdateTraceSegmentDestinationResultTypeDef:
        """
        Modifies the destination of data sent to <code>PutTraceSegments</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/update_trace_segment_destination.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#update_trace_segment_destination)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["batch_get_traces"]
    ) -> BatchGetTracesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_groups"]
    ) -> GetGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_sampling_rules"]
    ) -> GetSamplingRulesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_sampling_statistic_summaries"]
    ) -> GetSamplingStatisticSummariesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_service_graph"]
    ) -> GetServiceGraphPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_time_series_service_statistics"]
    ) -> GetTimeSeriesServiceStatisticsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_trace_graph"]
    ) -> GetTraceGraphPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_trace_summaries"]
    ) -> GetTraceSummariesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resource_policies"]
    ) -> ListResourcePoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/#get_paginator)
        """

    async def __aenter__(self) -> Self:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/)
        """

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_xray/client/)
        """
