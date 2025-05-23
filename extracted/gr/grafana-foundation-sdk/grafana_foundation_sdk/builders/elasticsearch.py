# Code generated - EDITING IS FUTILE. DO NOT EDIT.

import typing
from ..cog import builder as cogbuilder
from ..models import elasticsearch
from ..models import dashboard


class DateHistogram(cogbuilder.Builder[elasticsearch.DateHistogram]):
    _internal: elasticsearch.DateHistogram

    def __init__(self):
        self._internal = elasticsearch.DateHistogram()

    def build(self) -> elasticsearch.DateHistogram:
        """
        Builds the object.
        """
        return self._internal    
    
    def field(self, field: str) -> typing.Self:    
        self._internal.field = field
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchDateHistogramSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    


class Histogram(cogbuilder.Builder[elasticsearch.Histogram]):
    _internal: elasticsearch.Histogram

    def __init__(self):
        self._internal = elasticsearch.Histogram()

    def build(self) -> elasticsearch.Histogram:
        """
        Builds the object.
        """
        return self._internal    
    
    def field(self, field: str) -> typing.Self:    
        self._internal.field = field
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchHistogramSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    


class Terms(cogbuilder.Builder[elasticsearch.Terms]):
    _internal: elasticsearch.Terms

    def __init__(self):
        self._internal = elasticsearch.Terms()

    def build(self) -> elasticsearch.Terms:
        """
        Builds the object.
        """
        return self._internal    
    
    def field(self, field: str) -> typing.Self:    
        self._internal.field = field
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchTermsSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    


class Filters(cogbuilder.Builder[elasticsearch.Filters]):
    _internal: elasticsearch.Filters

    def __init__(self):
        self._internal = elasticsearch.Filters()

    def build(self) -> elasticsearch.Filters:
        """
        Builds the object.
        """
        return self._internal    
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchFiltersSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    


class Filter(cogbuilder.Builder[elasticsearch.Filter]):
    _internal: elasticsearch.Filter

    def __init__(self):
        self._internal = elasticsearch.Filter()

    def build(self) -> elasticsearch.Filter:
        """
        Builds the object.
        """
        return self._internal    
    
    def query(self, query: str) -> typing.Self:    
        self._internal.query = query
    
        return self
    
    def label(self, label: str) -> typing.Self:    
        self._internal.label = label
    
        return self
    


class GeoHashGrid(cogbuilder.Builder[elasticsearch.GeoHashGrid]):
    _internal: elasticsearch.GeoHashGrid

    def __init__(self):
        self._internal = elasticsearch.GeoHashGrid()

    def build(self) -> elasticsearch.GeoHashGrid:
        """
        Builds the object.
        """
        return self._internal    
    
    def field(self, field: str) -> typing.Self:    
        self._internal.field = field
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchGeoHashGridSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    


class Nested(cogbuilder.Builder[elasticsearch.Nested]):
    _internal: elasticsearch.Nested

    def __init__(self):
        self._internal = elasticsearch.Nested()

    def build(self) -> elasticsearch.Nested:
        """
        Builds the object.
        """
        return self._internal    
    
    def field(self, field: str) -> typing.Self:    
        self._internal.field = field
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def settings(self, settings: object) -> typing.Self:    
        self._internal.settings = settings
    
        return self
    


class Count(cogbuilder.Builder[elasticsearch.Count]):
    _internal: elasticsearch.Count

    def __init__(self):
        self._internal = elasticsearch.Count()

    def build(self) -> elasticsearch.Count:
        """
        Builds the object.
        """
        return self._internal    
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class MovingAverage(cogbuilder.Builder[elasticsearch.MovingAverage]):    
    """
    #MovingAverage's settings are overridden in types.ts
    """
    
    _internal: elasticsearch.MovingAverage

    def __init__(self):
        self._internal = elasticsearch.MovingAverage()

    def build(self) -> elasticsearch.MovingAverage:
        """
        Builds the object.
        """
        return self._internal    
    
    def pipeline_agg(self, pipeline_agg: str) -> typing.Self:    
        self._internal.pipeline_agg = pipeline_agg
    
        return self
    
    def field(self, field: str) -> typing.Self:    
        self._internal.field = field
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def settings(self, settings: dict[str, object]) -> typing.Self:    
        self._internal.settings = settings
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class Derivative(cogbuilder.Builder[elasticsearch.Derivative]):
    _internal: elasticsearch.Derivative

    def __init__(self):
        self._internal = elasticsearch.Derivative()

    def build(self) -> elasticsearch.Derivative:
        """
        Builds the object.
        """
        return self._internal    
    
    def pipeline_agg(self, pipeline_agg: str) -> typing.Self:    
        self._internal.pipeline_agg = pipeline_agg
    
        return self
    
    def field(self, field: str) -> typing.Self:    
        self._internal.field = field
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchDerivativeSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class CumulativeSum(cogbuilder.Builder[elasticsearch.CumulativeSum]):
    _internal: elasticsearch.CumulativeSum

    def __init__(self):
        self._internal = elasticsearch.CumulativeSum()

    def build(self) -> elasticsearch.CumulativeSum:
        """
        Builds the object.
        """
        return self._internal    
    
    def pipeline_agg(self, pipeline_agg: str) -> typing.Self:    
        self._internal.pipeline_agg = pipeline_agg
    
        return self
    
    def field(self, field: str) -> typing.Self:    
        self._internal.field = field
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchCumulativeSumSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class BucketScript(cogbuilder.Builder[elasticsearch.BucketScript]):
    _internal: elasticsearch.BucketScript

    def __init__(self):
        self._internal = elasticsearch.BucketScript()

    def build(self) -> elasticsearch.BucketScript:
        """
        Builds the object.
        """
        return self._internal    
    
    def pipeline_variables(self, pipeline_variables: list[cogbuilder.Builder[elasticsearch.PipelineVariable]]) -> typing.Self:    
        pipeline_variables_resources = [r1.build() for r1 in pipeline_variables]
        self._internal.pipeline_variables = pipeline_variables_resources
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchBucketScriptSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class PipelineVariable(cogbuilder.Builder[elasticsearch.PipelineVariable]):
    _internal: elasticsearch.PipelineVariable

    def __init__(self):
        self._internal = elasticsearch.PipelineVariable()

    def build(self) -> elasticsearch.PipelineVariable:
        """
        Builds the object.
        """
        return self._internal    
    
    def name(self, name: str) -> typing.Self:    
        self._internal.name = name
    
        return self
    
    def pipeline_agg(self, pipeline_agg: str) -> typing.Self:    
        self._internal.pipeline_agg = pipeline_agg
    
        return self
    


class SerialDiff(cogbuilder.Builder[elasticsearch.SerialDiff]):
    _internal: elasticsearch.SerialDiff

    def __init__(self):
        self._internal = elasticsearch.SerialDiff()

    def build(self) -> elasticsearch.SerialDiff:
        """
        Builds the object.
        """
        return self._internal    
    
    def pipeline_agg(self, pipeline_agg: str) -> typing.Self:    
        self._internal.pipeline_agg = pipeline_agg
    
        return self
    
    def field(self, field: str) -> typing.Self:    
        self._internal.field = field
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchSerialDiffSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class RawData(cogbuilder.Builder[elasticsearch.RawData]):
    _internal: elasticsearch.RawData

    def __init__(self):
        self._internal = elasticsearch.RawData()

    def build(self) -> elasticsearch.RawData:
        """
        Builds the object.
        """
        return self._internal    
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchRawDataSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class RawDocument(cogbuilder.Builder[elasticsearch.RawDocument]):
    _internal: elasticsearch.RawDocument

    def __init__(self):
        self._internal = elasticsearch.RawDocument()

    def build(self) -> elasticsearch.RawDocument:
        """
        Builds the object.
        """
        return self._internal    
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchRawDocumentSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class UniqueCount(cogbuilder.Builder[elasticsearch.UniqueCount]):
    _internal: elasticsearch.UniqueCount

    def __init__(self):
        self._internal = elasticsearch.UniqueCount()

    def build(self) -> elasticsearch.UniqueCount:
        """
        Builds the object.
        """
        return self._internal    
    
    def field(self, field: str) -> typing.Self:    
        self._internal.field = field
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchUniqueCountSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class Percentiles(cogbuilder.Builder[elasticsearch.Percentiles]):
    _internal: elasticsearch.Percentiles

    def __init__(self):
        self._internal = elasticsearch.Percentiles()

    def build(self) -> elasticsearch.Percentiles:
        """
        Builds the object.
        """
        return self._internal    
    
    def field(self, field: str) -> typing.Self:    
        self._internal.field = field
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchPercentilesSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class ExtendedStats(cogbuilder.Builder[elasticsearch.ExtendedStats]):
    _internal: elasticsearch.ExtendedStats

    def __init__(self):
        self._internal = elasticsearch.ExtendedStats()

    def build(self) -> elasticsearch.ExtendedStats:
        """
        Builds the object.
        """
        return self._internal    
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchExtendedStatsSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    
    def field(self, field: str) -> typing.Self:    
        self._internal.field = field
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def meta(self, meta: object) -> typing.Self:    
        self._internal.meta = meta
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class Min(cogbuilder.Builder[elasticsearch.Min]):
    _internal: elasticsearch.Min

    def __init__(self):
        self._internal = elasticsearch.Min()

    def build(self) -> elasticsearch.Min:
        """
        Builds the object.
        """
        return self._internal    
    
    def field(self, field: str) -> typing.Self:    
        self._internal.field = field
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchMinSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class Max(cogbuilder.Builder[elasticsearch.Max]):
    _internal: elasticsearch.Max

    def __init__(self):
        self._internal = elasticsearch.Max()

    def build(self) -> elasticsearch.Max:
        """
        Builds the object.
        """
        return self._internal    
    
    def field(self, field: str) -> typing.Self:    
        self._internal.field = field
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchMaxSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class Sum(cogbuilder.Builder[elasticsearch.Sum]):
    _internal: elasticsearch.Sum

    def __init__(self):
        self._internal = elasticsearch.Sum()

    def build(self) -> elasticsearch.Sum:
        """
        Builds the object.
        """
        return self._internal    
    
    def field(self, field: str) -> typing.Self:    
        self._internal.field = field
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchSumSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class Average(cogbuilder.Builder[elasticsearch.Average]):
    _internal: elasticsearch.Average

    def __init__(self):
        self._internal = elasticsearch.Average()

    def build(self) -> elasticsearch.Average:
        """
        Builds the object.
        """
        return self._internal    
    
    def field(self, field: str) -> typing.Self:    
        self._internal.field = field
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchAverageSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class MovingFunction(cogbuilder.Builder[elasticsearch.MovingFunction]):
    _internal: elasticsearch.MovingFunction

    def __init__(self):
        self._internal = elasticsearch.MovingFunction()

    def build(self) -> elasticsearch.MovingFunction:
        """
        Builds the object.
        """
        return self._internal    
    
    def pipeline_agg(self, pipeline_agg: str) -> typing.Self:    
        self._internal.pipeline_agg = pipeline_agg
    
        return self
    
    def field(self, field: str) -> typing.Self:    
        self._internal.field = field
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchMovingFunctionSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class Logs(cogbuilder.Builder[elasticsearch.Logs]):
    _internal: elasticsearch.Logs

    def __init__(self):
        self._internal = elasticsearch.Logs()

    def build(self) -> elasticsearch.Logs:
        """
        Builds the object.
        """
        return self._internal    
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchLogsSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class Rate(cogbuilder.Builder[elasticsearch.Rate]):
    _internal: elasticsearch.Rate

    def __init__(self):
        self._internal = elasticsearch.Rate()

    def build(self) -> elasticsearch.Rate:
        """
        Builds the object.
        """
        return self._internal    
    
    def field(self, field: str) -> typing.Self:    
        self._internal.field = field
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchRateSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class TopMetrics(cogbuilder.Builder[elasticsearch.TopMetrics]):
    _internal: elasticsearch.TopMetrics

    def __init__(self):
        self._internal = elasticsearch.TopMetrics()

    def build(self) -> elasticsearch.TopMetrics:
        """
        Builds the object.
        """
        return self._internal    
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchTopMetricsSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class BaseBucketAggregation(cogbuilder.Builder[elasticsearch.BaseBucketAggregation]):
    _internal: elasticsearch.BaseBucketAggregation

    def __init__(self):
        self._internal = elasticsearch.BaseBucketAggregation()

    def build(self) -> elasticsearch.BaseBucketAggregation:
        """
        Builds the object.
        """
        return self._internal    
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def type(self, type_val: elasticsearch.BucketAggregationType) -> typing.Self:    
        self._internal.type_val = type_val
    
        return self
    
    def settings(self, settings: object) -> typing.Self:    
        self._internal.settings = settings
    
        return self
    


class BucketAggregationWithField(cogbuilder.Builder[elasticsearch.BucketAggregationWithField]):
    _internal: elasticsearch.BucketAggregationWithField

    def __init__(self):
        self._internal = elasticsearch.BucketAggregationWithField()

    def build(self) -> elasticsearch.BucketAggregationWithField:
        """
        Builds the object.
        """
        return self._internal    
    
    def field(self, field: str) -> typing.Self:    
        self._internal.field = field
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def type(self, type_val: elasticsearch.BucketAggregationType) -> typing.Self:    
        self._internal.type_val = type_val
    
        return self
    
    def settings(self, settings: object) -> typing.Self:    
        self._internal.settings = settings
    
        return self
    


class DateHistogramSettings(cogbuilder.Builder[elasticsearch.DateHistogramSettings]):
    _internal: elasticsearch.DateHistogramSettings

    def __init__(self):
        self._internal = elasticsearch.DateHistogramSettings()

    def build(self) -> elasticsearch.DateHistogramSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def interval(self, interval: str) -> typing.Self:    
        self._internal.interval = interval
    
        return self
    
    def min_doc_count(self, min_doc_count: str) -> typing.Self:    
        self._internal.min_doc_count = min_doc_count
    
        return self
    
    def trim_edges(self, trim_edges: str) -> typing.Self:    
        self._internal.trim_edges = trim_edges
    
        return self
    
    def offset(self, offset: str) -> typing.Self:    
        self._internal.offset = offset
    
        return self
    
    def time_zone(self, time_zone: str) -> typing.Self:    
        self._internal.time_zone = time_zone
    
        return self
    


class HistogramSettings(cogbuilder.Builder[elasticsearch.HistogramSettings]):
    _internal: elasticsearch.HistogramSettings

    def __init__(self):
        self._internal = elasticsearch.HistogramSettings()

    def build(self) -> elasticsearch.HistogramSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def interval(self, interval: str) -> typing.Self:    
        self._internal.interval = interval
    
        return self
    
    def min_doc_count(self, min_doc_count: str) -> typing.Self:    
        self._internal.min_doc_count = min_doc_count
    
        return self
    


class TermsSettings(cogbuilder.Builder[elasticsearch.TermsSettings]):
    _internal: elasticsearch.TermsSettings

    def __init__(self):
        self._internal = elasticsearch.TermsSettings()

    def build(self) -> elasticsearch.TermsSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def order(self, order: elasticsearch.TermsOrder) -> typing.Self:    
        self._internal.order = order
    
        return self
    
    def size(self, size: str) -> typing.Self:    
        self._internal.size = size
    
        return self
    
    def min_doc_count(self, min_doc_count: str) -> typing.Self:    
        self._internal.min_doc_count = min_doc_count
    
        return self
    
    def order_by(self, order_by: str) -> typing.Self:    
        self._internal.order_by = order_by
    
        return self
    
    def missing(self, missing: str) -> typing.Self:    
        self._internal.missing = missing
    
        return self
    


class FiltersSettings(cogbuilder.Builder[elasticsearch.FiltersSettings]):
    _internal: elasticsearch.FiltersSettings

    def __init__(self):
        self._internal = elasticsearch.FiltersSettings()

    def build(self) -> elasticsearch.FiltersSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def filters(self, filters: list[cogbuilder.Builder[elasticsearch.Filter]]) -> typing.Self:    
        filters_resources = [r1.build() for r1 in filters]
        self._internal.filters = filters_resources
    
        return self
    


class GeoHashGridSettings(cogbuilder.Builder[elasticsearch.GeoHashGridSettings]):
    _internal: elasticsearch.GeoHashGridSettings

    def __init__(self):
        self._internal = elasticsearch.GeoHashGridSettings()

    def build(self) -> elasticsearch.GeoHashGridSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def precision(self, precision: str) -> typing.Self:    
        self._internal.precision = precision
    
        return self
    


class BaseMetricAggregation(cogbuilder.Builder[elasticsearch.BaseMetricAggregation]):
    _internal: elasticsearch.BaseMetricAggregation

    def __init__(self):
        self._internal = elasticsearch.BaseMetricAggregation()

    def build(self) -> elasticsearch.BaseMetricAggregation:
        """
        Builds the object.
        """
        return self._internal    
    
    def type(self, type_val: elasticsearch.MetricAggregationType) -> typing.Self:    
        self._internal.type_val = type_val
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class MetricAggregationWithField(cogbuilder.Builder[elasticsearch.MetricAggregationWithField]):
    _internal: elasticsearch.MetricAggregationWithField

    def __init__(self):
        self._internal = elasticsearch.MetricAggregationWithField()

    def build(self) -> elasticsearch.MetricAggregationWithField:
        """
        Builds the object.
        """
        return self._internal    
    
    def field(self, field: str) -> typing.Self:    
        self._internal.field = field
    
        return self
    
    def type(self, type_val: elasticsearch.MetricAggregationType) -> typing.Self:    
        self._internal.type_val = type_val
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class MetricAggregationWithMissingSupport(cogbuilder.Builder[elasticsearch.MetricAggregationWithMissingSupport]):
    _internal: elasticsearch.MetricAggregationWithMissingSupport

    def __init__(self):
        self._internal = elasticsearch.MetricAggregationWithMissingSupport()

    def build(self) -> elasticsearch.MetricAggregationWithMissingSupport:
        """
        Builds the object.
        """
        return self._internal    
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchMetricAggregationWithMissingSupportSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    
    def type(self, type_val: elasticsearch.MetricAggregationType) -> typing.Self:    
        self._internal.type_val = type_val
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class MetricAggregationWithInlineScript(cogbuilder.Builder[elasticsearch.MetricAggregationWithInlineScript]):
    _internal: elasticsearch.MetricAggregationWithInlineScript

    def __init__(self):
        self._internal = elasticsearch.MetricAggregationWithInlineScript()

    def build(self) -> elasticsearch.MetricAggregationWithInlineScript:
        """
        Builds the object.
        """
        return self._internal    
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchMetricAggregationWithInlineScriptSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    
    def type(self, type_val: elasticsearch.MetricAggregationType) -> typing.Self:    
        self._internal.type_val = type_val
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class ExtendedStat(cogbuilder.Builder[elasticsearch.ExtendedStat]):
    _internal: elasticsearch.ExtendedStat

    def __init__(self):
        self._internal = elasticsearch.ExtendedStat()

    def build(self) -> elasticsearch.ExtendedStat:
        """
        Builds the object.
        """
        return self._internal    
    
    def label(self, label: str) -> typing.Self:    
        self._internal.label = label
    
        return self
    
    def value(self, value: elasticsearch.ExtendedStatMetaType) -> typing.Self:    
        self._internal.value = value
    
        return self
    


class BasePipelineMetricAggregation(cogbuilder.Builder[elasticsearch.BasePipelineMetricAggregation]):
    _internal: elasticsearch.BasePipelineMetricAggregation

    def __init__(self):
        self._internal = elasticsearch.BasePipelineMetricAggregation()

    def build(self) -> elasticsearch.BasePipelineMetricAggregation:
        """
        Builds the object.
        """
        return self._internal    
    
    def pipeline_agg(self, pipeline_agg: str) -> typing.Self:    
        self._internal.pipeline_agg = pipeline_agg
    
        return self
    
    def field(self, field: str) -> typing.Self:    
        self._internal.field = field
    
        return self
    
    def type(self, type_val: str) -> typing.Self:    
        self._internal.type_val = type_val
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class PipelineMetricAggregationWithMultipleBucketPaths(cogbuilder.Builder[elasticsearch.PipelineMetricAggregationWithMultipleBucketPaths]):
    _internal: elasticsearch.PipelineMetricAggregationWithMultipleBucketPaths

    def __init__(self):
        self._internal = elasticsearch.PipelineMetricAggregationWithMultipleBucketPaths()

    def build(self) -> elasticsearch.PipelineMetricAggregationWithMultipleBucketPaths:
        """
        Builds the object.
        """
        return self._internal    
    
    def pipeline_variables(self, pipeline_variables: list[cogbuilder.Builder[elasticsearch.PipelineVariable]]) -> typing.Self:    
        pipeline_variables_resources = [r1.build() for r1 in pipeline_variables]
        self._internal.pipeline_variables = pipeline_variables_resources
    
        return self
    
    def type(self, type_val: elasticsearch.MetricAggregationType) -> typing.Self:    
        self._internal.type_val = type_val
    
        return self
    
    def id(self, id_val: str) -> typing.Self:    
        self._internal.id_val = id_val
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        self._internal.hide = hide
    
        return self
    


class MovingAverageModelOption(cogbuilder.Builder[elasticsearch.MovingAverageModelOption]):
    _internal: elasticsearch.MovingAverageModelOption

    def __init__(self):
        self._internal = elasticsearch.MovingAverageModelOption()

    def build(self) -> elasticsearch.MovingAverageModelOption:
        """
        Builds the object.
        """
        return self._internal    
    
    def label(self, label: str) -> typing.Self:    
        self._internal.label = label
    
        return self
    
    def value(self, value: elasticsearch.MovingAverageModel) -> typing.Self:    
        self._internal.value = value
    
        return self
    


class BaseMovingAverageModelSettings(cogbuilder.Builder[elasticsearch.BaseMovingAverageModelSettings]):
    _internal: elasticsearch.BaseMovingAverageModelSettings

    def __init__(self):
        self._internal = elasticsearch.BaseMovingAverageModelSettings()

    def build(self) -> elasticsearch.BaseMovingAverageModelSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def model(self, model: elasticsearch.MovingAverageModel) -> typing.Self:    
        self._internal.model = model
    
        return self
    
    def window(self, window: str) -> typing.Self:    
        self._internal.window = window
    
        return self
    
    def predict(self, predict: str) -> typing.Self:    
        self._internal.predict = predict
    
        return self
    


class MovingAverageSimpleModelSettings(cogbuilder.Builder[elasticsearch.MovingAverageSimpleModelSettings]):
    _internal: elasticsearch.MovingAverageSimpleModelSettings

    def __init__(self):
        self._internal = elasticsearch.MovingAverageSimpleModelSettings()

    def build(self) -> elasticsearch.MovingAverageSimpleModelSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def window(self, window: str) -> typing.Self:    
        self._internal.window = window
    
        return self
    
    def predict(self, predict: str) -> typing.Self:    
        self._internal.predict = predict
    
        return self
    


class MovingAverageLinearModelSettings(cogbuilder.Builder[elasticsearch.MovingAverageLinearModelSettings]):
    _internal: elasticsearch.MovingAverageLinearModelSettings

    def __init__(self):
        self._internal = elasticsearch.MovingAverageLinearModelSettings()

    def build(self) -> elasticsearch.MovingAverageLinearModelSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def window(self, window: str) -> typing.Self:    
        self._internal.window = window
    
        return self
    
    def predict(self, predict: str) -> typing.Self:    
        self._internal.predict = predict
    
        return self
    


class MovingAverageEWMAModelSettings(cogbuilder.Builder[elasticsearch.MovingAverageEWMAModelSettings]):
    _internal: elasticsearch.MovingAverageEWMAModelSettings

    def __init__(self):
        self._internal = elasticsearch.MovingAverageEWMAModelSettings()

    def build(self) -> elasticsearch.MovingAverageEWMAModelSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchMovingAverageEWMAModelSettingsSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    
    def window(self, window: str) -> typing.Self:    
        self._internal.window = window
    
        return self
    
    def minimize(self, minimize: bool) -> typing.Self:    
        self._internal.minimize = minimize
    
        return self
    
    def predict(self, predict: str) -> typing.Self:    
        self._internal.predict = predict
    
        return self
    


class MovingAverageHoltModelSettings(cogbuilder.Builder[elasticsearch.MovingAverageHoltModelSettings]):
    _internal: elasticsearch.MovingAverageHoltModelSettings

    def __init__(self):
        self._internal = elasticsearch.MovingAverageHoltModelSettings()

    def build(self) -> elasticsearch.MovingAverageHoltModelSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchMovingAverageHoltModelSettingsSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    
    def window(self, window: str) -> typing.Self:    
        self._internal.window = window
    
        return self
    
    def minimize(self, minimize: bool) -> typing.Self:    
        self._internal.minimize = minimize
    
        return self
    
    def predict(self, predict: str) -> typing.Self:    
        self._internal.predict = predict
    
        return self
    


class MovingAverageHoltWintersModelSettings(cogbuilder.Builder[elasticsearch.MovingAverageHoltWintersModelSettings]):
    _internal: elasticsearch.MovingAverageHoltWintersModelSettings

    def __init__(self):
        self._internal = elasticsearch.MovingAverageHoltWintersModelSettings()

    def build(self) -> elasticsearch.MovingAverageHoltWintersModelSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def settings(self, settings: cogbuilder.Builder[elasticsearch.ElasticsearchMovingAverageHoltWintersModelSettingsSettings]) -> typing.Self:    
        settings_resource = settings.build()
        self._internal.settings = settings_resource
    
        return self
    
    def window(self, window: str) -> typing.Self:    
        self._internal.window = window
    
        return self
    
    def minimize(self, minimize: bool) -> typing.Self:    
        self._internal.minimize = minimize
    
        return self
    
    def predict(self, predict: str) -> typing.Self:    
        self._internal.predict = predict
    
        return self
    


class Dataquery(cogbuilder.Builder[elasticsearch.Dataquery]):
    _internal: elasticsearch.Dataquery

    def __init__(self):
        self._internal = elasticsearch.Dataquery()

    def build(self) -> elasticsearch.Dataquery:
        """
        Builds the object.
        """
        return self._internal    
    
    def alias(self, alias: str) -> typing.Self:    
        """
        Alias pattern
        """
            
        self._internal.alias = alias
    
        return self
    
    def query(self, query: str) -> typing.Self:    
        """
        Lucene query
        """
            
        self._internal.query = query
    
        return self
    
    def time_field(self, time_field: str) -> typing.Self:    
        """
        Name of time field
        """
            
        self._internal.time_field = time_field
    
        return self
    
    def bucket_aggs(self, bucket_aggs: list[cogbuilder.Builder[elasticsearch.BucketAggregation]]) -> typing.Self:    
        """
        List of bucket aggregations
        """
            
        bucket_aggs_resources = [r1.build() for r1 in bucket_aggs]
        self._internal.bucket_aggs = bucket_aggs_resources
    
        return self
    
    def metrics(self, metrics: list[cogbuilder.Builder[elasticsearch.MetricAggregation]]) -> typing.Self:    
        """
        List of metric aggregations
        """
            
        metrics_resources = [r1.build() for r1 in metrics]
        self._internal.metrics = metrics_resources
    
        return self
    
    def ref_id(self, ref_id: str) -> typing.Self:    
        """
        A unique identifier for the query within the list of targets.
        In server side expressions, the refId is used as a variable name to identify results.
        By default, the UI will assign A->Z; however setting meaningful names may be useful.
        """
            
        self._internal.ref_id = ref_id
    
        return self
    
    def hide(self, hide: bool) -> typing.Self:    
        """
        true if query is disabled (ie should not be returned to the dashboard)
        Note this does not always imply that the query should not be executed since
        the results from a hidden query may be used as the input to other queries (SSE etc)
        """
            
        self._internal.hide = hide
    
        return self
    
    def query_type(self, query_type: str) -> typing.Self:    
        """
        Specify the query flavor
        TODO make this required and give it a default
        """
            
        self._internal.query_type = query_type
    
        return self
    
    def datasource(self, datasource: dashboard.DataSourceRef) -> typing.Self:    
        """
        For mixed data sources the selected datasource is on the query level.
        For non mixed scenarios this is undefined.
        TODO find a better way to do this ^ that's friendly to schema
        TODO this shouldn't be unknown but DataSourceRef | null
        """
            
        self._internal.datasource = datasource
    
        return self
    


class ElasticsearchDateHistogramSettings(cogbuilder.Builder[elasticsearch.ElasticsearchDateHistogramSettings]):
    _internal: elasticsearch.ElasticsearchDateHistogramSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchDateHistogramSettings()

    def build(self) -> elasticsearch.ElasticsearchDateHistogramSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def interval(self, interval: str) -> typing.Self:    
        self._internal.interval = interval
    
        return self
    
    def min_doc_count(self, min_doc_count: str) -> typing.Self:    
        self._internal.min_doc_count = min_doc_count
    
        return self
    
    def trim_edges(self, trim_edges: str) -> typing.Self:    
        self._internal.trim_edges = trim_edges
    
        return self
    
    def offset(self, offset: str) -> typing.Self:    
        self._internal.offset = offset
    
        return self
    
    def time_zone(self, time_zone: str) -> typing.Self:    
        self._internal.time_zone = time_zone
    
        return self
    


class ElasticsearchHistogramSettings(cogbuilder.Builder[elasticsearch.ElasticsearchHistogramSettings]):
    _internal: elasticsearch.ElasticsearchHistogramSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchHistogramSettings()

    def build(self) -> elasticsearch.ElasticsearchHistogramSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def interval(self, interval: str) -> typing.Self:    
        self._internal.interval = interval
    
        return self
    
    def min_doc_count(self, min_doc_count: str) -> typing.Self:    
        self._internal.min_doc_count = min_doc_count
    
        return self
    


class ElasticsearchTermsSettings(cogbuilder.Builder[elasticsearch.ElasticsearchTermsSettings]):
    _internal: elasticsearch.ElasticsearchTermsSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchTermsSettings()

    def build(self) -> elasticsearch.ElasticsearchTermsSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def order(self, order: elasticsearch.TermsOrder) -> typing.Self:    
        self._internal.order = order
    
        return self
    
    def size(self, size: str) -> typing.Self:    
        self._internal.size = size
    
        return self
    
    def min_doc_count(self, min_doc_count: str) -> typing.Self:    
        self._internal.min_doc_count = min_doc_count
    
        return self
    
    def order_by(self, order_by: str) -> typing.Self:    
        self._internal.order_by = order_by
    
        return self
    
    def missing(self, missing: str) -> typing.Self:    
        self._internal.missing = missing
    
        return self
    


class ElasticsearchFiltersSettings(cogbuilder.Builder[elasticsearch.ElasticsearchFiltersSettings]):
    _internal: elasticsearch.ElasticsearchFiltersSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchFiltersSettings()

    def build(self) -> elasticsearch.ElasticsearchFiltersSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def filters(self, filters: list[cogbuilder.Builder[elasticsearch.Filter]]) -> typing.Self:    
        filters_resources = [r1.build() for r1 in filters]
        self._internal.filters = filters_resources
    
        return self
    


class ElasticsearchGeoHashGridSettings(cogbuilder.Builder[elasticsearch.ElasticsearchGeoHashGridSettings]):
    _internal: elasticsearch.ElasticsearchGeoHashGridSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchGeoHashGridSettings()

    def build(self) -> elasticsearch.ElasticsearchGeoHashGridSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def precision(self, precision: str) -> typing.Self:    
        self._internal.precision = precision
    
        return self
    


class ElasticsearchDerivativeSettings(cogbuilder.Builder[elasticsearch.ElasticsearchDerivativeSettings]):
    _internal: elasticsearch.ElasticsearchDerivativeSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchDerivativeSettings()

    def build(self) -> elasticsearch.ElasticsearchDerivativeSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def unit(self, unit: str) -> typing.Self:    
        self._internal.unit = unit
    
        return self
    


class ElasticsearchCumulativeSumSettings(cogbuilder.Builder[elasticsearch.ElasticsearchCumulativeSumSettings]):
    _internal: elasticsearch.ElasticsearchCumulativeSumSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchCumulativeSumSettings()

    def build(self) -> elasticsearch.ElasticsearchCumulativeSumSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def format(self, format_val: str) -> typing.Self:    
        self._internal.format_val = format_val
    
        return self
    


class ElasticsearchBucketScriptSettings(cogbuilder.Builder[elasticsearch.ElasticsearchBucketScriptSettings]):
    _internal: elasticsearch.ElasticsearchBucketScriptSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchBucketScriptSettings()

    def build(self) -> elasticsearch.ElasticsearchBucketScriptSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def script(self, script: cogbuilder.Builder[elasticsearch.InlineScript]) -> typing.Self:    
        script_resource = script.build()
        self._internal.script = script_resource
    
        return self
    


class ElasticsearchInlineScript(cogbuilder.Builder[elasticsearch.ElasticsearchInlineScript]):
    _internal: elasticsearch.ElasticsearchInlineScript

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchInlineScript()

    def build(self) -> elasticsearch.ElasticsearchInlineScript:
        """
        Builds the object.
        """
        return self._internal    
    
    def inline(self, inline: str) -> typing.Self:    
        self._internal.inline = inline
    
        return self
    


class ElasticsearchSerialDiffSettings(cogbuilder.Builder[elasticsearch.ElasticsearchSerialDiffSettings]):
    _internal: elasticsearch.ElasticsearchSerialDiffSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchSerialDiffSettings()

    def build(self) -> elasticsearch.ElasticsearchSerialDiffSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def lag(self, lag: str) -> typing.Self:    
        self._internal.lag = lag
    
        return self
    


class ElasticsearchRawDataSettings(cogbuilder.Builder[elasticsearch.ElasticsearchRawDataSettings]):
    _internal: elasticsearch.ElasticsearchRawDataSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchRawDataSettings()

    def build(self) -> elasticsearch.ElasticsearchRawDataSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def size(self, size: str) -> typing.Self:    
        self._internal.size = size
    
        return self
    


class ElasticsearchRawDocumentSettings(cogbuilder.Builder[elasticsearch.ElasticsearchRawDocumentSettings]):
    _internal: elasticsearch.ElasticsearchRawDocumentSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchRawDocumentSettings()

    def build(self) -> elasticsearch.ElasticsearchRawDocumentSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def size(self, size: str) -> typing.Self:    
        self._internal.size = size
    
        return self
    


class ElasticsearchUniqueCountSettings(cogbuilder.Builder[elasticsearch.ElasticsearchUniqueCountSettings]):
    _internal: elasticsearch.ElasticsearchUniqueCountSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchUniqueCountSettings()

    def build(self) -> elasticsearch.ElasticsearchUniqueCountSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def precision_threshold(self, precision_threshold: str) -> typing.Self:    
        self._internal.precision_threshold = precision_threshold
    
        return self
    
    def missing(self, missing: str) -> typing.Self:    
        self._internal.missing = missing
    
        return self
    


class ElasticsearchPercentilesSettings(cogbuilder.Builder[elasticsearch.ElasticsearchPercentilesSettings]):
    _internal: elasticsearch.ElasticsearchPercentilesSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchPercentilesSettings()

    def build(self) -> elasticsearch.ElasticsearchPercentilesSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def script(self, script: cogbuilder.Builder[elasticsearch.InlineScript]) -> typing.Self:    
        script_resource = script.build()
        self._internal.script = script_resource
    
        return self
    
    def missing(self, missing: str) -> typing.Self:    
        self._internal.missing = missing
    
        return self
    
    def percents(self, percents: list[str]) -> typing.Self:    
        self._internal.percents = percents
    
        return self
    


class ElasticsearchExtendedStatsSettings(cogbuilder.Builder[elasticsearch.ElasticsearchExtendedStatsSettings]):
    _internal: elasticsearch.ElasticsearchExtendedStatsSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchExtendedStatsSettings()

    def build(self) -> elasticsearch.ElasticsearchExtendedStatsSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def script(self, script: cogbuilder.Builder[elasticsearch.InlineScript]) -> typing.Self:    
        script_resource = script.build()
        self._internal.script = script_resource
    
        return self
    
    def missing(self, missing: str) -> typing.Self:    
        self._internal.missing = missing
    
        return self
    
    def sigma(self, sigma: str) -> typing.Self:    
        self._internal.sigma = sigma
    
        return self
    


class ElasticsearchMinSettings(cogbuilder.Builder[elasticsearch.ElasticsearchMinSettings]):
    _internal: elasticsearch.ElasticsearchMinSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchMinSettings()

    def build(self) -> elasticsearch.ElasticsearchMinSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def script(self, script: cogbuilder.Builder[elasticsearch.InlineScript]) -> typing.Self:    
        script_resource = script.build()
        self._internal.script = script_resource
    
        return self
    
    def missing(self, missing: str) -> typing.Self:    
        self._internal.missing = missing
    
        return self
    


class ElasticsearchMaxSettings(cogbuilder.Builder[elasticsearch.ElasticsearchMaxSettings]):
    _internal: elasticsearch.ElasticsearchMaxSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchMaxSettings()

    def build(self) -> elasticsearch.ElasticsearchMaxSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def script(self, script: cogbuilder.Builder[elasticsearch.InlineScript]) -> typing.Self:    
        script_resource = script.build()
        self._internal.script = script_resource
    
        return self
    
    def missing(self, missing: str) -> typing.Self:    
        self._internal.missing = missing
    
        return self
    


class ElasticsearchSumSettings(cogbuilder.Builder[elasticsearch.ElasticsearchSumSettings]):
    _internal: elasticsearch.ElasticsearchSumSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchSumSettings()

    def build(self) -> elasticsearch.ElasticsearchSumSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def script(self, script: cogbuilder.Builder[elasticsearch.InlineScript]) -> typing.Self:    
        script_resource = script.build()
        self._internal.script = script_resource
    
        return self
    
    def missing(self, missing: str) -> typing.Self:    
        self._internal.missing = missing
    
        return self
    


class ElasticsearchAverageSettings(cogbuilder.Builder[elasticsearch.ElasticsearchAverageSettings]):
    _internal: elasticsearch.ElasticsearchAverageSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchAverageSettings()

    def build(self) -> elasticsearch.ElasticsearchAverageSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def script(self, script: cogbuilder.Builder[elasticsearch.InlineScript]) -> typing.Self:    
        script_resource = script.build()
        self._internal.script = script_resource
    
        return self
    
    def missing(self, missing: str) -> typing.Self:    
        self._internal.missing = missing
    
        return self
    


class ElasticsearchMovingFunctionSettings(cogbuilder.Builder[elasticsearch.ElasticsearchMovingFunctionSettings]):
    _internal: elasticsearch.ElasticsearchMovingFunctionSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchMovingFunctionSettings()

    def build(self) -> elasticsearch.ElasticsearchMovingFunctionSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def window(self, window: str) -> typing.Self:    
        self._internal.window = window
    
        return self
    
    def script(self, script: cogbuilder.Builder[elasticsearch.InlineScript]) -> typing.Self:    
        script_resource = script.build()
        self._internal.script = script_resource
    
        return self
    
    def shift(self, shift: str) -> typing.Self:    
        self._internal.shift = shift
    
        return self
    


class ElasticsearchLogsSettings(cogbuilder.Builder[elasticsearch.ElasticsearchLogsSettings]):
    _internal: elasticsearch.ElasticsearchLogsSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchLogsSettings()

    def build(self) -> elasticsearch.ElasticsearchLogsSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def limit(self, limit: str) -> typing.Self:    
        self._internal.limit = limit
    
        return self
    


class ElasticsearchRateSettings(cogbuilder.Builder[elasticsearch.ElasticsearchRateSettings]):
    _internal: elasticsearch.ElasticsearchRateSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchRateSettings()

    def build(self) -> elasticsearch.ElasticsearchRateSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def unit(self, unit: str) -> typing.Self:    
        self._internal.unit = unit
    
        return self
    
    def mode(self, mode: str) -> typing.Self:    
        self._internal.mode = mode
    
        return self
    


class ElasticsearchTopMetricsSettings(cogbuilder.Builder[elasticsearch.ElasticsearchTopMetricsSettings]):
    _internal: elasticsearch.ElasticsearchTopMetricsSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchTopMetricsSettings()

    def build(self) -> elasticsearch.ElasticsearchTopMetricsSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def order(self, order: str) -> typing.Self:    
        self._internal.order = order
    
        return self
    
    def order_by(self, order_by: str) -> typing.Self:    
        self._internal.order_by = order_by
    
        return self
    
    def metrics(self, metrics: list[str]) -> typing.Self:    
        self._internal.metrics = metrics
    
        return self
    


class ElasticsearchMetricAggregationWithMissingSupportSettings(cogbuilder.Builder[elasticsearch.ElasticsearchMetricAggregationWithMissingSupportSettings]):
    _internal: elasticsearch.ElasticsearchMetricAggregationWithMissingSupportSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchMetricAggregationWithMissingSupportSettings()

    def build(self) -> elasticsearch.ElasticsearchMetricAggregationWithMissingSupportSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def missing(self, missing: str) -> typing.Self:    
        self._internal.missing = missing
    
        return self
    


class ElasticsearchMetricAggregationWithInlineScriptSettings(cogbuilder.Builder[elasticsearch.ElasticsearchMetricAggregationWithInlineScriptSettings]):
    _internal: elasticsearch.ElasticsearchMetricAggregationWithInlineScriptSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchMetricAggregationWithInlineScriptSettings()

    def build(self) -> elasticsearch.ElasticsearchMetricAggregationWithInlineScriptSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def script(self, script: cogbuilder.Builder[elasticsearch.InlineScript]) -> typing.Self:    
        script_resource = script.build()
        self._internal.script = script_resource
    
        return self
    


class ElasticsearchMovingAverageEWMAModelSettingsSettings(cogbuilder.Builder[elasticsearch.ElasticsearchMovingAverageEWMAModelSettingsSettings]):
    _internal: elasticsearch.ElasticsearchMovingAverageEWMAModelSettingsSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchMovingAverageEWMAModelSettingsSettings()

    def build(self) -> elasticsearch.ElasticsearchMovingAverageEWMAModelSettingsSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def alpha(self, alpha: str) -> typing.Self:    
        self._internal.alpha = alpha
    
        return self
    


class ElasticsearchMovingAverageHoltModelSettingsSettings(cogbuilder.Builder[elasticsearch.ElasticsearchMovingAverageHoltModelSettingsSettings]):
    _internal: elasticsearch.ElasticsearchMovingAverageHoltModelSettingsSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchMovingAverageHoltModelSettingsSettings()

    def build(self) -> elasticsearch.ElasticsearchMovingAverageHoltModelSettingsSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def alpha(self, alpha: str) -> typing.Self:    
        self._internal.alpha = alpha
    
        return self
    
    def beta(self, beta: str) -> typing.Self:    
        self._internal.beta = beta
    
        return self
    


class ElasticsearchMovingAverageHoltWintersModelSettingsSettings(cogbuilder.Builder[elasticsearch.ElasticsearchMovingAverageHoltWintersModelSettingsSettings]):
    _internal: elasticsearch.ElasticsearchMovingAverageHoltWintersModelSettingsSettings

    def __init__(self):
        self._internal = elasticsearch.ElasticsearchMovingAverageHoltWintersModelSettingsSettings()

    def build(self) -> elasticsearch.ElasticsearchMovingAverageHoltWintersModelSettingsSettings:
        """
        Builds the object.
        """
        return self._internal    
    
    def alpha(self, alpha: str) -> typing.Self:    
        self._internal.alpha = alpha
    
        return self
    
    def beta(self, beta: str) -> typing.Self:    
        self._internal.beta = beta
    
        return self
    
    def gamma(self, gamma: str) -> typing.Self:    
        self._internal.gamma = gamma
    
        return self
    
    def period(self, period: str) -> typing.Self:    
        self._internal.period = period
    
        return self
    
    def pad(self, pad: bool) -> typing.Self:    
        self._internal.pad = pad
    
        return self
    
