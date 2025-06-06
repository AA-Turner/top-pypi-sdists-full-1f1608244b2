/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_core.h"
        #include <wx/power.h>



PyDoc_STRVAR(doc_wxPowerResourceBlocker_IsInEffect, "IsInEffect() -> bool\n"
"\n"
"Returns whether the power resource could be acquired.");

extern "C" {static PyObject *meth_wxPowerResourceBlocker_IsInEffect(PyObject *, PyObject *);}
static PyObject *meth_wxPowerResourceBlocker_IsInEffect(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxPowerResourceBlocker *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxPowerResourceBlocker, &sipCpp))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->IsInEffect();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_PowerResourceBlocker, sipName_IsInEffect, SIP_NULLPTR);

    return SIP_NULLPTR;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxPowerResourceBlocker(void *, int);}
static void release_wxPowerResourceBlocker(void *sipCppV, int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast<::wxPowerResourceBlocker *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void dealloc_wxPowerResourceBlocker(sipSimpleWrapper *);}
static void dealloc_wxPowerResourceBlocker(sipSimpleWrapper *sipSelf)
{
    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxPowerResourceBlocker(sipGetAddress(sipSelf), 0);
    }
}


extern "C" {static void *init_type_wxPowerResourceBlocker(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxPowerResourceBlocker(sipSimpleWrapper *, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    ::wxPowerResourceBlocker *sipCpp = SIP_NULLPTR;

    {
        ::wxPowerResourceKind kind;
        const ::wxString& reasondef = wxString();
        const ::wxString* reason = &reasondef;
        int reasonState = 0;

        static const char *sipKwdList[] = {
            sipName_kind,
            sipName_reason,
        };

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, sipKwdList, sipUnused, "E|J1", sipType_wxPowerResourceKind, &kind, sipType_wxString, &reason, &reasonState))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new ::wxPowerResourceBlocker(kind, *reason);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(reason), sipType_wxString, reasonState);

            if (PyErr_Occurred())
            {
                delete sipCpp;
                return SIP_NULLPTR;
            }

            return sipCpp;
        }
    }

    return SIP_NULLPTR;
}


static PyMethodDef methods_wxPowerResourceBlocker[] = {
    {sipName_IsInEffect, meth_wxPowerResourceBlocker_IsInEffect, METH_VARARGS, doc_wxPowerResourceBlocker_IsInEffect}
};

PyDoc_STRVAR(doc_wxPowerResourceBlocker, "PowerResourceBlocker(kind, reason=\"\") -> None\n"
"\n"
"Helper RAII class ensuring that power resources are released.");


sipClassTypeDef sipTypeDef__core_wxPowerResourceBlocker = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_CLASS,
        sipNameNr_wxPowerResourceBlocker,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_PowerResourceBlocker,
        {0, 0, 1},
        1, methods_wxPowerResourceBlocker,
        0, SIP_NULLPTR,
        0, SIP_NULLPTR,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxPowerResourceBlocker,
    -1,
    -1,
    SIP_NULLPTR,
    SIP_NULLPTR,
    init_type_wxPowerResourceBlocker,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxPowerResourceBlocker,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    release_wxPowerResourceBlocker,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    sizeof (::wxPowerResourceBlocker),
};
