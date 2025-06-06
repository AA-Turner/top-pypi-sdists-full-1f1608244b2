/*
 * SPDX-FileCopyrightText: All Contributors to the PyTango project
 *
 * SPDX-License-Identifier: LGPL-3.0-or-later
 */

#pragma once

#include <boost/python.hpp>
#include <tango/tango.h>

/**
 * Translates a seq<DevError> into a C++ DevErrorList
 *
 * @param [in] seq a python sequence of DevError
 * @param [out] err_list the object to be filled with the several DevError
 */
void sequencePyDevError_2_DevErrorList(PyObject *seq, Tango::DevErrorList &err_list);

/**
 * Translates a python DevFailed or a seq<DevError> into a C++ DevFailed
 *
 * @param [in] obj a python sequence of DevError or a DevFailed
 * @param [out] df the object to be filled with the information extracted from obj
 */
void PyDevFailed_2_DevFailed(PyObject *obj, Tango::DevFailed &df);

/**
 * Throws the current python exception. Assumes the python err is set and contains
 * a DevFailed exception
 */
void throw_python_dev_failed();

/**
 * Transforms a python exception into a Tango::DevFailed
 */
Tango::DevFailed to_dev_failed(PyObject *type = NULL, PyObject *value = NULL, PyObject *traceback = NULL);

/**
 * Throws the current python exception as a DevFailed exception.
 */
void throw_python_generic_exception(PyObject *type = NULL, PyObject *value = NULL, PyObject *traceback = NULL);

/**
 * Handles the current python exception:
 * If a PyTango DevFaild -> translates it to C++ and throws the DevFailed
 * If a generic python exception -> translates it to C++ DevFailed and throws the DevFailed
 *
 * @param[in] eas the boost python exception description (currently not used)
 */
void handle_python_exception(bopy::error_already_set &eas,
                             const std::string &reason = "",
                             const std::string &desc = "",
                             const std::string &origin = "");

#define SAFE_CATCH_REPORT(meth_name)                                                                         \
    catch(bopy::error_already_set &)                                                                         \
    {                                                                                                        \
        std::cerr << "PyTango generated an unexpected python exception in " << meth_name << "." << std::endl \
                  << "Please report this bug to PyTango with the following report:" << std::endl;            \
        PyErr_Print();                                                                                       \
    }                                                                                                        \
    catch(Tango::DevFailed & df)                                                                             \
    {                                                                                                        \
        std::cerr << "PyTango generated a DevFailed exception in " << meth_name << "." << std::endl          \
                  << "Please report this bug to PyTango with the following report:" << std::endl;            \
        Tango::Except::print_exception(df);                                                                  \
    }                                                                                                        \
    catch(...)                                                                                               \
    {                                                                                                        \
        std::cerr << "PyTango generated an unknown exception in " << meth_name << "." << std::endl           \
                  << "Please report this bug to PyTango." << std::endl;                                      \
    }

#define SAFE_CATCH_INFORM(meth_name)                                                            \
    catch(bopy::error_already_set &)                                                            \
    {                                                                                           \
        std::cerr << meth_name << " generated the following python exception:" << std::endl;    \
        PyErr_Print();                                                                          \
    }                                                                                           \
    catch(Tango::DevFailed & df)                                                                \
    {                                                                                           \
        std::cerr << meth_name << " generated the following DevFailed exception:" << std::endl; \
        Tango::Except::print_exception(df);                                                     \
    }                                                                                           \
    catch(...)                                                                                  \
    {                                                                                           \
        std::cerr << meth_name << " generated an unknown exception." << std::endl;              \
    }
