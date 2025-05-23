/*
 * SPDX-FileCopyrightText: All Contributors to the PyTango project
 *
 * SPDX-License-Identifier: LGPL-3.0-or-later
 */

#include "precompiled_header.hpp"
#include "pytgutils.h"
#include "exception.h"
#include "server/device_class.h"
#include "server/attr.h"
#include "server/command.h"
#include "server/pipe.h"

#define __AUX_DECL_CALL_DEVCLASS_METHOD AutoPythonGIL __py_lock;

#define __AUX_CATCH_PY_EXCEPTION         \
    catch(bopy::error_already_set & eas) \
    {                                    \
        handle_python_exception(eas);    \
    }

#define CALL_DEVCLASS_METHOD(name)              \
    __AUX_DECL_CALL_DEVCLASS_METHOD             \
    try                                         \
    {                                           \
        bopy::call_method<void>(m_self, #name); \
    }                                           \
    __AUX_CATCH_PY_EXCEPTION

#define CALL_DEVCLASS_METHOD_VARGS(name, ...)                \
    __AUX_DECL_CALL_DEVCLASS_METHOD                          \
    try                                                      \
    {                                                        \
        bopy::call_method<void>(m_self, #name, __VA_ARGS__); \
    }                                                        \
    __AUX_CATCH_PY_EXCEPTION

CppDeviceClass::CppDeviceClass(const std::string &name) :
    Tango::DeviceClass(const_cast<std::string &>(name))
{
}

CppDeviceClass::~CppDeviceClass() { }

void CppDeviceClass::create_command(const std::string &cmd_name,
                                    Tango::CmdArgType param_type,
                                    Tango::CmdArgType result_type,
                                    const std::string &param_desc,
                                    const std::string &result_desc,
                                    Tango::DispLevel display_level,
                                    bool default_command,
                                    long polling_period,
                                    const std::string &is_allowed)
{
    PyCmd *cmd_ptr =
        new PyCmd(cmd_name.c_str(), param_type, result_type, param_desc.c_str(), result_desc.c_str(), display_level);

    if(!is_allowed.empty())
    {
        cmd_ptr->set_allowed(is_allowed);
    }

    if(polling_period > 0)
    {
        cmd_ptr->set_polling_period(polling_period);
    }
    if(default_command)
    {
        set_default_command(cmd_ptr);
    }
    else
    {
        command_list.push_back(cmd_ptr);
    }
}

void CppDeviceClass::create_fwd_attribute(std::vector<Tango::Attr *> &att_list,
                                          const std::string &attr_name,
                                          Tango::UserDefaultFwdAttrProp *att_prop)
{
    Tango::FwdAttr *attr_ptr = new Tango::FwdAttr(attr_name);
    attr_ptr->set_default_properties(*att_prop);
    att_list.push_back(attr_ptr);
}

void CppDeviceClass::create_attribute(std::vector<Tango::Attr *> &att_list,
                                      const std::string &attr_name,
                                      Tango::CmdArgType attr_type,
                                      Tango::AttrDataFormat attr_format,
                                      Tango::AttrWriteType attr_write,
                                      long dim_x,
                                      long dim_y,
                                      Tango::DispLevel display_level,
                                      long polling_period,
                                      bool memorized,
                                      bool hw_memorized,
                                      const std::string &read_method_name,
                                      const std::string &write_method_name,
                                      const std::string &is_allowed_name,
                                      Tango::UserDefaultAttrProp *att_prop)
{
    //
    // Create the attribute objet according to attribute format
    //

    PyScaAttr *sca_attr_ptr = NULL;
    PySpecAttr *spec_attr_ptr = NULL;
    PyImaAttr *ima_attr_ptr = NULL;
    PyAttr *py_attr_ptr = NULL;
    Tango::Attr *attr_ptr = NULL;

    switch(attr_format)
    {
    case Tango::SCALAR:
        sca_attr_ptr = new PyScaAttr(attr_name, attr_type, attr_write);
        py_attr_ptr = sca_attr_ptr;
        attr_ptr = sca_attr_ptr;
        break;

    case Tango::SPECTRUM:
        spec_attr_ptr = new PySpecAttr(attr_name.c_str(), attr_type, attr_write, dim_x);
        py_attr_ptr = spec_attr_ptr;
        attr_ptr = spec_attr_ptr;
        break;

    case Tango::IMAGE:
        ima_attr_ptr = new PyImaAttr(attr_name.c_str(), attr_type, attr_write, dim_x, dim_y);
        py_attr_ptr = ima_attr_ptr;
        attr_ptr = ima_attr_ptr;
        break;

    default:
        TangoSys_OMemStream o;
        o << "Attribute " << attr_name << " has an unexpected data format\n"
          << "Please report this bug to the PyTango development team" << std::ends;
        Tango::Except::throw_exception(
            (const char *) "PyDs_UnexpectedAttributeFormat", o.str(), (const char *) "create_attribute");
        break;
    }

    py_attr_ptr->set_read_name(read_method_name);
    py_attr_ptr->set_write_name(write_method_name);
    py_attr_ptr->set_allowed_name(is_allowed_name);

    if(att_prop)
    {
        attr_ptr->set_default_properties(*att_prop);
    }

    attr_ptr->set_disp_level(display_level);
    if(memorized)
    {
        attr_ptr->set_memorized();
        attr_ptr->set_memorized_init(hw_memorized);
    }

    if(polling_period > 0)
    {
        attr_ptr->set_polling_period(polling_period);
    }

    att_list.push_back(attr_ptr);
}

void CppDeviceClass::create_pipe(std::vector<Tango::Pipe *> &pipe_list,
                                 const std::string &name,
                                 Tango::PipeWriteType access,
                                 Tango::DispLevel display_level,
                                 const std::string &read_method_name,
                                 const std::string &write_method_name,
                                 const std::string &is_allowed_name,
                                 Tango::UserDefaultPipeProp *prop)
{
    Tango::Pipe *pipe_ptr = NULL;
    if(access == Tango::PIPE_READ)
    {
        PyTango::Pipe::PyPipe *py_pipe_ptr = new PyTango::Pipe::PyPipe(name, display_level, access);
        py_pipe_ptr->set_read_name(read_method_name);
        py_pipe_ptr->set_allowed_name(is_allowed_name);
        pipe_ptr = py_pipe_ptr;
    }
    else
    {
        PyTango::Pipe::PyWPipe *py_pipe_ptr = new PyTango::Pipe::PyWPipe(name, display_level);
        py_pipe_ptr->set_read_name(read_method_name);
        py_pipe_ptr->set_allowed_name(is_allowed_name);
        py_pipe_ptr->set_write_name(write_method_name);
        pipe_ptr = py_pipe_ptr;
    }

    if(prop)
    {
        pipe_ptr->set_default_properties(*prop);
    }
    pipe_list.push_back(pipe_ptr);
}

CppDeviceClassWrap::CppDeviceClassWrap(PyObject *_self, const std::string &name) :
    CppDeviceClass(name),
    m_self(_self)
{
    init_class();
}

/**
 * Destructor
 */
CppDeviceClassWrap::~CppDeviceClassWrap() { }

void CppDeviceClassWrap::init_class()
{
    AutoPythonGIL python_guard;
    signal_handler_defined = is_method_defined(m_self, "signal_handler");
}

void CppDeviceClassWrap::attribute_factory(std::vector<Tango::Attr *> &att_list)
{
    //
    // make sure we pass the same vector object to the python method
    //
    AutoPythonGIL python_guard;

    bopy::object py_att_list(bopy::handle<>(
        bopy::to_python_indirect<std::vector<Tango::Attr *>, bopy::detail::make_reference_holder>()(att_list)));

    try
    {
        bopy::call_method<void>(m_self, "_attribute_factory", py_att_list);
    }
    catch(bopy::error_already_set &eas)
    {
        handle_python_exception(eas);
    }
}

void CppDeviceClassWrap::pipe_factory()
{
    //
    // make sure we pass the same vector object to the python method
    //
    AutoPythonGIL python_guard;

    bopy::object py_pipe_list(bopy::handle<>(
        bopy::to_python_indirect<std::vector<Tango::Pipe *>, bopy::detail::make_reference_holder>()(pipe_list)));

    try
    {
        bopy::call_method<void>(m_self, "_pipe_factory", py_pipe_list);
    }
    catch(bopy::error_already_set &eas)
    {
        handle_python_exception(eas);
    }
}

void CppDeviceClassWrap::command_factory()
{
    CALL_DEVCLASS_METHOD(_command_factory)
}

void CppDeviceClassWrap::device_name_factory(std::vector<std::string> &dev_list)
{
    //
    // make sure we pass the same vector object to the python method
    //
    AutoPythonGIL python_guard;

    bopy::object py_dev_list(bopy::handle<>(
        bopy::to_python_indirect<std::vector<std::string>, bopy::detail::make_reference_holder>()(dev_list)));
    try
    {
        bopy::call_method<void>(m_self, "device_name_factory", py_dev_list);
    }
    catch(bopy::error_already_set &eas)
    {
        handle_python_exception(eas);
    }
}

void CppDeviceClassWrap::device_factory(const Tango::DevVarStringArray *dev_list)
{
    CALL_DEVCLASS_METHOD_VARGS(device_factory, dev_list)
}

void CppDeviceClassWrap::signal_handler(long signo)
{
    if(signal_handler_defined == true)
    {
        CALL_DEVCLASS_METHOD_VARGS(signal_handler, signo)
    }
    else
    {
        Tango::DeviceClass::signal_handler(signo);
    }
}

void CppDeviceClassWrap::default_signal_handler(long signo)
{
    this->Tango::DeviceClass::signal_handler(signo);
}

namespace PyDeviceClass
{

bopy::object get_device_list(CppDeviceClass &self)
{
    bopy::list py_dev_list;
    std::vector<Tango::DeviceImpl *> dev_list = self.get_device_list();
    for(std::vector<Tango::DeviceImpl *>::iterator it = dev_list.begin(); it != dev_list.end(); ++it)
    {
        bopy::object py_value = bopy::object(
            bopy::handle<>(bopy::to_python_indirect<Tango::DeviceImpl *, bopy::detail::make_reference_holder>()(*it)));
        py_dev_list.append(py_value);
    }
    return py_dev_list;
}

bopy::object get_command_list(CppDeviceClass &self)
{
    bopy::list py_cmd_list;
    std::vector<Tango::Command *> cmd_list = self.get_command_list();
    for(std::vector<Tango::Command *>::iterator it = cmd_list.begin(); it != cmd_list.end(); ++it)
    {
        bopy::object py_value = bopy::object(
            bopy::handle<>(bopy::to_python_indirect<Tango::Command *, bopy::detail::make_reference_holder>()(*it)));
        py_cmd_list.append(py_value);
    }
    return py_cmd_list;
}

bopy::object get_pipe_list(CppDeviceClass &self, const std::string &dev_name)
{
    bopy::list py_pipe_list;
    std::vector<Tango::Pipe *> pipe_list = self.get_pipe_list(dev_name);
    //        std::vector<Tango::Pipe *> pipe_list = self.get_pipe_list();
    for(std::vector<Tango::Pipe *>::iterator it = pipe_list.begin(); it != pipe_list.end(); ++it)
    {
        bopy::object py_value = bopy::object(
            bopy::handle<>(bopy::to_python_indirect<Tango::Pipe *, bopy::detail::make_reference_holder>()(*it)));
        py_pipe_list.append(py_value);
    }
    return py_pipe_list;
}

void register_signal(CppDeviceClass &self, long signo)
{
    self.register_signal(signo);
}

#if(defined __linux)

void register_signal(CppDeviceClass &self, long signo, bool own_handler)
{
    self.register_signal(signo, own_handler);
}

#endif
} // namespace PyDeviceClass

BOOST_PYTHON_MEMBER_FUNCTION_OVERLOADS(export_device_overload, CppDeviceClass::export_device, 1, 2)

void export_device_class()
{
    bopy::class_<CppDeviceClass, std::shared_ptr<CppDeviceClassWrap>, boost::noncopyable>(
        "DeviceClass", bopy::init<const std::string &>())

        .def("device_factory", &CppDeviceClassWrap::device_factory)
        .def("device_name_factory", &CppDeviceClassWrap::device_name_factory)
        .def("export_device", &CppDeviceClass::export_device, export_device_overload())
        .def("_add_device", &CppDeviceClass::add_device)
        .def("register_signal", (void (*)(CppDeviceClass &, long)) & PyDeviceClass::register_signal)
#if defined __linux
        .def("register_signal", (void (*)(CppDeviceClass &, long, bool)) & PyDeviceClass::register_signal)
#endif
        .def("unregister_signal", &Tango::DeviceClass::unregister_signal)
        .def("signal_handler", &Tango::DeviceClass::signal_handler, &CppDeviceClassWrap::default_signal_handler)
        .def("get_name", &Tango::DeviceClass::get_name, bopy::return_value_policy<bopy::copy_non_const_reference>())
        .def("get_type", &Tango::DeviceClass::get_type, bopy::return_value_policy<bopy::copy_non_const_reference>())
        .def("get_doc_url",
             &Tango::DeviceClass::get_doc_url,
             bopy::return_value_policy<bopy::copy_non_const_reference>())
        .def("get_cvs_tag",
             &Tango::DeviceClass::get_cvs_tag,
             bopy::return_value_policy<bopy::copy_non_const_reference>())
        .def("get_cvs_location",
             &Tango::DeviceClass::get_cvs_location,
             bopy::return_value_policy<bopy::copy_non_const_reference>())
        .def("get_device_list", &PyDeviceClass::get_device_list)
        .def("get_command_list", &PyDeviceClass::get_command_list)
        .def("get_pipe_list", &PyDeviceClass::get_pipe_list)
        .def("get_cmd_by_name", &Tango::DeviceClass::get_cmd_by_name, bopy::return_internal_reference<>())
        .def("get_pipe_by_name", &Tango::DeviceClass::get_pipe_by_name, bopy::return_internal_reference<>())
        .def("set_type", (void(Tango::DeviceClass::*)(const char *)) & Tango::DeviceClass::set_type)
        .def("add_wiz_dev_prop",
             (void(Tango::DeviceClass::*)(const std::string &, const std::string &)) &
                 Tango::DeviceClass::add_wiz_dev_prop)
        .def("add_wiz_dev_prop",
             (void(Tango::DeviceClass::*)(const std::string &, const std::string &, const std::string &)) &
                 Tango::DeviceClass::add_wiz_dev_prop)
        .def("add_wiz_class_prop",
             (void(Tango::DeviceClass::*)(const std::string &, const std::string &)) &
                 Tango::DeviceClass::add_wiz_class_prop)
        .def("add_wiz_class_prop",
             (void(Tango::DeviceClass::*)(const std::string &, const std::string &, const std::string &)) &
                 Tango::DeviceClass::add_wiz_class_prop)
        .def("_device_destroyer", (void(Tango::DeviceClass::*)(const char *)) & Tango::DeviceClass::device_destroyer)
        .def("_create_attribute", &CppDeviceClass::create_attribute)
        .def("_create_fwd_attribute", &CppDeviceClass::create_fwd_attribute)
        .def("_create_pipe", &CppDeviceClass::create_pipe)
        .def("_create_command", &CppDeviceClass::create_command)
        .def("get_class_attr",
             &Tango::DeviceClass::get_class_attr,
             bopy::return_value_policy<bopy::reference_existing_object>());
    bopy::implicitly_convertible<std::shared_ptr<CppDeviceClassWrap>, std::shared_ptr<CppDeviceClass>>();
}
