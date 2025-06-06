/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_core.h"
        #include <wx/fontmap.h>
        #include <wx/window.h>
    wxArrayString* _wxFontMapper_GetAllEncodingNames(wxFontEncoding encoding)
    {
        wxArrayString* sArr = new wxArrayString;
        const wxChar** cArr = wxFontMapper::GetAllEncodingNames(encoding);
        if (cArr) {
            for (int idx=0; cArr[idx]; idx+=1)
                sArr->Add(cArr[idx]);
        }
        return sArr;
    }


class sipwxFontMapper : public ::wxFontMapper
{
public:
    sipwxFontMapper();
    virtual ~sipwxFontMapper();

    /*
     * There is a protected method for every virtual method visible from
     * this class.
     */
protected:
    bool IsEncodingAvailable(::wxFontEncoding, const ::wxString&) SIP_OVERRIDE;
    ::wxFontEncoding CharsetToEncoding(const ::wxString&, bool) SIP_OVERRIDE;

public:
    sipSimpleWrapper *sipPySelf;

private:
    sipwxFontMapper(const sipwxFontMapper &);
    sipwxFontMapper &operator = (const sipwxFontMapper &);

    char sipPyMethods[2];
};

sipwxFontMapper::sipwxFontMapper(): ::wxFontMapper(), sipPySelf(SIP_NULLPTR)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipwxFontMapper::~sipwxFontMapper()
{
    sipInstanceDestroyedEx(&sipPySelf);
}

bool sipwxFontMapper::IsEncodingAvailable(::wxFontEncoding encoding, const ::wxString& facename)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[0], &sipPySelf, SIP_NULLPTR, sipName_IsEncodingAvailable);

    if (!sipMeth)
        return ::wxFontMapper::IsEncodingAvailable(encoding, facename);

    extern bool sipVH__core_234(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxFontEncoding, const ::wxString&);

    return sipVH__core_234(sipGILState, 0, sipPySelf, sipMeth, encoding, facename);
}

::wxFontEncoding sipwxFontMapper::CharsetToEncoding(const ::wxString& charset, bool interactive)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[1], &sipPySelf, SIP_NULLPTR, sipName_CharsetToEncoding);

    if (!sipMeth)
        return ::wxFontMapper::CharsetToEncoding(charset, interactive);

    extern ::wxFontEncoding sipVH__core_233(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, const ::wxString&, bool);

    return sipVH__core_233(sipGILState, 0, sipPySelf, sipMeth, charset, interactive);
}


PyDoc_STRVAR(doc_wxFontMapper_GetAltForEncoding, "GetAltForEncoding(encoding, facename='', interactive=True) -> Tuple[bool, FontEncoding]\n"
"\n"
"Find an alternative for the given encoding (which is supposed to not\n"
"be available on this system).");

extern "C" {static PyObject *meth_wxFontMapper_GetAltForEncoding(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxFontMapper_GetAltForEncoding(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxFontEncoding encoding;
        ::wxFontEncoding alt_encoding;
        const ::wxString& facenamedef = wxEmptyString;
        const ::wxString* facename = &facenamedef;
        int facenameState = 0;
        bool interactive = 1;
        ::wxFontMapper *sipCpp;

        static const char *sipKwdList[] = {
            sipName_encoding,
            sipName_facename,
            sipName_interactive,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BE|J1b", &sipSelf, sipType_wxFontMapper, &sipCpp, sipType_wxFontEncoding, &encoding, sipType_wxString, &facename, &facenameState, &interactive))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetAltForEncoding(encoding, &alt_encoding, *facename, interactive);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(facename), sipType_wxString, facenameState);

            if (PyErr_Occurred())
                return 0;

            return sipBuildResult(0, "(bF)", sipRes, alt_encoding, sipType_wxFontEncoding);
        }
    }

    sipNoMethod(sipParseErr, sipName_FontMapper, sipName_GetAltForEncoding, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxFontMapper_CharsetToEncoding, "CharsetToEncoding(charset, interactive=True) -> FontEncoding\n"
"\n"
"Returns the encoding for the given charset (in the form of RFC 2046)\n"
"or wxFONTENCODING_SYSTEM if couldn't decode it.");

extern "C" {static PyObject *meth_wxFontMapper_CharsetToEncoding(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxFontMapper_CharsetToEncoding(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const ::wxString* charset;
        int charsetState = 0;
        bool interactive = 1;
        ::wxFontMapper *sipCpp;

        static const char *sipKwdList[] = {
            sipName_charset,
            sipName_interactive,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1|b", &sipSelf, sipType_wxFontMapper, &sipCpp, sipType_wxString, &charset, &charsetState, &interactive))
        {
            ::wxFontEncoding sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxFontMapper::CharsetToEncoding(*charset, interactive) : sipCpp->CharsetToEncoding(*charset, interactive));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(charset), sipType_wxString, charsetState);

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromEnum(static_cast<int>(sipRes), sipType_wxFontEncoding);
        }
    }

    sipNoMethod(sipParseErr, sipName_FontMapper, sipName_CharsetToEncoding, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxFontMapper_IsEncodingAvailable, "IsEncodingAvailable(encoding, facename='') -> bool\n"
"\n"
"Check whether given encoding is available in given face or not.");

extern "C" {static PyObject *meth_wxFontMapper_IsEncodingAvailable(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxFontMapper_IsEncodingAvailable(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxFontEncoding encoding;
        const ::wxString& facenamedef = wxEmptyString;
        const ::wxString* facename = &facenamedef;
        int facenameState = 0;
        ::wxFontMapper *sipCpp;

        static const char *sipKwdList[] = {
            sipName_encoding,
            sipName_facename,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BE|J1", &sipSelf, sipType_wxFontMapper, &sipCpp, sipType_wxFontEncoding, &encoding, sipType_wxString, &facename, &facenameState))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxFontMapper::IsEncodingAvailable(encoding, *facename) : sipCpp->IsEncodingAvailable(encoding, *facename));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(facename), sipType_wxString, facenameState);

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_FontMapper, sipName_IsEncodingAvailable, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxFontMapper_SetConfigPath, "SetConfigPath(prefix) -> None\n"
"\n"
"Set the root config path to use (should be an absolute path).");

extern "C" {static PyObject *meth_wxFontMapper_SetConfigPath(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxFontMapper_SetConfigPath(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxString* prefix;
        int prefixState = 0;
        ::wxFontMapper *sipCpp;

        static const char *sipKwdList[] = {
            sipName_prefix,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1", &sipSelf, sipType_wxFontMapper, &sipCpp, sipType_wxString, &prefix, &prefixState))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetConfigPath(*prefix);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(prefix), sipType_wxString, prefixState);

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_FontMapper, sipName_SetConfigPath, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxFontMapper_SetDialogParent, "SetDialogParent(parent) -> None\n"
"\n"
"The parent window for modal dialogs.");

extern "C" {static PyObject *meth_wxFontMapper_SetDialogParent(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxFontMapper_SetDialogParent(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxWindow* parent;
        ::wxFontMapper *sipCpp;

        static const char *sipKwdList[] = {
            sipName_parent,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ8", &sipSelf, sipType_wxFontMapper, &sipCpp, sipType_wxWindow, &parent))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetDialogParent(parent);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_FontMapper, sipName_SetDialogParent, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxFontMapper_SetDialogTitle, "SetDialogTitle(title) -> None\n"
"\n"
"The title for the dialogs (note that default is quite reasonable).");

extern "C" {static PyObject *meth_wxFontMapper_SetDialogTitle(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxFontMapper_SetDialogTitle(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxString* title;
        int titleState = 0;
        ::wxFontMapper *sipCpp;

        static const char *sipKwdList[] = {
            sipName_title,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1", &sipSelf, sipType_wxFontMapper, &sipCpp, sipType_wxString, &title, &titleState))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetDialogTitle(*title);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(title), sipType_wxString, titleState);

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_FontMapper, sipName_SetDialogTitle, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxFontMapper_Get, "Get() -> FontMapper\n"
"\n"
"Get the current font mapper object.");

extern "C" {static PyObject *meth_wxFontMapper_Get(PyObject *, PyObject *);}
static PyObject *meth_wxFontMapper_Get(PyObject *, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        if (sipParseArgs(&sipParseErr, sipArgs, ""))
        {
            ::wxFontMapper*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = ::wxFontMapper::Get();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxFontMapper, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_FontMapper, sipName_Get, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxFontMapper_GetAllEncodingNames, "GetAllEncodingNames(encoding) -> List[str]\n"
"\n"
"Returns the array of all possible names for the given encoding. If it\n"
"isn't empty, the first name in it is the canonical encoding name,\n"
"i.e. the same string as returned by GetEncodingName()");

extern "C" {static PyObject *meth_wxFontMapper_GetAllEncodingNames(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxFontMapper_GetAllEncodingNames(PyObject *, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxFontEncoding encoding;

        static const char *sipKwdList[] = {
            sipName_encoding,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "E", sipType_wxFontEncoding, &encoding))
        {
            ::wxArrayString*sipRes = 0;
            int sipIsErr = 0;
        PyErr_Clear();
        Py_BEGIN_ALLOW_THREADS
        sipRes = _wxFontMapper_GetAllEncodingNames(encoding);
        Py_END_ALLOW_THREADS
        if (PyErr_Occurred()) sipIsErr = 1;

            if (sipIsErr)
                return 0;

            return sipConvertFromType(sipRes, sipType_wxArrayString, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_FontMapper, sipName_GetAllEncodingNames, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxFontMapper_GetEncoding, "GetEncoding(n) -> FontEncoding\n"
"\n"
"Returns the n-th supported encoding.");

extern "C" {static PyObject *meth_wxFontMapper_GetEncoding(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxFontMapper_GetEncoding(PyObject *, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        size_t n;

        static const char *sipKwdList[] = {
            sipName_n,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "=", &n))
        {
            ::wxFontEncoding sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = ::wxFontMapper::GetEncoding(n);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromEnum(static_cast<int>(sipRes), sipType_wxFontEncoding);
        }
    }

    sipNoMethod(sipParseErr, sipName_FontMapper, sipName_GetEncoding, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxFontMapper_GetEncodingDescription, "GetEncodingDescription(encoding) -> str\n"
"\n"
"Return user-readable string describing the given encoding.");

extern "C" {static PyObject *meth_wxFontMapper_GetEncodingDescription(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxFontMapper_GetEncodingDescription(PyObject *, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxFontEncoding encoding;

        static const char *sipKwdList[] = {
            sipName_encoding,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "E", sipType_wxFontEncoding, &encoding))
        {
            ::wxString*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxString(::wxFontMapper::GetEncodingDescription(encoding));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxString, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_FontMapper, sipName_GetEncodingDescription, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxFontMapper_GetEncodingFromName, "GetEncodingFromName(encoding) -> FontEncoding\n"
"\n"
"Return the encoding corresponding to the given internal name.");

extern "C" {static PyObject *meth_wxFontMapper_GetEncodingFromName(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxFontMapper_GetEncodingFromName(PyObject *, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxString* encoding;
        int encodingState = 0;

        static const char *sipKwdList[] = {
            sipName_encoding,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "J1", sipType_wxString, &encoding, &encodingState))
        {
            ::wxFontEncoding sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = ::wxFontMapper::GetEncodingFromName(*encoding);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(encoding), sipType_wxString, encodingState);

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromEnum(static_cast<int>(sipRes), sipType_wxFontEncoding);
        }
    }

    sipNoMethod(sipParseErr, sipName_FontMapper, sipName_GetEncodingFromName, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxFontMapper_GetEncodingName, "GetEncodingName(encoding) -> str\n"
"\n"
"Return internal string identifier for the encoding (see also\n"
"wxFontMapper::GetEncodingDescription).");

extern "C" {static PyObject *meth_wxFontMapper_GetEncodingName(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxFontMapper_GetEncodingName(PyObject *, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxFontEncoding encoding;

        static const char *sipKwdList[] = {
            sipName_encoding,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "E", sipType_wxFontEncoding, &encoding))
        {
            ::wxString*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxString(::wxFontMapper::GetEncodingName(encoding));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxString, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_FontMapper, sipName_GetEncodingName, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxFontMapper_GetSupportedEncodingsCount, "GetSupportedEncodingsCount() -> int\n"
"\n"
"Returns the number of the font encodings supported by this class.");

extern "C" {static PyObject *meth_wxFontMapper_GetSupportedEncodingsCount(PyObject *, PyObject *);}
static PyObject *meth_wxFontMapper_GetSupportedEncodingsCount(PyObject *, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        if (sipParseArgs(&sipParseErr, sipArgs, ""))
        {
            size_t sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = ::wxFontMapper::GetSupportedEncodingsCount();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyLong_FromUnsignedLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_FontMapper, sipName_GetSupportedEncodingsCount, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxFontMapper_Set, "Set(mapper) -> FontMapper\n"
"\n"
"Set the current font mapper object and return previous one (may be NULL).");

extern "C" {static PyObject *meth_wxFontMapper_Set(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxFontMapper_Set(PyObject *, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxFontMapper* mapper;

        static const char *sipKwdList[] = {
            sipName_mapper,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "J8", sipType_wxFontMapper, &mapper))
        {
            ::wxFontMapper*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = ::wxFontMapper::Set(mapper);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxFontMapper, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_FontMapper, sipName_Set, SIP_NULLPTR);

    return SIP_NULLPTR;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxFontMapper(void *, int);}
static void release_wxFontMapper(void *sipCppV, int sipState)
{
    Py_BEGIN_ALLOW_THREADS

    if (sipState & SIP_DERIVED_CLASS)
        delete reinterpret_cast<sipwxFontMapper *>(sipCppV);
    else
        delete reinterpret_cast<::wxFontMapper *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void *array_wxFontMapper(Py_ssize_t);}
static void *array_wxFontMapper(Py_ssize_t sipNrElem)
{
    return new ::wxFontMapper[sipNrElem];
}


extern "C" {static void array_delete_wxFontMapper(void *);}
static void array_delete_wxFontMapper(void *sipCpp)
{
    delete[] reinterpret_cast<::wxFontMapper *>(sipCpp);
}


extern "C" {static void dealloc_wxFontMapper(sipSimpleWrapper *);}
static void dealloc_wxFontMapper(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerivedClass(sipSelf))
        reinterpret_cast<sipwxFontMapper *>(sipGetAddress(sipSelf))->sipPySelf = SIP_NULLPTR;

    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxFontMapper(sipGetAddress(sipSelf), sipIsDerivedClass(sipSelf));
    }
}


extern "C" {static void *init_type_wxFontMapper(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxFontMapper(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    sipwxFontMapper *sipCpp = SIP_NULLPTR;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, ""))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipwxFontMapper();
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


static PyMethodDef methods_wxFontMapper[] = {
    {sipName_CharsetToEncoding, SIP_MLMETH_CAST(meth_wxFontMapper_CharsetToEncoding), METH_VARARGS|METH_KEYWORDS, doc_wxFontMapper_CharsetToEncoding},
    {sipName_Get, meth_wxFontMapper_Get, METH_VARARGS, doc_wxFontMapper_Get},
    {sipName_GetAllEncodingNames, SIP_MLMETH_CAST(meth_wxFontMapper_GetAllEncodingNames), METH_VARARGS|METH_KEYWORDS, doc_wxFontMapper_GetAllEncodingNames},
    {sipName_GetAltForEncoding, SIP_MLMETH_CAST(meth_wxFontMapper_GetAltForEncoding), METH_VARARGS|METH_KEYWORDS, doc_wxFontMapper_GetAltForEncoding},
    {sipName_GetEncoding, SIP_MLMETH_CAST(meth_wxFontMapper_GetEncoding), METH_VARARGS|METH_KEYWORDS, doc_wxFontMapper_GetEncoding},
    {sipName_GetEncodingDescription, SIP_MLMETH_CAST(meth_wxFontMapper_GetEncodingDescription), METH_VARARGS|METH_KEYWORDS, doc_wxFontMapper_GetEncodingDescription},
    {sipName_GetEncodingFromName, SIP_MLMETH_CAST(meth_wxFontMapper_GetEncodingFromName), METH_VARARGS|METH_KEYWORDS, doc_wxFontMapper_GetEncodingFromName},
    {sipName_GetEncodingName, SIP_MLMETH_CAST(meth_wxFontMapper_GetEncodingName), METH_VARARGS|METH_KEYWORDS, doc_wxFontMapper_GetEncodingName},
    {sipName_GetSupportedEncodingsCount, meth_wxFontMapper_GetSupportedEncodingsCount, METH_VARARGS, doc_wxFontMapper_GetSupportedEncodingsCount},
    {sipName_IsEncodingAvailable, SIP_MLMETH_CAST(meth_wxFontMapper_IsEncodingAvailable), METH_VARARGS|METH_KEYWORDS, doc_wxFontMapper_IsEncodingAvailable},
    {sipName_Set, SIP_MLMETH_CAST(meth_wxFontMapper_Set), METH_VARARGS|METH_KEYWORDS, doc_wxFontMapper_Set},
    {sipName_SetConfigPath, SIP_MLMETH_CAST(meth_wxFontMapper_SetConfigPath), METH_VARARGS|METH_KEYWORDS, doc_wxFontMapper_SetConfigPath},
    {sipName_SetDialogParent, SIP_MLMETH_CAST(meth_wxFontMapper_SetDialogParent), METH_VARARGS|METH_KEYWORDS, doc_wxFontMapper_SetDialogParent},
    {sipName_SetDialogTitle, SIP_MLMETH_CAST(meth_wxFontMapper_SetDialogTitle), METH_VARARGS|METH_KEYWORDS, doc_wxFontMapper_SetDialogTitle}
};

PyDoc_STRVAR(doc_wxFontMapper, "FontMapper() -> None\n"
"\n"
"wxFontMapper manages user-definable correspondence between logical\n"
"font names and the fonts present on the machine.");


sipClassTypeDef sipTypeDef__core_wxFontMapper = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_CLASS,
        sipNameNr_wxFontMapper,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_FontMapper,
        {0, 0, 1},
        14, methods_wxFontMapper,
        0, SIP_NULLPTR,
        0, SIP_NULLPTR,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxFontMapper,
    -1,
    -1,
    SIP_NULLPTR,
    SIP_NULLPTR,
    init_type_wxFontMapper,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxFontMapper,
    SIP_NULLPTR,
    array_wxFontMapper,
    SIP_NULLPTR,
    release_wxFontMapper,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    array_delete_wxFontMapper,
    sizeof (::wxFontMapper),
};
