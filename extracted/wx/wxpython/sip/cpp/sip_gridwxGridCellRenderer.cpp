/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_grid.h"
        #include <wx/grid.h>
        #include <wx/gdicmn.h>
        #include <wx/grid.h>
        #include <wx/grid.h>
        #include <wx/dc.h>
        #include <wx/gdicmn.h>


class sipwxGridCellRenderer : public ::wxGridCellRenderer
{
public:
    sipwxGridCellRenderer();
    virtual ~sipwxGridCellRenderer();

    /*
     * There is a protected method for every virtual method visible from
     * this class.
     */
protected:
    ::wxSize GetMaxBestSize(::wxGrid&, ::wxGridCellAttr&, ::wxDC&) SIP_OVERRIDE;
    int GetBestWidth(::wxGrid&, ::wxGridCellAttr&, ::wxDC&, int, int, int) SIP_OVERRIDE;
    int GetBestHeight(::wxGrid&, ::wxGridCellAttr&, ::wxDC&, int, int, int) SIP_OVERRIDE;
    ::wxSize GetBestSize(::wxGrid&, ::wxGridCellAttr&, ::wxDC&, int, int) SIP_OVERRIDE;
    void Draw(::wxGrid&, ::wxGridCellAttr&, ::wxDC&, const ::wxRect&, int, int, bool) SIP_OVERRIDE;
    ::wxGridCellRenderer* Clone() const SIP_OVERRIDE;

public:
    sipSimpleWrapper *sipPySelf;

private:
    sipwxGridCellRenderer(const sipwxGridCellRenderer &);
    sipwxGridCellRenderer &operator = (const sipwxGridCellRenderer &);

    char sipPyMethods[6];
};

sipwxGridCellRenderer::sipwxGridCellRenderer(): ::wxGridCellRenderer(), sipPySelf(SIP_NULLPTR)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipwxGridCellRenderer::~sipwxGridCellRenderer()
{
    sipInstanceDestroyedEx(&sipPySelf);
}

::wxSize sipwxGridCellRenderer::GetMaxBestSize(::wxGrid& grid, ::wxGridCellAttr& attr, ::wxDC& dc)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[0], &sipPySelf, SIP_NULLPTR, sipName_GetMaxBestSize);

    if (!sipMeth)
        return ::wxGridCellRenderer::GetMaxBestSize(grid, attr, dc);

    extern ::wxSize sipVH__grid_4(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxGrid&, ::wxGridCellAttr&, ::wxDC&);

    return sipVH__grid_4(sipGILState, 0, sipPySelf, sipMeth, grid, attr, dc);
}

int sipwxGridCellRenderer::GetBestWidth(::wxGrid& grid, ::wxGridCellAttr& attr, ::wxDC& dc, int row, int col, int height)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[1], &sipPySelf, SIP_NULLPTR, sipName_GetBestWidth);

    if (!sipMeth)
        return ::wxGridCellRenderer::GetBestWidth(grid, attr, dc, row, col, height);

    extern int sipVH__grid_3(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxGrid&, ::wxGridCellAttr&, ::wxDC&, int, int, int);

    return sipVH__grid_3(sipGILState, 0, sipPySelf, sipMeth, grid, attr, dc, row, col, height);
}

int sipwxGridCellRenderer::GetBestHeight(::wxGrid& grid, ::wxGridCellAttr& attr, ::wxDC& dc, int row, int col, int width)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[2], &sipPySelf, SIP_NULLPTR, sipName_GetBestHeight);

    if (!sipMeth)
        return ::wxGridCellRenderer::GetBestHeight(grid, attr, dc, row, col, width);

    extern int sipVH__grid_3(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxGrid&, ::wxGridCellAttr&, ::wxDC&, int, int, int);

    return sipVH__grid_3(sipGILState, 0, sipPySelf, sipMeth, grid, attr, dc, row, col, width);
}

::wxSize sipwxGridCellRenderer::GetBestSize(::wxGrid& grid, ::wxGridCellAttr& attr, ::wxDC& dc, int row, int col)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[3], &sipPySelf, sipName_GridCellRenderer, sipName_GetBestSize);

    if (!sipMeth)
        return ::wxSize();

    extern ::wxSize sipVH__grid_2(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxGrid&, ::wxGridCellAttr&, ::wxDC&, int, int);

    return sipVH__grid_2(sipGILState, 0, sipPySelf, sipMeth, grid, attr, dc, row, col);
}

void sipwxGridCellRenderer::Draw(::wxGrid& grid, ::wxGridCellAttr& attr, ::wxDC& dc, const ::wxRect& rect, int row, int col, bool isSelected)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[4], &sipPySelf, SIP_NULLPTR, sipName_Draw);

    if (!sipMeth)
    {
        ::wxGridCellRenderer::Draw(grid, attr, dc, rect, row, col, isSelected);
        return;
    }

    extern void sipVH__grid_1(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxGrid&, ::wxGridCellAttr&, ::wxDC&, const ::wxRect&, int, int, bool);

    sipVH__grid_1(sipGILState, 0, sipPySelf, sipMeth, grid, attr, dc, rect, row, col, isSelected);
}

::wxGridCellRenderer* sipwxGridCellRenderer::Clone() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[5]), const_cast<sipSimpleWrapper **>(&sipPySelf), sipName_GridCellRenderer, sipName_Clone);

    if (!sipMeth)
        return 0;

    extern ::wxGridCellRenderer* sipVH__grid_0(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__grid_0(sipGILState, 0, sipPySelf, sipMeth);
}


PyDoc_STRVAR(doc_wxGridCellRenderer_Clone, "Clone() -> GridCellRenderer\n"
"\n"
"This function must be implemented in derived classes to return a copy\n"
"of itself.");

extern "C" {static PyObject *meth_wxGridCellRenderer_Clone(PyObject *, PyObject *);}
static PyObject *meth_wxGridCellRenderer_Clone(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    PyObject *sipOrigSelf = sipSelf;

    {
        const ::wxGridCellRenderer *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxGridCellRenderer, &sipCpp))
        {
            ::wxGridCellRenderer*sipRes;

            if (!sipOrigSelf)
            {
                sipAbstractMethod(sipName_GridCellRenderer, sipName_Clone);
                return SIP_NULLPTR;
            }

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->Clone();
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxGridCellRenderer, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_GridCellRenderer, sipName_Clone, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGridCellRenderer_Draw, "Draw(grid, attr, dc, rect, row, col, isSelected) -> None\n"
"\n"
"Draw the given cell on the provided DC inside the given rectangle using the style specified by the attribute and the default or selected state corresponding to the isSelected value.");

extern "C" {static PyObject *meth_wxGridCellRenderer_Draw(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxGridCellRenderer_Draw(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxGrid* grid;
        ::wxGridCellAttr* attr;
        ::wxDC* dc;
        const ::wxRect* rect;
        int rectState = 0;
        int row;
        int col;
        bool isSelected;
        ::wxGridCellRenderer *sipCpp;

        static const char *sipKwdList[] = {
            sipName_grid,
            sipName_attr,
            sipName_dc,
            sipName_rect,
            sipName_row,
            sipName_col,
            sipName_isSelected,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ9J9J9J1iib", &sipSelf, sipType_wxGridCellRenderer, &sipCpp, sipType_wxGrid, &grid, sipType_wxGridCellAttr, &attr, sipType_wxDC, &dc, sipType_wxRect, &rect, &rectState, &row, &col, &isSelected))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            (sipSelfWasArg ? sipCpp->::wxGridCellRenderer::Draw(*grid, *attr, *dc, *rect, row, col, isSelected) : sipCpp->Draw(*grid, *attr, *dc, *rect, row, col, isSelected));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<::wxRect *>(rect), sipType_wxRect, rectState);

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_GridCellRenderer, sipName_Draw, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGridCellRenderer_GetBestSize, "GetBestSize(grid, attr, dc, row, col) -> wx.Size\n"
"\n"
"Get the preferred size of the cell for its contents.");

extern "C" {static PyObject *meth_wxGridCellRenderer_GetBestSize(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxGridCellRenderer_GetBestSize(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    PyObject *sipOrigSelf = sipSelf;

    {
        ::wxGrid* grid;
        ::wxGridCellAttr* attr;
        ::wxDC* dc;
        int row;
        int col;
        ::wxGridCellRenderer *sipCpp;

        static const char *sipKwdList[] = {
            sipName_grid,
            sipName_attr,
            sipName_dc,
            sipName_row,
            sipName_col,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ9J9J9ii", &sipSelf, sipType_wxGridCellRenderer, &sipCpp, sipType_wxGrid, &grid, sipType_wxGridCellAttr, &attr, sipType_wxDC, &dc, &row, &col))
        {
            ::wxSize*sipRes;

            if (!sipOrigSelf)
            {
                sipAbstractMethod(sipName_GridCellRenderer, sipName_GetBestSize);
                return SIP_NULLPTR;
            }

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxSize(sipCpp->GetBestSize(*grid, *attr, *dc, row, col));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxSize, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_GridCellRenderer, sipName_GetBestSize, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGridCellRenderer_GetBestHeight, "GetBestHeight(grid, attr, dc, row, col, width) -> int\n"
"\n"
"Get the preferred height of the cell at the given width.");

extern "C" {static PyObject *meth_wxGridCellRenderer_GetBestHeight(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxGridCellRenderer_GetBestHeight(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxGrid* grid;
        ::wxGridCellAttr* attr;
        ::wxDC* dc;
        int row;
        int col;
        int width;
        ::wxGridCellRenderer *sipCpp;

        static const char *sipKwdList[] = {
            sipName_grid,
            sipName_attr,
            sipName_dc,
            sipName_row,
            sipName_col,
            sipName_width,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ9J9J9iii", &sipSelf, sipType_wxGridCellRenderer, &sipCpp, sipType_wxGrid, &grid, sipType_wxGridCellAttr, &attr, sipType_wxDC, &dc, &row, &col, &width))
        {
            int sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxGridCellRenderer::GetBestHeight(*grid, *attr, *dc, row, col, width) : sipCpp->GetBestHeight(*grid, *attr, *dc, row, col, width));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyLong_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_GridCellRenderer, sipName_GetBestHeight, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGridCellRenderer_GetBestWidth, "GetBestWidth(grid, attr, dc, row, col, height) -> int\n"
"\n"
"Get the preferred width of the cell at the given height.");

extern "C" {static PyObject *meth_wxGridCellRenderer_GetBestWidth(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxGridCellRenderer_GetBestWidth(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxGrid* grid;
        ::wxGridCellAttr* attr;
        ::wxDC* dc;
        int row;
        int col;
        int height;
        ::wxGridCellRenderer *sipCpp;

        static const char *sipKwdList[] = {
            sipName_grid,
            sipName_attr,
            sipName_dc,
            sipName_row,
            sipName_col,
            sipName_height,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ9J9J9iii", &sipSelf, sipType_wxGridCellRenderer, &sipCpp, sipType_wxGrid, &grid, sipType_wxGridCellAttr, &attr, sipType_wxDC, &dc, &row, &col, &height))
        {
            int sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxGridCellRenderer::GetBestWidth(*grid, *attr, *dc, row, col, height) : sipCpp->GetBestWidth(*grid, *attr, *dc, row, col, height));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyLong_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_GridCellRenderer, sipName_GetBestWidth, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxGridCellRenderer_GetMaxBestSize, "GetMaxBestSize(grid, attr, dc) -> wx.Size\n"
"\n"
"Get the maximum possible size for a cell using this renderer, if\n"
"possible.");

extern "C" {static PyObject *meth_wxGridCellRenderer_GetMaxBestSize(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxGridCellRenderer_GetMaxBestSize(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxGrid* grid;
        ::wxGridCellAttr* attr;
        ::wxDC* dc;
        ::wxGridCellRenderer *sipCpp;

        static const char *sipKwdList[] = {
            sipName_grid,
            sipName_attr,
            sipName_dc,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ9J9J9", &sipSelf, sipType_wxGridCellRenderer, &sipCpp, sipType_wxGrid, &grid, sipType_wxGridCellAttr, &attr, sipType_wxDC, &dc))
        {
            ::wxSize*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxSize((sipSelfWasArg ? sipCpp->::wxGridCellRenderer::GetMaxBestSize(*grid, *attr, *dc) : sipCpp->GetMaxBestSize(*grid, *attr, *dc)));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxSize, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_GridCellRenderer, sipName_GetMaxBestSize, SIP_NULLPTR);

    return SIP_NULLPTR;
}


/* Cast a pointer to a type somewhere in its inheritance hierarchy. */
extern "C" {static void *cast_wxGridCellRenderer(void *, const sipTypeDef *);}
static void *cast_wxGridCellRenderer(void *sipCppV, const sipTypeDef *targetType)
{
    ::wxGridCellRenderer *sipCpp = reinterpret_cast<::wxGridCellRenderer *>(sipCppV);

    if (targetType == sipType_wxGridCellRenderer)
        return sipCppV;

    if (targetType == sipType_wxSharedClientDataContainer)
        return static_cast<::wxSharedClientDataContainer *>(sipCpp);

    if (targetType == sipType_wxRefCounter)
        return static_cast<::wxRefCounter *>(sipCpp);

    return SIP_NULLPTR;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxGridCellRenderer(void *, int);}
static void release_wxGridCellRenderer(void *sipCppV, int sipState)
{
    Py_BEGIN_ALLOW_THREADS

    if (sipState & SIP_DERIVED_CLASS)
        delete reinterpret_cast<sipwxGridCellRenderer *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void dealloc_wxGridCellRenderer(sipSimpleWrapper *);}
static void dealloc_wxGridCellRenderer(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerivedClass(sipSelf))
        reinterpret_cast<sipwxGridCellRenderer *>(sipGetAddress(sipSelf))->sipPySelf = SIP_NULLPTR;

    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxGridCellRenderer(sipGetAddress(sipSelf), sipIsDerivedClass(sipSelf));
    }
}


extern "C" {static void *init_type_wxGridCellRenderer(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxGridCellRenderer(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **sipOwner, PyObject **sipParseErr)
{
    sipwxGridCellRenderer *sipCpp = SIP_NULLPTR;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, SIP_NULLPTR, sipUnused, ""))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipwxGridCellRenderer();
            Py_END_ALLOW_THREADS

            *sipOwner = Py_None;

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
static sipEncodedTypeDef supers_wxGridCellRenderer[] = {{26, 0, 0}, {22, 0, 1}};


static PyMethodDef methods_wxGridCellRenderer[] = {
    {sipName_Clone, meth_wxGridCellRenderer_Clone, METH_VARARGS, doc_wxGridCellRenderer_Clone},
    {sipName_Draw, SIP_MLMETH_CAST(meth_wxGridCellRenderer_Draw), METH_VARARGS|METH_KEYWORDS, doc_wxGridCellRenderer_Draw},
    {sipName_GetBestHeight, SIP_MLMETH_CAST(meth_wxGridCellRenderer_GetBestHeight), METH_VARARGS|METH_KEYWORDS, doc_wxGridCellRenderer_GetBestHeight},
    {sipName_GetBestSize, SIP_MLMETH_CAST(meth_wxGridCellRenderer_GetBestSize), METH_VARARGS|METH_KEYWORDS, doc_wxGridCellRenderer_GetBestSize},
    {sipName_GetBestWidth, SIP_MLMETH_CAST(meth_wxGridCellRenderer_GetBestWidth), METH_VARARGS|METH_KEYWORDS, doc_wxGridCellRenderer_GetBestWidth},
    {sipName_GetMaxBestSize, SIP_MLMETH_CAST(meth_wxGridCellRenderer_GetMaxBestSize), METH_VARARGS|METH_KEYWORDS, doc_wxGridCellRenderer_GetMaxBestSize}
};

PyDoc_STRVAR(doc_wxGridCellRenderer, "GridCellRenderer() -> None\n"
"\n"
"This class is responsible for actually drawing the cell in the grid.");


sipClassTypeDef sipTypeDef__grid_wxGridCellRenderer = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_ABSTRACT|SIP_TYPE_CLASS,
        sipNameNr_wxGridCellRenderer,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_GridCellRenderer,
        {0, 0, 1},
        6, methods_wxGridCellRenderer,
        0, SIP_NULLPTR,
        0, SIP_NULLPTR,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxGridCellRenderer,
    -1,
    -1,
    supers_wxGridCellRenderer,
    SIP_NULLPTR,
    init_type_wxGridCellRenderer,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxGridCellRenderer,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    release_wxGridCellRenderer,
    cast_wxGridCellRenderer,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    sizeof (::wxGridCellRenderer),
};
