/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_core.h"
        #include <wx/gbsizer.h>
    PyObject* _wxGBSpan_Get(wxGBSpan* self)
    {
        wxPyThreadBlocker blocker;
        return sipBuildResult(0, "(ii)", self->GetRowspan(), self->GetColspan());
    }
    void _wxGBSpan_Set(wxGBSpan* self, int rowspan, int colspan)
    {
        self->SetRowspan(rowspan);
        self->SetColspan(colspan);
    }


PyDoc_STRVAR(doc_wxGBSpan_GetColspan, "GetColspan() -> int\n"
"\n"
"Get the current colspan value.");

extern "C" {static PyObject *meth_wxGBSpan_GetColspan(PyObject *, PyObject *);}
static PyObject *meth_wxGBSpan_GetColspan(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxGBSpan *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGBSpan, &sipCpp))
        {
            int sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetColspan();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyLong_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_GBSpan, sipName_GetColspan, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGBSpan_GetRowspan, "GetRowspan() -> int\n"
"\n"
"Get the current rowspan value.");

extern "C" {static PyObject *meth_wxGBSpan_GetRowspan(PyObject *, PyObject *);}
static PyObject *meth_wxGBSpan_GetRowspan(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxGBSpan *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGBSpan, &sipCpp))
        {
            int sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetRowspan();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyLong_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_GBSpan, sipName_GetRowspan, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGBSpan_SetColspan, "SetColspan(colspan) -> None\n"
"\n"
"Set a new colspan value.");

extern "C" {static PyObject *meth_wxGBSpan_SetColspan(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxGBSpan_SetColspan(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        int colspan;
        ::wxGBSpan *sipCpp;

        static const char *sipKwdList[] = {
            sipName_colspan,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "Bi", &sipSelf, sipType_wxGBSpan, &sipCpp, &colspan))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetColspan(colspan);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_GBSpan, sipName_SetColspan, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGBSpan_SetRowspan, "SetRowspan(rowspan) -> None\n"
"\n"
"Set a new rowspan value.");

extern "C" {static PyObject *meth_wxGBSpan_SetRowspan(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxGBSpan_SetRowspan(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        int rowspan;
        ::wxGBSpan *sipCpp;

        static const char *sipKwdList[] = {
            sipName_rowspan,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "Bi", &sipSelf, sipType_wxGBSpan, &sipCpp, &rowspan))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetRowspan(rowspan);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_GBSpan, sipName_SetRowspan, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGBSpan_Get, "Get() -> (rowspan, colspan)\n"
"\n"
"Return the rowspan and colspan properties as a tuple.");

extern "C" {static PyObject *meth_wxGBSpan_Get(PyObject *, PyObject *);}
static PyObject *meth_wxGBSpan_Get(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxGBSpan *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGBSpan, &sipCpp))
        {
            PyObject * sipRes = SIP_NULLPTR;
            int sipIsErr = 0;
        PyErr_Clear();
        Py_BEGIN_ALLOW_THREADS
        sipRes = _wxGBSpan_Get(sipCpp);
        Py_END_ALLOW_THREADS
        if (PyErr_Occurred()) sipIsErr = 1;

            if (sipIsErr)
                return 0;

            return sipRes;
        }
    }

    sipNoMethod(sipParseErr, sipName_GBSpan, sipName_Get, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGBSpan_Set, "Set(rowspan=0, colspan=0) -> None\n"
"\n"
"Set both the rowspan and colspan properties.");

extern "C" {static PyObject *meth_wxGBSpan_Set(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxGBSpan_Set(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        int rowspan = 0;
        int colspan = 0;
        ::wxGBSpan *sipCpp;

        static const char *sipKwdList[] = {
            sipName_rowspan,
            sipName_colspan,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "B|ii", &sipSelf, sipType_wxGBSpan, &sipCpp, &rowspan, &colspan))
        {
            int sipIsErr = 0;
        PyErr_Clear();
        Py_BEGIN_ALLOW_THREADS
        _wxGBSpan_Set(sipCpp, rowspan, colspan);
        Py_END_ALLOW_THREADS
        if (PyErr_Occurred()) sipIsErr = 1;

            if (sipIsErr)
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_GBSpan, sipName_Set, SIP_NULLPTR);

    return SIP_NULLPTR;
}


extern "C" {static PyObject *slot_wxGBSpan___eq__(PyObject *, PyObject *);}
static PyObject *slot_wxGBSpan___eq__(PyObject *sipSelf, PyObject *sipArg)
{
    ::wxGBSpan *sipCpp = reinterpret_cast<::wxGBSpan *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf, sipType_wxGBSpan));

    if (!sipCpp)
        return SIP_NULLPTR;

    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxGBSpan* o;
        int oState = 0;

        if (sipParseArgs(&sipParseErr, sipArg, "1J1", sipType_wxGBSpan, &o, &oState))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->::wxGBSpan::operator==(*o);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxGBSpan *>(o), sipType_wxGBSpan, oState);

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    Py_XDECREF(sipParseErr);

    return sipPySlotExtend(&sipModuleAPI__core, eq_slot, sipType_wxGBSpan, sipSelf, sipArg);
}


extern "C" {static PyObject *slot_wxGBSpan___ne__(PyObject *, PyObject *);}
static PyObject *slot_wxGBSpan___ne__(PyObject *sipSelf, PyObject *sipArg)
{
    ::wxGBSpan *sipCpp = reinterpret_cast<::wxGBSpan *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf, sipType_wxGBSpan));

    if (!sipCpp)
        return SIP_NULLPTR;

    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxGBSpan* o;
        int oState = 0;

        if (sipParseArgs(&sipParseErr, sipArg, "1J1", sipType_wxGBSpan, &o, &oState))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->::wxGBSpan::operator!=(*o);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxGBSpan *>(o), sipType_wxGBSpan, oState);

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    Py_XDECREF(sipParseErr);

    return sipPySlotExtend(&sipModuleAPI__core, ne_slot, sipType_wxGBSpan, sipSelf, sipArg);
}


/* Call the instance's destructor. */
extern "C" {static void release_wxGBSpan(void *, int);}
static void release_wxGBSpan(void *sipCppV, int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast<::wxGBSpan *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void *array_wxGBSpan(Py_ssize_t);}
static void *array_wxGBSpan(Py_ssize_t sipNrElem)
{
    return new ::wxGBSpan[sipNrElem];
}


extern "C" {static void array_delete_wxGBSpan(void *);}
static void array_delete_wxGBSpan(void *sipCpp)
{
    delete[] reinterpret_cast<::wxGBSpan *>(sipCpp);
}


extern "C" {static void assign_wxGBSpan(void *, Py_ssize_t, void *);}
static void assign_wxGBSpan(void *sipDst, Py_ssize_t sipDstIdx, void *sipSrc)
{
    reinterpret_cast<::wxGBSpan *>(sipDst)[sipDstIdx] = *reinterpret_cast<::wxGBSpan *>(sipSrc);
}


extern "C" {static void *copy_wxGBSpan(const void *, Py_ssize_t);}
static void *copy_wxGBSpan(const void *sipSrc, Py_ssize_t sipSrcIdx)
{
    return new ::wxGBSpan(reinterpret_cast<const ::wxGBSpan *>(sipSrc)[sipSrcIdx]);
}


extern "C" {static void dealloc_wxGBSpan(sipSimpleWrapper *);}
static void dealloc_wxGBSpan(sipSimpleWrapper *sipSelf)
{
    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxGBSpan(sipGetAddress(sipSelf), 0);
    }
}


extern "C" {static void *init_type_wxGBSpan(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxGBSpan(sipSimpleWrapper *, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    ::wxGBSpan *sipCpp = SIP_NULLPTR;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, ""))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new ::wxGBSpan();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
            {
                delete sipCpp;
                return SIP_NULLPTR;
            }

            return sipCpp;
        }
    }

    {
        int rowspan;
        int colspan;

        static const char *sipKwdList[] = {
            sipName_rowspan,
            sipName_colspan,
        };

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, sipKwdList, sipUnused, "ii", &rowspan, &colspan))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new ::wxGBSpan(rowspan, colspan);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
            {
                delete sipCpp;
                return SIP_NULLPTR;
            }

            return sipCpp;
        }
    }

    {
        const ::wxGBSpan* a0;
        int a0State = 0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, "J1", sipType_wxGBSpan, &a0, &a0State))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new ::wxGBSpan(*a0);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxGBSpan *>(a0), sipType_wxGBSpan, a0State);

            return sipCpp;
        }
    }

    return SIP_NULLPTR;
}


extern "C" {static int convertTo_wxGBSpan(PyObject *, void **, int *, PyObject *);}
static int convertTo_wxGBSpan(PyObject *sipPy, void **sipCppPtrV, int *sipIsErr, PyObject *sipTransferObj)
{
    ::wxGBSpan **sipCppPtr = reinterpret_cast<::wxGBSpan **>(sipCppPtrV);
        // is it just a typecheck?
        if (!sipIsErr) {
            // is it already an instance of wxGBSpan?
            if (sipCanConvertToType(sipPy, sipType_wxGBSpan, SIP_NO_CONVERTORS))
                return 1;
        
            if (wxPyNumberSequenceCheck(sipPy, 2)) {
                return 1;
            }
            return 0;
        }
        
         // otherwise do the conversion
         if (sipCanConvertToType(sipPy, sipType_wxGBSpan, SIP_NO_CONVERTORS)) {
             // Just fetch the existing instance
             *sipCppPtr = reinterpret_cast<wxGBSpan*>(sipConvertToType(
                     sipPy, sipType_wxGBSpan, sipTransferObj, SIP_NO_CONVERTORS, 0, sipIsErr));
             return 0;  // not a new instance
         }
        
         // or create a new instance
         PyObject* o1 = PySequence_ITEM(sipPy, 0);
         PyObject* o2 = PySequence_ITEM(sipPy, 1);
         *sipCppPtr = new wxGBSpan(wxPyInt_AsLong(o1), wxPyInt_AsLong(o2));
         Py_DECREF(o1);
         Py_DECREF(o2);
         return SIP_TEMPORARY;
}


/* Define this type's Python slots. */
static sipPySlotDef slots_wxGBSpan[] = {
    {(void *)slot_wxGBSpan___eq__, eq_slot},
    {(void *)slot_wxGBSpan___ne__, ne_slot},
    {0, (sipPySlotType)0}
};


static PyMethodDef methods_wxGBSpan[] = {
    {sipName_Get, meth_wxGBSpan_Get, METH_VARARGS, doc_wxGBSpan_Get},
    {sipName_GetColspan, meth_wxGBSpan_GetColspan, METH_VARARGS, doc_wxGBSpan_GetColspan},
    {sipName_GetRowspan, meth_wxGBSpan_GetRowspan, METH_VARARGS, doc_wxGBSpan_GetRowspan},
    {sipName_Set, SIP_MLMETH_CAST(meth_wxGBSpan_Set), METH_VARARGS|METH_KEYWORDS, doc_wxGBSpan_Set},
    {sipName_SetColspan, SIP_MLMETH_CAST(meth_wxGBSpan_SetColspan), METH_VARARGS|METH_KEYWORDS, doc_wxGBSpan_SetColspan},
    {sipName_SetRowspan, SIP_MLMETH_CAST(meth_wxGBSpan_SetRowspan), METH_VARARGS|METH_KEYWORDS, doc_wxGBSpan_SetRowspan}
};

sipVariableDef variables_wxGBSpan[] = {
    {PropertyVariable, sipName_colspan, &methods_wxGBSpan[1], &methods_wxGBSpan[4], SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_rowspan, &methods_wxGBSpan[2], &methods_wxGBSpan[5], SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_Colspan, &methods_wxGBSpan[1], &methods_wxGBSpan[4], SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_Rowspan, &methods_wxGBSpan[2], &methods_wxGBSpan[5], SIP_NULLPTR, SIP_NULLPTR},
};

PyDoc_STRVAR(doc_wxGBSpan, "GBSpan() -> None\n"
"GBSpan(rowspan, colspan) -> None\n"
"\n"
"This class is used to hold the row and column spanning attributes of\n"
"items in a wxGridBagSizer.");


sipClassTypeDef sipTypeDef__core_wxGBSpan = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_CLASS,
        sipNameNr_wxGBSpan,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_GBSpan,
        {0, 0, 1},
        6, methods_wxGBSpan,
        0, SIP_NULLPTR,
        4, variables_wxGBSpan,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxGBSpan,
    -1,
    -1,
    SIP_NULLPTR,
    slots_wxGBSpan,
    init_type_wxGBSpan,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxGBSpan,
    assign_wxGBSpan,
    array_wxGBSpan,
    copy_wxGBSpan,
    release_wxGBSpan,
    SIP_NULLPTR,
    convertTo_wxGBSpan,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    array_delete_wxGBSpan,
    sizeof (::wxGBSpan),
};
