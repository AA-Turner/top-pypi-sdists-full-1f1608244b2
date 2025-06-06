// SPDX-FileCopyrightText: 2022 The meson-python developers
//
// SPDX-License-Identifier: MIT

#include <Python.h>

#include "examplelib.h"
#include "examplelib2.h"

static PyObject* example_sum(PyObject* self, PyObject *args)
{
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;
    }

    long result = sum(a, b);

    return PyLong_FromLong(result);
}

static PyObject* example_prod(PyObject* self, PyObject *args)
{
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;
    }

    long result = prod(a, b);

    return PyLong_FromLong(result);
}

static PyMethodDef methods[] = {
    {"example_prod", (PyCFunction)example_prod, METH_VARARGS, NULL},
    {"example_sum", (PyCFunction)example_sum, METH_VARARGS, NULL},
    {NULL, NULL, 0, NULL},
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "_example",
    NULL,
    -1,
    methods,
};

PyMODINIT_FUNC PyInit__example(void)
{
    return PyModule_Create(&module);
}
