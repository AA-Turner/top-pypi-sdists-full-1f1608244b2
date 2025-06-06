/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_core.h"
        #include <wx/event.h>
        #include <wx/window.h>
        #include <wx/event.h>
        #include <wx/object.h>
        #include <wx/object.h>
        #include <wx/object.h>


class sipwxWindowCreateEvent : public ::wxWindowCreateEvent
{
public:
    sipwxWindowCreateEvent(::wxWindow*);
    sipwxWindowCreateEvent(const ::wxWindowCreateEvent&);
    virtual ~sipwxWindowCreateEvent();

    /*
     * There is a protected method for every virtual method visible from
     * this class.
     */
protected:
    ::wxEventCategory GetEventCategory() const SIP_OVERRIDE;
    ::wxEvent* Clone() const SIP_OVERRIDE;

public:
    sipSimpleWrapper *sipPySelf;

private:
    sipwxWindowCreateEvent(const sipwxWindowCreateEvent &);
    sipwxWindowCreateEvent &operator = (const sipwxWindowCreateEvent &);

    char sipPyMethods[2];
};

sipwxWindowCreateEvent::sipwxWindowCreateEvent(::wxWindow*win): ::wxWindowCreateEvent(win), sipPySelf(SIP_NULLPTR)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipwxWindowCreateEvent::sipwxWindowCreateEvent(const ::wxWindowCreateEvent& a0): ::wxWindowCreateEvent(a0), sipPySelf(SIP_NULLPTR)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipwxWindowCreateEvent::~sipwxWindowCreateEvent()
{
    sipInstanceDestroyedEx(&sipPySelf);
}

::wxEventCategory sipwxWindowCreateEvent::GetEventCategory() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[0]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_GetEventCategory);

    if (!sipMeth)
        return ::wxWindowCreateEvent::GetEventCategory();

    extern ::wxEventCategory sipVH__core_104(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__core_104(sipGILState, 0, sipPySelf, sipMeth);
}

::wxEvent* sipwxWindowCreateEvent::Clone() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[1]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_Clone);

    if (!sipMeth)
        return ::wxWindowCreateEvent::Clone();

    extern ::wxEvent* sipVH__core_103(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__core_103(sipGILState, 0, sipPySelf, sipMeth);
}


PyDoc_STRVAR(doc_wxWindowCreateEvent_GetWindow, "GetWindow() -> Window\n"
"\n"
"Return the window being created.");

extern "C" {static PyObject *meth_wxWindowCreateEvent_GetWindow(PyObject *, PyObject *);}
static PyObject *meth_wxWindowCreateEvent_GetWindow(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxWindowCreateEvent *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxWindowCreateEvent, &sipCpp))
        {
            ::wxWindow*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetWindow();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxWindow, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_WindowCreateEvent, sipName_GetWindow, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxWindowCreateEvent_Clone, "Clone(self) -> Optional[Event]");

extern "C" {static PyObject *meth_wxWindowCreateEvent_Clone(PyObject *, PyObject *);}
static PyObject *meth_wxWindowCreateEvent_Clone(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const ::wxWindowCreateEvent *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxWindowCreateEvent, &sipCpp))
        {
            ::wxEvent*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxWindowCreateEvent::Clone() : sipCpp->Clone());
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxEvent, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_WindowCreateEvent, sipName_Clone, doc_wxWindowCreateEvent_Clone);

    return SIP_NULLPTR;
}


/* Cast a pointer to a type somewhere in its inheritance hierarchy. */
extern "C" {static void *cast_wxWindowCreateEvent(void *, const sipTypeDef *);}
static void *cast_wxWindowCreateEvent(void *sipCppV, const sipTypeDef *targetType)
{
    ::wxWindowCreateEvent *sipCpp = reinterpret_cast<::wxWindowCreateEvent *>(sipCppV);

    if (targetType == sipType_wxWindowCreateEvent)
        return sipCppV;

    sipCppV = ((const sipClassTypeDef *)sipType_wxCommandEvent)->ctd_cast(static_cast<::wxCommandEvent *>(sipCpp), targetType);
    if (sipCppV)
        return sipCppV;

    return SIP_NULLPTR;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxWindowCreateEvent(void *, int);}
static void release_wxWindowCreateEvent(void *sipCppV, int sipState)
{
    Py_BEGIN_ALLOW_THREADS

    if (sipState & SIP_DERIVED_CLASS)
        delete reinterpret_cast<sipwxWindowCreateEvent *>(sipCppV);
    else
        delete reinterpret_cast<::wxWindowCreateEvent *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void dealloc_wxWindowCreateEvent(sipSimpleWrapper *);}
static void dealloc_wxWindowCreateEvent(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerivedClass(sipSelf))
        reinterpret_cast<sipwxWindowCreateEvent *>(sipGetAddress(sipSelf))->sipPySelf = SIP_NULLPTR;

    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxWindowCreateEvent(sipGetAddress(sipSelf), sipIsDerivedClass(sipSelf));
    }
}


extern "C" {static void *init_type_wxWindowCreateEvent(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxWindowCreateEvent(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    sipwxWindowCreateEvent *sipCpp = SIP_NULLPTR;

    {
        ::wxWindow* win = 0;

        static const char *sipKwdList[] = {
            sipName_win,
        };

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, sipKwdList, sipUnused, "|J8", sipType_wxWindow, &win))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipwxWindowCreateEvent(win);
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
        const ::wxWindowCreateEvent* a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, "J9", sipType_wxWindowCreateEvent, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipwxWindowCreateEvent(*a0);
            Py_END_ALLOW_THREADS

            sipCpp->sipPySelf = sipSelf;

            return sipCpp;
        }
    }

    return SIP_NULLPTR;
}


/* Define this type's super-types. */
static sipEncodedTypeDef supers_wxWindowCreateEvent[] = {{84, 255, 1}};


static PyMethodDef methods_wxWindowCreateEvent[] = {
    {sipName_Clone, meth_wxWindowCreateEvent_Clone, METH_VARARGS, doc_wxWindowCreateEvent_Clone},
    {sipName_GetWindow, meth_wxWindowCreateEvent_GetWindow, METH_VARARGS, doc_wxWindowCreateEvent_GetWindow}
};

sipVariableDef variables_wxWindowCreateEvent[] = {
    {PropertyVariable, sipName_Window, &methods_wxWindowCreateEvent[1], SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
};

PyDoc_STRVAR(doc_wxWindowCreateEvent, "WindowCreateEvent(win=None) -> None\n"
"\n"
"This event is sent just after the actual window associated with a\n"
"wxWindow object has been created.");


sipClassTypeDef sipTypeDef__core_wxWindowCreateEvent = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_SCC|SIP_TYPE_CLASS,
        sipNameNr_wxWindowCreateEvent,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_WindowCreateEvent,
        {0, 0, 1},
        2, methods_wxWindowCreateEvent,
        0, SIP_NULLPTR,
        1, variables_wxWindowCreateEvent,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxWindowCreateEvent,
    -1,
    -1,
    supers_wxWindowCreateEvent,
    SIP_NULLPTR,
    init_type_wxWindowCreateEvent,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxWindowCreateEvent,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    release_wxWindowCreateEvent,
    cast_wxWindowCreateEvent,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    sizeof (::wxWindowCreateEvent),
};
