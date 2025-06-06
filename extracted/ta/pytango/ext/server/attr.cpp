/*
 * SPDX-FileCopyrightText: All Contributors to the PyTango project
 *
 * SPDX-License-Identifier: LGPL-3.0-or-later
 */

#include "precompiled_header.hpp"
#include "server/attr.h"

#define __AUX_DECL_CALL_ATTR_METHOD                                      \
    PyDeviceImplBase *__dev_ptr = dynamic_cast<PyDeviceImplBase *>(dev); \
    AutoPythonGIL __py_lock;

#define __AUX_CATCH_PY_EXCEPTION         \
    catch(bopy::error_already_set & eas) \
    {                                    \
        handle_python_exception(eas);    \
    }

#define CALL_ATTR_METHOD(dev, name)                         \
    __AUX_DECL_CALL_ATTR_METHOD                             \
    try                                                     \
    {                                                       \
        bopy::call_method<void>(__dev_ptr->the_self, name); \
    }                                                       \
    __AUX_CATCH_PY_EXCEPTION

#define CALL_ATTR_METHOD_VARGS(dev, name, ...)                           \
    __AUX_DECL_CALL_ATTR_METHOD                                          \
    try                                                                  \
    {                                                                    \
        bopy::call_method<void>(__dev_ptr->the_self, name, __VA_ARGS__); \
    }                                                                    \
    __AUX_CATCH_PY_EXCEPTION

#define CALL_ATTR_METHOD_RET(retType, ret, dev, name)                \
    __AUX_DECL_CALL_ATTR_METHOD                                      \
    try                                                              \
    {                                                                \
        ret = bopy::call_method<retType>(__dev_ptr->the_self, name); \
    }                                                                \
    __AUX_CATCH_PY_EXCEPTION

#define CALL_ATTR_METHOD_VARGS_RET(retType, ret, dev, name, ...)                  \
    __AUX_DECL_CALL_ATTR_METHOD                                                   \
    try                                                                           \
    {                                                                             \
        ret = bopy::call_method<retType>(__dev_ptr->the_self, name, __VA_ARGS__); \
    }                                                                             \
    __AUX_CATCH_PY_EXCEPTION

#define RET_CALL_ATTR_METHOD(retType, dev, name)                      \
    __AUX_DECL_CALL_ATTR_METHOD                                       \
    try                                                               \
    {                                                                 \
        return bopy::call_method<retType>(__dev_ptr->the_self, name); \
    }                                                                 \
    __AUX_CATCH_PY_EXCEPTION

#define RET_CALL_ATTR_METHOD_VARGS(retType, dev, name, ...)                        \
    __AUX_DECL_CALL_ATTR_METHOD                                                    \
    try                                                                            \
    {                                                                              \
        return bopy::call_method<retType>(__dev_ptr->the_self, name, __VA_ARGS__); \
    }                                                                              \
    __AUX_CATCH_PY_EXCEPTION

#if _MSC_VER > 1800
namespace boost
{
template <>
Tango::Attr const volatile *get_pointer<class Tango::Attr const volatile>(class Tango::Attr const volatile *c)
{
    return c;
}
} // namespace boost
#endif

void PyAttr::read(Tango::DeviceImpl *dev, Tango::Attribute &att)
{
    if(!_is_method(dev, read_name))
    {
        TangoSys_OMemStream o;
        o << read_name << " method not found for " << att.get_name();
        Tango::Except::throw_exception("PyTango_ReadAttributeMethodNotFound", o.str(), "PyTango::Attr::read");
    }
    CALL_ATTR_METHOD_VARGS(dev, read_name.c_str(), boost::ref(att))
}

void PyAttr::write(Tango::DeviceImpl *dev, Tango::WAttribute &att)
{
    if(!_is_method(dev, write_name))
    {
        TangoSys_OMemStream o;
        o << write_name << " method not found for " << att.get_name();
        Tango::Except::throw_exception("PyTango_WriteAttributeMethodNotFound", o.str(), "PyTango::Attr::write");
    }
    CALL_ATTR_METHOD_VARGS(dev, write_name.c_str(), boost::ref(att))
}

bool PyAttr::is_allowed(Tango::DeviceImpl *dev, Tango::AttReqType ty)
{
    if(_is_method(dev, py_allowed_name))
    {
        RET_CALL_ATTR_METHOD_VARGS(bool, dev, py_allowed_name.c_str(), ty)
    }
    // keep compiler quiet
    return true;
}

bool PyAttr::_is_method(Tango::DeviceImpl *dev, const std::string &name)
{
    AutoPythonGIL __py_lock;
    PyDeviceImplBase *__dev_ptr = dynamic_cast<PyDeviceImplBase *>(dev);
    PyObject *__dev_py = __dev_ptr->the_self;
    return is_method_defined(__dev_py, name);
}

void PyAttr::set_user_prop(std::vector<Tango::AttrProperty> &user_prop, Tango::UserDefaultAttrProp &def_prop)
{
    //
    // Is there any user defined prop. defined ?
    //

    size_t nb_prop = user_prop.size();
    if(nb_prop == 0)
    {
        return;
    }

    for(size_t loop = 0; loop < nb_prop; loop++)
    {
        Tango::AttrProperty prop = user_prop[loop];
        std::string &prop_name = prop.get_name();
        const char *prop_value = prop.get_value().c_str();

        if(prop_name == "label")
        {
            def_prop.set_label(prop_value);
        }
        else if(prop_name == "description")
        {
            def_prop.set_description(prop_value);
        }
        else if(prop_name == "unit")
        {
            def_prop.set_unit(prop_value);
        }
        else if(prop_name == "standard_unit")
        {
            def_prop.set_standard_unit(prop_value);
        }
        else if(prop_name == "display_unit")
        {
            def_prop.set_display_unit(prop_value);
        }
        else if(prop_name == "format")
        {
            def_prop.set_format(prop_value);
        }
        else if(prop_name == "min_value")
        {
            def_prop.set_min_value(prop_value);
        }
        else if(prop_name == "max_value")
        {
            def_prop.set_max_value(prop_value);
        }
        else if(prop_name == "min_alarm")
        {
            def_prop.set_min_alarm(prop_value);
        }
        else if(prop_name == "max_alarm")
        {
            def_prop.set_max_alarm(prop_value);
        }
        else if(prop_name == "min_warning")
        {
            def_prop.set_min_warning(prop_value);
        }
        else if(prop_name == "max_warning")
        {
            def_prop.set_max_warning(prop_value);
        }
        else if(prop_name == "delta_val")
        {
            def_prop.set_delta_val(prop_value);
        }
        else if(prop_name == "delta_t")
        {
            def_prop.set_delta_t(prop_value);
        }
        else if(prop_name == "abs_change")
        {
            def_prop.set_event_abs_change(prop_value);
        }
        else if(prop_name == "rel_change")
        {
            def_prop.set_event_rel_change(prop_value);
        }
        else if(prop_name == "period")
        {
            def_prop.set_event_period(prop_value);
        }
        else if(prop_name == "archive_abs_change")
        {
            def_prop.set_archive_event_abs_change(prop_value);
        }
        else if(prop_name == "archive_rel_change")
        {
            def_prop.set_archive_event_rel_change(prop_value);
        }
        else if(prop_name == "archive_period")
        {
            def_prop.set_archive_event_period(prop_value);
        }
        else if(prop_name == "enum_labels")
        {
            // Convert string back to vector
            std::vector<std::string> labels;
            std::string label_str = prop.get_value();
            size_t offset = 0, pos = 0;
            while((pos = label_str.find(",", offset)) != std::string::npos)
            {
                labels.push_back(label_str.substr(offset, pos - offset));
                offset = pos + 1;
            }
            labels.push_back(label_str.substr(offset));
            def_prop.set_enum_labels(labels);
        }
    }
}

void export_attr()
{
    bopy::class_<Tango::Attr, boost::noncopyable>(
        "Attr", bopy::init<const char *, long, bopy::optional<Tango::AttrWriteType, const char *>>())

        .def("set_default_properties", &Tango::Attr::set_default_properties)
        .def("set_disp_level", &Tango::Attr::set_disp_level)
        .def("set_polling_period", &Tango::Attr::set_polling_period)
        .def("set_memorized", &Tango::Attr::set_memorized)
        .def("set_memorized_init", &Tango::Attr::set_memorized_init)
        .def("set_change_event", &Tango::Attr::set_change_event)
        .def("is_change_event", &Tango::Attr::is_change_event)
        .def("set_alarm_event", &Tango::Attr::set_alarm_event)
        .def("is_alarm_event", &Tango::Attr::is_alarm_event)
        .def("is_check_change_criteria", &Tango::Attr::is_check_change_criteria)
        .def("set_archive_event", &Tango::Attr::set_archive_event)
        .def("is_archive_event", &Tango::Attr::is_archive_event)
        .def("is_check_archive_criteria", &Tango::Attr::is_check_archive_criteria)
        .def("set_data_ready_event", &Tango::Attr::set_data_ready_event)
        .def("is_data_ready_event", &Tango::Attr::is_data_ready_event)
        .def("get_name",
             (std::string const &(Tango::Attr::*) () const) & Tango::Attr::get_name,
             bopy::return_value_policy<bopy::copy_const_reference>())
        .def("get_format", &Tango::Attr::get_format)
        .def("get_writable", &Tango::Attr::get_writable)
        .def("get_type", &Tango::Attr::get_type)
        .def("get_disp_level", &Tango::Attr::get_disp_level)
        .def("get_polling_period", &Tango::Attr::get_polling_period)
        .def("get_memorized", &Tango::Attr::get_memorized)
        .def("get_memorized_init", &Tango::Attr::get_memorized_init)
        .def("get_assoc", &Tango::Attr::get_assoc, bopy::return_value_policy<bopy::copy_non_const_reference>())
        .def("is_assoc", &Tango::Attr::is_assoc)
        .def("get_cl_name", &Tango::Attr::get_cl_name, bopy::return_value_policy<bopy::copy_const_reference>())
        .def("set_cl_name", &Tango::Attr::set_cl_name)
        .def("get_class_properties", &Tango::Attr::get_class_properties, bopy::return_internal_reference<>())
        .def("get_user_default_properties",
             &Tango::Attr::get_user_default_properties,
             bopy::return_internal_reference<>())
        .def("set_class_properties", &Tango::Attr::set_class_properties)
        .def("check_type", &Tango::Attr::check_type)
        .def("read", &Tango::Attr::read)
        .def("write", &Tango::Attr::write)
        .def("is_allowed", &Tango::Attr::is_allowed);

    bopy::class_<Tango::SpectrumAttr, bopy::bases<Tango::Attr>, boost::noncopyable>(
        "SpectrumAttr", bopy::init<const char *, long, Tango::AttrWriteType, long>());

    bopy::class_<Tango::ImageAttr, bopy::bases<Tango::SpectrumAttr>, boost::noncopyable>(
        "ImageAttr", bopy::init<const char *, long, Tango::AttrWriteType, long, long>());

    //    class_<PyAttr>("PyAttr", no_init)
    //        .def("set_allowed", &PyAttr::set_allowed)
    //        .def("set_read_name", &PyAttr::set_read_name)
    //        .def("set_write_name", &PyAttr::set_write_name)
    //    ;
    //
    //    class_<PyScaAttr, bases<Tango::Attr, PyAttr>, boost::noncopyable>("PyScaAttr",
    //        init<const std::string &, long , Tango::AttrWriteType>())
    //    ;
    //
    //    class_<PySpecAttr, bases<Tango::SpectrumAttr, PyAttr>, boost::noncopyable>("PySpecAttr",
    //        init<const std::string &, long , Tango::AttrWriteType, long>())
    //    ;
    //
    //    class_<PyImaAttr, bases<Tango::ImageAttr, PyAttr>, boost::noncopyable>("PyImaAttr",
    //        init<const std::string &, long , Tango::AttrWriteType, long, long>())
    //    ;

    bopy::class_<Tango::AttrProperty>("AttrProperty", bopy::init<const char *, const char *>())
        .def(bopy::init<const char *, long>())
        .def("get_value",
             (std::string const &(Tango::AttrProperty::*) () const) & Tango::AttrProperty::get_value,
             bopy::return_value_policy<bopy::copy_const_reference>())
        .def("get_lg_value", &Tango::AttrProperty::get_lg_value)
        .def("get_name",
             (std::string const &(Tango::AttrProperty::*) () const) & Tango::AttrProperty::get_name,
             bopy::return_value_policy<bopy::copy_const_reference>());
}
