/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_propgrid.h"
        #include <wx/propgrid/props.h>
        #include <wx/propgrid/property.h>
        #include <wx/bmpbndl.h>
        #include <wx/validate.h>
        #include <wx/colour.h>
        #include <wx/propgrid/property.h>
        #include <wx/propgrid/property.h>
        #include <wx/propgrid/editors.h>
        #include <wx/bitmap.h>
        #include <wx/propgrid/propgrid.h>
        #include <wx/propgrid/editors.h>
        #include <wx/propgrid/property.h>
        #include <wx/dc.h>
        #include <wx/gdicmn.h>
        #include <wx/propgrid/property.h>
        #include <wx/window.h>
        #include <wx/event.h>
        #include <wx/gdicmn.h>
        #include <wx/propgrid/propgrid.h>
        #include <wx/object.h>
        #include <wx/object.h>
        #include <wx/object.h>


class sipwxBoolProperty : public ::wxBoolProperty
{
public:
    sipwxBoolProperty(const ::wxString&, const ::wxString&, bool);
    sipwxBoolProperty(const ::wxBoolProperty&);
    virtual ~sipwxBoolProperty();

    /*
     * There is a protected method for every virtual method visible from
     * this class.
     */
protected:
    void OnSetValue() SIP_OVERRIDE;
    ::wxPGVariant DoGetValue() const SIP_OVERRIDE;
    bool ValidateValue(::wxPGVariant&, ::wxPGValidationInfo&) const SIP_OVERRIDE;
    bool StringToValue(::wxPGVariant&, const ::wxString&, int) const SIP_OVERRIDE;
    bool IntToValue(::wxPGVariant&, int, int) const SIP_OVERRIDE;
    ::wxString ValueToString(::wxPGVariant&, int) const SIP_OVERRIDE;
    ::wxSize OnMeasureImage(int) const SIP_OVERRIDE;
    bool OnEvent(::wxPropertyGrid*, ::wxWindow*, ::wxEvent&) SIP_OVERRIDE;
    ::wxPGVariant ChildChanged(::wxPGVariant&, int, ::wxPGVariant&) const SIP_OVERRIDE;
    const ::wxPGEditor* DoGetEditorClass() const SIP_OVERRIDE;
    ::wxValidator* DoGetValidator() const SIP_OVERRIDE;
    void OnCustomPaint(::wxDC&, const ::wxRect&, ::wxPGPaintData&) SIP_OVERRIDE;
    ::wxPGCellRenderer* GetCellRenderer(int) const SIP_OVERRIDE;
    int GetChoiceSelection() const SIP_OVERRIDE;
    void RefreshChildren() SIP_OVERRIDE;
    bool DoSetAttribute(const ::wxString&, ::wxPGVariant&) SIP_OVERRIDE;
    ::wxPGVariant DoGetAttribute(const ::wxString&) const SIP_OVERRIDE;
    ::wxPGEditorDialogAdapter* GetEditorDialog() const SIP_OVERRIDE;
    void OnValidationFailure(::wxPGVariant&) SIP_OVERRIDE;
    ::wxString GetValueAsString(int) const SIP_OVERRIDE;

public:
    sipSimpleWrapper *sipPySelf;

private:
    sipwxBoolProperty(const sipwxBoolProperty &);
    sipwxBoolProperty &operator = (const sipwxBoolProperty &);

    char sipPyMethods[20];
};

sipwxBoolProperty::sipwxBoolProperty(const ::wxString& label, const ::wxString& name, bool value): ::wxBoolProperty(label, name, value), sipPySelf(SIP_NULLPTR)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipwxBoolProperty::sipwxBoolProperty(const ::wxBoolProperty& a0): ::wxBoolProperty(a0), sipPySelf(SIP_NULLPTR)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipwxBoolProperty::~sipwxBoolProperty()
{
    sipInstanceDestroyedEx(&sipPySelf);
}

void sipwxBoolProperty::OnSetValue()
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[0], &sipPySelf, SIP_NULLPTR, sipName_OnSetValue);

    if (!sipMeth)
    {
        ::wxBoolProperty::OnSetValue();
        return;
    }

    extern void sipVH__propgrid_3(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    sipVH__propgrid_3(sipGILState, 0, sipPySelf, sipMeth);
}

::wxPGVariant sipwxBoolProperty::DoGetValue() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[1]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_DoGetValue);

    if (!sipMeth)
        return ::wxBoolProperty::DoGetValue();

    extern ::wxPGVariant sipVH__propgrid_4(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__propgrid_4(sipGILState, 0, sipPySelf, sipMeth);
}

bool sipwxBoolProperty::ValidateValue(::wxPGVariant& value, ::wxPGValidationInfo& validationInfo) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[2]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_ValidateValue);

    if (!sipMeth)
        return ::wxBoolProperty::ValidateValue(value, validationInfo);

    extern bool sipVH__propgrid_5(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxPGVariant&, ::wxPGValidationInfo&);

    return sipVH__propgrid_5(sipGILState, 0, sipPySelf, sipMeth, value, validationInfo);
}

bool sipwxBoolProperty::StringToValue(::wxPGVariant& variant, const ::wxString& text, int argFlags) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[3]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_StringToValue);

    if (!sipMeth)
        return ::wxBoolProperty::StringToValue(variant, text, argFlags);

    extern bool sipVH__propgrid_6(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxPGVariant&, const ::wxString&, int);

    return sipVH__propgrid_6(sipGILState, 0, sipPySelf, sipMeth, variant, text, argFlags);
}

bool sipwxBoolProperty::IntToValue(::wxPGVariant& variant, int number, int argFlags) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[4]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_IntToValue);

    if (!sipMeth)
        return ::wxBoolProperty::IntToValue(variant, number, argFlags);

    extern bool sipVH__propgrid_7(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxPGVariant&, int, int);

    return sipVH__propgrid_7(sipGILState, 0, sipPySelf, sipMeth, variant, number, argFlags);
}

::wxString sipwxBoolProperty::ValueToString(::wxPGVariant& value, int argFlags) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[5]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_ValueToString);

    if (!sipMeth)
        return ::wxBoolProperty::ValueToString(value, argFlags);

    extern ::wxString sipVH__propgrid_8(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxPGVariant&, int);

    return sipVH__propgrid_8(sipGILState, 0, sipPySelf, sipMeth, value, argFlags);
}

::wxSize sipwxBoolProperty::OnMeasureImage(int item) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[6]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_OnMeasureImage);

    if (!sipMeth)
        return ::wxBoolProperty::OnMeasureImage(item);

    extern ::wxSize sipVH__propgrid_9(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, int);

    return sipVH__propgrid_9(sipGILState, 0, sipPySelf, sipMeth, item);
}

bool sipwxBoolProperty::OnEvent(::wxPropertyGrid*propgrid, ::wxWindow*wnd_primary, ::wxEvent& event)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[7], &sipPySelf, SIP_NULLPTR, sipName_OnEvent);

    if (!sipMeth)
        return ::wxBoolProperty::OnEvent(propgrid, wnd_primary, event);

    extern bool sipVH__propgrid_10(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxPropertyGrid*, ::wxWindow*, ::wxEvent&);

    return sipVH__propgrid_10(sipGILState, 0, sipPySelf, sipMeth, propgrid, wnd_primary, event);
}

::wxPGVariant sipwxBoolProperty::ChildChanged(::wxPGVariant& thisValue, int childIndex, ::wxPGVariant& childValue) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[8]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_ChildChanged);

    if (!sipMeth)
        return ::wxBoolProperty::ChildChanged(thisValue, childIndex, childValue);

    extern ::wxPGVariant sipVH__propgrid_11(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxPGVariant&, int, ::wxPGVariant&);

    return sipVH__propgrid_11(sipGILState, 0, sipPySelf, sipMeth, thisValue, childIndex, childValue);
}

const ::wxPGEditor* sipwxBoolProperty::DoGetEditorClass() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[9]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_DoGetEditorClass);

    if (!sipMeth)
        return ::wxBoolProperty::DoGetEditorClass();

    extern const ::wxPGEditor* sipVH__propgrid_12(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__propgrid_12(sipGILState, 0, sipPySelf, sipMeth);
}

::wxValidator* sipwxBoolProperty::DoGetValidator() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[10]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_DoGetValidator);

    if (!sipMeth)
        return ::wxBoolProperty::DoGetValidator();

    extern ::wxValidator* sipVH__propgrid_13(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__propgrid_13(sipGILState, 0, sipPySelf, sipMeth);
}

void sipwxBoolProperty::OnCustomPaint(::wxDC& dc, const ::wxRect& rect, ::wxPGPaintData& paintdata)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[11], &sipPySelf, SIP_NULLPTR, sipName_OnCustomPaint);

    if (!sipMeth)
    {
        ::wxBoolProperty::OnCustomPaint(dc, rect, paintdata);
        return;
    }

    extern void sipVH__propgrid_14(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxDC&, const ::wxRect&, ::wxPGPaintData&);

    sipVH__propgrid_14(sipGILState, 0, sipPySelf, sipMeth, dc, rect, paintdata);
}

::wxPGCellRenderer* sipwxBoolProperty::GetCellRenderer(int column) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[12]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_GetCellRenderer);

    if (!sipMeth)
        return ::wxBoolProperty::GetCellRenderer(column);

    extern ::wxPGCellRenderer* sipVH__propgrid_15(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, int);

    return sipVH__propgrid_15(sipGILState, 0, sipPySelf, sipMeth, column);
}

int sipwxBoolProperty::GetChoiceSelection() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[13]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_GetChoiceSelection);

    if (!sipMeth)
        return ::wxBoolProperty::GetChoiceSelection();

    extern int sipVH__propgrid_16(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__propgrid_16(sipGILState, 0, sipPySelf, sipMeth);
}

void sipwxBoolProperty::RefreshChildren()
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[14], &sipPySelf, SIP_NULLPTR, sipName_RefreshChildren);

    if (!sipMeth)
    {
        ::wxBoolProperty::RefreshChildren();
        return;
    }

    extern void sipVH__propgrid_3(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    sipVH__propgrid_3(sipGILState, 0, sipPySelf, sipMeth);
}

bool sipwxBoolProperty::DoSetAttribute(const ::wxString& name, ::wxPGVariant& value)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[15], &sipPySelf, SIP_NULLPTR, sipName_DoSetAttribute);

    if (!sipMeth)
        return ::wxBoolProperty::DoSetAttribute(name, value);

    extern bool sipVH__propgrid_17(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, const ::wxString&, ::wxPGVariant&);

    return sipVH__propgrid_17(sipGILState, 0, sipPySelf, sipMeth, name, value);
}

::wxPGVariant sipwxBoolProperty::DoGetAttribute(const ::wxString& name) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[16]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_DoGetAttribute);

    if (!sipMeth)
        return ::wxBoolProperty::DoGetAttribute(name);

    extern ::wxPGVariant sipVH__propgrid_18(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, const ::wxString&);

    return sipVH__propgrid_18(sipGILState, 0, sipPySelf, sipMeth, name);
}

::wxPGEditorDialogAdapter* sipwxBoolProperty::GetEditorDialog() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[17]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_GetEditorDialog);

    if (!sipMeth)
        return ::wxBoolProperty::GetEditorDialog();

    extern ::wxPGEditorDialogAdapter* sipVH__propgrid_19(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__propgrid_19(sipGILState, 0, sipPySelf, sipMeth);
}

void sipwxBoolProperty::OnValidationFailure(::wxPGVariant& pendingValue)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[18], &sipPySelf, SIP_NULLPTR, sipName_OnValidationFailure);

    if (!sipMeth)
    {
        ::wxBoolProperty::OnValidationFailure(pendingValue);
        return;
    }

    extern void sipVH__propgrid_20(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxPGVariant&);

    sipVH__propgrid_20(sipGILState, 0, sipPySelf, sipMeth, pendingValue);
}

::wxString sipwxBoolProperty::GetValueAsString(int argFlags) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[19]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_GetValueAsString);

    if (!sipMeth)
        return ::wxBoolProperty::GetValueAsString(argFlags);

    extern ::wxString sipVH__propgrid_21(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, int);

    return sipVH__propgrid_21(sipGILState, 0, sipPySelf, sipMeth, argFlags);
}


PyDoc_STRVAR(doc_wxBoolProperty_ValueToString, "ValueToString(value, argFlags=0) -> str\n"
"\n"
"Converts property value into a text representation.");

extern "C" {static PyObject *meth_wxBoolProperty_ValueToString(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxBoolProperty_ValueToString(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxPGVariant* value;
        int valueState = 0;
        int argFlags = 0;
        const ::wxBoolProperty *sipCpp;

        static const char *sipKwdList[] = {
            sipName_value,
            sipName_argFlags,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1|i", &sipSelf, sipType_wxBoolProperty, &sipCpp, sipType_wxPGVariant, &value, &valueState, &argFlags))
        {
            ::wxString*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxString((sipSelfWasArg ? sipCpp->::wxBoolProperty::ValueToString(*value, argFlags) : sipCpp->ValueToString(*value, argFlags)));
            Py_END_ALLOW_THREADS
            sipReleaseType(value, sipType_wxPGVariant, valueState);

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxString, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_BoolProperty, sipName_ValueToString, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxBoolProperty_StringToValue, "StringToValue(text, argFlags=0) -> Tuple[bool, PGVariant]\n"
"\n"
"Converts text into wxVariant value appropriate for this property.");

extern "C" {static PyObject *meth_wxBoolProperty_StringToValue(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxBoolProperty_StringToValue(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxPGVariant* variant;
        const ::wxString* text;
        int textState = 0;
        int argFlags = 0;
        const ::wxBoolProperty *sipCpp;

        static const char *sipKwdList[] = {
            sipName_text,
            sipName_argFlags,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1|i", &sipSelf, sipType_wxBoolProperty, &sipCpp, sipType_wxString, &text, &textState, &argFlags))
        {
            bool sipRes;
            variant = new ::wxPGVariant();

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxBoolProperty::StringToValue(*variant, *text, argFlags) : sipCpp->StringToValue(*variant, *text, argFlags));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(text), sipType_wxString, textState);

            if (PyErr_Occurred())
                return 0;

            return sipBuildResult(0, "(bN)", sipRes, variant, sipType_wxPGVariant, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_BoolProperty, sipName_StringToValue, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxBoolProperty_IntToValue, "IntToValue(number, argFlags=0) -> Tuple[bool, PGVariant]\n"
"\n"
"Converts integer (possibly a choice selection) into wxVariant value\n"
"appropriate for this property.");

extern "C" {static PyObject *meth_wxBoolProperty_IntToValue(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxBoolProperty_IntToValue(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxPGVariant* variant;
        int number;
        int argFlags = 0;
        const ::wxBoolProperty *sipCpp;

        static const char *sipKwdList[] = {
            sipName_number,
            sipName_argFlags,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "Bi|i", &sipSelf, sipType_wxBoolProperty, &sipCpp, &number, &argFlags))
        {
            bool sipRes;
            variant = new ::wxPGVariant();

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxBoolProperty::IntToValue(*variant, number, argFlags) : sipCpp->IntToValue(*variant, number, argFlags));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipBuildResult(0, "(bN)", sipRes, variant, sipType_wxPGVariant, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_BoolProperty, sipName_IntToValue, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxBoolProperty_DoSetAttribute, "DoSetAttribute(name, value) -> bool\n"
"\n"
"Reimplement this member function to add special handling for\n"
"attributes of this property.");

extern "C" {static PyObject *meth_wxBoolProperty_DoSetAttribute(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxBoolProperty_DoSetAttribute(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const ::wxString* name;
        int nameState = 0;
        ::wxPGVariant* value;
        int valueState = 0;
        ::wxBoolProperty *sipCpp;

        static const char *sipKwdList[] = {
            sipName_name,
            sipName_value,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1J1", &sipSelf, sipType_wxBoolProperty, &sipCpp, sipType_wxString, &name, &nameState, sipType_wxPGVariant, &value, &valueState))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxBoolProperty::DoSetAttribute(*name, *value) : sipCpp->DoSetAttribute(*name, *value));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(name), sipType_wxString, nameState);
            sipReleaseType(value, sipType_wxPGVariant, valueState);

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_BoolProperty, sipName_DoSetAttribute, SIP_NULLPTR);

    return SIP_NULLPTR;
}


/* Cast a pointer to a type somewhere in its inheritance hierarchy. */
extern "C" {static void *cast_wxBoolProperty(void *, const sipTypeDef *);}
static void *cast_wxBoolProperty(void *sipCppV, const sipTypeDef *targetType)
{
    ::wxBoolProperty *sipCpp = reinterpret_cast<::wxBoolProperty *>(sipCppV);

    if (targetType == sipType_wxBoolProperty)
        return sipCppV;

    sipCppV = ((const sipClassTypeDef *)sipType_wxPGProperty)->ctd_cast(static_cast<::wxPGProperty *>(sipCpp), targetType);
    if (sipCppV)
        return sipCppV;

    return SIP_NULLPTR;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxBoolProperty(void *, int);}
static void release_wxBoolProperty(void *sipCppV, int sipState)
{
    Py_BEGIN_ALLOW_THREADS

    if (sipState & SIP_DERIVED_CLASS)
        delete reinterpret_cast<sipwxBoolProperty *>(sipCppV);
    else
        delete reinterpret_cast<::wxBoolProperty *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void *array_wxBoolProperty(Py_ssize_t);}
static void *array_wxBoolProperty(Py_ssize_t sipNrElem)
{
    return new ::wxBoolProperty[sipNrElem];
}


extern "C" {static void array_delete_wxBoolProperty(void *);}
static void array_delete_wxBoolProperty(void *sipCpp)
{
    delete[] reinterpret_cast<::wxBoolProperty *>(sipCpp);
}


extern "C" {static void assign_wxBoolProperty(void *, Py_ssize_t, void *);}
static void assign_wxBoolProperty(void *sipDst, Py_ssize_t sipDstIdx, void *sipSrc)
{
    reinterpret_cast<::wxBoolProperty *>(sipDst)[sipDstIdx] = *reinterpret_cast<::wxBoolProperty *>(sipSrc);
}


extern "C" {static void *copy_wxBoolProperty(const void *, Py_ssize_t);}
static void *copy_wxBoolProperty(const void *sipSrc, Py_ssize_t sipSrcIdx)
{
    return new ::wxBoolProperty(reinterpret_cast<const ::wxBoolProperty *>(sipSrc)[sipSrcIdx]);
}


extern "C" {static void dealloc_wxBoolProperty(sipSimpleWrapper *);}
static void dealloc_wxBoolProperty(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerivedClass(sipSelf))
        reinterpret_cast<sipwxBoolProperty *>(sipGetAddress(sipSelf))->sipPySelf = SIP_NULLPTR;

    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxBoolProperty(sipGetAddress(sipSelf), sipIsDerivedClass(sipSelf));
    }
}


extern "C" {static void *init_type_wxBoolProperty(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxBoolProperty(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    sipwxBoolProperty *sipCpp = SIP_NULLPTR;

    {
        const ::wxString& labeldef = wxPG_LABEL;
        const ::wxString* label = &labeldef;
        int labelState = 0;
        const ::wxString& namedef = wxPG_LABEL;
        const ::wxString* name = &namedef;
        int nameState = 0;
        bool value = 0;

        static const char *sipKwdList[] = {
            sipName_label,
            sipName_name,
            sipName_value,
        };

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, sipKwdList, sipUnused, "|J1J1b", sipType_wxString, &label, &labelState, sipType_wxString, &name, &nameState, &value))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipwxBoolProperty(*label, *name, value);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxString *>(label), sipType_wxString, labelState);
            sipReleaseType(const_cast<::wxString *>(name), sipType_wxString, nameState);

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
        const ::wxBoolProperty* a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, "J9", sipType_wxBoolProperty, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipwxBoolProperty(*a0);
            Py_END_ALLOW_THREADS

            sipCpp->sipPySelf = sipSelf;

            return sipCpp;
        }
    }

    return SIP_NULLPTR;
}


/* Define this type's super-types. */
static sipEncodedTypeDef supers_wxBoolProperty[] = {{44, 255, 1}};


static PyMethodDef methods_wxBoolProperty[] = {
    {sipName_DoSetAttribute, SIP_MLMETH_CAST(meth_wxBoolProperty_DoSetAttribute), METH_VARARGS|METH_KEYWORDS, doc_wxBoolProperty_DoSetAttribute},
    {sipName_IntToValue, SIP_MLMETH_CAST(meth_wxBoolProperty_IntToValue), METH_VARARGS|METH_KEYWORDS, doc_wxBoolProperty_IntToValue},
    {sipName_StringToValue, SIP_MLMETH_CAST(meth_wxBoolProperty_StringToValue), METH_VARARGS|METH_KEYWORDS, doc_wxBoolProperty_StringToValue},
    {sipName_ValueToString, SIP_MLMETH_CAST(meth_wxBoolProperty_ValueToString), METH_VARARGS|METH_KEYWORDS, doc_wxBoolProperty_ValueToString}
};

PyDoc_STRVAR(doc_wxBoolProperty, "BoolProperty(label=PG_LABEL, name=PG_LABEL, value=False) -> None\n"
"\n"
"Basic property with boolean value.");


sipClassTypeDef sipTypeDef__propgrid_wxBoolProperty = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_SCC|SIP_TYPE_CLASS,
        sipNameNr_wxBoolProperty,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_BoolProperty,
        {0, 0, 1},
        4, methods_wxBoolProperty,
        0, SIP_NULLPTR,
        0, SIP_NULLPTR,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxBoolProperty,
    -1,
    -1,
    supers_wxBoolProperty,
    SIP_NULLPTR,
    init_type_wxBoolProperty,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxBoolProperty,
    assign_wxBoolProperty,
    array_wxBoolProperty,
    copy_wxBoolProperty,
    release_wxBoolProperty,
    cast_wxBoolProperty,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    array_delete_wxBoolProperty,
    sizeof (::wxBoolProperty),
};
