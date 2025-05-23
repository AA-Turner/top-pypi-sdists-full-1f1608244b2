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
# source: buf/validate/conformance/cases/repeated.proto
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
    'buf/validate/conformance/cases/repeated.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate.conformance.cases.other_package import embed_pb2 as buf_dot_validate_dot_conformance_dot_cases_dot_other__package_dot_embed__pb2
from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-buf/validate/conformance/cases/repeated.proto\x12\x1e\x62uf.validate.conformance.cases\x1a\x38\x62uf/validate/conformance/cases/other_package/embed.proto\x1a\x1b\x62uf/validate/validate.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\"\"\n\x05\x45mbed\x12\x19\n\x03val\x18\x01 \x01(\x03\x42\x07\xbaH\x04\"\x02 \x00R\x03val\" \n\x0cRepeatedNone\x12\x10\n\x03val\x18\x01 \x03(\x03R\x03val\"L\n\x11RepeatedEmbedNone\x12\x37\n\x03val\x18\x01 \x03(\x0b\x32%.buf.validate.conformance.cases.EmbedR\x03val\"f\n\x1dRepeatedEmbedCrossPackageNone\x12\x45\n\x03val\x18\x01 \x03(\x0b\x32\x33.buf.validate.conformance.cases.other_package.EmbedR\x03val\"P\n\x0bRepeatedMin\x12\x41\n\x03val\x18\x01 \x03(\x0b\x32%.buf.validate.conformance.cases.EmbedB\x08\xbaH\x05\x92\x01\x02\x08\x02R\x03val\")\n\x0bRepeatedMax\x12\x1a\n\x03val\x18\x01 \x03(\x01\x42\x08\xbaH\x05\x92\x01\x02\x10\x03R\x03val\".\n\x0eRepeatedMinMax\x12\x1c\n\x03val\x18\x01 \x03(\x0f\x42\n\xbaH\x07\x92\x01\x04\x08\x02\x10\x04R\x03val\"-\n\rRepeatedExact\x12\x1c\n\x03val\x18\x01 \x03(\rB\n\xbaH\x07\x92\x01\x04\x08\x03\x10\x03R\x03val\",\n\x0eRepeatedUnique\x12\x1a\n\x03val\x18\x01 \x03(\tB\x08\xbaH\x05\x92\x01\x02\x18\x01R\x03val\"/\n\x11RepeatedNotUnique\x12\x1a\n\x03val\x18\x01 \x03(\tB\x08\xbaH\x05\x92\x01\x02\x18\x00R\x03val\"H\n\x16RepeatedMultipleUnique\x12\x16\n\x01\x61\x18\x01 \x03(\tB\x08\xbaH\x05\x92\x01\x02\x18\x01R\x01\x61\x12\x16\n\x01\x62\x18\x02 \x03(\x05\x42\x08\xbaH\x05\x92\x01\x02\x18\x01R\x01\x62\"5\n\x10RepeatedItemRule\x12!\n\x03val\x18\x01 \x03(\x02\x42\x0f\xbaH\x0c\x92\x01\t\"\x07\n\x05%\x00\x00\x00\x00R\x03val\"D\n\x13RepeatedItemPattern\x12-\n\x03val\x18\x01 \x03(\tB\x1b\xbaH\x18\x92\x01\x15\"\x13r\x11\x32\x0f(?i)^[a-z0-9]+$R\x03val\"Y\n\x11RepeatedEmbedSkip\x12\x44\n\x03val\x18\x01 \x03(\x0b\x32%.buf.validate.conformance.cases.EmbedB\x0b\xbaH\x08\x92\x01\x05\"\x03\xd8\x01\x03R\x03val\"8\n\x0eRepeatedItemIn\x12&\n\x03val\x18\x01 \x03(\tB\x14\xbaH\x11\x92\x01\x0e\"\x0cr\nR\x03\x66ooR\x03\x62\x61rR\x03val\";\n\x11RepeatedItemNotIn\x12&\n\x03val\x18\x01 \x03(\tB\x14\xbaH\x11\x92\x01\x0e\"\x0cr\nZ\x03\x66ooZ\x03\x62\x61rR\x03val\"Y\n\x0eRepeatedEnumIn\x12G\n\x03val\x18\x01 \x03(\x0e\x32&.buf.validate.conformance.cases.AnEnumB\r\xbaH\n\x92\x01\x07\"\x05\x82\x01\x02\x18\x00R\x03val\"\\\n\x11RepeatedEnumNotIn\x12G\n\x03val\x18\x01 \x03(\x0e\x32&.buf.validate.conformance.cases.AnEnumB\r\xbaH\n\x92\x01\x07\"\x05\x82\x01\x02 \x00R\x03val\"\xdf\x01\n\x16RepeatedEmbeddedEnumIn\x12\x65\n\x03val\x18\x01 \x03(\x0e\x32\x44.buf.validate.conformance.cases.RepeatedEmbeddedEnumIn.AnotherInEnumB\r\xbaH\n\x92\x01\x07\"\x05\x82\x01\x02\x18\x00R\x03val\"^\n\rAnotherInEnum\x12\x1f\n\x1b\x41NOTHER_IN_ENUM_UNSPECIFIED\x10\x00\x12\x15\n\x11\x41NOTHER_IN_ENUM_A\x10\x01\x12\x15\n\x11\x41NOTHER_IN_ENUM_B\x10\x02\"\xf7\x01\n\x19RepeatedEmbeddedEnumNotIn\x12k\n\x03val\x18\x01 \x03(\x0e\x32J.buf.validate.conformance.cases.RepeatedEmbeddedEnumNotIn.AnotherNotInEnumB\r\xbaH\n\x92\x01\x07\"\x05\x82\x01\x02 \x00R\x03val\"m\n\x10\x41notherNotInEnum\x12#\n\x1f\x41NOTHER_NOT_IN_ENUM_UNSPECIFIED\x10\x00\x12\x19\n\x15\x41NOTHER_NOT_IN_ENUM_A\x10\x01\x12\x19\n\x15\x41NOTHER_NOT_IN_ENUM_B\x10\x02\"r\n\rRepeatedAnyIn\x12\x61\n\x03val\x18\x01 \x03(\x0b\x32\x14.google.protobuf.AnyB9\xbaH6\x92\x01\x33\"1\xa2\x01.\x12,type.googleapis.com/google.protobuf.DurationR\x03val\"v\n\x10RepeatedAnyNotIn\x12\x62\n\x03val\x18\x01 \x03(\x0b\x32\x14.google.protobuf.AnyB:\xbaH7\x92\x01\x34\"2\xa2\x01/\x1a-type.googleapis.com/google.protobuf.TimestampR\x03val\":\n\x15RepeatedMinAndItemLen\x12!\n\x03val\x18\x01 \x03(\tB\x0f\xbaH\x0c\x92\x01\t\x08\x01\"\x05r\x03\x98\x01\x03R\x03val\"8\n\x18RepeatedMinAndMaxItemLen\x12\x1c\n\x03val\x18\x01 \x03(\tB\n\xbaH\x07\x92\x01\x04\x08\x01\x10\x03R\x03val\"R\n\x10RepeatedDuration\x12>\n\x03val\x18\x01 \x03(\x0b\x32\x19.google.protobuf.DurationB\x11\xbaH\x0e\x92\x01\x0b\"\t\xaa\x01\x06\x32\x04\x10\xc0\x84=R\x03val\"6\n\x13RepeatedExactIgnore\x12\x1f\n\x03val\x18\x01 \x03(\rB\r\xbaH\n\x92\x01\x04\x08\x03\x10\x03\xd8\x01\x01R\x03val*?\n\x06\x41nEnum\x12\x17\n\x13\x41N_ENUM_UNSPECIFIED\x10\x00\x12\r\n\tAN_ENUM_X\x10\x01\x12\r\n\tAN_ENUM_Y\x10\x02\x42\xcf\x01\n\"com.buf.validate.conformance.casesB\rRepeatedProtoP\x01\xa2\x02\x04\x42VCC\xaa\x02\x1e\x42uf.Validate.Conformance.Cases\xca\x02\x1e\x42uf\\Validate\\Conformance\\Cases\xe2\x02*Buf\\Validate\\Conformance\\Cases\\GPBMetadata\xea\x02!Buf::Validate::Conformance::Casesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.conformance.cases.repeated_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.buf.validate.conformance.casesB\rRepeatedProtoP\001\242\002\004BVCC\252\002\036Buf.Validate.Conformance.Cases\312\002\036Buf\\Validate\\Conformance\\Cases\342\002*Buf\\Validate\\Conformance\\Cases\\GPBMetadata\352\002!Buf::Validate::Conformance::Cases'
  _globals['_EMBED'].fields_by_name['val']._loaded_options = None
  _globals['_EMBED'].fields_by_name['val']._serialized_options = b'\272H\004\"\002 \000'
  _globals['_REPEATEDMIN'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDMIN'].fields_by_name['val']._serialized_options = b'\272H\005\222\001\002\010\002'
  _globals['_REPEATEDMAX'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDMAX'].fields_by_name['val']._serialized_options = b'\272H\005\222\001\002\020\003'
  _globals['_REPEATEDMINMAX'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDMINMAX'].fields_by_name['val']._serialized_options = b'\272H\007\222\001\004\010\002\020\004'
  _globals['_REPEATEDEXACT'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDEXACT'].fields_by_name['val']._serialized_options = b'\272H\007\222\001\004\010\003\020\003'
  _globals['_REPEATEDUNIQUE'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDUNIQUE'].fields_by_name['val']._serialized_options = b'\272H\005\222\001\002\030\001'
  _globals['_REPEATEDNOTUNIQUE'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDNOTUNIQUE'].fields_by_name['val']._serialized_options = b'\272H\005\222\001\002\030\000'
  _globals['_REPEATEDMULTIPLEUNIQUE'].fields_by_name['a']._loaded_options = None
  _globals['_REPEATEDMULTIPLEUNIQUE'].fields_by_name['a']._serialized_options = b'\272H\005\222\001\002\030\001'
  _globals['_REPEATEDMULTIPLEUNIQUE'].fields_by_name['b']._loaded_options = None
  _globals['_REPEATEDMULTIPLEUNIQUE'].fields_by_name['b']._serialized_options = b'\272H\005\222\001\002\030\001'
  _globals['_REPEATEDITEMRULE'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDITEMRULE'].fields_by_name['val']._serialized_options = b'\272H\014\222\001\t\"\007\n\005%\000\000\000\000'
  _globals['_REPEATEDITEMPATTERN'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDITEMPATTERN'].fields_by_name['val']._serialized_options = b'\272H\030\222\001\025\"\023r\0212\017(?i)^[a-z0-9]+$'
  _globals['_REPEATEDEMBEDSKIP'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDEMBEDSKIP'].fields_by_name['val']._serialized_options = b'\272H\010\222\001\005\"\003\330\001\003'
  _globals['_REPEATEDITEMIN'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDITEMIN'].fields_by_name['val']._serialized_options = b'\272H\021\222\001\016\"\014r\nR\003fooR\003bar'
  _globals['_REPEATEDITEMNOTIN'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDITEMNOTIN'].fields_by_name['val']._serialized_options = b'\272H\021\222\001\016\"\014r\nZ\003fooZ\003bar'
  _globals['_REPEATEDENUMIN'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDENUMIN'].fields_by_name['val']._serialized_options = b'\272H\n\222\001\007\"\005\202\001\002\030\000'
  _globals['_REPEATEDENUMNOTIN'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDENUMNOTIN'].fields_by_name['val']._serialized_options = b'\272H\n\222\001\007\"\005\202\001\002 \000'
  _globals['_REPEATEDEMBEDDEDENUMIN'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDEMBEDDEDENUMIN'].fields_by_name['val']._serialized_options = b'\272H\n\222\001\007\"\005\202\001\002\030\000'
  _globals['_REPEATEDEMBEDDEDENUMNOTIN'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDEMBEDDEDENUMNOTIN'].fields_by_name['val']._serialized_options = b'\272H\n\222\001\007\"\005\202\001\002 \000'
  _globals['_REPEATEDANYIN'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDANYIN'].fields_by_name['val']._serialized_options = b'\272H6\222\0013\"1\242\001.\022,type.googleapis.com/google.protobuf.Duration'
  _globals['_REPEATEDANYNOTIN'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDANYNOTIN'].fields_by_name['val']._serialized_options = b'\272H7\222\0014\"2\242\001/\032-type.googleapis.com/google.protobuf.Timestamp'
  _globals['_REPEATEDMINANDITEMLEN'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDMINANDITEMLEN'].fields_by_name['val']._serialized_options = b'\272H\014\222\001\t\010\001\"\005r\003\230\001\003'
  _globals['_REPEATEDMINANDMAXITEMLEN'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDMINANDMAXITEMLEN'].fields_by_name['val']._serialized_options = b'\272H\007\222\001\004\010\001\020\003'
  _globals['_REPEATEDDURATION'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDDURATION'].fields_by_name['val']._serialized_options = b'\272H\016\222\001\013\"\t\252\001\0062\004\020\300\204='
  _globals['_REPEATEDEXACTIGNORE'].fields_by_name['val']._loaded_options = None
  _globals['_REPEATEDEXACTIGNORE'].fields_by_name['val']._serialized_options = b'\272H\n\222\001\004\010\003\020\003\330\001\001'
  _globals['_ANENUM']._serialized_start=2358
  _globals['_ANENUM']._serialized_end=2421
  _globals['_EMBED']._serialized_start=227
  _globals['_EMBED']._serialized_end=261
  _globals['_REPEATEDNONE']._serialized_start=263
  _globals['_REPEATEDNONE']._serialized_end=295
  _globals['_REPEATEDEMBEDNONE']._serialized_start=297
  _globals['_REPEATEDEMBEDNONE']._serialized_end=373
  _globals['_REPEATEDEMBEDCROSSPACKAGENONE']._serialized_start=375
  _globals['_REPEATEDEMBEDCROSSPACKAGENONE']._serialized_end=477
  _globals['_REPEATEDMIN']._serialized_start=479
  _globals['_REPEATEDMIN']._serialized_end=559
  _globals['_REPEATEDMAX']._serialized_start=561
  _globals['_REPEATEDMAX']._serialized_end=602
  _globals['_REPEATEDMINMAX']._serialized_start=604
  _globals['_REPEATEDMINMAX']._serialized_end=650
  _globals['_REPEATEDEXACT']._serialized_start=652
  _globals['_REPEATEDEXACT']._serialized_end=697
  _globals['_REPEATEDUNIQUE']._serialized_start=699
  _globals['_REPEATEDUNIQUE']._serialized_end=743
  _globals['_REPEATEDNOTUNIQUE']._serialized_start=745
  _globals['_REPEATEDNOTUNIQUE']._serialized_end=792
  _globals['_REPEATEDMULTIPLEUNIQUE']._serialized_start=794
  _globals['_REPEATEDMULTIPLEUNIQUE']._serialized_end=866
  _globals['_REPEATEDITEMRULE']._serialized_start=868
  _globals['_REPEATEDITEMRULE']._serialized_end=921
  _globals['_REPEATEDITEMPATTERN']._serialized_start=923
  _globals['_REPEATEDITEMPATTERN']._serialized_end=991
  _globals['_REPEATEDEMBEDSKIP']._serialized_start=993
  _globals['_REPEATEDEMBEDSKIP']._serialized_end=1082
  _globals['_REPEATEDITEMIN']._serialized_start=1084
  _globals['_REPEATEDITEMIN']._serialized_end=1140
  _globals['_REPEATEDITEMNOTIN']._serialized_start=1142
  _globals['_REPEATEDITEMNOTIN']._serialized_end=1201
  _globals['_REPEATEDENUMIN']._serialized_start=1203
  _globals['_REPEATEDENUMIN']._serialized_end=1292
  _globals['_REPEATEDENUMNOTIN']._serialized_start=1294
  _globals['_REPEATEDENUMNOTIN']._serialized_end=1386
  _globals['_REPEATEDEMBEDDEDENUMIN']._serialized_start=1389
  _globals['_REPEATEDEMBEDDEDENUMIN']._serialized_end=1612
  _globals['_REPEATEDEMBEDDEDENUMIN_ANOTHERINENUM']._serialized_start=1518
  _globals['_REPEATEDEMBEDDEDENUMIN_ANOTHERINENUM']._serialized_end=1612
  _globals['_REPEATEDEMBEDDEDENUMNOTIN']._serialized_start=1615
  _globals['_REPEATEDEMBEDDEDENUMNOTIN']._serialized_end=1862
  _globals['_REPEATEDEMBEDDEDENUMNOTIN_ANOTHERNOTINENUM']._serialized_start=1753
  _globals['_REPEATEDEMBEDDEDENUMNOTIN_ANOTHERNOTINENUM']._serialized_end=1862
  _globals['_REPEATEDANYIN']._serialized_start=1864
  _globals['_REPEATEDANYIN']._serialized_end=1978
  _globals['_REPEATEDANYNOTIN']._serialized_start=1980
  _globals['_REPEATEDANYNOTIN']._serialized_end=2098
  _globals['_REPEATEDMINANDITEMLEN']._serialized_start=2100
  _globals['_REPEATEDMINANDITEMLEN']._serialized_end=2158
  _globals['_REPEATEDMINANDMAXITEMLEN']._serialized_start=2160
  _globals['_REPEATEDMINANDMAXITEMLEN']._serialized_end=2216
  _globals['_REPEATEDDURATION']._serialized_start=2218
  _globals['_REPEATEDDURATION']._serialized_end=2300
  _globals['_REPEATEDEXACTIGNORE']._serialized_start=2302
  _globals['_REPEATEDEXACTIGNORE']._serialized_end=2356
# @@protoc_insertion_point(module_scope)
