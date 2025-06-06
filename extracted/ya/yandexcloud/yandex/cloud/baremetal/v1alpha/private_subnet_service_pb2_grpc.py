# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.baremetal.v1alpha import private_subnet_pb2 as yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__pb2
from yandex.cloud.baremetal.v1alpha import private_subnet_service_pb2 as yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in yandex/cloud/baremetal/v1alpha/private_subnet_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class PrivateSubnetServiceStub(object):
    """A set of methods for managing PrivateSubnet resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.baremetal.v1alpha.PrivateSubnetService/Get',
                request_serializer=yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.GetPrivateSubnetRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__pb2.PrivateSubnet.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.baremetal.v1alpha.PrivateSubnetService/List',
                request_serializer=yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.ListPrivateSubnetRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.ListPrivateSubnetResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.baremetal.v1alpha.PrivateSubnetService/Create',
                request_serializer=yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.CreatePrivateSubnetRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/yandex.cloud.baremetal.v1alpha.PrivateSubnetService/Update',
                request_serializer=yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.UpdatePrivateSubnetRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.baremetal.v1alpha.PrivateSubnetService/Delete',
                request_serializer=yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.DeletePrivateSubnetRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.baremetal.v1alpha.PrivateSubnetService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.ListPrivateSubnetOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.ListPrivateSubnetOperationsResponse.FromString,
                _registered_method=True)


class PrivateSubnetServiceServicer(object):
    """A set of methods for managing PrivateSubnet resources.
    """

    def Get(self, request, context):
        """Returns the specific PrivateSubnet resource.

        To get the list of available PrivateSubnet resources, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of PrivateSubnet resources in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a private subnet in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified private subnet.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified private subnet.

        Deleting a private subnet removes its data permanently and is irreversible.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Lists operations for the specified private subnet.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PrivateSubnetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.GetPrivateSubnetRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__pb2.PrivateSubnet.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.ListPrivateSubnetRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.ListPrivateSubnetResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.CreatePrivateSubnetRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.UpdatePrivateSubnetRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.DeletePrivateSubnetRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.ListPrivateSubnetOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.ListPrivateSubnetOperationsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.baremetal.v1alpha.PrivateSubnetService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.baremetal.v1alpha.PrivateSubnetService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PrivateSubnetService(object):
    """A set of methods for managing PrivateSubnet resources.
    """

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.baremetal.v1alpha.PrivateSubnetService/Get',
            yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.GetPrivateSubnetRequest.SerializeToString,
            yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__pb2.PrivateSubnet.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.baremetal.v1alpha.PrivateSubnetService/List',
            yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.ListPrivateSubnetRequest.SerializeToString,
            yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.ListPrivateSubnetResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.baremetal.v1alpha.PrivateSubnetService/Create',
            yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.CreatePrivateSubnetRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.baremetal.v1alpha.PrivateSubnetService/Update',
            yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.UpdatePrivateSubnetRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.baremetal.v1alpha.PrivateSubnetService/Delete',
            yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.DeletePrivateSubnetRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListOperations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.baremetal.v1alpha.PrivateSubnetService/ListOperations',
            yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.ListPrivateSubnetOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_baremetal_dot_v1alpha_dot_private__subnet__service__pb2.ListPrivateSubnetOperationsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
