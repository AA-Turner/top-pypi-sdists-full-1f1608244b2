/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_core.h"
        #include <wx/fs_filter.h>
        #include <wx/filesys.h>
        #include <wx/filesys.h>
        #include <wx/object.h>
        #include <wx/object.h>
        #include <wx/object.h>


class sipwxFilterFSHandler : public ::wxFilterFSHandler
{
public:
    sipwxFilterFSHandler();
    virtual ~sipwxFilterFSHandler();

    /*
     * There is a public method for every protected method visible from
     * this class.
     */
    static ::wxString sipProtect_GetAnchor(const ::wxString&);
    static ::wxString sipProtect_GetLeftLocation(const ::wxString&);
    static ::wxString sipProtect_GetProtocol(const ::wxString&);
    static ::wxString sipProtect_GetRightLocation(const ::wxString&);

    /*
     * There is a protected method for every virtual method visible from
     * this class.
     */
protected:
    bool CanOpen(const ::wxString&) SIP_OVERRIDE;
    ::wxString FindFirst(const ::wxString&, int) SIP_OVERRIDE;
    ::wxString FindNext() SIP_OVERRIDE;
    ::wxFSFile* OpenFile(::wxFileSystem&, const ::wxString&) SIP_OVERRIDE;

public:
    sipSimpleWrapper *sipPySelf;

private:
    sipwxFilterFSHandler(const sipwxFilterFSHandler &);
    sipwxFilterFSHandler &operator = (const sipwxFilterFSHandler &);

    char sipPyMethods[4];
};

sipwxFilterFSHandler::sipwxFilterFSHandler(): ::wxFilterFSHandler(), sipPySelf(SIP_NULLPTR)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipwxFilterFSHandler::~sipwxFilterFSHandler()
{
    sipInstanceDestroyedEx(&sipPySelf);
}

bool sipwxFilterFSHandler::CanOpen(const ::wxString& location)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[0], &sipPySelf, SIP_NULLPTR, sipName_CanOpen);

    if (!sipMeth)
        return ::wxFilterFSHandler::CanOpen(location);

    extern bool sipVH__core_9(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, const ::wxString&);

    return sipVH__core_9(sipGILState, 0, sipPySelf, sipMeth, location);
}

::wxString sipwxFilterFSHandler::FindFirst(const ::wxString& spec, int flags)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[1], &sipPySelf, SIP_NULLPTR, sipName_FindFirst);

    if (!sipMeth)
        return ::wxFilterFSHandler::FindFirst(spec, flags);

    extern ::wxString sipVH__core_10(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, const ::wxString&, int);

    return sipVH__core_10(sipGILState, 0, sipPySelf, sipMeth, spec, flags);
}

::wxString sipwxFilterFSHandler::FindNext()
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[2], &sipPySelf, SIP_NULLPTR, sipName_FindNext);

    if (!sipMeth)
        return ::wxFilterFSHandler::FindNext();

    extern ::wxString sipVH__core_11(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__core_11(sipGILState, 0, sipPySelf, sipMeth);
}

::wxFSFile* sipwxFilterFSHandler::OpenFile(::wxFileSystem& fs, const ::wxString& location)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[3], &sipPySelf, SIP_NULLPTR, sipName_OpenFile);

    if (!sipMeth)
        return ::wxFilterFSHandler::OpenFile(fs, location);

    extern ::wxFSFile* sipVH__core_12(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxFileSystem&, const ::wxString&);

    return sipVH__core_12(sipGILState, 0, sipPySelf, sipMeth, fs, location);
}

::wxString sipwxFilterFSHandler::sipProtect_GetAnchor(const ::wxString& location)
{
    return ::wxFileSystemHandler::GetAnchor(location);
}

::wxString sipwxFilterFSHandler::sipProtect_GetLeftLocation(const ::wxString& location)
{
    return ::wxFileSystemHandler::GetLeftLocation(location);
}

::wxString sipwxFilterFSHandler::sipProtect_GetProtocol(const ::wxString& location)
{
    return ::wxFileSystemHandler::GetProtocol(location);
}

::wxString sipwxFilterFSHandler::sipProtect_GetRightLocation(const ::wxString& location)
{
    return ::wxFileSystemHandler::GetRightLocation(location);
}


PyDoc_STRVAR(doc_wxFilterFSHandler_GetAnchor, "GetAnchor(location) -> str\n"
"\n"
"Returns the anchor if present in the location.");

extern "C" {static PyObject *meth_wxFilterFSHandler_GetAnchor(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxFilterFSHandler_GetAnchor(PyObject *, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxString* location;
        int locationState = 0;

        static const char *sipKwdList[] = {
            sipName_location,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "J1", sipType_wxString, &location, &locationState))
        {
            ::wxString*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxString(sipwxFilterFSHandler::sipProtect_GetAnchor(*location));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(location), sipType_wxString, locationState);

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxString, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_FilterFSHandler, sipName_GetAnchor, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxFilterFSHandler_GetLeftLocation, "GetLeftLocation(location) -> str\n"
"\n"
"Returns the left location string extracted from location.");

extern "C" {static PyObject *meth_wxFilterFSHandler_GetLeftLocation(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxFilterFSHandler_GetLeftLocation(PyObject *, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxString* location;
        int locationState = 0;

        static const char *sipKwdList[] = {
            sipName_location,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "J1", sipType_wxString, &location, &locationState))
        {
            ::wxString*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxString(sipwxFilterFSHandler::sipProtect_GetLeftLocation(*location));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(location), sipType_wxString, locationState);

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxString, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_FilterFSHandler, sipName_GetLeftLocation, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxFilterFSHandler_GetProtocol, "GetProtocol(location) -> str\n"
"\n"
"Returns the protocol string extracted from location.");

extern "C" {static PyObject *meth_wxFilterFSHandler_GetProtocol(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxFilterFSHandler_GetProtocol(PyObject *, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxString* location;
        int locationState = 0;

        static const char *sipKwdList[] = {
            sipName_location,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "J1", sipType_wxString, &location, &locationState))
        {
            ::wxString*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxString(sipwxFilterFSHandler::sipProtect_GetProtocol(*location));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(location), sipType_wxString, locationState);

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxString, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_FilterFSHandler, sipName_GetProtocol, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxFilterFSHandler_GetRightLocation, "GetRightLocation(location) -> str\n"
"\n"
"Returns the right location string extracted from location.");

extern "C" {static PyObject *meth_wxFilterFSHandler_GetRightLocation(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxFilterFSHandler_GetRightLocation(PyObject *, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxString* location;
        int locationState = 0;

        static const char *sipKwdList[] = {
            sipName_location,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "J1", sipType_wxString, &location, &locationState))
        {
            ::wxString*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxString(sipwxFilterFSHandler::sipProtect_GetRightLocation(*location));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(location), sipType_wxString, locationState);

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxString, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_FilterFSHandler, sipName_GetRightLocation, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxFilterFSHandler_CanOpen, "CanOpen(self, location: Any) -> bool");

extern "C" {static PyObject *meth_wxFilterFSHandler_CanOpen(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxFilterFSHandler_CanOpen(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const ::wxString* location;
        int locationState = 0;
        ::wxFilterFSHandler *sipCpp;

        static const char *sipKwdList[] = {
            sipName_location,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1", &sipSelf, sipType_wxFilterFSHandler, &sipCpp, sipType_wxString, &location, &locationState))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxFilterFSHandler::CanOpen(*location) : sipCpp->CanOpen(*location));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(location), sipType_wxString, locationState);

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_FilterFSHandler, sipName_CanOpen, doc_wxFilterFSHandler_CanOpen);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxFilterFSHandler_OpenFile, "OpenFile(self, fs: FileSystem, location: Any) -> Optional[FSFile]");

extern "C" {static PyObject *meth_wxFilterFSHandler_OpenFile(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxFilterFSHandler_OpenFile(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxFileSystem* fs;
        const ::wxString* location;
        int locationState = 0;
        ::wxFilterFSHandler *sipCpp;

        static const char *sipKwdList[] = {
            sipName_fs,
            sipName_location,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ9J1", &sipSelf, sipType_wxFilterFSHandler, &sipCpp, sipType_wxFileSystem, &fs, sipType_wxString, &location, &locationState))
        {
            ::wxFSFile*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxFilterFSHandler::OpenFile(*fs, *location) : sipCpp->OpenFile(*fs, *location));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(location), sipType_wxString, locationState);

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxFSFile, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_FilterFSHandler, sipName_OpenFile, doc_wxFilterFSHandler_OpenFile);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxFilterFSHandler_FindFirst, "FindFirst(self, spec: Any, flags: int = 0) -> Any");

extern "C" {static PyObject *meth_wxFilterFSHandler_FindFirst(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxFilterFSHandler_FindFirst(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const ::wxString* spec;
        int specState = 0;
        int flags = 0;
        ::wxFilterFSHandler *sipCpp;

        static const char *sipKwdList[] = {
            sipName_spec,
            sipName_flags,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1|i", &sipSelf, sipType_wxFilterFSHandler, &sipCpp, sipType_wxString, &spec, &specState, &flags))
        {
            ::wxString*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxString((sipSelfWasArg ? sipCpp->::wxFilterFSHandler::FindFirst(*spec, flags) : sipCpp->FindFirst(*spec, flags)));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(spec), sipType_wxString, specState);

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxString, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_FilterFSHandler, sipName_FindFirst, doc_wxFilterFSHandler_FindFirst);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxFilterFSHandler_FindNext, "FindNext(self) -> Any");

extern "C" {static PyObject *meth_wxFilterFSHandler_FindNext(PyObject *, PyObject *);}
static PyObject *meth_wxFilterFSHandler_FindNext(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxFilterFSHandler *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxFilterFSHandler, &sipCpp))
        {
            ::wxString*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxString((sipSelfWasArg ? sipCpp->::wxFilterFSHandler::FindNext() : sipCpp->FindNext()));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxString, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_FilterFSHandler, sipName_FindNext, doc_wxFilterFSHandler_FindNext);

    return SIP_NULLPTR;
}


/* Cast a pointer to a type somewhere in its inheritance hierarchy. */
extern "C" {static void *cast_wxFilterFSHandler(void *, const sipTypeDef *);}
static void *cast_wxFilterFSHandler(void *sipCppV, const sipTypeDef *targetType)
{
    ::wxFilterFSHandler *sipCpp = reinterpret_cast<::wxFilterFSHandler *>(sipCppV);

    if (targetType == sipType_wxFilterFSHandler)
        return sipCppV;

    sipCppV = ((const sipClassTypeDef *)sipType_wxFileSystemHandler)->ctd_cast(static_cast<::wxFileSystemHandler *>(sipCpp), targetType);
    if (sipCppV)
        return sipCppV;

    return SIP_NULLPTR;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxFilterFSHandler(void *, int);}
static void release_wxFilterFSHandler(void *sipCppV, int sipState)
{
    Py_BEGIN_ALLOW_THREADS

    if (sipState & SIP_DERIVED_CLASS)
        delete reinterpret_cast<sipwxFilterFSHandler *>(sipCppV);
    else
        delete reinterpret_cast<::wxFilterFSHandler *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void *array_wxFilterFSHandler(Py_ssize_t);}
static void *array_wxFilterFSHandler(Py_ssize_t sipNrElem)
{
    return new ::wxFilterFSHandler[sipNrElem];
}


extern "C" {static void array_delete_wxFilterFSHandler(void *);}
static void array_delete_wxFilterFSHandler(void *sipCpp)
{
    delete[] reinterpret_cast<::wxFilterFSHandler *>(sipCpp);
}


extern "C" {static void dealloc_wxFilterFSHandler(sipSimpleWrapper *);}
static void dealloc_wxFilterFSHandler(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerivedClass(sipSelf))
        reinterpret_cast<sipwxFilterFSHandler *>(sipGetAddress(sipSelf))->sipPySelf = SIP_NULLPTR;

    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxFilterFSHandler(sipGetAddress(sipSelf), sipIsDerivedClass(sipSelf));
    }
}


extern "C" {static void *init_type_wxFilterFSHandler(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxFilterFSHandler(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    sipwxFilterFSHandler *sipCpp = SIP_NULLPTR;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, ""))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipwxFilterFSHandler();
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
static sipEncodedTypeDef supers_wxFilterFSHandler[] = {{186, 255, 1}};


static PyMethodDef methods_wxFilterFSHandler[] = {
    {sipName_CanOpen, SIP_MLMETH_CAST(meth_wxFilterFSHandler_CanOpen), METH_VARARGS|METH_KEYWORDS, doc_wxFilterFSHandler_CanOpen},
    {sipName_FindFirst, SIP_MLMETH_CAST(meth_wxFilterFSHandler_FindFirst), METH_VARARGS|METH_KEYWORDS, doc_wxFilterFSHandler_FindFirst},
    {sipName_FindNext, meth_wxFilterFSHandler_FindNext, METH_VARARGS, doc_wxFilterFSHandler_FindNext},
    {sipName_GetAnchor, SIP_MLMETH_CAST(meth_wxFilterFSHandler_GetAnchor), METH_VARARGS|METH_KEYWORDS, SIP_NULLPTR},
    {sipName_GetLeftLocation, SIP_MLMETH_CAST(meth_wxFilterFSHandler_GetLeftLocation), METH_VARARGS|METH_KEYWORDS, SIP_NULLPTR},
    {sipName_GetProtocol, SIP_MLMETH_CAST(meth_wxFilterFSHandler_GetProtocol), METH_VARARGS|METH_KEYWORDS, SIP_NULLPTR},
    {sipName_GetRightLocation, SIP_MLMETH_CAST(meth_wxFilterFSHandler_GetRightLocation), METH_VARARGS|METH_KEYWORDS, SIP_NULLPTR},
    {sipName_OpenFile, SIP_MLMETH_CAST(meth_wxFilterFSHandler_OpenFile), METH_VARARGS|METH_KEYWORDS, doc_wxFilterFSHandler_OpenFile}
};

PyDoc_STRVAR(doc_wxFilterFSHandler, "FilterFSHandler() -> None\n"
"\n"
"Filter file system handler.");


sipClassTypeDef sipTypeDef__core_wxFilterFSHandler = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_SCC|SIP_TYPE_CLASS,
        sipNameNr_wxFilterFSHandler,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_FilterFSHandler,
        {0, 0, 1},
        8, methods_wxFilterFSHandler,
        0, SIP_NULLPTR,
        0, SIP_NULLPTR,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxFilterFSHandler,
    -1,
    -1,
    supers_wxFilterFSHandler,
    SIP_NULLPTR,
    init_type_wxFilterFSHandler,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxFilterFSHandler,
    SIP_NULLPTR,
    array_wxFilterFSHandler,
    SIP_NULLPTR,
    release_wxFilterFSHandler,
    cast_wxFilterFSHandler,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    array_delete_wxFilterFSHandler,
    sizeof (::wxFilterFSHandler),
};
