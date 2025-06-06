/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_propgrid.h"
        #include <wx/propgrid/props.h>
        #include <wx/propgrid/propgrid.h>
        #include <wx/validate.h>


PyDoc_STRVAR(doc_wxPGInDialogValidator_DoValidate, "DoValidate(propGrid, validator, value) -> bool");

extern "C" {static PyObject *meth_wxPGInDialogValidator_DoValidate(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxPGInDialogValidator_DoValidate(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxPropertyGrid* propGrid;
        ::wxValidator* validator;
        const ::wxString* value;
        int valueState = 0;
        ::wxPGInDialogValidator *sipCpp;

        static const char *sipKwdList[] = {
            sipName_propGrid,
            sipName_validator,
            sipName_value,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ8J8J1", &sipSelf, sipType_wxPGInDialogValidator, &sipCpp, sipType_wxPropertyGrid, &propGrid, sipType_wxValidator, &validator, sipType_wxString, &value, &valueState))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->DoValidate(propGrid, validator, *value);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(value), sipType_wxString, valueState);

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_PGInDialogValidator, sipName_DoValidate, SIP_NULLPTR);

    return SIP_NULLPTR;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxPGInDialogValidator(void *, int);}
static void release_wxPGInDialogValidator(void *sipCppV, int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast<::wxPGInDialogValidator *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void *array_wxPGInDialogValidator(Py_ssize_t);}
static void *array_wxPGInDialogValidator(Py_ssize_t sipNrElem)
{
    return new ::wxPGInDialogValidator[sipNrElem];
}


extern "C" {static void array_delete_wxPGInDialogValidator(void *);}
static void array_delete_wxPGInDialogValidator(void *sipCpp)
{
    delete[] reinterpret_cast<::wxPGInDialogValidator *>(sipCpp);
}


extern "C" {static void assign_wxPGInDialogValidator(void *, Py_ssize_t, void *);}
static void assign_wxPGInDialogValidator(void *sipDst, Py_ssize_t sipDstIdx, void *sipSrc)
{
    reinterpret_cast<::wxPGInDialogValidator *>(sipDst)[sipDstIdx] = *reinterpret_cast<::wxPGInDialogValidator *>(sipSrc);
}


extern "C" {static void *copy_wxPGInDialogValidator(const void *, Py_ssize_t);}
static void *copy_wxPGInDialogValidator(const void *sipSrc, Py_ssize_t sipSrcIdx)
{
    return new ::wxPGInDialogValidator(reinterpret_cast<const ::wxPGInDialogValidator *>(sipSrc)[sipSrcIdx]);
}


extern "C" {static void dealloc_wxPGInDialogValidator(sipSimpleWrapper *);}
static void dealloc_wxPGInDialogValidator(sipSimpleWrapper *sipSelf)
{
    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxPGInDialogValidator(sipGetAddress(sipSelf), 0);
    }
}


extern "C" {static void *init_type_wxPGInDialogValidator(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxPGInDialogValidator(sipSimpleWrapper *, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    ::wxPGInDialogValidator *sipCpp = SIP_NULLPTR;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, ""))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new ::wxPGInDialogValidator();
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
        const ::wxPGInDialogValidator* a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, "J9", sipType_wxPGInDialogValidator, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new ::wxPGInDialogValidator(*a0);
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    return SIP_NULLPTR;
}


static PyMethodDef methods_wxPGInDialogValidator[] = {
    {sipName_DoValidate, SIP_MLMETH_CAST(meth_wxPGInDialogValidator_DoValidate), METH_VARARGS|METH_KEYWORDS, doc_wxPGInDialogValidator_DoValidate}
};

PyDoc_STRVAR(doc_wxPGInDialogValidator, "PGInDialogValidator() -> None\n"
"\n"
"Creates and manages a temporary wxTextCtrl for validation purposes.");


sipClassTypeDef sipTypeDef__propgrid_wxPGInDialogValidator = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_CLASS,
        sipNameNr_wxPGInDialogValidator,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_PGInDialogValidator,
        {0, 0, 1},
        1, methods_wxPGInDialogValidator,
        0, SIP_NULLPTR,
        0, SIP_NULLPTR,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxPGInDialogValidator,
    -1,
    -1,
    SIP_NULLPTR,
    SIP_NULLPTR,
    init_type_wxPGInDialogValidator,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxPGInDialogValidator,
    assign_wxPGInDialogValidator,
    array_wxPGInDialogValidator,
    copy_wxPGInDialogValidator,
    release_wxPGInDialogValidator,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    array_delete_wxPGInDialogValidator,
    sizeof (::wxPGInDialogValidator),
};
