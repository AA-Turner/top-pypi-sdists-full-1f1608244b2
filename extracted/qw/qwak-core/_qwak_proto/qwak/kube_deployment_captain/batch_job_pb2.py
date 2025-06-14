# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qwak/kube_deployment_captain/batch_job.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,qwak/kube_deployment_captain/batch_job.proto\x12\x1cqwak.kube.deployment.captain\"\xd2\x03\n\x1cListInferenceJobFilesRequest\x12\x0e\n\x06\x62ucket\x18\x01 \x01(\t\x12\x16\n\x0e\x64irectory_path\x18\x02 \x01(\t\x12\x18\n\x0ctoken_secret\x18\x03 \x01(\tB\x02\x18\x01\x12\x19\n\rsecret_secret\x18\x04 \x01(\tB\x02\x18\x01\x12\x1a\n\x12secret_service_url\x18\x05 \x01(\t\x12\x14\n\x08role_arn\x18\x06 \x01(\tB\x02\x18\x01\x12G\n\x0f\x61ws_credentials\x18\x07 \x01(\x0b\x32,.qwak.kube.deployment.captain.AwsCredentialsH\x00\x12G\n\x0fgcp_credentials\x18\x08 \x01(\x0b\x32,.qwak.kube.deployment.captain.GcpCredentialsH\x00\x12P\n\x14grouped_task_details\x18\t \x01(\x0b\x32\x30.qwak.kube.deployment.captain.GroupedTaskDetailsH\x01\x12\x16\n\x0e\x65nvironment_id\x18\n \x01(\tB\x1a\n\x18\x63loud_client_credentialsB\x0b\n\ttask_flow\"c\n\x12GroupedTaskDetails\x12\x17\n\x0f\x63oncurrentTasks\x18\x01 \x01(\x05\x12\x18\n\x10\x64\x65stination_path\x18\x02 \x01(\t\x12\x1a\n\x12\x64\x65stination_bucket\x18\x03 \x01(\t\"\xb4\x02\n)CleanStorageObjectFromCloudStorageRequest\x12\x0e\n\x06\x62ucket\x18\x01 \x01(\t\x12\x15\n\robject_prefix\x18\x02 \x03(\t\x12\x1a\n\x12secret_service_url\x18\x03 \x01(\t\x12G\n\x0f\x61ws_credentials\x18\x04 \x01(\x0b\x32,.qwak.kube.deployment.captain.AwsCredentialsH\x00\x12G\n\x0fgcp_credentials\x18\x05 \x01(\x0b\x32,.qwak.kube.deployment.captain.GcpCredentialsH\x00\x12\x16\n\x0e\x65nvironment_id\x18\x06 \x01(\tB\x1a\n\x18\x63loud_client_credentials\"O\n\x0e\x41wsCredentials\x12\x10\n\x08role_arn\x18\x01 \x01(\t\x12\x14\n\x0ctoken_secret\x18\x02 \x01(\t\x12\x15\n\rsecret_secret\x18\x04 \x01(\t\"9\n\x0eGcpCredentials\x12\'\n\x1fservice_account_json_key_secret\x18\x01 \x01(\t\"\xa6\x01\n\x1dListInferenceJobFilesResponse\x12\x12\n\nfile_names\x18\x01 \x03(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x16\n\x0e\x66\x61ilure_reason\x18\x03 \x01(\t\x12H\n\x11list_file_details\x18\x04 \x03(\x0b\x32-.qwak.kube.deployment.captain.ListFileDetails\"W\n\x0fListFileDetails\x12\x15\n\ris_point_file\x18\x01 \x01(\x08\x12\x17\n\x0fpoint_file_path\x18\x02 \x01(\t\x12\x14\n\x0cobject_paths\x18\x03 \x03(\t\"\xf0\x01\n\"CreateInferenceTaskExecutorRequest\x12\x63\n\x1btask_executor_configuration\x18\x01 \x01(\x0b\x32>.qwak.kube.deployment.captain.TaskExecutorConfigurationMessage\x12\x65\n\x1cinference_task_configuration\x18\x02 \x01(\x0b\x32?.qwak.kube.deployment.captain.InferenceTaskConfigurationMessage\"\x89\x01\n\x1aPrepareInferenceJobRequest\x12k\n#inference_job_configuration_message\x18\x01 \x01(\x0b\x32>.qwak.kube.deployment.captain.InferenceJobConfigurationMessage\"F\n\x1bPrepareInferenceJobResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x16\n\x0e\x66\x61ilure_reason\x18\x02 \x01(\t\"\xcd\x04\n TaskExecutorConfigurationMessage\x12\x18\n\x10inference_job_id\x18\x01 \x01(\t\x12\x19\n\x11inference_task_id\x18\x02 \x01(\t\x12G\n\x10model_identifier\x18\x05 \x01(\x0b\x32-.qwak.kube.deployment.captain.ModelIdentifier\x12\x11\n\timage_url\x18\x06 \x01(\t\x12\x15\n\rbackoff_limit\x18\x07 \x01(\x05\x12\x0f\n\x03\x63pu\x18\x08 \x01(\x02\x42\x02\x18\x01\x12\x19\n\rmemory_amount\x18\t \x01(\x05\x42\x02\x18\x01\x12\x45\n\x0cmemory_units\x18\n \x01(\x0e\x32+.qwak.kube.deployment.captain.MemoryUnitApiB\x02\x18\x01\x12\x16\n\x0e\x65nvironment_id\x18\x0b \x01(\t\x12\x1b\n\x13\x63ustom_iam_role_arn\x18\x0c \x01(\t\x12\x41\n\x08job_size\x18\r \x01(\x0b\x32/.qwak.kube.deployment.captain.BatchJobResources\x12\x17\n\x0fpurchase_option\x18\x0e \x01(\t\x12\x19\n\x11image_pull_secret\x18\x0f \x01(\t\x12%\n\x1d\x63ustom_service_account_secret\x18\x10 \x01(\t\x12#\n\x1bjfrog_token_api_secret_name\x18\x11 \x01(\t\x12\x16\n\x0ejfrog_base_url\x18\x12 \x01(\t\"q\n InferenceJobConfigurationMessage\x12\x18\n\x10inference_job_id\x18\x01 \x01(\t\x12\x16\n\x0e\x65nvironment_id\x18\x02 \x01(\t\x12\x1b\n\x13\x63ustom_iam_role_arn\x18\x03 \x01(\t\"`\n\x0fModelIdentifier\x12\x10\n\x08model_id\x18\x01 \x01(\t\x12\x10\n\x08\x62uild_id\x18\x02 \x01(\t\x12\x15\n\tbranch_id\x18\x03 \x01(\tB\x02\x18\x01\x12\x12\n\nmodel_uuid\x18\x04 \x01(\t\"\x85\x01\n\x1dListFilesPreStepConfiguration\x12\x13\n\x0bsource_path\x18\x01 \x01(\t\x12\x1c\n\x14list_files_file_name\x18\x02 \x01(\t\x12\x1d\n\x15total_number_of_tasks\x18\x03 \x01(\x05\x12\x12\n\ntask_index\x18\x04 \x01(\x05\"\xf4\x04\n!InferenceTaskConfigurationMessage\x12\x15\n\rsource_bucket\x18\x01 \x01(\t\x12\x1a\n\x12\x64\x65stination_bucket\x18\x02 \x01(\t\x12\x10\n\x08\x66ilepath\x18\x03 \x01(\t\x12\x18\n\x10\x64\x65stination_path\x18\x04 \x01(\t\x12\x44\n\x0finput_file_type\x18\x05 \x01(\x0e\x32+.qwak.kube.deployment.captain.InputFileType\x12\x46\n\x10output_file_type\x18\x06 \x01(\x0e\x32,.qwak.kube.deployment.captain.OutputFileType\x12\x14\n\x0ctoken_secret\x18\x07 \x01(\t\x12\x15\n\rsecret_secret\x18\x08 \x01(\t\x12\x43\n\nparameters\x18\t \x03(\x0b\x32/.qwak.kube.deployment.captain.BatchJobParameter\x12\x43\n\x0e\x63loud_provider\x18\n \x01(\x0e\x32+.qwak.kube.deployment.captain.CloudProvider\x12\'\n\x1fservice_account_json_key_secret\x18\x0b \x01(\t\x12\x1a\n\x12is_point_file_path\x18\x0c \x01(\x08\x12\x66\n!list_files_pre_step_configuration\x18\r \x01(\x0b\x32;.qwak.kube.deployment.captain.ListFilesPreStepConfiguration\"/\n\x11\x42\x61tchJobParameter\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"?\n#CleanInferenceTasksExecutorsRequest\x12\x18\n\x10inference_job_id\x18\x01 \x01(\t\"O\n$CleanInferenceTasksExecutorsResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x16\n\x0e\x66\x61ilure_reason\x18\x02 \x01(\t\"X\n!CleanInferenceTaskExecutorRequest\x12\x18\n\x10inference_job_id\x18\x01 \x01(\t\x12\x19\n\x11inference_task_id\x18\x02 \x01(\t\"M\n\"CleanInferenceTaskExecutorResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x16\n\x0e\x66\x61ilure_reason\x18\x02 \x01(\t\"N\n#CreateInferenceTaskExecutorResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x16\n\x0e\x66\x61ilure_reason\x18\x02 \x01(\t\"\xf7\x02\n\x1eStartInferenceJobWarmupRequest\x12\x10\n\x08model_id\x18\x01 \x01(\t\x12\x15\n\tbranch_id\x18\x02 \x01(\tB\x02\x18\x01\x12\x10\n\x08\x62uild_id\x18\x03 \x01(\t\x12\x11\n\timage_url\x18\x04 \x01(\t\x12\x0f\n\x03\x63pu\x18\x05 \x01(\x02\x42\x02\x18\x01\x12\x19\n\rmemory_amount\x18\x06 \x01(\x05\x42\x02\x18\x01\x12\x45\n\x0cmemory_units\x18\x07 \x01(\x0e\x32+.qwak.kube.deployment.captain.MemoryUnitApiB\x02\x18\x01\x12\x11\n\texecutors\x18\x08 \x01(\x05\x12\x0f\n\x07timeout\x18\t \x01(\x05\x12\x41\n\x08job_size\x18\n \x01(\x0b\x32/.qwak.kube.deployment.captain.BatchJobResources\x12\x12\n\nmodel_uuid\x18\x0b \x01(\t\x12\x19\n\x11image_pull_secret\x18\x0c \x01(\t\"!\n\x1fStartInferenceJobWarmupResponse\"p\n\x1f\x43\x61ncelInferenceJobWarmupRequest\x12\x10\n\x08model_id\x18\x01 \x01(\t\x12\x15\n\tbranch_id\x18\x02 \x01(\tB\x02\x18\x01\x12\x10\n\x08\x62uild_id\x18\x03 \x01(\t\x12\x12\n\nmodel_uuid\x18\x04 \x01(\t\"\"\n CancelInferenceJobWarmupResponse\"\xd5\x01\n\x11\x42\x61tchJobResources\x12\x16\n\x0enumber_of_pods\x18\x01 \x01(\x05\x12\x0b\n\x03\x63pu\x18\x02 \x01(\x02\x12\x15\n\rmemory_amount\x18\x03 \x01(\x05\x12\x41\n\x0cmemory_units\x18\x04 \x01(\x0e\x32+.qwak.kube.deployment.captain.MemoryUnitApi\x12\x41\n\rgpu_resources\x18\x05 \x01(\x0b\x32*.qwak.kube.deployment.captain.GpuResources\"[\n\x0cGpuResources\x12\x37\n\x08gpu_type\x18\x01 \x01(\x0e\x32%.qwak.kube.deployment.captain.GpuType\x12\x12\n\ngpu_amount\x18\x02 \x01(\x05*:\n\rMemoryUnitApi\x12\x17\n\x13UNKNOWN_MEMORY_UNIT\x10\x00\x12\x07\n\x03MIB\x10\x01\x12\x07\n\x03GIB\x10\x02*\x81\x01\n\rInputFileType\x12\x1d\n\x19UNDEFINED_INPUT_FILE_TYPE\x10\x00\x12\x17\n\x13\x43SV_INPUT_FILE_TYPE\x10\x01\x12\x1b\n\x17\x46\x45\x41THER_INPUT_FILE_TYPE\x10\x02\x12\x1b\n\x17PARQUET_INPUT_FILE_TYPE\x10\x03*\x86\x01\n\x0eOutputFileType\x12\x1e\n\x1aUNDEFINED_OUTPUT_FILE_TYPE\x10\x00\x12\x18\n\x14\x43SV_OUTPUT_FILE_TYPE\x10\x01\x12\x1c\n\x18\x46\x45\x41THER_OUTPUT_FILE_TYPE\x10\x02\x12\x1c\n\x18PARQUET_OUTPUT_FILE_TYPE\x10\x03*\x90\x02\n\x07GpuType\x12\x0f\n\x0bINVALID_GPU\x10\x00\x12\x0e\n\nNVIDIA_K80\x10\x01\x12\x0f\n\x0bNVIDIA_V100\x10\x02\x12\x0f\n\x0bNVIDIA_A100\x10\x03\x12\r\n\tNVIDIA_T4\x10\x04\x12\x0f\n\x0bNVIDIA_A10G\x10\x05\x12\r\n\tNVIDIA_L4\x10\x06\x12\x14\n\x10NVIDIA_T4_1_4_15\x10\x07\x12\x14\n\x10NVIDIA_T4_1_8_30\x10\x08\x12\x15\n\x11NVIDIA_T4_1_16_60\x10\t\x12\x1e\n\x1aNVIDIA_A100_80GB_8_96_1360\x10\n\x12\x16\n\x12NVIDIA_V100_1_8_52\x10\x0b\x12\x18\n\x14NVIDIA_V100_4_32_208\x10\x0c*=\n\rCloudProvider\x12\x1a\n\x16UNKNOWN_CLOUD_PROVIDER\x10\x00\x12\x07\n\x03\x41WS\x10\x01\x12\x07\n\x03GCP\x10\x02\x42+\n\'com.qwak.ai.kube.deployment.captain.apiP\x01\x62\x06proto3')

_MEMORYUNITAPI = DESCRIPTOR.enum_types_by_name['MemoryUnitApi']
MemoryUnitApi = enum_type_wrapper.EnumTypeWrapper(_MEMORYUNITAPI)
_INPUTFILETYPE = DESCRIPTOR.enum_types_by_name['InputFileType']
InputFileType = enum_type_wrapper.EnumTypeWrapper(_INPUTFILETYPE)
_OUTPUTFILETYPE = DESCRIPTOR.enum_types_by_name['OutputFileType']
OutputFileType = enum_type_wrapper.EnumTypeWrapper(_OUTPUTFILETYPE)
_GPUTYPE = DESCRIPTOR.enum_types_by_name['GpuType']
GpuType = enum_type_wrapper.EnumTypeWrapper(_GPUTYPE)
_CLOUDPROVIDER = DESCRIPTOR.enum_types_by_name['CloudProvider']
CloudProvider = enum_type_wrapper.EnumTypeWrapper(_CLOUDPROVIDER)
UNKNOWN_MEMORY_UNIT = 0
MIB = 1
GIB = 2
UNDEFINED_INPUT_FILE_TYPE = 0
CSV_INPUT_FILE_TYPE = 1
FEATHER_INPUT_FILE_TYPE = 2
PARQUET_INPUT_FILE_TYPE = 3
UNDEFINED_OUTPUT_FILE_TYPE = 0
CSV_OUTPUT_FILE_TYPE = 1
FEATHER_OUTPUT_FILE_TYPE = 2
PARQUET_OUTPUT_FILE_TYPE = 3
INVALID_GPU = 0
NVIDIA_K80 = 1
NVIDIA_V100 = 2
NVIDIA_A100 = 3
NVIDIA_T4 = 4
NVIDIA_A10G = 5
NVIDIA_L4 = 6
NVIDIA_T4_1_4_15 = 7
NVIDIA_T4_1_8_30 = 8
NVIDIA_T4_1_16_60 = 9
NVIDIA_A100_80GB_8_96_1360 = 10
NVIDIA_V100_1_8_52 = 11
NVIDIA_V100_4_32_208 = 12
UNKNOWN_CLOUD_PROVIDER = 0
AWS = 1
GCP = 2


_LISTINFERENCEJOBFILESREQUEST = DESCRIPTOR.message_types_by_name['ListInferenceJobFilesRequest']
_GROUPEDTASKDETAILS = DESCRIPTOR.message_types_by_name['GroupedTaskDetails']
_CLEANSTORAGEOBJECTFROMCLOUDSTORAGEREQUEST = DESCRIPTOR.message_types_by_name['CleanStorageObjectFromCloudStorageRequest']
_AWSCREDENTIALS = DESCRIPTOR.message_types_by_name['AwsCredentials']
_GCPCREDENTIALS = DESCRIPTOR.message_types_by_name['GcpCredentials']
_LISTINFERENCEJOBFILESRESPONSE = DESCRIPTOR.message_types_by_name['ListInferenceJobFilesResponse']
_LISTFILEDETAILS = DESCRIPTOR.message_types_by_name['ListFileDetails']
_CREATEINFERENCETASKEXECUTORREQUEST = DESCRIPTOR.message_types_by_name['CreateInferenceTaskExecutorRequest']
_PREPAREINFERENCEJOBREQUEST = DESCRIPTOR.message_types_by_name['PrepareInferenceJobRequest']
_PREPAREINFERENCEJOBRESPONSE = DESCRIPTOR.message_types_by_name['PrepareInferenceJobResponse']
_TASKEXECUTORCONFIGURATIONMESSAGE = DESCRIPTOR.message_types_by_name['TaskExecutorConfigurationMessage']
_INFERENCEJOBCONFIGURATIONMESSAGE = DESCRIPTOR.message_types_by_name['InferenceJobConfigurationMessage']
_MODELIDENTIFIER = DESCRIPTOR.message_types_by_name['ModelIdentifier']
_LISTFILESPRESTEPCONFIGURATION = DESCRIPTOR.message_types_by_name['ListFilesPreStepConfiguration']
_INFERENCETASKCONFIGURATIONMESSAGE = DESCRIPTOR.message_types_by_name['InferenceTaskConfigurationMessage']
_BATCHJOBPARAMETER = DESCRIPTOR.message_types_by_name['BatchJobParameter']
_CLEANINFERENCETASKSEXECUTORSREQUEST = DESCRIPTOR.message_types_by_name['CleanInferenceTasksExecutorsRequest']
_CLEANINFERENCETASKSEXECUTORSRESPONSE = DESCRIPTOR.message_types_by_name['CleanInferenceTasksExecutorsResponse']
_CLEANINFERENCETASKEXECUTORREQUEST = DESCRIPTOR.message_types_by_name['CleanInferenceTaskExecutorRequest']
_CLEANINFERENCETASKEXECUTORRESPONSE = DESCRIPTOR.message_types_by_name['CleanInferenceTaskExecutorResponse']
_CREATEINFERENCETASKEXECUTORRESPONSE = DESCRIPTOR.message_types_by_name['CreateInferenceTaskExecutorResponse']
_STARTINFERENCEJOBWARMUPREQUEST = DESCRIPTOR.message_types_by_name['StartInferenceJobWarmupRequest']
_STARTINFERENCEJOBWARMUPRESPONSE = DESCRIPTOR.message_types_by_name['StartInferenceJobWarmupResponse']
_CANCELINFERENCEJOBWARMUPREQUEST = DESCRIPTOR.message_types_by_name['CancelInferenceJobWarmupRequest']
_CANCELINFERENCEJOBWARMUPRESPONSE = DESCRIPTOR.message_types_by_name['CancelInferenceJobWarmupResponse']
_BATCHJOBRESOURCES = DESCRIPTOR.message_types_by_name['BatchJobResources']
_GPURESOURCES = DESCRIPTOR.message_types_by_name['GpuResources']
ListInferenceJobFilesRequest = _reflection.GeneratedProtocolMessageType('ListInferenceJobFilesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTINFERENCEJOBFILESREQUEST,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.ListInferenceJobFilesRequest)
  })
_sym_db.RegisterMessage(ListInferenceJobFilesRequest)

GroupedTaskDetails = _reflection.GeneratedProtocolMessageType('GroupedTaskDetails', (_message.Message,), {
  'DESCRIPTOR' : _GROUPEDTASKDETAILS,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.GroupedTaskDetails)
  })
_sym_db.RegisterMessage(GroupedTaskDetails)

CleanStorageObjectFromCloudStorageRequest = _reflection.GeneratedProtocolMessageType('CleanStorageObjectFromCloudStorageRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLEANSTORAGEOBJECTFROMCLOUDSTORAGEREQUEST,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.CleanStorageObjectFromCloudStorageRequest)
  })
_sym_db.RegisterMessage(CleanStorageObjectFromCloudStorageRequest)

AwsCredentials = _reflection.GeneratedProtocolMessageType('AwsCredentials', (_message.Message,), {
  'DESCRIPTOR' : _AWSCREDENTIALS,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.AwsCredentials)
  })
_sym_db.RegisterMessage(AwsCredentials)

GcpCredentials = _reflection.GeneratedProtocolMessageType('GcpCredentials', (_message.Message,), {
  'DESCRIPTOR' : _GCPCREDENTIALS,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.GcpCredentials)
  })
_sym_db.RegisterMessage(GcpCredentials)

ListInferenceJobFilesResponse = _reflection.GeneratedProtocolMessageType('ListInferenceJobFilesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTINFERENCEJOBFILESRESPONSE,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.ListInferenceJobFilesResponse)
  })
_sym_db.RegisterMessage(ListInferenceJobFilesResponse)

ListFileDetails = _reflection.GeneratedProtocolMessageType('ListFileDetails', (_message.Message,), {
  'DESCRIPTOR' : _LISTFILEDETAILS,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.ListFileDetails)
  })
_sym_db.RegisterMessage(ListFileDetails)

CreateInferenceTaskExecutorRequest = _reflection.GeneratedProtocolMessageType('CreateInferenceTaskExecutorRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEINFERENCETASKEXECUTORREQUEST,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.CreateInferenceTaskExecutorRequest)
  })
_sym_db.RegisterMessage(CreateInferenceTaskExecutorRequest)

PrepareInferenceJobRequest = _reflection.GeneratedProtocolMessageType('PrepareInferenceJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _PREPAREINFERENCEJOBREQUEST,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.PrepareInferenceJobRequest)
  })
_sym_db.RegisterMessage(PrepareInferenceJobRequest)

PrepareInferenceJobResponse = _reflection.GeneratedProtocolMessageType('PrepareInferenceJobResponse', (_message.Message,), {
  'DESCRIPTOR' : _PREPAREINFERENCEJOBRESPONSE,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.PrepareInferenceJobResponse)
  })
_sym_db.RegisterMessage(PrepareInferenceJobResponse)

TaskExecutorConfigurationMessage = _reflection.GeneratedProtocolMessageType('TaskExecutorConfigurationMessage', (_message.Message,), {
  'DESCRIPTOR' : _TASKEXECUTORCONFIGURATIONMESSAGE,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.TaskExecutorConfigurationMessage)
  })
_sym_db.RegisterMessage(TaskExecutorConfigurationMessage)

InferenceJobConfigurationMessage = _reflection.GeneratedProtocolMessageType('InferenceJobConfigurationMessage', (_message.Message,), {
  'DESCRIPTOR' : _INFERENCEJOBCONFIGURATIONMESSAGE,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.InferenceJobConfigurationMessage)
  })
_sym_db.RegisterMessage(InferenceJobConfigurationMessage)

ModelIdentifier = _reflection.GeneratedProtocolMessageType('ModelIdentifier', (_message.Message,), {
  'DESCRIPTOR' : _MODELIDENTIFIER,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.ModelIdentifier)
  })
_sym_db.RegisterMessage(ModelIdentifier)

ListFilesPreStepConfiguration = _reflection.GeneratedProtocolMessageType('ListFilesPreStepConfiguration', (_message.Message,), {
  'DESCRIPTOR' : _LISTFILESPRESTEPCONFIGURATION,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.ListFilesPreStepConfiguration)
  })
_sym_db.RegisterMessage(ListFilesPreStepConfiguration)

InferenceTaskConfigurationMessage = _reflection.GeneratedProtocolMessageType('InferenceTaskConfigurationMessage', (_message.Message,), {
  'DESCRIPTOR' : _INFERENCETASKCONFIGURATIONMESSAGE,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.InferenceTaskConfigurationMessage)
  })
_sym_db.RegisterMessage(InferenceTaskConfigurationMessage)

BatchJobParameter = _reflection.GeneratedProtocolMessageType('BatchJobParameter', (_message.Message,), {
  'DESCRIPTOR' : _BATCHJOBPARAMETER,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.BatchJobParameter)
  })
_sym_db.RegisterMessage(BatchJobParameter)

CleanInferenceTasksExecutorsRequest = _reflection.GeneratedProtocolMessageType('CleanInferenceTasksExecutorsRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLEANINFERENCETASKSEXECUTORSREQUEST,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.CleanInferenceTasksExecutorsRequest)
  })
_sym_db.RegisterMessage(CleanInferenceTasksExecutorsRequest)

CleanInferenceTasksExecutorsResponse = _reflection.GeneratedProtocolMessageType('CleanInferenceTasksExecutorsResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLEANINFERENCETASKSEXECUTORSRESPONSE,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.CleanInferenceTasksExecutorsResponse)
  })
_sym_db.RegisterMessage(CleanInferenceTasksExecutorsResponse)

CleanInferenceTaskExecutorRequest = _reflection.GeneratedProtocolMessageType('CleanInferenceTaskExecutorRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLEANINFERENCETASKEXECUTORREQUEST,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.CleanInferenceTaskExecutorRequest)
  })
_sym_db.RegisterMessage(CleanInferenceTaskExecutorRequest)

CleanInferenceTaskExecutorResponse = _reflection.GeneratedProtocolMessageType('CleanInferenceTaskExecutorResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLEANINFERENCETASKEXECUTORRESPONSE,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.CleanInferenceTaskExecutorResponse)
  })
_sym_db.RegisterMessage(CleanInferenceTaskExecutorResponse)

CreateInferenceTaskExecutorResponse = _reflection.GeneratedProtocolMessageType('CreateInferenceTaskExecutorResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEINFERENCETASKEXECUTORRESPONSE,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.CreateInferenceTaskExecutorResponse)
  })
_sym_db.RegisterMessage(CreateInferenceTaskExecutorResponse)

StartInferenceJobWarmupRequest = _reflection.GeneratedProtocolMessageType('StartInferenceJobWarmupRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTINFERENCEJOBWARMUPREQUEST,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.StartInferenceJobWarmupRequest)
  })
_sym_db.RegisterMessage(StartInferenceJobWarmupRequest)

StartInferenceJobWarmupResponse = _reflection.GeneratedProtocolMessageType('StartInferenceJobWarmupResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTINFERENCEJOBWARMUPRESPONSE,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.StartInferenceJobWarmupResponse)
  })
_sym_db.RegisterMessage(StartInferenceJobWarmupResponse)

CancelInferenceJobWarmupRequest = _reflection.GeneratedProtocolMessageType('CancelInferenceJobWarmupRequest', (_message.Message,), {
  'DESCRIPTOR' : _CANCELINFERENCEJOBWARMUPREQUEST,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.CancelInferenceJobWarmupRequest)
  })
_sym_db.RegisterMessage(CancelInferenceJobWarmupRequest)

CancelInferenceJobWarmupResponse = _reflection.GeneratedProtocolMessageType('CancelInferenceJobWarmupResponse', (_message.Message,), {
  'DESCRIPTOR' : _CANCELINFERENCEJOBWARMUPRESPONSE,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.CancelInferenceJobWarmupResponse)
  })
_sym_db.RegisterMessage(CancelInferenceJobWarmupResponse)

BatchJobResources = _reflection.GeneratedProtocolMessageType('BatchJobResources', (_message.Message,), {
  'DESCRIPTOR' : _BATCHJOBRESOURCES,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.BatchJobResources)
  })
_sym_db.RegisterMessage(BatchJobResources)

GpuResources = _reflection.GeneratedProtocolMessageType('GpuResources', (_message.Message,), {
  'DESCRIPTOR' : _GPURESOURCES,
  '__module__' : 'qwak.kube_deployment_captain.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:qwak.kube.deployment.captain.GpuResources)
  })
_sym_db.RegisterMessage(GpuResources)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\'com.qwak.ai.kube.deployment.captain.apiP\001'
  _LISTINFERENCEJOBFILESREQUEST.fields_by_name['token_secret']._options = None
  _LISTINFERENCEJOBFILESREQUEST.fields_by_name['token_secret']._serialized_options = b'\030\001'
  _LISTINFERENCEJOBFILESREQUEST.fields_by_name['secret_secret']._options = None
  _LISTINFERENCEJOBFILESREQUEST.fields_by_name['secret_secret']._serialized_options = b'\030\001'
  _LISTINFERENCEJOBFILESREQUEST.fields_by_name['role_arn']._options = None
  _LISTINFERENCEJOBFILESREQUEST.fields_by_name['role_arn']._serialized_options = b'\030\001'
  _TASKEXECUTORCONFIGURATIONMESSAGE.fields_by_name['cpu']._options = None
  _TASKEXECUTORCONFIGURATIONMESSAGE.fields_by_name['cpu']._serialized_options = b'\030\001'
  _TASKEXECUTORCONFIGURATIONMESSAGE.fields_by_name['memory_amount']._options = None
  _TASKEXECUTORCONFIGURATIONMESSAGE.fields_by_name['memory_amount']._serialized_options = b'\030\001'
  _TASKEXECUTORCONFIGURATIONMESSAGE.fields_by_name['memory_units']._options = None
  _TASKEXECUTORCONFIGURATIONMESSAGE.fields_by_name['memory_units']._serialized_options = b'\030\001'
  _MODELIDENTIFIER.fields_by_name['branch_id']._options = None
  _MODELIDENTIFIER.fields_by_name['branch_id']._serialized_options = b'\030\001'
  _STARTINFERENCEJOBWARMUPREQUEST.fields_by_name['branch_id']._options = None
  _STARTINFERENCEJOBWARMUPREQUEST.fields_by_name['branch_id']._serialized_options = b'\030\001'
  _STARTINFERENCEJOBWARMUPREQUEST.fields_by_name['cpu']._options = None
  _STARTINFERENCEJOBWARMUPREQUEST.fields_by_name['cpu']._serialized_options = b'\030\001'
  _STARTINFERENCEJOBWARMUPREQUEST.fields_by_name['memory_amount']._options = None
  _STARTINFERENCEJOBWARMUPREQUEST.fields_by_name['memory_amount']._serialized_options = b'\030\001'
  _STARTINFERENCEJOBWARMUPREQUEST.fields_by_name['memory_units']._options = None
  _STARTINFERENCEJOBWARMUPREQUEST.fields_by_name['memory_units']._serialized_options = b'\030\001'
  _CANCELINFERENCEJOBWARMUPREQUEST.fields_by_name['branch_id']._options = None
  _CANCELINFERENCEJOBWARMUPREQUEST.fields_by_name['branch_id']._serialized_options = b'\030\001'
  _MEMORYUNITAPI._serialized_start=4700
  _MEMORYUNITAPI._serialized_end=4758
  _INPUTFILETYPE._serialized_start=4761
  _INPUTFILETYPE._serialized_end=4890
  _OUTPUTFILETYPE._serialized_start=4893
  _OUTPUTFILETYPE._serialized_end=5027
  _GPUTYPE._serialized_start=5030
  _GPUTYPE._serialized_end=5302
  _CLOUDPROVIDER._serialized_start=5304
  _CLOUDPROVIDER._serialized_end=5365
  _LISTINFERENCEJOBFILESREQUEST._serialized_start=79
  _LISTINFERENCEJOBFILESREQUEST._serialized_end=545
  _GROUPEDTASKDETAILS._serialized_start=547
  _GROUPEDTASKDETAILS._serialized_end=646
  _CLEANSTORAGEOBJECTFROMCLOUDSTORAGEREQUEST._serialized_start=649
  _CLEANSTORAGEOBJECTFROMCLOUDSTORAGEREQUEST._serialized_end=957
  _AWSCREDENTIALS._serialized_start=959
  _AWSCREDENTIALS._serialized_end=1038
  _GCPCREDENTIALS._serialized_start=1040
  _GCPCREDENTIALS._serialized_end=1097
  _LISTINFERENCEJOBFILESRESPONSE._serialized_start=1100
  _LISTINFERENCEJOBFILESRESPONSE._serialized_end=1266
  _LISTFILEDETAILS._serialized_start=1268
  _LISTFILEDETAILS._serialized_end=1355
  _CREATEINFERENCETASKEXECUTORREQUEST._serialized_start=1358
  _CREATEINFERENCETASKEXECUTORREQUEST._serialized_end=1598
  _PREPAREINFERENCEJOBREQUEST._serialized_start=1601
  _PREPAREINFERENCEJOBREQUEST._serialized_end=1738
  _PREPAREINFERENCEJOBRESPONSE._serialized_start=1740
  _PREPAREINFERENCEJOBRESPONSE._serialized_end=1810
  _TASKEXECUTORCONFIGURATIONMESSAGE._serialized_start=1813
  _TASKEXECUTORCONFIGURATIONMESSAGE._serialized_end=2402
  _INFERENCEJOBCONFIGURATIONMESSAGE._serialized_start=2404
  _INFERENCEJOBCONFIGURATIONMESSAGE._serialized_end=2517
  _MODELIDENTIFIER._serialized_start=2519
  _MODELIDENTIFIER._serialized_end=2615
  _LISTFILESPRESTEPCONFIGURATION._serialized_start=2618
  _LISTFILESPRESTEPCONFIGURATION._serialized_end=2751
  _INFERENCETASKCONFIGURATIONMESSAGE._serialized_start=2754
  _INFERENCETASKCONFIGURATIONMESSAGE._serialized_end=3382
  _BATCHJOBPARAMETER._serialized_start=3384
  _BATCHJOBPARAMETER._serialized_end=3431
  _CLEANINFERENCETASKSEXECUTORSREQUEST._serialized_start=3433
  _CLEANINFERENCETASKSEXECUTORSREQUEST._serialized_end=3496
  _CLEANINFERENCETASKSEXECUTORSRESPONSE._serialized_start=3498
  _CLEANINFERENCETASKSEXECUTORSRESPONSE._serialized_end=3577
  _CLEANINFERENCETASKEXECUTORREQUEST._serialized_start=3579
  _CLEANINFERENCETASKEXECUTORREQUEST._serialized_end=3667
  _CLEANINFERENCETASKEXECUTORRESPONSE._serialized_start=3669
  _CLEANINFERENCETASKEXECUTORRESPONSE._serialized_end=3746
  _CREATEINFERENCETASKEXECUTORRESPONSE._serialized_start=3748
  _CREATEINFERENCETASKEXECUTORRESPONSE._serialized_end=3826
  _STARTINFERENCEJOBWARMUPREQUEST._serialized_start=3829
  _STARTINFERENCEJOBWARMUPREQUEST._serialized_end=4204
  _STARTINFERENCEJOBWARMUPRESPONSE._serialized_start=4206
  _STARTINFERENCEJOBWARMUPRESPONSE._serialized_end=4239
  _CANCELINFERENCEJOBWARMUPREQUEST._serialized_start=4241
  _CANCELINFERENCEJOBWARMUPREQUEST._serialized_end=4353
  _CANCELINFERENCEJOBWARMUPRESPONSE._serialized_start=4355
  _CANCELINFERENCEJOBWARMUPRESPONSE._serialized_end=4389
  _BATCHJOBRESOURCES._serialized_start=4392
  _BATCHJOBRESOURCES._serialized_end=4605
  _GPURESOURCES._serialized_start=4607
  _GPURESOURCES._serialized_end=4698
# @@protoc_insertion_point(module_scope)
