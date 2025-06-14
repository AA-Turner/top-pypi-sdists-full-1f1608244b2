# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flat

import flatbuffers

# /// Notification when the local player is spectating another player.
class PlayerSpectate(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsPlayerSpectate(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PlayerSpectate()
        x.Init(buf, n + offset)
        return x

    # PlayerSpectate
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

# /// index of the player that is being spectated. Will be -1 if not spectating anyone.
    # PlayerSpectate
    def PlayerIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def PlayerSpectateStart(builder): builder.StartObject(1)
def PlayerSpectateAddPlayerIndex(builder, playerIndex): builder.PrependInt32Slot(0, playerIndex, 0)
def PlayerSpectateEnd(builder): return builder.EndObject()
