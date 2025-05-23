# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
from gams.core.opt import _optcc

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


optDataNone = _optcc.optDataNone
optDataInteger = _optcc.optDataInteger
optDataDouble = _optcc.optDataDouble
optDataString = _optcc.optDataString
optDataStrList = _optcc.optDataStrList
optTypeInteger = _optcc.optTypeInteger
optTypeDouble = _optcc.optTypeDouble
optTypeString = _optcc.optTypeString
optTypeBoolean = _optcc.optTypeBoolean
optTypeEnumStr = _optcc.optTypeEnumStr
optTypeEnumInt = _optcc.optTypeEnumInt
optTypeMultiList = _optcc.optTypeMultiList
optTypeStrList = _optcc.optTypeStrList
optTypeMacro = _optcc.optTypeMacro
optTypeImmediate = _optcc.optTypeImmediate
optsubRequired = _optcc.optsubRequired
optsubNoValue = _optcc.optsubNoValue
optsubOptional = _optcc.optsubOptional
optsub2Values = _optcc.optsub2Values
optMsgInputEcho = _optcc.optMsgInputEcho
optMsgHelp = _optcc.optMsgHelp
optMsgDefineError = _optcc.optMsgDefineError
optMsgValueError = _optcc.optMsgValueError
optMsgValueWarning = _optcc.optMsgValueWarning
optMsgDeprecated = _optcc.optMsgDeprecated
optMsgFileEnter = _optcc.optMsgFileEnter
optMsgFileLeave = _optcc.optMsgFileLeave
optMsgTooManyMsgs = _optcc.optMsgTooManyMsgs
optMsgUserError = _optcc.optMsgUserError
optMapIndicator = _optcc.optMapIndicator
optMapDefinedVar = _optcc.optMapDefinedVar
class intArray(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, nelements):
        _optcc.intArray_swiginit(self, _optcc.new_intArray(nelements))
    __swig_destroy__ = _optcc.delete_intArray

    def __getitem__(self, index):
        return _optcc.intArray___getitem__(self, index)

    def __setitem__(self, index, value):
        return _optcc.intArray___setitem__(self, index, value)

    def cast(self):
        return _optcc.intArray_cast(self)

    @staticmethod
    def frompointer(t):
        return _optcc.intArray_frompointer(t)

# Register intArray in _optcc:
_optcc.intArray_swigregister(intArray)
class doubleArray(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, nelements):
        _optcc.doubleArray_swiginit(self, _optcc.new_doubleArray(nelements))
    __swig_destroy__ = _optcc.delete_doubleArray

    def __getitem__(self, index):
        return _optcc.doubleArray___getitem__(self, index)

    def __setitem__(self, index, value):
        return _optcc.doubleArray___setitem__(self, index, value)

    def cast(self):
        return _optcc.doubleArray_cast(self)

    @staticmethod
    def frompointer(t):
        return _optcc.doubleArray_frompointer(t)

# Register doubleArray in _optcc:
_optcc.doubleArray_swigregister(doubleArray)

def new_intp():
    return _optcc.new_intp()

def copy_intp(value):
    return _optcc.copy_intp(value)

def delete_intp(obj):
    return _optcc.delete_intp(obj)

def intp_assign(obj, value):
    return _optcc.intp_assign(obj, value)

def intp_value(obj):
    return _optcc.intp_value(obj)

def new_doublep():
    return _optcc.new_doublep()

def copy_doublep(value):
    return _optcc.copy_doublep(value)

def delete_doublep(obj):
    return _optcc.delete_doublep(obj)

def doublep_assign(obj, value):
    return _optcc.doublep_assign(obj, value)

def doublep_value(obj):
    return _optcc.doublep_value(obj)

def new_optHandle_tp():
    return _optcc.new_optHandle_tp()

def copy_optHandle_tp(value):
    return _optcc.copy_optHandle_tp(value)

def delete_optHandle_tp(obj):
    return _optcc.delete_optHandle_tp(obj)

def optHandle_tp_assign(obj, value):
    return _optcc.optHandle_tp_assign(obj, value)

def optHandle_tp_value(obj):
    return _optcc.optHandle_tp_value(obj)

def new_TArgvCB_tp():
    return _optcc.new_TArgvCB_tp()

def copy_TArgvCB_tp(value):
    return _optcc.copy_TArgvCB_tp(value)

def delete_TArgvCB_tp(obj):
    return _optcc.delete_TArgvCB_tp(obj)

def TArgvCB_tp_assign(obj, value):
    return _optcc.TArgvCB_tp_assign(obj, value)

def TArgvCB_tp_value(obj):
    return _optcc.TArgvCB_tp_value(obj)

def optHandleToPtr(popt):
    r"""optHandleToPtr(popt) -> void *"""
    return _optcc.optHandleToPtr(popt)

def ptrTooptHandle(vptr):
    r"""ptrTooptHandle(vptr) -> optHandle_t"""
    return _optcc.ptrTooptHandle(vptr)

def optGetReady(msgBufSize):
    r"""optGetReady(msgBufSize) -> int"""
    return _optcc.optGetReady(msgBufSize)

def optGetReadyD(dirName, msgBufSize):
    r"""optGetReadyD(dirName, msgBufSize) -> int"""
    return _optcc.optGetReadyD(dirName, msgBufSize)

def optGetReadyL(libName, msgBufSize):
    r"""optGetReadyL(libName, msgBufSize) -> int"""
    return _optcc.optGetReadyL(libName, msgBufSize)

def optCreate(popt, msgBufSize):
    r"""optCreate(popt, msgBufSize) -> int"""
    return _optcc.optCreate(popt, msgBufSize)

def optCreateD(popt, dirName, msgBufSize):
    r"""optCreateD(popt, dirName, msgBufSize) -> int"""
    return _optcc.optCreateD(popt, dirName, msgBufSize)

def optCreateL(popt, libName, msgBufSize):
    r"""optCreateL(popt, libName, msgBufSize) -> int"""
    return _optcc.optCreateL(popt, libName, msgBufSize)

def optFree(popt):
    r"""optFree(popt) -> int"""
    return _optcc.optFree(popt)

def optLibraryLoaded():
    r"""optLibraryLoaded() -> int"""
    return _optcc.optLibraryLoaded()

def optLibraryUnload():
    r"""optLibraryUnload() -> int"""
    return _optcc.optLibraryUnload()

def optGetScreenIndicator():
    r"""optGetScreenIndicator() -> int"""
    return _optcc.optGetScreenIndicator()

def optSetScreenIndicator(scrind):
    r"""optSetScreenIndicator(scrind)"""
    return _optcc.optSetScreenIndicator(scrind)

def optGetExceptionIndicator():
    r"""optGetExceptionIndicator() -> int"""
    return _optcc.optGetExceptionIndicator()

def optSetExceptionIndicator(excind):
    r"""optSetExceptionIndicator(excind)"""
    return _optcc.optSetExceptionIndicator(excind)

def optGetExitIndicator():
    r"""optGetExitIndicator() -> int"""
    return _optcc.optGetExitIndicator()

def optSetExitIndicator(extind):
    r"""optSetExitIndicator(extind)"""
    return _optcc.optSetExitIndicator(extind)

def optGetErrorCallback():
    r"""optGetErrorCallback() -> optErrorCallback_t"""
    return _optcc.optGetErrorCallback()

def optSetErrorCallback(func):
    r"""optSetErrorCallback(func)"""
    return _optcc.optSetErrorCallback(func)

def optGetAPIErrorCount():
    r"""optGetAPIErrorCount() -> int"""
    return _optcc.optGetAPIErrorCount()

def optSetAPIErrorCount(ecnt):
    r"""optSetAPIErrorCount(ecnt)"""
    return _optcc.optSetAPIErrorCount(ecnt)

def optErrorHandling(msg):
    r"""optErrorHandling(msg)"""
    return _optcc.optErrorHandling(msg)

def optReadDefinition(popt, fn):
    r"""optReadDefinition(popt, fn) -> int"""
    return _optcc.optReadDefinition(popt, fn)

def optReadDefinitionFromPChar(popt, p_mut):
    r"""optReadDefinitionFromPChar(popt, p_mut) -> int"""
    return _optcc.optReadDefinitionFromPChar(popt, p_mut)

def optReadParameterFile(popt, fn):
    r"""optReadParameterFile(popt, fn) -> int"""
    return _optcc.optReadParameterFile(popt, fn)

def optReadFromStr(popt, s):
    r"""optReadFromStr(popt, s)"""
    return _optcc.optReadFromStr(popt, s)

def optWriteParameterFile(popt, fn):
    r"""optWriteParameterFile(popt, fn) -> int"""
    return _optcc.optWriteParameterFile(popt, fn)

def optClearMessages(popt):
    r"""optClearMessages(popt)"""
    return _optcc.optClearMessages(popt)

def optAddMessage(popt, info):
    r"""optAddMessage(popt, info)"""
    return _optcc.optAddMessage(popt, info)

def optGetMessage(popt, NrMsg):
    r"""optGetMessage(popt, NrMsg)"""
    return _optcc.optGetMessage(popt, NrMsg)

def optResetAll(popt):
    r"""optResetAll(popt)"""
    return _optcc.optResetAll(popt)

def optResetAllRecent(popt):
    r"""optResetAllRecent(popt)"""
    return _optcc.optResetAllRecent(popt)

def optResetRecentChanges(popt):
    r"""optResetRecentChanges(popt)"""
    return _optcc.optResetRecentChanges(popt)

def optShowHelp(popt, AHlpID):
    r"""optShowHelp(popt, AHlpID)"""
    return _optcc.optShowHelp(popt, AHlpID)

def optResetNr(popt, ANr):
    r"""optResetNr(popt, ANr) -> int"""
    return _optcc.optResetNr(popt, ANr)

def optFindStr(popt, AName):
    r"""optFindStr(popt, AName) -> int"""
    return _optcc.optFindStr(popt, AName)

def optGetInfoNr(popt, ANr):
    r"""optGetInfoNr(popt, ANr) -> int"""
    return _optcc.optGetInfoNr(popt, ANr)

def optGetValuesNr(popt, ANr):
    r"""optGetValuesNr(popt, ANr) -> int"""
    return _optcc.optGetValuesNr(popt, ANr)

def optSetValuesNr(popt, ANr, AIVal, ADVal, ASVal):
    r"""optSetValuesNr(popt, ANr, AIVal, ADVal, ASVal) -> int"""
    return _optcc.optSetValuesNr(popt, ANr, AIVal, ADVal, ASVal)

def optSetValues2Nr(popt, ANr, AIVal, ADVal, ASVal):
    r"""optSetValues2Nr(popt, ANr, AIVal, ADVal, ASVal) -> int"""
    return _optcc.optSetValues2Nr(popt, ANr, AIVal, ADVal, ASVal)

def optVersion(popt):
    r"""optVersion(popt)"""
    return _optcc.optVersion(popt)

def optDefinitionFile(popt):
    r"""optDefinitionFile(popt)"""
    return _optcc.optDefinitionFile(popt)

def optGetFromAnyStrList(popt, idash):
    r"""optGetFromAnyStrList(popt, idash) -> int"""
    return _optcc.optGetFromAnyStrList(popt, idash)

def optGetFromListStr(popt, skey):
    r"""optGetFromListStr(popt, skey) -> int"""
    return _optcc.optGetFromListStr(popt, skey)

def optListCountStr(popt, skey):
    r"""optListCountStr(popt, skey) -> int"""
    return _optcc.optListCountStr(popt, skey)

def optReadFromListStr(popt, skey, iPos):
    r"""optReadFromListStr(popt, skey, iPos) -> int"""
    return _optcc.optReadFromListStr(popt, skey, iPos)

def optSynonymCount(popt):
    r"""optSynonymCount(popt) -> int"""
    return _optcc.optSynonymCount(popt)

def optGetSynonym(popt, NrSyn):
    r"""optGetSynonym(popt, NrSyn) -> int"""
    return _optcc.optGetSynonym(popt, NrSyn)

def optEchoSet(popt, AIVal):
    r"""optEchoSet(popt, AIVal)"""
    return _optcc.optEchoSet(popt, AIVal)

def optEOLOnlySet(popt, AIVal):
    r"""optEOLOnlySet(popt, AIVal) -> int"""
    return _optcc.optEOLOnlySet(popt, AIVal)

def optNoBoundsSet(popt, AIVal):
    r"""optNoBoundsSet(popt, AIVal)"""
    return _optcc.optNoBoundsSet(popt, AIVal)

def optEOLChars(popt):
    r"""optEOLChars(popt) -> int"""
    return _optcc.optEOLChars(popt)

def optErrorCount(popt):
    r"""optErrorCount(popt)"""
    return _optcc.optErrorCount(popt)

def optGetBoundsInt(popt, ANr):
    r"""optGetBoundsInt(popt, ANr) -> int"""
    return _optcc.optGetBoundsInt(popt, ANr)

def optGetBoundsDbl(popt, ANr):
    r"""optGetBoundsDbl(popt, ANr) -> int"""
    return _optcc.optGetBoundsDbl(popt, ANr)

def optGetDefaultStr(popt, ANr):
    r"""optGetDefaultStr(popt, ANr) -> int"""
    return _optcc.optGetDefaultStr(popt, ANr)

def optGetIntNr(popt, ANr):
    r"""optGetIntNr(popt, ANr) -> int"""
    return _optcc.optGetIntNr(popt, ANr)

def optGetInt2Nr(popt, ANr):
    r"""optGetInt2Nr(popt, ANr) -> int"""
    return _optcc.optGetInt2Nr(popt, ANr)

def optSetIntNr(popt, ANr, AIVal):
    r"""optSetIntNr(popt, ANr, AIVal) -> int"""
    return _optcc.optSetIntNr(popt, ANr, AIVal)

def optSetInt2Nr(popt, ANr, AIVal):
    r"""optSetInt2Nr(popt, ANr, AIVal) -> int"""
    return _optcc.optSetInt2Nr(popt, ANr, AIVal)

def optGetStrNr(popt, ANr):
    r"""optGetStrNr(popt, ANr) -> int"""
    return _optcc.optGetStrNr(popt, ANr)

def optGetOptHelpNr(popt, ANr):
    r"""optGetOptHelpNr(popt, ANr) -> int"""
    return _optcc.optGetOptHelpNr(popt, ANr)

def optGetEnumHelp(popt, ANr, AOrd):
    r"""optGetEnumHelp(popt, ANr, AOrd) -> int"""
    return _optcc.optGetEnumHelp(popt, ANr, AOrd)

def optGetEnumStrNr(popt, ANr):
    r"""optGetEnumStrNr(popt, ANr) -> int"""
    return _optcc.optGetEnumStrNr(popt, ANr)

def optGetEnumCount(popt, ANr):
    r"""optGetEnumCount(popt, ANr) -> int"""
    return _optcc.optGetEnumCount(popt, ANr)

def optGetEnumValue(popt, ANr, AOrd):
    r"""optGetEnumValue(popt, ANr, AOrd) -> int"""
    return _optcc.optGetEnumValue(popt, ANr, AOrd)

def optGetStr2Nr(popt, ANr):
    r"""optGetStr2Nr(popt, ANr) -> int"""
    return _optcc.optGetStr2Nr(popt, ANr)

def optSetStrNr(popt, ANr, ASVal):
    r"""optSetStrNr(popt, ANr, ASVal) -> int"""
    return _optcc.optSetStrNr(popt, ANr, ASVal)

def optSetStr2Nr(popt, ANr, ASVal):
    r"""optSetStr2Nr(popt, ANr, ASVal) -> int"""
    return _optcc.optSetStr2Nr(popt, ANr, ASVal)

def optGetDblNr(popt, ANr):
    r"""optGetDblNr(popt, ANr) -> int"""
    return _optcc.optGetDblNr(popt, ANr)

def optGetDbl2Nr(popt, ANr):
    r"""optGetDbl2Nr(popt, ANr) -> int"""
    return _optcc.optGetDbl2Nr(popt, ANr)

def optSetDblNr(popt, ANr, ADVal):
    r"""optSetDblNr(popt, ANr, ADVal) -> int"""
    return _optcc.optSetDblNr(popt, ANr, ADVal)

def optSetDbl2Nr(popt, ANr, ADVal):
    r"""optSetDbl2Nr(popt, ANr, ADVal) -> int"""
    return _optcc.optSetDbl2Nr(popt, ANr, ADVal)

def optGetValStr(popt, AName):
    r"""optGetValStr(popt, AName) -> int"""
    return _optcc.optGetValStr(popt, AName)

def optGetVal2Str(popt, AName):
    r"""optGetVal2Str(popt, AName) -> int"""
    return _optcc.optGetVal2Str(popt, AName)

def optGetNameNr(popt, ANr):
    r"""optGetNameNr(popt, ANr) -> int"""
    return _optcc.optGetNameNr(popt, ANr)

def optGetDefinedNr(popt, ANr):
    r"""optGetDefinedNr(popt, ANr) -> int"""
    return _optcc.optGetDefinedNr(popt, ANr)

def optGetHelpNr(popt, ANr):
    r"""optGetHelpNr(popt, ANr) -> int"""
    return _optcc.optGetHelpNr(popt, ANr)

def optGetGroupNr(popt, ANr):
    r"""optGetGroupNr(popt, ANr) -> int"""
    return _optcc.optGetGroupNr(popt, ANr)

def optGetGroupGrpNr(popt, AGroup):
    r"""optGetGroupGrpNr(popt, AGroup) -> int"""
    return _optcc.optGetGroupGrpNr(popt, AGroup)

def optGetOptGroupNr(popt, ANr):
    r"""optGetOptGroupNr(popt, ANr) -> int"""
    return _optcc.optGetOptGroupNr(popt, ANr)

def optGetDotOptNr(popt, ANr):
    r"""optGetDotOptNr(popt, ANr) -> int"""
    return _optcc.optGetDotOptNr(popt, ANr)

def optGetDotOptUel(popt, ANr, ADim):
    r"""optGetDotOptUel(popt, ANr, ADim) -> int"""
    return _optcc.optGetDotOptUel(popt, ANr, ADim)

def optGetVarEquMapNr(popt, maptype, ANr):
    r"""optGetVarEquMapNr(popt, maptype, ANr) -> int"""
    return _optcc.optGetVarEquMapNr(popt, maptype, ANr)

def optGetEquVarEquMapNr(popt, maptype, ANr, ADim):
    r"""optGetEquVarEquMapNr(popt, maptype, ANr, ADim) -> int"""
    return _optcc.optGetEquVarEquMapNr(popt, maptype, ANr, ADim)

def optGetVarVarEquMapNr(popt, maptype, ANr, ADim):
    r"""optGetVarVarEquMapNr(popt, maptype, ANr, ADim) -> int"""
    return _optcc.optGetVarVarEquMapNr(popt, maptype, ANr, ADim)

def optVarEquMapCount(popt, maptype):
    r"""optVarEquMapCount(popt, maptype) -> int"""
    return _optcc.optVarEquMapCount(popt, maptype)

def optGetIndicatorNr(popt, ANr):
    r"""optGetIndicatorNr(popt, ANr) -> int"""
    return _optcc.optGetIndicatorNr(popt, ANr)

def optGetEquIndicatorNr(popt, ANr, ADim):
    r"""optGetEquIndicatorNr(popt, ANr, ADim) -> int"""
    return _optcc.optGetEquIndicatorNr(popt, ANr, ADim)

def optGetVarIndicatorNr(popt, ANr, ADim):
    r"""optGetVarIndicatorNr(popt, ANr, ADim) -> int"""
    return _optcc.optGetVarIndicatorNr(popt, ANr, ADim)

def optIndicatorCount(popt):
    r"""optIndicatorCount(popt) -> int"""
    return _optcc.optIndicatorCount(popt)

def optDotOptCount(popt):
    r"""optDotOptCount(popt) -> int"""
    return _optcc.optDotOptCount(popt)

def optSetRefNr(popt, ANr, ARefNr):
    r"""optSetRefNr(popt, ANr, ARefNr) -> int"""
    return _optcc.optSetRefNr(popt, ANr, ARefNr)

def optSetRefNrStr(popt, AOpt, ARefNr):
    r"""optSetRefNrStr(popt, AOpt, ARefNr) -> int"""
    return _optcc.optSetRefNrStr(popt, AOpt, ARefNr)

def optGetConstName(popt, cgroup, cindex):
    r"""optGetConstName(popt, cgroup, cindex) -> int"""
    return _optcc.optGetConstName(popt, cgroup, cindex)

def optGetTypeName(popt, TNr):
    r"""optGetTypeName(popt, TNr) -> int"""
    return _optcc.optGetTypeName(popt, TNr)

def optLookUp(popt, AOpt):
    r"""optLookUp(popt, AOpt) -> int"""
    return _optcc.optLookUp(popt, AOpt)

def optReadFromPChar(popt, p_mut):
    r"""optReadFromPChar(popt, p_mut)"""
    return _optcc.optReadFromPChar(popt, p_mut)

def optReadFromCmdLine(popt, p_mut):
    r"""optReadFromCmdLine(popt, p_mut)"""
    return _optcc.optReadFromCmdLine(popt, p_mut)

def optReadFromCmdArgs(popt, cb):
    r"""optReadFromCmdArgs(popt, cb)"""
    return _optcc.optReadFromCmdArgs(popt, cb)

def optGetNameOpt(popt, ASVal):
    r"""optGetNameOpt(popt, ASVal) -> int"""
    return _optcc.optGetNameOpt(popt, ASVal)

def optResetStr(popt, AName):
    r"""optResetStr(popt, AName) -> int"""
    return _optcc.optResetStr(popt, AName)

def optGetDefinedStr(popt, AName):
    r"""optGetDefinedStr(popt, AName) -> int"""
    return _optcc.optGetDefinedStr(popt, AName)

def optGetIntStr(popt, AName):
    r"""optGetIntStr(popt, AName) -> int"""
    return _optcc.optGetIntStr(popt, AName)

def optGetDblStr(popt, AName):
    r"""optGetDblStr(popt, AName) -> double"""
    return _optcc.optGetDblStr(popt, AName)

def optGetStrStr(popt, AName):
    r"""optGetStrStr(popt, AName) -> char *"""
    return _optcc.optGetStrStr(popt, AName)

def optSetIntStr(popt, AName, AIVal):
    r"""optSetIntStr(popt, AName, AIVal)"""
    return _optcc.optSetIntStr(popt, AName, AIVal)

def optSetDblStr(popt, AName, ADVal):
    r"""optSetDblStr(popt, AName, ADVal)"""
    return _optcc.optSetDblStr(popt, AName, ADVal)

def optSetStrStr(popt, AName, ASVal):
    r"""optSetStrStr(popt, AName, ASVal)"""
    return _optcc.optSetStrStr(popt, AName, ASVal)

def optIsDeprecated(popt, AName):
    r"""optIsDeprecated(popt, AName) -> int"""
    return _optcc.optIsDeprecated(popt, AName)

def optCount(popt):
    r"""optCount(popt) -> int"""
    return _optcc.optCount(popt)

def optMessageCount(popt):
    r"""optMessageCount(popt) -> int"""
    return _optcc.optMessageCount(popt)

def optGroupCount(popt):
    r"""optGroupCount(popt) -> int"""
    return _optcc.optGroupCount(popt)

def optRecentEnabled(popt):
    r"""optRecentEnabled(popt) -> int"""
    return _optcc.optRecentEnabled(popt)

def optRecentEnabledSet(popt, x):
    r"""optRecentEnabledSet(popt, x)"""
    return _optcc.optRecentEnabledSet(popt, x)

def optSeparator(popt):
    r"""optSeparator(popt) -> char *"""
    return _optcc.optSeparator(popt)

def optStringQuote(popt):
    r"""optStringQuote(popt) -> char *"""
    return _optcc.optStringQuote(popt)
GLOBAL_MAX_INDEX_DIM = _optcc.GLOBAL_MAX_INDEX_DIM

GLOBAL_UEL_IDENT_SIZE = _optcc.GLOBAL_UEL_IDENT_SIZE

ITERLIM_INFINITY = _optcc.ITERLIM_INFINITY

RESLIM_INFINITY = _optcc.RESLIM_INFINITY

GMS_MAX_SOLVERS = _optcc.GMS_MAX_SOLVERS

GMS_MAX_INDEX_DIM = _optcc.GMS_MAX_INDEX_DIM

GMS_UEL_IDENT_SIZE = _optcc.GMS_UEL_IDENT_SIZE

GMS_SSSIZE = _optcc.GMS_SSSIZE

GMS_VARTYPE_UNKNOWN = _optcc.GMS_VARTYPE_UNKNOWN

GMS_VARTYPE_BINARY = _optcc.GMS_VARTYPE_BINARY

GMS_VARTYPE_INTEGER = _optcc.GMS_VARTYPE_INTEGER

GMS_VARTYPE_POSITIVE = _optcc.GMS_VARTYPE_POSITIVE

GMS_VARTYPE_NEGATIVE = _optcc.GMS_VARTYPE_NEGATIVE

GMS_VARTYPE_FREE = _optcc.GMS_VARTYPE_FREE

GMS_VARTYPE_SOS1 = _optcc.GMS_VARTYPE_SOS1

GMS_VARTYPE_SOS2 = _optcc.GMS_VARTYPE_SOS2

GMS_VARTYPE_SEMICONT = _optcc.GMS_VARTYPE_SEMICONT

GMS_VARTYPE_SEMIINT = _optcc.GMS_VARTYPE_SEMIINT

GMS_VARTYPE_MAX = _optcc.GMS_VARTYPE_MAX

GMS_EQU_USERINFO_BASE = _optcc.GMS_EQU_USERINFO_BASE

GMS_EQUTYPE_E = _optcc.GMS_EQUTYPE_E

GMS_EQUTYPE_G = _optcc.GMS_EQUTYPE_G

GMS_EQUTYPE_L = _optcc.GMS_EQUTYPE_L

GMS_EQUTYPE_N = _optcc.GMS_EQUTYPE_N

GMS_EQUTYPE_X = _optcc.GMS_EQUTYPE_X

GMS_EQUTYPE_C = _optcc.GMS_EQUTYPE_C

GMS_EQUTYPE_B = _optcc.GMS_EQUTYPE_B

GMS_EQUTYPE_MAX = _optcc.GMS_EQUTYPE_MAX

GMS_EQUEOFFSET = _optcc.GMS_EQUEOFFSET

GMS_SETTYPE_DEFAULT = _optcc.GMS_SETTYPE_DEFAULT

GMS_SETTYPE_SINGLETON = _optcc.GMS_SETTYPE_SINGLETON

GMS_SETTYPE_MAX = _optcc.GMS_SETTYPE_MAX

GMS_VAL_LEVEL = _optcc.GMS_VAL_LEVEL

GMS_VAL_MARGINAL = _optcc.GMS_VAL_MARGINAL

GMS_VAL_LOWER = _optcc.GMS_VAL_LOWER

GMS_VAL_UPPER = _optcc.GMS_VAL_UPPER

GMS_VAL_SCALE = _optcc.GMS_VAL_SCALE

GMS_VAL_MAX = _optcc.GMS_VAL_MAX

sv_valund = _optcc.sv_valund

sv_valna = _optcc.sv_valna

sv_valpin = _optcc.sv_valpin

sv_valmin = _optcc.sv_valmin

sv_valeps = _optcc.sv_valeps

sv_normal = _optcc.sv_normal

sv_acronym = _optcc.sv_acronym

GMS_SVIDX_UNDEF = _optcc.GMS_SVIDX_UNDEF

GMS_SVIDX_NA = _optcc.GMS_SVIDX_NA

GMS_SVIDX_PINF = _optcc.GMS_SVIDX_PINF

GMS_SVIDX_MINF = _optcc.GMS_SVIDX_MINF

GMS_SVIDX_EPS = _optcc.GMS_SVIDX_EPS

GMS_SVIDX_NORMAL = _optcc.GMS_SVIDX_NORMAL

GMS_SVIDX_ACR = _optcc.GMS_SVIDX_ACR

GMS_SVIDX_MAX = _optcc.GMS_SVIDX_MAX

dt_set = _optcc.dt_set

dt_par = _optcc.dt_par

dt_var = _optcc.dt_var

dt_equ = _optcc.dt_equ

dt_alias = _optcc.dt_alias

GMS_DT_SET = _optcc.GMS_DT_SET

GMS_DT_PAR = _optcc.GMS_DT_PAR

GMS_DT_VAR = _optcc.GMS_DT_VAR

GMS_DT_EQU = _optcc.GMS_DT_EQU

GMS_DT_ALIAS = _optcc.GMS_DT_ALIAS

GMS_DT_MAX = _optcc.GMS_DT_MAX

GMS_SV_UNDEF = _optcc.GMS_SV_UNDEF

GMS_SV_NA = _optcc.GMS_SV_NA

GMS_SV_PINF = _optcc.GMS_SV_PINF

GMS_SV_MINF = _optcc.GMS_SV_MINF

GMS_SV_EPS = _optcc.GMS_SV_EPS

GMS_SV_ACR = _optcc.GMS_SV_ACR

GMS_SV_NAINT = _optcc.GMS_SV_NAINT

STAT_OK = _optcc.STAT_OK

STAT_NOPT = _optcc.STAT_NOPT

STAT_INFES = _optcc.STAT_INFES

STAT_UNBND = _optcc.STAT_UNBND

STAT_EVAL = _optcc.STAT_EVAL

STAT_UNKNW = _optcc.STAT_UNKNW

STAT_REDEF = _optcc.STAT_REDEF

STAT_DEPND = _optcc.STAT_DEPND

STAT_REDIR = _optcc.STAT_REDIR

STAT_MAX = _optcc.STAT_MAX

SS_MAX = _optcc.SS_MAX

MS_MAX = _optcc.MS_MAX


cvar = _optcc.cvar
gmsGdxTypeText = cvar.gmsGdxTypeText
gmsVarTypeText = cvar.gmsVarTypeText
gmsValTypeText = cvar.gmsValTypeText
gmsSVText = cvar.gmsSVText
gmsSpecialValues = cvar.gmsSpecialValues
gmsDefRecVar = cvar.gmsDefRecVar
gmsDefRecEqu = cvar.gmsDefRecEqu
rcStat = cvar.rcStat
solveStatusTxt = cvar.solveStatusTxt
modelStatusTxt = cvar.modelStatusTxt

