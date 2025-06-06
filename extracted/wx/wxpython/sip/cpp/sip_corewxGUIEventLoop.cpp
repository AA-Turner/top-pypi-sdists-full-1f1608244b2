/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_core.h"
        #include <wx/evtloop.h>
        #include <wx/evtloop.h>


class sipwxGUIEventLoop : public ::wxGUIEventLoop
{
public:
    sipwxGUIEventLoop();
    virtual ~sipwxGUIEventLoop();

    /*
     * There is a public method for every protected method visible from
     * this class.
     */
    void sipProtectVirt_OnExit(bool);

    /*
     * There is a protected method for every virtual method visible from
     * this class.
     */
protected:
    bool YieldFor(long) SIP_OVERRIDE;
    int Run() SIP_OVERRIDE;
    bool IsOk() const SIP_OVERRIDE;
    void Exit(int) SIP_OVERRIDE;
    void ScheduleExit(int) SIP_OVERRIDE;
    bool Pending() const SIP_OVERRIDE;
    bool Dispatch() SIP_OVERRIDE;
    int DispatchTimeout(unsigned long) SIP_OVERRIDE;
    void WakeUp() SIP_OVERRIDE;
    bool ProcessIdle() SIP_OVERRIDE;
    bool IsYielding() const SIP_OVERRIDE;
    bool IsEventAllowedInsideYield(::wxEventCategory) const SIP_OVERRIDE;
    void OnExit() SIP_OVERRIDE;

public:
    sipSimpleWrapper *sipPySelf;

private:
    sipwxGUIEventLoop(const sipwxGUIEventLoop &);
    sipwxGUIEventLoop &operator = (const sipwxGUIEventLoop &);

    char sipPyMethods[13];
};

sipwxGUIEventLoop::sipwxGUIEventLoop(): ::wxGUIEventLoop(), sipPySelf(SIP_NULLPTR)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipwxGUIEventLoop::~sipwxGUIEventLoop()
{
    sipInstanceDestroyedEx(&sipPySelf);
}

bool sipwxGUIEventLoop::YieldFor(long eventsToProcess)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[0], &sipPySelf, SIP_NULLPTR, sipName_YieldFor);

    if (!sipMeth)
        return ::wxGUIEventLoop::YieldFor(eventsToProcess);

    extern bool sipVH__core_116(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, long);

    return sipVH__core_116(sipGILState, 0, sipPySelf, sipMeth, eventsToProcess);
}

int sipwxGUIEventLoop::Run()
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[1], &sipPySelf, SIP_NULLPTR, sipName_Run);

    if (!sipMeth)
        return ::wxGUIEventLoop::Run();

    extern int sipVH__core_112(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__core_112(sipGILState, 0, sipPySelf, sipMeth);
}

bool sipwxGUIEventLoop::IsOk() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[2]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_IsOk);

    if (!sipMeth)
        return ::wxGUIEventLoop::IsOk();

    extern bool sipVH__core_6(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__core_6(sipGILState, 0, sipPySelf, sipMeth);
}

void sipwxGUIEventLoop::Exit(int rc)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[3], &sipPySelf, SIP_NULLPTR, sipName_Exit);

    if (!sipMeth)
    {
        ::wxGUIEventLoop::Exit(rc);
        return;
    }

    extern void sipVH__core_113(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, int);

    sipVH__core_113(sipGILState, 0, sipPySelf, sipMeth, rc);
}

void sipwxGUIEventLoop::ScheduleExit(int rc)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[4], &sipPySelf, SIP_NULLPTR, sipName_ScheduleExit);

    if (!sipMeth)
    {
        ::wxGUIEventLoop::ScheduleExit(rc);
        return;
    }

    extern void sipVH__core_113(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, int);

    sipVH__core_113(sipGILState, 0, sipPySelf, sipMeth, rc);
}

bool sipwxGUIEventLoop::Pending() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[5]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_Pending);

    if (!sipMeth)
        return ::wxGUIEventLoop::Pending();

    extern bool sipVH__core_6(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__core_6(sipGILState, 0, sipPySelf, sipMeth);
}

bool sipwxGUIEventLoop::Dispatch()
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[6], &sipPySelf, SIP_NULLPTR, sipName_Dispatch);

    if (!sipMeth)
        return ::wxGUIEventLoop::Dispatch();

    extern bool sipVH__core_6(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__core_6(sipGILState, 0, sipPySelf, sipMeth);
}

int sipwxGUIEventLoop::DispatchTimeout(unsigned long timeout)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[7], &sipPySelf, SIP_NULLPTR, sipName_DispatchTimeout);

    if (!sipMeth)
        return ::wxGUIEventLoop::DispatchTimeout(timeout);

    extern int sipVH__core_114(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, unsigned long);

    return sipVH__core_114(sipGILState, 0, sipPySelf, sipMeth, timeout);
}

void sipwxGUIEventLoop::WakeUp()
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[8], &sipPySelf, SIP_NULLPTR, sipName_WakeUp);

    if (!sipMeth)
    {
        ::wxGUIEventLoop::WakeUp();
        return;
    }

    extern void sipVH__core_57(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    sipVH__core_57(sipGILState, 0, sipPySelf, sipMeth);
}

bool sipwxGUIEventLoop::ProcessIdle()
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[9], &sipPySelf, SIP_NULLPTR, sipName_ProcessIdle);

    if (!sipMeth)
        return ::wxGUIEventLoop::ProcessIdle();

    extern bool sipVH__core_6(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__core_6(sipGILState, 0, sipPySelf, sipMeth);
}

bool sipwxGUIEventLoop::IsYielding() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[10]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_IsYielding);

    if (!sipMeth)
        return ::wxGUIEventLoop::IsYielding();

    extern bool sipVH__core_6(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__core_6(sipGILState, 0, sipPySelf, sipMeth);
}

bool sipwxGUIEventLoop::IsEventAllowedInsideYield(::wxEventCategory cat) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[11]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_IsEventAllowedInsideYield);

    if (!sipMeth)
        return ::wxGUIEventLoop::IsEventAllowedInsideYield(cat);

    extern bool sipVH__core_115(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxEventCategory);

    return sipVH__core_115(sipGILState, 0, sipPySelf, sipMeth, cat);
}

void sipwxGUIEventLoop::OnExit()
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[12], &sipPySelf, SIP_NULLPTR, sipName_OnExit);

    if (!sipMeth)
    {
        ::wxGUIEventLoop::OnExit();
        return;
    }

    extern void sipVH__core_57(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    sipVH__core_57(sipGILState, 0, sipPySelf, sipMeth);
}

void sipwxGUIEventLoop::sipProtectVirt_OnExit(bool sipSelfWasArg)
{
    (sipSelfWasArg ? ::wxEventLoopBase::OnExit() : OnExit());
}


PyDoc_STRVAR(doc_wxGUIEventLoop_OnExit, "OnExit() -> None\n"
"\n"
"This function is called before the event loop terminates, whether this\n"
"happens normally (because of Exit() call) or abnormally (because of an\n"
"exception thrown from inside the loop).");

extern "C" {static PyObject *meth_wxGUIEventLoop_OnExit(PyObject *, PyObject *);}
static PyObject *meth_wxGUIEventLoop_OnExit(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        sipwxGUIEventLoop *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGUIEventLoop, &sipCpp))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->sipProtectVirt_OnExit(sipSelfWasArg);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_GUIEventLoop, sipName_OnExit, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGUIEventLoop_Run, "Run(self) -> int");

extern "C" {static PyObject *meth_wxGUIEventLoop_Run(PyObject *, PyObject *);}
static PyObject *meth_wxGUIEventLoop_Run(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxGUIEventLoop *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGUIEventLoop, &sipCpp))
        {
            int sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxGUIEventLoop::Run() : sipCpp->Run());
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyLong_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_GUIEventLoop, sipName_Run, doc_wxGUIEventLoop_Run);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGUIEventLoop_Exit, "Exit(self, rc: int = 0)");

extern "C" {static PyObject *meth_wxGUIEventLoop_Exit(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxGUIEventLoop_Exit(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        int rc = 0;
        ::wxGUIEventLoop *sipCpp;

        static const char *sipKwdList[] = {
            sipName_rc,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "B|i", &sipSelf, sipType_wxGUIEventLoop, &sipCpp, &rc))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            (sipSelfWasArg ? sipCpp->::wxGUIEventLoop::Exit(rc) : sipCpp->Exit(rc));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_GUIEventLoop, sipName_Exit, doc_wxGUIEventLoop_Exit);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGUIEventLoop_ScheduleExit, "ScheduleExit(self, rc: int = 0)");

extern "C" {static PyObject *meth_wxGUIEventLoop_ScheduleExit(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxGUIEventLoop_ScheduleExit(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        int rc = 0;
        ::wxGUIEventLoop *sipCpp;

        static const char *sipKwdList[] = {
            sipName_rc,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "B|i", &sipSelf, sipType_wxGUIEventLoop, &sipCpp, &rc))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            (sipSelfWasArg ? sipCpp->::wxGUIEventLoop::ScheduleExit(rc) : sipCpp->ScheduleExit(rc));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_GUIEventLoop, sipName_ScheduleExit, doc_wxGUIEventLoop_ScheduleExit);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGUIEventLoop_Pending, "Pending(self) -> bool");

extern "C" {static PyObject *meth_wxGUIEventLoop_Pending(PyObject *, PyObject *);}
static PyObject *meth_wxGUIEventLoop_Pending(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const ::wxGUIEventLoop *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGUIEventLoop, &sipCpp))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxGUIEventLoop::Pending() : sipCpp->Pending());
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_GUIEventLoop, sipName_Pending, doc_wxGUIEventLoop_Pending);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGUIEventLoop_Dispatch, "Dispatch(self) -> bool");

extern "C" {static PyObject *meth_wxGUIEventLoop_Dispatch(PyObject *, PyObject *);}
static PyObject *meth_wxGUIEventLoop_Dispatch(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxGUIEventLoop *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGUIEventLoop, &sipCpp))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxGUIEventLoop::Dispatch() : sipCpp->Dispatch());
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_GUIEventLoop, sipName_Dispatch, doc_wxGUIEventLoop_Dispatch);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGUIEventLoop_DispatchTimeout, "DispatchTimeout(self, timeout: int) -> int");

extern "C" {static PyObject *meth_wxGUIEventLoop_DispatchTimeout(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxGUIEventLoop_DispatchTimeout(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        unsigned long timeout;
        ::wxGUIEventLoop *sipCpp;

        static const char *sipKwdList[] = {
            sipName_timeout,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "Bm", &sipSelf, sipType_wxGUIEventLoop, &sipCpp, &timeout))
        {
            int sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxGUIEventLoop::DispatchTimeout(timeout) : sipCpp->DispatchTimeout(timeout));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyLong_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_GUIEventLoop, sipName_DispatchTimeout, doc_wxGUIEventLoop_DispatchTimeout);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGUIEventLoop_WakeUp, "WakeUp(self)");

extern "C" {static PyObject *meth_wxGUIEventLoop_WakeUp(PyObject *, PyObject *);}
static PyObject *meth_wxGUIEventLoop_WakeUp(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxGUIEventLoop *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGUIEventLoop, &sipCpp))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            (sipSelfWasArg ? sipCpp->::wxGUIEventLoop::WakeUp() : sipCpp->WakeUp());
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_GUIEventLoop, sipName_WakeUp, doc_wxGUIEventLoop_WakeUp);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGUIEventLoop_YieldFor, "YieldFor(self, eventsToProcess: int) -> bool");

extern "C" {static PyObject *meth_wxGUIEventLoop_YieldFor(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxGUIEventLoop_YieldFor(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        long eventsToProcess;
        ::wxGUIEventLoop *sipCpp;

        static const char *sipKwdList[] = {
            sipName_eventsToProcess,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "Bl", &sipSelf, sipType_wxGUIEventLoop, &sipCpp, &eventsToProcess))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxGUIEventLoop::YieldFor(eventsToProcess) : sipCpp->YieldFor(eventsToProcess));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_GUIEventLoop, sipName_YieldFor, doc_wxGUIEventLoop_YieldFor);

    return SIP_NULLPTR;
}


/* Cast a pointer to a type somewhere in its inheritance hierarchy. */
extern "C" {static void *cast_wxGUIEventLoop(void *, const sipTypeDef *);}
static void *cast_wxGUIEventLoop(void *sipCppV, const sipTypeDef *targetType)
{
    ::wxGUIEventLoop *sipCpp = reinterpret_cast<::wxGUIEventLoop *>(sipCppV);

    if (targetType == sipType_wxGUIEventLoop)
        return sipCppV;

    if (targetType == sipType_wxEventLoopBase)
        return static_cast<::wxEventLoopBase *>(sipCpp);

    return SIP_NULLPTR;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxGUIEventLoop(void *, int);}
static void release_wxGUIEventLoop(void *sipCppV, int sipState)
{
    Py_BEGIN_ALLOW_THREADS

    if (sipState & SIP_DERIVED_CLASS)
        delete reinterpret_cast<sipwxGUIEventLoop *>(sipCppV);
    else
        delete reinterpret_cast<::wxGUIEventLoop *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void *array_wxGUIEventLoop(Py_ssize_t);}
static void *array_wxGUIEventLoop(Py_ssize_t sipNrElem)
{
    return new ::wxGUIEventLoop[sipNrElem];
}


extern "C" {static void array_delete_wxGUIEventLoop(void *);}
static void array_delete_wxGUIEventLoop(void *sipCpp)
{
    delete[] reinterpret_cast<::wxGUIEventLoop *>(sipCpp);
}


extern "C" {static void dealloc_wxGUIEventLoop(sipSimpleWrapper *);}
static void dealloc_wxGUIEventLoop(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerivedClass(sipSelf))
        reinterpret_cast<sipwxGUIEventLoop *>(sipGetAddress(sipSelf))->sipPySelf = SIP_NULLPTR;

    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxGUIEventLoop(sipGetAddress(sipSelf), sipIsDerivedClass(sipSelf));
    }
}


extern "C" {static void *init_type_wxGUIEventLoop(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxGUIEventLoop(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    sipwxGUIEventLoop *sipCpp = SIP_NULLPTR;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, ""))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipwxGUIEventLoop();
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
static sipEncodedTypeDef supers_wxGUIEventLoop[] = {{156, 255, 1}};


static PyMethodDef methods_wxGUIEventLoop[] = {
    {sipName_Dispatch, meth_wxGUIEventLoop_Dispatch, METH_VARARGS, doc_wxGUIEventLoop_Dispatch},
    {sipName_DispatchTimeout, SIP_MLMETH_CAST(meth_wxGUIEventLoop_DispatchTimeout), METH_VARARGS|METH_KEYWORDS, doc_wxGUIEventLoop_DispatchTimeout},
    {sipName_Exit, SIP_MLMETH_CAST(meth_wxGUIEventLoop_Exit), METH_VARARGS|METH_KEYWORDS, doc_wxGUIEventLoop_Exit},
    {sipName_OnExit, meth_wxGUIEventLoop_OnExit, METH_VARARGS, SIP_NULLPTR},
    {sipName_Pending, meth_wxGUIEventLoop_Pending, METH_VARARGS, doc_wxGUIEventLoop_Pending},
    {sipName_Run, meth_wxGUIEventLoop_Run, METH_VARARGS, doc_wxGUIEventLoop_Run},
    {sipName_ScheduleExit, SIP_MLMETH_CAST(meth_wxGUIEventLoop_ScheduleExit), METH_VARARGS|METH_KEYWORDS, doc_wxGUIEventLoop_ScheduleExit},
    {sipName_WakeUp, meth_wxGUIEventLoop_WakeUp, METH_VARARGS, doc_wxGUIEventLoop_WakeUp},
    {sipName_YieldFor, SIP_MLMETH_CAST(meth_wxGUIEventLoop_YieldFor), METH_VARARGS|METH_KEYWORDS, doc_wxGUIEventLoop_YieldFor}
};

PyDoc_STRVAR(doc_wxGUIEventLoop, "GUIEventLoop() -> None\n"
"\n"
"A generic implementation of the GUI event loop.");


sipClassTypeDef sipTypeDef__core_wxGUIEventLoop = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_CLASS,
        sipNameNr_wxGUIEventLoop,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_GUIEventLoop,
        {0, 0, 1},
        9, methods_wxGUIEventLoop,
        0, SIP_NULLPTR,
        0, SIP_NULLPTR,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxGUIEventLoop,
    -1,
    -1,
    supers_wxGUIEventLoop,
    SIP_NULLPTR,
    init_type_wxGUIEventLoop,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxGUIEventLoop,
    SIP_NULLPTR,
    array_wxGUIEventLoop,
    SIP_NULLPTR,
    release_wxGUIEventLoop,
    cast_wxGUIEventLoop,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    array_delete_wxGUIEventLoop,
    sizeof (::wxGUIEventLoop),
};
