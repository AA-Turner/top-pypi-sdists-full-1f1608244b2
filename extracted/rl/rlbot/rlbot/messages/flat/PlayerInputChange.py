# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flat

import flatbuffers

# /// Rocket League is notifying us that some player has moved their controller. This is an *output*
class PlayerInputChange(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsPlayerInputChange(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PlayerInputChange()
        x.Init(buf, n + offset)
        return x

    # PlayerInputChange
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # PlayerInputChange
    def PlayerIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PlayerInputChange
    def ControllerState(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .ControllerState import ControllerState
            obj = ControllerState()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # PlayerInputChange
    def DodgeForward(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # PlayerInputChange
    def DodgeRight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def PlayerInputChangeStart(builder): builder.StartObject(4)
def PlayerInputChangeAddPlayerIndex(builder, playerIndex): builder.PrependInt32Slot(0, playerIndex, 0)
def PlayerInputChangeAddControllerState(builder, controllerState): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(controllerState), 0)
def PlayerInputChangeAddDodgeForward(builder, dodgeForward): builder.PrependFloat32Slot(2, dodgeForward, 0.0)
def PlayerInputChangeAddDodgeRight(builder, dodgeRight): builder.PrependFloat32Slot(3, dodgeRight, 0.0)
def PlayerInputChangeEnd(builder): return builder.EndObject()
