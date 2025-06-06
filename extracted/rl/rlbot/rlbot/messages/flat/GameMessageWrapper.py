# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flat

import flatbuffers

class GameMessageWrapper(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsGameMessageWrapper(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GameMessageWrapper()
        x.Init(buf, n + offset)
        return x

    # GameMessageWrapper
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # GameMessageWrapper
    def MessageType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # GameMessageWrapper
    def Message(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

def GameMessageWrapperStart(builder): builder.StartObject(2)
def GameMessageWrapperAddMessageType(builder, MessageType): builder.PrependUint8Slot(0, MessageType, 0)
def GameMessageWrapperAddMessage(builder, Message): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(Message), 0)
def GameMessageWrapperEnd(builder): return builder.EndObject()
