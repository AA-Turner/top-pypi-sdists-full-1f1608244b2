# if CYTHON_COMPILING_IN_CPYTHON
static int
__Pyx_unicode_modifiable(PyObject *unicode)
{
    if (Py_REFCNT(unicode) != 1)
        return 0;
    if (!PyUnicode_CheckExact(unicode))
        return 0;
    if (PyUnicode_CHECK_INTERNED(unicode))
        return 0;
    return 1;
}
static CYTHON_INLINE PyObject *__Pyx_PyUnicode_ConcatInPlaceImpl(PyObject **p_left, PyObject *right
        #if CYTHON_REFNANNY
        , void* __pyx_refnanny
        #endif
    ) {
    PyObject *left = *p_left;
    Py_ssize_t left_len, right_len, new_len;
    if (unlikely(__Pyx_PyUnicode_READY(left) == -1))
        return NULL;
    if (unlikely(__Pyx_PyUnicode_READY(right) == -1))
        return NULL;
    left_len = PyUnicode_GET_LENGTH(left);
    if (left_len == 0) {
        Py_INCREF(right);
        return right;
    }
    right_len = PyUnicode_GET_LENGTH(right);
    if (right_len == 0) {
        Py_INCREF(left);
        return left;
    }
    if (unlikely(left_len > PY_SSIZE_T_MAX - right_len)) {
        PyErr_SetString(PyExc_OverflowError,
                        "strings are too large to concat");
        return NULL;
    }
    new_len = left_len + right_len;
    if (__Pyx_unicode_modifiable(left)
            && PyUnicode_CheckExact(right)
            && PyUnicode_KIND(right) <= PyUnicode_KIND(left)
            && !(PyUnicode_IS_ASCII(left) && !PyUnicode_IS_ASCII(right))) {
        int ret;
        __Pyx_GIVEREF(*p_left);
        ret = PyUnicode_Resize(p_left, new_len);
        __Pyx_GOTREF(*p_left);
        if (unlikely(ret != 0))
            return NULL;
        #if PY_VERSION_HEX >= 0x030d0000
        if (unlikely(PyUnicode_CopyCharacters(*p_left, left_len, right, 0, right_len) < 0)) return NULL;
        #else
        _PyUnicode_FastCopyCharacters(*p_left, left_len, right, 0, right_len);
        #endif
        __Pyx_INCREF(*p_left);
        __Pyx_GIVEREF(*p_left);
        return *p_left;
    } else {
        return __Pyx_PyUnicode_Concat(left, right);
    }
  }
#endif

