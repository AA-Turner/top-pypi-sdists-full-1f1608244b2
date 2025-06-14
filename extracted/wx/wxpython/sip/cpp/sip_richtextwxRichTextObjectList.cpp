/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_richtext.h"
        #include <wx/richtext/richtextbuffer.h>
        
        
        class wxRichTextObjectList_iterator {
        public:
            wxRichTextObjectList_iterator(wxRichTextObjectList::compatibility_iterator start)
                : m_node(start) {}

            wxRichTextObject* __next__() {
                wxRichTextObject* obj = NULL;
                if (m_node) {
                    obj = (wxRichTextObject*) m_node->GetData();
                    m_node = m_node->GetNext();
                }
                else {
                    PyErr_SetString(PyExc_StopIteration, "");
                }
                return (wxRichTextObject*)obj;
            }
        private:
            wxRichTextObjectList::compatibility_iterator m_node;
        };


PyDoc_STRVAR(doc_wxRichTextObjectList_index, "index(self, obj: Optional[RichTextObject]) -> int");

extern "C" {static PyObject *meth_wxRichTextObjectList_index(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxRichTextObjectList_index(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxRichTextObject* obj;
        ::wxRichTextObjectList *sipCpp;

        static const char *sipKwdList[] = {
            sipName_obj,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ8", &sipSelf, sipType_wxRichTextObjectList, &sipCpp, sipType_wxRichTextObject, &obj))
        {
            int sipRes = 0;
            sipErrorState sipError = sipErrorNone;
        int idx = sipCpp->IndexOf((wxRichTextObject*)obj);
        if (idx == wxNOT_FOUND) {
            sipError = sipErrorFail;
            wxPyErr_SetString(PyExc_ValueError,
                              "sequence.index(x): x not in sequence");
        }
        sipRes = idx;

            if (sipError == sipErrorFail)
                return 0;

            if (sipError == sipErrorNone)
            {
            return PyLong_FromLong(sipRes);
            }

            sipAddException(sipError, &sipParseErr);
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextObjectList, sipName_index, doc_wxRichTextObjectList_index);

    return SIP_NULLPTR;
}


extern "C" {static PyObject *slot_wxRichTextObjectList___iter__(PyObject *);}
static PyObject *slot_wxRichTextObjectList___iter__(PyObject *sipSelf)
{
    ::wxRichTextObjectList *sipCpp = reinterpret_cast<::wxRichTextObjectList *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf, sipType_wxRichTextObjectList));

    if (!sipCpp)
        return SIP_NULLPTR;


    {
        {
            ::wxRichTextObjectList_iterator*sipRes = 0;
        sipRes =  new wxRichTextObjectList_iterator(sipCpp->GetFirst());

            return sipConvertFromNewType(sipRes, sipType_wxRichTextObjectList_iterator, SIP_NULLPTR);
        }
    }

    return 0;
}


extern "C" {static int slot_wxRichTextObjectList___contains__(PyObject *, PyObject *);}
static int slot_wxRichTextObjectList___contains__(PyObject *sipSelf, PyObject *sipArg)
{
    ::wxRichTextObjectList *sipCpp = reinterpret_cast<::wxRichTextObjectList *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf, sipType_wxRichTextObjectList));

    if (!sipCpp)
        return -1;

    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxRichTextObject* obj;

        if (sipParseArgs(&sipParseErr, sipArg, "1J8", sipType_wxRichTextObject, &obj))
        {
            int sipRes = 0;
        wxRichTextObjectList::compatibility_iterator node;
        node = sipCpp->Find((wxRichTextObject*)obj);
        sipRes = node != NULL;

            return sipRes;
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextObjectList, sipName___contains__, SIP_NULLPTR);

    return -1;
}


extern "C" {static PyObject *slot_wxRichTextObjectList___getitem__(PyObject *, PyObject *);}
static PyObject *slot_wxRichTextObjectList___getitem__(PyObject *sipSelf, PyObject *sipArg)
{
    ::wxRichTextObjectList *sipCpp = reinterpret_cast<::wxRichTextObjectList *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf, sipType_wxRichTextObjectList));

    if (!sipCpp)
        return SIP_NULLPTR;

    PyObject *sipParseErr = SIP_NULLPTR;

    {
        long index;

        if (sipParseArgs(&sipParseErr, sipArg, "1l", &index))
        {
            ::wxRichTextObject*sipRes = 0;
            sipErrorState sipError = sipErrorNone;
        if (0 > index)
            index += sipCpp->size();

        if (index < sipCpp->size() && (0 <= index)) {
            wxRichTextObjectList::compatibility_iterator node = sipCpp->Item(index);
            if (node)
                sipRes = (wxRichTextObject*)node->GetData();
        }
        else {
            wxPyErr_SetString(PyExc_IndexError, "sequence index out of range");
            sipError = sipErrorFail;
        }

            if (sipError == sipErrorFail)
                return 0;

            if (sipError == sipErrorNone)
            {
            return sipConvertFromType(sipRes, sipType_wxRichTextObject, SIP_NULLPTR);
            }

            sipAddException(sipError, &sipParseErr);
        }
    }

    sipNoMethod(sipParseErr, sipName_RichTextObjectList, sipName___getitem__, SIP_NULLPTR);

    return SIP_NULLPTR;
}


extern "C" {static Py_ssize_t slot_wxRichTextObjectList___len__(PyObject *);}
static Py_ssize_t slot_wxRichTextObjectList___len__(PyObject *sipSelf)
{
    ::wxRichTextObjectList *sipCpp = reinterpret_cast<::wxRichTextObjectList *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf, sipType_wxRichTextObjectList));

    if (!sipCpp)
        return 0;


    {
        {
            Py_ssize_t sipRes = 0;
        sipRes = sipCpp->size();

            return sipRes;
        }
    }

    return 0;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxRichTextObjectList(void *, int);}
static void release_wxRichTextObjectList(void *sipCppV, int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast<::wxRichTextObjectList *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void *array_wxRichTextObjectList(Py_ssize_t);}
static void *array_wxRichTextObjectList(Py_ssize_t sipNrElem)
{
    return new ::wxRichTextObjectList[sipNrElem];
}


extern "C" {static void array_delete_wxRichTextObjectList(void *);}
static void array_delete_wxRichTextObjectList(void *sipCpp)
{
    delete[] reinterpret_cast<::wxRichTextObjectList *>(sipCpp);
}


extern "C" {static void assign_wxRichTextObjectList(void *, Py_ssize_t, void *);}
static void assign_wxRichTextObjectList(void *sipDst, Py_ssize_t sipDstIdx, void *sipSrc)
{
    reinterpret_cast<::wxRichTextObjectList *>(sipDst)[sipDstIdx] = *reinterpret_cast<::wxRichTextObjectList *>(sipSrc);
}


extern "C" {static void *copy_wxRichTextObjectList(const void *, Py_ssize_t);}
static void *copy_wxRichTextObjectList(const void *sipSrc, Py_ssize_t sipSrcIdx)
{
    return new ::wxRichTextObjectList(reinterpret_cast<const ::wxRichTextObjectList *>(sipSrc)[sipSrcIdx]);
}


extern "C" {static void dealloc_wxRichTextObjectList(sipSimpleWrapper *);}
static void dealloc_wxRichTextObjectList(sipSimpleWrapper *sipSelf)
{
    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxRichTextObjectList(sipGetAddress(sipSelf), 0);
    }
}


extern "C" {static void *init_type_wxRichTextObjectList(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxRichTextObjectList(sipSimpleWrapper *, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    ::wxRichTextObjectList *sipCpp = SIP_NULLPTR;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, ""))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new ::wxRichTextObjectList();
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    {
        const ::wxRichTextObjectList* a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, "J9", sipType_wxRichTextObjectList, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new ::wxRichTextObjectList(*a0);
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    return SIP_NULLPTR;
}


/* Define this type's Python slots. */
static sipPySlotDef slots_wxRichTextObjectList[] = {
    {(void *)slot_wxRichTextObjectList___iter__, iter_slot},
    {(void *)slot_wxRichTextObjectList___contains__, contains_slot},
    {(void *)slot_wxRichTextObjectList___getitem__, getitem_slot},
    {(void *)slot_wxRichTextObjectList___len__, len_slot},
    {0, (sipPySlotType)0}
};


static PyMethodDef methods_wxRichTextObjectList[] = {
    {sipName_index, SIP_MLMETH_CAST(meth_wxRichTextObjectList_index), METH_VARARGS|METH_KEYWORDS, doc_wxRichTextObjectList_index}
};

PyDoc_STRVAR(doc_wxRichTextObjectList, "\1RichTextObjectList()\n"
"RichTextObjectList(a0: RichTextObjectList)");


sipClassTypeDef sipTypeDef__richtext_wxRichTextObjectList = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_CLASS,
        sipNameNr_wxRichTextObjectList,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_RichTextObjectList,
        {0, 0, 1},
        1, methods_wxRichTextObjectList,
        0, SIP_NULLPTR,
        0, SIP_NULLPTR,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxRichTextObjectList,
    -1,
    -1,
    SIP_NULLPTR,
    slots_wxRichTextObjectList,
    init_type_wxRichTextObjectList,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxRichTextObjectList,
    assign_wxRichTextObjectList,
    array_wxRichTextObjectList,
    copy_wxRichTextObjectList,
    release_wxRichTextObjectList,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    array_delete_wxRichTextObjectList,
    sizeof (::wxRichTextObjectList),
};
