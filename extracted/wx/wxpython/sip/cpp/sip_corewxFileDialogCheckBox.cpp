/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_core.h"
        #include <wx/filedlgcustomize.h>
        #include <wx/event.h>
        #include <wx/eventfilter.h>
        #include <wx/event.h>
        #include <wx/object.h>
        #include <wx/object.h>
        #include <wx/object.h>


PyDoc_STRVAR(doc_wxFileDialogCheckBox_GetValue, "GetValue() -> bool\n"
"\n"
"Return true if the checkbox is checked.");

extern "C" {static PyObject *meth_wxFileDialogCheckBox_GetValue(PyObject *, PyObject *);}
static PyObject *meth_wxFileDialogCheckBox_GetValue(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxFileDialogCheckBox *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxFileDialogCheckBox, &sipCpp))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetValue();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_FileDialogCheckBox, sipName_GetValue, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxFileDialogCheckBox_SetValue, "SetValue(value) -> None\n"
"\n"
"Check or uncheck the checkbox.");

extern "C" {static PyObject *meth_wxFileDialogCheckBox_SetValue(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxFileDialogCheckBox_SetValue(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        bool value;
        ::wxFileDialogCheckBox *sipCpp;

        static const char *sipKwdList[] = {
            sipName_value,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "Bb", &sipSelf, sipType_wxFileDialogCheckBox, &sipCpp, &value))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetValue(value);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_FileDialogCheckBox, sipName_SetValue, SIP_NULLPTR);

    return SIP_NULLPTR;
}


/* Cast a pointer to a type somewhere in its inheritance hierarchy. */
extern "C" {static void *cast_wxFileDialogCheckBox(void *, const sipTypeDef *);}
static void *cast_wxFileDialogCheckBox(void *sipCppV, const sipTypeDef *targetType)
{
    ::wxFileDialogCheckBox *sipCpp = reinterpret_cast<::wxFileDialogCheckBox *>(sipCppV);

    if (targetType == sipType_wxFileDialogCheckBox)
        return sipCppV;

    sipCppV = ((const sipClassTypeDef *)sipType_wxFileDialogCustomControl)->ctd_cast(static_cast<::wxFileDialogCustomControl *>(sipCpp), targetType);
    if (sipCppV)
        return sipCppV;

    return SIP_NULLPTR;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxFileDialogCheckBox(void *, int);}
static void release_wxFileDialogCheckBox(void *sipCppV, int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast<::wxFileDialogCheckBox *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void dealloc_wxFileDialogCheckBox(sipSimpleWrapper *);}
static void dealloc_wxFileDialogCheckBox(sipSimpleWrapper *sipSelf)
{
    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxFileDialogCheckBox(sipGetAddress(sipSelf), 0);
    }
}


/* Define this type's super-types. */
static sipEncodedTypeDef supers_wxFileDialogCheckBox[] = {{171, 255, 1}};


static PyMethodDef methods_wxFileDialogCheckBox[] = {
    {sipName_GetValue, meth_wxFileDialogCheckBox_GetValue, METH_VARARGS, doc_wxFileDialogCheckBox_GetValue},
    {sipName_SetValue, SIP_MLMETH_CAST(meth_wxFileDialogCheckBox_SetValue), METH_VARARGS|METH_KEYWORDS, doc_wxFileDialogCheckBox_SetValue}
};

sipVariableDef variables_wxFileDialogCheckBox[] = {
    {PropertyVariable, sipName_Value, &methods_wxFileDialogCheckBox[0], &methods_wxFileDialogCheckBox[1], SIP_NULLPTR, SIP_NULLPTR},
};

PyDoc_STRVAR(doc_wxFileDialogCheckBox, "Represents a custom checkbox inside wxFileDialog.");


sipClassTypeDef sipTypeDef__core_wxFileDialogCheckBox = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_SCC|SIP_TYPE_CLASS,
        sipNameNr_wxFileDialogCheckBox,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_FileDialogCheckBox,
        {0, 0, 1},
        2, methods_wxFileDialogCheckBox,
        0, SIP_NULLPTR,
        1, variables_wxFileDialogCheckBox,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxFileDialogCheckBox,
    -1,
    -1,
    supers_wxFileDialogCheckBox,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxFileDialogCheckBox,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    release_wxFileDialogCheckBox,
    cast_wxFileDialogCheckBox,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    0,
};
