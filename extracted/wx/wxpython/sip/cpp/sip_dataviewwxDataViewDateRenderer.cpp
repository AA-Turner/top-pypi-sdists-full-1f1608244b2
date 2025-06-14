/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_dataview.h"
        #include <wx/dataview.h>
        #include <wx/dataview.h>
        #include <wx/window.h>
        #include <wx/dataview.h>
        #include <wx/gdicmn.h>
        #include <wx/dataview.h>
        #include <wx/dataview.h>
        #include <wx/object.h>
        #include <wx/object.h>
        #include <wx/object.h>


class sipwxDataViewDateRenderer : public ::wxDataViewDateRenderer
{
public:
    sipwxDataViewDateRenderer(const ::wxString&, ::wxDataViewCellMode, int);
    virtual ~sipwxDataViewDateRenderer();

    /*
     * There is a public method for every protected method visible from
     * this class.
     */
    ::wxDataViewCtrl* sipProtect_GetView() const;

    /*
     * There is a protected method for every virtual method visible from
     * this class.
     */
protected:
    int GetAlignment() const SIP_OVERRIDE;
    ::wxDataViewCellMode GetMode() const SIP_OVERRIDE;
    bool GetValue(::wxVariant&) const SIP_OVERRIDE;
    bool IsCompatibleVariantType(const ::wxString&) const SIP_OVERRIDE;
    void SetAlignment(int) SIP_OVERRIDE;
    bool SetValue(const ::wxVariant&) SIP_OVERRIDE;
    bool Validate(::wxDVCVariant&) SIP_OVERRIDE;
    bool HasEditorCtrl() const SIP_OVERRIDE;
    ::wxWindow* CreateEditorCtrl(::wxWindow*, ::wxRect, const ::wxVariant&) SIP_OVERRIDE;
    bool GetValueFromEditorCtrl(::wxWindow*, ::wxVariant&) SIP_OVERRIDE;
    bool StartEditing(const ::wxDataViewItem&, ::wxRect) SIP_OVERRIDE;
    void CancelEditing() SIP_OVERRIDE;
    bool FinishEditing() SIP_OVERRIDE;

public:
    sipSimpleWrapper *sipPySelf;

private:
    sipwxDataViewDateRenderer(const sipwxDataViewDateRenderer &);
    sipwxDataViewDateRenderer &operator = (const sipwxDataViewDateRenderer &);

    char sipPyMethods[13];
};

sipwxDataViewDateRenderer::sipwxDataViewDateRenderer(const ::wxString& varianttype, ::wxDataViewCellMode mode, int align): ::wxDataViewDateRenderer(varianttype, mode, align), sipPySelf(SIP_NULLPTR)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipwxDataViewDateRenderer::~sipwxDataViewDateRenderer()
{
    sipInstanceDestroyedEx(&sipPySelf);
}

int sipwxDataViewDateRenderer::GetAlignment() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[0]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_GetAlignment);

    if (!sipMeth)
        return ::wxDataViewDateRenderer::GetAlignment();

    extern int sipVH__dataview_20(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__dataview_20(sipGILState, 0, sipPySelf, sipMeth);
}

::wxDataViewCellMode sipwxDataViewDateRenderer::GetMode() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[1]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_GetMode);

    if (!sipMeth)
        return ::wxDataViewDateRenderer::GetMode();

    extern ::wxDataViewCellMode sipVH__dataview_21(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__dataview_21(sipGILState, 0, sipPySelf, sipMeth);
}

bool sipwxDataViewDateRenderer::GetValue(::wxVariant& value) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[2]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_GetValue);

    if (!sipMeth)
        return ::wxDataViewDateRenderer::GetValue(value);

    extern bool sipVH__dataview_22(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxVariant&);

    return sipVH__dataview_22(sipGILState, 0, sipPySelf, sipMeth, value);
}

bool sipwxDataViewDateRenderer::IsCompatibleVariantType(const ::wxString& variantType) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[3]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_IsCompatibleVariantType);

    if (!sipMeth)
        return ::wxDataViewDateRenderer::IsCompatibleVariantType(variantType);

    extern bool sipVH__dataview_23(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, const ::wxString&);

    return sipVH__dataview_23(sipGILState, 0, sipPySelf, sipMeth, variantType);
}

void sipwxDataViewDateRenderer::SetAlignment(int align)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[4], &sipPySelf, SIP_NULLPTR, sipName_SetAlignment);

    if (!sipMeth)
    {
        ::wxDataViewDateRenderer::SetAlignment(align);
        return;
    }

    extern void sipVH__dataview_24(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, int);

    sipVH__dataview_24(sipGILState, 0, sipPySelf, sipMeth, align);
}

bool sipwxDataViewDateRenderer::SetValue(const ::wxVariant& value)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[5], &sipPySelf, SIP_NULLPTR, sipName_SetValue);

    if (!sipMeth)
        return ::wxDataViewDateRenderer::SetValue(value);

    extern bool sipVH__dataview_25(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, const ::wxVariant&);

    return sipVH__dataview_25(sipGILState, 0, sipPySelf, sipMeth, value);
}

bool sipwxDataViewDateRenderer::Validate(::wxDVCVariant& value)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[6], &sipPySelf, SIP_NULLPTR, sipName_Validate);

    if (!sipMeth)
        return ::wxDataViewDateRenderer::Validate(value);

    extern bool sipVH__dataview_26(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxDVCVariant&);

    return sipVH__dataview_26(sipGILState, 0, sipPySelf, sipMeth, value);
}

bool sipwxDataViewDateRenderer::HasEditorCtrl() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[7]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_HasEditorCtrl);

    if (!sipMeth)
        return ::wxDataViewDateRenderer::HasEditorCtrl();

    extern bool sipVH__dataview_0(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__dataview_0(sipGILState, 0, sipPySelf, sipMeth);
}

::wxWindow* sipwxDataViewDateRenderer::CreateEditorCtrl(::wxWindow*parent, ::wxRect labelRect, const ::wxVariant& value)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[8], &sipPySelf, SIP_NULLPTR, sipName_CreateEditorCtrl);

    if (!sipMeth)
        return ::wxDataViewDateRenderer::CreateEditorCtrl(parent, labelRect, value);

    extern ::wxWindow* sipVH__dataview_27(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxWindow*, ::wxRect, const ::wxVariant&);

    return sipVH__dataview_27(sipGILState, 0, sipPySelf, sipMeth, parent, labelRect, value);
}

bool sipwxDataViewDateRenderer::GetValueFromEditorCtrl(::wxWindow*editor, ::wxVariant& value)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[9], &sipPySelf, SIP_NULLPTR, sipName_GetValueFromEditorCtrl);

    if (!sipMeth)
        return ::wxDataViewDateRenderer::GetValueFromEditorCtrl(editor, value);

    extern bool sipVH__dataview_28(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxWindow*, ::wxVariant&);

    return sipVH__dataview_28(sipGILState, 0, sipPySelf, sipMeth, editor, value);
}

bool sipwxDataViewDateRenderer::StartEditing(const ::wxDataViewItem& item, ::wxRect labelRect)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[10], &sipPySelf, SIP_NULLPTR, sipName_StartEditing);

    if (!sipMeth)
        return ::wxDataViewDateRenderer::StartEditing(item, labelRect);

    extern bool sipVH__dataview_29(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, const ::wxDataViewItem&, ::wxRect);

    return sipVH__dataview_29(sipGILState, 0, sipPySelf, sipMeth, item, labelRect);
}

void sipwxDataViewDateRenderer::CancelEditing()
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[11], &sipPySelf, SIP_NULLPTR, sipName_CancelEditing);

    if (!sipMeth)
    {
        ::wxDataViewDateRenderer::CancelEditing();
        return;
    }

    extern void sipVH__dataview_5(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    sipVH__dataview_5(sipGILState, 0, sipPySelf, sipMeth);
}

bool sipwxDataViewDateRenderer::FinishEditing()
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[12], &sipPySelf, SIP_NULLPTR, sipName_FinishEditing);

    if (!sipMeth)
        return ::wxDataViewDateRenderer::FinishEditing();

    extern bool sipVH__dataview_0(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__dataview_0(sipGILState, 0, sipPySelf, sipMeth);
}

::wxDataViewCtrl* sipwxDataViewDateRenderer::sipProtect_GetView() const
{
    return ::wxDataViewRenderer::GetView();
}


PyDoc_STRVAR(doc_wxDataViewDateRenderer_GetView, "GetView() -> DataViewCtrl");

extern "C" {static PyObject *meth_wxDataViewDateRenderer_GetView(PyObject *, PyObject *);}
static PyObject *meth_wxDataViewDateRenderer_GetView(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const sipwxDataViewDateRenderer *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxDataViewDateRenderer, &sipCpp))
        {
            ::wxDataViewCtrl*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->sipProtect_GetView();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxDataViewCtrl, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_DataViewDateRenderer, sipName_GetView, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxDataViewDateRenderer_GetDefaultType, "GetDefaultType() -> str\n"
"\n"
"Returns the wxVariant type used with this renderer.");

extern "C" {static PyObject *meth_wxDataViewDateRenderer_GetDefaultType(PyObject *, PyObject *);}
static PyObject *meth_wxDataViewDateRenderer_GetDefaultType(PyObject *, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        if (sipParseArgs(&sipParseErr, sipArgs, ""))
        {
            ::wxString*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxString(::wxDataViewDateRenderer::GetDefaultType());
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxString, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_DataViewDateRenderer, sipName_GetDefaultType, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxDataViewDateRenderer_SetValue, "SetValue(self, value: Optional[Any]) -> bool");

extern "C" {static PyObject *meth_wxDataViewDateRenderer_SetValue(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxDataViewDateRenderer_SetValue(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const ::wxDVCVariant* value;
        int valueState = 0;
        ::wxDataViewDateRenderer *sipCpp;

        static const char *sipKwdList[] = {
            sipName_value,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1", &sipSelf, sipType_wxDataViewDateRenderer, &sipCpp, sipType_wxDVCVariant, &value, &valueState))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxDataViewDateRenderer::SetValue(*value) : sipCpp->SetValue(*value));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxDVCVariant *>(value), sipType_wxDVCVariant, valueState);

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_DataViewDateRenderer, sipName_SetValue, doc_wxDataViewDateRenderer_SetValue);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxDataViewDateRenderer_GetValue, "GetValue(self) -> Optional[Any]");

extern "C" {static PyObject *meth_wxDataViewDateRenderer_GetValue(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxDataViewDateRenderer_GetValue(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxDVCVariant* value;
        const ::wxDataViewDateRenderer *sipCpp;

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, SIP_NULLPTR, "B", &sipSelf, sipType_wxDataViewDateRenderer, &sipCpp))
        {
            value = new ::wxDVCVariant();

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            (sipSelfWasArg ? sipCpp->::wxDataViewDateRenderer::GetValue(*value) : sipCpp->GetValue(*value));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(value, sipType_wxDVCVariant, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_DataViewDateRenderer, sipName_GetValue, doc_wxDataViewDateRenderer_GetValue);

    return SIP_NULLPTR;
}


/* Cast a pointer to a type somewhere in its inheritance hierarchy. */
extern "C" {static void *cast_wxDataViewDateRenderer(void *, const sipTypeDef *);}
static void *cast_wxDataViewDateRenderer(void *sipCppV, const sipTypeDef *targetType)
{
    ::wxDataViewDateRenderer *sipCpp = reinterpret_cast<::wxDataViewDateRenderer *>(sipCppV);

    if (targetType == sipType_wxDataViewDateRenderer)
        return sipCppV;

    sipCppV = ((const sipClassTypeDef *)sipType_wxDataViewRenderer)->ctd_cast(static_cast<::wxDataViewRenderer *>(sipCpp), targetType);
    if (sipCppV)
        return sipCppV;

    return SIP_NULLPTR;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxDataViewDateRenderer(void *, int);}
static void release_wxDataViewDateRenderer(void *sipCppV, int sipState)
{
    Py_BEGIN_ALLOW_THREADS

    if (sipState & SIP_DERIVED_CLASS)
        delete reinterpret_cast<sipwxDataViewDateRenderer *>(sipCppV);
    else
        delete reinterpret_cast<::wxDataViewDateRenderer *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void *array_wxDataViewDateRenderer(Py_ssize_t);}
static void *array_wxDataViewDateRenderer(Py_ssize_t sipNrElem)
{
    return new ::wxDataViewDateRenderer[sipNrElem];
}


extern "C" {static void array_delete_wxDataViewDateRenderer(void *);}
static void array_delete_wxDataViewDateRenderer(void *sipCpp)
{
    delete[] reinterpret_cast<::wxDataViewDateRenderer *>(sipCpp);
}


extern "C" {static void dealloc_wxDataViewDateRenderer(sipSimpleWrapper *);}
static void dealloc_wxDataViewDateRenderer(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerivedClass(sipSelf))
        reinterpret_cast<sipwxDataViewDateRenderer *>(sipGetAddress(sipSelf))->sipPySelf = SIP_NULLPTR;

    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxDataViewDateRenderer(sipGetAddress(sipSelf), sipIsDerivedClass(sipSelf));
    }
}


extern "C" {static void *init_type_wxDataViewDateRenderer(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxDataViewDateRenderer(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    sipwxDataViewDateRenderer *sipCpp = SIP_NULLPTR;

    {
        const ::wxString& varianttypedef = wxDataViewDateRenderer::GetDefaultType();
        const ::wxString* varianttype = &varianttypedef;
        int varianttypeState = 0;
        ::wxDataViewCellMode mode = wxDATAVIEW_CELL_ACTIVATABLE;
        int align = wxDVR_DEFAULT_ALIGNMENT;

        static const char *sipKwdList[] = {
            sipName_varianttype,
            sipName_mode,
            sipName_align,
        };

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, sipKwdList, sipUnused, "|J1Ei", sipType_wxString, &varianttype, &varianttypeState, sipType_wxDataViewCellMode, &mode, &align))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipwxDataViewDateRenderer(*varianttype, mode, align);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(varianttype), sipType_wxString, varianttypeState);

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
static sipEncodedTypeDef supers_wxDataViewDateRenderer[] = {{25, 255, 1}};


static PyMethodDef methods_wxDataViewDateRenderer[] = {
    {sipName_GetDefaultType, meth_wxDataViewDateRenderer_GetDefaultType, METH_VARARGS, doc_wxDataViewDateRenderer_GetDefaultType},
    {sipName_GetValue, SIP_MLMETH_CAST(meth_wxDataViewDateRenderer_GetValue), METH_VARARGS|METH_KEYWORDS, doc_wxDataViewDateRenderer_GetValue},
    {sipName_GetView, meth_wxDataViewDateRenderer_GetView, METH_VARARGS, SIP_NULLPTR},
    {sipName_SetValue, SIP_MLMETH_CAST(meth_wxDataViewDateRenderer_SetValue), METH_VARARGS|METH_KEYWORDS, doc_wxDataViewDateRenderer_SetValue}
};

sipVariableDef variables_wxDataViewDateRenderer[] = {
    {PropertyVariable, sipName_Value, &methods_wxDataViewDateRenderer[1], &methods_wxDataViewDateRenderer[3], SIP_NULLPTR, SIP_NULLPTR},
};

PyDoc_STRVAR(doc_wxDataViewDateRenderer, "DataViewDateRenderer(varianttype=DataViewDateRenderer.GetDefaultType(), mode=DATAVIEW_CELL_ACTIVATABLE, align=DVR_DEFAULT_ALIGNMENT) -> None\n"
"\n"
"This class is used by wxDataViewCtrl to render calendar controls.");


sipClassTypeDef sipTypeDef__dataview_wxDataViewDateRenderer = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_SCC|SIP_TYPE_CLASS,
        sipNameNr_wxDataViewDateRenderer,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_DataViewDateRenderer,
        {0, 0, 1},
        4, methods_wxDataViewDateRenderer,
        0, SIP_NULLPTR,
        1, variables_wxDataViewDateRenderer,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxDataViewDateRenderer,
    -1,
    -1,
    supers_wxDataViewDateRenderer,
    SIP_NULLPTR,
    init_type_wxDataViewDateRenderer,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxDataViewDateRenderer,
    SIP_NULLPTR,
    array_wxDataViewDateRenderer,
    SIP_NULLPTR,
    release_wxDataViewDateRenderer,
    cast_wxDataViewDateRenderer,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    array_delete_wxDataViewDateRenderer,
    sizeof (::wxDataViewDateRenderer),
};
