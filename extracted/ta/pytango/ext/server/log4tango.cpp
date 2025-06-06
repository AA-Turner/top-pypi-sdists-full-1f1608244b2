/*
 * SPDX-FileCopyrightText: All Contributors to the PyTango project
 *
 * SPDX-License-Identifier: LGPL-3.0-or-later
 */

#include "precompiled_header.hpp"
#include "defs.h"
#include "pytgutils.h"

extern const char *param_must_be_seq;
extern const char *non_string_seq;

// cppTango Logger API has changed between 9.3 and 9.4 to support source code
// location information (filename and line number). On PyTango side we always
// require this information from the caller and pass it to cppTango if it has
// the new signature.
typedef void (log4tango::Logger::*StringOnlyLogSignature)(const std::string &);
typedef void (log4tango::Logger::*StringAndLocationLogSignature)(const std::string &, int, const std::string &);

typedef void (log4tango::Logger::*StringOnlyWithLevelLogSignature)(log4tango::Level::Value, const std::string &);

typedef void (log4tango::Logger::*StringAndLocationWithLevelLogSignature)(const std::string &,
                                                                          int,
                                                                          log4tango::Level::Value,
                                                                          const std::string &);

template <StringOnlyLogSignature ptr>
static void call_logger(log4tango::Logger &logger, const std::string & /*file*/, int /*line*/, const std::string &msg)
{
    return (logger.*ptr)(msg);
}

template <StringAndLocationLogSignature ptr>
static void call_logger(log4tango::Logger &logger, const std::string &file, int line, const std::string &msg)
{
    return (logger.*ptr)(file, line, msg);
}

template <StringOnlyWithLevelLogSignature ptr>
static void call_logger(log4tango::Logger &logger,
                        const std::string & /*file*/,
                        int /*line*/,
                        log4tango::Level::Value level,
                        const std::string &msg)
{
    return (logger.*ptr)(level, msg);
}

template <StringAndLocationWithLevelLogSignature ptr>
static void call_logger(
    log4tango::Logger &logger, const std::string &file, int line, log4tango::Level::Value level, const std::string &msg)
{
    return (logger.*ptr)(file, line, level, msg);
}

namespace PyLogging
{
void add_logging_target(bopy::object &obj)
{
    PyObject *obj_ptr = obj.ptr();
    if(PySequence_Check(obj_ptr) == 0)
    {
        raise_(PyExc_TypeError, param_must_be_seq);
    }

    Tango::DevVarStringArray par;
    int len = (int) PySequence_Length(obj_ptr);
    par.length(len);
    for(int i = 0; i < len; ++i)
    {
        PyObject *item_ptr = PySequence_GetItem(obj_ptr, i);
        bopy::str item = bopy::str(bopy::handle<>(item_ptr));
        par[i] = CORBA::string_dup(bopy::extract<const char *>(item));
    }
    Tango::Logging::add_logging_target(&par);
}

void remove_logging_target(bopy::object &obj)
{
    PyObject *obj_ptr = obj.ptr();
    if(PySequence_Check(obj_ptr) == 0)
    {
        raise_(PyExc_TypeError, param_must_be_seq);
    }

    Tango::DevVarStringArray par;
    int len = (int) PySequence_Length(obj_ptr);
    par.length(len);
    for(int i = 0; i < len; ++i)
    {
        PyObject *item_ptr = PySequence_GetItem(obj_ptr, i);
        bopy::str item = bopy::str(bopy::handle<>(item_ptr));
        par[i] = CORBA::string_dup(bopy::extract<const char *>(item));
    }
    Tango::Logging::remove_logging_target(&par);
}
} // namespace PyLogging

void export_log4tango()
{
    {
        bopy::scope level_scope =
            bopy::class_<log4tango::Level, boost::noncopyable>("Level", bopy::no_init)

                .def("get_name", &log4tango::Level::get_name, bopy::return_value_policy<bopy::copy_const_reference>())
                .def("get_value", &log4tango::Level::get_value)
                .staticmethod("get_name")
                .staticmethod("get_value");

        bopy::enum_<log4tango::Level::LevelLevel>("LevelLevel")
            .value("OFF", log4tango::Level::OFF)
            .value("FATAL", log4tango::Level::FATAL)
            .value("ERROR", log4tango::Level::ERROR)
            .value("WARN", log4tango::Level::WARN)
            .value("INFO", log4tango::Level::INFO)
            .value("DEBUG", log4tango::Level::DEBUG);
    }

    bopy::class_<log4tango::Logger, boost::noncopyable>(
        "Logger", bopy::init<const std::string &, bopy::optional<log4tango::Level::Value>>())

        .def("get_name", &log4tango::Logger::get_name, bopy::return_value_policy<bopy::copy_const_reference>())
        .def("set_level", &log4tango::Logger::set_level)
        .def("get_level", &log4tango::Logger::get_level)
        .def("is_level_enabled", &log4tango::Logger::is_level_enabled)
        .def("__log", &call_logger<&log4tango::Logger::log>)
        .def("__log_unconditionally", &call_logger<&log4tango::Logger::log_unconditionally>)
        .def("__debug", &call_logger<&log4tango::Logger::debug>)
        .def("__info", &call_logger<&log4tango::Logger::info>)
        .def("__warn", &call_logger<&log4tango::Logger::warn>)
        .def("__error", &call_logger<&log4tango::Logger::error>)
        .def("__fatal", &call_logger<&log4tango::Logger::fatal>)
        .def("is_debug_enabled", &log4tango::Logger::is_debug_enabled)
        .def("is_info_enabled", &log4tango::Logger::is_info_enabled)
        .def("is_warn_enabled", &log4tango::Logger::is_warn_enabled)
        .def("is_error_enabled", &log4tango::Logger::is_error_enabled)
        .def("is_fatal_enabled", &log4tango::Logger::is_fatal_enabled);

    bopy::class_<Tango::Logging, boost::noncopyable>("Logging", bopy::no_init)
        .def("get_core_logger",
             &Tango::Logging::get_core_logger,
             bopy::return_value_policy<bopy::reference_existing_object>())
        .def("add_logging_target", &PyLogging::add_logging_target)
        .def("remove_logging_target", &PyLogging::remove_logging_target)
        .def("start_logging", &Tango::Logging::start_logging)
        .def("stop_logging", &Tango::Logging::stop_logging)
        .staticmethod("get_core_logger")
        .staticmethod("add_logging_target")
        .staticmethod("remove_logging_target")
        .staticmethod("start_logging")
        .staticmethod("stop_logging");
}
