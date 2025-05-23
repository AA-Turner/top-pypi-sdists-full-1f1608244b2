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
        #include <wx/gdicmn.h>
        #include <wx/event.h>
        #include <wx/gdicmn.h>
        #include <wx/object.h>
        #include <wx/object.h>
        #include <wx/object.h>


class sipwxSizeEvent : public ::wxSizeEvent
{
public:
    sipwxSizeEvent(const ::wxSize&, int);
    sipwxSizeEvent(const ::wxSizeEvent&);
    virtual ~sipwxSizeEvent();

    /*
     * There is a protected method for every virtual method visible from
     * this class.
     */
protected:
    ::wxEvent* Clone() const SIP_OVERRIDE;
    ::wxEventCategory GetEventCategory() const SIP_OVERRIDE;

public:
    sipSimpleWrapper *sipPySelf;

private:
    sipwxSizeEvent(const sipwxSizeEvent &);
    sipwxSizeEvent &operator = (const sipwxSizeEvent &);

    char sipPyMethods[2];
};

sipwxSizeEvent::sipwxSizeEvent(const ::wxSize& sz, int id): ::wxSizeEvent(sz, id), sipPySelf(SIP_NULLPTR)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipwxSizeEvent::sipwxSizeEvent(const ::wxSizeEvent& a0): ::wxSizeEvent(a0), sipPySelf(SIP_NULLPTR)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipwxSizeEvent::~sipwxSizeEvent()
{
    sipInstanceDestroyedEx(&sipPySelf);
}

::wxEvent* sipwxSizeEvent::Clone() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[0]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_Clone);

    if (!sipMeth)
        return ::wxSizeEvent::Clone();

    extern ::wxEvent* sipVH__core_103(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__core_103(sipGILState, 0, sipPySelf, sipMeth);
}

::wxEventCategory sipwxSizeEvent::GetEventCategory() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[1]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_GetEventCategory);

    if (!sipMeth)
        return ::wxSizeEvent::GetEventCategory();

    extern ::wxEventCategory sipVH__core_104(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__core_104(sipGILState, 0, sipPySelf, sipMeth);
}


PyDoc_STRVAR(doc_wxSizeEvent_GetSize, "GetSize() -> Size\n"
"\n"
"Returns the entire size of the window generating the size change\n"
"event.");

extern "C" {static PyObject *meth_wxSizeEvent_GetSize(PyObject *, PyObject *);}
static PyObject *meth_wxSizeEvent_GetSize(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxSizeEvent *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxSizeEvent, &sipCpp))
        {
            ::wxSize*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxSize(sipCpp->GetSize());
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxSize, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_SizeEvent, sipName_GetSize, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxSizeEvent_SetSize, "SetSize(size) -> None");

extern "C" {static PyObject *meth_wxSizeEvent_SetSize(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxSizeEvent_SetSize(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxSize* size;
        int sizeState = 0;
        ::wxSizeEvent *sipCpp;

        static const char *sipKwdList[] = {
            sipName_size,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1", &sipSelf, sipType_wxSizeEvent, &sipCpp, sipType_wxSize, &size, &sizeState))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetSize(*size);
            Py_END_ALLOW_THREADS
            sipReleaseType(size, sipType_wxSize, sizeState);

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_SizeEvent, sipName_SetSize, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxSizeEvent_GetRect, "GetRect() -> Rect");

extern "C" {static PyObject *meth_wxSizeEvent_GetRect(PyObject *, PyObject *);}
static PyObject *meth_wxSizeEvent_GetRect(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxSizeEvent *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxSizeEvent, &sipCpp))
        {
            ::wxRect*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxRect(sipCpp->GetRect());
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxRect, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_SizeEvent, sipName_GetRect, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxSizeEvent_SetRect, "SetRect(rect) -> None");

extern "C" {static PyObject *meth_wxSizeEvent_SetRect(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxSizeEvent_SetRect(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxRect* rect;
        int rectState = 0;
        ::wxSizeEvent *sipCpp;

        static const char *sipKwdList[] = {
            sipName_rect,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1", &sipSelf, sipType_wxSizeEvent, &sipCpp, sipType_wxRect, &rect, &rectState))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetRect(*rect);
            Py_END_ALLOW_THREADS
            sipReleaseType(rect, sipType_wxRect, rectState);

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_SizeEvent, sipName_SetRect, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxSizeEvent_Clone, "Clone(self) -> Optional[Event]");

extern "C" {static PyObject *meth_wxSizeEvent_Clone(PyObject *, PyObject *);}
static PyObject *meth_wxSizeEvent_Clone(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const ::wxSizeEvent *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxSizeEvent, &sipCpp))
        {
            ::wxEvent*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxSizeEvent::Clone() : sipCpp->Clone());
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxEvent, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_SizeEvent, sipName_Clone, doc_wxSizeEvent_Clone);

    return SIP_NULLPTR;
}


/* Cast a pointer to a type somewhere in its inheritance hierarchy. */
extern "C" {static void *cast_wxSizeEvent(void *, const sipTypeDef *);}
static void *cast_wxSizeEvent(void *sipCppV, const sipTypeDef *targetType)
{
    ::wxSizeEvent *sipCpp = reinterpret_cast<::wxSizeEvent *>(sipCppV);

    if (targetType == sipType_wxSizeEvent)
        return sipCppV;

    sipCppV = ((const sipClassTypeDef *)sipType_wxEvent)->ctd_cast(static_cast<::wxEvent *>(sipCpp), targetType);
    if (sipCppV)
        return sipCppV;

    return SIP_NULLPTR;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxSizeEvent(void *, int);}
static void release_wxSizeEvent(void *sipCppV, int sipState)
{
    Py_BEGIN_ALLOW_THREADS

    if (sipState & SIP_DERIVED_CLASS)
        delete reinterpret_cast<sipwxSizeEvent *>(sipCppV);
    else
        delete reinterpret_cast<::wxSizeEvent *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void dealloc_wxSizeEvent(sipSimpleWrapper *);}
static void dealloc_wxSizeEvent(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerivedClass(sipSelf))
        reinterpret_cast<sipwxSizeEvent *>(sipGetAddress(sipSelf))->sipPySelf = SIP_NULLPTR;

    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxSizeEvent(sipGetAddress(sipSelf), sipIsDerivedClass(sipSelf));
    }
}


extern "C" {static void *init_type_wxSizeEvent(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxSizeEvent(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    sipwxSizeEvent *sipCpp = SIP_NULLPTR;

    {
        const ::wxSize* sz;
        int szState = 0;
        int id = 0;

        static const char *sipKwdList[] = {
            sipName_sz,
            sipName_id,
        };

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, sipKwdList, sipUnused, "J1|i", sipType_wxSize, &sz, &szState, &id))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipwxSizeEvent(*sz, id);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxSize *>(sz), sipType_wxSize, szState);

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
        const ::wxSizeEvent* a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, "J9", sipType_wxSizeEvent, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipwxSizeEvent(*a0);
            Py_END_ALLOW_THREADS

            sipCpp->sipPySelf = sipSelf;

            return sipCpp;
        }
    }

    return SIP_NULLPTR;
}


/* Define this type's super-types. */
static sipEncodedTypeDef supers_wxSizeEvent[] = {{151, 255, 1}};


static PyMethodDef methods_wxSizeEvent[] = {
    {sipName_Clone, meth_wxSizeEvent_Clone, METH_VARARGS, doc_wxSizeEvent_Clone},
    {sipName_GetRect, meth_wxSizeEvent_GetRect, METH_VARARGS, doc_wxSizeEvent_GetRect},
    {sipName_GetSize, meth_wxSizeEvent_GetSize, METH_VARARGS, doc_wxSizeEvent_GetSize},
    {sipName_SetRect, SIP_MLMETH_CAST(meth_wxSizeEvent_SetRect), METH_VARARGS|METH_KEYWORDS, doc_wxSizeEvent_SetRect},
    {sipName_SetSize, SIP_MLMETH_CAST(meth_wxSizeEvent_SetSize), METH_VARARGS|METH_KEYWORDS, doc_wxSizeEvent_SetSize}
};

sipVariableDef variables_wxSizeEvent[] = {
    {PropertyVariable, sipName_Size, &methods_wxSizeEvent[2], &methods_wxSizeEvent[4], SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_Rect, &methods_wxSizeEvent[1], &methods_wxSizeEvent[3], SIP_NULLPTR, SIP_NULLPTR},
};

PyDoc_STRVAR(doc_wxSizeEvent, "SizeEvent(sz, id=0) -> None\n"
"\n"
"A size event holds information about size change events of wxWindow.");


sipClassTypeDef sipTypeDef__core_wxSizeEvent = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_SCC|SIP_TYPE_CLASS,
        sipNameNr_wxSizeEvent,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_SizeEvent,
        {0, 0, 1},
        5, methods_wxSizeEvent,
        0, SIP_NULLPTR,
        2, variables_wxSizeEvent,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxSizeEvent,
    -1,
    -1,
    supers_wxSizeEvent,
    SIP_NULLPTR,
    init_type_wxSizeEvent,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxSizeEvent,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    release_wxSizeEvent,
    cast_wxSizeEvent,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    sizeof (::wxSizeEvent),
};
