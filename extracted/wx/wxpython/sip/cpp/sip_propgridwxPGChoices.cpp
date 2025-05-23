/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_propgrid.h"
        #include <wx/propgrid/property.h>
        #include <wx/propgrid/property.h>
        #include <wx/propgrid/property.h>
    #include <wx/setup.h>
    #include <wxPython/wxpy_api.h>
        #include <wx/bitmap.h>


PyDoc_STRVAR(doc_wxPGChoices_Add, "Add(arr, arrint) -> None\n"
"Add(label, value=PG_INVALID_VALUE) -> PGChoiceEntry\n"
"Add(label, bitmap, value=PG_INVALID_VALUE) -> PGChoiceEntry\n"
"Add(entry) -> PGChoiceEntry\n"
"\n"
"This is an overloaded member function, provided for convenience. It\n"
"differs from the above function only in what argument(s) it accepts.\n"
"\n"
"\n"
"");

extern "C" {static PyObject *meth_wxPGChoices_Add(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_Add(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxArrayString* arr;
        int arrState = 0;
        const ::wxArrayInt* arrint;
        int arrintState = 0;
        ::wxPGChoices *sipCpp;

        static const char *sipKwdList[] = {
            sipName_arr,
            sipName_arrint,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1J1", &sipSelf, sipType_wxPGChoices, &sipCpp, sipType_wxArrayString, &arr, &arrState, sipType_wxArrayInt, &arrint, &arrintState))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->Add(*arr, *arrint);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxArrayString *>(arr), sipType_wxArrayString, arrState);
            sipReleaseType(const_cast<::wxArrayInt *>(arrint), sipType_wxArrayInt, arrintState);

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    {
        const ::wxString* label;
        int labelState = 0;
        int value = wxPG_INVALID_VALUE;
        ::wxPGChoices *sipCpp;

        static const char *sipKwdList[] = {
            sipName_label,
            sipName_value,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1|i", &sipSelf, sipType_wxPGChoices, &sipCpp, sipType_wxString, &label, &labelState, &value))
        {
            ::wxPGChoiceEntry*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = &sipCpp->Add(*label, value);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(label), sipType_wxString, labelState);

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxPGChoiceEntry, SIP_NULLPTR);
        }
    }

    {
        const ::wxString* label;
        int labelState = 0;
        const ::wxBitmap* bitmap;
        int value = wxPG_INVALID_VALUE;
        ::wxPGChoices *sipCpp;

        static const char *sipKwdList[] = {
            sipName_label,
            sipName_bitmap,
            sipName_value,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1J9|i", &sipSelf, sipType_wxPGChoices, &sipCpp, sipType_wxString, &label, &labelState, sipType_wxBitmap, &bitmap, &value))
        {
            ::wxPGChoiceEntry*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = &sipCpp->Add(*label, *bitmap, value);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(label), sipType_wxString, labelState);

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxPGChoiceEntry, SIP_NULLPTR);
        }
    }

    {
        const ::wxPGChoiceEntry* entry;
        ::wxPGChoices *sipCpp;

        static const char *sipKwdList[] = {
            sipName_entry,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ9", &sipSelf, sipType_wxPGChoices, &sipCpp, sipType_wxPGChoiceEntry, &entry))
        {
            ::wxPGChoiceEntry*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = &sipCpp->Add(*entry);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxPGChoiceEntry, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_Add, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoices_AddAsSorted, "AddAsSorted(label, value=PG_INVALID_VALUE) -> PGChoiceEntry\n"
"\n"
"Adds a single item, sorted.");

extern "C" {static PyObject *meth_wxPGChoices_AddAsSorted(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_AddAsSorted(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxString* label;
        int labelState = 0;
        int value = wxPG_INVALID_VALUE;
        ::wxPGChoices *sipCpp;

        static const char *sipKwdList[] = {
            sipName_label,
            sipName_value,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1|i", &sipSelf, sipType_wxPGChoices, &sipCpp, sipType_wxString, &label, &labelState, &value))
        {
            ::wxPGChoiceEntry*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = &sipCpp->AddAsSorted(*label, value);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(label), sipType_wxString, labelState);

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxPGChoiceEntry, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_AddAsSorted, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoices_Assign, "Assign(a) -> None\n"
"\n"
"Assigns choices data, using reference counting.");

extern "C" {static PyObject *meth_wxPGChoices_Assign(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_Assign(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxPGChoices* a;
        ::wxPGChoices *sipCpp;

        static const char *sipKwdList[] = {
            sipName_a,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ9", &sipSelf, sipType_wxPGChoices, &sipCpp, sipType_wxPGChoices, &a))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->Assign(*a);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_Assign, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoices_AssignData, "AssignData(data) -> None\n"
"\n"
"Assigns data from another set of choices.");

extern "C" {static PyObject *meth_wxPGChoices_AssignData(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_AssignData(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxPGChoicesData* data;
        ::wxPGChoices *sipCpp;

        static const char *sipKwdList[] = {
            sipName_data,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ8", &sipSelf, sipType_wxPGChoices, &sipCpp, sipType_wxPGChoicesData, &data))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->AssignData(data);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_AssignData, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoices_Clear, "Clear() -> None\n"
"\n"
"Deletes all items.");

extern "C" {static PyObject *meth_wxPGChoices_Clear(PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_Clear(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxPGChoices *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxPGChoices, &sipCpp))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->Clear();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_Clear, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoices_Copy, "Copy() -> PGChoices\n"
"\n"
"Returns a real copy of the choices.");

extern "C" {static PyObject *meth_wxPGChoices_Copy(PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_Copy(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxPGChoices *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxPGChoices, &sipCpp))
        {
            ::wxPGChoices*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxPGChoices(sipCpp->Copy());
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxPGChoices, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_Copy, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoices_EnsureData, "EnsureData() -> None");

extern "C" {static PyObject *meth_wxPGChoices_EnsureData(PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_EnsureData(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxPGChoices *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxPGChoices, &sipCpp))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->EnsureData();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_EnsureData, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoices_GetId, "GetId() -> IntPtr\n"
"\n"
"Gets an unsigned number identifying this list.");

extern "C" {static PyObject *meth_wxPGChoices_GetId(PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_GetId(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxPGChoices *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxPGChoices, &sipCpp))
        {
            ::wxIntPtr*sipRes = 0;
        sipRes = new  ::wxIntPtr((wxIntPtr)sipCpp->GetId());

            return sipConvertFromNewType(sipRes, sipType_wxIntPtr, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_GetId, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoices_GetLabel, "GetLabel(ind) -> str\n"
"\n"
"Returns label of item.");

extern "C" {static PyObject *meth_wxPGChoices_GetLabel(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_GetLabel(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        uint ind;
        const ::wxPGChoices *sipCpp;

        static const char *sipKwdList[] = {
            sipName_ind,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "Bu", &sipSelf, sipType_wxPGChoices, &sipCpp, &ind))
        {
            ::wxString*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxString(sipCpp->GetLabel(ind));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxString, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_GetLabel, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoices_GetCount, "GetCount() -> int\n"
"\n"
"Returns number of items.");

extern "C" {static PyObject *meth_wxPGChoices_GetCount(PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_GetCount(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxPGChoices *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxPGChoices, &sipCpp))
        {
            uint sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetCount();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyLong_FromUnsignedLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_GetCount, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoices_GetValue, "GetValue(ind) -> int\n"
"\n"
"Returns value of item.");

extern "C" {static PyObject *meth_wxPGChoices_GetValue(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_GetValue(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        uint ind;
        const ::wxPGChoices *sipCpp;

        static const char *sipKwdList[] = {
            sipName_ind,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "Bu", &sipSelf, sipType_wxPGChoices, &sipCpp, &ind))
        {
            int sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetValue(ind);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyLong_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_GetValue, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoices_GetValuesForStrings, "GetValuesForStrings(strings) -> List[int]\n"
"\n"
"Returns array of values matching the given strings.");

extern "C" {static PyObject *meth_wxPGChoices_GetValuesForStrings(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_GetValuesForStrings(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxArrayString* strings;
        int stringsState = 0;
        const ::wxPGChoices *sipCpp;

        static const char *sipKwdList[] = {
            sipName_strings,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1", &sipSelf, sipType_wxPGChoices, &sipCpp, sipType_wxArrayString, &strings, &stringsState))
        {
            ::wxArrayInt*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxArrayInt(sipCpp->GetValuesForStrings(*strings));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxArrayString *>(strings), sipType_wxArrayString, stringsState);

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxArrayInt, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_GetValuesForStrings, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoices_GetIndicesForStrings, "GetIndicesForStrings(strings, unmatched=None) -> List[int]\n"
"\n"
"Returns array of indices matching given strings.");

extern "C" {static PyObject *meth_wxPGChoices_GetIndicesForStrings(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_GetIndicesForStrings(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxArrayString* strings;
        int stringsState = 0;
        ::wxArrayString* unmatched = 0;
        int unmatchedState = 0;
        const ::wxPGChoices *sipCpp;

        static const char *sipKwdList[] = {
            sipName_strings,
            sipName_unmatched,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1|J0", &sipSelf, sipType_wxPGChoices, &sipCpp, sipType_wxArrayString, &strings, &stringsState, sipType_wxArrayString, &unmatched, &unmatchedState))
        {
            ::wxArrayInt*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxArrayInt(sipCpp->GetIndicesForStrings(*strings, unmatched));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxArrayString *>(strings), sipType_wxArrayString, stringsState);
            sipReleaseType(unmatched, sipType_wxArrayString, unmatchedState);

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxArrayInt, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_GetIndicesForStrings, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoices_Index, "Index(label) -> int\n"
"Index(val) -> int\n"
"\n"
"Returns index of item with given label.\n"
"");

extern "C" {static PyObject *meth_wxPGChoices_Index(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_Index(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxString* label;
        int labelState = 0;
        const ::wxPGChoices *sipCpp;

        static const char *sipKwdList[] = {
            sipName_label,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1", &sipSelf, sipType_wxPGChoices, &sipCpp, sipType_wxString, &label, &labelState))
        {
            int sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->Index(*label);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(label), sipType_wxString, labelState);

            if (PyErr_Occurred())
                return 0;

            return PyLong_FromLong(sipRes);
        }
    }

    {
        int val;
        const ::wxPGChoices *sipCpp;

        static const char *sipKwdList[] = {
            sipName_val,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "Bi", &sipSelf, sipType_wxPGChoices, &sipCpp, &val))
        {
            int sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->Index(val);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyLong_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_Index, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoices_Insert, "Insert(label, index, value=PG_INVALID_VALUE) -> PGChoiceEntry\n"
"Insert(entry, index) -> PGChoiceEntry\n"
"\n"
"Inserts a single item.\n"
"");

extern "C" {static PyObject *meth_wxPGChoices_Insert(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_Insert(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxString* label;
        int labelState = 0;
        int index;
        int value = wxPG_INVALID_VALUE;
        ::wxPGChoices *sipCpp;

        static const char *sipKwdList[] = {
            sipName_label,
            sipName_index,
            sipName_value,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1i|i", &sipSelf, sipType_wxPGChoices, &sipCpp, sipType_wxString, &label, &labelState, &index, &value))
        {
            ::wxPGChoiceEntry*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = &sipCpp->Insert(*label, index, value);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(label), sipType_wxString, labelState);

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxPGChoiceEntry, SIP_NULLPTR);
        }
    }

    {
        const ::wxPGChoiceEntry* entry;
        int index;
        ::wxPGChoices *sipCpp;

        static const char *sipKwdList[] = {
            sipName_entry,
            sipName_index,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ9i", &sipSelf, sipType_wxPGChoices, &sipCpp, sipType_wxPGChoiceEntry, &entry, &index))
        {
            ::wxPGChoiceEntry*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = &sipCpp->Insert(*entry, index);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxPGChoiceEntry, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_Insert, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoices_IsOk, "IsOk() -> bool\n"
"\n"
"Returns false if this is a constant empty set of choices, which should\n"
"not be modified.");

extern "C" {static PyObject *meth_wxPGChoices_IsOk(PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_IsOk(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxPGChoices *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxPGChoices, &sipCpp))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->IsOk();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_IsOk, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoices_Item, "Item(i) -> PGChoiceEntry\n"
"\n"
"Returns item at given index.");

extern "C" {static PyObject *meth_wxPGChoices_Item(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_Item(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        uint i;
        ::wxPGChoices *sipCpp;

        static const char *sipKwdList[] = {
            sipName_i,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "Bu", &sipSelf, sipType_wxPGChoices, &sipCpp, &i))
        {
            ::wxPGChoiceEntry*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = &sipCpp->Item(i);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxPGChoiceEntry, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_Item, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoices_RemoveAt, "RemoveAt(nIndex, count=1) -> None\n"
"\n"
"Removes count items starting at position nIndex.");

extern "C" {static PyObject *meth_wxPGChoices_RemoveAt(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_RemoveAt(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        size_t nIndex;
        size_t count = 1;
        ::wxPGChoices *sipCpp;

        static const char *sipKwdList[] = {
            sipName_nIndex,
            sipName_count,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "B=|=", &sipSelf, sipType_wxPGChoices, &sipCpp, &nIndex, &count))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->RemoveAt(nIndex, count);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_RemoveAt, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoices_Set, "Set(labels, values=[]) -> None\n"
"\n"
"This is an overloaded member function, provided for convenience. It\n"
"differs from the above function only in what argument(s) it accepts.");

extern "C" {static PyObject *meth_wxPGChoices_Set(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_Set(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxArrayString* labels;
        int labelsState = 0;
        const ::wxArrayInt& valuesdef = wxArrayInt();
        const ::wxArrayInt* values = &valuesdef;
        int valuesState = 0;
        ::wxPGChoices *sipCpp;

        static const char *sipKwdList[] = {
            sipName_labels,
            sipName_values,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1|J1", &sipSelf, sipType_wxPGChoices, &sipCpp, sipType_wxArrayString, &labels, &labelsState, sipType_wxArrayInt, &values, &valuesState))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->Set(*labels, *values);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxArrayString *>(labels), sipType_wxArrayString, labelsState);
            sipReleaseType(const_cast<::wxArrayInt *>(values), sipType_wxArrayInt, valuesState);

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_Set, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoices_AllocExclusive, "AllocExclusive() -> None\n"
"\n"
"Creates exclusive copy of current choices.");

extern "C" {static PyObject *meth_wxPGChoices_AllocExclusive(PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_AllocExclusive(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxPGChoices *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxPGChoices, &sipCpp))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->AllocExclusive();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_AllocExclusive, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoices_GetData, "GetData() -> PGChoicesData\n"
"\n"
"Returns data, increases refcount.");

extern "C" {static PyObject *meth_wxPGChoices_GetData(PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_GetData(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxPGChoices *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxPGChoices, &sipCpp))
        {
            ::wxPGChoicesData*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetData();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxPGChoicesData, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_GetData, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoices_GetDataPtr, "GetDataPtr() -> PGChoicesData\n"
"\n"
"Returns plain data ptr - no refcounting stuff is done.");

extern "C" {static PyObject *meth_wxPGChoices_GetDataPtr(PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_GetDataPtr(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxPGChoices *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxPGChoices, &sipCpp))
        {
            ::wxPGChoicesData*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetDataPtr();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxPGChoicesData, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_GetDataPtr, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoices_ExtractData, "ExtractData() -> PGChoicesData\n"
"\n"
"Changes ownership of data to you.");

extern "C" {static PyObject *meth_wxPGChoices_ExtractData(PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_ExtractData(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxPGChoices *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxPGChoices, &sipCpp))
        {
            ::wxPGChoicesData*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->ExtractData();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxPGChoicesData, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_ExtractData, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoices_GetLabels, "GetLabels() -> List[str]\n"
"\n"
"Returns array of choice labels.");

extern "C" {static PyObject *meth_wxPGChoices_GetLabels(PyObject *, PyObject *);}
static PyObject *meth_wxPGChoices_GetLabels(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxPGChoices *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxPGChoices, &sipCpp))
        {
            ::wxArrayString*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxArrayString(sipCpp->GetLabels());
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxArrayString, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoices, sipName_GetLabels, SIP_NULLPTR);

    return SIP_NULLPTR;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxPGChoices(void *, int);}
static void release_wxPGChoices(void *sipCppV, int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast<::wxPGChoices *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void *array_wxPGChoices(Py_ssize_t);}
static void *array_wxPGChoices(Py_ssize_t sipNrElem)
{
    return new ::wxPGChoices[sipNrElem];
}


extern "C" {static void array_delete_wxPGChoices(void *);}
static void array_delete_wxPGChoices(void *sipCpp)
{
    delete[] reinterpret_cast<::wxPGChoices *>(sipCpp);
}


extern "C" {static void assign_wxPGChoices(void *, Py_ssize_t, void *);}
static void assign_wxPGChoices(void *sipDst, Py_ssize_t sipDstIdx, void *sipSrc)
{
    reinterpret_cast<::wxPGChoices *>(sipDst)[sipDstIdx] = *reinterpret_cast<::wxPGChoices *>(sipSrc);
}


extern "C" {static void *copy_wxPGChoices(const void *, Py_ssize_t);}
static void *copy_wxPGChoices(const void *sipSrc, Py_ssize_t sipSrcIdx)
{
    return new ::wxPGChoices(reinterpret_cast<const ::wxPGChoices *>(sipSrc)[sipSrcIdx]);
}


extern "C" {static void dealloc_wxPGChoices(sipSimpleWrapper *);}
static void dealloc_wxPGChoices(sipSimpleWrapper *sipSelf)
{
    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxPGChoices(sipGetAddress(sipSelf), 0);
    }
}


extern "C" {static void *init_type_wxPGChoices(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxPGChoices(sipSimpleWrapper *, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    ::wxPGChoices *sipCpp = SIP_NULLPTR;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, ""))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new ::wxPGChoices();
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
        const ::wxPGChoices* a;

        static const char *sipKwdList[] = {
            sipName_a,
        };

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, sipKwdList, sipUnused, "J9", sipType_wxPGChoices, &a))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new ::wxPGChoices(*a);
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
        const ::wxArrayString* labels;
        int labelsState = 0;
        const ::wxArrayInt& valuesdef = wxArrayInt();
        const ::wxArrayInt* values = &valuesdef;
        int valuesState = 0;

        static const char *sipKwdList[] = {
            sipName_labels,
            sipName_values,
        };

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, sipKwdList, sipUnused, "J1|J1", sipType_wxArrayString, &labels, &labelsState, sipType_wxArrayInt, &values, &valuesState))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new ::wxPGChoices(*labels, *values);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxArrayString *>(labels), sipType_wxArrayString, labelsState);
            sipReleaseType(const_cast<::wxArrayInt *>(values), sipType_wxArrayInt, valuesState);

            if (PyErr_Occurred())
            {
                delete sipCpp;
                return SIP_NULLPTR;
            }

            return sipCpp;
        }
    }

    {
        ::wxPGChoicesData* data;

        static const char *sipKwdList[] = {
            sipName_data,
        };

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, sipKwdList, sipUnused, "J8", sipType_wxPGChoicesData, &data))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new ::wxPGChoices(data);
            Py_END_ALLOW_THREADS

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


static PyMethodDef methods_wxPGChoices[] = {
    {sipName_Add, SIP_MLMETH_CAST(meth_wxPGChoices_Add), METH_VARARGS|METH_KEYWORDS, doc_wxPGChoices_Add},
    {sipName_AddAsSorted, SIP_MLMETH_CAST(meth_wxPGChoices_AddAsSorted), METH_VARARGS|METH_KEYWORDS, doc_wxPGChoices_AddAsSorted},
    {sipName_AllocExclusive, meth_wxPGChoices_AllocExclusive, METH_VARARGS, doc_wxPGChoices_AllocExclusive},
    {sipName_Assign, SIP_MLMETH_CAST(meth_wxPGChoices_Assign), METH_VARARGS|METH_KEYWORDS, doc_wxPGChoices_Assign},
    {sipName_AssignData, SIP_MLMETH_CAST(meth_wxPGChoices_AssignData), METH_VARARGS|METH_KEYWORDS, doc_wxPGChoices_AssignData},
    {sipName_Clear, meth_wxPGChoices_Clear, METH_VARARGS, doc_wxPGChoices_Clear},
    {sipName_Copy, meth_wxPGChoices_Copy, METH_VARARGS, doc_wxPGChoices_Copy},
    {sipName_EnsureData, meth_wxPGChoices_EnsureData, METH_VARARGS, doc_wxPGChoices_EnsureData},
    {sipName_ExtractData, meth_wxPGChoices_ExtractData, METH_VARARGS, doc_wxPGChoices_ExtractData},
    {sipName_GetCount, meth_wxPGChoices_GetCount, METH_VARARGS, doc_wxPGChoices_GetCount},
    {sipName_GetData, meth_wxPGChoices_GetData, METH_VARARGS, doc_wxPGChoices_GetData},
    {sipName_GetDataPtr, meth_wxPGChoices_GetDataPtr, METH_VARARGS, doc_wxPGChoices_GetDataPtr},
    {sipName_GetId, meth_wxPGChoices_GetId, METH_VARARGS, doc_wxPGChoices_GetId},
    {sipName_GetIndicesForStrings, SIP_MLMETH_CAST(meth_wxPGChoices_GetIndicesForStrings), METH_VARARGS|METH_KEYWORDS, doc_wxPGChoices_GetIndicesForStrings},
    {sipName_GetLabel, SIP_MLMETH_CAST(meth_wxPGChoices_GetLabel), METH_VARARGS|METH_KEYWORDS, doc_wxPGChoices_GetLabel},
    {sipName_GetLabels, meth_wxPGChoices_GetLabels, METH_VARARGS, doc_wxPGChoices_GetLabels},
    {sipName_GetValue, SIP_MLMETH_CAST(meth_wxPGChoices_GetValue), METH_VARARGS|METH_KEYWORDS, doc_wxPGChoices_GetValue},
    {sipName_GetValuesForStrings, SIP_MLMETH_CAST(meth_wxPGChoices_GetValuesForStrings), METH_VARARGS|METH_KEYWORDS, doc_wxPGChoices_GetValuesForStrings},
    {sipName_Index, SIP_MLMETH_CAST(meth_wxPGChoices_Index), METH_VARARGS|METH_KEYWORDS, doc_wxPGChoices_Index},
    {sipName_Insert, SIP_MLMETH_CAST(meth_wxPGChoices_Insert), METH_VARARGS|METH_KEYWORDS, doc_wxPGChoices_Insert},
    {sipName_IsOk, meth_wxPGChoices_IsOk, METH_VARARGS, doc_wxPGChoices_IsOk},
    {sipName_Item, SIP_MLMETH_CAST(meth_wxPGChoices_Item), METH_VARARGS|METH_KEYWORDS, doc_wxPGChoices_Item},
    {sipName_RemoveAt, SIP_MLMETH_CAST(meth_wxPGChoices_RemoveAt), METH_VARARGS|METH_KEYWORDS, doc_wxPGChoices_RemoveAt},
    {sipName_Set, SIP_MLMETH_CAST(meth_wxPGChoices_Set), METH_VARARGS|METH_KEYWORDS, doc_wxPGChoices_Set}
};

sipVariableDef variables_wxPGChoices[] = {
    {PropertyVariable, sipName_Labels, &methods_wxPGChoices[15], SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_Id, &methods_wxPGChoices[12], SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_DataPtr, &methods_wxPGChoices[11], SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_Data, &methods_wxPGChoices[10], SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_Count, &methods_wxPGChoices[9], SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
};

PyDoc_STRVAR(doc_wxPGChoices, "PGChoices() -> None\n"
"PGChoices(a) -> None\n"
"PGChoices(labels, values=[]) -> None\n"
"PGChoices(data) -> None\n"
"\n"
"Helper class for managing choices of wxPropertyGrid properties.");


sipClassTypeDef sipTypeDef__propgrid_wxPGChoices = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_CLASS,
        sipNameNr_wxPGChoices,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_PGChoices,
        {0, 0, 1},
        24, methods_wxPGChoices,
        0, SIP_NULLPTR,
        5, variables_wxPGChoices,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxPGChoices,
    -1,
    -1,
    SIP_NULLPTR,
    SIP_NULLPTR,
    init_type_wxPGChoices,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxPGChoices,
    assign_wxPGChoices,
    array_wxPGChoices,
    copy_wxPGChoices,
    release_wxPGChoices,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    array_delete_wxPGChoices,
    sizeof (::wxPGChoices),
};
