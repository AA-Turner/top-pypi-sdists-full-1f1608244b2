# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from admobilize.proto.devicemanagement.v1 import device_manager_pb2 as admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2
from admobilize.proto.devicemanagement.v1 import resources_pb2 as admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class DeviceManagerStub(object):
    """API design guide: https://cloud.google.com/apis/design/

    The service that an application uses to create, update, delete, manipulate and obtain
    devices and projects.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateDevice = channel.unary_unary(
                '/admobilize.devicemanagement.v1.DeviceManager/CreateDevice',
                request_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.CreateDeviceRequest.SerializeToString,
                response_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Device.FromString,
                )
        self.GetDevice = channel.unary_unary(
                '/admobilize.devicemanagement.v1.DeviceManager/GetDevice',
                request_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.GetDeviceRequest.SerializeToString,
                response_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Device.FromString,
                )
        self.ListDevices = channel.unary_unary(
                '/admobilize.devicemanagement.v1.DeviceManager/ListDevices',
                request_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.ListDevicesRequest.SerializeToString,
                response_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.ListDevicesResponse.FromString,
                )
        self.UpdateDevice = channel.unary_unary(
                '/admobilize.devicemanagement.v1.DeviceManager/UpdateDevice',
                request_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.UpdateDeviceRequest.SerializeToString,
                response_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Device.FromString,
                )
        self.DeleteDevice = channel.unary_unary(
                '/admobilize.devicemanagement.v1.DeviceManager/DeleteDevice',
                request_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.DeleteDeviceRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.CreateProject = channel.unary_unary(
                '/admobilize.devicemanagement.v1.DeviceManager/CreateProject',
                request_serializer=admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Project.SerializeToString,
                response_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Project.FromString,
                )
        self.GetProject = channel.unary_unary(
                '/admobilize.devicemanagement.v1.DeviceManager/GetProject',
                request_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.GetProjectRequest.SerializeToString,
                response_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Project.FromString,
                )
        self.ListProjects = channel.unary_unary(
                '/admobilize.devicemanagement.v1.DeviceManager/ListProjects',
                request_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.ListProjectsRequest.SerializeToString,
                response_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.ListProjectsResponse.FromString,
                )
        self.UpdateProject = channel.unary_unary(
                '/admobilize.devicemanagement.v1.DeviceManager/UpdateProject',
                request_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.UpdateProjectRequest.SerializeToString,
                response_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Project.FromString,
                )
        self.DeleteProject = channel.unary_unary(
                '/admobilize.devicemanagement.v1.DeviceManager/DeleteProject',
                request_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.DeleteProjectRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.AddProjectUser = channel.unary_unary(
                '/admobilize.devicemanagement.v1.DeviceManager/AddProjectUser',
                request_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.AddProjectUserRequest.SerializeToString,
                response_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Project.FromString,
                )
        self.RemoveProjectUser = channel.unary_unary(
                '/admobilize.devicemanagement.v1.DeviceManager/RemoveProjectUser',
                request_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.RemoveProjectUserRequest.SerializeToString,
                response_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Project.FromString,
                )
        self.GenerateProvisioningToken = channel.unary_unary(
                '/admobilize.devicemanagement.v1.DeviceManager/GenerateProvisioningToken',
                request_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.GenerateProvisioningTokenRequest.SerializeToString,
                response_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.GenerateProvisioningTokenResponse.FromString,
                )
        self.ProvisionDevices = channel.unary_unary(
                '/admobilize.devicemanagement.v1.DeviceManager/ProvisionDevices',
                request_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.ProvisionDevicesRequest.SerializeToString,
                response_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.ProvisionDevicesResponse.FromString,
                )
        self.MoveDevices = channel.unary_unary(
                '/admobilize.devicemanagement.v1.DeviceManager/MoveDevices',
                request_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.MoveDevicesRequest.SerializeToString,
                response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
                )
        self.SendCommandToDevice = channel.unary_unary(
                '/admobilize.devicemanagement.v1.DeviceManager/SendCommandToDevice',
                request_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.SendCommandToDeviceRequest.SerializeToString,
                response_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.SendCommandToDeviceResponse.FromString,
                )
        self.BatchCreateDevices = channel.unary_unary(
                '/admobilize.devicemanagement.v1.DeviceManager/BatchCreateDevices',
                request_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.BatchCreateDevicesRequest.SerializeToString,
                response_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.BatchCreateDevicesResponse.FromString,
                )
        self.ArchiveDevice = channel.unary_unary(
                '/admobilize.devicemanagement.v1.DeviceManager/ArchiveDevice',
                request_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.ArchiveDeviceRequest.SerializeToString,
                response_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Device.FromString,
                )
        self.DearchiveDevice = channel.unary_unary(
                '/admobilize.devicemanagement.v1.DeviceManager/DearchiveDevice',
                request_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.DearchiveDeviceRequest.SerializeToString,
                response_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Device.FromString,
                )
        self.CreateServiceToken = channel.unary_unary(
                '/admobilize.devicemanagement.v1.DeviceManager/CreateServiceToken',
                request_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.CreateServiceTokenRequest.SerializeToString,
                response_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.CreateServiceTokenResponse.FromString,
                )


class DeviceManagerServicer(object):
    """API design guide: https://cloud.google.com/apis/design/

    The service that an application uses to create, update, delete, manipulate and obtain
    devices and projects.
    """

    def CreateDevice(self, request, context):
        """--- Standard Device methods -----------------------------------------------------------

        Creates a device
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDevice(self, request, context):
        """Gets a device
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDevices(self, request, context):
        """Lists devices in a project
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateDevice(self, request, context):
        """Updates a device
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteDevice(self, request, context):
        """Deletes a device
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateProject(self, request, context):
        """--- Standard Project methods -----------------------------------------------------------

        Creates a project
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProject(self, request, context):
        """Gets a project
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListProjects(self, request, context):
        """List the projects to which the current authenticated user has access to
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProject(self, request, context):
        """Updates a project
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteProject(self, request, context):
        """Deletes a project
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddProjectUser(self, request, context):
        """--- Custom methods -----------------------------------------------------------

        Add user to project
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveProjectUser(self, request, context):
        """Remove user from project
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateProvisioningToken(self, request, context):
        """Generate a new provisioning token for a device
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProvisionDevices(self, request, context):
        """Provision devices
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MoveDevices(self, request, context):
        """Move device from one project to another
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendCommandToDevice(self, request, context):
        """Send command to device
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchCreateDevices(self, request, context):
        """Create many devices at once
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ArchiveDevice(self, request, context):
        """Archives a device
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DearchiveDevice(self, request, context):
        """Dearchives a device
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateServiceToken(self, request, context):
        """Create a token used to call other services
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DeviceManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDevice,
                    request_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.CreateDeviceRequest.FromString,
                    response_serializer=admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Device.SerializeToString,
            ),
            'GetDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDevice,
                    request_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.GetDeviceRequest.FromString,
                    response_serializer=admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Device.SerializeToString,
            ),
            'ListDevices': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDevices,
                    request_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.ListDevicesRequest.FromString,
                    response_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.ListDevicesResponse.SerializeToString,
            ),
            'UpdateDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateDevice,
                    request_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.UpdateDeviceRequest.FromString,
                    response_serializer=admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Device.SerializeToString,
            ),
            'DeleteDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteDevice,
                    request_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.DeleteDeviceRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'CreateProject': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateProject,
                    request_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Project.FromString,
                    response_serializer=admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Project.SerializeToString,
            ),
            'GetProject': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProject,
                    request_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.GetProjectRequest.FromString,
                    response_serializer=admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Project.SerializeToString,
            ),
            'ListProjects': grpc.unary_unary_rpc_method_handler(
                    servicer.ListProjects,
                    request_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.ListProjectsRequest.FromString,
                    response_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.ListProjectsResponse.SerializeToString,
            ),
            'UpdateProject': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProject,
                    request_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.UpdateProjectRequest.FromString,
                    response_serializer=admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Project.SerializeToString,
            ),
            'DeleteProject': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteProject,
                    request_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.DeleteProjectRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'AddProjectUser': grpc.unary_unary_rpc_method_handler(
                    servicer.AddProjectUser,
                    request_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.AddProjectUserRequest.FromString,
                    response_serializer=admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Project.SerializeToString,
            ),
            'RemoveProjectUser': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveProjectUser,
                    request_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.RemoveProjectUserRequest.FromString,
                    response_serializer=admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Project.SerializeToString,
            ),
            'GenerateProvisioningToken': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateProvisioningToken,
                    request_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.GenerateProvisioningTokenRequest.FromString,
                    response_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.GenerateProvisioningTokenResponse.SerializeToString,
            ),
            'ProvisionDevices': grpc.unary_unary_rpc_method_handler(
                    servicer.ProvisionDevices,
                    request_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.ProvisionDevicesRequest.FromString,
                    response_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.ProvisionDevicesResponse.SerializeToString,
            ),
            'MoveDevices': grpc.unary_unary_rpc_method_handler(
                    servicer.MoveDevices,
                    request_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.MoveDevicesRequest.FromString,
                    response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
            ),
            'SendCommandToDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.SendCommandToDevice,
                    request_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.SendCommandToDeviceRequest.FromString,
                    response_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.SendCommandToDeviceResponse.SerializeToString,
            ),
            'BatchCreateDevices': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchCreateDevices,
                    request_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.BatchCreateDevicesRequest.FromString,
                    response_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.BatchCreateDevicesResponse.SerializeToString,
            ),
            'ArchiveDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.ArchiveDevice,
                    request_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.ArchiveDeviceRequest.FromString,
                    response_serializer=admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Device.SerializeToString,
            ),
            'DearchiveDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.DearchiveDevice,
                    request_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.DearchiveDeviceRequest.FromString,
                    response_serializer=admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Device.SerializeToString,
            ),
            'CreateServiceToken': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateServiceToken,
                    request_deserializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.CreateServiceTokenRequest.FromString,
                    response_serializer=admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.CreateServiceTokenResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'admobilize.devicemanagement.v1.DeviceManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DeviceManager(object):
    """API design guide: https://cloud.google.com/apis/design/

    The service that an application uses to create, update, delete, manipulate and obtain
    devices and projects.
    """

    @staticmethod
    def CreateDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.devicemanagement.v1.DeviceManager/CreateDevice',
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.CreateDeviceRequest.SerializeToString,
            admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Device.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.devicemanagement.v1.DeviceManager/GetDevice',
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.GetDeviceRequest.SerializeToString,
            admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Device.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListDevices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.devicemanagement.v1.DeviceManager/ListDevices',
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.ListDevicesRequest.SerializeToString,
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.ListDevicesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.devicemanagement.v1.DeviceManager/UpdateDevice',
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.UpdateDeviceRequest.SerializeToString,
            admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Device.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.devicemanagement.v1.DeviceManager/DeleteDevice',
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.DeleteDeviceRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.devicemanagement.v1.DeviceManager/CreateProject',
            admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Project.SerializeToString,
            admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Project.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.devicemanagement.v1.DeviceManager/GetProject',
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.GetProjectRequest.SerializeToString,
            admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Project.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListProjects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.devicemanagement.v1.DeviceManager/ListProjects',
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.ListProjectsRequest.SerializeToString,
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.ListProjectsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.devicemanagement.v1.DeviceManager/UpdateProject',
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.UpdateProjectRequest.SerializeToString,
            admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Project.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.devicemanagement.v1.DeviceManager/DeleteProject',
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.DeleteProjectRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddProjectUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.devicemanagement.v1.DeviceManager/AddProjectUser',
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.AddProjectUserRequest.SerializeToString,
            admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Project.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveProjectUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.devicemanagement.v1.DeviceManager/RemoveProjectUser',
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.RemoveProjectUserRequest.SerializeToString,
            admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Project.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GenerateProvisioningToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.devicemanagement.v1.DeviceManager/GenerateProvisioningToken',
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.GenerateProvisioningTokenRequest.SerializeToString,
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.GenerateProvisioningTokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ProvisionDevices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.devicemanagement.v1.DeviceManager/ProvisionDevices',
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.ProvisionDevicesRequest.SerializeToString,
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.ProvisionDevicesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MoveDevices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.devicemanagement.v1.DeviceManager/MoveDevices',
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.MoveDevicesRequest.SerializeToString,
            google_dot_longrunning_dot_operations__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendCommandToDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.devicemanagement.v1.DeviceManager/SendCommandToDevice',
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.SendCommandToDeviceRequest.SerializeToString,
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.SendCommandToDeviceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchCreateDevices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.devicemanagement.v1.DeviceManager/BatchCreateDevices',
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.BatchCreateDevicesRequest.SerializeToString,
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.BatchCreateDevicesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ArchiveDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.devicemanagement.v1.DeviceManager/ArchiveDevice',
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.ArchiveDeviceRequest.SerializeToString,
            admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Device.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DearchiveDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.devicemanagement.v1.DeviceManager/DearchiveDevice',
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.DearchiveDeviceRequest.SerializeToString,
            admobilize_dot_devicemanagement_dot_v1_dot_resources__pb2.Device.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateServiceToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.devicemanagement.v1.DeviceManager/CreateServiceToken',
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.CreateServiceTokenRequest.SerializeToString,
            admobilize_dot_devicemanagement_dot_v1_dot_device__manager__pb2.CreateServiceTokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
