/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_propgrid.h"
        #include <wx/propgrid/editors.h>
        #include <wx/propgrid/editors.h>
        #include <wx/propgrid/propgrid.h>
        #include <wx/propgrid/property.h>
        #include <wx/gdicmn.h>
        #include <wx/gdicmn.h>
        #include <wx/window.h>
        #include <wx/event.h>
        #include <wx/propgrid/property.h>
        #include <wx/dc.h>
        #include <wx/gdicmn.h>
        #include <wx/object.h>
        #include <wx/object.h>
        #include <wx/object.h>


class sipwxPGChoiceAndButtonEditor : public ::wxPGChoiceAndButtonEditor
{
public:
    sipwxPGChoiceAndButtonEditor();
    sipwxPGChoiceAndButtonEditor(const ::wxPGChoiceAndButtonEditor&);
    virtual ~sipwxPGChoiceAndButtonEditor();

    /*
     * There is a protected method for every virtual method visible from
     * this class.
     */
protected:
    bool CanContainCustomImage() const SIP_OVERRIDE;
    void OnFocus(::wxPGProperty*, ::wxWindow*) const SIP_OVERRIDE;
    void DeleteItem(::wxWindow*, int) const SIP_OVERRIDE;
    int InsertItem(::wxWindow*, const ::wxString&, int) const SIP_OVERRIDE;
    void SetControlIntValue(::wxPGProperty*, ::wxWindow*, int) const SIP_OVERRIDE;
    void SetControlStringValue(::wxPGProperty*, ::wxWindow*, const ::wxString&) const SIP_OVERRIDE;
    void SetControlAppearance(::wxPropertyGrid*, ::wxPGProperty*, ::wxWindow*, const ::wxPGCell&, const ::wxPGCell&, bool) const SIP_OVERRIDE;
    void SetValueToUnspecified(::wxPGProperty*, ::wxWindow*) const SIP_OVERRIDE;
    bool OnEvent(::wxPropertyGrid*, ::wxPGProperty*, ::wxWindow*, ::wxEvent&) const SIP_OVERRIDE;
    void DrawValue(::wxDC&, const ::wxRect&, ::wxPGProperty*, const ::wxString&) const SIP_OVERRIDE;
    void UpdateControl(::wxPGProperty*, ::wxWindow*) const SIP_OVERRIDE;
    ::wxPGWindowList CreateControls(::wxPropertyGrid*, ::wxPGProperty*, const ::wxPoint&, const ::wxSize&) const SIP_OVERRIDE;
    ::wxString GetName() const SIP_OVERRIDE;
    bool GetValueFromControl(::wxPGVariant&, ::wxPGProperty*, ::wxWindow*) const SIP_OVERRIDE;

public:
    sipSimpleWrapper *sipPySelf;

private:
    sipwxPGChoiceAndButtonEditor(const sipwxPGChoiceAndButtonEditor &);
    sipwxPGChoiceAndButtonEditor &operator = (const sipwxPGChoiceAndButtonEditor &);

    char sipPyMethods[14];
};

sipwxPGChoiceAndButtonEditor::sipwxPGChoiceAndButtonEditor(): ::wxPGChoiceAndButtonEditor(), sipPySelf(SIP_NULLPTR)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipwxPGChoiceAndButtonEditor::sipwxPGChoiceAndButtonEditor(const ::wxPGChoiceAndButtonEditor& a0): ::wxPGChoiceAndButtonEditor(a0), sipPySelf(SIP_NULLPTR)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipwxPGChoiceAndButtonEditor::~sipwxPGChoiceAndButtonEditor()
{
    sipInstanceDestroyedEx(&sipPySelf);
}

bool sipwxPGChoiceAndButtonEditor::CanContainCustomImage() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[0]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_CanContainCustomImage);

    if (!sipMeth)
        return ::wxPGChoiceAndButtonEditor::CanContainCustomImage();

    extern bool sipVH__propgrid_33(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__propgrid_33(sipGILState, 0, sipPySelf, sipMeth);
}

void sipwxPGChoiceAndButtonEditor::OnFocus(::wxPGProperty*property, ::wxWindow*wnd) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[1]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_OnFocus);

    if (!sipMeth)
    {
        ::wxPGChoiceAndButtonEditor::OnFocus(property, wnd);
        return;
    }

    extern void sipVH__propgrid_24(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxPGProperty*, ::wxWindow*);

    sipVH__propgrid_24(sipGILState, 0, sipPySelf, sipMeth, property, wnd);
}

void sipwxPGChoiceAndButtonEditor::DeleteItem(::wxWindow*ctrl, int index) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[2]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_DeleteItem);

    if (!sipMeth)
    {
        ::wxPGChoiceAndButtonEditor::DeleteItem(ctrl, index);
        return;
    }

    extern void sipVH__propgrid_32(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxWindow*, int);

    sipVH__propgrid_32(sipGILState, 0, sipPySelf, sipMeth, ctrl, index);
}

int sipwxPGChoiceAndButtonEditor::InsertItem(::wxWindow*ctrl, const ::wxString& label, int index) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[3]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_InsertItem);

    if (!sipMeth)
        return ::wxPGChoiceAndButtonEditor::InsertItem(ctrl, label, index);

    extern int sipVH__propgrid_31(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxWindow*, const ::wxString&, int);

    return sipVH__propgrid_31(sipGILState, 0, sipPySelf, sipMeth, ctrl, label, index);
}

void sipwxPGChoiceAndButtonEditor::SetControlIntValue(::wxPGProperty*property, ::wxWindow*ctrl, int value) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[4]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_SetControlIntValue);

    if (!sipMeth)
    {
        ::wxPGChoiceAndButtonEditor::SetControlIntValue(property, ctrl, value);
        return;
    }

    extern void sipVH__propgrid_30(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxPGProperty*, ::wxWindow*, int);

    sipVH__propgrid_30(sipGILState, 0, sipPySelf, sipMeth, property, ctrl, value);
}

void sipwxPGChoiceAndButtonEditor::SetControlStringValue(::wxPGProperty*property, ::wxWindow*ctrl, const ::wxString& txt) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[5]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_SetControlStringValue);

    if (!sipMeth)
    {
        ::wxPGChoiceAndButtonEditor::SetControlStringValue(property, ctrl, txt);
        return;
    }

    extern void sipVH__propgrid_29(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxPGProperty*, ::wxWindow*, const ::wxString&);

    sipVH__propgrid_29(sipGILState, 0, sipPySelf, sipMeth, property, ctrl, txt);
}

void sipwxPGChoiceAndButtonEditor::SetControlAppearance(::wxPropertyGrid*pg, ::wxPGProperty*property, ::wxWindow*ctrl, const ::wxPGCell& appearance, const ::wxPGCell& oldAppearance, bool unspecified) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[6]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_SetControlAppearance);

    if (!sipMeth)
    {
        ::wxPGChoiceAndButtonEditor::SetControlAppearance(pg, property, ctrl, appearance, oldAppearance, unspecified);
        return;
    }

    extern void sipVH__propgrid_28(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxPropertyGrid*, ::wxPGProperty*, ::wxWindow*, const ::wxPGCell&, const ::wxPGCell&, bool);

    sipVH__propgrid_28(sipGILState, 0, sipPySelf, sipMeth, pg, property, ctrl, appearance, oldAppearance, unspecified);
}

void sipwxPGChoiceAndButtonEditor::SetValueToUnspecified(::wxPGProperty*property, ::wxWindow*ctrl) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[7]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_SetValueToUnspecified);

    if (!sipMeth)
    {
        ::wxPGChoiceAndButtonEditor::SetValueToUnspecified(property, ctrl);
        return;
    }

    extern void sipVH__propgrid_24(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxPGProperty*, ::wxWindow*);

    sipVH__propgrid_24(sipGILState, 0, sipPySelf, sipMeth, property, ctrl);
}

bool sipwxPGChoiceAndButtonEditor::OnEvent(::wxPropertyGrid*propgrid, ::wxPGProperty*property, ::wxWindow*wnd_primary, ::wxEvent& event) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[8]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_OnEvent);

    if (!sipMeth)
        return ::wxPGChoiceAndButtonEditor::OnEvent(propgrid, property, wnd_primary, event);

    extern bool sipVH__propgrid_26(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxPropertyGrid*, ::wxPGProperty*, ::wxWindow*, ::wxEvent&);

    return sipVH__propgrid_26(sipGILState, 0, sipPySelf, sipMeth, propgrid, property, wnd_primary, event);
}

void sipwxPGChoiceAndButtonEditor::DrawValue(::wxDC& dc, const ::wxRect& rect, ::wxPGProperty*property, const ::wxString& text) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[9]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_DrawValue);

    if (!sipMeth)
    {
        ::wxPGChoiceAndButtonEditor::DrawValue(dc, rect, property, text);
        return;
    }

    extern void sipVH__propgrid_25(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxDC&, const ::wxRect&, ::wxPGProperty*, const ::wxString&);

    sipVH__propgrid_25(sipGILState, 0, sipPySelf, sipMeth, dc, rect, property, text);
}

void sipwxPGChoiceAndButtonEditor::UpdateControl(::wxPGProperty*property, ::wxWindow*ctrl) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[10]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_UpdateControl);

    if (!sipMeth)
    {
        ::wxPGChoiceAndButtonEditor::UpdateControl(property, ctrl);
        return;
    }

    extern void sipVH__propgrid_24(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxPGProperty*, ::wxWindow*);

    sipVH__propgrid_24(sipGILState, 0, sipPySelf, sipMeth, property, ctrl);
}

::wxPGWindowList sipwxPGChoiceAndButtonEditor::CreateControls(::wxPropertyGrid*propgrid, ::wxPGProperty*property, const ::wxPoint& pos, const ::wxSize& size) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[11]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_CreateControls);

    if (!sipMeth)
        return ::wxPGChoiceAndButtonEditor::CreateControls(propgrid, property, pos, size);

    extern ::wxPGWindowList sipVH__propgrid_23(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxPropertyGrid*, ::wxPGProperty*, const ::wxPoint&, const ::wxSize&);

    return sipVH__propgrid_23(sipGILState, 0, sipPySelf, sipMeth, propgrid, property, pos, size);
}

::wxString sipwxPGChoiceAndButtonEditor::GetName() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[12]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_GetName);

    if (!sipMeth)
        return ::wxPGChoiceAndButtonEditor::GetName();

    extern ::wxString sipVH__propgrid_22(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__propgrid_22(sipGILState, 0, sipPySelf, sipMeth);
}

bool sipwxPGChoiceAndButtonEditor::GetValueFromControl(::wxPGVariant& variant, ::wxPGProperty*property, ::wxWindow*ctrl) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[13]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_GetValueFromControl);

    if (!sipMeth)
        return ::wxPGChoiceAndButtonEditor::GetValueFromControl(variant, property, ctrl);

    extern bool sipVH__propgrid_34(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxPGVariant&, ::wxPGProperty*, ::wxWindow*);

    return sipVH__propgrid_34(sipGILState, 0, sipPySelf, sipMeth, variant, property, ctrl);
}


PyDoc_STRVAR(doc_wxPGChoiceAndButtonEditor_GetName, "GetName() -> str\n"
"\n"
"Returns pointer to the name of the editor.");

extern "C" {static PyObject *meth_wxPGChoiceAndButtonEditor_GetName(PyObject *, PyObject *);}
static PyObject *meth_wxPGChoiceAndButtonEditor_GetName(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const ::wxPGChoiceAndButtonEditor *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxPGChoiceAndButtonEditor, &sipCpp))
        {
            ::wxString*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxString((sipSelfWasArg ? sipCpp->::wxPGChoiceAndButtonEditor::GetName() : sipCpp->GetName()));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxString, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoiceAndButtonEditor, sipName_GetName, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxPGChoiceAndButtonEditor_CreateControls, "CreateControls(propgrid, property, pos, size) -> PGWindowList\n"
"\n"
"Instantiates editor controls.");

extern "C" {static PyObject *meth_wxPGChoiceAndButtonEditor_CreateControls(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxPGChoiceAndButtonEditor_CreateControls(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxPropertyGrid* propgrid;
        ::wxPGProperty* property;
        const ::wxPoint* pos;
        int posState = 0;
        const ::wxSize* size;
        int sizeState = 0;
        const ::wxPGChoiceAndButtonEditor *sipCpp;

        static const char *sipKwdList[] = {
            sipName_propgrid,
            sipName_property,
            sipName_pos,
            sipName_size,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ8J8J1J1", &sipSelf, sipType_wxPGChoiceAndButtonEditor, &sipCpp, sipType_wxPropertyGrid, &propgrid, sipType_wxPGProperty, &property, sipType_wxPoint, &pos, &posState, sipType_wxSize, &size, &sizeState))
        {
            ::wxPGWindowList*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxPGWindowList((sipSelfWasArg ? sipCpp->::wxPGChoiceAndButtonEditor::CreateControls(propgrid, property, *pos, *size) : sipCpp->CreateControls(propgrid, property, *pos, *size)));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxPoint *>(pos), sipType_wxPoint, posState);
            sipReleaseType(const_cast<::wxSize *>(size), sipType_wxSize, sizeState);

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxPGWindowList, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_PGChoiceAndButtonEditor, sipName_CreateControls, SIP_NULLPTR);

    return SIP_NULLPTR;
}


/* Cast a pointer to a type somewhere in its inheritance hierarchy. */
extern "C" {static void *cast_wxPGChoiceAndButtonEditor(void *, const sipTypeDef *);}
static void *cast_wxPGChoiceAndButtonEditor(void *sipCppV, const sipTypeDef *targetType)
{
    ::wxPGChoiceAndButtonEditor *sipCpp = reinterpret_cast<::wxPGChoiceAndButtonEditor *>(sipCppV);

    if (targetType == sipType_wxPGChoiceAndButtonEditor)
        return sipCppV;

    sipCppV = ((const sipClassTypeDef *)sipType_wxPGChoiceEditor)->ctd_cast(static_cast<::wxPGChoiceEditor *>(sipCpp), targetType);
    if (sipCppV)
        return sipCppV;

    return SIP_NULLPTR;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxPGChoiceAndButtonEditor(void *, int);}
static void release_wxPGChoiceAndButtonEditor(void *sipCppV, int sipState)
{
    Py_BEGIN_ALLOW_THREADS

    if (sipState & SIP_DERIVED_CLASS)
        delete reinterpret_cast<sipwxPGChoiceAndButtonEditor *>(sipCppV);
    else
        delete reinterpret_cast<::wxPGChoiceAndButtonEditor *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void *array_wxPGChoiceAndButtonEditor(Py_ssize_t);}
static void *array_wxPGChoiceAndButtonEditor(Py_ssize_t sipNrElem)
{
    return new ::wxPGChoiceAndButtonEditor[sipNrElem];
}


extern "C" {static void array_delete_wxPGChoiceAndButtonEditor(void *);}
static void array_delete_wxPGChoiceAndButtonEditor(void *sipCpp)
{
    delete[] reinterpret_cast<::wxPGChoiceAndButtonEditor *>(sipCpp);
}


extern "C" {static void assign_wxPGChoiceAndButtonEditor(void *, Py_ssize_t, void *);}
static void assign_wxPGChoiceAndButtonEditor(void *sipDst, Py_ssize_t sipDstIdx, void *sipSrc)
{
    reinterpret_cast<::wxPGChoiceAndButtonEditor *>(sipDst)[sipDstIdx] = *reinterpret_cast<::wxPGChoiceAndButtonEditor *>(sipSrc);
}


extern "C" {static void *copy_wxPGChoiceAndButtonEditor(const void *, Py_ssize_t);}
static void *copy_wxPGChoiceAndButtonEditor(const void *sipSrc, Py_ssize_t sipSrcIdx)
{
    return new ::wxPGChoiceAndButtonEditor(reinterpret_cast<const ::wxPGChoiceAndButtonEditor *>(sipSrc)[sipSrcIdx]);
}


extern "C" {static void dealloc_wxPGChoiceAndButtonEditor(sipSimpleWrapper *);}
static void dealloc_wxPGChoiceAndButtonEditor(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerivedClass(sipSelf))
        reinterpret_cast<sipwxPGChoiceAndButtonEditor *>(sipGetAddress(sipSelf))->sipPySelf = SIP_NULLPTR;

    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxPGChoiceAndButtonEditor(sipGetAddress(sipSelf), sipIsDerivedClass(sipSelf));
    }
}


extern "C" {static void *init_type_wxPGChoiceAndButtonEditor(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxPGChoiceAndButtonEditor(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    sipwxPGChoiceAndButtonEditor *sipCpp = SIP_NULLPTR;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, ""))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipwxPGChoiceAndButtonEditor();
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
        const ::wxPGChoiceAndButtonEditor* a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, "J9", sipType_wxPGChoiceAndButtonEditor, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipwxPGChoiceAndButtonEditor(*a0);
            Py_END_ALLOW_THREADS

            sipCpp->sipPySelf = sipSelf;

            return sipCpp;
        }
    }

    return SIP_NULLPTR;
}


/* Define this type's super-types. */
static sipEncodedTypeDef supers_wxPGChoiceAndButtonEditor[] = {{31, 255, 1}};


static PyMethodDef methods_wxPGChoiceAndButtonEditor[] = {
    {sipName_CreateControls, SIP_MLMETH_CAST(meth_wxPGChoiceAndButtonEditor_CreateControls), METH_VARARGS|METH_KEYWORDS, doc_wxPGChoiceAndButtonEditor_CreateControls},
    {sipName_GetName, meth_wxPGChoiceAndButtonEditor_GetName, METH_VARARGS, doc_wxPGChoiceAndButtonEditor_GetName}
};

sipVariableDef variables_wxPGChoiceAndButtonEditor[] = {
    {PropertyVariable, sipName_Name, &methods_wxPGChoiceAndButtonEditor[1], SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
};

PyDoc_STRVAR(doc_wxPGChoiceAndButtonEditor, "PGChoiceAndButtonEditor() -> None");


sipClassTypeDef sipTypeDef__propgrid_wxPGChoiceAndButtonEditor = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_SCC|SIP_TYPE_CLASS,
        sipNameNr_wxPGChoiceAndButtonEditor,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_PGChoiceAndButtonEditor,
        {0, 0, 1},
        2, methods_wxPGChoiceAndButtonEditor,
        0, SIP_NULLPTR,
        1, variables_wxPGChoiceAndButtonEditor,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxPGChoiceAndButtonEditor,
    -1,
    -1,
    supers_wxPGChoiceAndButtonEditor,
    SIP_NULLPTR,
    init_type_wxPGChoiceAndButtonEditor,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxPGChoiceAndButtonEditor,
    assign_wxPGChoiceAndButtonEditor,
    array_wxPGChoiceAndButtonEditor,
    copy_wxPGChoiceAndButtonEditor,
    release_wxPGChoiceAndButtonEditor,
    cast_wxPGChoiceAndButtonEditor,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    array_delete_wxPGChoiceAndButtonEditor,
    sizeof (::wxPGChoiceAndButtonEditor),
};
