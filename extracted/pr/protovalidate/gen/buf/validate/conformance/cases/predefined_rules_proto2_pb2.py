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
# source: buf/validate/conformance/cases/predefined_rules_proto2.proto
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
    'buf/validate/conformance/cases/predefined_rules_proto2.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<buf/validate/conformance/cases/predefined_rules_proto2.proto\x12\x1e\x62uf.validate.conformance.cases\x1a\x1b\x62uf/validate/validate.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\":\n\x19PredefinedFloatRuleProto2\x12\x1d\n\x03val\x18\x01 \x01(\x02\x42\x0b\xbaH\x08\n\x06\xcdH\x00\x00\x80?R\x03val\"?\n\x1aPredefinedDoubleRuleProto2\x12!\n\x03val\x18\x01 \x01(\x01\x42\x0f\xbaH\x0c\x12\n\xc9H\x00\x00\x00\x00\x00\x00\xf0?R\x03val\"@\n\x19PredefinedInt32RuleProto2\x12#\n\x03val\x18\x01 \x01(\x05\x42\x11\xbaH\x0e\x1a\x0c\xc8H\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01R\x03val\"B\n\x19PredefinedInt64RuleProto2\x12%\n\x03val\x18\x01 \x01(\x03\x42\x13\xbaH\x10\"\x0e\xcaH\x0b\x08\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01R\x03val\"8\n\x1aPredefinedUInt32RuleProto2\x12\x1a\n\x03val\x18\x01 \x01(\rB\x08\xbaH\x05*\x03\xc8H\x01R\x03val\"8\n\x1aPredefinedUInt64RuleProto2\x12\x1a\n\x03val\x18\x01 \x01(\x04\x42\x08\xbaH\x05\x32\x03\xc8H\x01R\x03val\"8\n\x1aPredefinedSInt32RuleProto2\x12\x1a\n\x03val\x18\x01 \x01(\x11\x42\x08\xbaH\x05:\x03\xc8H\x01R\x03val\"8\n\x1aPredefinedSInt64RuleProto2\x12\x1a\n\x03val\x18\x01 \x01(\x12\x42\x08\xbaH\x05\x42\x03\xc8H\x01R\x03val\"9\n\x1bPredefinedFixed32RuleProto2\x12\x1a\n\x03val\x18\x01 \x01(\x07\x42\x08\xbaH\x05J\x03\xc8H\x01R\x03val\"9\n\x1bPredefinedFixed64RuleProto2\x12\x1a\n\x03val\x18\x01 \x01(\x06\x42\x08\xbaH\x05R\x03\xc8H\x01R\x03val\":\n\x1cPredefinedSFixed32RuleProto2\x12\x1a\n\x03val\x18\x01 \x01(\x0f\x42\x08\xbaH\x05Z\x03\xc8H\x01R\x03val\":\n\x1cPredefinedSFixed64RuleProto2\x12\x1a\n\x03val\x18\x01 \x01(\x10\x42\x08\xbaH\x05\x62\x03\xc8H\x01R\x03val\"6\n\x18PredefinedBoolRuleProto2\x12\x1a\n\x03val\x18\x01 \x01(\x08\x42\x08\xbaH\x05j\x03\xc8H\x01R\x03val\"8\n\x1aPredefinedStringRuleProto2\x12\x1a\n\x03val\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xc8H\x01R\x03val\"7\n\x19PredefinedBytesRuleProto2\x12\x1a\n\x03val\x18\x01 \x01(\x0c\x42\x08\xbaH\x05z\x03\xc8H\x01R\x03val\"\xc1\x01\n\x18PredefinedEnumRuleProto2\x12`\n\x03val\x18\x01 \x01(\x0e\x32\x43.buf.validate.conformance.cases.PredefinedEnumRuleProto2.EnumProto2B\t\xbaH\x06\x82\x01\x03\xc8H\x01R\x03val\"C\n\nEnumProto2\x12 \n\x1c\x45NUM_PROTO2_ZERO_UNSPECIFIED\x10\x00\x12\x13\n\x0f\x45NUM_PROTO2_ONE\x10\x01\";\n\x1cPredefinedRepeatedRuleProto2\x12\x1b\n\x03val\x18\x01 \x03(\x04\x42\t\xbaH\x06\x92\x01\x03\xc8H\x01R\x03val\"V\n\x1cPredefinedDurationRuleProto2\x12\x36\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\t\xbaH\x06\xaa\x01\x03\xc8H\x01R\x03val\"X\n\x1dPredefinedTimestampRuleProto2\x12\x37\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\t\xbaH\x06\xb2\x01\x03\xc8H\x01R\x03val\"^\n PredefinedWrappedFloatRuleProto2\x12:\n\x03val\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.FloatValueB\x0b\xbaH\x08\n\x06\xcdH\x00\x00\x80?R\x03val\"d\n!PredefinedWrappedDoubleRuleProto2\x12?\n\x03val\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueB\x0f\xbaH\x0c\x12\n\xc9H\x00\x00\x00\x00\x00\x00\xf0?R\x03val\"d\n PredefinedWrappedInt32RuleProto2\x12@\n\x03val\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueB\x11\xbaH\x0e\x1a\x0c\xc8H\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01R\x03val\"f\n PredefinedWrappedInt64RuleProto2\x12\x42\n\x03val\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x13\xbaH\x10\"\x0e\xcaH\x0b\x08\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01R\x03val\"]\n!PredefinedWrappedUInt32RuleProto2\x12\x38\n\x03val\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\x08\xbaH\x05*\x03\xc8H\x01R\x03val\"]\n!PredefinedWrappedUInt64RuleProto2\x12\x38\n\x03val\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64ValueB\x08\xbaH\x05\x32\x03\xc8H\x01R\x03val\"Y\n\x1fPredefinedWrappedBoolRuleProto2\x12\x36\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueB\x08\xbaH\x05j\x03\xc8H\x01R\x03val\"]\n!PredefinedWrappedStringRuleProto2\x12\x38\n\x03val\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x08\xbaH\x05r\x03\xc8H\x01R\x03val\"[\n PredefinedWrappedBytesRuleProto2\x12\x37\n\x03val\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.BytesValueB\x08\xbaH\x05z\x03\xc8H\x01R\x03val\"k\n(PredefinedRepeatedWrappedFloatRuleProto2\x12?\n\x03val\x18\x01 \x03(\x0b\x32\x1b.google.protobuf.FloatValueB\x10\xbaH\r\x92\x01\n\"\x08\n\x06\xcdH\x00\x00\x80?R\x03val\"q\n)PredefinedRepeatedWrappedDoubleRuleProto2\x12\x44\n\x03val\x18\x01 \x03(\x0b\x32\x1c.google.protobuf.DoubleValueB\x14\xbaH\x11\x92\x01\x0e\"\x0c\x12\n\xc9H\x00\x00\x00\x00\x00\x00\xf0?R\x03val\"q\n(PredefinedRepeatedWrappedInt32RuleProto2\x12\x45\n\x03val\x18\x01 \x03(\x0b\x32\x1b.google.protobuf.Int32ValueB\x16\xbaH\x13\x92\x01\x10\"\x0e\x1a\x0c\xc8H\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01R\x03val\"s\n(PredefinedRepeatedWrappedInt64RuleProto2\x12G\n\x03val\x18\x01 \x03(\x0b\x32\x1b.google.protobuf.Int64ValueB\x18\xbaH\x15\x92\x01\x12\"\x10\"\x0e\xcaH\x0b\x08\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01R\x03val\"j\n)PredefinedRepeatedWrappedUInt32RuleProto2\x12=\n\x03val\x18\x01 \x03(\x0b\x32\x1c.google.protobuf.UInt32ValueB\r\xbaH\n\x92\x01\x07\"\x05*\x03\xc8H\x01R\x03val\"j\n)PredefinedRepeatedWrappedUInt64RuleProto2\x12=\n\x03val\x18\x01 \x03(\x0b\x32\x1c.google.protobuf.UInt64ValueB\r\xbaH\n\x92\x01\x07\"\x05\x32\x03\xc8H\x01R\x03val\"f\n\'PredefinedRepeatedWrappedBoolRuleProto2\x12;\n\x03val\x18\x01 \x03(\x0b\x32\x1a.google.protobuf.BoolValueB\r\xbaH\n\x92\x01\x07\"\x05j\x03\xc8H\x01R\x03val\"j\n)PredefinedRepeatedWrappedStringRuleProto2\x12=\n\x03val\x18\x01 \x03(\x0b\x32\x1c.google.protobuf.StringValueB\r\xbaH\n\x92\x01\x07\"\x05r\x03\xc8H\x01R\x03val\"h\n(PredefinedRepeatedWrappedBytesRuleProto2\x12<\n\x03val\x18\x01 \x03(\x0b\x32\x1b.google.protobuf.BytesValueB\r\xbaH\n\x92\x01\x07\"\x05z\x03\xc8H\x01R\x03val\"\xbe\x03\n\x1dPredefinedAndCustomRuleProto2\x12q\n\x01\x61\x18\x01 \x01(\x11\x42\x63\xbaH`:\x03\xc8H\x01\xba\x01X\n(predefined_and_custom_rule_scalar_proto2\x1a,this > 24 ? \'\' : \'a must be greater than 24\'R\x01\x61\x12\xb4\x01\n\x01\x62\x18\x02 \x01(\x0b\x32\x44.buf.validate.conformance.cases.PredefinedAndCustomRuleProto2.NestedB`\xbaH]\xba\x01Z\n*predefined_and_custom_rule_embedded_proto2\x12\x1b\x62.c must be a multiple of 3\x1a\x0fthis.c % 3 == 0R\x01\x62\x1as\n\x06Nested\x12i\n\x01\x63\x18\x01 \x01(\x11\x42[\xbaHX:\x03\xc8H\x01\xba\x01P\n(predefined_and_custom_rule_nested_proto2\x1a$this > 0 ? \'\' : \'c must be positive\'R\x01\x63\"\xa5\x01\n%StandardPredefinedAndCustomRuleProto2\x12|\n\x01\x61\x18\x01 \x01(\x11\x42n\xbaHk:\x05\x10\x38\xc8H\x01\xba\x01\x61\n1standard_predefined_and_custom_rule_scalar_proto2\x1a,this > 24 ? \'\' : \'a must be greater than 24\'R\x01\x61:\xa9\x01\n\x16\x66loat_abs_range_proto2\x12\x18.buf.validate.FloatRules\x18\x89\t \x01(\x02\x42Y\xc2HV\nT\n\x16\x66loat.abs_range.proto2\x12\x1b\x66loat value is out of range\x1a\x1dthis >= -rule && this <= ruleR\x13\x66loatAbsRangeProto2:\xae\x01\n\x17\x64ouble_abs_range_proto2\x12\x19.buf.validate.DoubleRules\x18\x89\t \x01(\x01\x42[\xc2HX\nV\n\x17\x64ouble.abs_range.proto2\x12\x1c\x64ouble value is out of range\x1a\x1dthis >= -rule && this <= ruleR\x14\x64oubleAbsRangeProto2:\xb6\x01\n\x13int32_abs_in_proto2\x12\x18.buf.validate.Int32Rules\x18\x89\t \x03(\x05\x42l\xc2Hi\ng\n\x13int32.abs_in.proto2\x12\'value must be in absolute value of list\x1a\'this in rule || this in rule.map(n, -n)R\x10int32AbsInProto2:\xd3\x01\n\x13int64_abs_in_proto2\x12\x18.buf.validate.Int64Rules\x18\x89\t \x03(\x0b\x32\x1b.google.protobuf.Int64ValueBl\xc2Hi\ng\n\x13int64.abs_in.proto2\x12\'value must be in absolute value of list\x1a\'this in rule || this in rule.map(n, -n)R\x10int64AbsInProto2:\x8e\x01\n\x12uint32_even_proto2\x12\x19.buf.validate.UInt32Rules\x18\x89\t \x01(\x08\x42\x44\xc2HA\n?\n\x12uint32.even.proto2\x12\x18uint32 value is not even\x1a\x0fthis % 2u == 0uR\x10uint32EvenProto2:\x8e\x01\n\x12uint64_even_proto2\x12\x19.buf.validate.UInt64Rules\x18\x89\t \x01(\x08\x42\x44\xc2HA\n?\n\x12uint64.even.proto2\x12\x18uint64 value is not even\x1a\x0fthis % 2u == 0uR\x10uint64EvenProto2:\x8c\x01\n\x12sint32_even_proto2\x12\x19.buf.validate.SInt32Rules\x18\x89\t \x01(\x08\x42\x42\xc2H?\n=\n\x12sint32.even.proto2\x12\x18sint32 value is not even\x1a\rthis % 2 == 0R\x10sint32EvenProto2:\x8c\x01\n\x12sint64_even_proto2\x12\x19.buf.validate.SInt64Rules\x18\x89\t \x01(\x08\x42\x42\xc2H?\n=\n\x12sint64.even.proto2\x12\x18sint64 value is not even\x1a\rthis % 2 == 0R\x10sint64EvenProto2:\x93\x01\n\x13\x66ixed32_even_proto2\x12\x1a.buf.validate.Fixed32Rules\x18\x89\t \x01(\x08\x42\x46\xc2HC\nA\n\x13\x66ixed32.even.proto2\x12\x19\x66ixed32 value is not even\x1a\x0fthis % 2u == 0uR\x11\x66ixed32EvenProto2:\x93\x01\n\x13\x66ixed64_even_proto2\x12\x1a.buf.validate.Fixed64Rules\x18\x89\t \x01(\x08\x42\x46\xc2HC\nA\n\x13\x66ixed64.even.proto2\x12\x19\x66ixed64 value is not even\x1a\x0fthis % 2u == 0uR\x11\x66ixed64EvenProto2:\x96\x01\n\x14sfixed32_even_proto2\x12\x1b.buf.validate.SFixed32Rules\x18\x89\t \x01(\x08\x42\x46\xc2HC\nA\n\x14sfixed32.even.proto2\x12\x1asfixed32 value is not even\x1a\rthis % 2 == 0R\x12sfixed32EvenProto2:\x96\x01\n\x14sfixed64_even_proto2\x12\x1b.buf.validate.SFixed64Rules\x18\x89\t \x01(\x08\x42\x46\xc2HC\nA\n\x14sfixed64.even.proto2\x12\x1asfixed64 value is not even\x1a\rthis % 2 == 0R\x12sfixed64EvenProto2:\x86\x01\n\x11\x62ool_false_proto2\x12\x17.buf.validate.BoolRules\x18\x89\t \x01(\x08\x42@\xc2H=\n;\n\x11\x62ool.false.proto2\x12\x17\x62ool value is not false\x1a\rthis == falseR\x0f\x62oolFalseProto2:\xfe\x01\n\x18string_valid_path_proto2\x12\x19.buf.validate.StringRules\x18\x89\t \x01(\x08\x42\xa8\x01\xc2H\xa4\x01\n\xa1\x01\n\x18string.valid_path.proto2\x1a\x84\x01!this.matches(\'^([^/.][^/]?|[^/][^/.]|[^/]{3,})(/([^/.][^/]?|[^/][^/.]|[^/]{3,}))*$\') ? \'not a valid path: `%s`\'.format([this]) : \'\'R\x15stringValidPathProto2:\x82\x02\n\x17\x62ytes_valid_path_proto2\x12\x18.buf.validate.BytesRules\x18\x89\t \x01(\x08\x42\xaf\x01\xc2H\xab\x01\n\xa8\x01\n\x17\x62ytes.valid_path.proto2\x1a\x8c\x01!string(this).matches(\'^([^/.][^/]?|[^/][^/.]|[^/]{3,})(/([^/.][^/]?|[^/][^/.]|[^/]{3,}))*$\') ? \'not a valid path: `%s`\'.format([this]) : \'\'R\x14\x62ytesValidPathProto2:\x92\x01\n\x14\x65num_non_zero_proto2\x12\x17.buf.validate.EnumRules\x18\x89\t \x01(\x08\x42G\xc2HD\nB\n\x14\x65num.non_zero.proto2\x12\x1a\x65num value is not non-zero\x1a\x0eint(this) != 0R\x11\x65numNonZeroProto2:\xcc\x01\n\x1drepeated_at_least_five_proto2\x12\x1b.buf.validate.RepeatedRules\x18\x89\t \x01(\x08\x42l\xc2Hi\ng\n\x1drepeated.at_least_five.proto2\x12-repeated field must have at least five values\x1a\x17uint(this.size()) >= 5uR\x19repeatedAtLeastFiveProto2:\xb9\x01\n\x18\x64uration_too_long_proto2\x12\x1b.buf.validate.DurationRules\x18\x89\t \x01(\x08\x42\x62\xc2H_\n]\n\x18\x64uration.too_long.proto2\x12(duration can\'t be longer than 10 seconds\x1a\x17this <= duration(\'10s\')R\x15\x64urationTooLongProto2:\xc8\x01\n\x19timestamp_in_range_proto2\x12\x1c.buf.validate.TimestampRules\x18\x89\t \x01(\x08\x42n\xc2Hk\ni\n\x1btimestamp.time_range.proto2\x12\x16timestamp out of range\x1a\x32int(this) >= 1049587200 && int(this) <= 1080432000R\x16timestampInRangeProto2B\xdc\x01\n\"com.buf.validate.conformance.casesB\x1aPredefinedRulesProto2ProtoP\x01\xa2\x02\x04\x42VCC\xaa\x02\x1e\x42uf.Validate.Conformance.Cases\xca\x02\x1e\x42uf\\Validate\\Conformance\\Cases\xe2\x02*Buf\\Validate\\Conformance\\Cases\\GPBMetadata\xea\x02!Buf::Validate::Conformance::Cases')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.conformance.cases.predefined_rules_proto2_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.buf.validate.conformance.casesB\032PredefinedRulesProto2ProtoP\001\242\002\004BVCC\252\002\036Buf.Validate.Conformance.Cases\312\002\036Buf\\Validate\\Conformance\\Cases\342\002*Buf\\Validate\\Conformance\\Cases\\GPBMetadata\352\002!Buf::Validate::Conformance::Cases'
  _globals['float_abs_range_proto2']._loaded_options = None
  _globals['float_abs_range_proto2']._serialized_options = b'\302HV\nT\n\026float.abs_range.proto2\022\033float value is out of range\032\035this >= -rule && this <= rule'
  _globals['double_abs_range_proto2']._loaded_options = None
  _globals['double_abs_range_proto2']._serialized_options = b'\302HX\nV\n\027double.abs_range.proto2\022\034double value is out of range\032\035this >= -rule && this <= rule'
  _globals['int32_abs_in_proto2']._loaded_options = None
  _globals['int32_abs_in_proto2']._serialized_options = b'\302Hi\ng\n\023int32.abs_in.proto2\022\'value must be in absolute value of list\032\'this in rule || this in rule.map(n, -n)'
  _globals['int64_abs_in_proto2']._loaded_options = None
  _globals['int64_abs_in_proto2']._serialized_options = b'\302Hi\ng\n\023int64.abs_in.proto2\022\'value must be in absolute value of list\032\'this in rule || this in rule.map(n, -n)'
  _globals['uint32_even_proto2']._loaded_options = None
  _globals['uint32_even_proto2']._serialized_options = b'\302HA\n?\n\022uint32.even.proto2\022\030uint32 value is not even\032\017this % 2u == 0u'
  _globals['uint64_even_proto2']._loaded_options = None
  _globals['uint64_even_proto2']._serialized_options = b'\302HA\n?\n\022uint64.even.proto2\022\030uint64 value is not even\032\017this % 2u == 0u'
  _globals['sint32_even_proto2']._loaded_options = None
  _globals['sint32_even_proto2']._serialized_options = b'\302H?\n=\n\022sint32.even.proto2\022\030sint32 value is not even\032\rthis % 2 == 0'
  _globals['sint64_even_proto2']._loaded_options = None
  _globals['sint64_even_proto2']._serialized_options = b'\302H?\n=\n\022sint64.even.proto2\022\030sint64 value is not even\032\rthis % 2 == 0'
  _globals['fixed32_even_proto2']._loaded_options = None
  _globals['fixed32_even_proto2']._serialized_options = b'\302HC\nA\n\023fixed32.even.proto2\022\031fixed32 value is not even\032\017this % 2u == 0u'
  _globals['fixed64_even_proto2']._loaded_options = None
  _globals['fixed64_even_proto2']._serialized_options = b'\302HC\nA\n\023fixed64.even.proto2\022\031fixed64 value is not even\032\017this % 2u == 0u'
  _globals['sfixed32_even_proto2']._loaded_options = None
  _globals['sfixed32_even_proto2']._serialized_options = b'\302HC\nA\n\024sfixed32.even.proto2\022\032sfixed32 value is not even\032\rthis % 2 == 0'
  _globals['sfixed64_even_proto2']._loaded_options = None
  _globals['sfixed64_even_proto2']._serialized_options = b'\302HC\nA\n\024sfixed64.even.proto2\022\032sfixed64 value is not even\032\rthis % 2 == 0'
  _globals['bool_false_proto2']._loaded_options = None
  _globals['bool_false_proto2']._serialized_options = b'\302H=\n;\n\021bool.false.proto2\022\027bool value is not false\032\rthis == false'
  _globals['string_valid_path_proto2']._loaded_options = None
  _globals['string_valid_path_proto2']._serialized_options = b'\302H\244\001\n\241\001\n\030string.valid_path.proto2\032\204\001!this.matches(\'^([^/.][^/]?|[^/][^/.]|[^/]{3,})(/([^/.][^/]?|[^/][^/.]|[^/]{3,}))*$\') ? \'not a valid path: `%s`\'.format([this]) : \'\''
  _globals['bytes_valid_path_proto2']._loaded_options = None
  _globals['bytes_valid_path_proto2']._serialized_options = b'\302H\253\001\n\250\001\n\027bytes.valid_path.proto2\032\214\001!string(this).matches(\'^([^/.][^/]?|[^/][^/.]|[^/]{3,})(/([^/.][^/]?|[^/][^/.]|[^/]{3,}))*$\') ? \'not a valid path: `%s`\'.format([this]) : \'\''
  _globals['enum_non_zero_proto2']._loaded_options = None
  _globals['enum_non_zero_proto2']._serialized_options = b'\302HD\nB\n\024enum.non_zero.proto2\022\032enum value is not non-zero\032\016int(this) != 0'
  _globals['repeated_at_least_five_proto2']._loaded_options = None
  _globals['repeated_at_least_five_proto2']._serialized_options = b'\302Hi\ng\n\035repeated.at_least_five.proto2\022-repeated field must have at least five values\032\027uint(this.size()) >= 5u'
  _globals['duration_too_long_proto2']._loaded_options = None
  _globals['duration_too_long_proto2']._serialized_options = b'\302H_\n]\n\030duration.too_long.proto2\022(duration can\'t be longer than 10 seconds\032\027this <= duration(\'10s\')'
  _globals['timestamp_in_range_proto2']._loaded_options = None
  _globals['timestamp_in_range_proto2']._serialized_options = b'\302Hk\ni\n\033timestamp.time_range.proto2\022\026timestamp out of range\0322int(this) >= 1049587200 && int(this) <= 1080432000'
  _globals['_PREDEFINEDFLOATRULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDFLOATRULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\010\n\006\315H\000\000\200?'
  _globals['_PREDEFINEDDOUBLERULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDDOUBLERULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\014\022\n\311H\000\000\000\000\000\000\360?'
  _globals['_PREDEFINEDINT32RULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDINT32RULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\016\032\014\310H\376\377\377\377\377\377\377\377\377\001'
  _globals['_PREDEFINEDINT64RULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDINT64RULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\020\"\016\312H\013\010\376\377\377\377\377\377\377\377\377\001'
  _globals['_PREDEFINEDUINT32RULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDUINT32RULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\005*\003\310H\001'
  _globals['_PREDEFINEDUINT64RULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDUINT64RULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\0052\003\310H\001'
  _globals['_PREDEFINEDSINT32RULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDSINT32RULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\005:\003\310H\001'
  _globals['_PREDEFINEDSINT64RULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDSINT64RULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\005B\003\310H\001'
  _globals['_PREDEFINEDFIXED32RULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDFIXED32RULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\005J\003\310H\001'
  _globals['_PREDEFINEDFIXED64RULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDFIXED64RULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\005R\003\310H\001'
  _globals['_PREDEFINEDSFIXED32RULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDSFIXED32RULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\005Z\003\310H\001'
  _globals['_PREDEFINEDSFIXED64RULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDSFIXED64RULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\005b\003\310H\001'
  _globals['_PREDEFINEDBOOLRULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDBOOLRULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\005j\003\310H\001'
  _globals['_PREDEFINEDSTRINGRULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDSTRINGRULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\005r\003\310H\001'
  _globals['_PREDEFINEDBYTESRULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDBYTESRULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\005z\003\310H\001'
  _globals['_PREDEFINEDENUMRULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDENUMRULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\006\202\001\003\310H\001'
  _globals['_PREDEFINEDREPEATEDRULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDREPEATEDRULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\006\222\001\003\310H\001'
  _globals['_PREDEFINEDDURATIONRULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDDURATIONRULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\006\252\001\003\310H\001'
  _globals['_PREDEFINEDTIMESTAMPRULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDTIMESTAMPRULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\006\262\001\003\310H\001'
  _globals['_PREDEFINEDWRAPPEDFLOATRULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDWRAPPEDFLOATRULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\010\n\006\315H\000\000\200?'
  _globals['_PREDEFINEDWRAPPEDDOUBLERULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDWRAPPEDDOUBLERULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\014\022\n\311H\000\000\000\000\000\000\360?'
  _globals['_PREDEFINEDWRAPPEDINT32RULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDWRAPPEDINT32RULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\016\032\014\310H\376\377\377\377\377\377\377\377\377\001'
  _globals['_PREDEFINEDWRAPPEDINT64RULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDWRAPPEDINT64RULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\020\"\016\312H\013\010\376\377\377\377\377\377\377\377\377\001'
  _globals['_PREDEFINEDWRAPPEDUINT32RULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDWRAPPEDUINT32RULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\005*\003\310H\001'
  _globals['_PREDEFINEDWRAPPEDUINT64RULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDWRAPPEDUINT64RULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\0052\003\310H\001'
  _globals['_PREDEFINEDWRAPPEDBOOLRULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDWRAPPEDBOOLRULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\005j\003\310H\001'
  _globals['_PREDEFINEDWRAPPEDSTRINGRULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDWRAPPEDSTRINGRULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\005r\003\310H\001'
  _globals['_PREDEFINEDWRAPPEDBYTESRULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDWRAPPEDBYTESRULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\005z\003\310H\001'
  _globals['_PREDEFINEDREPEATEDWRAPPEDFLOATRULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDREPEATEDWRAPPEDFLOATRULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\r\222\001\n\"\010\n\006\315H\000\000\200?'
  _globals['_PREDEFINEDREPEATEDWRAPPEDDOUBLERULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDREPEATEDWRAPPEDDOUBLERULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\021\222\001\016\"\014\022\n\311H\000\000\000\000\000\000\360?'
  _globals['_PREDEFINEDREPEATEDWRAPPEDINT32RULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDREPEATEDWRAPPEDINT32RULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\023\222\001\020\"\016\032\014\310H\376\377\377\377\377\377\377\377\377\001'
  _globals['_PREDEFINEDREPEATEDWRAPPEDINT64RULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDREPEATEDWRAPPEDINT64RULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\025\222\001\022\"\020\"\016\312H\013\010\376\377\377\377\377\377\377\377\377\001'
  _globals['_PREDEFINEDREPEATEDWRAPPEDUINT32RULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDREPEATEDWRAPPEDUINT32RULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\n\222\001\007\"\005*\003\310H\001'
  _globals['_PREDEFINEDREPEATEDWRAPPEDUINT64RULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDREPEATEDWRAPPEDUINT64RULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\n\222\001\007\"\0052\003\310H\001'
  _globals['_PREDEFINEDREPEATEDWRAPPEDBOOLRULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDREPEATEDWRAPPEDBOOLRULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\n\222\001\007\"\005j\003\310H\001'
  _globals['_PREDEFINEDREPEATEDWRAPPEDSTRINGRULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDREPEATEDWRAPPEDSTRINGRULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\n\222\001\007\"\005r\003\310H\001'
  _globals['_PREDEFINEDREPEATEDWRAPPEDBYTESRULEPROTO2'].fields_by_name['val']._loaded_options = None
  _globals['_PREDEFINEDREPEATEDWRAPPEDBYTESRULEPROTO2'].fields_by_name['val']._serialized_options = b'\272H\n\222\001\007\"\005z\003\310H\001'
  _globals['_PREDEFINEDANDCUSTOMRULEPROTO2_NESTED'].fields_by_name['c']._loaded_options = None
  _globals['_PREDEFINEDANDCUSTOMRULEPROTO2_NESTED'].fields_by_name['c']._serialized_options = b'\272HX:\003\310H\001\272\001P\n(predefined_and_custom_rule_nested_proto2\032$this > 0 ? \'\' : \'c must be positive\''
  _globals['_PREDEFINEDANDCUSTOMRULEPROTO2'].fields_by_name['a']._loaded_options = None
  _globals['_PREDEFINEDANDCUSTOMRULEPROTO2'].fields_by_name['a']._serialized_options = b'\272H`:\003\310H\001\272\001X\n(predefined_and_custom_rule_scalar_proto2\032,this > 24 ? \'\' : \'a must be greater than 24\''
  _globals['_PREDEFINEDANDCUSTOMRULEPROTO2'].fields_by_name['b']._loaded_options = None
  _globals['_PREDEFINEDANDCUSTOMRULEPROTO2'].fields_by_name['b']._serialized_options = b'\272H]\272\001Z\n*predefined_and_custom_rule_embedded_proto2\022\033b.c must be a multiple of 3\032\017this.c % 3 == 0'
  _globals['_STANDARDPREDEFINEDANDCUSTOMRULEPROTO2'].fields_by_name['a']._loaded_options = None
  _globals['_STANDARDPREDEFINEDANDCUSTOMRULEPROTO2'].fields_by_name['a']._serialized_options = b'\272Hk:\005\0208\310H\001\272\001a\n1standard_predefined_and_custom_rule_scalar_proto2\032,this > 24 ? \'\' : \'a must be greater than 24\''
  _globals['_PREDEFINEDFLOATRULEPROTO2']._serialized_start=222
  _globals['_PREDEFINEDFLOATRULEPROTO2']._serialized_end=280
  _globals['_PREDEFINEDDOUBLERULEPROTO2']._serialized_start=282
  _globals['_PREDEFINEDDOUBLERULEPROTO2']._serialized_end=345
  _globals['_PREDEFINEDINT32RULEPROTO2']._serialized_start=347
  _globals['_PREDEFINEDINT32RULEPROTO2']._serialized_end=411
  _globals['_PREDEFINEDINT64RULEPROTO2']._serialized_start=413
  _globals['_PREDEFINEDINT64RULEPROTO2']._serialized_end=479
  _globals['_PREDEFINEDUINT32RULEPROTO2']._serialized_start=481
  _globals['_PREDEFINEDUINT32RULEPROTO2']._serialized_end=537
  _globals['_PREDEFINEDUINT64RULEPROTO2']._serialized_start=539
  _globals['_PREDEFINEDUINT64RULEPROTO2']._serialized_end=595
  _globals['_PREDEFINEDSINT32RULEPROTO2']._serialized_start=597
  _globals['_PREDEFINEDSINT32RULEPROTO2']._serialized_end=653
  _globals['_PREDEFINEDSINT64RULEPROTO2']._serialized_start=655
  _globals['_PREDEFINEDSINT64RULEPROTO2']._serialized_end=711
  _globals['_PREDEFINEDFIXED32RULEPROTO2']._serialized_start=713
  _globals['_PREDEFINEDFIXED32RULEPROTO2']._serialized_end=770
  _globals['_PREDEFINEDFIXED64RULEPROTO2']._serialized_start=772
  _globals['_PREDEFINEDFIXED64RULEPROTO2']._serialized_end=829
  _globals['_PREDEFINEDSFIXED32RULEPROTO2']._serialized_start=831
  _globals['_PREDEFINEDSFIXED32RULEPROTO2']._serialized_end=889
  _globals['_PREDEFINEDSFIXED64RULEPROTO2']._serialized_start=891
  _globals['_PREDEFINEDSFIXED64RULEPROTO2']._serialized_end=949
  _globals['_PREDEFINEDBOOLRULEPROTO2']._serialized_start=951
  _globals['_PREDEFINEDBOOLRULEPROTO2']._serialized_end=1005
  _globals['_PREDEFINEDSTRINGRULEPROTO2']._serialized_start=1007
  _globals['_PREDEFINEDSTRINGRULEPROTO2']._serialized_end=1063
  _globals['_PREDEFINEDBYTESRULEPROTO2']._serialized_start=1065
  _globals['_PREDEFINEDBYTESRULEPROTO2']._serialized_end=1120
  _globals['_PREDEFINEDENUMRULEPROTO2']._serialized_start=1123
  _globals['_PREDEFINEDENUMRULEPROTO2']._serialized_end=1316
  _globals['_PREDEFINEDENUMRULEPROTO2_ENUMPROTO2']._serialized_start=1249
  _globals['_PREDEFINEDENUMRULEPROTO2_ENUMPROTO2']._serialized_end=1316
  _globals['_PREDEFINEDREPEATEDRULEPROTO2']._serialized_start=1318
  _globals['_PREDEFINEDREPEATEDRULEPROTO2']._serialized_end=1377
  _globals['_PREDEFINEDDURATIONRULEPROTO2']._serialized_start=1379
  _globals['_PREDEFINEDDURATIONRULEPROTO2']._serialized_end=1465
  _globals['_PREDEFINEDTIMESTAMPRULEPROTO2']._serialized_start=1467
  _globals['_PREDEFINEDTIMESTAMPRULEPROTO2']._serialized_end=1555
  _globals['_PREDEFINEDWRAPPEDFLOATRULEPROTO2']._serialized_start=1557
  _globals['_PREDEFINEDWRAPPEDFLOATRULEPROTO2']._serialized_end=1651
  _globals['_PREDEFINEDWRAPPEDDOUBLERULEPROTO2']._serialized_start=1653
  _globals['_PREDEFINEDWRAPPEDDOUBLERULEPROTO2']._serialized_end=1753
  _globals['_PREDEFINEDWRAPPEDINT32RULEPROTO2']._serialized_start=1755
  _globals['_PREDEFINEDWRAPPEDINT32RULEPROTO2']._serialized_end=1855
  _globals['_PREDEFINEDWRAPPEDINT64RULEPROTO2']._serialized_start=1857
  _globals['_PREDEFINEDWRAPPEDINT64RULEPROTO2']._serialized_end=1959
  _globals['_PREDEFINEDWRAPPEDUINT32RULEPROTO2']._serialized_start=1961
  _globals['_PREDEFINEDWRAPPEDUINT32RULEPROTO2']._serialized_end=2054
  _globals['_PREDEFINEDWRAPPEDUINT64RULEPROTO2']._serialized_start=2056
  _globals['_PREDEFINEDWRAPPEDUINT64RULEPROTO2']._serialized_end=2149
  _globals['_PREDEFINEDWRAPPEDBOOLRULEPROTO2']._serialized_start=2151
  _globals['_PREDEFINEDWRAPPEDBOOLRULEPROTO2']._serialized_end=2240
  _globals['_PREDEFINEDWRAPPEDSTRINGRULEPROTO2']._serialized_start=2242
  _globals['_PREDEFINEDWRAPPEDSTRINGRULEPROTO2']._serialized_end=2335
  _globals['_PREDEFINEDWRAPPEDBYTESRULEPROTO2']._serialized_start=2337
  _globals['_PREDEFINEDWRAPPEDBYTESRULEPROTO2']._serialized_end=2428
  _globals['_PREDEFINEDREPEATEDWRAPPEDFLOATRULEPROTO2']._serialized_start=2430
  _globals['_PREDEFINEDREPEATEDWRAPPEDFLOATRULEPROTO2']._serialized_end=2537
  _globals['_PREDEFINEDREPEATEDWRAPPEDDOUBLERULEPROTO2']._serialized_start=2539
  _globals['_PREDEFINEDREPEATEDWRAPPEDDOUBLERULEPROTO2']._serialized_end=2652
  _globals['_PREDEFINEDREPEATEDWRAPPEDINT32RULEPROTO2']._serialized_start=2654
  _globals['_PREDEFINEDREPEATEDWRAPPEDINT32RULEPROTO2']._serialized_end=2767
  _globals['_PREDEFINEDREPEATEDWRAPPEDINT64RULEPROTO2']._serialized_start=2769
  _globals['_PREDEFINEDREPEATEDWRAPPEDINT64RULEPROTO2']._serialized_end=2884
  _globals['_PREDEFINEDREPEATEDWRAPPEDUINT32RULEPROTO2']._serialized_start=2886
  _globals['_PREDEFINEDREPEATEDWRAPPEDUINT32RULEPROTO2']._serialized_end=2992
  _globals['_PREDEFINEDREPEATEDWRAPPEDUINT64RULEPROTO2']._serialized_start=2994
  _globals['_PREDEFINEDREPEATEDWRAPPEDUINT64RULEPROTO2']._serialized_end=3100
  _globals['_PREDEFINEDREPEATEDWRAPPEDBOOLRULEPROTO2']._serialized_start=3102
  _globals['_PREDEFINEDREPEATEDWRAPPEDBOOLRULEPROTO2']._serialized_end=3204
  _globals['_PREDEFINEDREPEATEDWRAPPEDSTRINGRULEPROTO2']._serialized_start=3206
  _globals['_PREDEFINEDREPEATEDWRAPPEDSTRINGRULEPROTO2']._serialized_end=3312
  _globals['_PREDEFINEDREPEATEDWRAPPEDBYTESRULEPROTO2']._serialized_start=3314
  _globals['_PREDEFINEDREPEATEDWRAPPEDBYTESRULEPROTO2']._serialized_end=3418
  _globals['_PREDEFINEDANDCUSTOMRULEPROTO2']._serialized_start=3421
  _globals['_PREDEFINEDANDCUSTOMRULEPROTO2']._serialized_end=3867
  _globals['_PREDEFINEDANDCUSTOMRULEPROTO2_NESTED']._serialized_start=3752
  _globals['_PREDEFINEDANDCUSTOMRULEPROTO2_NESTED']._serialized_end=3867
  _globals['_STANDARDPREDEFINEDANDCUSTOMRULEPROTO2']._serialized_start=3870
  _globals['_STANDARDPREDEFINEDANDCUSTOMRULEPROTO2']._serialized_end=4035
# @@protoc_insertion_point(module_scope)
