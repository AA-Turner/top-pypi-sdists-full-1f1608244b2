# Copyright 2023-2025 Buf Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: buf/validate/conformance/cases/bool.proto
# Protobuf Python Version: 6.30.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    1,
    '',
    'buf/validate/conformance/cases/bool.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)buf/validate/conformance/cases/bool.proto\x12\x1e\x62uf.validate.conformance.cases\x1a\x1b\x62uf/validate/validate.proto\"\x1c\n\x08\x42oolNone\x12\x10\n\x03val\x18\x01 \x01(\x08R\x03val\"*\n\rBoolConstTrue\x12\x19\n\x03val\x18\x01 \x01(\x08\x42\x07\xbaH\x04j\x02\x08\x01R\x03val\"+\n\x0e\x42oolConstFalse\x12\x19\n\x03val\x18\x01 \x01(\x08\x42\x07\xbaH\x04j\x02\x08\x00R\x03val\"(\n\x0b\x42oolExample\x12\x19\n\x03val\x18\x01 \x01(\x08\x42\x07\xbaH\x04j\x02\x10\x01R\x03valB\xcb\x01\n\"com.buf.validate.conformance.casesB\tBoolProtoP\x01\xa2\x02\x04\x42VCC\xaa\x02\x1e\x42uf.Validate.Conformance.Cases\xca\x02\x1e\x42uf\\Validate\\Conformance\\Cases\xe2\x02*Buf\\Validate\\Conformance\\Cases\\GPBMetadata\xea\x02!Buf::Validate::Conformance::Casesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.conformance.cases.bool_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.buf.validate.conformance.casesB\tBoolProtoP\001\242\002\004BVCC\252\002\036Buf.Validate.Conformance.Cases\312\002\036Buf\\Validate\\Conformance\\Cases\342\002*Buf\\Validate\\Conformance\\Cases\\GPBMetadata\352\002!Buf::Validate::Conformance::Cases'
  _globals['_BOOLCONSTTRUE'].fields_by_name['val']._loaded_options = None
  _globals['_BOOLCONSTTRUE'].fields_by_name['val']._serialized_options = b'\272H\004j\002\010\001'
  _globals['_BOOLCONSTFALSE'].fields_by_name['val']._loaded_options = None
  _globals['_BOOLCONSTFALSE'].fields_by_name['val']._serialized_options = b'\272H\004j\002\010\000'
  _globals['_BOOLEXAMPLE'].fields_by_name['val']._loaded_options = None
  _globals['_BOOLEXAMPLE'].fields_by_name['val']._serialized_options = b'\272H\004j\002\020\001'
  _globals['_BOOLNONE']._serialized_start=106
  _globals['_BOOLNONE']._serialized_end=134
  _globals['_BOOLCONSTTRUE']._serialized_start=136
  _globals['_BOOLCONSTTRUE']._serialized_end=178
  _globals['_BOOLCONSTFALSE']._serialized_start=180
  _globals['_BOOLCONSTFALSE']._serialized_end=223
  _globals['_BOOLEXAMPLE']._serialized_start=225
  _globals['_BOOLEXAMPLE']._serialized_end=265
# @@protoc_insertion_point(module_scope)
