/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_propgrid.h"
        #include <wx/propgrid/editors.h>
        #include <wx/propgrid/propgrid.h>
        #include <wx/propgrid/property.h>
        #include <wx/object.h>
        #include <wx/object.h>
        #include <wx/object.h>


class sipwxPGEditorDialogAdapter : public ::wxPGEditorDialogAdapter
{
public:
    sipwxPGEditorDialogAdapter();
    sipwxPGEditorDialogAdapter(const ::wxPGEditorDialogAdapter&);
    virtual ~sipwxPGEditorDialogAdapter();

    /*
     * There is a protected method for every virtual method visible from
     * this class.
     */
protected:
    bool DoShowDialog(::wxPropertyGrid*, ::wxPGProperty*) SIP_OVERRIDE;

public:
    sipSimpleWrapper *sipPySelf;

private:
    sipwxPGEditorDialogAdapter(const sipwxPGEditorDialogAdapter &);
    sipwxPGEditorDialogAdapter &operator = (const sipwxPGEditorDialogAdapter &);

    char sipPyMethods[1];
};

sipwxPGEditorDialogAdapter::sipwxPGEditorDialogAdapter(): ::wxPGEditorDialogAdapter(), sipPySelf(SIP_NULLPTR)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipwxPGEditorDialogAdapter::sipwxPGEditorDialogAdapter(const ::wxPGEditorDialogAdapter& a0): ::wxPGEditorDialogAdapter(a0), sipPySelf(SIP_NULLPTR)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipwxPGEditorDialogAdapter::~sipwxPGEditorDialogAdapter()
{
    sipInstanceDestroyedEx(&sipPySelf);
}

bool sipwxPGEditorDialogAdapter::DoShowDialog(::wxPropertyGrid*propGrid, ::wxPGProperty*property)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[0], &sipPySelf, sipName_PGEditorDialogAdapter, sipName_DoShowDialog);

    if (!sipMeth)
        return 0;

    extern bool sipVH__propgrid_35(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxPropertyGrid*, ::wxPGProperty*);

    return sipVH__propgrid_35(sipGILState, 0, sipPySelf, sipMeth, propGrid, property);
}


PyDoc_STRVAR(doc_wxPGEditorDialogAdapter_ShowDialog, "ShowDialog(propGrid, property) -> bool");

extern "C" {static PyObject *meth_wxPGEditorDialogAdapter_ShowDialog(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxPGEditorDialogAdapter_ShowDialog(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxPropertyGrid* propGrid;
        ::wxPGProperty* property;
        ::wxPGEditorDialogAdapter *sipCpp;

        static const char *sipKwdList[] = {
            sipName_propGrid,
            sipName_property,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ8J8", &sipSelf, sipType_wxPGEditorDialogAdapter, &sipCpp, sipType_wxPropertyGrid, &propGrid, sipType_wxPGProperty, &property))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->ShowDialog(propGrid, property);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_PGEditorDialogAdapter, sipName_ShowDialog, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGEditorDialogAdapter_DoShowDialog, "DoShowDialog(propGrid, property) -> bool");

extern "C" {static PyObject *meth_wxPGEditorDialogAdapter_DoShowDialog(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxPGEditorDialogAdapter_DoShowDialog(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    PyObject *sipOrigSelf = sipSelf;

    {
        ::wxPropertyGrid* propGrid;
        ::wxPGProperty* property;
        ::wxPGEditorDialogAdapter *sipCpp;

        static const char *sipKwdList[] = {
            sipName_propGrid,
            sipName_property,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ8J8", &sipSelf, sipType_wxPGEditorDialogAdapter, &sipCpp, sipType_wxPropertyGrid, &propGrid, sipType_wxPGProperty, &property))
        {
            bool sipRes;

            if (!sipOrigSelf)
            {
                sipAbstractMethod(sipName_PGEditorDialogAdapter, sipName_DoShowDialog);
                return SIP_NULLPTR;
            }

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->DoShowDialog(propGrid, property);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_PGEditorDialogAdapter, sipName_DoShowDialog, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGEditorDialogAdapter_SetValue, "SetValue(value) -> None");

extern "C" {static PyObject *meth_wxPGEditorDialogAdapter_SetValue(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxPGEditorDialogAdapter_SetValue(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxPGVariant* value;
        int valueState = 0;
        ::wxPGEditorDialogAdapter *sipCpp;

        static const char *sipKwdList[] = {
            sipName_value,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1", &sipSelf, sipType_wxPGEditorDialogAdapter, &sipCpp, sipType_wxPGVariant, &value, &valueState))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetValue(*value);
            Py_END_ALLOW_THREADS
            sipReleaseType(value, sipType_wxPGVariant, valueState);

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_PGEditorDialogAdapter, sipName_SetValue, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGEditorDialogAdapter_GetValue, "GetValue() -> PGVariant\n"
"\n"
"This method is typically only used if deriving class from existing\n"
"adapter with value conversion purposes.");

extern "C" {static PyObject *meth_wxPGEditorDialogAdapter_GetValue(PyObject *, PyObject *);}
static PyObject *meth_wxPGEditorDialogAdapter_GetValue(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxPGEditorDialogAdapter *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxPGEditorDialogAdapter, &sipCpp))
        {
            ::wxPGVariant*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = &sipCpp->GetValue();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxPGVariant, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_PGEditorDialogAdapter, sipName_GetValue, SIP_NULLPTR);

    return SIP_NULLPTR;
}


/* Cast a pointer to a type somewhere in its inheritance hierarchy. */
extern "C" {static void *cast_wxPGEditorDialogAdapter(void *, const sipTypeDef *);}
static void *cast_wxPGEditorDialogAdapter(void *sipCppV, const sipTypeDef *targetType)
{
    ::wxPGEditorDialogAdapter *sipCpp = reinterpret_cast<::wxPGEditorDialogAdapter *>(sipCppV);

    if (targetType == sipType_wxPGEditorDialogAdapter)
        return sipCppV;

    if (targetType == sipType_wxObject)
        return static_cast<::wxObject *>(sipCpp);

    return SIP_NULLPTR;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxPGEditorDialogAdapter(void *, int);}
static void release_wxPGEditorDialogAdapter(void *sipCppV, int sipState)
{
    Py_BEGIN_ALLOW_THREADS

    if (sipState & SIP_DERIVED_CLASS)
        delete reinterpret_cast<sipwxPGEditorDialogAdapter *>(sipCppV);
    else
        delete reinterpret_cast<::wxPGEditorDialogAdapter *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void dealloc_wxPGEditorDialogAdapter(sipSimpleWrapper *);}
static void dealloc_wxPGEditorDialogAdapter(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerivedClass(sipSelf))
        reinterpret_cast<sipwxPGEditorDialogAdapter *>(sipGetAddress(sipSelf))->sipPySelf = SIP_NULLPTR;

    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxPGEditorDialogAdapter(sipGetAddress(sipSelf), sipIsDerivedClass(sipSelf));
    }
}


extern "C" {static void *init_type_wxPGEditorDialogAdapter(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxPGEditorDialogAdapter(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    sipwxPGEditorDialogAdapter *sipCpp = SIP_NULLPTR;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, ""))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipwxPGEditorDialogAdapter();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
            {
                delete sipCpp;
                return SIP_NULLPTR;
            }

            sipCpp->sipPySelf = sipSelf;

            return sipCpp;
        }
    }

    {
        const ::wxPGEditorDialogAdapter* a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, "J9", sipType_wxPGEditorDialogAdapter, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipwxPGEditorDialogAdapter(*a0);
            Py_END_ALLOW_THREADS

            sipCpp->sipPySelf = sipSelf;

            return sipCpp;
        }
    }

    return SIP_NULLPTR;
}


/* Define this type's super-types. */
static sipEncodedTypeDef supers_wxPGEditorDialogAdapter[] = {{20, 0, 1}};


static PyMethodDef methods_wxPGEditorDialogAdapter[] = {
    {sipName_DoShowDialog, SIP_MLMETH_CAST(meth_wxPGEditorDialogAdapter_DoShowDialog), METH_VARARGS|METH_KEYWORDS, doc_wxPGEditorDialogAdapter_DoShowDialog},
    {sipName_GetValue, meth_wxPGEditorDialogAdapter_GetValue, METH_VARARGS, doc_wxPGEditorDialogAdapter_GetValue},
    {sipName_SetValue, SIP_MLMETH_CAST(meth_wxPGEditorDialogAdapter_SetValue), METH_VARARGS|METH_KEYWORDS, doc_wxPGEditorDialogAdapter_SetValue},
    {sipName_ShowDialog, SIP_MLMETH_CAST(meth_wxPGEditorDialogAdapter_ShowDialog), METH_VARARGS|METH_KEYWORDS, doc_wxPGEditorDialogAdapter_ShowDialog}
};


extern "C" {static PyObject *varget_wxPGEditorDialogAdapter_m_clientData(void *, PyObject *, PyObject *);}
static PyObject *varget_wxPGEditorDialogAdapter_m_clientData(void *sipSelf, PyObject *, PyObject *)
{
    void*sipVal;
    ::wxPGEditorDialogAdapter *sipCpp = reinterpret_cast<::wxPGEditorDialogAdapter *>(sipSelf);

    sipVal = sipCpp->m_clientData;

    return sipConvertFromVoidPtr(sipVal);
}


extern "C" {static int varset_wxPGEditorDialogAdapter_m_clientData(void *, PyObject *, PyObject *);}
static int varset_wxPGEditorDialogAdapter_m_clientData(void *sipSelf, PyObject *sipPy, PyObject *)
{
    void*sipVal;
    ::wxPGEditorDialogAdapter *sipCpp = reinterpret_cast<::wxPGEditorDialogAdapter *>(sipSelf);

    sipVal = sipConvertToVoidPtr(sipPy);

    if (PyErr_Occurred() != SIP_NULLPTR)
        return -1;

    sipCpp->m_clientData = sipVal;

    return 0;
}

sipVariableDef variables_wxPGEditorDialogAdapter[] = {
    {PropertyVariable, sipName_Value, &methods_wxPGEditorDialogAdapter[1], &methods_wxPGEditorDialogAdapter[2], SIP_NULLPTR, SIP_NULLPTR},
    {InstanceVariable, sipName_m_clientData, (PyMethodDef *)varget_wxPGEditorDialogAdapter_m_clientData, (PyMethodDef *)varset_wxPGEditorDialogAdapter_m_clientData, SIP_NULLPTR, SIP_NULLPTR},
};

PyDoc_STRVAR(doc_wxPGEditorDialogAdapter, "PGEditorDialogAdapter() -> None\n"
"\n"
"Derive a class from this to adapt an existing editor dialog or\n"
"function to be used when editor button of a property is pushed.");


sipClassTypeDef sipTypeDef__propgrid_wxPGEditorDialogAdapter = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_ABSTRACT|SIP_TYPE_SCC|SIP_TYPE_CLASS,
        sipNameNr_wxPGEditorDialogAdapter,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_PGEditorDialogAdapter,
        {0, 0, 1},
        4, methods_wxPGEditorDialogAdapter,
        0, SIP_NULLPTR,
        2, variables_wxPGEditorDialogAdapter,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxPGEditorDialogAdapter,
    -1,
    -1,
    supers_wxPGEditorDialogAdapter,
    SIP_NULLPTR,
    init_type_wxPGEditorDialogAdapter,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxPGEditorDialogAdapter,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    release_wxPGEditorDialogAdapter,
    cast_wxPGEditorDialogAdapter,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    sizeof (::wxPGEditorDialogAdapter),
};
