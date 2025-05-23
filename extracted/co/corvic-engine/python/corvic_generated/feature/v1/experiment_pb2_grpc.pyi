"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import collections.abc
import corvic_generated.feature.v1.experiment_pb2
import grpc
import grpc.aio
import typing

_T = typing.TypeVar('_T')

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta):
    ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore
    ...

class ExperimentServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    GetExperiment: grpc.UnaryUnaryMultiCallable[
        corvic_generated.feature.v1.experiment_pb2.GetExperimentRequest,
        corvic_generated.feature.v1.experiment_pb2.GetExperimentResponse,
    ]
    CreateExperiment: grpc.UnaryUnaryMultiCallable[
        corvic_generated.feature.v1.experiment_pb2.CreateExperimentRequest,
        corvic_generated.feature.v1.experiment_pb2.CreateExperimentResponse,
    ]
    DeleteExperiment: grpc.UnaryUnaryMultiCallable[
        corvic_generated.feature.v1.experiment_pb2.DeleteExperimentRequest,
        corvic_generated.feature.v1.experiment_pb2.DeleteExperimentResponse,
    ]
    ListExperiments: grpc.UnaryUnaryMultiCallable[
        corvic_generated.feature.v1.experiment_pb2.ListExperimentsRequest,
        corvic_generated.feature.v1.experiment_pb2.ListExperimentsResponse,
    ]
    GetExperimentResult: grpc.UnaryUnaryMultiCallable[
        corvic_generated.feature.v1.experiment_pb2.GetExperimentResultRequest,
        corvic_generated.feature.v1.experiment_pb2.GetExperimentResultResponse,
    ]
    GetExperimentVisualization: grpc.UnaryUnaryMultiCallable[
        corvic_generated.feature.v1.experiment_pb2.GetExperimentVisualizationRequest,
        corvic_generated.feature.v1.experiment_pb2.GetExperimentVisualizationResponse,
    ]

class ExperimentServiceAsyncStub:
    GetExperiment: grpc.aio.UnaryUnaryMultiCallable[
        corvic_generated.feature.v1.experiment_pb2.GetExperimentRequest,
        corvic_generated.feature.v1.experiment_pb2.GetExperimentResponse,
    ]
    CreateExperiment: grpc.aio.UnaryUnaryMultiCallable[
        corvic_generated.feature.v1.experiment_pb2.CreateExperimentRequest,
        corvic_generated.feature.v1.experiment_pb2.CreateExperimentResponse,
    ]
    DeleteExperiment: grpc.aio.UnaryUnaryMultiCallable[
        corvic_generated.feature.v1.experiment_pb2.DeleteExperimentRequest,
        corvic_generated.feature.v1.experiment_pb2.DeleteExperimentResponse,
    ]
    ListExperiments: grpc.aio.UnaryUnaryMultiCallable[
        corvic_generated.feature.v1.experiment_pb2.ListExperimentsRequest,
        corvic_generated.feature.v1.experiment_pb2.ListExperimentsResponse,
    ]
    GetExperimentResult: grpc.aio.UnaryUnaryMultiCallable[
        corvic_generated.feature.v1.experiment_pb2.GetExperimentResultRequest,
        corvic_generated.feature.v1.experiment_pb2.GetExperimentResultResponse,
    ]
    GetExperimentVisualization: grpc.aio.UnaryUnaryMultiCallable[
        corvic_generated.feature.v1.experiment_pb2.GetExperimentVisualizationRequest,
        corvic_generated.feature.v1.experiment_pb2.GetExperimentVisualizationResponse,
    ]

class ExperimentServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetExperiment(
        self,
        request: corvic_generated.feature.v1.experiment_pb2.GetExperimentRequest,
        context: _ServicerContext,
    ) -> typing.Union[corvic_generated.feature.v1.experiment_pb2.GetExperimentResponse, collections.abc.Awaitable[corvic_generated.feature.v1.experiment_pb2.GetExperimentResponse]]: ...
    @abc.abstractmethod
    def CreateExperiment(
        self,
        request: corvic_generated.feature.v1.experiment_pb2.CreateExperimentRequest,
        context: _ServicerContext,
    ) -> typing.Union[corvic_generated.feature.v1.experiment_pb2.CreateExperimentResponse, collections.abc.Awaitable[corvic_generated.feature.v1.experiment_pb2.CreateExperimentResponse]]: ...
    @abc.abstractmethod
    def DeleteExperiment(
        self,
        request: corvic_generated.feature.v1.experiment_pb2.DeleteExperimentRequest,
        context: _ServicerContext,
    ) -> typing.Union[corvic_generated.feature.v1.experiment_pb2.DeleteExperimentResponse, collections.abc.Awaitable[corvic_generated.feature.v1.experiment_pb2.DeleteExperimentResponse]]: ...
    @abc.abstractmethod
    def ListExperiments(
        self,
        request: corvic_generated.feature.v1.experiment_pb2.ListExperimentsRequest,
        context: _ServicerContext,
    ) -> typing.Union[corvic_generated.feature.v1.experiment_pb2.ListExperimentsResponse, collections.abc.Awaitable[corvic_generated.feature.v1.experiment_pb2.ListExperimentsResponse]]: ...
    @abc.abstractmethod
    def GetExperimentResult(
        self,
        request: corvic_generated.feature.v1.experiment_pb2.GetExperimentResultRequest,
        context: _ServicerContext,
    ) -> typing.Union[corvic_generated.feature.v1.experiment_pb2.GetExperimentResultResponse, collections.abc.Awaitable[corvic_generated.feature.v1.experiment_pb2.GetExperimentResultResponse]]: ...
    @abc.abstractmethod
    def GetExperimentVisualization(
        self,
        request: corvic_generated.feature.v1.experiment_pb2.GetExperimentVisualizationRequest,
        context: _ServicerContext,
    ) -> typing.Union[corvic_generated.feature.v1.experiment_pb2.GetExperimentVisualizationResponse, collections.abc.Awaitable[corvic_generated.feature.v1.experiment_pb2.GetExperimentVisualizationResponse]]: ...

def add_ExperimentServiceServicer_to_server(servicer: ExperimentServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
