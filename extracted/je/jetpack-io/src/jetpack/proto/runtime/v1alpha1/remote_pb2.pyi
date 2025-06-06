"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ErrorCode:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _ErrorCodeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ErrorCode.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN: _ErrorCode.ValueType  # 0
    SYSTEM: _ErrorCode.ValueType  # 100
    """HTTP 5xx error code"""

    APPLICATION: _ErrorCode.ValueType  # 200
    """HTTP 4xx error code"""

class ErrorCode(_ErrorCode, metaclass=_ErrorCodeEnumTypeWrapper):
    pass

UNKNOWN: ErrorCode.ValueType  # 0
SYSTEM: ErrorCode.ValueType  # 100
"""HTTP 5xx error code"""

APPLICATION: ErrorCode.ValueType  # 200
"""HTTP 4xx error code"""

global___ErrorCode = ErrorCode


class _Unit:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _UnitEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Unit.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN_UNIT: _Unit.ValueType  # 0
    """Sort by unit size so we can use > and < in code."""

    SECONDS: _Unit.ValueType  # 1
    """k8s cronjobs does not support seconds, but schedule does. Keep just in case"""

    MINUTES: _Unit.ValueType  # 2
    HOURS: _Unit.ValueType  # 3
    DAYS: _Unit.ValueType  # 4
    WEEKS: _Unit.ValueType  # 5
    """python schedule module does not support months/years"""

class Unit(_Unit, metaclass=_UnitEnumTypeWrapper):
    """TODO: the CronJob and timing messages below were copied over from
    the non-open source //models/runtime/cronjob.proto. It might make
    sense to merge these in the future, and, even if unmerged, to move
    these definitions to another file for better organization.
    """
    pass

UNKNOWN_UNIT: Unit.ValueType  # 0
"""Sort by unit size so we can use > and < in code."""

SECONDS: Unit.ValueType  # 1
"""k8s cronjobs does not support seconds, but schedule does. Keep just in case"""

MINUTES: Unit.ValueType  # 2
HOURS: Unit.ValueType  # 3
DAYS: Unit.ValueType  # 4
WEEKS: Unit.ValueType  # 5
"""python schedule module does not support months/years"""

global___Unit = Unit


class _DayOfWeek:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _DayOfWeekEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_DayOfWeek.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN_DAY: _DayOfWeek.ValueType  # 0
    SUNDAY: _DayOfWeek.ValueType  # 1
    """Start on Sunday to match crontab order. We need zero to be default but we don't
    want to default to Sunday. So in code we can do (enumValue - 1) to determine
    crontab value.
    """

    MONDAY: _DayOfWeek.ValueType  # 2
    TUESDAY: _DayOfWeek.ValueType  # 3
    WEDNESDAY: _DayOfWeek.ValueType  # 4
    THURSDAY: _DayOfWeek.ValueType  # 5
    FRIDAY: _DayOfWeek.ValueType  # 6
    SATURDAY: _DayOfWeek.ValueType  # 7
class DayOfWeek(_DayOfWeek, metaclass=_DayOfWeekEnumTypeWrapper):
    pass

UNKNOWN_DAY: DayOfWeek.ValueType  # 0
SUNDAY: DayOfWeek.ValueType  # 1
"""Start on Sunday to match crontab order. We need zero to be default but we don't
want to default to Sunday. So in code we can do (enumValue - 1) to determine
crontab value.
"""

MONDAY: DayOfWeek.ValueType  # 2
TUESDAY: DayOfWeek.ValueType  # 3
WEDNESDAY: DayOfWeek.ValueType  # 4
THURSDAY: DayOfWeek.ValueType  # 5
FRIDAY: DayOfWeek.ValueType  # 6
SATURDAY: DayOfWeek.ValueType  # 7
global___DayOfWeek = DayOfWeek


class RemoteCallRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    QUALIFIED_SYMBOL_FIELD_NUMBER: builtins.int
    JSON_ARGS_FIELD_NUMBER: builtins.int
    qualified_symbol: typing.Text
    json_args: typing.Text
    """TODO: encode as protobuf instead"""

    def __init__(self,
        *,
        qualified_symbol: typing.Text = ...,
        json_args: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["json_args",b"json_args","qualified_symbol",b"qualified_symbol"]) -> None: ...
global___RemoteCallRequest = RemoteCallRequest

class RemoteCallResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    JSON_RESULTS_FIELD_NUMBER: builtins.int
    json_results: typing.Text
    """TODO: encode as protobuf instead"""

    def __init__(self,
        *,
        json_results: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["json_results",b"json_results"]) -> None: ...
global___RemoteCallResponse = RemoteCallResponse

class CreateTaskRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TASK_FIELD_NUMBER: builtins.int
    SDK_VERSION_FIELD_NUMBER: builtins.int
    @property
    def task(self) -> global___Task: ...
    sdk_version: typing.Text
    def __init__(self,
        *,
        task: typing.Optional[global___Task] = ...,
        sdk_version: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["task",b"task"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["sdk_version",b"sdk_version","task",b"task"]) -> None: ...
global___CreateTaskRequest = CreateTaskRequest

class CreateTaskResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TASK_ID_FIELD_NUMBER: builtins.int
    task_id: typing.Text
    def __init__(self,
        *,
        task_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["task_id",b"task_id"]) -> None: ...
global___CreateTaskResponse = CreateTaskResponse

class CancelTaskRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TASK_ID_FIELD_NUMBER: builtins.int
    task_id: typing.Text
    def __init__(self,
        *,
        task_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["task_id",b"task_id"]) -> None: ...
global___CancelTaskRequest = CancelTaskRequest

class CancelTaskResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SUCCESS_FIELD_NUMBER: builtins.int
    success: builtins.bool
    def __init__(self,
        *,
        success: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["success",b"success"]) -> None: ...
global___CancelTaskResponse = CancelTaskResponse

class PostResultRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    EXEC_ID_FIELD_NUMBER: builtins.int
    RESULT_FIELD_NUMBER: builtins.int
    exec_id: typing.Text
    """An id that identifies an instance of a Task execution."""

    @property
    def result(self) -> global___Result: ...
    def __init__(self,
        *,
        exec_id: typing.Text = ...,
        result: typing.Optional[global___Result] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["result",b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["exec_id",b"exec_id","result",b"result"]) -> None: ...
global___PostResultRequest = PostResultRequest

class PostResultResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___PostResultResponse = PostResultResponse

class Task(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAMESPACE_FIELD_NUMBER: builtins.int
    HOSTNAME_FIELD_NUMBER: builtins.int
    APP_NAME_FIELD_NUMBER: builtins.int
    PROJECT_ID_FIELD_NUMBER: builtins.int
    CHART_REVISION_FIELD_NUMBER: builtins.int
    QUALIFIED_SYMBOL_FIELD_NUMBER: builtins.int
    ENCODED_ARGS_FIELD_NUMBER: builtins.int
    PARENT_TASK_ID_FIELD_NUMBER: builtins.int
    TARGET_TIME_FIELD_NUMBER: builtins.int
    WITH_CHECKPOINTING_FIELD_NUMBER: builtins.int
    TASK_ID_FIELD_NUMBER: builtins.int
    namespace: typing.Text
    """unused for now, but keeping for when we have cross-namespace calls"""

    hostname: typing.Text
    """The hostname of the pod that will be used as a "base" for this
    task. The base pod's environment/image will be used to run the task.
    """

    app_name: typing.Text
    project_id: typing.Text
    chart_revision: typing.Text
    qualified_symbol: typing.Text
    encoded_args: builtins.bytes
    parent_task_id: typing.Text
    @property
    def target_time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    with_checkpointing: builtins.bool
    task_id: typing.Text
    """TODO: this is a clutch, only used server-side for now. Remove after
    we a separate Task definition for the server-side.
    """

    def __init__(self,
        *,
        namespace: typing.Text = ...,
        hostname: typing.Text = ...,
        app_name: typing.Text = ...,
        project_id: typing.Text = ...,
        chart_revision: typing.Text = ...,
        qualified_symbol: typing.Text = ...,
        encoded_args: builtins.bytes = ...,
        parent_task_id: typing.Text = ...,
        target_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        with_checkpointing: builtins.bool = ...,
        task_id: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["target_time",b"target_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["app_name",b"app_name","chart_revision",b"chart_revision","encoded_args",b"encoded_args","hostname",b"hostname","namespace",b"namespace","parent_task_id",b"parent_task_id","project_id",b"project_id","qualified_symbol",b"qualified_symbol","target_time",b"target_time","task_id",b"task_id","with_checkpointing",b"with_checkpointing"]) -> None: ...
global___Task = Task

class Result(google.protobuf.message.Message):
    """Result should always have either `value` OR `error` set, and both should
    not be set.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALUE_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    @property
    def value(self) -> global___Value: ...
    @property
    def error(self) -> global___Error: ...
    def __init__(self,
        *,
        value: typing.Optional[global___Value] = ...,
        error: typing.Optional[global___Error] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error",b"error","value",b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error",b"error","value",b"value"]) -> None: ...
global___Result = Result

class Error(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CODE_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    ENCODED_ERROR_FIELD_NUMBER: builtins.int
    code: global___ErrorCode.ValueType
    message: typing.Text
    """Human readable error message."""

    encoded_error: builtins.bytes
    """For now, we use a generic bytes type. This lets us use jsonpickle
    for python-to-python service calls, specifically an Error object
    returned from an python-application running via jetpack.

    Long term:
    We'll likely want this to be `repeated google.protobuf.Any` type.
    This will let us encode specific details for different error codes
    that correspond to specific protobuf-message kinds, and stack traces.
    However, we'd need to implement a python type to protobuf converter
    ("protopickle") and so we can punt on that for now.

    Consider using pkg cockroachdb/errors in runtime and storing that error's
    protobuf message here.
    """

    def __init__(self,
        *,
        code: global___ErrorCode.ValueType = ...,
        message: typing.Text = ...,
        encoded_error: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["code",b"code","encoded_error",b"encoded_error","message",b"message"]) -> None: ...
global___Error = Error

class Value(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENCODED_VALUE_FIELD_NUMBER: builtins.int
    encoded_value: builtins.bytes
    """This should contain the json-pickled value being returned"""

    def __init__(self,
        *,
        encoded_value: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["encoded_value",b"encoded_value"]) -> None: ...
global___Value = Value

class RegisterAppRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class EndpointsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        value: typing.Text
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    NAMESPACE_FIELD_NUMBER: builtins.int
    HOSTNAME_FIELD_NUMBER: builtins.int
    CRON_JOBS_FIELD_NUMBER: builtins.int
    QUALIFIED_SYMBOLS_FIELD_NUMBER: builtins.int
    ENDPOINTS_FIELD_NUMBER: builtins.int
    namespace: typing.Text
    """Namespace and hostname (pod name) of the app. Used to locate the
    app pod and copy over its spec into the k8s cron jobs.
    """

    hostname: typing.Text
    @property
    def cron_jobs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CronJob]: ...
    @property
    def qualified_symbols(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def endpoints(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    def __init__(self,
        *,
        namespace: typing.Text = ...,
        hostname: typing.Text = ...,
        cron_jobs: typing.Optional[typing.Iterable[global___CronJob]] = ...,
        qualified_symbols: typing.Optional[typing.Iterable[typing.Text]] = ...,
        endpoints: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cron_jobs",b"cron_jobs","endpoints",b"endpoints","hostname",b"hostname","namespace",b"namespace","qualified_symbols",b"qualified_symbols"]) -> None: ...
global___RegisterAppRequest = RegisterAppRequest

class RegisterAppResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___RegisterAppResponse = RegisterAppResponse

class DeregisterAppRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAMESPACE_FIELD_NUMBER: builtins.int
    PROJECT_ID_FIELD_NUMBER: builtins.int
    namespace: typing.Text
    project_id: typing.Text
    def __init__(self,
        *,
        namespace: typing.Text = ...,
        project_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["namespace",b"namespace","project_id",b"project_id"]) -> None: ...
global___DeregisterAppRequest = DeregisterAppRequest

class DeregisterAppResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___DeregisterAppResponse = DeregisterAppResponse

class WaitForResultRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TASK_ID_FIELD_NUMBER: builtins.int
    task_id: typing.Text
    def __init__(self,
        *,
        task_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["task_id",b"task_id"]) -> None: ...
global___WaitForResultRequest = WaitForResultRequest

class WaitForResultResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> global___Result: ...
    def __init__(self,
        *,
        result: typing.Optional[global___Result] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["result",b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["result",b"result"]) -> None: ...
global___WaitForResultResponse = WaitForResultResponse

class GetSymbolFromEndpointRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENDPOINT_FIELD_NUMBER: builtins.int
    endpoint: typing.Text
    def __init__(self,
        *,
        endpoint: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["endpoint",b"endpoint"]) -> None: ...
global___GetSymbolFromEndpointRequest = GetSymbolFromEndpointRequest

class GetSymbolFromEndpointResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SYMBOL_FIELD_NUMBER: builtins.int
    symbol: typing.Text
    def __init__(self,
        *,
        symbol: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["symbol",b"symbol"]) -> None: ...
global___GetSymbolFromEndpointResponse = GetSymbolFromEndpointResponse

class CronJob(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    QUALIFIED_SYMBOL_FIELD_NUMBER: builtins.int
    TARGET_TIME_FIELD_NUMBER: builtins.int
    TARGET_DAY_OF_WEEK_FIELD_NUMBER: builtins.int
    UNIT_FIELD_NUMBER: builtins.int
    INTERVAL_FIELD_NUMBER: builtins.int
    SCHEDULE_RULE_FIELD_NUMBER: builtins.int
    qualified_symbol: typing.Text
    """Fully-qualified name of the function to run. Cannot be empty."""

    target_time: typing.Text
    """Timing information

    Target time, e.g. 10:22:00 - k8s cronjobs does not support seconds
    Schedule uses a datetime.time without any timezone. So we should default
    to UTC and maybe in the future modify schedule to include timezone.
    We convert it by using datetime.time.isoformat()
    """

    target_day_of_week: global___DayOfWeek.ValueType
    unit: global___Unit.ValueType
    interval: builtins.int
    """e.g. 10 [unit = minutes] means every 10 minutes"""

    schedule_rule: typing.Text
    """Standard crontab like syntax (* * * * *) supported by Kubernetes
    Once the python SDK supports this, we should deprecate
    the other schedule fields
    """

    def __init__(self,
        *,
        qualified_symbol: typing.Text = ...,
        target_time: typing.Text = ...,
        target_day_of_week: global___DayOfWeek.ValueType = ...,
        unit: global___Unit.ValueType = ...,
        interval: builtins.int = ...,
        schedule_rule: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["interval",b"interval","qualified_symbol",b"qualified_symbol","schedule_rule",b"schedule_rule","target_day_of_week",b"target_day_of_week","target_time",b"target_time","unit",b"unit"]) -> None: ...
global___CronJob = CronJob

class GetTaskRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TASK_ID_FIELD_NUMBER: builtins.int
    task_id: typing.Text
    def __init__(self,
        *,
        task_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["task_id",b"task_id"]) -> None: ...
global___GetTaskRequest = GetTaskRequest

class GetTaskResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    ENCODED_ARGS_FIELD_NUMBER: builtins.int
    id: typing.Text
    encoded_args: builtins.bytes
    def __init__(self,
        *,
        id: typing.Text = ...,
        encoded_args: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["encoded_args",b"encoded_args","id",b"id"]) -> None: ...
global___GetTaskResponse = GetTaskResponse
