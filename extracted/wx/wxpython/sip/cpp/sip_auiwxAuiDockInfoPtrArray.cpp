/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_aui.h"
        #include <wx/aui/framemanager.h>


PyDoc_STRVAR(doc_wxAuiDockInfoPtrArray_append, "append(self, obj: Optional[AuiDockInfo])");

extern "C" {static PyObject *meth_wxAuiDockInfoPtrArray_append(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxAuiDockInfoPtrArray_append(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxAuiDockInfo* obj;
        ::wxAuiDockInfoPtrArray *sipCpp;

        static const char *sipKwdList[] = {
            sipName_obj,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ8", &sipSelf, sipType_wxAuiDockInfoPtrArray, &sipCpp, sipType_wxAuiDockInfo, &obj))
        {
        sipCpp->Add(obj);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_AuiDockInfoPtrArray, sipName_append, doc_wxAuiDockInfoPtrArray_append);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxAuiDockInfoPtrArray_index, "index(self, obj: Optional[AuiDockInfo]) -> int");

extern "C" {static PyObject *meth_wxAuiDockInfoPtrArray_index(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxAuiDockInfoPtrArray_index(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxAuiDockInfo* obj;
        ::wxAuiDockInfoPtrArray *sipCpp;

        static const char *sipKwdList[] = {
            sipName_obj,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ8", &sipSelf, sipType_wxAuiDockInfoPtrArray, &sipCpp, sipType_wxAuiDockInfo, &obj))
        {
            int sipRes = 0;
            sipErrorState sipError = sipErrorNone;
        int idx = sipCpp->Index(obj, false);
        if (idx == wxNOT_FOUND) {
            sipError = sipErrorFail;
            wxPyErr_SetString(PyExc_ValueError,
                              "sequence.index(x): x not in sequence");
            }
        sipRes = idx;

            if (sipError == sipErrorFail)
                return 0;

            if (sipError == sipErrorNone)
            {
            return PyLong_FromLong(sipRes);
            }

            sipAddException(sipError, &sipParseErr);
        }
    }

    sipNoMethod(sipParseErr, sipName_AuiDockInfoPtrArray, sipName_index, doc_wxAuiDockInfoPtrArray_index);

    return SIP_NULLPTR;
}


extern "C" {static int slot_wxAuiDockInfoPtrArray___contains__(PyObject *, PyObject *);}
static int slot_wxAuiDockInfoPtrArray___contains__(PyObject *sipSelf, PyObject *sipArg)
{
    ::wxAuiDockInfoPtrArray *sipCpp = reinterpret_cast<::wxAuiDockInfoPtrArray *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf, sipType_wxAuiDockInfoPtrArray));

    if (!sipCpp)
        return -1;

    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxAuiDockInfo* obj;

        if (sipParseArgs(&sipParseErr, sipArg, "1J8", sipType_wxAuiDockInfo, &obj))
        {
            int sipRes = 0;
        int idx = sipCpp->Index(obj, false);
        sipRes = idx != wxNOT_FOUND;

            return sipRes;
        }
    }

    sipNoMethod(sipParseErr, sipName_AuiDockInfoPtrArray, sipName___contains__, SIP_NULLPTR);

    return -1;
}


extern "C" {static PyObject *slot_wxAuiDockInfoPtrArray___getitem__(PyObject *, PyObject *);}
static PyObject *slot_wxAuiDockInfoPtrArray___getitem__(PyObject *sipSelf, PyObject *sipArg)
{
    ::wxAuiDockInfoPtrArray *sipCpp = reinterpret_cast<::wxAuiDockInfoPtrArray *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf, sipType_wxAuiDockInfoPtrArray));

    if (!sipCpp)
        return SIP_NULLPTR;

    PyObject *sipParseErr = SIP_NULLPTR;

    {
        long index;

        if (sipParseArgs(&sipParseErr, sipArg, "1l", &index))
        {
            ::wxAuiDockInfo*sipRes = 0;
            sipErrorState sipError = sipErrorNone;
            if (0 > index)
                index += sipCpp->GetCount();

            if ((index < sipCpp->GetCount()) && (0 <= index)) {
                sipRes = sipCpp->Item(index);
            }
            else {
                wxPyErr_SetString(PyExc_IndexError, "sequence index out of range");
                sipError = sipErrorFail;
            }

            if (sipError == sipErrorFail)
                return 0;

            if (sipError == sipErrorNone)
            {
            return sipConvertFromType(sipRes, sipType_wxAuiDockInfo, SIP_NULLPTR);
            }

            sipAddException(sipError, &sipParseErr);
        }
    }

    sipNoMethod(sipParseErr, sipName_AuiDockInfoPtrArray, sipName___getitem__, SIP_NULLPTR);

    return SIP_NULLPTR;
}


extern "C" {static Py_ssize_t slot_wxAuiDockInfoPtrArray___len__(PyObject *);}
static Py_ssize_t slot_wxAuiDockInfoPtrArray___len__(PyObject *sipSelf)
{
    ::wxAuiDockInfoPtrArray *sipCpp = reinterpret_cast<::wxAuiDockInfoPtrArray *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf, sipType_wxAuiDockInfoPtrArray));

    if (!sipCpp)
        return 0;


    {
        {
            Py_ssize_t sipRes = 0;
        sipRes = sipCpp->GetCount();

            return sipRes;
        }
    }

    return 0;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxAuiDockInfoPtrArray(void *, int);}
static void release_wxAuiDockInfoPtrArray(void *sipCppV, int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast<::wxAuiDockInfoPtrArray *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void *array_wxAuiDockInfoPtrArray(Py_ssize_t);}
static void *array_wxAuiDockInfoPtrArray(Py_ssize_t sipNrElem)
{
    return new ::wxAuiDockInfoPtrArray[sipNrElem];
}


extern "C" {static void array_delete_wxAuiDockInfoPtrArray(void *);}
static void array_delete_wxAuiDockInfoPtrArray(void *sipCpp)
{
    delete[] reinterpret_cast<::wxAuiDockInfoPtrArray *>(sipCpp);
}


extern "C" {static void assign_wxAuiDockInfoPtrArray(void *, Py_ssize_t, void *);}
static void assign_wxAuiDockInfoPtrArray(void *sipDst, Py_ssize_t sipDstIdx, void *sipSrc)
{
    reinterpret_cast<::wxAuiDockInfoPtrArray *>(sipDst)[sipDstIdx] = *reinterpret_cast<::wxAuiDockInfoPtrArray *>(sipSrc);
}


extern "C" {static void *copy_wxAuiDockInfoPtrArray(const void *, Py_ssize_t);}
static void *copy_wxAuiDockInfoPtrArray(const void *sipSrc, Py_ssize_t sipSrcIdx)
{
    return new ::wxAuiDockInfoPtrArray(reinterpret_cast<const ::wxAuiDockInfoPtrArray *>(sipSrc)[sipSrcIdx]);
}


extern "C" {static void dealloc_wxAuiDockInfoPtrArray(sipSimpleWrapper *);}
static void dealloc_wxAuiDockInfoPtrArray(sipSimpleWrapper *sipSelf)
{
    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxAuiDockInfoPtrArray(sipGetAddress(sipSelf), 0);
    }
}


extern "C" {static void *init_type_wxAuiDockInfoPtrArray(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxAuiDockInfoPtrArray(sipSimpleWrapper *, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    ::wxAuiDockInfoPtrArray *sipCpp = SIP_NULLPTR;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, ""))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new ::wxAuiDockInfoPtrArray();
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    {
        const ::wxAuiDockInfoPtrArray* a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, "J9", sipType_wxAuiDockInfoPtrArray, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new ::wxAuiDockInfoPtrArray(*a0);
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    return SIP_NULLPTR;
}


/* Define this type's Python slots. */
static sipPySlotDef slots_wxAuiDockInfoPtrArray[] = {
    {(void *)slot_wxAuiDockInfoPtrArray___contains__, contains_slot},
    {(void *)slot_wxAuiDockInfoPtrArray___getitem__, getitem_slot},
    {(void *)slot_wxAuiDockInfoPtrArray___len__, len_slot},
    {0, (sipPySlotType)0}
};


static PyMethodDef methods_wxAuiDockInfoPtrArray[] = {
    {sipName_append, SIP_MLMETH_CAST(meth_wxAuiDockInfoPtrArray_append), METH_VARARGS|METH_KEYWORDS, doc_wxAuiDockInfoPtrArray_append},
    {sipName_index, SIP_MLMETH_CAST(meth_wxAuiDockInfoPtrArray_index), METH_VARARGS|METH_KEYWORDS, doc_wxAuiDockInfoPtrArray_index}
};

PyDoc_STRVAR(doc_wxAuiDockInfoPtrArray, "\1AuiDockInfoPtrArray()\n"
"AuiDockInfoPtrArray(a0: AuiDockInfoPtrArray)");


sipClassTypeDef sipTypeDef__aui_wxAuiDockInfoPtrArray = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_CLASS,
        sipNameNr_wxAuiDockInfoPtrArray,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_AuiDockInfoPtrArray,
        {0, 0, 1},
        2, methods_wxAuiDockInfoPtrArray,
        0, SIP_NULLPTR,
        0, SIP_NULLPTR,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxAuiDockInfoPtrArray,
    -1,
    -1,
    SIP_NULLPTR,
    slots_wxAuiDockInfoPtrArray,
    init_type_wxAuiDockInfoPtrArray,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxAuiDockInfoPtrArray,
    assign_wxAuiDockInfoPtrArray,
    array_wxAuiDockInfoPtrArray,
    copy_wxAuiDockInfoPtrArray,
    release_wxAuiDockInfoPtrArray,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    array_delete_wxAuiDockInfoPtrArray,
    sizeof (::wxAuiDockInfoPtrArray),
};
