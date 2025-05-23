/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_core.h"
        #include <wx/log.h>
        #include <wx/log.h>
        #include <wx/log.h>
        #include <wx/log.h>


class sipwxLogStderr : public ::wxLogStderr
{
public:
    sipwxLogStderr();
    virtual ~sipwxLogStderr();

    /*
     * There is a public method for every protected method visible from
     * this class.
     */
    void sipProtectVirt_DoLogRecord(bool, ::wxLogLevel, const ::wxString&, const ::wxLogRecordInfo&);
    void sipProtectVirt_DoLogTextAtLevel(bool, ::wxLogLevel, const ::wxString&);
    void sipProtectVirt_DoLogText(bool, const ::wxString&);

    /*
     * There is a protected method for every virtual method visible from
     * this class.
     */
protected:
    void Flush() SIP_OVERRIDE;
    void DoLogRecord(::wxLogLevel, const ::wxString&, const ::wxLogRecordInfo&) SIP_OVERRIDE;
    void DoLogTextAtLevel(::wxLogLevel, const ::wxString&) SIP_OVERRIDE;
    void DoLogText(const ::wxString&) SIP_OVERRIDE;

public:
    sipSimpleWrapper *sipPySelf;

private:
    sipwxLogStderr(const sipwxLogStderr &);
    sipwxLogStderr &operator = (const sipwxLogStderr &);

    char sipPyMethods[4];
};

sipwxLogStderr::sipwxLogStderr(): ::wxLogStderr(), sipPySelf(SIP_NULLPTR)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipwxLogStderr::~sipwxLogStderr()
{
    sipInstanceDestroyedEx(&sipPySelf);
}

void sipwxLogStderr::Flush()
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[0], &sipPySelf, SIP_NULLPTR, sipName_Flush);

    if (!sipMeth)
    {
        ::wxLogStderr::Flush();
        return;
    }

    extern void sipVH__core_57(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    sipVH__core_57(sipGILState, 0, sipPySelf, sipMeth);
}

void sipwxLogStderr::DoLogRecord(::wxLogLevel level, const ::wxString& msg, const ::wxLogRecordInfo& info)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[1], &sipPySelf, SIP_NULLPTR, sipName_DoLogRecord);

    if (!sipMeth)
    {
        ::wxLogStderr::DoLogRecord(level, msg, info);
        return;
    }

    extern void sipVH__core_58(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxLogLevel, const ::wxString&, const ::wxLogRecordInfo&);

    sipVH__core_58(sipGILState, 0, sipPySelf, sipMeth, level, msg, info);
}

void sipwxLogStderr::DoLogTextAtLevel(::wxLogLevel level, const ::wxString& msg)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[2], &sipPySelf, SIP_NULLPTR, sipName_DoLogTextAtLevel);

    if (!sipMeth)
    {
        ::wxLogStderr::DoLogTextAtLevel(level, msg);
        return;
    }

    extern void sipVH__core_59(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxLogLevel, const ::wxString&);

    sipVH__core_59(sipGILState, 0, sipPySelf, sipMeth, level, msg);
}

void sipwxLogStderr::DoLogText(const ::wxString& msg)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[3], &sipPySelf, SIP_NULLPTR, sipName_DoLogText);

    if (!sipMeth)
    {
        ::wxLogStderr::DoLogText(msg);
        return;
    }

    extern void sipVH__core_60(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, const ::wxString&);

    sipVH__core_60(sipGILState, 0, sipPySelf, sipMeth, msg);
}

void sipwxLogStderr::sipProtectVirt_DoLogRecord(bool sipSelfWasArg, ::wxLogLevel level, const ::wxString& msg, const ::wxLogRecordInfo& info)
{
    (sipSelfWasArg ? ::wxLog::DoLogRecord(level, msg, info) : DoLogRecord(level, msg, info));
}

void sipwxLogStderr::sipProtectVirt_DoLogTextAtLevel(bool sipSelfWasArg, ::wxLogLevel level, const ::wxString& msg)
{
    (sipSelfWasArg ? ::wxLog::DoLogTextAtLevel(level, msg) : DoLogTextAtLevel(level, msg));
}

void sipwxLogStderr::sipProtectVirt_DoLogText(bool sipSelfWasArg, const ::wxString& msg)
{
    (sipSelfWasArg ? ::wxLog::DoLogText(msg) : DoLogText(msg));
}


PyDoc_STRVAR(doc_wxLogStderr_DoLogRecord, "DoLogRecord(level, msg, info) -> None\n"
"\n"
"Called to log a new record.");

extern "C" {static PyObject *meth_wxLogStderr_DoLogRecord(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxLogStderr_DoLogRecord(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxLogLevel level;
        const ::wxString* msg;
        int msgState = 0;
        const ::wxLogRecordInfo* info;
        sipwxLogStderr *sipCpp;

        static const char *sipKwdList[] = {
            sipName_level,
            sipName_msg,
            sipName_info,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BmJ1J9", &sipSelf, sipType_wxLogStderr, &sipCpp, &level, sipType_wxString, &msg, &msgState, sipType_wxLogRecordInfo, &info))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->sipProtectVirt_DoLogRecord(sipSelfWasArg, level, *msg, *info);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(msg), sipType_wxString, msgState);

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_LogStderr, sipName_DoLogRecord, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxLogStderr_DoLogTextAtLevel, "DoLogTextAtLevel(level, msg) -> None\n"
"\n"
"Called to log the specified string at given level.");

extern "C" {static PyObject *meth_wxLogStderr_DoLogTextAtLevel(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxLogStderr_DoLogTextAtLevel(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxLogLevel level;
        const ::wxString* msg;
        int msgState = 0;
        sipwxLogStderr *sipCpp;

        static const char *sipKwdList[] = {
            sipName_level,
            sipName_msg,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BmJ1", &sipSelf, sipType_wxLogStderr, &sipCpp, &level, sipType_wxString, &msg, &msgState))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->sipProtectVirt_DoLogTextAtLevel(sipSelfWasArg, level, *msg);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(msg), sipType_wxString, msgState);

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_LogStderr, sipName_DoLogTextAtLevel, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxLogStderr_DoLogText, "DoLogText(msg) -> None\n"
"\n"
"Called to log the specified string.");

extern "C" {static PyObject *meth_wxLogStderr_DoLogText(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxLogStderr_DoLogText(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const ::wxString* msg;
        int msgState = 0;
        sipwxLogStderr *sipCpp;

        static const char *sipKwdList[] = {
            sipName_msg,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1", &sipSelf, sipType_wxLogStderr, &sipCpp, sipType_wxString, &msg, &msgState))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->sipProtectVirt_DoLogText(sipSelfWasArg, *msg);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(msg), sipType_wxString, msgState);

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_LogStderr, sipName_DoLogText, SIP_NULLPTR);

    return SIP_NULLPTR;
}


/* Cast a pointer to a type somewhere in its inheritance hierarchy. */
extern "C" {static void *cast_wxLogStderr(void *, const sipTypeDef *);}
static void *cast_wxLogStderr(void *sipCppV, const sipTypeDef *targetType)
{
    ::wxLogStderr *sipCpp = reinterpret_cast<::wxLogStderr *>(sipCppV);

    if (targetType == sipType_wxLogStderr)
        return sipCppV;

    if (targetType == sipType_wxLog)
        return static_cast<::wxLog *>(sipCpp);

    return SIP_NULLPTR;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxLogStderr(void *, int);}
static void release_wxLogStderr(void *sipCppV, int sipState)
{
    Py_BEGIN_ALLOW_THREADS

    if (sipState & SIP_DERIVED_CLASS)
        delete reinterpret_cast<sipwxLogStderr *>(sipCppV);
    else
        delete reinterpret_cast<::wxLogStderr *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void dealloc_wxLogStderr(sipSimpleWrapper *);}
static void dealloc_wxLogStderr(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerivedClass(sipSelf))
        reinterpret_cast<sipwxLogStderr *>(sipGetAddress(sipSelf))->sipPySelf = SIP_NULLPTR;

    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxLogStderr(sipGetAddress(sipSelf), sipIsDerivedClass(sipSelf));
    }
}


extern "C" {static void *init_type_wxLogStderr(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxLogStderr(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    sipwxLogStderr *sipCpp = SIP_NULLPTR;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, ""))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipwxLogStderr();
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
static sipEncodedTypeDef supers_wxLogStderr[] = {{330, 255, 1}};


static PyMethodDef methods_wxLogStderr[] = {
    {sipName_DoLogRecord, SIP_MLMETH_CAST(meth_wxLogStderr_DoLogRecord), METH_VARARGS|METH_KEYWORDS, SIP_NULLPTR},
    {sipName_DoLogText, SIP_MLMETH_CAST(meth_wxLogStderr_DoLogText), METH_VARARGS|METH_KEYWORDS, SIP_NULLPTR},
    {sipName_DoLogTextAtLevel, SIP_MLMETH_CAST(meth_wxLogStderr_DoLogTextAtLevel), METH_VARARGS|METH_KEYWORDS, SIP_NULLPTR}
};

PyDoc_STRVAR(doc_wxLogStderr, "LogStderr() -> None\n"
"\n"
"This class can be used to redirect the log messages to a C file stream\n"
"(not to be confused with C++ streams).");


sipClassTypeDef sipTypeDef__core_wxLogStderr = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_CLASS,
        sipNameNr_wxLogStderr,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_LogStderr,
        {0, 0, 1},
        3, methods_wxLogStderr,
        0, SIP_NULLPTR,
        0, SIP_NULLPTR,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxLogStderr,
    -1,
    -1,
    supers_wxLogStderr,
    SIP_NULLPTR,
    init_type_wxLogStderr,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxLogStderr,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    release_wxLogStderr,
    cast_wxLogStderr,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    sizeof (::wxLogStderr),
};
