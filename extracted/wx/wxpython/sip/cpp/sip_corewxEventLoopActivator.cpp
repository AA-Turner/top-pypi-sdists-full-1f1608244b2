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


/* Call the instance's destructor. */
extern "C" {static void release_wxEventLoopActivator(void *, int);}
static void release_wxEventLoopActivator(void *sipCppV, int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast<::wxEventLoopActivator *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void dealloc_wxEventLoopActivator(sipSimpleWrapper *);}
static void dealloc_wxEventLoopActivator(sipSimpleWrapper *sipSelf)
{
    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxEventLoopActivator(sipGetAddress(sipSelf), 0);
    }
}


extern "C" {static void *init_type_wxEventLoopActivator(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxEventLoopActivator(sipSimpleWrapper *, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    ::wxEventLoopActivator *sipCpp = SIP_NULLPTR;

    {
        ::wxEventLoopBase* loop;

        static const char *sipKwdList[] = {
            sipName_loop,
        };

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, sipKwdList, sipUnused, "J8", sipType_wxEventLoopBase, &loop))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new ::wxEventLoopActivator(loop);
            Py_END_ALLOW_THREADS

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

PyDoc_STRVAR(doc_wxEventLoopActivator, "EventLoopActivator(loop) -> None\n"
"\n"
"Makes an event loop temporarily active.");


sipClassTypeDef sipTypeDef__core_wxEventLoopActivator = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_CLASS,
        sipNameNr_wxEventLoopActivator,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_EventLoopActivator,
        {0, 0, 1},
        0, SIP_NULLPTR,
        0, SIP_NULLPTR,
        0, SIP_NULLPTR,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxEventLoopActivator,
    -1,
    -1,
    SIP_NULLPTR,
    SIP_NULLPTR,
    init_type_wxEventLoopActivator,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxEventLoopActivator,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    release_wxEventLoopActivator,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    sizeof (::wxEventLoopActivator),
};
