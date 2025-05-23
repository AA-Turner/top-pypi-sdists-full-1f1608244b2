"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

from abc import (
    ABCMeta,
    abstractmethod,
)
from chalk._gen.chalk.engine.v2.feature_values_chart_pb2 import (
    GetFeatureValuesTimeSeriesChartRequest,
    GetFeatureValuesTimeSeriesChartResponse,
)
from chalk._gen.chalk.engine.v2.feature_values_pb2 import (
    GetFeatureValuesRequest,
    GetFeatureValuesResponse,
)
from chalk._gen.chalk.engine.v2.query_log_pb2 import (
    GetQueryLogEntriesRequest,
    GetQueryLogEntriesResponse,
)
from chalk._gen.chalk.engine.v2.query_values_pb2 import (
    GetQueryValuesRequest,
    GetQueryValuesResponse,
)
from grpc import (
    Channel,
    Server,
    ServicerContext,
    UnaryUnaryMultiCallable,
)

class OfflineStoreServiceStub:
    """This service exposes endpoints for dealing with the offline store. It should never depend on the python graph.
    v2 introduces two breaking changes:
    Uses messages from engine.v2 instead of common.v1 (common is not meant for engine-specific messages)
    Removes certain endpoints added and had to be immediately deprecated due to deprecation
    """

    def __init__(self, channel: Channel) -> None: ...
    GetQueryLogEntries: UnaryUnaryMultiCallable[
        GetQueryLogEntriesRequest,
        GetQueryLogEntriesResponse,
    ]
    GetQueryValues: UnaryUnaryMultiCallable[
        GetQueryValuesRequest,
        GetQueryValuesResponse,
    ]
    GetFeatureValuesTimeSeriesChart: UnaryUnaryMultiCallable[
        GetFeatureValuesTimeSeriesChartRequest,
        GetFeatureValuesTimeSeriesChartResponse,
    ]
    GetFeatureValues: UnaryUnaryMultiCallable[
        GetFeatureValuesRequest,
        GetFeatureValuesResponse,
    ]

class OfflineStoreServiceServicer(metaclass=ABCMeta):
    """This service exposes endpoints for dealing with the offline store. It should never depend on the python graph.
    v2 introduces two breaking changes:
    Uses messages from engine.v2 instead of common.v1 (common is not meant for engine-specific messages)
    Removes certain endpoints added and had to be immediately deprecated due to deprecation
    """

    @abstractmethod
    def GetQueryLogEntries(
        self,
        request: GetQueryLogEntriesRequest,
        context: ServicerContext,
    ) -> GetQueryLogEntriesResponse: ...
    @abstractmethod
    def GetQueryValues(
        self,
        request: GetQueryValuesRequest,
        context: ServicerContext,
    ) -> GetQueryValuesResponse: ...
    @abstractmethod
    def GetFeatureValuesTimeSeriesChart(
        self,
        request: GetFeatureValuesTimeSeriesChartRequest,
        context: ServicerContext,
    ) -> GetFeatureValuesTimeSeriesChartResponse: ...
    @abstractmethod
    def GetFeatureValues(
        self,
        request: GetFeatureValuesRequest,
        context: ServicerContext,
    ) -> GetFeatureValuesResponse: ...

def add_OfflineStoreServiceServicer_to_server(servicer: OfflineStoreServiceServicer, server: Server) -> None: ...
