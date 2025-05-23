# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/google/fhir/proto/stu3/ml_extensions.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.google.fhir.proto import annotations_pb2 as proto_dot_google_dot_fhir_dot_proto_dot_annotations__pb2
from proto.google.fhir.proto.stu3 import datatypes_pb2 as proto_dot_google_dot_fhir_dot_proto_dot_stu3_dot_datatypes__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/google/fhir/proto/stu3/ml_extensions.proto',
  package='google.fhir.stu3.ml',
  syntax='proto3',
  serialized_options=b'\n\027com.google.fhir.stu3.mlP\001\230\306\260\265\007\002',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n0proto/google/fhir/proto/stu3/ml_extensions.proto\x12\x13google.fhir.stu3.ml\x1a)proto/google/fhir/proto/annotations.proto\x1a,proto/google/fhir/proto/stu3/datatypes.proto\"\xa6\n\n\nEventLabel\x12*\n\x02id\x18\x01 \x01(\x0b\x32\x1e.google.fhir.stu3.proto.String\x12\x34\n\textension\x18\x02 \x03(\x0b\x32!.google.fhir.stu3.proto.Extension\x12\x64\n\x07patient\x18\x04 \x01(\x0b\x32!.google.fhir.stu3.proto.ReferenceB0\xf0\xd0\x87\xeb\x04\x01\xf2\xbe\xc0\xa4\x07$extension.exists() != value.exists()\x12^\n\x04type\x18\x05 \x01(\x0b\x32\x1e.google.fhir.stu3.proto.CodingB0\xf0\xd0\x87\xeb\x04\x01\xf2\xbe\xc0\xa4\x07$extension.exists() != value.exists()\x12`\n\nevent_time\x18\x06 \x01(\x0b\x32 .google.fhir.stu3.proto.DateTimeB*\xf2\xbe\xc0\xa4\x07$extension.exists() != value.exists()\x12]\n\x06source\x18\x07 \x01(\x0b\x32!.google.fhir.stu3.proto.ReferenceB*\xf2\xbe\xc0\xa4\x07$extension.exists() != value.exists()\x12`\n\x05label\x18\x08 \x03(\x0b\x32%.google.fhir.stu3.ml.EventLabel.LabelB*\xf2\xbe\xc0\xa4\x07$extension.exists() != value.exists()\x1a\xd7\x04\n\x05Label\x12*\n\x02id\x18\x01 \x01(\x0b\x32\x1e.google.fhir.stu3.proto.String\x12\x64\n\nclass_name\x18\x04 \x01(\x0b\x32\x1e.google.fhir.stu3.proto.CodingB0\xf0\xd0\x87\xeb\x04\x01\xf2\xbe\xc0\xa4\x07$extension.exists() != value.exists()\x12w\n\x0b\x63lass_value\x18\x05 \x01(\x0b\x32\x30.google.fhir.stu3.ml.EventLabel.Label.ClassValueB0\xf0\xd0\x87\xeb\x04\x01\xf2\xbe\xc0\xa4\x07$extension.exists() != value.exists()\x1a\xb6\x02\n\nClassValue\x12\x32\n\x07\x62oolean\x18\x01 \x01(\x0b\x32\x1f.google.fhir.stu3.proto.BooleanH\x00\x12\x32\n\x07\x64\x65\x63imal\x18\x02 \x01(\x0b\x32\x1f.google.fhir.stu3.proto.DecimalH\x00\x12\x32\n\x07integer\x18\x03 \x01(\x0b\x32\x1f.google.fhir.stu3.proto.IntegerH\x00\x12>\n\x0cstring_value\x18\x04 \x01(\x0b\x32\x1e.google.fhir.stu3.proto.StringH\x00R\x06string\x12\x35\n\tdate_time\x18\x05 \x01(\x0b\x32 .google.fhir.stu3.proto.DateTimeH\x00:\x06\xa0\x83\x83\xe8\x06\x01\x42\r\n\x0b\x63lass_valueJ\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04:s\xc0\x9f\xe3\xb6\x05\x02\x9a\xb5\x8e\x93\x06\x31http://hl7.org/fhir/StructureDefinition/Extension\xb2\xfe\xe4\x97\x06\x30https://g.co/fhir/StructureDefinition/eventLabel\"\xd8\x03\n\x0c\x45ventTrigger\x12*\n\x02id\x18\x01 \x01(\x0b\x32\x1e.google.fhir.stu3.proto.String\x12^\n\x04type\x18\x04 \x01(\x0b\x32\x1e.google.fhir.stu3.proto.CodingB0\xf0\xd0\x87\xeb\x04\x01\xf2\xbe\xc0\xa4\x07$extension.exists() != value.exists()\x12\x66\n\nevent_time\x18\x05 \x01(\x0b\x32 .google.fhir.stu3.proto.DateTimeB0\xf0\xd0\x87\xeb\x04\x01\xf2\xbe\xc0\xa4\x07$extension.exists() != value.exists()\x12]\n\x06source\x18\x06 \x01(\x0b\x32!.google.fhir.stu3.proto.ReferenceB*\xf2\xbe\xc0\xa4\x07$extension.exists() != value.exists():u\xc0\x9f\xe3\xb6\x05\x02\x9a\xb5\x8e\x93\x06\x31http://hl7.org/fhir/StructureDefinition/Extension\xb2\xfe\xe4\x97\x06\x32https://g.co/fhir/StructureDefinition/eventTriggerB!\n\x17\x63om.google.fhir.stu3.mlP\x01\x98\xc6\xb0\xb5\x07\x02\x62\x06proto3'
  ,
  dependencies=[proto_dot_google_dot_fhir_dot_proto_dot_annotations__pb2.DESCRIPTOR,proto_dot_google_dot_fhir_dot_proto_dot_stu3_dot_datatypes__pb2.DESCRIPTOR,])




_EVENTLABEL_LABEL_CLASSVALUE = _descriptor.Descriptor(
  name='ClassValue',
  full_name='google.fhir.stu3.ml.EventLabel.Label.ClassValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='boolean', full_name='google.fhir.stu3.ml.EventLabel.Label.ClassValue.boolean', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='decimal', full_name='google.fhir.stu3.ml.EventLabel.Label.ClassValue.decimal', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='integer', full_name='google.fhir.stu3.ml.EventLabel.Label.ClassValue.integer', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='google.fhir.stu3.ml.EventLabel.Label.ClassValue.string_value', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='string', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date_time', full_name='google.fhir.stu3.ml.EventLabel.Label.ClassValue.date_time', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\240\203\203\350\006\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='class_value', full_name='google.fhir.stu3.ml.EventLabel.Label.ClassValue.class_value',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1042,
  serialized_end=1352,
)

_EVENTLABEL_LABEL = _descriptor.Descriptor(
  name='Label',
  full_name='google.fhir.stu3.ml.EventLabel.Label',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.fhir.stu3.ml.EventLabel.Label.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='class_name', full_name='google.fhir.stu3.ml.EventLabel.Label.class_name', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360\320\207\353\004\001\362\276\300\244\007$extension.exists() != value.exists()', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='class_value', full_name='google.fhir.stu3.ml.EventLabel.Label.class_value', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360\320\207\353\004\001\362\276\300\244\007$extension.exists() != value.exists()', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EVENTLABEL_LABEL_CLASSVALUE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=765,
  serialized_end=1364,
)

_EVENTLABEL = _descriptor.Descriptor(
  name='EventLabel',
  full_name='google.fhir.stu3.ml.EventLabel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.fhir.stu3.ml.EventLabel.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extension', full_name='google.fhir.stu3.ml.EventLabel.extension', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='patient', full_name='google.fhir.stu3.ml.EventLabel.patient', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360\320\207\353\004\001\362\276\300\244\007$extension.exists() != value.exists()', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.fhir.stu3.ml.EventLabel.type', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360\320\207\353\004\001\362\276\300\244\007$extension.exists() != value.exists()', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event_time', full_name='google.fhir.stu3.ml.EventLabel.event_time', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\276\300\244\007$extension.exists() != value.exists()', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='google.fhir.stu3.ml.EventLabel.source', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\276\300\244\007$extension.exists() != value.exists()', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='google.fhir.stu3.ml.EventLabel.label', index=6,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\276\300\244\007$extension.exists() != value.exists()', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EVENTLABEL_LABEL, ],
  enum_types=[
  ],
  serialized_options=b'\300\237\343\266\005\002\232\265\216\223\0061http://hl7.org/fhir/StructureDefinition/Extension\262\376\344\227\0060https://g.co/fhir/StructureDefinition/eventLabel',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=163,
  serialized_end=1481,
)


_EVENTTRIGGER = _descriptor.Descriptor(
  name='EventTrigger',
  full_name='google.fhir.stu3.ml.EventTrigger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.fhir.stu3.ml.EventTrigger.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.fhir.stu3.ml.EventTrigger.type', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360\320\207\353\004\001\362\276\300\244\007$extension.exists() != value.exists()', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event_time', full_name='google.fhir.stu3.ml.EventTrigger.event_time', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360\320\207\353\004\001\362\276\300\244\007$extension.exists() != value.exists()', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='google.fhir.stu3.ml.EventTrigger.source', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\276\300\244\007$extension.exists() != value.exists()', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\300\237\343\266\005\002\232\265\216\223\0061http://hl7.org/fhir/StructureDefinition/Extension\262\376\344\227\0062https://g.co/fhir/StructureDefinition/eventTrigger',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1484,
  serialized_end=1956,
)

_EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['boolean'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_stu3_dot_datatypes__pb2._BOOLEAN
_EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['decimal'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_stu3_dot_datatypes__pb2._DECIMAL
_EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['integer'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_stu3_dot_datatypes__pb2._INTEGER
_EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['string_value'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_stu3_dot_datatypes__pb2._STRING
_EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['date_time'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_stu3_dot_datatypes__pb2._DATETIME
_EVENTLABEL_LABEL_CLASSVALUE.containing_type = _EVENTLABEL_LABEL
_EVENTLABEL_LABEL_CLASSVALUE.oneofs_by_name['class_value'].fields.append(
  _EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['boolean'])
_EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['boolean'].containing_oneof = _EVENTLABEL_LABEL_CLASSVALUE.oneofs_by_name['class_value']
_EVENTLABEL_LABEL_CLASSVALUE.oneofs_by_name['class_value'].fields.append(
  _EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['decimal'])
_EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['decimal'].containing_oneof = _EVENTLABEL_LABEL_CLASSVALUE.oneofs_by_name['class_value']
_EVENTLABEL_LABEL_CLASSVALUE.oneofs_by_name['class_value'].fields.append(
  _EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['integer'])
_EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['integer'].containing_oneof = _EVENTLABEL_LABEL_CLASSVALUE.oneofs_by_name['class_value']
_EVENTLABEL_LABEL_CLASSVALUE.oneofs_by_name['class_value'].fields.append(
  _EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['string_value'])
_EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['string_value'].containing_oneof = _EVENTLABEL_LABEL_CLASSVALUE.oneofs_by_name['class_value']
_EVENTLABEL_LABEL_CLASSVALUE.oneofs_by_name['class_value'].fields.append(
  _EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['date_time'])
_EVENTLABEL_LABEL_CLASSVALUE.fields_by_name['date_time'].containing_oneof = _EVENTLABEL_LABEL_CLASSVALUE.oneofs_by_name['class_value']
_EVENTLABEL_LABEL.fields_by_name['id'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_stu3_dot_datatypes__pb2._STRING
_EVENTLABEL_LABEL.fields_by_name['class_name'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_stu3_dot_datatypes__pb2._CODING
_EVENTLABEL_LABEL.fields_by_name['class_value'].message_type = _EVENTLABEL_LABEL_CLASSVALUE
_EVENTLABEL_LABEL.containing_type = _EVENTLABEL
_EVENTLABEL.fields_by_name['id'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_stu3_dot_datatypes__pb2._STRING
_EVENTLABEL.fields_by_name['extension'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_stu3_dot_datatypes__pb2._EXTENSION
_EVENTLABEL.fields_by_name['patient'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_stu3_dot_datatypes__pb2._REFERENCE
_EVENTLABEL.fields_by_name['type'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_stu3_dot_datatypes__pb2._CODING
_EVENTLABEL.fields_by_name['event_time'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_stu3_dot_datatypes__pb2._DATETIME
_EVENTLABEL.fields_by_name['source'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_stu3_dot_datatypes__pb2._REFERENCE
_EVENTLABEL.fields_by_name['label'].message_type = _EVENTLABEL_LABEL
_EVENTTRIGGER.fields_by_name['id'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_stu3_dot_datatypes__pb2._STRING
_EVENTTRIGGER.fields_by_name['type'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_stu3_dot_datatypes__pb2._CODING
_EVENTTRIGGER.fields_by_name['event_time'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_stu3_dot_datatypes__pb2._DATETIME
_EVENTTRIGGER.fields_by_name['source'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_stu3_dot_datatypes__pb2._REFERENCE
DESCRIPTOR.message_types_by_name['EventLabel'] = _EVENTLABEL
DESCRIPTOR.message_types_by_name['EventTrigger'] = _EVENTTRIGGER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventLabel = _reflection.GeneratedProtocolMessageType('EventLabel', (_message.Message,), {

  'Label' : _reflection.GeneratedProtocolMessageType('Label', (_message.Message,), {

    'ClassValue' : _reflection.GeneratedProtocolMessageType('ClassValue', (_message.Message,), {
      'DESCRIPTOR' : _EVENTLABEL_LABEL_CLASSVALUE,
      '__module__' : 'proto.google.fhir.proto.stu3.ml_extensions_pb2'
      # @@protoc_insertion_point(class_scope:google.fhir.stu3.ml.EventLabel.Label.ClassValue)
      })
    ,
    'DESCRIPTOR' : _EVENTLABEL_LABEL,
    '__module__' : 'proto.google.fhir.proto.stu3.ml_extensions_pb2'
    # @@protoc_insertion_point(class_scope:google.fhir.stu3.ml.EventLabel.Label)
    })
  ,
  'DESCRIPTOR' : _EVENTLABEL,
  '__module__' : 'proto.google.fhir.proto.stu3.ml_extensions_pb2'
  # @@protoc_insertion_point(class_scope:google.fhir.stu3.ml.EventLabel)
  })
_sym_db.RegisterMessage(EventLabel)
_sym_db.RegisterMessage(EventLabel.Label)
_sym_db.RegisterMessage(EventLabel.Label.ClassValue)

EventTrigger = _reflection.GeneratedProtocolMessageType('EventTrigger', (_message.Message,), {
  'DESCRIPTOR' : _EVENTTRIGGER,
  '__module__' : 'proto.google.fhir.proto.stu3.ml_extensions_pb2'
  # @@protoc_insertion_point(class_scope:google.fhir.stu3.ml.EventTrigger)
  })
_sym_db.RegisterMessage(EventTrigger)


DESCRIPTOR._options = None
_EVENTLABEL_LABEL_CLASSVALUE._options = None
_EVENTLABEL_LABEL.fields_by_name['class_name']._options = None
_EVENTLABEL_LABEL.fields_by_name['class_value']._options = None
_EVENTLABEL.fields_by_name['patient']._options = None
_EVENTLABEL.fields_by_name['type']._options = None
_EVENTLABEL.fields_by_name['event_time']._options = None
_EVENTLABEL.fields_by_name['source']._options = None
_EVENTLABEL.fields_by_name['label']._options = None
_EVENTLABEL._options = None
_EVENTTRIGGER.fields_by_name['type']._options = None
_EVENTTRIGGER.fields_by_name['event_time']._options = None
_EVENTTRIGGER.fields_by_name['source']._options = None
_EVENTTRIGGER._options = None
# @@protoc_insertion_point(module_scope)
