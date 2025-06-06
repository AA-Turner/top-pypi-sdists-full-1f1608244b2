# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: gateway/training.proto
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
    'gateway/training.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from . import deployment_pb2 as gateway_dot_deployment__pb2
from ..google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ..google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16gateway/training.proto\x12\x07gateway\x1a\x1b\x62uf/validate/validate.proto\x1a\x18gateway/deployment.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/visibility.proto\">\n\x0f\x45\x61rlyStopConfig\x12\x14\n\x06is_set\x18\x01 \x01(\x08\x42\x04\xe2\x41\x01\x01\x12\x15\n\x07\x65nabled\x18\x02 \x01(\x08\x42\x04\xe2\x41\x01\x01\"\xa6\x06\n\x12\x42\x61seTrainingConfig\x12\x1a\n\x0coutput_model\x18\x01 \x01(\tB\x04\xe2\x41\x01\x01\x12\x18\n\nbase_model\x18\x02 \x01(\tB\x04\xe2\x41\x01\x01\x12\x1d\n\x0fwarm_start_from\x18\x03 \x01(\tB\x04\xe2\x41\x01\x01\x12\x1c\n\x0ejinja_template\x18\x04 \x01(\tB\x04\xe2\x41\x01\x01\x12*\n\rlearning_rate\x18\x05 \x01(\x02\x42\x13\xe2\x41\x01\x01\xbaH\x0c\n\n\x1d\xcd\xcc\xcc=-\x00\x00\x00\x00\x12 \n\x12max_context_length\x18\x06 \x01(\x05\x42\x04\xe2\x41\x01\x01\x12 \n\tlora_rank\x18\x07 \x01(\x05\x42\r\xe2\x41\x01\x01\xbaH\x06\x1a\x04\x18 (\x00\x12Y\n\x1b\x62\x61se_model_weight_precision\x18\x08 \x01(\x0e\x32\x18.gateway.WeightPrecisionB\x1a\xe2\x41\x01\x01\xfa\xd2\xe4\x93\x02\x10\x12\x0eSUPERUSER_ONLY\x12N\n\x10\x61\x63\x63\x65lerator_type\x18\t \x01(\x0e\x32\x18.gateway.AcceleratorTypeB\x1a\xe2\x41\x01\x01\xfa\xd2\xe4\x93\x02\x10\x12\x0eSUPERUSER_ONLY\x12\x35\n\x11\x61\x63\x63\x65lerator_count\x18\n \x01(\x05\x42\x1a\xe2\x41\x01\x01\xfa\xd2\xe4\x93\x02\x10\x12\x0eSUPERUSER_ONLY\x12%\n\x06region\x18\x0b \x01(\x0e\x32\x0f.gateway.RegionB\x04\xe2\x41\x01\x01\x12\x1b\n\x06\x65pochs\x18\x0c \x01(\x05\x42\x0b\xe2\x41\x01\x01\xbaH\x04\x1a\x02(\x00\x12\x18\n\nbatch_size\x18\r \x01(\x05\x42\x04\xe2\x41\x01\x01\x12\x33\n\x0fis_intermediate\x18\x0e \x01(\x08\x42\x1a\xe2\x41\x01\x01\xfa\xd2\xe4\x93\x02\x10\x12\x0eSUPERUSER_ONLY:\xb7\x01\xbaH\xb3\x01\x1a\xb0\x01\n5base_training_config.exactly_one_of_must_be_specified\x12>exactly one of base_model or warm_start_from must be specified\x1a\x37(this.base_model != \'\') != (this.warm_start_from != \'\')*T\n\x0fWeightPrecision\x12 \n\x1cWEIGHT_PRECISION_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x42\x46LOAT16\x10\x01\x12\x08\n\x04INT8\x10\x02\x12\x07\n\x03NF4\x10\x03\x42\x43ZAgithub.com/fw-ai/fireworks/control_plane/protos/generated/gatewayb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gateway.training_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZAgithub.com/fw-ai/fireworks/control_plane/protos/generated/gateway'
  _globals['_EARLYSTOPCONFIG'].fields_by_name['is_set']._loaded_options = None
  _globals['_EARLYSTOPCONFIG'].fields_by_name['is_set']._serialized_options = b'\342A\001\001'
  _globals['_EARLYSTOPCONFIG'].fields_by_name['enabled']._loaded_options = None
  _globals['_EARLYSTOPCONFIG'].fields_by_name['enabled']._serialized_options = b'\342A\001\001'
  _globals['_BASETRAININGCONFIG'].fields_by_name['output_model']._loaded_options = None
  _globals['_BASETRAININGCONFIG'].fields_by_name['output_model']._serialized_options = b'\342A\001\001'
  _globals['_BASETRAININGCONFIG'].fields_by_name['base_model']._loaded_options = None
  _globals['_BASETRAININGCONFIG'].fields_by_name['base_model']._serialized_options = b'\342A\001\001'
  _globals['_BASETRAININGCONFIG'].fields_by_name['warm_start_from']._loaded_options = None
  _globals['_BASETRAININGCONFIG'].fields_by_name['warm_start_from']._serialized_options = b'\342A\001\001'
  _globals['_BASETRAININGCONFIG'].fields_by_name['jinja_template']._loaded_options = None
  _globals['_BASETRAININGCONFIG'].fields_by_name['jinja_template']._serialized_options = b'\342A\001\001'
  _globals['_BASETRAININGCONFIG'].fields_by_name['learning_rate']._loaded_options = None
  _globals['_BASETRAININGCONFIG'].fields_by_name['learning_rate']._serialized_options = b'\342A\001\001\272H\014\n\n\035\315\314\314=-\000\000\000\000'
  _globals['_BASETRAININGCONFIG'].fields_by_name['max_context_length']._loaded_options = None
  _globals['_BASETRAININGCONFIG'].fields_by_name['max_context_length']._serialized_options = b'\342A\001\001'
  _globals['_BASETRAININGCONFIG'].fields_by_name['lora_rank']._loaded_options = None
  _globals['_BASETRAININGCONFIG'].fields_by_name['lora_rank']._serialized_options = b'\342A\001\001\272H\006\032\004\030 (\000'
  _globals['_BASETRAININGCONFIG'].fields_by_name['base_model_weight_precision']._loaded_options = None
  _globals['_BASETRAININGCONFIG'].fields_by_name['base_model_weight_precision']._serialized_options = b'\342A\001\001\372\322\344\223\002\020\022\016SUPERUSER_ONLY'
  _globals['_BASETRAININGCONFIG'].fields_by_name['accelerator_type']._loaded_options = None
  _globals['_BASETRAININGCONFIG'].fields_by_name['accelerator_type']._serialized_options = b'\342A\001\001\372\322\344\223\002\020\022\016SUPERUSER_ONLY'
  _globals['_BASETRAININGCONFIG'].fields_by_name['accelerator_count']._loaded_options = None
  _globals['_BASETRAININGCONFIG'].fields_by_name['accelerator_count']._serialized_options = b'\342A\001\001\372\322\344\223\002\020\022\016SUPERUSER_ONLY'
  _globals['_BASETRAININGCONFIG'].fields_by_name['region']._loaded_options = None
  _globals['_BASETRAININGCONFIG'].fields_by_name['region']._serialized_options = b'\342A\001\001'
  _globals['_BASETRAININGCONFIG'].fields_by_name['epochs']._loaded_options = None
  _globals['_BASETRAININGCONFIG'].fields_by_name['epochs']._serialized_options = b'\342A\001\001\272H\004\032\002(\000'
  _globals['_BASETRAININGCONFIG'].fields_by_name['batch_size']._loaded_options = None
  _globals['_BASETRAININGCONFIG'].fields_by_name['batch_size']._serialized_options = b'\342A\001\001'
  _globals['_BASETRAININGCONFIG'].fields_by_name['is_intermediate']._loaded_options = None
  _globals['_BASETRAININGCONFIG'].fields_by_name['is_intermediate']._serialized_options = b'\342A\001\001\372\322\344\223\002\020\022\016SUPERUSER_ONLY'
  _globals['_BASETRAININGCONFIG']._loaded_options = None
  _globals['_BASETRAININGCONFIG']._serialized_options = b'\272H\263\001\032\260\001\n5base_training_config.exactly_one_of_must_be_specified\022>exactly one of base_model or warm_start_from must be specified\0327(this.base_model != \'\') != (this.warm_start_from != \'\')'
  _globals['_WEIGHTPRECISION']._serialized_start=1025
  _globals['_WEIGHTPRECISION']._serialized_end=1109
  _globals['_EARLYSTOPCONFIG']._serialized_start=152
  _globals['_EARLYSTOPCONFIG']._serialized_end=214
  _globals['_BASETRAININGCONFIG']._serialized_start=217
  _globals['_BASETRAININGCONFIG']._serialized_end=1023
# @@protoc_insertion_point(module_scope)
