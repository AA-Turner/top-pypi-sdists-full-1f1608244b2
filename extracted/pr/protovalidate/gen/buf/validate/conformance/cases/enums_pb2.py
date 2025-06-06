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
# source: buf/validate/conformance/cases/enums.proto
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
    'buf/validate/conformance/cases/enums.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate.conformance.cases.other_package import embed_pb2 as buf_dot_validate_dot_conformance_dot_cases_dot_other__package_dot_embed__pb2
from buf.validate.conformance.cases.yet_another_package import embed2_pb2 as buf_dot_validate_dot_conformance_dot_cases_dot_yet__another__package_dot_embed2__pb2
from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*buf/validate/conformance/cases/enums.proto\x12\x1e\x62uf.validate.conformance.cases\x1a\x38\x62uf/validate/conformance/cases/other_package/embed.proto\x1a?buf/validate/conformance/cases/yet_another_package/embed2.proto\x1a\x1b\x62uf/validate/validate.proto\"F\n\x08\x45numNone\x12:\n\x03val\x18\x01 \x01(\x0e\x32(.buf.validate.conformance.cases.TestEnumR\x03val\"Q\n\tEnumConst\x12\x44\n\x03val\x18\x01 \x01(\x0e\x32(.buf.validate.conformance.cases.TestEnumB\x08\xbaH\x05\x82\x01\x02\x08\x02R\x03val\"[\n\x0e\x45numAliasConst\x12I\n\x03val\x18\x01 \x01(\x0e\x32-.buf.validate.conformance.cases.TestEnumAliasB\x08\xbaH\x05\x82\x01\x02\x08\x02R\x03val\"S\n\x0b\x45numDefined\x12\x44\n\x03val\x18\x01 \x01(\x0e\x32(.buf.validate.conformance.cases.TestEnumB\x08\xbaH\x05\x82\x01\x02\x10\x01R\x03val\"]\n\x10\x45numAliasDefined\x12I\n\x03val\x18\x01 \x01(\x0e\x32-.buf.validate.conformance.cases.TestEnumAliasB\x08\xbaH\x05\x82\x01\x02\x10\x01R\x03val\"P\n\x06\x45numIn\x12\x46\n\x03val\x18\x01 \x01(\x0e\x32(.buf.validate.conformance.cases.TestEnumB\n\xbaH\x07\x82\x01\x04\x18\x00\x18\x02R\x03val\"Z\n\x0b\x45numAliasIn\x12K\n\x03val\x18\x01 \x01(\x0e\x32-.buf.validate.conformance.cases.TestEnumAliasB\n\xbaH\x07\x82\x01\x04\x18\x00\x18\x02R\x03val\"Q\n\tEnumNotIn\x12\x44\n\x03val\x18\x01 \x01(\x0e\x32(.buf.validate.conformance.cases.TestEnumB\x08\xbaH\x05\x82\x01\x02 \x01R\x03val\"[\n\x0e\x45numAliasNotIn\x12I\n\x03val\x18\x01 \x01(\x0e\x32-.buf.validate.conformance.cases.TestEnumAliasB\x08\xbaH\x05\x82\x01\x02 \x01R\x03val\"j\n\x0c\x45numExternal\x12Z\n\x03val\x18\x01 \x01(\x0e\x32>.buf.validate.conformance.cases.other_package.Embed.EnumeratedB\x08\xbaH\x05\x82\x01\x02\x10\x01R\x03val\"}\n\rEnumExternal2\x12l\n\x03val\x18\x01 \x01(\x0e\x32P.buf.validate.conformance.cases.other_package.Embed.DoubleEmbed.DoubleEnumeratedB\x08\xbaH\x05\x82\x01\x02\x10\x01R\x03val\"`\n\x13RepeatedEnumDefined\x12I\n\x03val\x18\x01 \x03(\x0e\x32(.buf.validate.conformance.cases.TestEnumB\r\xbaH\n\x92\x01\x07\"\x05\x82\x01\x02\x10\x01R\x03val\"~\n\x1bRepeatedExternalEnumDefined\x12_\n\x03val\x18\x01 \x03(\x0e\x32>.buf.validate.conformance.cases.other_package.Embed.EnumeratedB\r\xbaH\n\x92\x01\x07\"\x05\x82\x01\x02\x10\x01R\x03val\"\x8e\x01\n%RepeatedYetAnotherExternalEnumDefined\x12\x65\n\x03val\x18\x01 \x03(\x0e\x32\x44.buf.validate.conformance.cases.yet_another_package.Embed.EnumeratedB\r\xbaH\n\x92\x01\x07\"\x05\x82\x01\x02\x10\x01R\x03val\"\xcc\x01\n\x0eMapEnumDefined\x12X\n\x03val\x18\x01 \x03(\x0b\x32\x37.buf.validate.conformance.cases.MapEnumDefined.ValEntryB\r\xbaH\n\x9a\x01\x07*\x05\x82\x01\x02\x10\x01R\x03val\x1a`\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12>\n\x05value\x18\x02 \x01(\x0e\x32(.buf.validate.conformance.cases.TestEnumR\x05value:\x02\x38\x01\"\xf2\x01\n\x16MapExternalEnumDefined\x12`\n\x03val\x18\x01 \x03(\x0b\x32?.buf.validate.conformance.cases.MapExternalEnumDefined.ValEntryB\r\xbaH\n\x9a\x01\x07*\x05\x82\x01\x02\x10\x01R\x03val\x1av\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12T\n\x05value\x18\x02 \x01(\x0e\x32>.buf.validate.conformance.cases.other_package.Embed.EnumeratedR\x05value:\x02\x38\x01\"\xb3\x01\n\x0f\x45numInsideOneof\x12\x46\n\x03val\x18\x01 \x01(\x0e\x32(.buf.validate.conformance.cases.TestEnumB\x08\xbaH\x05\x82\x01\x02\x10\x01H\x00R\x03val\x12J\n\x04val2\x18\x02 \x01(\x0e\x32(.buf.validate.conformance.cases.TestEnumB\n\xbaH\x07\x82\x01\x04\x10\x01 \x00H\x01R\x04val2B\x05\n\x03\x66ooB\x05\n\x03\x62\x61r\"S\n\x0b\x45numExample\x12\x44\n\x03val\x18\x01 \x01(\x0e\x32(.buf.validate.conformance.cases.TestEnumB\x08\xbaH\x05\x82\x01\x02(\x02R\x03val*K\n\x08TestEnum\x12\x19\n\x15TEST_ENUM_UNSPECIFIED\x10\x00\x12\x11\n\rTEST_ENUM_ONE\x10\x01\x12\x11\n\rTEST_ENUM_TWO\x10\x02*\xc9\x01\n\rTestEnumAlias\x12\x1f\n\x1bTEST_ENUM_ALIAS_UNSPECIFIED\x10\x00\x12\x15\n\x11TEST_ENUM_ALIAS_A\x10\x01\x12\x15\n\x11TEST_ENUM_ALIAS_B\x10\x02\x12\x15\n\x11TEST_ENUM_ALIAS_C\x10\x03\x12\x19\n\x15TEST_ENUM_ALIAS_ALPHA\x10\x01\x12\x18\n\x14TEST_ENUM_ALIAS_BETA\x10\x02\x12\x19\n\x15TEST_ENUM_ALIAS_GAMMA\x10\x03\x1a\x02\x10\x01\x42\xcc\x01\n\"com.buf.validate.conformance.casesB\nEnumsProtoP\x01\xa2\x02\x04\x42VCC\xaa\x02\x1e\x42uf.Validate.Conformance.Cases\xca\x02\x1e\x42uf\\Validate\\Conformance\\Cases\xe2\x02*Buf\\Validate\\Conformance\\Cases\\GPBMetadata\xea\x02!Buf::Validate::Conformance::Casesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.conformance.cases.enums_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.buf.validate.conformance.casesB\nEnumsProtoP\001\242\002\004BVCC\252\002\036Buf.Validate.Conformance.Cases\312\002\036Buf\\Validate\\Conformance\\Cases\342\002*Buf\\Validate\\Conformance\\Cases\\GPBMetadata\352\002!Buf::Validate::Conformance::Cases'
  _globals['_TESTENUMALIAS']._loaded_options = None
  _globals['_TESTENUMALIAS']._serialized_options = b'\020\001'
  _globals['_ENUMCONST'].fields_by_name['val']._loaded_options = None
  _globals['_ENUMCONST'].fields_by_name['val']._serialized_options = b'\272H\005\202\001\002\010\002'
  _globals['_ENUMALIASCONST'].fields_by_name['val']._loaded_options = None
  _globals['_ENUMALIASCONST'].fields_by_name['val']._serialized_options = b'\272H\005\202\001\002\010\002'
  _globals['_ENUMDEFINED'].fields_by_name['val']._loaded_options = None
  _globals['_ENUMDEFINED'].fields_by_name['val']._serialized_options = b'\272H\005\202\001\002\020\001'
  _globals['_ENUMALIASDEFINED'].fields_by_name['val']._loaded_options = None
  _globals['_ENUMALIASDEFINED'].fields_by_name['val']._serialized_options = b'\272H\005\202\001\002\020\001'
  _globals['_ENUMIN'].fields_by_name['val']._loaded_options = None
  _globals['_ENUMIN'].fields_by_name['val']._serialized_options = b'\272H\007\202\001\004\030\000\030\002'
  _globals['_ENUMALIASIN'].fields_by_name['val']._loaded_options = None
  _globals['_ENUMALIASIN'].fields_by_name['val']._serialized_options = b'\272H\007\202\001\004\030\000\030\002'
  _globals['_ENUMNOTIN'].fields_by_name['val']._loaded_options = None
  _globals['_ENUMNOTIN'].fields_by_name['val']._serialized_options = b'\272H\005\202\001\002 \001'
  _globals['_ENUMALIASNOTIN'].fields_by_name['val']._loaded_options = None
  _globals['_ENUMALIASNOTIN'].fields_by_name['val']._serialized_options = b'\272H\005\202\001\002 \001'
  _globals['_ENUMEXTERNAL'].fields_by_name['val']._loaded_options = None
  _globals['_ENUMEXTERNAL'].fields_by_name['val']._serialized_options = b'\272H\005\202\001\002\020\001'
  _globals['_ENUMEXTERNAL2'].fields_by_name['val']._loaded_options = None
  _globals['_ENUMEXTERNAL2'].fields_by_name['val']._serialized_options = b'\272H\005\202\001\002\020\001'
  _globals['_REPEATEDENUMDEFINED'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDENUMDEFINED'].fields_by_name['val']._serialized_options = b'\272H\n\222\001\007\"\005\202\001\002\020\001'
  _globals['_REPEATEDEXTERNALENUMDEFINED'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDEXTERNALENUMDEFINED'].fields_by_name['val']._serialized_options = b'\272H\n\222\001\007\"\005\202\001\002\020\001'
  _globals['_REPEATEDYETANOTHEREXTERNALENUMDEFINED'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDYETANOTHEREXTERNALENUMDEFINED'].fields_by_name['val']._serialized_options = b'\272H\n\222\001\007\"\005\202\001\002\020\001'
  _globals['_MAPENUMDEFINED_VALENTRY']._loaded_options = None
  _globals['_MAPENUMDEFINED_VALENTRY']._serialized_options = b'8\001'
  _globals['_MAPENUMDEFINED'].fields_by_name['val']._loaded_options = None
  _globals['_MAPENUMDEFINED'].fields_by_name['val']._serialized_options = b'\272H\n\232\001\007*\005\202\001\002\020\001'
  _globals['_MAPEXTERNALENUMDEFINED_VALENTRY']._loaded_options = None
  _globals['_MAPEXTERNALENUMDEFINED_VALENTRY']._serialized_options = b'8\001'
  _globals['_MAPEXTERNALENUMDEFINED'].fields_by_name['val']._loaded_options = None
  _globals['_MAPEXTERNALENUMDEFINED'].fields_by_name['val']._serialized_options = b'\272H\n\232\001\007*\005\202\001\002\020\001'
  _globals['_ENUMINSIDEONEOF'].fields_by_name['val']._loaded_options = None
  _globals['_ENUMINSIDEONEOF'].fields_by_name['val']._serialized_options = b'\272H\005\202\001\002\020\001'
  _globals['_ENUMINSIDEONEOF'].fields_by_name['val2']._loaded_options = None
  _globals['_ENUMINSIDEONEOF'].fields_by_name['val2']._serialized_options = b'\272H\007\202\001\004\020\001 \000'
  _globals['_ENUMEXAMPLE'].fields_by_name['val']._loaded_options = None
  _globals['_ENUMEXAMPLE'].fields_by_name['val']._serialized_options = b'\272H\005\202\001\002(\002'
  _globals['_TESTENUM']._serialized_start=2333
  _globals['_TESTENUM']._serialized_end=2408
  _globals['_TESTENUMALIAS']._serialized_start=2411
  _globals['_TESTENUMALIAS']._serialized_end=2612
  _globals['_ENUMNONE']._serialized_start=230
  _globals['_ENUMNONE']._serialized_end=300
  _globals['_ENUMCONST']._serialized_start=302
  _globals['_ENUMCONST']._serialized_end=383
  _globals['_ENUMALIASCONST']._serialized_start=385
  _globals['_ENUMALIASCONST']._serialized_end=476
  _globals['_ENUMDEFINED']._serialized_start=478
  _globals['_ENUMDEFINED']._serialized_end=561
  _globals['_ENUMALIASDEFINED']._serialized_start=563
  _globals['_ENUMALIASDEFINED']._serialized_end=656
  _globals['_ENUMIN']._serialized_start=658
  _globals['_ENUMIN']._serialized_end=738
  _globals['_ENUMALIASIN']._serialized_start=740
  _globals['_ENUMALIASIN']._serialized_end=830
  _globals['_ENUMNOTIN']._serialized_start=832
  _globals['_ENUMNOTIN']._serialized_end=913
  _globals['_ENUMALIASNOTIN']._serialized_start=915
  _globals['_ENUMALIASNOTIN']._serialized_end=1006
  _globals['_ENUMEXTERNAL']._serialized_start=1008
  _globals['_ENUMEXTERNAL']._serialized_end=1114
  _globals['_ENUMEXTERNAL2']._serialized_start=1116
  _globals['_ENUMEXTERNAL2']._serialized_end=1241
  _globals['_REPEATEDENUMDEFINED']._serialized_start=1243
  _globals['_REPEATEDENUMDEFINED']._serialized_end=1339
  _globals['_REPEATEDEXTERNALENUMDEFINED']._serialized_start=1341
  _globals['_REPEATEDEXTERNALENUMDEFINED']._serialized_end=1467
  _globals['_REPEATEDYETANOTHEREXTERNALENUMDEFINED']._serialized_start=1470
  _globals['_REPEATEDYETANOTHEREXTERNALENUMDEFINED']._serialized_end=1612
  _globals['_MAPENUMDEFINED']._serialized_start=1615
  _globals['_MAPENUMDEFINED']._serialized_end=1819
  _globals['_MAPENUMDEFINED_VALENTRY']._serialized_start=1723
  _globals['_MAPENUMDEFINED_VALENTRY']._serialized_end=1819
  _globals['_MAPEXTERNALENUMDEFINED']._serialized_start=1822
  _globals['_MAPEXTERNALENUMDEFINED']._serialized_end=2064
  _globals['_MAPEXTERNALENUMDEFINED_VALENTRY']._serialized_start=1946
  _globals['_MAPEXTERNALENUMDEFINED_VALENTRY']._serialized_end=2064
  _globals['_ENUMINSIDEONEOF']._serialized_start=2067
  _globals['_ENUMINSIDEONEOF']._serialized_end=2246
  _globals['_ENUMEXAMPLE']._serialized_start=2248
  _globals['_ENUMEXAMPLE']._serialized_end=2331
# @@protoc_insertion_point(module_scope)
