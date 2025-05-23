# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter import advanced_rate_limiter_profile_pb2 as yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__pb2
from yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter import advanced_rate_limiter_profile_service_pb2 as yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__service__pb2

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
        + f' but the generated code in yandex/cloud/smartwebsecurity/v1/advanced_rate_limiter/advanced_rate_limiter_profile_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class AdvancedRateLimiterProfileServiceStub(object):
    """A set of methods for managing AdvancedRateLimiterProfile resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterProfileService/Get',
                request_serializer=yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__service__pb2.GetAdvancedRateLimiterProfileRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__pb2.AdvancedRateLimiterProfile.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterProfileService/List',
                request_serializer=yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__service__pb2.ListAdvancedRateLimiterProfilesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__service__pb2.ListAdvancedRateLimiterProfilesResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterProfileService/Create',
                request_serializer=yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__service__pb2.CreateAdvancedRateLimiterProfileRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterProfileService/Update',
                request_serializer=yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__service__pb2.UpdateAdvancedRateLimiterProfileRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterProfileService/Delete',
                request_serializer=yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__service__pb2.DeleteAdvancedRateLimiterProfileRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class AdvancedRateLimiterProfileServiceServicer(object):
    """A set of methods for managing AdvancedRateLimiterProfile resources.
    """

    def Get(self, request, context):
        """Returns the specified AdvancedRateLimiterProfile resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of AdvancedRateLimiterProfile resources in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a ARL profile in the specified folder using the data specified in the request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified ARL profile.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified ARL profile.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AdvancedRateLimiterProfileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__service__pb2.GetAdvancedRateLimiterProfileRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__pb2.AdvancedRateLimiterProfile.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__service__pb2.ListAdvancedRateLimiterProfilesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__service__pb2.ListAdvancedRateLimiterProfilesResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__service__pb2.CreateAdvancedRateLimiterProfileRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__service__pb2.UpdateAdvancedRateLimiterProfileRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__service__pb2.DeleteAdvancedRateLimiterProfileRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterProfileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterProfileService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class AdvancedRateLimiterProfileService(object):
    """A set of methods for managing AdvancedRateLimiterProfile resources.
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
            '/yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterProfileService/Get',
            yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__service__pb2.GetAdvancedRateLimiterProfileRequest.SerializeToString,
            yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__pb2.AdvancedRateLimiterProfile.FromString,
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
            '/yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterProfileService/List',
            yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__service__pb2.ListAdvancedRateLimiterProfilesRequest.SerializeToString,
            yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__service__pb2.ListAdvancedRateLimiterProfilesResponse.FromString,
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
            '/yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterProfileService/Create',
            yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__service__pb2.CreateAdvancedRateLimiterProfileRequest.SerializeToString,
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
            '/yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterProfileService/Update',
            yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__service__pb2.UpdateAdvancedRateLimiterProfileRequest.SerializeToString,
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
            '/yandex.cloud.smartwebsecurity.v1.advanced_rate_limiter.AdvancedRateLimiterProfileService/Delete',
            yandex_dot_cloud_dot_smartwebsecurity_dot_v1_dot_advanced__rate__limiter_dot_advanced__rate__limiter__profile__service__pb2.DeleteAdvancedRateLimiterProfileRequest.SerializeToString,
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
