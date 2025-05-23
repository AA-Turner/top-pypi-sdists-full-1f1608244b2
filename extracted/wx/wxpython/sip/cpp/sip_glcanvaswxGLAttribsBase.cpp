/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_glcanvas.h"
        #include <wx/glcanvas.h>



PyDoc_STRVAR(doc_wxGLAttribsBase_AddAttribute, "AddAttribute(attribute) -> None\n"
"\n"
"Adds an integer value to the list of attributes.");

extern "C" {static PyObject *meth_wxGLAttribsBase_AddAttribute(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxGLAttribsBase_AddAttribute(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        int attribute;
        ::wxGLAttribsBase *sipCpp;

        static const char *sipKwdList[] = {
            sipName_attribute,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "Bi", &sipSelf, sipType_wxGLAttribsBase, &sipCpp, &attribute))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->AddAttribute(attribute);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_GLAttribsBase, sipName_AddAttribute, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGLAttribsBase_AddAttribBits, "AddAttribBits(searchVal, combineVal) -> None\n"
"\n"
"Combine (bitwise OR) a given value with the existing one, if any.");

extern "C" {static PyObject *meth_wxGLAttribsBase_AddAttribBits(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxGLAttribsBase_AddAttribBits(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        int searchVal;
        int combineVal;
        ::wxGLAttribsBase *sipCpp;

        static const char *sipKwdList[] = {
            sipName_searchVal,
            sipName_combineVal,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "Bii", &sipSelf, sipType_wxGLAttribsBase, &sipCpp, &searchVal, &combineVal))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->AddAttribBits(searchVal, combineVal);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_GLAttribsBase, sipName_AddAttribBits, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGLAttribsBase_SetNeedsARB, "SetNeedsARB(needsARB=True) -> None\n"
"\n"
"Sets the necessity of using special ARB-functions (e.g.");

extern "C" {static PyObject *meth_wxGLAttribsBase_SetNeedsARB(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxGLAttribsBase_SetNeedsARB(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        bool needsARB = 1;
        ::wxGLAttribsBase *sipCpp;

        static const char *sipKwdList[] = {
            sipName_needsARB,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "B|b", &sipSelf, sipType_wxGLAttribsBase, &sipCpp, &needsARB))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetNeedsARB(needsARB);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_GLAttribsBase, sipName_SetNeedsARB, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGLAttribsBase_Reset, "Reset() -> None\n"
"\n"
"Delete contents and sets ARB-flag to false.");

extern "C" {static PyObject *meth_wxGLAttribsBase_Reset(PyObject *, PyObject *);}
static PyObject *meth_wxGLAttribsBase_Reset(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxGLAttribsBase *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGLAttribsBase, &sipCpp))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->Reset();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_GLAttribsBase, sipName_Reset, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGLAttribsBase_GetSize, "GetSize() -> int\n"
"\n"
"Returns the size of the internal list of attributes.");

extern "C" {static PyObject *meth_wxGLAttribsBase_GetSize(PyObject *, PyObject *);}
static PyObject *meth_wxGLAttribsBase_GetSize(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxGLAttribsBase *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGLAttribsBase, &sipCpp))
        {
            int sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetSize();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyLong_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_GLAttribsBase, sipName_GetSize, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGLAttribsBase_NeedsARB, "NeedsARB() -> bool\n"
"\n"
"Returns the current value of the ARB-flag.");

extern "C" {static PyObject *meth_wxGLAttribsBase_NeedsARB(PyObject *, PyObject *);}
static PyObject *meth_wxGLAttribsBase_NeedsARB(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxGLAttribsBase *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGLAttribsBase, &sipCpp))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->NeedsARB();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_GLAttribsBase, sipName_NeedsARB, SIP_NULLPTR);

    return SIP_NULLPTR;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxGLAttribsBase(void *, int);}
static void release_wxGLAttribsBase(void *sipCppV, int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast<::wxGLAttribsBase *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void *array_wxGLAttribsBase(Py_ssize_t);}
static void *array_wxGLAttribsBase(Py_ssize_t sipNrElem)
{
    return new ::wxGLAttribsBase[sipNrElem];
}


extern "C" {static void array_delete_wxGLAttribsBase(void *);}
static void array_delete_wxGLAttribsBase(void *sipCpp)
{
    delete[] reinterpret_cast<::wxGLAttribsBase *>(sipCpp);
}


extern "C" {static void assign_wxGLAttribsBase(void *, Py_ssize_t, void *);}
static void assign_wxGLAttribsBase(void *sipDst, Py_ssize_t sipDstIdx, void *sipSrc)
{
    reinterpret_cast<::wxGLAttribsBase *>(sipDst)[sipDstIdx] = *reinterpret_cast<::wxGLAttribsBase *>(sipSrc);
}


extern "C" {static void *copy_wxGLAttribsBase(const void *, Py_ssize_t);}
static void *copy_wxGLAttribsBase(const void *sipSrc, Py_ssize_t sipSrcIdx)
{
    return new ::wxGLAttribsBase(reinterpret_cast<const ::wxGLAttribsBase *>(sipSrc)[sipSrcIdx]);
}


extern "C" {static void dealloc_wxGLAttribsBase(sipSimpleWrapper *);}
static void dealloc_wxGLAttribsBase(sipSimpleWrapper *sipSelf)
{
    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxGLAttribsBase(sipGetAddress(sipSelf), 0);
    }
}


extern "C" {static void *init_type_wxGLAttribsBase(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxGLAttribsBase(sipSimpleWrapper *, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    ::wxGLAttribsBase *sipCpp = SIP_NULLPTR;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, ""))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new ::wxGLAttribsBase();
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
        const ::wxGLAttribsBase* a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, "J9", sipType_wxGLAttribsBase, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new ::wxGLAttribsBase(*a0);
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    return SIP_NULLPTR;
}


static PyMethodDef methods_wxGLAttribsBase[] = {
    {sipName_AddAttribBits, SIP_MLMETH_CAST(meth_wxGLAttribsBase_AddAttribBits), METH_VARARGS|METH_KEYWORDS, doc_wxGLAttribsBase_AddAttribBits},
    {sipName_AddAttribute, SIP_MLMETH_CAST(meth_wxGLAttribsBase_AddAttribute), METH_VARARGS|METH_KEYWORDS, doc_wxGLAttribsBase_AddAttribute},
    {sipName_GetSize, meth_wxGLAttribsBase_GetSize, METH_VARARGS, doc_wxGLAttribsBase_GetSize},
    {sipName_NeedsARB, meth_wxGLAttribsBase_NeedsARB, METH_VARARGS, doc_wxGLAttribsBase_NeedsARB},
    {sipName_Reset, meth_wxGLAttribsBase_Reset, METH_VARARGS, doc_wxGLAttribsBase_Reset},
    {sipName_SetNeedsARB, SIP_MLMETH_CAST(meth_wxGLAttribsBase_SetNeedsARB), METH_VARARGS|METH_KEYWORDS, doc_wxGLAttribsBase_SetNeedsARB}
};

sipVariableDef variables_wxGLAttribsBase[] = {
    {PropertyVariable, sipName_Size, &methods_wxGLAttribsBase[2], SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
};

PyDoc_STRVAR(doc_wxGLAttribsBase, "GLAttribsBase() -> None\n"
"\n"
"This is the base class for wxGLAttributes and wxGLContextAttrs.");


sipClassTypeDef sipTypeDef__glcanvas_wxGLAttribsBase = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_CLASS,
        sipNameNr_wxGLAttribsBase,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_GLAttribsBase,
        {0, 0, 1},
        6, methods_wxGLAttribsBase,
        0, SIP_NULLPTR,
        1, variables_wxGLAttribsBase,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxGLAttribsBase,
    -1,
    -1,
    SIP_NULLPTR,
    SIP_NULLPTR,
    init_type_wxGLAttribsBase,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxGLAttribsBase,
    assign_wxGLAttribsBase,
    array_wxGLAttribsBase,
    copy_wxGLAttribsBase,
    release_wxGLAttribsBase,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    array_delete_wxGLAttribsBase,
    sizeof (::wxGLAttribsBase),
};
