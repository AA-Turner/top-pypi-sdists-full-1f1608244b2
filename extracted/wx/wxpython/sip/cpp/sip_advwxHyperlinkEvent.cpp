/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_adv.h"
        #include <wx/hyperlink.h>
        #include <wx/object.h>
        #include <wx/event.h>
        #include <wx/object.h>
        #include <wx/object.h>


class sipwxHyperlinkEvent : public ::wxHyperlinkEvent
{
public:
    sipwxHyperlinkEvent(::wxObject*, int, const ::wxString&);
    sipwxHyperlinkEvent(const ::wxHyperlinkEvent&);
    virtual ~sipwxHyperlinkEvent();

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
    sipwxHyperlinkEvent(const sipwxHyperlinkEvent &);
    sipwxHyperlinkEvent &operator = (const sipwxHyperlinkEvent &);

    char sipPyMethods[2];
};

sipwxHyperlinkEvent::sipwxHyperlinkEvent(::wxObject*generator, int id, const ::wxString& url): ::wxHyperlinkEvent(generator, id, url), sipPySelf(SIP_NULLPTR)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipwxHyperlinkEvent::sipwxHyperlinkEvent(const ::wxHyperlinkEvent& a0): ::wxHyperlinkEvent(a0), sipPySelf(SIP_NULLPTR)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipwxHyperlinkEvent::~sipwxHyperlinkEvent()
{
    sipInstanceDestroyedEx(&sipPySelf);
}

::wxEventCategory sipwxHyperlinkEvent::GetEventCategory() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[0]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_GetEventCategory);

    if (!sipMeth)
        return ::wxHyperlinkEvent::GetEventCategory();

    extern ::wxEventCategory sipVH__adv_28(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__adv_28(sipGILState, 0, sipPySelf, sipMeth);
}

::wxEvent* sipwxHyperlinkEvent::Clone() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[1]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_Clone);

    if (!sipMeth)
        return ::wxHyperlinkEvent::Clone();

    extern ::wxEvent* sipVH__adv_27(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__adv_27(sipGILState, 0, sipPySelf, sipMeth);
}


PyDoc_STRVAR(doc_wxHyperlinkEvent_GetURL, "GetURL() -> str\n"
"\n"
"Returns the URL of the hyperlink where the user has just clicked.");

extern "C" {static PyObject *meth_wxHyperlinkEvent_GetURL(PyObject *, PyObject *);}
static PyObject *meth_wxHyperlinkEvent_GetURL(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxHyperlinkEvent *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxHyperlinkEvent, &sipCpp))
        {
            ::wxString*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxString(sipCpp->GetURL());
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxString, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_HyperlinkEvent, sipName_GetURL, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxHyperlinkEvent_SetURL, "SetURL(url) -> None\n"
"\n"
"Sets the URL associated with the event.");

extern "C" {static PyObject *meth_wxHyperlinkEvent_SetURL(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxHyperlinkEvent_SetURL(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxString* url;
        int urlState = 0;
        ::wxHyperlinkEvent *sipCpp;

        static const char *sipKwdList[] = {
            sipName_url,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1", &sipSelf, sipType_wxHyperlinkEvent, &sipCpp, sipType_wxString, &url, &urlState))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetURL(*url);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(url), sipType_wxString, urlState);

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_HyperlinkEvent, sipName_SetURL, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxHyperlinkEvent_Clone, "Clone(self) -> Optional[Event]");

extern "C" {static PyObject *meth_wxHyperlinkEvent_Clone(PyObject *, PyObject *);}
static PyObject *meth_wxHyperlinkEvent_Clone(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const ::wxHyperlinkEvent *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxHyperlinkEvent, &sipCpp))
        {
            ::wxEvent*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxHyperlinkEvent::Clone() : sipCpp->Clone());
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxEvent, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_HyperlinkEvent, sipName_Clone, doc_wxHyperlinkEvent_Clone);

    return SIP_NULLPTR;
}


/* Cast a pointer to a type somewhere in its inheritance hierarchy. */
extern "C" {static void *cast_wxHyperlinkEvent(void *, const sipTypeDef *);}
static void *cast_wxHyperlinkEvent(void *sipCppV, const sipTypeDef *targetType)
{
    ::wxHyperlinkEvent *sipCpp = reinterpret_cast<::wxHyperlinkEvent *>(sipCppV);

    if (targetType == sipType_wxHyperlinkEvent)
        return sipCppV;

    sipCppV = ((const sipClassTypeDef *)sipType_wxCommandEvent)->ctd_cast(static_cast<::wxCommandEvent *>(sipCpp), targetType);
    if (sipCppV)
        return sipCppV;

    return SIP_NULLPTR;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxHyperlinkEvent(void *, int);}
static void release_wxHyperlinkEvent(void *sipCppV, int sipState)
{
    Py_BEGIN_ALLOW_THREADS

    if (sipState & SIP_DERIVED_CLASS)
        delete reinterpret_cast<sipwxHyperlinkEvent *>(sipCppV);
    else
        delete reinterpret_cast<::wxHyperlinkEvent *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void dealloc_wxHyperlinkEvent(sipSimpleWrapper *);}
static void dealloc_wxHyperlinkEvent(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerivedClass(sipSelf))
        reinterpret_cast<sipwxHyperlinkEvent *>(sipGetAddress(sipSelf))->sipPySelf = SIP_NULLPTR;

    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxHyperlinkEvent(sipGetAddress(sipSelf), sipIsDerivedClass(sipSelf));
    }
}


extern "C" {static void *init_type_wxHyperlinkEvent(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxHyperlinkEvent(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    sipwxHyperlinkEvent *sipCpp = SIP_NULLPTR;

    {
        ::wxObject* generator;
        int id;
        const ::wxString* url;
        int urlState = 0;

        static const char *sipKwdList[] = {
            sipName_generator,
            sipName_id,
            sipName_url,
        };

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, sipKwdList, sipUnused, "J8iJ1", sipType_wxObject, &generator, &id, sipType_wxString, &url, &urlState))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipwxHyperlinkEvent(generator, id, *url);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(url), sipType_wxString, urlState);

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
        const ::wxHyperlinkEvent* a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, "J9", sipType_wxHyperlinkEvent, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipwxHyperlinkEvent(*a0);
            Py_END_ALLOW_THREADS

            sipCpp->sipPySelf = sipSelf;

            return sipCpp;
        }
    }

    return SIP_NULLPTR;
}


/* Define this type's super-types. */
static sipEncodedTypeDef supers_wxHyperlinkEvent[] = {{14, 0, 1}};


static PyMethodDef methods_wxHyperlinkEvent[] = {
    {sipName_Clone, meth_wxHyperlinkEvent_Clone, METH_VARARGS, doc_wxHyperlinkEvent_Clone},
    {sipName_GetURL, meth_wxHyperlinkEvent_GetURL, METH_VARARGS, doc_wxHyperlinkEvent_GetURL},
    {sipName_SetURL, SIP_MLMETH_CAST(meth_wxHyperlinkEvent_SetURL), METH_VARARGS|METH_KEYWORDS, doc_wxHyperlinkEvent_SetURL}
};

sipVariableDef variables_wxHyperlinkEvent[] = {
    {PropertyVariable, sipName_URL, &methods_wxHyperlinkEvent[1], &methods_wxHyperlinkEvent[2], SIP_NULLPTR, SIP_NULLPTR},
};

PyDoc_STRVAR(doc_wxHyperlinkEvent, "HyperlinkEvent(generator, id, url) -> None\n"
"\n"
"This event class is used for the events generated by wxHyperlinkCtrl.");


sipClassTypeDef sipTypeDef__adv_wxHyperlinkEvent = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_SCC|SIP_TYPE_CLASS,
        sipNameNr_wxHyperlinkEvent,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_HyperlinkEvent,
        {0, 0, 1},
        3, methods_wxHyperlinkEvent,
        0, SIP_NULLPTR,
        1, variables_wxHyperlinkEvent,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxHyperlinkEvent,
    -1,
    -1,
    supers_wxHyperlinkEvent,
    SIP_NULLPTR,
    init_type_wxHyperlinkEvent,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxHyperlinkEvent,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    release_wxHyperlinkEvent,
    cast_wxHyperlinkEvent,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    sizeof (::wxHyperlinkEvent),
};
