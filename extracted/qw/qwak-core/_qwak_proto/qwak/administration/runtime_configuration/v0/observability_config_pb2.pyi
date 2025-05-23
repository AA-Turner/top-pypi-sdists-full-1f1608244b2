"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import qwak.administration.runtime_configuration.v0.external.prometheus_config_pb2
import qwak.administration.runtime_configuration.v0.external.victoriametrics_config_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ObservabilityConfiguration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MONITORING_FIELD_NUMBER: builtins.int
    ALERTING_FIELD_NUMBER: builtins.int
    @property
    def monitoring(self) -> global___MonitoringConfiguration: ...
    @property
    def alerting(self) -> global___AlertingIntegrationConfiguration: ...
    def __init__(
        self,
        *,
        monitoring: global___MonitoringConfiguration | None = ...,
        alerting: global___AlertingIntegrationConfiguration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["alerting", b"alerting", "monitoring", b"monitoring"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["alerting", b"alerting", "monitoring", b"monitoring"]) -> None: ...

global___ObservabilityConfiguration = ObservabilityConfiguration

class MonitoringConfiguration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROMETHEUS_FIELD_NUMBER: builtins.int
    VICTORIA_METRICS_FIELD_NUMBER: builtins.int
    @property
    def prometheus(self) -> qwak.administration.runtime_configuration.v0.external.prometheus_config_pb2.PrometheusConfiguration: ...
    @property
    def victoria_metrics(self) -> qwak.administration.runtime_configuration.v0.external.victoriametrics_config_pb2.VictoriaMetricsConfiguration: ...
    def __init__(
        self,
        *,
        prometheus: qwak.administration.runtime_configuration.v0.external.prometheus_config_pb2.PrometheusConfiguration | None = ...,
        victoria_metrics: qwak.administration.runtime_configuration.v0.external.victoriametrics_config_pb2.VictoriaMetricsConfiguration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["prometheus", b"prometheus", "type", b"type", "victoria_metrics", b"victoria_metrics"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["prometheus", b"prometheus", "type", b"type", "victoria_metrics", b"victoria_metrics"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["type", b"type"]) -> typing_extensions.Literal["prometheus", "victoria_metrics"] | None: ...

global___MonitoringConfiguration = MonitoringConfiguration

class AlertingIntegrationConfiguration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROMETHEUS_FIELD_NUMBER: builtins.int
    VICTORIA_METRICS_FIELD_NUMBER: builtins.int
    @property
    def prometheus(self) -> qwak.administration.runtime_configuration.v0.external.prometheus_config_pb2.PrometheusConfiguration: ...
    @property
    def victoria_metrics(self) -> qwak.administration.runtime_configuration.v0.external.victoriametrics_config_pb2.VictoriaMetricsConfiguration: ...
    def __init__(
        self,
        *,
        prometheus: qwak.administration.runtime_configuration.v0.external.prometheus_config_pb2.PrometheusConfiguration | None = ...,
        victoria_metrics: qwak.administration.runtime_configuration.v0.external.victoriametrics_config_pb2.VictoriaMetricsConfiguration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["prometheus", b"prometheus", "type", b"type", "victoria_metrics", b"victoria_metrics"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["prometheus", b"prometheus", "type", b"type", "victoria_metrics", b"victoria_metrics"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["type", b"type"]) -> typing_extensions.Literal["prometheus", "victoria_metrics"] | None: ...

global___AlertingIntegrationConfiguration = AlertingIntegrationConfiguration
