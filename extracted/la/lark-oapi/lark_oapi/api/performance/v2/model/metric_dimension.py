# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n
from .i18n import I18n
from .custom_metric_config import CustomMetricConfig


class MetricDimension(object):
    _types = {
        "group_id": int,
        "metric_dimension_id": int,
        "name": I18n,
        "evaluation_rule_id_for_each_metric": int,
        "dimension_weight": str,
        "description": I18n,
        "review_rule_option": int,
        "custom_metric_config": CustomMetricConfig,
    }

    def __init__(self, d=None):
        self.group_id: Optional[int] = None
        self.metric_dimension_id: Optional[int] = None
        self.name: Optional[I18n] = None
        self.evaluation_rule_id_for_each_metric: Optional[int] = None
        self.dimension_weight: Optional[str] = None
        self.description: Optional[I18n] = None
        self.review_rule_option: Optional[int] = None
        self.custom_metric_config: Optional[CustomMetricConfig] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MetricDimensionBuilder":
        return MetricDimensionBuilder()


class MetricDimensionBuilder(object):
    def __init__(self) -> None:
        self._metric_dimension = MetricDimension()

    def group_id(self, group_id: int) -> "MetricDimensionBuilder":
        self._metric_dimension.group_id = group_id
        return self

    def metric_dimension_id(self, metric_dimension_id: int) -> "MetricDimensionBuilder":
        self._metric_dimension.metric_dimension_id = metric_dimension_id
        return self

    def name(self, name: I18n) -> "MetricDimensionBuilder":
        self._metric_dimension.name = name
        return self

    def evaluation_rule_id_for_each_metric(self, evaluation_rule_id_for_each_metric: int) -> "MetricDimensionBuilder":
        self._metric_dimension.evaluation_rule_id_for_each_metric = evaluation_rule_id_for_each_metric
        return self

    def dimension_weight(self, dimension_weight: str) -> "MetricDimensionBuilder":
        self._metric_dimension.dimension_weight = dimension_weight
        return self

    def description(self, description: I18n) -> "MetricDimensionBuilder":
        self._metric_dimension.description = description
        return self

    def review_rule_option(self, review_rule_option: int) -> "MetricDimensionBuilder":
        self._metric_dimension.review_rule_option = review_rule_option
        return self

    def custom_metric_config(self, custom_metric_config: CustomMetricConfig) -> "MetricDimensionBuilder":
        self._metric_dimension.custom_metric_config = custom_metric_config
        return self

    def build(self) -> "MetricDimension":
        return self._metric_dimension
