/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_html.h"
        #include <wx/html/helpdata.h>


PyDoc_STRVAR(doc_wxHtmlBookRecArray_append, "append(self, obj: HtmlBookRecord)");

extern "C" {static PyObject *meth_wxHtmlBookRecArray_append(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxHtmlBookRecArray_append(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxHtmlBookRecord* obj;
        ::wxHtmlBookRecArray *sipCpp;

        static const char *sipKwdList[] = {
            sipName_obj,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ9", &sipSelf, sipType_wxHtmlBookRecArray, &sipCpp, sipType_wxHtmlBookRecord, &obj))
        {
        sipCpp->Add(*obj);

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_HtmlBookRecArray, sipName_append, doc_wxHtmlBookRecArray_append);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxHtmlBookRecArray_index, "index(self, obj: HtmlBookRecord) -> int");

extern "C" {static PyObject *meth_wxHtmlBookRecArray_index(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxHtmlBookRecArray_index(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxHtmlBookRecord* obj;
        ::wxHtmlBookRecArray *sipCpp;

        static const char *sipKwdList[] = {
            sipName_obj,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ9", &sipSelf, sipType_wxHtmlBookRecArray, &sipCpp, sipType_wxHtmlBookRecord, &obj))
        {
            int sipRes = 0;
            sipErrorState sipError = sipErrorNone;
        int idx = sipCpp->Index(*obj, false);
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

    sipNoMethod(sipParseErr, sipName_HtmlBookRecArray, sipName_index, doc_wxHtmlBookRecArray_index);

    return SIP_NULLPTR;
}


extern "C" {static int slot_wxHtmlBookRecArray___contains__(PyObject *, PyObject *);}
static int slot_wxHtmlBookRecArray___contains__(PyObject *sipSelf, PyObject *sipArg)
{
    ::wxHtmlBookRecArray *sipCpp = reinterpret_cast<::wxHtmlBookRecArray *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf, sipType_wxHtmlBookRecArray));

    if (!sipCpp)
        return -1;

    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxHtmlBookRecord* obj;

        if (sipParseArgs(&sipParseErr, sipArg, "1J9", sipType_wxHtmlBookRecord, &obj))
        {
            int sipRes = 0;
        int idx = sipCpp->Index(*obj, false);
        sipRes = idx != wxNOT_FOUND;

            return sipRes;
        }
    }

    sipNoMethod(sipParseErr, sipName_HtmlBookRecArray, sipName___contains__, SIP_NULLPTR);

    return -1;
}


extern "C" {static PyObject *slot_wxHtmlBookRecArray___getitem__(PyObject *, PyObject *);}
static PyObject *slot_wxHtmlBookRecArray___getitem__(PyObject *sipSelf, PyObject *sipArg)
{
    ::wxHtmlBookRecArray *sipCpp = reinterpret_cast<::wxHtmlBookRecArray *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf, sipType_wxHtmlBookRecArray));

    if (!sipCpp)
        return SIP_NULLPTR;

    PyObject *sipParseErr = SIP_NULLPTR;

    {
        long index;

        if (sipParseArgs(&sipParseErr, sipArg, "1l", &index))
        {
            ::wxHtmlBookRecord*sipRes = 0;
            sipErrorState sipError = sipErrorNone;
            if (0 > index)
                index += sipCpp->GetCount();

            if ((index < sipCpp->GetCount()) && (0 <= index)) {
                sipRes = &sipCpp->Item(index);
            }
            else {
                wxPyErr_SetString(PyExc_IndexError, "sequence index out of range");
                sipError = sipErrorFail;
            }

            if (sipError == sipErrorFail)
                return 0;

            if (sipError == sipErrorNone)
            {
            return sipConvertFromType(sipRes, sipType_wxHtmlBookRecord, SIP_NULLPTR);
            }

            sipAddException(sipError, &sipParseErr);
        }
    }

    sipNoMethod(sipParseErr, sipName_HtmlBookRecArray, sipName___getitem__, SIP_NULLPTR);

    return SIP_NULLPTR;
}


extern "C" {static Py_ssize_t slot_wxHtmlBookRecArray___len__(PyObject *);}
static Py_ssize_t slot_wxHtmlBookRecArray___len__(PyObject *sipSelf)
{
    ::wxHtmlBookRecArray *sipCpp = reinterpret_cast<::wxHtmlBookRecArray *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf, sipType_wxHtmlBookRecArray));

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
extern "C" {static void release_wxHtmlBookRecArray(void *, int);}
static void release_wxHtmlBookRecArray(void *sipCppV, int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast<::wxHtmlBookRecArray *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void *array_wxHtmlBookRecArray(Py_ssize_t);}
static void *array_wxHtmlBookRecArray(Py_ssize_t sipNrElem)
{
    return new ::wxHtmlBookRecArray[sipNrElem];
}


extern "C" {static void array_delete_wxHtmlBookRecArray(void *);}
static void array_delete_wxHtmlBookRecArray(void *sipCpp)
{
    delete[] reinterpret_cast<::wxHtmlBookRecArray *>(sipCpp);
}


extern "C" {static void assign_wxHtmlBookRecArray(void *, Py_ssize_t, void *);}
static void assign_wxHtmlBookRecArray(void *sipDst, Py_ssize_t sipDstIdx, void *sipSrc)
{
    reinterpret_cast<::wxHtmlBookRecArray *>(sipDst)[sipDstIdx] = *reinterpret_cast<::wxHtmlBookRecArray *>(sipSrc);
}


extern "C" {static void *copy_wxHtmlBookRecArray(const void *, Py_ssize_t);}
static void *copy_wxHtmlBookRecArray(const void *sipSrc, Py_ssize_t sipSrcIdx)
{
    return new ::wxHtmlBookRecArray(reinterpret_cast<const ::wxHtmlBookRecArray *>(sipSrc)[sipSrcIdx]);
}


extern "C" {static void dealloc_wxHtmlBookRecArray(sipSimpleWrapper *);}
static void dealloc_wxHtmlBookRecArray(sipSimpleWrapper *sipSelf)
{
    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxHtmlBookRecArray(sipGetAddress(sipSelf), 0);
    }
}


extern "C" {static void *init_type_wxHtmlBookRecArray(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxHtmlBookRecArray(sipSimpleWrapper *, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    ::wxHtmlBookRecArray *sipCpp = SIP_NULLPTR;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, ""))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new ::wxHtmlBookRecArray();
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    {
        const ::wxHtmlBookRecArray* a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, "J9", sipType_wxHtmlBookRecArray, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new ::wxHtmlBookRecArray(*a0);
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    return SIP_NULLPTR;
}


/* Define this type's Python slots. */
static sipPySlotDef slots_wxHtmlBookRecArray[] = {
    {(void *)slot_wxHtmlBookRecArray___contains__, contains_slot},
    {(void *)slot_wxHtmlBookRecArray___getitem__, getitem_slot},
    {(void *)slot_wxHtmlBookRecArray___len__, len_slot},
    {0, (sipPySlotType)0}
};


static PyMethodDef methods_wxHtmlBookRecArray[] = {
    {sipName_append, SIP_MLMETH_CAST(meth_wxHtmlBookRecArray_append), METH_VARARGS|METH_KEYWORDS, doc_wxHtmlBookRecArray_append},
    {sipName_index, SIP_MLMETH_CAST(meth_wxHtmlBookRecArray_index), METH_VARARGS|METH_KEYWORDS, doc_wxHtmlBookRecArray_index}
};

PyDoc_STRVAR(doc_wxHtmlBookRecArray, "\1HtmlBookRecArray()\n"
"HtmlBookRecArray(a0: HtmlBookRecArray)");


sipClassTypeDef sipTypeDef__html_wxHtmlBookRecArray = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_CLASS,
        sipNameNr_wxHtmlBookRecArray,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_HtmlBookRecArray,
        {0, 0, 1},
        2, methods_wxHtmlBookRecArray,
        0, SIP_NULLPTR,
        0, SIP_NULLPTR,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxHtmlBookRecArray,
    -1,
    -1,
    SIP_NULLPTR,
    slots_wxHtmlBookRecArray,
    init_type_wxHtmlBookRecArray,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxHtmlBookRecArray,
    assign_wxHtmlBookRecArray,
    array_wxHtmlBookRecArray,
    copy_wxHtmlBookRecArray,
    release_wxHtmlBookRecArray,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    array_delete_wxHtmlBookRecArray,
    sizeof (::wxHtmlBookRecArray),
};
