/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_dataview.h"
        #include <wx/treelist.h>
        #include <wx/treelist.h>
        #include <wx/treelist.h>


class sipwxTreeListItemComparator : public ::wxTreeListItemComparator
{
public:
    sipwxTreeListItemComparator();
    virtual ~sipwxTreeListItemComparator();

    /*
     * There is a protected method for every virtual method visible from
     * this class.
     */
protected:
    int Compare(::wxTreeListCtrl*, uint, ::wxTreeListItem, ::wxTreeListItem) SIP_OVERRIDE;

public:
    sipSimpleWrapper *sipPySelf;

private:
    sipwxTreeListItemComparator(const sipwxTreeListItemComparator &);
    sipwxTreeListItemComparator &operator = (const sipwxTreeListItemComparator &);

    char sipPyMethods[1];
};

sipwxTreeListItemComparator::sipwxTreeListItemComparator(): ::wxTreeListItemComparator(), sipPySelf(SIP_NULLPTR)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipwxTreeListItemComparator::~sipwxTreeListItemComparator()
{
    sipInstanceDestroyedEx(&sipPySelf);
}

int sipwxTreeListItemComparator::Compare(::wxTreeListCtrl*treelist, uint column, ::wxTreeListItem first, ::wxTreeListItem second)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[0], &sipPySelf, sipName_TreeListItemComparator, sipName_Compare);

    if (!sipMeth)
        return 0;

    extern int sipVH__dataview_62(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxTreeListCtrl*, uint, ::wxTreeListItem, ::wxTreeListItem);

    return sipVH__dataview_62(sipGILState, 0, sipPySelf, sipMeth, treelist, column, first, second);
}


PyDoc_STRVAR(doc_wxTreeListItemComparator_Compare, "Compare(treelist, column, first, second) -> int\n"
"\n"
"Pure virtual function which must be overridden to define sort order.");

extern "C" {static PyObject *meth_wxTreeListItemComparator_Compare(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxTreeListItemComparator_Compare(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    PyObject *sipOrigSelf = sipSelf;

    {
        ::wxTreeListCtrl* treelist;
        uint column;
        ::wxTreeListItem* first;
        ::wxTreeListItem* second;
        ::wxTreeListItemComparator *sipCpp;

        static const char *sipKwdList[] = {
            sipName_treelist,
            sipName_column,
            sipName_first,
            sipName_second,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ8uJ9J9", &sipSelf, sipType_wxTreeListItemComparator, &sipCpp, sipType_wxTreeListCtrl, &treelist, &column, sipType_wxTreeListItem, &first, sipType_wxTreeListItem, &second))
        {
            int sipRes;

            if (!sipOrigSelf)
            {
                sipAbstractMethod(sipName_TreeListItemComparator, sipName_Compare);
                return SIP_NULLPTR;
            }

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->Compare(treelist, column, *first, *second);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyLong_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_TreeListItemComparator, sipName_Compare, SIP_NULLPTR);

    return SIP_NULLPTR;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxTreeListItemComparator(void *, int);}
static void release_wxTreeListItemComparator(void *sipCppV, int sipState)
{
    Py_BEGIN_ALLOW_THREADS

    if (sipState & SIP_DERIVED_CLASS)
        delete reinterpret_cast<sipwxTreeListItemComparator *>(sipCppV);
    else
        delete reinterpret_cast<::wxTreeListItemComparator *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void dealloc_wxTreeListItemComparator(sipSimpleWrapper *);}
static void dealloc_wxTreeListItemComparator(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerivedClass(sipSelf))
        reinterpret_cast<sipwxTreeListItemComparator *>(sipGetAddress(sipSelf))->sipPySelf = SIP_NULLPTR;

    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxTreeListItemComparator(sipGetAddress(sipSelf), sipIsDerivedClass(sipSelf));
    }
}


extern "C" {static void *init_type_wxTreeListItemComparator(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxTreeListItemComparator(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    sipwxTreeListItemComparator *sipCpp = SIP_NULLPTR;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, ""))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipwxTreeListItemComparator();
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


static PyMethodDef methods_wxTreeListItemComparator[] = {
    {sipName_Compare, SIP_MLMETH_CAST(meth_wxTreeListItemComparator_Compare), METH_VARARGS|METH_KEYWORDS, doc_wxTreeListItemComparator_Compare}
};

PyDoc_STRVAR(doc_wxTreeListItemComparator, "TreeListItemComparator() -> None\n"
"\n"
"Class defining sort order for the items in wxTreeListCtrl.");


sipClassTypeDef sipTypeDef__dataview_wxTreeListItemComparator = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_ABSTRACT|SIP_TYPE_CLASS,
        sipNameNr_wxTreeListItemComparator,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_TreeListItemComparator,
        {0, 0, 1},
        1, methods_wxTreeListItemComparator,
        0, SIP_NULLPTR,
        0, SIP_NULLPTR,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxTreeListItemComparator,
    -1,
    -1,
    SIP_NULLPTR,
    SIP_NULLPTR,
    init_type_wxTreeListItemComparator,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxTreeListItemComparator,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    release_wxTreeListItemComparator,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    sizeof (::wxTreeListItemComparator),
};
