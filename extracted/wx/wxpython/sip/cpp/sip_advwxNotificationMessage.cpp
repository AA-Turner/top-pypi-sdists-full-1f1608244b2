/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_adv.h"
        #include <wx/notifmsg.h>
        #include <wx/window.h>
        #include <wx/taskbar.h>
        #include <wx/icon.h>
        #include <wx/event.h>
        #include <wx/eventfilter.h>
        #include <wx/event.h>
        #include <wx/object.h>
        #include <wx/object.h>
        #include <wx/object.h>
    wxTaskBarIcon * _wxNotificationMessage_UseTaskBarIcon(wxTaskBarIcon *icon)
    {
        #ifdef __WXMSW__
            return wxNotificationMessage::UseTaskBarIcon(icon);
        #else
            wxPyRaiseNotImplemented();
            return NULL;
        #endif
    }
    bool _wxNotificationMessage_MSWUseToasts(const wxString *shortcutPath, const wxString *appId)
    {
        #ifdef __WXMSW__
            return wxNotificationMessage::MSWUseToasts(*shortcutPath, *appId);
        #else
            wxPyRaiseNotImplemented();
            return false;
        #endif
    }


class sipwxNotificationMessage : public ::wxNotificationMessage
{
public:
    sipwxNotificationMessage();
    sipwxNotificationMessage(const ::wxString&, const ::wxString&, ::wxWindow*, int);
    virtual ~sipwxNotificationMessage();

    /*
     * There is a public method for every protected method visible from
     * this class.
     */
    bool sipProtectVirt_TryBefore(bool, ::wxEvent&);
    bool sipProtectVirt_TryAfter(bool, ::wxEvent&);

    /*
     * There is a protected method for every virtual method visible from
     * this class.
     */
protected:
    bool ProcessEvent(::wxEvent&) SIP_OVERRIDE;
    bool TryBefore(::wxEvent&) SIP_OVERRIDE;
    bool TryAfter(::wxEvent&) SIP_OVERRIDE;

public:
    sipSimpleWrapper *sipPySelf;

private:
    sipwxNotificationMessage(const sipwxNotificationMessage &);
    sipwxNotificationMessage &operator = (const sipwxNotificationMessage &);

    char sipPyMethods[3];
};

sipwxNotificationMessage::sipwxNotificationMessage(): ::wxNotificationMessage(), sipPySelf(SIP_NULLPTR)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipwxNotificationMessage::sipwxNotificationMessage(const ::wxString& title, const ::wxString& message, ::wxWindow*parent, int flags): ::wxNotificationMessage(title, message, parent, flags), sipPySelf(SIP_NULLPTR)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipwxNotificationMessage::~sipwxNotificationMessage()
{
    sipInstanceDestroyedEx(&sipPySelf);
}

bool sipwxNotificationMessage::ProcessEvent(::wxEvent& event)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[0], &sipPySelf, SIP_NULLPTR, sipName_ProcessEvent);

    if (!sipMeth)
        return ::wxNotificationMessage::ProcessEvent(event);

    extern bool sipVH__adv_13(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxEvent&);

    return sipVH__adv_13(sipGILState, 0, sipPySelf, sipMeth, event);
}

bool sipwxNotificationMessage::TryBefore(::wxEvent& event)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[1], &sipPySelf, SIP_NULLPTR, sipName_TryBefore);

    if (!sipMeth)
        return ::wxNotificationMessage::TryBefore(event);

    extern bool sipVH__adv_13(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxEvent&);

    return sipVH__adv_13(sipGILState, 0, sipPySelf, sipMeth, event);
}

bool sipwxNotificationMessage::TryAfter(::wxEvent& event)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[2], &sipPySelf, SIP_NULLPTR, sipName_TryAfter);

    if (!sipMeth)
        return ::wxNotificationMessage::TryAfter(event);

    extern bool sipVH__adv_13(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxEvent&);

    return sipVH__adv_13(sipGILState, 0, sipPySelf, sipMeth, event);
}

bool sipwxNotificationMessage::sipProtectVirt_TryBefore(bool sipSelfWasArg, ::wxEvent& event)
{
    return (sipSelfWasArg ? ::wxEvtHandler::TryBefore(event) : TryBefore(event));
}

bool sipwxNotificationMessage::sipProtectVirt_TryAfter(bool sipSelfWasArg, ::wxEvent& event)
{
    return (sipSelfWasArg ? ::wxEvtHandler::TryAfter(event) : TryAfter(event));
}


PyDoc_STRVAR(doc_wxNotificationMessage_TryBefore, "TryBefore(event) -> bool\n"
"\n"
"Method called by ProcessEvent() before examining this object event\n"
"tables.");

extern "C" {static PyObject *meth_wxNotificationMessage_TryBefore(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxNotificationMessage_TryBefore(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxEvent* event;
        sipwxNotificationMessage *sipCpp;

        static const char *sipKwdList[] = {
            sipName_event,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ9", &sipSelf, sipType_wxNotificationMessage, &sipCpp, sipType_wxEvent, &event))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->sipProtectVirt_TryBefore(sipSelfWasArg, *event);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_NotificationMessage, sipName_TryBefore, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxNotificationMessage_TryAfter, "TryAfter(event) -> bool\n"
"\n"
"Method called by ProcessEvent() as last resort.");

extern "C" {static PyObject *meth_wxNotificationMessage_TryAfter(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxNotificationMessage_TryAfter(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxEvent* event;
        sipwxNotificationMessage *sipCpp;

        static const char *sipKwdList[] = {
            sipName_event,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ9", &sipSelf, sipType_wxNotificationMessage, &sipCpp, sipType_wxEvent, &event))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->sipProtectVirt_TryAfter(sipSelfWasArg, *event);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_NotificationMessage, sipName_TryAfter, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxNotificationMessage_AddAction, "AddAction(actionid, label=\"\") -> bool\n"
"\n"
"Add an action to the notification.");

extern "C" {static PyObject *meth_wxNotificationMessage_AddAction(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxNotificationMessage_AddAction(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxWindowID actionid;
        const ::wxString& labeldef = wxString();
        const ::wxString* label = &labeldef;
        int labelState = 0;
        ::wxNotificationMessage *sipCpp;

        static const char *sipKwdList[] = {
            sipName_actionid,
            sipName_label,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "Bi|J1", &sipSelf, sipType_wxNotificationMessage, &sipCpp, &actionid, sipType_wxString, &label, &labelState))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->AddAction(actionid, *label);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(label), sipType_wxString, labelState);

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_NotificationMessage, sipName_AddAction, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxNotificationMessage_Close, "Close() -> bool\n"
"\n"
"Hides the notification.");

extern "C" {static PyObject *meth_wxNotificationMessage_Close(PyObject *, PyObject *);}
static PyObject *meth_wxNotificationMessage_Close(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxNotificationMessage *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxNotificationMessage, &sipCpp))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->Close();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_NotificationMessage, sipName_Close, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxNotificationMessage_SetFlags, "SetFlags(flags) -> None\n"
"\n"
"This parameter can be currently used to specify the icon to show in\n"
"the notification.");

extern "C" {static PyObject *meth_wxNotificationMessage_SetFlags(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxNotificationMessage_SetFlags(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        int flags;
        ::wxNotificationMessage *sipCpp;

        static const char *sipKwdList[] = {
            sipName_flags,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "Bi", &sipSelf, sipType_wxNotificationMessage, &sipCpp, &flags))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetFlags(flags);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_NotificationMessage, sipName_SetFlags, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxNotificationMessage_SetIcon, "SetIcon(icon) -> None\n"
"\n"
"Specify a custom icon to be displayed in the notification.");

extern "C" {static PyObject *meth_wxNotificationMessage_SetIcon(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxNotificationMessage_SetIcon(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxIcon* icon;
        ::wxNotificationMessage *sipCpp;

        static const char *sipKwdList[] = {
            sipName_icon,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ9", &sipSelf, sipType_wxNotificationMessage, &sipCpp, sipType_wxIcon, &icon))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetIcon(*icon);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_NotificationMessage, sipName_SetIcon, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxNotificationMessage_SetMessage, "SetMessage(message) -> None\n"
"\n"
"Set the main text of the notification.");

extern "C" {static PyObject *meth_wxNotificationMessage_SetMessage(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxNotificationMessage_SetMessage(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxString* message;
        int messageState = 0;
        ::wxNotificationMessage *sipCpp;

        static const char *sipKwdList[] = {
            sipName_message,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1", &sipSelf, sipType_wxNotificationMessage, &sipCpp, sipType_wxString, &message, &messageState))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetMessage(*message);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(message), sipType_wxString, messageState);

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_NotificationMessage, sipName_SetMessage, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxNotificationMessage_SetParent, "SetParent(parent) -> None\n"
"\n"
"Set the parent for this notification: the notification will be\n"
"associated with the top level parent of this window or, if this method\n"
"is not called, with the main application window by default.");

extern "C" {static PyObject *meth_wxNotificationMessage_SetParent(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxNotificationMessage_SetParent(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxWindow* parent;
        ::wxNotificationMessage *sipCpp;

        static const char *sipKwdList[] = {
            sipName_parent,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ8", &sipSelf, sipType_wxNotificationMessage, &sipCpp, sipType_wxWindow, &parent))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp->SetParent(parent);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_NotificationMessage, sipName_SetParent, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxNotificationMessage_SetTitle, "SetTitle(title) -> None\n"
"\n"
"Set the title, it must be a concise string (not more than 64\n"
"characters), use SetMessage() to give the user more details.");

extern "C" {static PyObject *meth_wxNotificationMessage_SetTitle(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxNotificationMessage_SetTitle(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxString* title;
        int titleState = 0;
        ::wxNotificationMessage *sipCpp;

        static const char *sipKwdList[] = {
            sipName_title,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1", &sipSelf, sipType_wxNotificationMessage, &sipCpp, sipType_wxString, &title, &titleState))
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

    sipNoMethod(sipParseErr, sipName_NotificationMessage, sipName_SetTitle, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxNotificationMessage_Show, "Show(timeout=Timeout_Auto) -> bool\n"
"\n"
"Show the notification to the user and hides it after timeout seconds are elapsed.");

extern "C" {static PyObject *meth_wxNotificationMessage_Show(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxNotificationMessage_Show(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        int timeout = ::wxNotificationMessage::Timeout_Auto;
        ::wxNotificationMessage *sipCpp;

        static const char *sipKwdList[] = {
            sipName_timeout,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "B|i", &sipSelf, sipType_wxNotificationMessage, &sipCpp, &timeout))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->Show(timeout);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_NotificationMessage, sipName_Show, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxNotificationMessage_UseTaskBarIcon, "UseTaskBarIcon(icon) -> TaskBarIcon\n"
"\n"
"If the application already uses a wxTaskBarIcon, it should be\n"
"connected to notifications by using this method.");

extern "C" {static PyObject *meth_wxNotificationMessage_UseTaskBarIcon(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxNotificationMessage_UseTaskBarIcon(PyObject *, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxTaskBarIcon* icon;

        static const char *sipKwdList[] = {
            sipName_icon,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "J8", sipType_wxTaskBarIcon, &icon))
        {
            ::wxTaskBarIcon*sipRes = 0;
            int sipIsErr = 0;
        PyErr_Clear();
        Py_BEGIN_ALLOW_THREADS
        sipRes = _wxNotificationMessage_UseTaskBarIcon(icon);
        Py_END_ALLOW_THREADS
        if (PyErr_Occurred()) sipIsErr = 1;

            if (sipIsErr)
                return 0;

            return sipConvertFromType(sipRes, sipType_wxTaskBarIcon, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_NotificationMessage, sipName_UseTaskBarIcon, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxNotificationMessage_MSWUseToasts, "MSWUseToasts(shortcutPath=\"\", appId=\"\") -> bool\n"
"\n"
"Enables toast notifications available since Windows 8 and suppresses\n"
"the additional icon in the notification area on Windows 10.");

extern "C" {static PyObject *meth_wxNotificationMessage_MSWUseToasts(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxNotificationMessage_MSWUseToasts(PyObject *, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxString& shortcutPathdef = wxString();
        const ::wxString* shortcutPath = &shortcutPathdef;
        int shortcutPathState = 0;
        const ::wxString& appIddef = wxString();
        const ::wxString* appId = &appIddef;
        int appIdState = 0;

        static const char *sipKwdList[] = {
            sipName_shortcutPath,
            sipName_appId,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "|J1J1", sipType_wxString, &shortcutPath, &shortcutPathState, sipType_wxString, &appId, &appIdState))
        {
            bool sipRes = 0;
            int sipIsErr = 0;
        PyErr_Clear();
        Py_BEGIN_ALLOW_THREADS
        sipRes = _wxNotificationMessage_MSWUseToasts(shortcutPath, appId);
        Py_END_ALLOW_THREADS
        if (PyErr_Occurred()) sipIsErr = 1;
            sipReleaseType(const_cast<::wxString *>(shortcutPath), sipType_wxString, shortcutPathState);
            sipReleaseType(const_cast<::wxString *>(appId), sipType_wxString, appIdState);

            if (sipIsErr)
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_NotificationMessage, sipName_MSWUseToasts, SIP_NULLPTR);

    return SIP_NULLPTR;
}


/* Cast a pointer to a type somewhere in its inheritance hierarchy. */
extern "C" {static void *cast_wxNotificationMessage(void *, const sipTypeDef *);}
static void *cast_wxNotificationMessage(void *sipCppV, const sipTypeDef *targetType)
{
    ::wxNotificationMessage *sipCpp = reinterpret_cast<::wxNotificationMessage *>(sipCppV);

    if (targetType == sipType_wxNotificationMessage)
        return sipCppV;

    sipCppV = ((const sipClassTypeDef *)sipType_wxEvtHandler)->ctd_cast(static_cast<::wxEvtHandler *>(sipCpp), targetType);
    if (sipCppV)
        return sipCppV;

    return SIP_NULLPTR;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxNotificationMessage(void *, int);}
static void release_wxNotificationMessage(void *sipCppV, int sipState)
{
    Py_BEGIN_ALLOW_THREADS

    if (sipState & SIP_DERIVED_CLASS)
        delete reinterpret_cast<sipwxNotificationMessage *>(sipCppV);
    else
        delete reinterpret_cast<::wxNotificationMessage *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void *array_wxNotificationMessage(Py_ssize_t);}
static void *array_wxNotificationMessage(Py_ssize_t sipNrElem)
{
    return new ::wxNotificationMessage[sipNrElem];
}


extern "C" {static void array_delete_wxNotificationMessage(void *);}
static void array_delete_wxNotificationMessage(void *sipCpp)
{
    delete[] reinterpret_cast<::wxNotificationMessage *>(sipCpp);
}


extern "C" {static void dealloc_wxNotificationMessage(sipSimpleWrapper *);}
static void dealloc_wxNotificationMessage(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerivedClass(sipSelf))
        reinterpret_cast<sipwxNotificationMessage *>(sipGetAddress(sipSelf))->sipPySelf = SIP_NULLPTR;

    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxNotificationMessage(sipGetAddress(sipSelf), sipIsDerivedClass(sipSelf));
    }
}


extern "C" {static void *init_type_wxNotificationMessage(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxNotificationMessage(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    sipwxNotificationMessage *sipCpp = SIP_NULLPTR;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, ""))
        {
        if (!wxPyCheckForApp()) return NULL;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipwxNotificationMessage();
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
        const ::wxString* title;
        int titleState = 0;
        const ::wxString& messagedef = wxEmptyString;
        const ::wxString* message = &messagedef;
        int messageState = 0;
        ::wxWindow* parent = 0;
        int flags = wxICON_INFORMATION;

        static const char *sipKwdList[] = {
            sipName_title,
            sipName_message,
            sipName_parent,
            sipName_flags,
        };

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, sipKwdList, sipUnused, "J1|J1J8i", sipType_wxString, &title, &titleState, sipType_wxString, &message, &messageState, sipType_wxWindow, &parent, &flags))
        {
        if (!wxPyCheckForApp()) return NULL;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipwxNotificationMessage(*title, *message, parent, flags);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(title), sipType_wxString, titleState);
            sipReleaseType(const_cast<::wxString *>(message), sipType_wxString, messageState);

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
static sipEncodedTypeDef supers_wxNotificationMessage[] = {{23, 0, 1}};


static PyMethodDef methods_wxNotificationMessage[] = {
    {sipName_AddAction, SIP_MLMETH_CAST(meth_wxNotificationMessage_AddAction), METH_VARARGS|METH_KEYWORDS, doc_wxNotificationMessage_AddAction},
    {sipName_Close, meth_wxNotificationMessage_Close, METH_VARARGS, doc_wxNotificationMessage_Close},
    {sipName_MSWUseToasts, SIP_MLMETH_CAST(meth_wxNotificationMessage_MSWUseToasts), METH_VARARGS|METH_KEYWORDS, doc_wxNotificationMessage_MSWUseToasts},
    {sipName_SetFlags, SIP_MLMETH_CAST(meth_wxNotificationMessage_SetFlags), METH_VARARGS|METH_KEYWORDS, doc_wxNotificationMessage_SetFlags},
    {sipName_SetIcon, SIP_MLMETH_CAST(meth_wxNotificationMessage_SetIcon), METH_VARARGS|METH_KEYWORDS, doc_wxNotificationMessage_SetIcon},
    {sipName_SetMessage, SIP_MLMETH_CAST(meth_wxNotificationMessage_SetMessage), METH_VARARGS|METH_KEYWORDS, doc_wxNotificationMessage_SetMessage},
    {sipName_SetParent, SIP_MLMETH_CAST(meth_wxNotificationMessage_SetParent), METH_VARARGS|METH_KEYWORDS, doc_wxNotificationMessage_SetParent},
    {sipName_SetTitle, SIP_MLMETH_CAST(meth_wxNotificationMessage_SetTitle), METH_VARARGS|METH_KEYWORDS, doc_wxNotificationMessage_SetTitle},
    {sipName_Show, SIP_MLMETH_CAST(meth_wxNotificationMessage_Show), METH_VARARGS|METH_KEYWORDS, doc_wxNotificationMessage_Show},
    {sipName_TryAfter, SIP_MLMETH_CAST(meth_wxNotificationMessage_TryAfter), METH_VARARGS|METH_KEYWORDS, SIP_NULLPTR},
    {sipName_TryBefore, SIP_MLMETH_CAST(meth_wxNotificationMessage_TryBefore), METH_VARARGS|METH_KEYWORDS, SIP_NULLPTR},
    {sipName_UseTaskBarIcon, SIP_MLMETH_CAST(meth_wxNotificationMessage_UseTaskBarIcon), METH_VARARGS|METH_KEYWORDS, doc_wxNotificationMessage_UseTaskBarIcon}
};

static sipEnumMemberDef enummembers_wxNotificationMessage[] = {
    {sipName_Timeout_Auto, static_cast<int>(::wxNotificationMessage::Timeout_Auto), -1},
    {sipName_Timeout_Never, static_cast<int>(::wxNotificationMessage::Timeout_Never), -1},
};

PyDoc_STRVAR(doc_wxNotificationMessage, "NotificationMessage() -> None\n"
"NotificationMessage(title, message='', parent=None, flags=wx.ICON_INFORMATION) -> None\n"
"\n"
"This class allows showing the user a message non intrusively.");


sipClassTypeDef sipTypeDef__adv_wxNotificationMessage = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_SCC|SIP_TYPE_CLASS,
        sipNameNr_wxNotificationMessage,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_NotificationMessage,
        {0, 0, 1},
        12, methods_wxNotificationMessage,
        2, enummembers_wxNotificationMessage,
        0, SIP_NULLPTR,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxNotificationMessage,
    -1,
    -1,
    supers_wxNotificationMessage,
    SIP_NULLPTR,
    init_type_wxNotificationMessage,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxNotificationMessage,
    SIP_NULLPTR,
    array_wxNotificationMessage,
    SIP_NULLPTR,
    release_wxNotificationMessage,
    cast_wxNotificationMessage,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    array_delete_wxNotificationMessage,
    sizeof (::wxNotificationMessage),
};
