/*
 * Interface wrapper code.
 *
 * Generated by SIP 6.10.0
 *
 *     Copyright: (c) 2020 by Total Control Software
 *     License:   wxWindows License
 */

#include "sipAPI_core.h"
        #include <wx/dataobj.h>
        #include <wx/bitmap.h>
        #include <wx/dataobj.h>
        #include <wx/dataobj.h>
    PyObject* _wxBitmapDataObject_GetAllFormats(const wxBitmapDataObject* self, wxDataObject::Direction dir)
    {
        size_t count = self->GetFormatCount(dir);
        wxDataFormat* formats = new wxDataFormat[count];
        self->GetAllFormats(formats, dir);
        wxPyThreadBlocker blocker;
        PyObject* list = PyList_New(count);
        for (size_t i=0; i<count; i++) {
            wxDataFormat* format = new wxDataFormat(formats[i]);
            PyObject* obj = wxPyConstructObject((void*)format, wxT("wxDataFormat"), true);
            PyList_SET_ITEM(list, i, obj); // PyList_SET_ITEM steals a reference
        }
        delete [] formats;
        return list;
    }
    bool _wxBitmapDataObject_SetData(wxBitmapDataObject* self, const wxDataFormat* format, wxPyBuffer* buf)
    {
        return self->SetData(*format, buf->m_len, buf->m_ptr);
    }


class sipwxBitmapDataObject : public ::wxBitmapDataObject
{
public:
    sipwxBitmapDataObject(const ::wxBitmap&);
    virtual ~sipwxBitmapDataObject();

    /*
     * There is a protected method for every virtual method visible from
     * this class.
     */
protected:
    void SetBitmap(const ::wxBitmap&) SIP_OVERRIDE;
    ::wxBitmap GetBitmap() const SIP_OVERRIDE;
    bool SetData(const ::wxDataFormat&, size_t, const void*) SIP_OVERRIDE;
    ::wxDataFormat GetPreferredFormat(::wxDataObject::Direction) const SIP_OVERRIDE;
    size_t GetFormatCount(::wxDataObject::Direction) const SIP_OVERRIDE;
    void GetAllFormats(::wxDataFormat*, ::wxDataObject::Direction) const SIP_OVERRIDE;
    bool GetDataHere(void*) const SIP_OVERRIDE;
    size_t GetDataSize() const SIP_OVERRIDE;
    bool SetData(size_t, const void*) SIP_OVERRIDE;

public:
    sipSimpleWrapper *sipPySelf;

private:
    sipwxBitmapDataObject(const sipwxBitmapDataObject &);
    sipwxBitmapDataObject &operator = (const sipwxBitmapDataObject &);

    char sipPyMethods[9];
};

sipwxBitmapDataObject::sipwxBitmapDataObject(const ::wxBitmap& bitmap): ::wxBitmapDataObject(bitmap), sipPySelf(SIP_NULLPTR)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipwxBitmapDataObject::~sipwxBitmapDataObject()
{
    sipInstanceDestroyedEx(&sipPySelf);
}

void sipwxBitmapDataObject::SetBitmap(const ::wxBitmap& bitmap)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[0], &sipPySelf, SIP_NULLPTR, sipName_SetBitmap);

    if (!sipMeth)
    {
        ::wxBitmapDataObject::SetBitmap(bitmap);
        return;
    }

    extern void sipVH__core_81(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, const ::wxBitmap&);

    sipVH__core_81(sipGILState, 0, sipPySelf, sipMeth, bitmap);
}

::wxBitmap sipwxBitmapDataObject::GetBitmap() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[1]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_GetBitmap);

    if (!sipMeth)
        return ::wxBitmapDataObject::GetBitmap();

    extern ::wxBitmap sipVH__core_80(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__core_80(sipGILState, 0, sipPySelf, sipMeth);
}

bool sipwxBitmapDataObject::SetData(const ::wxDataFormat& format, size_t len, const void*buf)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[2], &sipPySelf, SIP_NULLPTR, sipName_SetData);

    if (!sipMeth)
        return ::wxBitmapDataObject::SetData(format, len, buf);

    extern bool sipVH__core_79(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, const ::wxDataFormat&, size_t, const void*);

    return sipVH__core_79(sipGILState, 0, sipPySelf, sipMeth, format, len, buf);
}

::wxDataFormat sipwxBitmapDataObject::GetPreferredFormat(::wxDataObject::Direction dir) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[3]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_GetPreferredFormat);

    if (!sipMeth)
        return ::wxBitmapDataObject::GetPreferredFormat(dir);

    extern ::wxDataFormat sipVH__core_69(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxDataObject::Direction);

    return sipVH__core_69(sipGILState, 0, sipPySelf, sipMeth, dir);
}

size_t sipwxBitmapDataObject::GetFormatCount(::wxDataObject::Direction dir) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[4]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_GetFormatCount);

    if (!sipMeth)
        return ::wxBitmapDataObject::GetFormatCount(dir);

    extern size_t sipVH__core_68(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxDataObject::Direction);

    return sipVH__core_68(sipGILState, 0, sipPySelf, sipMeth, dir);
}

void sipwxBitmapDataObject::GetAllFormats(::wxDataFormat*formats, ::wxDataObject::Direction dir) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[5]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_GetAllFormats);

    if (!sipMeth)
    {
        ::wxBitmapDataObject::GetAllFormats(formats, dir);
        return;
    }

    extern void sipVH__core_65(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, ::wxDataFormat*, ::wxDataObject::Direction);

    sipVH__core_65(sipGILState, 0, sipPySelf, sipMeth, formats, dir);
}

bool sipwxBitmapDataObject::GetDataHere(void*buf) const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[6]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_GetDataHere);

    if (!sipMeth)
        return ::wxBitmapDataObject::GetDataHere(buf);

    extern bool sipVH__core_77(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, void*);

    return sipVH__core_77(sipGILState, 0, sipPySelf, sipMeth, buf);
}

size_t sipwxBitmapDataObject::GetDataSize() const
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, const_cast<char *>(&sipPyMethods[7]), const_cast<sipSimpleWrapper **>(&sipPySelf), SIP_NULLPTR, sipName_GetDataSize);

    if (!sipMeth)
        return ::wxBitmapDataObject::GetDataSize();

    extern size_t sipVH__core_74(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *);

    return sipVH__core_74(sipGILState, 0, sipPySelf, sipMeth);
}

bool sipwxBitmapDataObject::SetData(size_t len, const void*buf)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState, &sipPyMethods[8], &sipPySelf, SIP_NULLPTR, sipName_SetData);

    if (!sipMeth)
        return ::wxBitmapDataObject::SetData(len, buf);

    extern bool sipVH__core_76(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, size_t, const void*);

    return sipVH__core_76(sipGILState, 0, sipPySelf, sipMeth, len, buf);
}


PyDoc_STRVAR(doc_wxBitmapDataObject_GetBitmap, "GetBitmap() -> Bitmap\n"
"\n"
"Returns the bitmap associated with the data object.");

extern "C" {static PyObject *meth_wxBitmapDataObject_GetBitmap(PyObject *, PyObject *);}
static PyObject *meth_wxBitmapDataObject_GetBitmap(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const ::wxBitmapDataObject *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxBitmapDataObject, &sipCpp))
        {
            ::wxBitmap*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxBitmap((sipSelfWasArg ? sipCpp->::wxBitmapDataObject::GetBitmap() : sipCpp->GetBitmap()));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxBitmap, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_BitmapDataObject, sipName_GetBitmap, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxBitmapDataObject_SetBitmap, "SetBitmap(bitmap) -> None\n"
"\n"
"Sets the bitmap associated with the data object.");

extern "C" {static PyObject *meth_wxBitmapDataObject_SetBitmap(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxBitmapDataObject_SetBitmap(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const ::wxBitmap* bitmap;
        ::wxBitmapDataObject *sipCpp;

        static const char *sipKwdList[] = {
            sipName_bitmap,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ9", &sipSelf, sipType_wxBitmapDataObject, &sipCpp, sipType_wxBitmap, &bitmap))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            (sipSelfWasArg ? sipCpp->::wxBitmapDataObject::SetBitmap(*bitmap) : sipCpp->SetBitmap(*bitmap));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    sipNoMethod(sipParseErr, sipName_BitmapDataObject, sipName_SetBitmap, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxBitmapDataObject_GetAllFormats, "GetAllFormats(dir=DataObject.Get)\n"
"\n"
"Returns a list of wx.DataFormat objects which this data object\n"
"supports transferring in the given direction.");

extern "C" {static PyObject *meth_wxBitmapDataObject_GetAllFormats(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxBitmapDataObject_GetAllFormats(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxDataObject::Direction dir = wxDataObject::Get;
        const ::wxBitmapDataObject *sipCpp;

        static const char *sipKwdList[] = {
            sipName_dir,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "B|E", &sipSelf, sipType_wxBitmapDataObject, &sipCpp, sipType_wxDataObject_Direction, &dir))
        {
            PyObject * sipRes = SIP_NULLPTR;
            int sipIsErr = 0;
        PyErr_Clear();
        Py_BEGIN_ALLOW_THREADS
        sipRes = _wxBitmapDataObject_GetAllFormats(sipCpp, dir);
        Py_END_ALLOW_THREADS
        if (PyErr_Occurred()) sipIsErr = 1;

            if (sipIsErr)
                return 0;

            return sipRes;
        }
    }

    sipNoMethod(sipParseErr, sipName_BitmapDataObject, sipName_GetAllFormats, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxBitmapDataObject_SetData, "SetData(format, buf) -> bool\n"
"");

extern "C" {static PyObject *meth_wxBitmapDataObject_SetData(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxBitmapDataObject_SetData(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const ::wxDataFormat* format;
        ::wxPyBuffer* buf;
        int bufState = 0;
        ::wxBitmapDataObject *sipCpp;

        static const char *sipKwdList[] = {
            sipName_format,
            sipName_buf,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "BJ9J0", &sipSelf, sipType_wxBitmapDataObject, &sipCpp, sipType_wxDataFormat, &format, sipType_wxPyBuffer, &buf, &bufState))
        {
            bool sipRes = 0;
            int sipIsErr = 0;
        PyErr_Clear();
        Py_BEGIN_ALLOW_THREADS
        sipRes = _wxBitmapDataObject_SetData(sipCpp, format, buf);
        Py_END_ALLOW_THREADS
        if (PyErr_Occurred()) sipIsErr = 1;
            sipReleaseType(buf, sipType_wxPyBuffer, bufState);

            if (sipIsErr)
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    {
        size_t len;
        const void* buf;
        ::wxBitmapDataObject *sipCpp;

        static const char *sipKwdList[] = {
            sipName_len,
            sipName_buf,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "B=v", &sipSelf, sipType_wxBitmapDataObject, &sipCpp, &len, &buf))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxBitmapDataObject::SetData(len, buf) : sipCpp->SetData(len, buf));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_BitmapDataObject, sipName_SetData, SIP_NULLPTR);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxBitmapDataObject_GetFormatCount, "GetFormatCount(self, dir: DataObject.Direction = wxDataObject.Get) -> int");

extern "C" {static PyObject *meth_wxBitmapDataObject_GetFormatCount(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxBitmapDataObject_GetFormatCount(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxDataObject::Direction dir = ::wxDataObject::Get;
        const ::wxBitmapDataObject *sipCpp;

        static const char *sipKwdList[] = {
            sipName_dir,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "B|E", &sipSelf, sipType_wxBitmapDataObject, &sipCpp, sipType_wxDataObject_Direction, &dir))
        {
            size_t sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxBitmapDataObject::GetFormatCount(dir) : sipCpp->GetFormatCount(dir));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyLong_FromUnsignedLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_BitmapDataObject, sipName_GetFormatCount, doc_wxBitmapDataObject_GetFormatCount);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxBitmapDataObject_GetPreferredFormat, "GetPreferredFormat(self, dir: DataObject.Direction = wxDataObject.Get) -> DataFormat");

extern "C" {static PyObject *meth_wxBitmapDataObject_GetPreferredFormat(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxBitmapDataObject_GetPreferredFormat(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        ::wxDataObject::Direction dir = ::wxDataObject::Get;
        const ::wxBitmapDataObject *sipCpp;

        static const char *sipKwdList[] = {
            sipName_dir,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "B|E", &sipSelf, sipType_wxBitmapDataObject, &sipCpp, sipType_wxDataObject_Direction, &dir))
        {
            ::wxDataFormat*sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = new ::wxDataFormat((sipSelfWasArg ? sipCpp->::wxBitmapDataObject::GetPreferredFormat(dir) : sipCpp->GetPreferredFormat(dir)));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return sipConvertFromNewType(sipRes, sipType_wxDataFormat, SIP_NULLPTR);
        }
    }

    sipNoMethod(sipParseErr, sipName_BitmapDataObject, sipName_GetPreferredFormat, doc_wxBitmapDataObject_GetPreferredFormat);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxBitmapDataObject_GetDataSize, "GetDataSize(self) -> int");

extern "C" {static PyObject *meth_wxBitmapDataObject_GetDataSize(PyObject *, PyObject *);}
static PyObject *meth_wxBitmapDataObject_GetDataSize(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        const ::wxBitmapDataObject *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_wxBitmapDataObject, &sipCpp))
        {
            size_t sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxBitmapDataObject::GetDataSize() : sipCpp->GetDataSize());
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyLong_FromUnsignedLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_BitmapDataObject, sipName_GetDataSize, doc_wxBitmapDataObject_GetDataSize);

    return SIP_NULLPTR;
}


PyDoc_STRVAR(doc_wxBitmapDataObject_GetDataHere, "GetDataHere(self, buf: Optional[wx.siplib.voidptr]) -> bool");

extern "C" {static PyObject *meth_wxBitmapDataObject_GetDataHere(PyObject *, PyObject *, PyObject *);}
static PyObject *meth_wxBitmapDataObject_GetDataHere(PyObject *sipSelf, PyObject *sipArgs, PyObject *sipKwds)
{
    PyObject *sipParseErr = SIP_NULLPTR;
    bool sipSelfWasArg = (!sipSelf || sipIsDerivedClass((sipSimpleWrapper *)sipSelf));

    {
        void* buf;
        const ::wxBitmapDataObject *sipCpp;

        static const char *sipKwdList[] = {
            sipName_buf,
        };

        if (sipParseKwdArgs(&sipParseErr, sipArgs, sipKwds, sipKwdList, SIP_NULLPTR, "Bv", &sipSelf, sipType_wxBitmapDataObject, &sipCpp, &buf))
        {
            bool sipRes;

            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->::wxBitmapDataObject::GetDataHere(buf) : sipCpp->GetDataHere(buf));
            Py_END_ALLOW_THREADS

            if (PyErr_Occurred())
                return 0;

            return PyBool_FromLong(sipRes);
        }
    }

    sipNoMethod(sipParseErr, sipName_BitmapDataObject, sipName_GetDataHere, doc_wxBitmapDataObject_GetDataHere);

    return SIP_NULLPTR;
}


/* Cast a pointer to a type somewhere in its inheritance hierarchy. */
extern "C" {static void *cast_wxBitmapDataObject(void *, const sipTypeDef *);}
static void *cast_wxBitmapDataObject(void *sipCppV, const sipTypeDef *targetType)
{
    ::wxBitmapDataObject *sipCpp = reinterpret_cast<::wxBitmapDataObject *>(sipCppV);

    if (targetType == sipType_wxBitmapDataObject)
        return sipCppV;

    sipCppV = ((const sipClassTypeDef *)sipType_wxDataObjectSimple)->ctd_cast(static_cast<::wxDataObjectSimple *>(sipCpp), targetType);
    if (sipCppV)
        return sipCppV;

    return SIP_NULLPTR;
}


/* Call the instance's destructor. */
extern "C" {static void release_wxBitmapDataObject(void *, int);}
static void release_wxBitmapDataObject(void *sipCppV, int sipState)
{
    Py_BEGIN_ALLOW_THREADS

    if (sipState & SIP_DERIVED_CLASS)
        delete reinterpret_cast<sipwxBitmapDataObject *>(sipCppV);
    else
        delete reinterpret_cast<::wxBitmapDataObject *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void *array_wxBitmapDataObject(Py_ssize_t);}
static void *array_wxBitmapDataObject(Py_ssize_t sipNrElem)
{
    return new ::wxBitmapDataObject[sipNrElem];
}


extern "C" {static void array_delete_wxBitmapDataObject(void *);}
static void array_delete_wxBitmapDataObject(void *sipCpp)
{
    delete[] reinterpret_cast<::wxBitmapDataObject *>(sipCpp);
}


extern "C" {static void dealloc_wxBitmapDataObject(sipSimpleWrapper *);}
static void dealloc_wxBitmapDataObject(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerivedClass(sipSelf))
        reinterpret_cast<sipwxBitmapDataObject *>(sipGetAddress(sipSelf))->sipPySelf = SIP_NULLPTR;

    if (sipIsOwnedByPython(sipSelf))
    {
        release_wxBitmapDataObject(sipGetAddress(sipSelf), sipIsDerivedClass(sipSelf));
    }
}


extern "C" {static void *init_type_wxBitmapDataObject(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_wxBitmapDataObject(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    sipwxBitmapDataObject *sipCpp = SIP_NULLPTR;

    {
        const ::wxBitmap& bitmapdef = wxNullBitmap;
        const ::wxBitmap* bitmap = &bitmapdef;

        static const char *sipKwdList[] = {
            sipName_bitmap,
        };

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, sipKwdList, sipUnused, "|J9", sipType_wxBitmap, &bitmap))
        {
            PyErr_Clear();

            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipwxBitmapDataObject(*bitmap);
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


/* Define this type's super-types. */
static sipEncodedTypeDef supers_wxBitmapDataObject[] = {{117, 255, 1}};


static PyMethodDef methods_wxBitmapDataObject[] = {
    {sipName_GetAllFormats, SIP_MLMETH_CAST(meth_wxBitmapDataObject_GetAllFormats), METH_VARARGS|METH_KEYWORDS, doc_wxBitmapDataObject_GetAllFormats},
    {sipName_GetBitmap, meth_wxBitmapDataObject_GetBitmap, METH_VARARGS, doc_wxBitmapDataObject_GetBitmap},
    {sipName_GetDataHere, SIP_MLMETH_CAST(meth_wxBitmapDataObject_GetDataHere), METH_VARARGS|METH_KEYWORDS, doc_wxBitmapDataObject_GetDataHere},
    {sipName_GetDataSize, meth_wxBitmapDataObject_GetDataSize, METH_VARARGS, doc_wxBitmapDataObject_GetDataSize},
    {sipName_GetFormatCount, SIP_MLMETH_CAST(meth_wxBitmapDataObject_GetFormatCount), METH_VARARGS|METH_KEYWORDS, doc_wxBitmapDataObject_GetFormatCount},
    {sipName_GetPreferredFormat, SIP_MLMETH_CAST(meth_wxBitmapDataObject_GetPreferredFormat), METH_VARARGS|METH_KEYWORDS, doc_wxBitmapDataObject_GetPreferredFormat},
    {sipName_SetBitmap, SIP_MLMETH_CAST(meth_wxBitmapDataObject_SetBitmap), METH_VARARGS|METH_KEYWORDS, doc_wxBitmapDataObject_SetBitmap},
    {sipName_SetData, SIP_MLMETH_CAST(meth_wxBitmapDataObject_SetData), METH_VARARGS|METH_KEYWORDS, doc_wxBitmapDataObject_SetData}
};

sipVariableDef variables_wxBitmapDataObject[] = {
    {PropertyVariable, sipName_Bitmap, &methods_wxBitmapDataObject[1], &methods_wxBitmapDataObject[6], SIP_NULLPTR, SIP_NULLPTR},
    {PropertyVariable, sipName_AllFormats, &methods_wxBitmapDataObject[0], SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
};

PyDoc_STRVAR(doc_wxBitmapDataObject, "BitmapDataObject(bitmap=NullBitmap) -> None\n"
"\n"
"wxBitmapDataObject is a specialization of wxDataObject for bitmap\n"
"data.");


sipClassTypeDef sipTypeDef__core_wxBitmapDataObject = {
    {
        -1,
        SIP_NULLPTR,
        SIP_NULLPTR,
        SIP_TYPE_CLASS,
        sipNameNr_wxBitmapDataObject,
        SIP_NULLPTR,
        SIP_NULLPTR,
    },
    {
        sipNameNr_BitmapDataObject,
        {0, 0, 1},
        8, methods_wxBitmapDataObject,
        0, SIP_NULLPTR,
        2, variables_wxBitmapDataObject,
        {SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR, SIP_NULLPTR},
    },
    doc_wxBitmapDataObject,
    -1,
    -1,
    supers_wxBitmapDataObject,
    SIP_NULLPTR,
    init_type_wxBitmapDataObject,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    dealloc_wxBitmapDataObject,
    SIP_NULLPTR,
    array_wxBitmapDataObject,
    SIP_NULLPTR,
    release_wxBitmapDataObject,
    cast_wxBitmapDataObject,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    SIP_NULLPTR,
    array_delete_wxBitmapDataObject,
    sizeof (::wxBitmapDataObject),
};
