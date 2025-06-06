/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_core.h"
        #include <wx/graphics.h>
        #include <wx/colour.h>
        #include <wx/graphics.h>
        #include <wx/bitmap.h>
        #include <wx/graphics.h>


PyDoc_STRVAR(doc_wxGraphicsPenInfo_Colour, "Colour(col) -> GraphicsPenInfo");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_Colour(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_Colour(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxColour* col;
        int colState = 0;
        ::wxGraphicsPenInfo *sipCpp;

        static const char *sipKwdList[] = {
            sipName_col,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ1", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp, sipType_wxColour, &col, &colState))
        {
            ::wxGraphicsPenInfo*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = &sipCpp->Colour(*col);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxColour *>(col), sipType_wxColour, colState);

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxGraphicsPenInfo, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_Colour, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_Width, "Width(width) -> GraphicsPenInfo");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_Width(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_Width(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxDouble width;
        ::wxGraphicsPenInfo *sipCpp;

        static const char *sipKwdList[] = {
            sipName_width,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "Bd", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp, &width))
        {
            ::wxGraphicsPenInfo*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = &sipCpp->Width(width);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxGraphicsPenInfo, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_Width, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_Style, "Style(style) -> GraphicsPenInfo");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_Style(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_Style(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxPenStyle style;
        ::wxGraphicsPenInfo *sipCpp;

        static const char *sipKwdList[] = {
            sipName_style,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BE", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp, sipType_wxPenStyle, &style))
        {
            ::wxGraphicsPenInfo*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = &sipCpp->Style(style);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxGraphicsPenInfo, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_Style, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_Stipple, "Stipple(stipple) -> GraphicsPenInfo");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_Stipple(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_Stipple(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxBitmap* stipple;
        ::wxGraphicsPenInfo *sipCpp;

        static const char *sipKwdList[] = {
            sipName_stipple,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ9", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp, sipType_wxBitmap, &stipple))
        {
            ::wxGraphicsPenInfo*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = &sipCpp->Stipple(*stipple);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxGraphicsPenInfo, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_Stipple, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_Join, "Join(join) -> GraphicsPenInfo");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_Join(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_Join(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxPenJoin join;
        ::wxGraphicsPenInfo *sipCpp;

        static const char *sipKwdList[] = {
            sipName_join,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BE", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp, sipType_wxPenJoin, &join))
        {
            ::wxGraphicsPenInfo*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = &sipCpp->Join(join);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxGraphicsPenInfo, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_Join, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_Cap, "Cap(cap) -> GraphicsPenInfo");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_Cap(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_Cap(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxPenCap cap;
        ::wxGraphicsPenInfo *sipCpp;

        static const char *sipKwdList[] = {
            sipName_cap,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BE", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp, sipType_wxPenCap, &cap))
        {
            ::wxGraphicsPenInfo*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = &sipCpp->Cap(cap);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxGraphicsPenInfo, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_Cap, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_LinearGradient, "LinearGradient(x1, y1, x2, y2, c1, c2, matrix=NullGraphicsMatrix) -> GraphicsPenInfo\n"
"LinearGradient(x1, y1, x2, y2, stops, matrix=NullGraphicsMatrix) -> GraphicsPenInfo\n"
"");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_LinearGradient(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_LinearGradient(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxDouble x1;
        ::wxDouble y1;
        ::wxDouble x2;
        ::wxDouble y2;
        const ::wxColour* c1;
        int c1State = 0;
        const ::wxColour* c2;
        int c2State = 0;
        const ::wxGraphicsMatrix& matrixdef = wxNullGraphicsMatrix;
        const ::wxGraphicsMatrix* matrix = &matrixdef;
        ::wxGraphicsPenInfo *sipCpp;

        static const char *sipKwdList[] = {
            sipName_x1,
            sipName_y1,
            sipName_x2,
            sipName_y2,
            sipName_c1,
            sipName_c2,
            sipName_matrix,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BddddJ1J1|J9", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp, &x1, &y1, &x2, &y2, sipType_wxColour, &c1, &c1State, sipType_wxColour, &c2, &c2State, sipType_wxGraphicsMatrix, &matrix))
        {
            ::wxGraphicsPenInfo*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = &sipCpp->LinearGradient(x1, y1, x2, y2, *c1, *c2, *matrix);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxColour *>(c1), sipType_wxColour, c1State);
            sipReleaseType(const_cast<::wxColour *>(c2), sipType_wxColour, c2State);

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxGraphicsPenInfo, SIP_NULLPTR);
        }
    }

    {
        ::wxDouble x1;
        ::wxDouble y1;
        ::wxDouble x2;
        ::wxDouble y2;
        const ::wxGraphicsGradientStops* stops;
        const ::wxGraphicsMatrix& matrixdef = wxNullGraphicsMatrix;
        const ::wxGraphicsMatrix* matrix = &matrixdef;
        ::wxGraphicsPenInfo *sipCpp;

        static const char *sipKwdList[] = {
            sipName_x1,
            sipName_y1,
            sipName_x2,
            sipName_y2,
            sipName_stops,
            sipName_matrix,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BddddJ9|J9", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp, &x1, &y1, &x2, &y2, sipType_wxGraphicsGradientStops, &stops, sipType_wxGraphicsMatrix, &matrix))
        {
            ::wxGraphicsPenInfo*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = &sipCpp->LinearGradient(x1, y1, x2, y2, *stops, *matrix);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxGraphicsPenInfo, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_LinearGradient, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_RadialGradient, "RadialGradient(startX, startY, endX, endY, radius, oColor, cColor, matrix=NullGraphicsMatrix) -> GraphicsPenInfo\n"
"RadialGradient(startX, startY, endX, endY, radius, stops, matrix=NullGraphicsMatrix) -> GraphicsPenInfo\n"
"");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_RadialGradient(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_RadialGradient(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        ::wxDouble startX;
        ::wxDouble startY;
        ::wxDouble endX;
        ::wxDouble endY;
        ::wxDouble radius;
        const ::wxColour* oColor;
        int oColorState = 0;
        const ::wxColour* cColor;
        int cColorState = 0;
        const ::wxGraphicsMatrix& matrixdef = wxNullGraphicsMatrix;
        const ::wxGraphicsMatrix* matrix = &matrixdef;
        ::wxGraphicsPenInfo *sipCpp;

        static const char *sipKwdList[] = {
            sipName_startX,
            sipName_startY,
            sipName_endX,
            sipName_endY,
            sipName_radius,
            sipName_oColor,
            sipName_cColor,
            sipName_matrix,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BdddddJ1J1|J9", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp, &startX, &startY, &endX, &endY, &radius, sipType_wxColour, &oColor, &oColorState, sipType_wxColour, &cColor, &cColorState, sipType_wxGraphicsMatrix, &matrix))
        {
            ::wxGraphicsPenInfo*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = &sipCpp->RadialGradient(startX, startY, endX, endY, radius, *oColor, *cColor, *matrix);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxColour *>(oColor), sipType_wxColour, oColorState);
            sipReleaseType(const_cast<::wxColour *>(cColor), sipType_wxColour, cColorState);

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxGraphicsPenInfo, SIP_NULLPTR);
        }
    }

    {
        ::wxDouble startX;
        ::wxDouble startY;
        ::wxDouble endX;
        ::wxDouble endY;
        ::wxDouble radius;
        const ::wxGraphicsGradientStops* stops;
        const ::wxGraphicsMatrix& matrixdef = wxNullGraphicsMatrix;
        const ::wxGraphicsMatrix* matrix = &matrixdef;
        ::wxGraphicsPenInfo *sipCpp;

        static const char *sipKwdList[] = {
            sipName_startX,
            sipName_startY,
            sipName_endX,
            sipName_endY,
            sipName_radius,
            sipName_stops,
            sipName_matrix,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BdddddJ9|J9", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp, &startX, &startY, &endX, &endY, &radius, sipType_wxGraphicsGradientStops, &stops, sipType_wxGraphicsMatrix, &matrix))
        {
            ::wxGraphicsPenInfo*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = &sipCpp->RadialGradient(startX, startY, endX, endY, radius, *stops, *matrix);
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromType(sipRes, sipType_wxGraphicsPenInfo, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_RadialGradient, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_GetColour, "GetColour() -> Colour");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_GetColour(PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_GetColour(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxGraphicsPenInfo *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp))
        {
            ::wxColour*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxColour(sipCpp->GetColour());
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxColour, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_GetColour, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_GetStipple, "GetStipple() -> Bitmap");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_GetStipple(PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_GetStipple(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxGraphicsPenInfo *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp))
        {
            ::wxBitmap*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxBitmap(sipCpp->GetStipple());
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxBitmap, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_GetStipple, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_GetStyle, "GetStyle() -> PenStyle");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_GetStyle(PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_GetStyle(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxGraphicsPenInfo *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp))
        {
            ::wxPenStyle sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetStyle();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromEnum(static_cast<int>(sipRes), sipType_wxPenStyle);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_GetStyle, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_GetJoin, "GetJoin() -> PenJoin");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_GetJoin(PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_GetJoin(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxGraphicsPenInfo *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp))
        {
            ::wxPenJoin sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetJoin();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromEnum(static_cast<int>(sipRes), sipType_wxPenJoin);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_GetJoin, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_GetCap, "GetCap() -> PenCap");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_GetCap(PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_GetCap(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxGraphicsPenInfo *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp))
        {
            ::wxPenCap sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetCap();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromEnum(static_cast<int>(sipRes), sipType_wxPenCap);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_GetCap, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_IsTransparent, "IsTransparent() -> bool");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_IsTransparent(PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_IsTransparent(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxGraphicsPenInfo *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->IsTransparent();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_IsTransparent, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_GetWidth, "GetWidth() -> float");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_GetWidth(PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_GetWidth(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxGraphicsPenInfo *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp))
        {
            ::wxDouble sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetWidth();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyFloat_FromDouble(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_GetWidth, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_GetGradientType, "GetGradientType() -> GradientType");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_GetGradientType(PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_GetGradientType(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxGraphicsPenInfo *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp))
        {
            ::wxGradientType sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetGradientType();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromEnum(static_cast<int>(sipRes), sipType_wxGradientType);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_GetGradientType, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_GetX1, "GetX1() -> float");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_GetX1(PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_GetX1(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxGraphicsPenInfo *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp))
        {
            ::wxDouble sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetX1();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyFloat_FromDouble(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_GetX1, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_GetY1, "GetY1() -> float");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_GetY1(PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_GetY1(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxGraphicsPenInfo *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp))
        {
            ::wxDouble sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetY1();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyFloat_FromDouble(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_GetY1, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_GetX2, "GetX2() -> float");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_GetX2(PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_GetX2(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxGraphicsPenInfo *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp))
        {
            ::wxDouble sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetX2();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyFloat_FromDouble(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_GetX2, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_GetY2, "GetY2() -> float");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_GetY2(PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_GetY2(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxGraphicsPenInfo *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp))
        {
            ::wxDouble sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetY2();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyFloat_FromDouble(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_GetY2, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_GetStartX, "GetStartX() -> float");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_GetStartX(PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_GetStartX(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxGraphicsPenInfo *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp))
        {
            ::wxDouble sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetStartX();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyFloat_FromDouble(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_GetStartX, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_GetStartY, "GetStartY() -> float");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_GetStartY(PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_GetStartY(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxGraphicsPenInfo *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp))
        {
            ::wxDouble sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetStartY();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyFloat_FromDouble(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_GetStartY, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_GetEndX, "GetEndX() -> float");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_GetEndX(PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_GetEndX(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxGraphicsPenInfo *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp))
        {
            ::wxDouble sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetEndX();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyFloat_FromDouble(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_GetEndX, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_GetEndY, "GetEndY() -> float");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_GetEndY(PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_GetEndY(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxGraphicsPenInfo *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp))
        {
            ::wxDouble sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetEndY();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyFloat_FromDouble(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_GetEndY, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_GetRadius, "GetRadius() -> float");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_GetRadius(PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_GetRadius(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxGraphicsPenInfo *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp))
        {
            ::wxDouble sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->GetRadius();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyFloat_FromDouble(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_GetRadius, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGraphicsPenInfo_GetStops, "GetStops() -> GraphicsGradientStops");

extern "C" {static PyObject *meth_wxGraphicsPenInfo_GetStops(PyObject *, PyObject *);}
static PyObject *meth_wxGraphicsPenInfo_GetStops(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;

    {
        const ::wxGraphicsPenInfo *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGraphicsPenInfo, &sipCpp))
        {
            ::wxGraphicsGradientStops*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxGraphicsGradientStops(sipCpp->GetStops());
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxGraphicsGradientStops, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_GraphicsPenInfo, sipName_GetStops, SIP_NULLPTR);

    return SIP_NULLPTR;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxGraphicsPenInfo(void *, int);}
static void release_wxGraphicsPenInfo(void *sipCppV, int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast<::wxGraphicsPenInfo *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void *array_wxGraphicsPenInfo(Py_ssize_t);}
static void *array_wxGraphicsPenInfo(Py_ssize_t sipNrElem)
{
    return new ::wxGraphicsPenInfo[sipNrElem];
}


extern "C" {static void array_delete_wxGraphicsPenInfo(void *);}
static void array_delete_wxGraphicsPenInfo(void *sipCpp)
{
    delete[] reinterpret_cast<::wxGraphicsPenInfo *>(sipCpp);
}


extern "C" {static void assign_wxGraphicsPenInfo(void *, Py_ssize_t, void *);}
static void assign_wxGraphicsPenInfo(void *sipDst, Py_ssize_t sipDstIdx, void *sipSrc)
{
    reinterpret_cast<::wxGraphicsPenInfo *>(sipDst)[sipDstIdx] = *reinterpret_cast<::wxGraphicsPenInfo *>(sipSrc);
}


extern "C" {static void *copy_wxGraphicsPenInfo(const void *, Py_ssize_t);}
static void *copy_wxGraphicsPenInfo(const void *sipSrc, Py_ssize_t sipSrcIdx)
{
    return new ::wxGraphicsPenInfo(reinterpret_cast<const ::wxGraphicsPenInfo *>(sipSrc)[sipSrcIdx]);
}


extern "C" {static void dealloc_wxGraphicsPenInfo(sipSimpleWrapper *);}
static void dealloc_wxGraphicsPenInfo(sipSimpleWrapper *sipSelf)
{
    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxGraphicsPenInfo(sipGetAddress(sipSelf), 0);
    }
}


extern "C" {static void *init_type_wxGraphicsPenInfo(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxGraphicsPenInfo(sipSimpleWrapper *, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    ::wxGraphicsPenInfo *sipCpp = SIP_NULLPTR;

    {
        const ::wxColour& colourdef = wxColour();
        const ::wxColour* colour = &colourdef;
        int colourState = 0;
        ::wxDouble width = 1;
        ::wxPenStyle style = wxPENSTYLE_SOLID;

        static const char *sipKwdList[] = {
            sipName_colour,
            sipName_width,
            sipName_style,
        };

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, sipKwdList, sipUnused, "|J1dE", sipType_wxColour, &colour, &colourState, &width, sipType_wxPenStyle, &style))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new ::wxGraphicsPenInfo(*colour, width, style);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxColour *>(colour), sipType_wxColour, colourState);

            if (PyErr_Occurred())
            {
                delete sipCpp;
                return SIP_NULLPTR;
            }

            return sipCpp;
        }
    }

    {
        const ::wxGraphicsPenInfo* a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, "J9", sipType_wxGraphicsPenInfo, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new ::wxGraphicsPenInfo(*a0);
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    return SIP_NULLPTR;
}


static PyMethodDef methods_wxGraphicsPenInfo[] = {
    {sipName_Cap, SIP_MLMETH_CAST(meth_wxGraphicsPenInfo_Cap), METH_VARARGS|METH_KEYWORDS, doc_wxGraphicsPenInfo_Cap},
    {sipName_Colour, SIP_MLMETH_CAST(meth_wxGraphicsPenInfo_Colour), METH_VARARGS|METH_KEYWORDS, doc_wxGraphicsPenInfo_Colour},
    {sipName_GetCap, meth_wxGraphicsPenInfo_GetCap, METH_VARARGS, doc_wxGraphicsPenInfo_GetCap},
    {sipName_GetColour, meth_wxGraphicsPenInfo_GetColour, METH_VARARGS, doc_wxGraphicsPenInfo_GetColour},
    {sipName_GetEndX, meth_wxGraphicsPenInfo_GetEndX, METH_VARARGS, doc_wxGraphicsPenInfo_GetEndX},
    {sipName_GetEndY, meth_wxGraphicsPenInfo_GetEndY, METH_VARARGS, doc_wxGraphicsPenInfo_GetEndY},
    {sipName_GetGradientType, meth_wxGraphicsPenInfo_GetGradientType, METH_VARARGS, doc_wxGraphicsPenInfo_GetGradientType},
    {sipName_GetJoin, meth_wxGraphicsPenInfo_GetJoin, METH_VARARGS, doc_wxGraphicsPenInfo_GetJoin},
    {sipName_GetRadius, meth_wxGraphicsPenInfo_GetRadius, METH_VARARGS, doc_wxGraphicsPenInfo_GetRadius},
    {sipName_GetStartX, meth_wxGraphicsPenInfo_GetStartX, METH_VARARGS, doc_wxGraphicsPenInfo_GetStartX},
    {sipName_GetStartY, meth_wxGraphicsPenInfo_GetStartY, METH_VARARGS, doc_wxGraphicsPenInfo_GetStartY},
    {sipName_GetStipple, meth_wxGraphicsPenInfo_GetStipple, METH_VARARGS, doc_wxGraphicsPenInfo_GetStipple},
    {sipName_GetStops, meth_wxGraphicsPenInfo_GetStops, METH_VARARGS, doc_wxGraphicsPenInfo_GetStops},
    {sipName_GetStyle, meth_wxGraphicsPenInfo_GetStyle, METH_VARARGS, doc_wxGraphicsPenInfo_GetStyle},
    {sipName_GetWidth, meth_wxGraphicsPenInfo_GetWidth, METH_VARARGS, doc_wxGraphicsPenInfo_GetWidth},
    {sipName_GetX1, meth_wxGraphicsPenInfo_GetX1, METH_VARARGS, doc_wxGraphicsPenInfo_GetX1},
    {sipName_GetX2, meth_wxGraphicsPenInfo_GetX2, METH_VARARGS, doc_wxGraphicsPenInfo_GetX2},
    {sipName_GetY1, meth_wxGraphicsPenInfo_GetY1, METH_VARARGS, doc_wxGraphicsPenInfo_GetY1},
    {sipName_GetY2, meth_wxGraphicsPenInfo_GetY2, METH_VARARGS, doc_wxGraphicsPenInfo_GetY2},
    {sipName_IsTransparent, meth_wxGraphicsPenInfo_IsTransparent, METH_VARARGS, doc_wxGraphicsPenInfo_IsTransparent},
    {sipName_Join, SIP_MLMETH_CAST(meth_wxGraphicsPenInfo_Join), METH_VARARGS|METH_KEYWORDS, doc_wxGraphicsPenInfo_Join},
    {sipName_LinearGradient, SIP_MLMETH_CAST(meth_wxGraphicsPenInfo_LinearGradient), METH_VARARGS|METH_KEYWORDS, doc_wxGraphicsPenInfo_LinearGradient},
    {sipName_RadialGradient, SIP_MLMETH_CAST(meth_wxGraphicsPenInfo_RadialGradient), METH_VARARGS|METH_KEYWORDS, doc_wxGraphicsPenInfo_RadialGradient},
    {sipName_Stipple, SIP_MLMETH_CAST(meth_wxGraphicsPenInfo_Stipple), METH_VARARGS|METH_KEYWORDS, doc_wxGraphicsPenInfo_Stipple},
    {sipName_Style, SIP_MLMETH_CAST(meth_wxGraphicsPenInfo_Style), METH_VARARGS|METH_KEYWORDS, doc_wxGraphicsPenInfo_Style},
    {sipName_Width, SIP_MLMETH_CAST(meth_wxGraphicsPenInfo_Width), METH_VARARGS|METH_KEYWORDS, doc_wxGraphicsPenInfo_Width}
};

sipVariableDef variables_wxGraphicsPenInfo[] = {
    {PropertyVariable, sipName_Y2, &methods_wxGraphicsPenInfo[18], SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_Y1, &methods_wxGraphicsPenInfo[17], SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_X2, &methods_wxGraphicsPenInfo[16], SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_X1, &methods_wxGraphicsPenInfo[15], SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_Stops, &methods_wxGraphicsPenInfo[12], SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_StartY, &methods_wxGraphicsPenInfo[10], SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_StartX, &methods_wxGraphicsPenInfo[9], SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_Radius, &methods_wxGraphicsPenInfo[8], SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_GradientType, &methods_wxGraphicsPenInfo[6], SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_EndY, &methods_wxGraphicsPenInfo[5], SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_EndX, &methods_wxGraphicsPenInfo[4], SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
};

PyDoc_STRVAR(doc_wxGraphicsPenInfo, "GraphicsPenInfo(colour=Colour(), width=1.0, style=PENSTYLE_SOLID) -> None\n"
"\n"
"This class is a helper used for wxGraphicsPen creation using named\n"
"parameter idiom: it allows specifying various wxGraphicsPen attributes\n"
"using the chained calls to its clearly named methods instead of\n"
"passing them in the fixed order to wxGraphicsPen constructors.");


sipClassTypeDef sipTypeDef__core_wxGraphicsPenInfo = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_CLASS,
        sipNameNr_wxGraphicsPenInfo,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_GraphicsPenInfo,
        {0, 0, 1},
        26, methods_wxGraphicsPenInfo,
        0, SIP_NULLPTR,
        11, variables_wxGraphicsPenInfo,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxGraphicsPenInfo,
    -1,
    -1,
    SIP_NULLPTR,
    SIP_NULLPTR,
    init_type_wxGraphicsPenInfo,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxGraphicsPenInfo,
    assign_wxGraphicsPenInfo,
    array_wxGraphicsPenInfo,
    copy_wxGraphicsPenInfo,
    release_wxGraphicsPenInfo,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    array_delete_wxGraphicsPenInfo,
    sizeof (::wxGraphicsPenInfo),
};
