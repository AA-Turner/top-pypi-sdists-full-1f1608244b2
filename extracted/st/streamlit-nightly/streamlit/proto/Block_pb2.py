# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/Block.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from streamlit.proto import WidthConfig_pb2 as streamlit_dot_proto_dot_WidthConfig__pb2
from streamlit.proto import HeightConfig_pb2 as streamlit_dot_proto_dot_HeightConfig__pb2
from streamlit.proto import GapSize_pb2 as streamlit_dot_proto_dot_GapSize__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bstreamlit/proto/Block.proto\x1a!streamlit/proto/WidthConfig.proto\x1a\"streamlit/proto/HeightConfig.proto\x1a\x1dstreamlit/proto/GapSize.proto\"\xe3\r\n\x05\x42lock\x12#\n\x08vertical\x18\x01 \x01(\x0b\x32\x0f.Block.VerticalH\x00\x12\'\n\nhorizontal\x18\x02 \x01(\x0b\x32\x11.Block.HorizontalH\x00\x12\x1f\n\x06\x63olumn\x18\x03 \x01(\x0b\x32\r.Block.ColumnH\x00\x12\'\n\nexpandable\x18\x04 \x01(\x0b\x32\x11.Block.ExpandableH\x00\x12\x1b\n\x04\x66orm\x18\x05 \x01(\x0b\x32\x0b.Block.FormH\x00\x12,\n\rtab_container\x18\x06 \x01(\x0b\x32\x13.Block.TabContainerH\x00\x12\x19\n\x03tab\x18\x07 \x01(\x0b\x32\n.Block.TabH\x00\x12*\n\x0c\x63hat_message\x18\t \x01(\x0b\x32\x12.Block.ChatMessageH\x00\x12!\n\x07popover\x18\n \x01(\x0b\x32\x0e.Block.PopoverH\x00\x12\x1f\n\x06\x64ialog\x18\x0b \x01(\x0b\x32\r.Block.DialogH\x00\x12.\n\x0e\x66lex_container\x18\r \x01(\x0b\x32\x14.Block.FlexContainerH\x00\x12\x13\n\x0b\x61llow_empty\x18\x08 \x01(\x08\x12\x0f\n\x02id\x18\x0c \x01(\tH\x01\x88\x01\x01\x12\x33\n\rheight_config\x18\x0e \x01(\x0b\x32\x17.streamlit.HeightConfigH\x02\x88\x01\x01\x12\x31\n\x0cwidth_config\x18\x0f \x01(\x0b\x32\x16.streamlit.WidthConfigH\x03\x88\x01\x01\x1a*\n\x08Vertical\x12\x0e\n\x06\x62order\x18\x01 \x01(\x08\x12\x0e\n\x06height\x18\x02 \x01(\r\x1a\x19\n\nHorizontal\x12\x0b\n\x03gap\x18\x01 \x01(\t\x1a\xdd\x01\n\rFlexContainer\x12\x0e\n\x06\x62order\x18\x01 \x01(\x08\x12(\n\ngap_config\x18\x02 \x01(\x0b\x32\x14.streamlit.GapConfig\x12\r\n\x05scale\x18\x03 \x01(\x02\x12\x31\n\tdirection\x18\x04 \x01(\x0e\x32\x1e.Block.FlexContainer.Direction\x12\x0c\n\x04wrap\x18\x05 \x01(\x08\"B\n\tDirection\x12\x17\n\x13\x44IRECTION_UNDEFINED\x10\x00\x12\x0c\n\x08VERTICAL\x10\x01\x12\x0e\n\nHORIZONTAL\x10\x02\x1a\xef\x01\n\x06\x43olumn\x12\x0e\n\x06weight\x18\x01 \x01(\x01\x12\x0f\n\x03gap\x18\x02 \x01(\tB\x02\x18\x01\x12;\n\x12vertical_alignment\x18\x03 \x01(\x0e\x32\x1f.Block.Column.VerticalAlignment\x12\x13\n\x0bshow_border\x18\x04 \x01(\x08\x12-\n\ngap_config\x18\x05 \x01(\x0b\x32\x14.streamlit.GapConfigH\x00\x88\x01\x01\"4\n\x11VerticalAlignment\x12\x07\n\x03TOP\x10\x00\x12\n\n\x06\x43\x45NTER\x10\x01\x12\n\n\x06\x42OTTOM\x10\x02\x42\r\n\x0b_gap_config\x1aM\n\nExpandable\x12\r\n\x05label\x18\x01 \x01(\t\x12\x15\n\x08\x65xpanded\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12\x0c\n\x04icon\x18\x03 \x01(\tB\x0b\n\t_expanded\x1a\x9d\x01\n\x06\x44ialog\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64ismissible\x18\x02 \x01(\x08\x12(\n\x05width\x18\x03 \x01(\x0e\x32\x19.Block.Dialog.DialogWidth\x12\x14\n\x07is_open\x18\x04 \x01(\x08H\x00\x88\x01\x01\"#\n\x0b\x44ialogWidth\x12\t\n\x05SMALL\x10\x00\x12\t\n\x05LARGE\x10\x01\x42\n\n\x08_is_open\x1aY\n\x04\x46orm\x12\x0f\n\x07\x66orm_id\x18\x01 \x01(\t\x12\x17\n\x0f\x63lear_on_submit\x18\x02 \x01(\x08\x12\x0e\n\x06\x62order\x18\x03 \x01(\x08\x12\x17\n\x0f\x65nter_to_submit\x18\x04 \x01(\x08\x1a\x0e\n\x0cTabContainer\x1a\x14\n\x03Tab\x12\r\n\x05label\x18\x01 \x01(\t\x1a\x63\n\x07Popover\x12\r\n\x05label\x18\x01 \x01(\t\x12\x1b\n\x13use_container_width\x18\x02 \x01(\x08\x12\x0c\n\x04help\x18\x03 \x01(\t\x12\x10\n\x08\x64isabled\x18\x04 \x01(\x08\x12\x0c\n\x04icon\x18\x05 \x01(\t\x1a\x8d\x01\n\x0b\x43hatMessage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x02 \x01(\t\x12\x32\n\x0b\x61vatar_type\x18\x03 \x01(\x0e\x32\x1d.Block.ChatMessage.AvatarType\",\n\nAvatarType\x12\t\n\x05IMAGE\x10\x00\x12\t\n\x05\x45MOJI\x10\x01\x12\x08\n\x04ICON\x10\x02\x42\x06\n\x04typeB\x05\n\x03_idB\x10\n\x0e_height_configB\x0f\n\r_width_configB*\n\x1c\x63om.snowflake.apps.streamlitB\nBlockProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'streamlit.proto.Block_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.snowflake.apps.streamlitB\nBlockProto'
  _globals['_BLOCK_COLUMN'].fields_by_name['gap']._loaded_options = None
  _globals['_BLOCK_COLUMN'].fields_by_name['gap']._serialized_options = b'\030\001'
  _globals['_BLOCK']._serialized_start=134
  _globals['_BLOCK']._serialized_end=1897
  _globals['_BLOCK_VERTICAL']._serialized_start=699
  _globals['_BLOCK_VERTICAL']._serialized_end=741
  _globals['_BLOCK_HORIZONTAL']._serialized_start=743
  _globals['_BLOCK_HORIZONTAL']._serialized_end=768
  _globals['_BLOCK_FLEXCONTAINER']._serialized_start=771
  _globals['_BLOCK_FLEXCONTAINER']._serialized_end=992
  _globals['_BLOCK_FLEXCONTAINER_DIRECTION']._serialized_start=926
  _globals['_BLOCK_FLEXCONTAINER_DIRECTION']._serialized_end=992
  _globals['_BLOCK_COLUMN']._serialized_start=995
  _globals['_BLOCK_COLUMN']._serialized_end=1234
  _globals['_BLOCK_COLUMN_VERTICALALIGNMENT']._serialized_start=1167
  _globals['_BLOCK_COLUMN_VERTICALALIGNMENT']._serialized_end=1219
  _globals['_BLOCK_EXPANDABLE']._serialized_start=1236
  _globals['_BLOCK_EXPANDABLE']._serialized_end=1313
  _globals['_BLOCK_DIALOG']._serialized_start=1316
  _globals['_BLOCK_DIALOG']._serialized_end=1473
  _globals['_BLOCK_DIALOG_DIALOGWIDTH']._serialized_start=1426
  _globals['_BLOCK_DIALOG_DIALOGWIDTH']._serialized_end=1461
  _globals['_BLOCK_FORM']._serialized_start=1475
  _globals['_BLOCK_FORM']._serialized_end=1564
  _globals['_BLOCK_TABCONTAINER']._serialized_start=1566
  _globals['_BLOCK_TABCONTAINER']._serialized_end=1580
  _globals['_BLOCK_TAB']._serialized_start=1582
  _globals['_BLOCK_TAB']._serialized_end=1602
  _globals['_BLOCK_POPOVER']._serialized_start=1604
  _globals['_BLOCK_POPOVER']._serialized_end=1703
  _globals['_BLOCK_CHATMESSAGE']._serialized_start=1706
  _globals['_BLOCK_CHATMESSAGE']._serialized_end=1847
  _globals['_BLOCK_CHATMESSAGE_AVATARTYPE']._serialized_start=1803
  _globals['_BLOCK_CHATMESSAGE_AVATARTYPE']._serialized_end=1847
# @@protoc_insertion_point(module_scope)
