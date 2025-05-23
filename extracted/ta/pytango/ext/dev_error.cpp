/*
 * SPDX-FileCopyrightText: All Contributors to the PyTango project
 *
 * SPDX-License-Identifier: LGPL-3.0-or-later
 */

#include "precompiled_header.hpp"
#include <tango/tango.h>
#include "pyutils.h"

namespace PyDevError
{
static void from_str_to_char(PyObject *in, CORBA::String_member &out)
{
    if(PyUnicode_Check(in))
    {
        PyObject *bytes_in = EncodeAsLatin1(in);
        out = CORBA::string_dup(PyBytes_AsString(bytes_in));
        Py_DECREF(bytes_in);
    }
    else
    {
        out = CORBA::string_dup(PyBytes_AsString(in));
    }
}

static inline PyObject *get_reason(Tango::DevError &self)
{
    return from_char_to_python_str(self.reason);
}

static inline void set_reason(Tango::DevError &self, PyObject *str)
{
    PyDevError::from_str_to_char(str, self.reason);
}

static inline PyObject *get_desc(Tango::DevError &self)
{
    return from_char_to_python_str(self.desc);
}

static inline void set_desc(Tango::DevError &self, PyObject *str)
{
    PyDevError::from_str_to_char(str, self.desc);
}

static inline PyObject *get_origin(Tango::DevError &self)
{
    return from_char_to_python_str(self.origin);
}

static inline void set_origin(Tango::DevError &self, PyObject *str)
{
    PyDevError::from_str_to_char(str, self.origin);
}
}; // namespace PyDevError

void export_dev_error()
{
    bopy::class_<Tango::DevError>("DevError")
        .enable_pickling()
        .add_property("reason", &PyDevError::get_reason, &PyDevError::set_reason)
        .def_readwrite("severity", &Tango::DevError::severity)
        .add_property("desc", &PyDevError::get_desc, &PyDevError::set_desc)
        .add_property("origin", &PyDevError::get_origin, &PyDevError::set_origin);
}
