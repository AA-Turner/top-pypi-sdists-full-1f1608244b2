/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_richtext.h"
        #include <wx/richtext/richtextprint.h>
        #include <wx/window.h>
        #include <wx/cmndata.h>
        #include <wx/gdicmn.h>
        #include <wx/cmndata.h>
        #include <wx/colour.h>
        #include <wx/font.h>
        #include <wx/richtext/richtextprint.h>
        #include <wx/richtext/richtextbuffer.h>
        #include <wx/object.h>
        #include <wx/object.h>
        #include <wx/object.h>


PyDoc_STRVAR(doc_wxRichTextPrinting_GetFooterText, "GetFooterText(page=RICHTEXT_PAGE_EVEN, location=RICHTEXT_PAGE_CENTRE) -> str\n"
"\n"
"A convenience function to get the footer text.");

extern "C" {static PyObject *meth_wxRichTextPrinting_GetFooterText(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_GetFooterText(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxRichTextOddEvenPage page = wxRICHTEXT_PAGE_EVEN;
        ::wxRichTextPageLocation location = wxRICHTEXT_PAGE_CENTRE;
        const ::wxRichTextPrinting *sipCpp;

        static const char *sipKwdList[] = {
            sipName_page,
            sipName_location,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "B|EE", &sipSelf, sipType_wxRichTextPrinting, &sipCpp, sipType_wxRichTextOddEvenPage, &page, sipType_wxRichTextPageLocation, &location))
        {
            ::wxString*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxString(sipCpp->GetFooterText(page, location));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxString, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_GetFooterText, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxRichTextPrinting_GetHeaderFooterData, "GetHeaderFooterData() -> RichTextHeaderFooterData\n"
"\n"
"Returns the internal wxRichTextHeaderFooterData object.");

extern "C" {static PyObject *meth_wxRichTextPrinting_GetHeaderFooterData(PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_GetHeaderFooterData(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxRichTextPrinting *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxRichTextPrinting, &sipCpp))
        {
            ::wxRichTextHeaderFooterData*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxRichTextHeaderFooterData(sipCpp->GetHeaderFooterData());
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxRichTextHeaderFooterData, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_GetHeaderFooterData, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxRichTextPrinting_GetHeaderText, "GetHeaderText(page=RICHTEXT_PAGE_EVEN, location=RICHTEXT_PAGE_CENTRE) -> str\n"
"\n"
"A convenience function to get the header text.");

extern "C" {static PyObject *meth_wxRichTextPrinting_GetHeaderText(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_GetHeaderText(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxRichTextOddEvenPage page = wxRICHTEXT_PAGE_EVEN;
        ::wxRichTextPageLocation location = wxRICHTEXT_PAGE_CENTRE;
        const ::wxRichTextPrinting *sipCpp;

        static const char *sipKwdList[] = {
            sipName_page,
            sipName_location,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "B|EE", &sipSelf, sipType_wxRichTextPrinting, &sipCpp, sipType_wxRichTextOddEvenPage, &page, sipType_wxRichTextPageLocation, &location))
        {
            ::wxString*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxString(sipCpp->GetHeaderText(page, location));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxString, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_GetHeaderText, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxRichTextPrinting_GetPageSetupData, "GetPageSetupData() -> wx.PageSetupDialogData\n"
"\n"
"Returns a pointer to the internal page setup data.");

extern "C" {static PyObject *meth_wxRichTextPrinting_GetPageSetupData(PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_GetPageSetupData(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxRichTextPrinting *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxRichTextPrinting, &sipCpp))
        {
            ::wxPageSetupDialogData*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetPageSetupData();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxPageSetupDialogData, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_GetPageSetupData, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxRichTextPrinting_GetParentWindow, "GetParentWindow() -> wx.Window\n"
"\n"
"Returns the parent window to be used for the preview window and\n"
"printing wait dialog.");

extern "C" {static PyObject *meth_wxRichTextPrinting_GetParentWindow(PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_GetParentWindow(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxRichTextPrinting *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxRichTextPrinting, &sipCpp))
        {
            ::wxWindow*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetParentWindow();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxWindow, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_GetParentWindow, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxRichTextPrinting_GetPreviewRect, "GetPreviewRect() -> wx.Rect\n"
"\n"
"Returns the dimensions to be used for the preview window.");

extern "C" {static PyObject *meth_wxRichTextPrinting_GetPreviewRect(PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_GetPreviewRect(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxRichTextPrinting *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxRichTextPrinting, &sipCpp))
        {
            ::wxRect*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxRect(sipCpp->GetPreviewRect());
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxRect, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_GetPreviewRect, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxRichTextPrinting_GetPrintData, "GetPrintData() -> wx.PrintData\n"
"\n"
"Returns a pointer to the internal print data.");

extern "C" {static PyObject *meth_wxRichTextPrinting_GetPrintData(PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_GetPrintData(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxRichTextPrinting *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxRichTextPrinting, &sipCpp))
        {
            ::wxPrintData*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetPrintData();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxPrintData, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_GetPrintData, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxRichTextPrinting_GetTitle, "GetTitle() -> str\n"
"\n"
"Returns the title of the preview window or printing wait caption.");

extern "C" {static PyObject *meth_wxRichTextPrinting_GetTitle(PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_GetTitle(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxRichTextPrinting *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxRichTextPrinting, &sipCpp))
        {
            ::wxString*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxString(sipCpp->GetTitle());
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxString, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_GetTitle, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxRichTextPrinting_PageSetup, "PageSetup() -> None\n"
"\n"
"Shows the page setup dialog.");

extern "C" {static PyObject *meth_wxRichTextPrinting_PageSetup(PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_PageSetup(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxRichTextPrinting *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxRichTextPrinting, &sipCpp))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->PageSetup();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_PageSetup, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxRichTextPrinting_PreviewBuffer, "PreviewBuffer(buffer) -> bool\n"
"\n"
"Shows a preview window for the given buffer.");

extern "C" {static PyObject *meth_wxRichTextPrinting_PreviewBuffer(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_PreviewBuffer(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxRichTextBuffer* buffer;
        ::wxRichTextPrinting *sipCpp;

        static const char *sipKwdList[] = {
            sipName_buffer,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ9", &sipSelf, sipType_wxRichTextPrinting, &sipCpp, sipType_wxRichTextBuffer, &buffer))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->PreviewBuffer(*buffer);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_PreviewBuffer, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxRichTextPrinting_PreviewFile, "PreviewFile(richTextFile) -> bool\n"
"\n"
"Shows a preview window for the given file.");

extern "C" {static PyObject *meth_wxRichTextPrinting_PreviewFile(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_PreviewFile(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxString* richTextFile;
        int richTextFileState = 0;
        ::wxRichTextPrinting *sipCpp;

        static const char *sipKwdList[] = {
            sipName_richTextFile,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1", &sipSelf, sipType_wxRichTextPrinting, &sipCpp, sipType_wxString, &richTextFile, &richTextFileState))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->PreviewFile(*richTextFile);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(richTextFile), sipType_wxString, richTextFileState);

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_PreviewFile, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxRichTextPrinting_PrintBuffer, "PrintBuffer(buffer, showPrintDialog=True) -> bool\n"
"\n"
"Prints the given buffer.");

extern "C" {static PyObject *meth_wxRichTextPrinting_PrintBuffer(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_PrintBuffer(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxRichTextBuffer* buffer;
        bool showPrintDialog = 1;
        ::wxRichTextPrinting *sipCpp;

        static const char *sipKwdList[] = {
            sipName_buffer,
            sipName_showPrintDialog,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ9|b", &sipSelf, sipType_wxRichTextPrinting, &sipCpp, sipType_wxRichTextBuffer, &buffer, &showPrintDialog))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->PrintBuffer(*buffer, showPrintDialog);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_PrintBuffer, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxRichTextPrinting_PrintFile, "PrintFile(richTextFile, showPrintDialog=True) -> bool\n"
"\n"
"Prints the given file.");

extern "C" {static PyObject *meth_wxRichTextPrinting_PrintFile(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_PrintFile(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxString* richTextFile;
        int richTextFileState = 0;
        bool showPrintDialog = 1;
        ::wxRichTextPrinting *sipCpp;

        static const char *sipKwdList[] = {
            sipName_richTextFile,
            sipName_showPrintDialog,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1|b", &sipSelf, sipType_wxRichTextPrinting, &sipCpp, sipType_wxString, &richTextFile, &richTextFileState, &showPrintDialog))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->PrintFile(*richTextFile, showPrintDialog);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(richTextFile), sipType_wxString, richTextFileState);

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_PrintFile, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxRichTextPrinting_SetFooterText, "SetFooterText(text, page=RICHTEXT_PAGE_ALL, location=RICHTEXT_PAGE_CENTRE) -> None\n"
"\n"
"A convenience function to set the footer text.");

extern "C" {static PyObject *meth_wxRichTextPrinting_SetFooterText(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_SetFooterText(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxString* text;
        int textState = 0;
        ::wxRichTextOddEvenPage page = wxRICHTEXT_PAGE_ALL;
        ::wxRichTextPageLocation location = wxRICHTEXT_PAGE_CENTRE;
        ::wxRichTextPrinting *sipCpp;

        static const char *sipKwdList[] = {
            sipName_text,
            sipName_page,
            sipName_location,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1|EE", &sipSelf, sipType_wxRichTextPrinting, &sipCpp, sipType_wxString, &text, &textState, sipType_wxRichTextOddEvenPage, &page, sipType_wxRichTextPageLocation, &location))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetFooterText(*text, page, location);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(text), sipType_wxString, textState);

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_SetFooterText, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxRichTextPrinting_SetHeaderFooterData, "SetHeaderFooterData(data) -> None\n"
"\n"
"Sets the internal wxRichTextHeaderFooterData object.");

extern "C" {static PyObject *meth_wxRichTextPrinting_SetHeaderFooterData(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_SetHeaderFooterData(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxRichTextHeaderFooterData* data;
        ::wxRichTextPrinting *sipCpp;

        static const char *sipKwdList[] = {
            sipName_data,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ9", &sipSelf, sipType_wxRichTextPrinting, &sipCpp, sipType_wxRichTextHeaderFooterData, &data))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetHeaderFooterData(*data);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_SetHeaderFooterData, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxRichTextPrinting_SetHeaderFooterFont, "SetHeaderFooterFont(font) -> None\n"
"\n"
"Sets the wxRichTextHeaderFooterData font.");

extern "C" {static PyObject *meth_wxRichTextPrinting_SetHeaderFooterFont(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_SetHeaderFooterFont(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxFont* font;
        ::wxRichTextPrinting *sipCpp;

        static const char *sipKwdList[] = {
            sipName_font,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ9", &sipSelf, sipType_wxRichTextPrinting, &sipCpp, sipType_wxFont, &font))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetHeaderFooterFont(*font);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_SetHeaderFooterFont, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxRichTextPrinting_SetHeaderFooterTextColour, "SetHeaderFooterTextColour(colour) -> None\n"
"\n"
"Sets the wxRichTextHeaderFooterData text colour.");

extern "C" {static PyObject *meth_wxRichTextPrinting_SetHeaderFooterTextColour(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_SetHeaderFooterTextColour(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxColour* colour;
        int colourState = 0;
        ::wxRichTextPrinting *sipCpp;

        static const char *sipKwdList[] = {
            sipName_colour,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1", &sipSelf, sipType_wxRichTextPrinting, &sipCpp, sipType_wxColour, &colour, &colourState))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetHeaderFooterTextColour(*colour);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxColour *>(colour), sipType_wxColour, colourState);

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_SetHeaderFooterTextColour, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxRichTextPrinting_SetHeaderText, "SetHeaderText(text, page=RICHTEXT_PAGE_ALL, location=RICHTEXT_PAGE_CENTRE) -> None\n"
"\n"
"A convenience function to set the header text.");

extern "C" {static PyObject *meth_wxRichTextPrinting_SetHeaderText(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_SetHeaderText(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxString* text;
        int textState = 0;
        ::wxRichTextOddEvenPage page = wxRICHTEXT_PAGE_ALL;
        ::wxRichTextPageLocation location = wxRICHTEXT_PAGE_CENTRE;
        ::wxRichTextPrinting *sipCpp;

        static const char *sipKwdList[] = {
            sipName_text,
            sipName_page,
            sipName_location,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1|EE", &sipSelf, sipType_wxRichTextPrinting, &sipCpp, sipType_wxString, &text, &textState, sipType_wxRichTextOddEvenPage, &page, sipType_wxRichTextPageLocation, &location))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetHeaderText(*text, page, location);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(text), sipType_wxString, textState);

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_SetHeaderText, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxRichTextPrinting_SetPageSetupData, "SetPageSetupData(pageSetupData) -> None\n"
"\n"
"Sets the page setup data.");

extern "C" {static PyObject *meth_wxRichTextPrinting_SetPageSetupData(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_SetPageSetupData(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxPageSetupDialogData* pageSetupData;
        ::wxRichTextPrinting *sipCpp;

        static const char *sipKwdList[] = {
            sipName_pageSetupData,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ9", &sipSelf, sipType_wxRichTextPrinting, &sipCpp, sipType_wxPageSetupDialogData, &pageSetupData))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetPageSetupData(*pageSetupData);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_SetPageSetupData, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxRichTextPrinting_SetParentWindow, "SetParentWindow(parent) -> None\n"
"\n"
"Sets the parent window to be used for the preview window and printing\n"
"wait dialog.");

extern "C" {static PyObject *meth_wxRichTextPrinting_SetParentWindow(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_SetParentWindow(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxWindow* parent;
        ::wxRichTextPrinting *sipCpp;

        static const char *sipKwdList[] = {
            sipName_parent,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ8", &sipSelf, sipType_wxRichTextPrinting, &sipCpp, sipType_wxWindow, &parent))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetParentWindow(parent);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_SetParentWindow, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxRichTextPrinting_SetPreviewRect, "SetPreviewRect(rect) -> None\n"
"\n"
"Sets the dimensions to be used for the preview window.");

extern "C" {static PyObject *meth_wxRichTextPrinting_SetPreviewRect(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_SetPreviewRect(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxRect* rect;
        int rectState = 0;
        ::wxRichTextPrinting *sipCpp;

        static const char *sipKwdList[] = {
            sipName_rect,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1", &sipSelf, sipType_wxRichTextPrinting, &sipCpp, sipType_wxRect, &rect, &rectState))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetPreviewRect(*rect);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxRect *>(rect), sipType_wxRect, rectState);

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_SetPreviewRect, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxRichTextPrinting_SetPrintData, "SetPrintData(printData) -> None\n"
"\n"
"Sets the print data.");

extern "C" {static PyObject *meth_wxRichTextPrinting_SetPrintData(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_SetPrintData(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxPrintData* printData;
        ::wxRichTextPrinting *sipCpp;

        static const char *sipKwdList[] = {
            sipName_printData,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ9", &sipSelf, sipType_wxRichTextPrinting, &sipCpp, sipType_wxPrintData, &printData))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetPrintData(*printData);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_SetPrintData, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxRichTextPrinting_SetShowOnFirstPage, "SetShowOnFirstPage(show) -> None\n"
"\n"
"Pass true to show the header and footer on the first page.");

extern "C" {static PyObject *meth_wxRichTextPrinting_SetShowOnFirstPage(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_SetShowOnFirstPage(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        bool show;
        ::wxRichTextPrinting *sipCpp;

        static const char *sipKwdList[] = {
            sipName_show,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "Bb", &sipSelf, sipType_wxRichTextPrinting, &sipCpp, &show))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetShowOnFirstPage(show);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_SetShowOnFirstPage, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxRichTextPrinting_SetTitle, "SetTitle(title) -> None\n"
"\n"
"Pass the title of the preview window or printing wait caption.");

extern "C" {static PyObject *meth_wxRichTextPrinting_SetTitle(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxRichTextPrinting_SetTitle(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxString* title;
        int titleState = 0;
        ::wxRichTextPrinting *sipCpp;

        static const char *sipKwdList[] = {
            sipName_title,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1", &sipSelf, sipType_wxRichTextPrinting, &sipCpp, sipType_wxString, &title, &titleState))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetTitle(*title);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(title), sipType_wxString, titleState);

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextPrinting, sipName_SetTitle, SIP_NULLPTR);

    return SIP_NULLPTR;
}


/* Cast a pointer to a type somewhere in its inheritance hierarchy. */
extern "C" {static void *cast_wxRichTextPrinting(void *, const sipTypeDef *);}
static void *cast_wxRichTextPrinting(void *sipCppV, const sipTypeDef *targetType)
{
    ::wxRichTextPrinting *sipCpp = reinterpret_cast<::wxRichTextPrinting *>(sipCppV);

    if (targetType == sipType_wxRichTextPrinting)
        return sipCppV;

    if (targetType == sipType_wxObject)
        return static_cast<::wxObject *>(sipCpp);

    return SIP_NULLPTR;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxRichTextPrinting(void *, int);}
static void release_wxRichTextPrinting(void *sipCppV, int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast<::wxRichTextPrinting *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void *array_wxRichTextPrinting(Py_ssize_t);}
static void *array_wxRichTextPrinting(Py_ssize_t sipNrElem)
{
    return new ::wxRichTextPrinting[sipNrElem];
}


extern "C" {static void array_delete_wxRichTextPrinting(void *);}
static void array_delete_wxRichTextPrinting(void *sipCpp)
{
    delete[] reinterpret_cast<::wxRichTextPrinting *>(sipCpp);
}


extern "C" {static void dealloc_wxRichTextPrinting(sipSimpleWrapper *);}
static void dealloc_wxRichTextPrinting(sipSimpleWrapper *sipSelf)
{
    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxRichTextPrinting(sipGetAddress(sipSelf), 0);
    }
}


extern "C" {static void *init_type_wxRichTextPrinting(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxRichTextPrinting(sipSimpleWrapper *, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    ::wxRichTextPrinting *sipCpp = SIP_NULLPTR;

    {
        const ::wxString& namedef = "Printing";
        const ::wxString* name = &namedef;
        int nameState = 0;
        ::wxWindow* parentWindow = 0;

        static const char *sipKwdList[] = {
            sipName_name,
            sipName_parentWindow,
        };

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, sipKwdList, sipUnused, "|J1J8", sipType_wxString, &name, &nameState, sipType_wxWindow, &parentWindow))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new ::wxRichTextPrinting(*name, parentWindow);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(name), sipType_wxString, nameState);

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


/* Define this type's super-types. */
static sipEncodedTypeDef supers_wxRichTextPrinting[] = {{42, 0, 1}};


static PyMethodDef methods_wxRichTextPrinting[] = {
    {sipName_GetFooterText, SIP_MLMETH_CAST(meth_wxRichTextPrinting_GetFooterText), METH_VARARGS|METH_KEYWORDS, doc_wxRichTextPrinting_GetFooterText},
    {sipName_GetHeaderFooterData, meth_wxRichTextPrinting_GetHeaderFooterData, METH_VARARGS, doc_wxRichTextPrinting_GetHeaderFooterData},
    {sipName_GetHeaderText, SIP_MLMETH_CAST(meth_wxRichTextPrinting_GetHeaderText), METH_VARARGS|METH_KEYWORDS, doc_wxRichTextPrinting_GetHeaderText},
    {sipName_GetPageSetupData, meth_wxRichTextPrinting_GetPageSetupData, METH_VARARGS, doc_wxRichTextPrinting_GetPageSetupData},
    {sipName_GetParentWindow, meth_wxRichTextPrinting_GetParentWindow, METH_VARARGS, doc_wxRichTextPrinting_GetParentWindow},
    {sipName_GetPreviewRect, meth_wxRichTextPrinting_GetPreviewRect, METH_VARARGS, doc_wxRichTextPrinting_GetPreviewRect},
    {sipName_GetPrintData, meth_wxRichTextPrinting_GetPrintData, METH_VARARGS, doc_wxRichTextPrinting_GetPrintData},
    {sipName_GetTitle, meth_wxRichTextPrinting_GetTitle, METH_VARARGS, doc_wxRichTextPrinting_GetTitle},
    {sipName_PageSetup, meth_wxRichTextPrinting_PageSetup, METH_VARARGS, doc_wxRichTextPrinting_PageSetup},
    {sipName_PreviewBuffer, SIP_MLMETH_CAST(meth_wxRichTextPrinting_PreviewBuffer), METH_VARARGS|METH_KEYWORDS, doc_wxRichTextPrinting_PreviewBuffer},
    {sipName_PreviewFile, SIP_MLMETH_CAST(meth_wxRichTextPrinting_PreviewFile), METH_VARARGS|METH_KEYWORDS, doc_wxRichTextPrinting_PreviewFile},
    {sipName_PrintBuffer, SIP_MLMETH_CAST(meth_wxRichTextPrinting_PrintBuffer), METH_VARARGS|METH_KEYWORDS, doc_wxRichTextPrinting_PrintBuffer},
    {sipName_PrintFile, SIP_MLMETH_CAST(meth_wxRichTextPrinting_PrintFile), METH_VARARGS|METH_KEYWORDS, doc_wxRichTextPrinting_PrintFile},
    {sipName_SetFooterText, SIP_MLMETH_CAST(meth_wxRichTextPrinting_SetFooterText), METH_VARARGS|METH_KEYWORDS, doc_wxRichTextPrinting_SetFooterText},
    {sipName_SetHeaderFooterData, SIP_MLMETH_CAST(meth_wxRichTextPrinting_SetHeaderFooterData), METH_VARARGS|METH_KEYWORDS, doc_wxRichTextPrinting_SetHeaderFooterData},
    {sipName_SetHeaderFooterFont, SIP_MLMETH_CAST(meth_wxRichTextPrinting_SetHeaderFooterFont), METH_VARARGS|METH_KEYWORDS, doc_wxRichTextPrinting_SetHeaderFooterFont},
    {sipName_SetHeaderFooterTextColour, SIP_MLMETH_CAST(meth_wxRichTextPrinting_SetHeaderFooterTextColour), METH_VARARGS|METH_KEYWORDS, doc_wxRichTextPrinting_SetHeaderFooterTextColour},
    {sipName_SetHeaderText, SIP_MLMETH_CAST(meth_wxRichTextPrinting_SetHeaderText), METH_VARARGS|METH_KEYWORDS, doc_wxRichTextPrinting_SetHeaderText},
    {sipName_SetPageSetupData, SIP_MLMETH_CAST(meth_wxRichTextPrinting_SetPageSetupData), METH_VARARGS|METH_KEYWORDS, doc_wxRichTextPrinting_SetPageSetupData},
    {sipName_SetParentWindow, SIP_MLMETH_CAST(meth_wxRichTextPrinting_SetParentWindow), METH_VARARGS|METH_KEYWORDS, doc_wxRichTextPrinting_SetParentWindow},
    {sipName_SetPreviewRect, SIP_MLMETH_CAST(meth_wxRichTextPrinting_SetPreviewRect), METH_VARARGS|METH_KEYWORDS, doc_wxRichTextPrinting_SetPreviewRect},
    {sipName_SetPrintData, SIP_MLMETH_CAST(meth_wxRichTextPrinting_SetPrintData), METH_VARARGS|METH_KEYWORDS, doc_wxRichTextPrinting_SetPrintData},
    {sipName_SetShowOnFirstPage, SIP_MLMETH_CAST(meth_wxRichTextPrinting_SetShowOnFirstPage), METH_VARARGS|METH_KEYWORDS, doc_wxRichTextPrinting_SetShowOnFirstPage},
    {sipName_SetTitle, SIP_MLMETH_CAST(meth_wxRichTextPrinting_SetTitle), METH_VARARGS|METH_KEYWORDS, doc_wxRichTextPrinting_SetTitle}
};

sipVariableDef variables_wxRichTextPrinting[] = {
    {PropertyVariable, sipName_Title, &methods_wxRichTextPrinting[7], &methods_wxRichTextPrinting[23], SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_PrintData, &methods_wxRichTextPrinting[6], &methods_wxRichTextPrinting[21], SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_PreviewRect, &methods_wxRichTextPrinting[5], &methods_wxRichTextPrinting[20], SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_ParentWindow, &methods_wxRichTextPrinting[4], &methods_wxRichTextPrinting[19], SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_PageSetupData, &methods_wxRichTextPrinting[3], &methods_wxRichTextPrinting[18], SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_HeaderText, &methods_wxRichTextPrinting[2], &methods_wxRichTextPrinting[17], SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_HeaderFooterData, &methods_wxRichTextPrinting[1], &methods_wxRichTextPrinting[14], SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_FooterText, &methods_wxRichTextPrinting[0], &methods_wxRichTextPrinting[13], SIP_NULLPTR, SIP_NULLPTR},
};

PyDoc_STRVAR(doc_wxRichTextPrinting, "RichTextPrinting(name=\"Printing\", parentWindow=None) -> None\n"
"\n"
"This class provides a simple interface for performing wxRichTextBuffer\n"
"printing and previewing.");


sipClassTypeDef sipTypeDef__richtext_wxRichTextPrinting = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_SCC|SIP_TYPE_CLASS,
        sipNameNr_wxRichTextPrinting,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_RichTextPrinting,
        {0, 0, 1},
        24, methods_wxRichTextPrinting,
        0, SIP_NULLPTR,
        8, variables_wxRichTextPrinting,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxRichTextPrinting,
    -1,
    -1,
    supers_wxRichTextPrinting,
    SIP_NULLPTR,
    init_type_wxRichTextPrinting,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxRichTextPrinting,
    SIP_NULLPTR,
    array_wxRichTextPrinting,
    SIP_NULLPTR,
    release_wxRichTextPrinting,
    cast_wxRichTextPrinting,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    array_delete_wxRichTextPrinting,
    sizeof (::wxRichTextPrinting),
};
