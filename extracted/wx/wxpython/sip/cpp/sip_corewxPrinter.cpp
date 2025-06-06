/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_core.h"
        #include <wx/print.h>
        #include <wx/cmndata.h>
        #include <wx/window.h>
        #include <wx/print.h>
        #include <wx/dc.h>
        #include <wx/print.h>
        #include <wx/object.h>
        #include <wx/object.h>
        #include <wx/object.h>


class sipwxPrinter : public ::wxPrinter
{
public:
    sipwxPrinter(::wxPrintDialogData*);
    virtual ~sipwxPrinter();

    /*
     * There is a protected method for every virtual method visible from
     * this class.
     */
protected:
    bool Setup(::wxWindow*) SIP_OVERRIDE;
    void ReportError(::wxWindow*, ::wxPrintout*, const ::wxString&) SIP_OVERRIDE;
    ::wxDC* PrintDialog(::wxWindow*) SIP_OVERRIDE;
    bool Print(::wxWindow*, ::wxPrintout*, bool) SIP_OVERRIDE;
    ::wxPrintDialogData& GetPrintDialogData() const SIP_OVERRIDE;
    ::wxPrintAbortDialog* CreateAbortWindow(::wxWindow*, ::wxPrintout*) SIP_OVERRIDE;

public:
    sipSimpleWrapper *sipPySelf;

private:
    sipwxPrinter(const sipwxPrinter &);
    sipwxPrinter &operator = (const sipwxPrinter &);

    char sipPyMethods[6];
};

sipwxPrinter::sipwxPrinter(::wxPrintDialogData*data): ::wxPrinter(data), sipPySelf(SIP_NULLPTR)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipwxPrinter::~sipwxPrinter()
{
    sipInstanceDestroyedEx(&sipPySelf);
}

bool sipwxPrinter::Setup(::wxWindow*parent)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[0], &sipPySelf, SIP_NULLPTR, sipName_Setup);

    if (!sipMeth)
        return ::wxPrinter::Setup(parent);

    extern bool sipVH__core_139(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxWindow*);

    return sipVH__core_139(sipGILState, 0, sipPySelf, sipMeth, parent);
}

void sipwxPrinter::ReportError(::wxWindow*parent, ::wxPrintout*printout, const ::wxString& message)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[1], &sipPySelf, SIP_NULLPTR, sipName_ReportError);

    if (!sipMeth)
    {
        ::wxPrinter::ReportError(parent, printout, message);
        return;
    }

    extern void sipVH__core_227(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxWindow*, ::wxPrintout*, const ::wxString&);

    sipVH__core_227(sipGILState, 0, sipPySelf, sipMeth, parent, printout, message);
}

::wxDC* sipwxPrinter::PrintDialog(::wxWindow*parent)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[2], &sipPySelf, SIP_NULLPTR, sipName_PrintDialog);

    if (!sipMeth)
        return ::wxPrinter::PrintDialog(parent);

    extern ::wxDC* sipVH__core_226(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxWindow*);

    return sipVH__core_226(sipGILState, 0, sipPySelf, sipMeth, parent);
}

bool sipwxPrinter::Print(::wxWindow*parent, ::wxPrintout*printout, bool prompt)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[3], &sipPySelf, SIP_NULLPTR, sipName_Print);

    if (!sipMeth)
        return ::wxPrinter::Print(parent, printout, prompt);

    extern bool sipVH__core_225(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxWindow*, ::wxPrintout*, bool);

    return sipVH__core_225(sipGILState, 0, sipPySelf, sipMeth, parent, printout, prompt);
}

::wxPrintDialogData& sipwxPrinter::GetPrintDialogData() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[4]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_GetPrintDialogData);

    if (!sipMeth)
        return ::wxPrinter::GetPrintDialogData();

    extern ::wxPrintDialogData& sipVH__core_224(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__core_224(sipGILState, 0, sipPySelf, sipMeth);
}

::wxPrintAbortDialog* sipwxPrinter::CreateAbortWindow(::wxWindow*parent, ::wxPrintout*printout)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[5], &sipPySelf, SIP_NULLPTR, sipName_CreateAbortWindow);

    if (!sipMeth)
        return ::wxPrinter::CreateAbortWindow(parent, printout);

    extern ::wxPrintAbortDialog* sipVH__core_223(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxWindow*, ::wxPrintout*);

    return sipVH__core_223(sipGILState, 0, sipPySelf, sipMeth, parent, printout);
}


PyDoc_STRVAR(doc_wxPrinter_CreateAbortWindow, "CreateAbortWindow(parent, printout) -> PrintAbortDialog\n"
"\n"
"Creates the default printing abort window, with a cancel button.");

extern "C" {static PyObject *meth_wxPrinter_CreateAbortWindow(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxPrinter_CreateAbortWindow(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxWindow* parent;
        ::wxPrintout* printout;
        ::wxPrinter *sipCpp;

        static const char *sipKwdList[] = {
            sipName_parent,
            sipName_printout,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ8J8", &sipSelf, sipType_wxPrinter, &sipCpp, sipType_wxWindow, &parent, sipType_wxPrintout, &printout))
        {
            ::wxPrintAbortDialog*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxPrinter::CreateAbortWindow(parent, printout) : sipCpp->CreateAbortWindow(parent, printout));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxPrintAbortDialog, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_Printer, sipName_CreateAbortWindow, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPrinter_GetAbort, "GetAbort() -> bool\n"
"\n"
"Returns true if the user has aborted the print job.");

extern "C" {static PyObject *meth_wxPrinter_GetAbort(PyObject *, PyObject *);}
static PyObject *meth_wxPrinter_GetAbort(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxPrinter *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxPrinter, &sipCpp))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetAbort();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_Printer, sipName_GetAbort, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPrinter_GetPrintDialogData, "GetPrintDialogData() -> PrintDialogData\n"
"\n"
"Returns the print data associated with the printer object.");

extern "C" {static PyObject *meth_wxPrinter_GetPrintDialogData(PyObject *, PyObject *);}
static PyObject *meth_wxPrinter_GetPrintDialogData(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const ::wxPrinter *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxPrinter, &sipCpp))
        {
            ::wxPrintDialogData*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = &(sipSelfWasArg ? sipCpp->::wxPrinter::GetPrintDialogData() : sipCpp->GetPrintDialogData());
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxPrintDialogData, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_Printer, sipName_GetPrintDialogData, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPrinter_Print, "Print(parent, printout, prompt=True) -> bool\n"
"\n"
"Starts the printing process.");

extern "C" {static PyObject *meth_wxPrinter_Print(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxPrinter_Print(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxWindow* parent;
        ::wxPrintout* printout;
        bool prompt = 1;
        ::wxPrinter *sipCpp;

        static const char *sipKwdList[] = {
            sipName_parent,
            sipName_printout,
            sipName_prompt,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ8J8|b", &sipSelf, sipType_wxPrinter, &sipCpp, sipType_wxWindow, &parent, sipType_wxPrintout, &printout, &prompt))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxPrinter::Print(parent, printout, prompt) : sipCpp->Print(parent, printout, prompt));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_Printer, sipName_Print, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPrinter_PrintDialog, "PrintDialog(parent) -> DC\n"
"\n"
"Invokes the print dialog.");

extern "C" {static PyObject *meth_wxPrinter_PrintDialog(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxPrinter_PrintDialog(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxWindow* parent;
        ::wxPrinter *sipCpp;

        static const char *sipKwdList[] = {
            sipName_parent,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ8", &sipSelf, sipType_wxPrinter, &sipCpp, sipType_wxWindow, &parent))
        {
            ::wxDC*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxPrinter::PrintDialog(parent) : sipCpp->PrintDialog(parent));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxDC, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_Printer, sipName_PrintDialog, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPrinter_ReportError, "ReportError(parent, printout, message) -> None\n"
"\n"
"Default error-reporting function.");

extern "C" {static PyObject *meth_wxPrinter_ReportError(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxPrinter_ReportError(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxWindow* parent;
        ::wxPrintout* printout;
        const ::wxString* message;
        int messageState = 0;
        ::wxPrinter *sipCpp;

        static const char *sipKwdList[] = {
            sipName_parent,
            sipName_printout,
            sipName_message,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ8J8J1", &sipSelf, sipType_wxPrinter, &sipCpp, sipType_wxWindow, &parent, sipType_wxPrintout, &printout, sipType_wxString, &message, &messageState))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            (sipSelfWasArg ? sipCpp->::wxPrinter::ReportError(parent, printout, *message) : sipCpp->ReportError(parent, printout, *message));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(message), sipType_wxString, messageState);

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_Printer, sipName_ReportError, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPrinter_Setup, "Setup(parent) -> bool\n"
"\n"
"Invokes the print setup dialog.");

extern "C" {static PyObject *meth_wxPrinter_Setup(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxPrinter_Setup(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxWindow* parent;
        ::wxPrinter *sipCpp;

        static const char *sipKwdList[] = {
            sipName_parent,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ8", &sipSelf, sipType_wxPrinter, &sipCpp, sipType_wxWindow, &parent))
        {
            bool sipRes;

            if (sipDeprecated(sipName_Printer, sipName_Setup) < 0)
                return SIP_NULLPTR;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxPrinter::Setup(parent) : sipCpp->Setup(parent));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_Printer, sipName_Setup, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPrinter_GetLastError, "GetLastError() -> PrinterError\n"
"\n"
"Return last error.");

extern "C" {static PyObject *meth_wxPrinter_GetLastError(PyObject *, PyObject *);}
static PyObject *meth_wxPrinter_GetLastError(PyObject *, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        if (sipParseArgs(&sipParseErr, sipArgs, ""))
        {
            ::wxPrinterError sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = ::wxPrinter::GetLastError();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromEnum(static_cast<int>(sipRes), sipType_wxPrinterError);
        }
    }

    sipNoMethod(sipParseErr, sipName_Printer, sipName_GetLastError, SIP_NULLPTR);

    return SIP_NULLPTR;
}


/* Cast a pointer to a type somewhere in its inheritance hierarchy. */
extern "C" {static void *cast_wxPrinter(void *, const sipTypeDef *);}
static void *cast_wxPrinter(void *sipCppV, const sipTypeDef *targetType)
{
    ::wxPrinter *sipCpp = reinterpret_cast<::wxPrinter *>(sipCppV);

    if (targetType == sipType_wxPrinter)
        return sipCppV;

    if (targetType == sipType_wxObject)
        return static_cast<::wxObject *>(sipCpp);

    return SIP_NULLPTR;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxPrinter(void *, int);}
static void release_wxPrinter(void *sipCppV, int sipState)
{
    Py_BEGIN_ALLOW_THREADS

    if (sipState & SIP_DERIVED_CLASS)
        delete reinterpret_cast<sipwxPrinter *>(sipCppV);
    else
        delete reinterpret_cast<::wxPrinter *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void *array_wxPrinter(Py_ssize_t);}
static void *array_wxPrinter(Py_ssize_t sipNrElem)
{
    return new ::wxPrinter[sipNrElem];
}


extern "C" {static void array_delete_wxPrinter(void *);}
static void array_delete_wxPrinter(void *sipCpp)
{
    delete[] reinterpret_cast<::wxPrinter *>(sipCpp);
}


extern "C" {static void dealloc_wxPrinter(sipSimpleWrapper *);}
static void dealloc_wxPrinter(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerivedClass(sipSelf))
        reinterpret_cast<sipwxPrinter *>(sipGetAddress(sipSelf))->sipPySelf = SIP_NULLPTR;

    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxPrinter(sipGetAddress(sipSelf), sipIsDerivedClass(sipSelf));
    }
}


extern "C" {static void *init_type_wxPrinter(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxPrinter(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    sipwxPrinter *sipCpp = SIP_NULLPTR;

    {
        ::wxPrintDialogData* data = 0;

        static const char *sipKwdList[] = {
            sipName_data,
        };

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, sipKwdList, sipUnused, "|J8", sipType_wxPrintDialogData, &data))
        {
        if (!wxPyCheckForApp()) return NULL;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipwxPrinter(data);
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

    return SIP_NULLPTR;
}


/* Define this type's super-types. */
static sipEncodedTypeDef supers_wxPrinter[] = {{392, 255, 1}};


static PyMethodDef methods_wxPrinter[] = {
    {sipName_CreateAbortWindow, SIP_MLMETH_CAST(meth_wxPrinter_CreateAbortWindow), METH_VARARGS|METH_KEYWORDS, doc_wxPrinter_CreateAbortWindow},
    {sipName_GetAbort, meth_wxPrinter_GetAbort, METH_VARARGS, doc_wxPrinter_GetAbort},
    {sipName_GetLastError, meth_wxPrinter_GetLastError, METH_VARARGS, doc_wxPrinter_GetLastError},
    {sipName_GetPrintDialogData, meth_wxPrinter_GetPrintDialogData, METH_VARARGS, doc_wxPrinter_GetPrintDialogData},
    {sipName_Print, SIP_MLMETH_CAST(meth_wxPrinter_Print), METH_VARARGS|METH_KEYWORDS, doc_wxPrinter_Print},
    {sipName_PrintDialog, SIP_MLMETH_CAST(meth_wxPrinter_PrintDialog), METH_VARARGS|METH_KEYWORDS, doc_wxPrinter_PrintDialog},
    {sipName_ReportError, SIP_MLMETH_CAST(meth_wxPrinter_ReportError), METH_VARARGS|METH_KEYWORDS, doc_wxPrinter_ReportError},
    {sipName_Setup, SIP_MLMETH_CAST(meth_wxPrinter_Setup), METH_VARARGS|METH_KEYWORDS, doc_wxPrinter_Setup}
};

sipVariableDef variables_wxPrinter[] = {
    {PropertyVariable, sipName_PrintDialogData, &methods_wxPrinter[3], SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_Abort, &methods_wxPrinter[1], SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
};

PyDoc_STRVAR(doc_wxPrinter, "Printer(data=None) -> None\n"
"\n"
"This class represents the Windows or PostScript printer, and is the\n"
"vehicle through which printing may be launched by an application.");


sipClassTypeDef sipTypeDef__core_wxPrinter = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_SCC|SIP_TYPE_CLASS,
        sipNameNr_wxPrinter,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_Printer,
        {0, 0, 1},
        8, methods_wxPrinter,
        0, SIP_NULLPTR,
        2, variables_wxPrinter,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxPrinter,
    -1,
    -1,
    supers_wxPrinter,
    SIP_NULLPTR,
    init_type_wxPrinter,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxPrinter,
    SIP_NULLPTR,
    array_wxPrinter,
    SIP_NULLPTR,
    release_wxPrinter,
    cast_wxPrinter,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    array_delete_wxPrinter,
    sizeof (::wxPrinter),
};
