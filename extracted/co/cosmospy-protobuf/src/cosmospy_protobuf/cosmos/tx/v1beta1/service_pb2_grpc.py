"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....cosmos.tx.v1beta1 import service_pb2 as cosmos_dot_tx_dot_v1beta1_dot_service__pb2

class ServiceStub(object):
    """Service defines a gRPC service for interacting with transactions.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Simulate = channel.unary_unary('/cosmos.tx.v1beta1.Service/Simulate', request_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.SimulateRequest.SerializeToString, response_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.SimulateResponse.FromString)
        self.GetTx = channel.unary_unary('/cosmos.tx.v1beta1.Service/GetTx', request_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxRequest.SerializeToString, response_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxResponse.FromString)
        self.BroadcastTx = channel.unary_unary('/cosmos.tx.v1beta1.Service/BroadcastTx', request_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.BroadcastTxRequest.SerializeToString, response_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.BroadcastTxResponse.FromString)
        self.GetTxsEvent = channel.unary_unary('/cosmos.tx.v1beta1.Service/GetTxsEvent', request_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxsEventRequest.SerializeToString, response_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxsEventResponse.FromString)
        self.GetBlockWithTxs = channel.unary_unary('/cosmos.tx.v1beta1.Service/GetBlockWithTxs', request_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetBlockWithTxsRequest.SerializeToString, response_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetBlockWithTxsResponse.FromString)

class ServiceServicer(object):
    """Service defines a gRPC service for interacting with transactions.
    """

    def Simulate(self, request, context):
        """Simulate simulates executing a transaction for estimating gas usage.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTx(self, request, context):
        """GetTx fetches a tx by hash.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BroadcastTx(self, request, context):
        """BroadcastTx broadcast transaction.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTxsEvent(self, request, context):
        """GetTxsEvent fetches txs by event.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlockWithTxs(self, request, context):
        """GetBlockWithTxs fetches a block with decoded txs.

        Since: cosmos-sdk 0.45.2
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_ServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'Simulate': grpc.unary_unary_rpc_method_handler(servicer.Simulate, request_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.SimulateRequest.FromString, response_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.SimulateResponse.SerializeToString), 'GetTx': grpc.unary_unary_rpc_method_handler(servicer.GetTx, request_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxRequest.FromString, response_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxResponse.SerializeToString), 'BroadcastTx': grpc.unary_unary_rpc_method_handler(servicer.BroadcastTx, request_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.BroadcastTxRequest.FromString, response_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.BroadcastTxResponse.SerializeToString), 'GetTxsEvent': grpc.unary_unary_rpc_method_handler(servicer.GetTxsEvent, request_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxsEventRequest.FromString, response_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxsEventResponse.SerializeToString), 'GetBlockWithTxs': grpc.unary_unary_rpc_method_handler(servicer.GetBlockWithTxs, request_deserializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetBlockWithTxsRequest.FromString, response_serializer=cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetBlockWithTxsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('cosmos.tx.v1beta1.Service', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Service(object):
    """Service defines a gRPC service for interacting with transactions.
    """

    @staticmethod
    def Simulate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.tx.v1beta1.Service/Simulate', cosmos_dot_tx_dot_v1beta1_dot_service__pb2.SimulateRequest.SerializeToString, cosmos_dot_tx_dot_v1beta1_dot_service__pb2.SimulateResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTx(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.tx.v1beta1.Service/GetTx', cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxRequest.SerializeToString, cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BroadcastTx(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.tx.v1beta1.Service/BroadcastTx', cosmos_dot_tx_dot_v1beta1_dot_service__pb2.BroadcastTxRequest.SerializeToString, cosmos_dot_tx_dot_v1beta1_dot_service__pb2.BroadcastTxResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTxsEvent(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.tx.v1beta1.Service/GetTxsEvent', cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxsEventRequest.SerializeToString, cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetTxsEventResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBlockWithTxs(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.tx.v1beta1.Service/GetBlockWithTxs', cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetBlockWithTxsRequest.SerializeToString, cosmos_dot_tx_dot_v1beta1_dot_service__pb2.GetBlockWithTxsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)