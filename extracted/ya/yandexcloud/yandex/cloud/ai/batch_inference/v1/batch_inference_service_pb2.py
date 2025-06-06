# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/ai/batch_inference/v1/batch_inference_service.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'yandex/cloud/ai/batch_inference/v1/batch_inference_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.ai.batch_inference.v1 import batch_inference_task_pb2 as yandex_dot_cloud_dot_ai_dot_batch__inference_dot_v1_dot_batch__inference__task__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@yandex/cloud/ai/batch_inference/v1/batch_inference_service.proto\x12\"yandex.cloud.ai.batch_inference.v1\x1a\x1dyandex/cloud/validation.proto\x1a=yandex/cloud/ai/batch_inference/v1/batch_inference_task.proto\"\xaf\x01\n\x16\x42\x61tchInferenceMetadata\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12R\n\x0btask_status\x18\x02 \x01(\x0e\x32=.yandex.cloud.ai.batch_inference.v1.BatchInferenceTask.Status\x12\x19\n\x11\x63ompleted_batches\x18\x03 \x01(\x03\x12\x15\n\rtotal_batches\x18\x04 \x01(\x03\"^\n\x16\x42\x61tchInferenceResponse\x12\x44\n\x04task\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.ai.batch_inference.v1.BatchInferenceTask\"6\n\x1d\x44\x65scribeBatchInferenceRequest\x12\x15\n\x07task_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"f\n\x1e\x44\x65scribeBatchInferenceResponse\x12\x44\n\x04task\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.ai.batch_inference.v1.BatchInferenceTask\"\xab\x01\n\x1aListBatchInferencesRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\x12M\n\x06status\x18\x04 \x01(\x0e\x32=.yandex.cloud.ai.batch_inference.v1.BatchInferenceTask.Status\"}\n\x1bListBatchInferencesResponse\x12\x45\n\x05tasks\x18\x01 \x03(\x0b\x32\x36.yandex.cloud.ai.batch_inference.v1.BatchInferenceTask\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"4\n\x1b\x43\x61ncelBatchInferenceRequest\x12\x15\n\x07task_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"/\n\x1c\x43\x61ncelBatchInferenceResponse\x12\x0f\n\x07task_id\x18\x01 \x01(\t\"4\n\x1b\x44\x65leteBatchInferenceRequest\x12\x15\n\x07task_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"/\n\x1c\x44\x65leteBatchInferenceResponse\x12\x0f\n\x07task_id\x18\x01 \x01(\t2\xd1\x04\n\x15\x42\x61tchInferenceService\x12\x91\x01\n\x08\x44\x65scribe\x12\x41.yandex.cloud.ai.batch_inference.v1.DescribeBatchInferenceRequest\x1a\x42.yandex.cloud.ai.batch_inference.v1.DescribeBatchInferenceResponse\x12\x87\x01\n\x04List\x12>.yandex.cloud.ai.batch_inference.v1.ListBatchInferencesRequest\x1a?.yandex.cloud.ai.batch_inference.v1.ListBatchInferencesResponse\x12\x8b\x01\n\x06\x43\x61ncel\x12?.yandex.cloud.ai.batch_inference.v1.CancelBatchInferenceRequest\x1a@.yandex.cloud.ai.batch_inference.v1.CancelBatchInferenceResponse\x12\x8b\x01\n\x06\x44\x65lete\x12?.yandex.cloud.ai.batch_inference.v1.DeleteBatchInferenceRequest\x1a@.yandex.cloud.ai.batch_inference.v1.DeleteBatchInferenceResponseBu\n&yandex.cloud.api.ai.batch_inference.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/batch_inference/v1;fomob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.batch_inference.v1.batch_inference_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&yandex.cloud.api.ai.batch_inference.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/batch_inference/v1;fomo'
  _globals['_DESCRIBEBATCHINFERENCEREQUEST'].fields_by_name['task_id']._loaded_options = None
  _globals['_DESCRIBEBATCHINFERENCEREQUEST'].fields_by_name['task_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTBATCHINFERENCESREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTBATCHINFERENCESREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _globals['_CANCELBATCHINFERENCEREQUEST'].fields_by_name['task_id']._loaded_options = None
  _globals['_CANCELBATCHINFERENCEREQUEST'].fields_by_name['task_id']._serialized_options = b'\350\3071\001'
  _globals['_DELETEBATCHINFERENCEREQUEST'].fields_by_name['task_id']._loaded_options = None
  _globals['_DELETEBATCHINFERENCEREQUEST'].fields_by_name['task_id']._serialized_options = b'\350\3071\001'
  _globals['_BATCHINFERENCEMETADATA']._serialized_start=199
  _globals['_BATCHINFERENCEMETADATA']._serialized_end=374
  _globals['_BATCHINFERENCERESPONSE']._serialized_start=376
  _globals['_BATCHINFERENCERESPONSE']._serialized_end=470
  _globals['_DESCRIBEBATCHINFERENCEREQUEST']._serialized_start=472
  _globals['_DESCRIBEBATCHINFERENCEREQUEST']._serialized_end=526
  _globals['_DESCRIBEBATCHINFERENCERESPONSE']._serialized_start=528
  _globals['_DESCRIBEBATCHINFERENCERESPONSE']._serialized_end=630
  _globals['_LISTBATCHINFERENCESREQUEST']._serialized_start=633
  _globals['_LISTBATCHINFERENCESREQUEST']._serialized_end=804
  _globals['_LISTBATCHINFERENCESRESPONSE']._serialized_start=806
  _globals['_LISTBATCHINFERENCESRESPONSE']._serialized_end=931
  _globals['_CANCELBATCHINFERENCEREQUEST']._serialized_start=933
  _globals['_CANCELBATCHINFERENCEREQUEST']._serialized_end=985
  _globals['_CANCELBATCHINFERENCERESPONSE']._serialized_start=987
  _globals['_CANCELBATCHINFERENCERESPONSE']._serialized_end=1034
  _globals['_DELETEBATCHINFERENCEREQUEST']._serialized_start=1036
  _globals['_DELETEBATCHINFERENCEREQUEST']._serialized_end=1088
  _globals['_DELETEBATCHINFERENCERESPONSE']._serialized_start=1090
  _globals['_DELETEBATCHINFERENCERESPONSE']._serialized_end=1137
  _globals['_BATCHINFERENCESERVICE']._serialized_start=1140
  _globals['_BATCHINFERENCESERVICE']._serialized_end=1733
# @@protoc_insertion_point(module_scope)
