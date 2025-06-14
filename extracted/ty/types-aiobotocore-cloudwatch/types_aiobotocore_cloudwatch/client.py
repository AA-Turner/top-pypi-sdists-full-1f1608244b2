"""
Type annotations for cloudwatch service Client.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_cloudwatch.client import CloudWatchClient

    session = get_session()
    async with session.create_client("cloudwatch") as client:
        client: CloudWatchClient
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
    DescribeAlarmHistoryPaginator,
    DescribeAlarmsPaginator,
    DescribeAnomalyDetectorsPaginator,
    GetMetricDataPaginator,
    ListDashboardsPaginator,
    ListMetricsPaginator,
)
from .type_defs import (
    DeleteAlarmsInputTypeDef,
    DeleteAnomalyDetectorInputTypeDef,
    DeleteDashboardsInputTypeDef,
    DeleteInsightRulesInputTypeDef,
    DeleteInsightRulesOutputTypeDef,
    DeleteMetricStreamInputTypeDef,
    DescribeAlarmHistoryInputTypeDef,
    DescribeAlarmHistoryOutputTypeDef,
    DescribeAlarmsForMetricInputTypeDef,
    DescribeAlarmsForMetricOutputTypeDef,
    DescribeAlarmsInputTypeDef,
    DescribeAlarmsOutputTypeDef,
    DescribeAnomalyDetectorsInputTypeDef,
    DescribeAnomalyDetectorsOutputTypeDef,
    DescribeInsightRulesInputTypeDef,
    DescribeInsightRulesOutputTypeDef,
    DisableAlarmActionsInputTypeDef,
    DisableInsightRulesInputTypeDef,
    DisableInsightRulesOutputTypeDef,
    EmptyResponseMetadataTypeDef,
    EnableAlarmActionsInputTypeDef,
    EnableInsightRulesInputTypeDef,
    EnableInsightRulesOutputTypeDef,
    GetDashboardInputTypeDef,
    GetDashboardOutputTypeDef,
    GetInsightRuleReportInputTypeDef,
    GetInsightRuleReportOutputTypeDef,
    GetMetricDataInputTypeDef,
    GetMetricDataOutputTypeDef,
    GetMetricStatisticsInputTypeDef,
    GetMetricStatisticsOutputTypeDef,
    GetMetricStreamInputTypeDef,
    GetMetricStreamOutputTypeDef,
    GetMetricWidgetImageInputTypeDef,
    GetMetricWidgetImageOutputTypeDef,
    ListDashboardsInputTypeDef,
    ListDashboardsOutputTypeDef,
    ListManagedInsightRulesInputTypeDef,
    ListManagedInsightRulesOutputTypeDef,
    ListMetricsInputTypeDef,
    ListMetricsOutputTypeDef,
    ListMetricStreamsInputTypeDef,
    ListMetricStreamsOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    PutAnomalyDetectorInputTypeDef,
    PutCompositeAlarmInputTypeDef,
    PutDashboardInputTypeDef,
    PutDashboardOutputTypeDef,
    PutInsightRuleInputTypeDef,
    PutManagedInsightRulesInputTypeDef,
    PutManagedInsightRulesOutputTypeDef,
    PutMetricAlarmInputTypeDef,
    PutMetricDataInputTypeDef,
    PutMetricStreamInputTypeDef,
    PutMetricStreamOutputTypeDef,
    SetAlarmStateInputTypeDef,
    StartMetricStreamsInputTypeDef,
    StopMetricStreamsInputTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
)
from .waiter import AlarmExistsWaiter, CompositeAlarmExistsWaiter

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


__all__ = ("CloudWatchClient",)


class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DashboardInvalidInputError: Type[BotocoreClientError]
    DashboardNotFoundError: Type[BotocoreClientError]
    InternalServiceFault: Type[BotocoreClientError]
    InvalidFormatFault: Type[BotocoreClientError]
    InvalidNextToken: Type[BotocoreClientError]
    InvalidParameterCombinationException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    LimitExceededFault: Type[BotocoreClientError]
    MissingRequiredParameterException: Type[BotocoreClientError]
    ResourceNotFound: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]


class CloudWatchClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudWatchClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/can_paginate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#can_paginate)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/generate_presigned_url.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#generate_presigned_url)
        """

    async def delete_alarms(
        self, **kwargs: Unpack[DeleteAlarmsInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/delete_alarms.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#delete_alarms)
        """

    async def delete_anomaly_detector(
        self, **kwargs: Unpack[DeleteAnomalyDetectorInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified anomaly detection model from your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/delete_anomaly_detector.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#delete_anomaly_detector)
        """

    async def delete_dashboards(
        self, **kwargs: Unpack[DeleteDashboardsInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes all dashboards that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/delete_dashboards.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#delete_dashboards)
        """

    async def delete_insight_rules(
        self, **kwargs: Unpack[DeleteInsightRulesInputTypeDef]
    ) -> DeleteInsightRulesOutputTypeDef:
        """
        Permanently deletes the specified Contributor Insights rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/delete_insight_rules.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#delete_insight_rules)
        """

    async def delete_metric_stream(
        self, **kwargs: Unpack[DeleteMetricStreamInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Permanently deletes the metric stream that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/delete_metric_stream.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#delete_metric_stream)
        """

    async def describe_alarm_history(
        self, **kwargs: Unpack[DescribeAlarmHistoryInputTypeDef]
    ) -> DescribeAlarmHistoryOutputTypeDef:
        """
        Retrieves the history for the specified alarm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/describe_alarm_history.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#describe_alarm_history)
        """

    async def describe_alarms(
        self, **kwargs: Unpack[DescribeAlarmsInputTypeDef]
    ) -> DescribeAlarmsOutputTypeDef:
        """
        Retrieves the specified alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/describe_alarms.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#describe_alarms)
        """

    async def describe_alarms_for_metric(
        self, **kwargs: Unpack[DescribeAlarmsForMetricInputTypeDef]
    ) -> DescribeAlarmsForMetricOutputTypeDef:
        """
        Retrieves the alarms for the specified metric.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/describe_alarms_for_metric.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#describe_alarms_for_metric)
        """

    async def describe_anomaly_detectors(
        self, **kwargs: Unpack[DescribeAnomalyDetectorsInputTypeDef]
    ) -> DescribeAnomalyDetectorsOutputTypeDef:
        """
        Lists the anomaly detection models that you have created in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/describe_anomaly_detectors.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#describe_anomaly_detectors)
        """

    async def describe_insight_rules(
        self, **kwargs: Unpack[DescribeInsightRulesInputTypeDef]
    ) -> DescribeInsightRulesOutputTypeDef:
        """
        Returns a list of all the Contributor Insights rules in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/describe_insight_rules.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#describe_insight_rules)
        """

    async def disable_alarm_actions(
        self, **kwargs: Unpack[DisableAlarmActionsInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disables the actions for the specified alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/disable_alarm_actions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#disable_alarm_actions)
        """

    async def disable_insight_rules(
        self, **kwargs: Unpack[DisableInsightRulesInputTypeDef]
    ) -> DisableInsightRulesOutputTypeDef:
        """
        Disables the specified Contributor Insights rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/disable_insight_rules.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#disable_insight_rules)
        """

    async def enable_alarm_actions(
        self, **kwargs: Unpack[EnableAlarmActionsInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Enables the actions for the specified alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/enable_alarm_actions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#enable_alarm_actions)
        """

    async def enable_insight_rules(
        self, **kwargs: Unpack[EnableInsightRulesInputTypeDef]
    ) -> EnableInsightRulesOutputTypeDef:
        """
        Enables the specified Contributor Insights rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/enable_insight_rules.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#enable_insight_rules)
        """

    async def get_dashboard(
        self, **kwargs: Unpack[GetDashboardInputTypeDef]
    ) -> GetDashboardOutputTypeDef:
        """
        Displays the details of the dashboard that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/get_dashboard.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#get_dashboard)
        """

    async def get_insight_rule_report(
        self, **kwargs: Unpack[GetInsightRuleReportInputTypeDef]
    ) -> GetInsightRuleReportOutputTypeDef:
        """
        This operation returns the time series data collected by a Contributor Insights
        rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/get_insight_rule_report.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#get_insight_rule_report)
        """

    async def get_metric_data(
        self, **kwargs: Unpack[GetMetricDataInputTypeDef]
    ) -> GetMetricDataOutputTypeDef:
        """
        You can use the <code>GetMetricData</code> API to retrieve CloudWatch metric
        values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/get_metric_data.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#get_metric_data)
        """

    async def get_metric_statistics(
        self, **kwargs: Unpack[GetMetricStatisticsInputTypeDef]
    ) -> GetMetricStatisticsOutputTypeDef:
        """
        Gets statistics for the specified metric.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/get_metric_statistics.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#get_metric_statistics)
        """

    async def get_metric_stream(
        self, **kwargs: Unpack[GetMetricStreamInputTypeDef]
    ) -> GetMetricStreamOutputTypeDef:
        """
        Returns information about the metric stream that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/get_metric_stream.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#get_metric_stream)
        """

    async def get_metric_widget_image(
        self, **kwargs: Unpack[GetMetricWidgetImageInputTypeDef]
    ) -> GetMetricWidgetImageOutputTypeDef:
        """
        You can use the <code>GetMetricWidgetImage</code> API to retrieve a snapshot
        graph of one or more Amazon CloudWatch metrics as a bitmap image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/get_metric_widget_image.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#get_metric_widget_image)
        """

    async def list_dashboards(
        self, **kwargs: Unpack[ListDashboardsInputTypeDef]
    ) -> ListDashboardsOutputTypeDef:
        """
        Returns a list of the dashboards for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/list_dashboards.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#list_dashboards)
        """

    async def list_managed_insight_rules(
        self, **kwargs: Unpack[ListManagedInsightRulesInputTypeDef]
    ) -> ListManagedInsightRulesOutputTypeDef:
        """
        Returns a list that contains the number of managed Contributor Insights rules
        in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/list_managed_insight_rules.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#list_managed_insight_rules)
        """

    async def list_metric_streams(
        self, **kwargs: Unpack[ListMetricStreamsInputTypeDef]
    ) -> ListMetricStreamsOutputTypeDef:
        """
        Returns a list of metric streams in this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/list_metric_streams.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#list_metric_streams)
        """

    async def list_metrics(
        self, **kwargs: Unpack[ListMetricsInputTypeDef]
    ) -> ListMetricsOutputTypeDef:
        """
        List the specified metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/list_metrics.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#list_metrics)
        """

    async def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Displays the tags associated with a CloudWatch resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/list_tags_for_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#list_tags_for_resource)
        """

    async def put_anomaly_detector(
        self, **kwargs: Unpack[PutAnomalyDetectorInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates an anomaly detection model for a CloudWatch metric.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/put_anomaly_detector.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#put_anomaly_detector)
        """

    async def put_composite_alarm(
        self, **kwargs: Unpack[PutCompositeAlarmInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates or updates a <i>composite alarm</i>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/put_composite_alarm.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#put_composite_alarm)
        """

    async def put_dashboard(
        self, **kwargs: Unpack[PutDashboardInputTypeDef]
    ) -> PutDashboardOutputTypeDef:
        """
        Creates a dashboard if it does not already exist, or updates an existing
        dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/put_dashboard.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#put_dashboard)
        """

    async def put_insight_rule(
        self, **kwargs: Unpack[PutInsightRuleInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates a Contributor Insights rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/put_insight_rule.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#put_insight_rule)
        """

    async def put_managed_insight_rules(
        self, **kwargs: Unpack[PutManagedInsightRulesInputTypeDef]
    ) -> PutManagedInsightRulesOutputTypeDef:
        """
        Creates a managed Contributor Insights rule for a specified Amazon Web Services
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/put_managed_insight_rules.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#put_managed_insight_rules)
        """

    async def put_metric_alarm(
        self, **kwargs: Unpack[PutMetricAlarmInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates or updates an alarm and associates it with the specified metric, metric
        math expression, anomaly detection model, or Metrics Insights query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/put_metric_alarm.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#put_metric_alarm)
        """

    async def put_metric_data(
        self, **kwargs: Unpack[PutMetricDataInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Publishes metric data to Amazon CloudWatch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/put_metric_data.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#put_metric_data)
        """

    async def put_metric_stream(
        self, **kwargs: Unpack[PutMetricStreamInputTypeDef]
    ) -> PutMetricStreamOutputTypeDef:
        """
        Creates or updates a metric stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/put_metric_stream.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#put_metric_stream)
        """

    async def set_alarm_state(
        self, **kwargs: Unpack[SetAlarmStateInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Temporarily sets the state of an alarm for testing purposes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/set_alarm_state.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#set_alarm_state)
        """

    async def start_metric_streams(
        self, **kwargs: Unpack[StartMetricStreamsInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Starts the streaming of metrics for one or more of your metric streams.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/start_metric_streams.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#start_metric_streams)
        """

    async def stop_metric_streams(
        self, **kwargs: Unpack[StopMetricStreamsInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Stops the streaming of metrics for one or more of your metric streams.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/stop_metric_streams.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#stop_metric_streams)
        """

    async def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified CloudWatch resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/tag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#tag_resource)
        """

    async def untag_resource(self, **kwargs: Unpack[UntagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/untag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#untag_resource)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_alarm_history"]
    ) -> DescribeAlarmHistoryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_alarms"]
    ) -> DescribeAlarmsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_anomaly_detectors"]
    ) -> DescribeAnomalyDetectorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_metric_data"]
    ) -> GetMetricDataPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_dashboards"]
    ) -> ListDashboardsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_metrics"]
    ) -> ListMetricsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["alarm_exists"]
    ) -> AlarmExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["composite_alarm_exists"]
    ) -> CompositeAlarmExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/get_waiter.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/#get_waiter)
        """

    async def __aenter__(self) -> Self:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/)
        """

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/client/)
        """
