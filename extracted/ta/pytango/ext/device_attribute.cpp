/*
 * SPDX-FileCopyrightText: All Contributors to the PyTango project
 *
 * SPDX-License-Identifier: LGPL-3.0-or-later
 */

#include "precompiled_header.hpp"
#include "device_attribute.h"
#include "pytgutils.h"
#include "tango_numpy.h"
#include "fast_from_py.h"

extern const char *non_valid_image;
extern const char *non_valid_spectrum;

// Why am I storing 'type' as a python attribute with object::attr
// instead of as a property calling DeviceAttribute::get_type here?
// Because after 'extract'ing, any call to get_type() will fail. Same
// for "value" and "w_value". And for has_failed and is_empty...
static const char *value_attr_name = "value";
static const char *w_value_attr_name = "w_value";
static const char *type_attr_name = "type";
static const char *is_empty_attr_name = "is_empty";
static const char *has_failed_attr_name = "has_failed";

#include "device_attribute_numpy.hpp"

#define EXTRACT_VALUE(self, value_ptr)                                       \
    try                                                                      \
    {                                                                        \
        self >> value_ptr;                                                   \
    }                                                                        \
    catch(Tango::DevFailed & e)                                              \
    {                                                                        \
        if(strcmp(e.errors[0].reason.in(), "API_EmptyDeviceAttribute") != 0) \
            throw;                                                           \
    }

namespace PyDeviceAttribute
{
template <long tangoTypeConst>
static inline void _update_value_as_bin(Tango::DeviceAttribute &self, bopy::object py_value, bool read_only)
{
    typedef typename TANGO_const2type(tangoTypeConst) TangoScalarType;
    typedef typename TANGO_const2arraytype(tangoTypeConst) TangoArrayType;

    const int read_length = self.get_nb_read();
    const int written_length = self.get_nb_written();

    // Extract the actual data from Tango::DeviceAttribute (self)
    TangoArrayType *value_ptr = 0;
    EXTRACT_VALUE(self, value_ptr)
    unique_pointer<TangoArrayType> guard_value_ptr(value_ptr);

    TangoArrayType empty;
    if(value_ptr == 0)
    {
        // Empty device attribute
        value_ptr = &empty;
    }

    TangoScalarType *buffer = value_ptr->get_buffer();

    const char *ch_ptr = reinterpret_cast<char *>(buffer);

    Py_ssize_t nb_bytes_read = read_length * sizeof(TangoScalarType);
    Py_ssize_t nb_bytes_written = written_length * sizeof(TangoScalarType);

    PyObject *read_data_ptr = NULL;
    if(read_only)
    {
        read_data_ptr = PyBytes_FromStringAndSize(ch_ptr, nb_bytes_read);
    }
    else
    {
        read_data_ptr = PyByteArray_FromStringAndSize(ch_ptr, nb_bytes_read);
    }

    py_value.attr(value_attr_name) = bopy::object(bopy::handle<>(read_data_ptr));

    PyObject *written_data_ptr = NULL;
    if(read_only)
    {
        written_data_ptr = PyBytes_FromStringAndSize(ch_ptr + nb_bytes_read, nb_bytes_written);
    }
    else
    {
        written_data_ptr = PyByteArray_FromStringAndSize(ch_ptr + nb_bytes_read, nb_bytes_written);
    }

    py_value.attr(w_value_attr_name) = bopy::object(bopy::handle<>(written_data_ptr));
}

template <>
inline void _update_value_as_bin<Tango::DEV_STRING>(Tango::DeviceAttribute &self, bopy::object py_value, bool read_only)
{
    assert(false);
}

template <>
inline void
    _update_value_as_bin<Tango::DEV_ENCODED>(Tango::DeviceAttribute &self, bopy::object py_value, bool read_only)
{
    Tango::DevVarEncodedArray *value_ptr;
    EXTRACT_VALUE(self, value_ptr)
    unique_pointer<Tango::DevVarEncodedArray> guard(value_ptr);

    Tango::DevEncoded *buffer = value_ptr->get_buffer();
    Tango::DevEncoded &r_buffer = buffer[0];
    bopy::str r_encoded_format(r_buffer.encoded_format);

    Tango::DevVarCharArray &r_encoded_data_array = r_buffer.encoded_data;
    char *r_ch_ptr = (char *) r_encoded_data_array.get_buffer();
    Py_ssize_t r_size = r_encoded_data_array.length();
    PyObject *r_encoded_data_ptr = NULL;
    if(read_only)
    {
        r_encoded_data_ptr = PyBytes_FromStringAndSize(r_ch_ptr, r_size);
    }
    else
    {
        r_encoded_data_ptr = PyByteArray_FromStringAndSize(r_ch_ptr, r_size);
    }
    bopy::object r_encoded_data = bopy::object(bopy::handle<>(r_encoded_data_ptr));

    py_value.attr(value_attr_name) = bopy::make_tuple(r_encoded_format, r_encoded_data);

    if(self.get_written_dim_x() > 0)
    {
        bool is_write_type = self.get_written_dim_x() && (value_ptr->length() < 2);
        if(is_write_type)
        {
            bopy::object w_encoded_format(r_encoded_format);
            bopy::object w_encoded_data(r_encoded_data);
            py_value.attr(w_value_attr_name) = bopy::make_tuple(w_encoded_format, w_encoded_data);
        }
        else
        {
            Tango::DevEncoded &w_buffer = buffer[1];
            bopy::str w_encoded_format(w_buffer.encoded_format);

            Tango::DevVarCharArray &w_encoded_data_array = w_buffer.encoded_data;
            char *w_ch_ptr = (char *) w_encoded_data_array.get_buffer();
            PyObject *w_encoded_data_ptr = NULL;
            Py_ssize_t w_size = w_encoded_data_array.length();
            if(read_only)
            {
                w_encoded_data_ptr = PyBytes_FromStringAndSize(w_ch_ptr, w_size);
            }
            else
            {
                w_encoded_data_ptr = PyByteArray_FromStringAndSize(w_ch_ptr, w_size);
            }
            bopy::object w_encoded_data = bopy::object(bopy::handle<>(w_encoded_data_ptr));

            py_value.attr(w_value_attr_name) = bopy::make_tuple(w_encoded_format, w_encoded_data);
        }
    }
    else
    {
        py_value.attr(w_value_attr_name) = bopy::object();
    }
}

template <>
inline void
    _update_value_as_bin<Tango::DEV_PIPE_BLOB>(Tango::DeviceAttribute &self, bopy::object py_value, bool read_only)
{
    assert(false);
}

template <long tangoTypeConst>
static inline void _update_value_as_string(Tango::DeviceAttribute &self, bopy::object py_value)
{
    typedef typename TANGO_const2type(tangoTypeConst) TangoScalarType;
    typedef typename TANGO_const2arraytype(tangoTypeConst) TangoArrayType;

    const int read_length = self.get_nb_read();
    const int written_length = self.get_nb_written();

    // Extract the actual data from Tango::DeviceAttribute (self)
    TangoArrayType *value_ptr = 0;
    EXTRACT_VALUE(self, value_ptr)
    unique_pointer<TangoArrayType> guard_value_ptr(value_ptr);

    TangoArrayType empty;
    if(value_ptr == 0)
    {
        // Empty device attribute
        value_ptr = &empty;
    }

    TangoScalarType *buffer = value_ptr->get_buffer();

    const char *ch_ptr = reinterpret_cast<char *>(buffer);
    size_t nb_bytes_read = read_length * sizeof(TangoScalarType);
    size_t nb_bytes_written = written_length * sizeof(TangoScalarType);

    py_value.attr(value_attr_name) = bopy::str(ch_ptr, (size_t) nb_bytes_read);
    py_value.attr(w_value_attr_name) = bopy::str(ch_ptr + nb_bytes_read, (size_t) nb_bytes_written);
}

template <>
inline void _update_value_as_string<Tango::DEV_STRING>(Tango::DeviceAttribute &self, bopy::object py_value)
{
    assert(false);
}

template <>
inline void _update_value_as_string<Tango::DEV_ENCODED>(Tango::DeviceAttribute &self, bopy::object py_value)
{
    Tango::DevVarEncodedArray *value_ptr;
    EXTRACT_VALUE(self, value_ptr)
    unique_pointer<Tango::DevVarEncodedArray> guard(value_ptr);

    Tango::DevEncoded *buffer = value_ptr->get_buffer();

    Tango::DevEncoded &r_buffer = buffer[0];
    bopy::str r_encoded_format(r_buffer.encoded_format);

    Tango::DevVarCharArray &r_encoded_data_array = r_buffer.encoded_data;
    char *r_ch_ptr = (char *) r_encoded_data_array.get_buffer();
    bopy::str r_encoded_data(r_ch_ptr, r_encoded_data_array.length());

    py_value.attr(value_attr_name) = bopy::make_tuple(r_encoded_format, r_encoded_data);

    if(self.get_written_dim_x() > 0)
    {
        bool is_write_type = self.get_written_dim_x() && (value_ptr->length() < 2);
        if(is_write_type)
        {
            bopy::object w_encoded_format(r_encoded_format);
            bopy::object w_encoded_data(r_encoded_data);
            py_value.attr(w_value_attr_name) = bopy::make_tuple(w_encoded_format, w_encoded_data);
        }
        else
        {
            Tango::DevEncoded &w_buffer = buffer[1];
            bopy::str w_encoded_format(w_buffer.encoded_format);

            Tango::DevVarCharArray &w_encoded_data_array = w_buffer.encoded_data;
            char *w_ch_ptr = (char *) w_encoded_data_array.get_buffer();
            bopy::str w_encoded_data(w_ch_ptr, w_encoded_data_array.length());

            py_value.attr(w_value_attr_name) = bopy::make_tuple(w_encoded_format, w_encoded_data);
        }
    }
    else
    {
        py_value.attr(w_value_attr_name) = bopy::object();
    }
}

template <>
inline void _update_value_as_string<Tango::DEV_PIPE_BLOB>(Tango::DeviceAttribute &self, bopy::object py_value)
{
    assert(false);
}

template <long tangoTypeConst>
static inline void _update_scalar_values(Tango::DeviceAttribute &self, bopy::object py_value)
{
    typedef typename TANGO_const2type(tangoTypeConst) TangoScalarType;

    if(self.get_written_dim_x() > 0)
    {
        std::vector<TangoScalarType> val;
        self.extract_read(val);
        // In the following lines, the cast is absolutely necessary because
        // vector<TangoScalarType> may not be a vector<TangoScalarType> at
        // compile time. For example, for vector<DevBoolean>, the compiler
        // may create a std::_Bit_reference type.
        py_value.attr(value_attr_name) = bopy::object((TangoScalarType) val[0]);
        self.extract_set(val);
        py_value.attr(w_value_attr_name) = bopy::object((TangoScalarType) val[0]);
    }
    else
    {
        TangoScalarType rvalue;
        EXTRACT_VALUE(self, rvalue)
        py_value.attr(value_attr_name) = bopy::object(rvalue);
        py_value.attr(w_value_attr_name) = bopy::object();
    }
}

template <>
inline void _update_scalar_values<Tango::DEV_ENCODED>(Tango::DeviceAttribute &self, bopy::object py_value)
{
    _update_value_as_bin<Tango::DEV_ENCODED>(self, py_value, true);
}

template <>
inline void _update_scalar_values<Tango::DEV_STRING>(Tango::DeviceAttribute &self, bopy::object py_value)
{
    if(self.get_written_dim_x() > 0)
    {
        std::vector<std::string> r_val, w_val;
        self.extract_read(r_val);
        py_value.attr(value_attr_name) = from_char_to_boost_str(r_val[0]);
        self.extract_set(w_val);
        py_value.attr(w_value_attr_name) = from_char_to_boost_str(w_val[0]);
    }
    else
    {
        std::string rvalue;
        EXTRACT_VALUE(self, rvalue)
        py_value.attr(value_attr_name) = from_char_to_boost_str(rvalue);
        py_value.attr(w_value_attr_name) = bopy::object();
    }
}

template <>
inline void _update_scalar_values<Tango::DEV_PIPE_BLOB>(Tango::DeviceAttribute &self, bopy::object py_value)
{
    assert(false);
}

template <long tangoTypeConst>
static inline void _update_array_values_as_lists(Tango::DeviceAttribute &self, bool isImage, bopy::object py_value)
{
    typedef typename TANGO_const2type(tangoTypeConst) TangoScalarType;
    typedef typename TANGO_const2arraytype(tangoTypeConst) TangoArrayType;

    // Extract the actual data from Tango::DeviceAttribute (self)
    TangoArrayType *value_ptr = 0;
    EXTRACT_VALUE(self, value_ptr)
    unique_pointer<TangoArrayType> guard_value_ptr(value_ptr);

    if(value_ptr == 0)
    {
        // Empty device attribute
        py_value.attr(value_attr_name) = bopy::list();
        py_value.attr(w_value_attr_name) = bopy::list();
        return;
    }

    TangoScalarType *buffer = value_ptr->get_buffer();
    int total_length = value_ptr->length();

    // Determine if the attribute is AttrWriteType.WRITE
    int read_size = 0, write_size = 0;
    if(isImage)
    {
        read_size = self.get_dim_x() * self.get_dim_y();
        write_size = self.get_written_dim_x() * self.get_written_dim_y();
    }
    else
    {
        read_size = self.get_dim_x();
        write_size = self.get_written_dim_x();
    }
    bool is_write_type = (read_size + write_size) > total_length;

    // Convert to a list of lists
    long offset = 0;
    for(int it = 1; it >= 0; --it)
    { // 2 iterations: read part/write part
        if((!it) && is_write_type)
        {
            py_value.attr(w_value_attr_name) = py_value.attr(value_attr_name);
            continue;
        }
        bopy::list result;

        if(isImage)
        {
            const int dim_x = it ? self.get_dim_x() : self.get_written_dim_x();
            const int dim_y = it ? self.get_dim_y() : self.get_written_dim_y();

            for(int y = 0; y < dim_y; ++y)
            {
                bopy::list row;
                for(int x = 0; x < dim_x; ++x)
                {
                    row.append(python_tangocpp<tangoTypeConst>::to_python(buffer[offset + x + y * dim_x]));
                }
                result.append(row);
            }
            offset += dim_x * dim_y;
        }
        else
        {
            const int dim_x = it ? self.get_dim_x() : self.get_written_dim_x();
            for(int x = 0; x < dim_x; ++x)
            {
                result.append(python_tangocpp<tangoTypeConst>::to_python(buffer[offset + x]));
            }
            offset += dim_x;
        }
        py_value.attr(it ? value_attr_name : w_value_attr_name) = result;
    }
}

template <>
inline void _update_array_values_as_lists<Tango::DEV_PIPE_BLOB>(Tango::DeviceAttribute &self,
                                                                bool isImage,
                                                                bopy::object py_value)
{
    assert(false);
}

template <long tangoTypeConst>
static void _update_array_values_as_tuples(Tango::DeviceAttribute &self, bool isImage, bopy::object py_value)
{
    typedef typename TANGO_const2type(tangoTypeConst) TangoScalarType;
    typedef typename TANGO_const2arraytype(tangoTypeConst) TangoArrayType;

    // Extract the actual data from Tango::DeviceAttribute (self)
    TangoArrayType *value_ptr = 0;
    EXTRACT_VALUE(self, value_ptr)
    unique_pointer<TangoArrayType> guard_value_ptr(value_ptr);

    if(value_ptr == 0)
    {
        // Empty device attribute
        py_value.attr(value_attr_name) = bopy::tuple();
        py_value.attr(w_value_attr_name) = bopy::tuple();
        return;
    }

    TangoScalarType *buffer = value_ptr->get_buffer();
    int total_length = value_ptr->length();

    // Determine if the attribute is AttrWriteType.WRITE
    int read_size = 0, write_size = 0;
    if(isImage)
    {
        read_size = self.get_dim_x() * self.get_dim_y();
        write_size = self.get_written_dim_x() * self.get_written_dim_y();
    }
    else
    {
        read_size = self.get_dim_x();
        write_size = self.get_written_dim_x();
    }
    bool is_write_type = (read_size + write_size) > total_length;

    // Convert to a tuple of tuples
    long offset = 0;
    for(int it = 1; it >= 0; --it)
    { // 2 iterations: read part/write part
        if((!it) && is_write_type)
        {
            py_value.attr(w_value_attr_name) = py_value.attr(value_attr_name);
            continue;
        }

        bopy::object result_guard;
        if(isImage)
        {
            const int dim_x = it ? self.get_dim_x() : self.get_written_dim_x();
            const int dim_y = it ? self.get_dim_y() : self.get_written_dim_y();

            PyObject *result = PyTuple_New(dim_y);
            if(!result)
            {
                bopy::throw_error_already_set();
            }
            result_guard = bopy::object(bopy::handle<>(result));

            for(int y = 0; y < dim_y; ++y)
            {
                PyObject *row = PyTuple_New(dim_x);
                if(!row)
                {
                    bopy::throw_error_already_set();
                }
                bopy::object row_guard = bopy::object(bopy::handle<>(row));
                for(int x = 0; x < dim_x; ++x)
                {
                    bopy::object el = python_tangocpp<tangoTypeConst>::to_python(buffer[offset + x + y * dim_x]);
                    PyTuple_SetItem(row, x, el.ptr());
                    bopy::incref(el.ptr());
                }
                PyTuple_SetItem(result, y, row);
                bopy::incref(row);
            }
            offset += dim_x * dim_y;
        }
        else
        {
            const int dim_x = it ? self.get_dim_x() : self.get_written_dim_x();

            PyObject *result = PyTuple_New(dim_x);
            if(!result)
            {
                bopy::throw_error_already_set();
            }
            result_guard = bopy::object(bopy::handle<>(result));

            for(int x = 0; x < dim_x; ++x)
            {
                bopy::object el = python_tangocpp<tangoTypeConst>::to_python(buffer[offset + x]);
                PyTuple_SetItem(result, x, el.ptr());
                bopy::incref(el.ptr());
            }
            offset += dim_x;
        }
        py_value.attr(it ? value_attr_name : w_value_attr_name) = result_guard;
    }
}

template <>
inline void _update_array_values_as_tuples<Tango::DEV_PIPE_BLOB>(Tango::DeviceAttribute &self,
                                                                 bool isImage,
                                                                 bopy::object py_value)
{
    assert(false);
}

void update_values(Tango::DeviceAttribute &self,
                   bopy::object &py_value,
                   PyTango::ExtractAs extract_as /*=ExtractAsNumpy*/)
{
    // We do not want is_empty to launch an exception!!
    self.reset_exceptions(Tango::DeviceAttribute::isempty_flag);

    const bool has_failed = self.has_failed();
    py_value.attr(has_failed_attr_name) = bopy::object(has_failed);

    const bool is_empty = self.is_empty();
    py_value.attr(is_empty_attr_name) = bopy::object(is_empty);

    const int quality = self.get_quality();
    const bool is_invalid = quality == Tango::ATTR_INVALID;

    const int data_type = self.get_type();
    const bool failed_data_type = ((data_type < 0) || (data_type == Tango::DATA_TYPE_UNKNOWN));

    Tango::AttrDataFormat data_format = self.get_data_format();
    py_value.attr(type_attr_name) = bopy::object(static_cast<Tango::CmdArgType>(data_type));

    if(failed_data_type || has_failed || is_invalid)
    {
        // In these cases we cannot/should not (to maintain backward compatibility) extract data
        py_value.attr(value_attr_name) = bopy::object();
        py_value.attr(w_value_attr_name) = bopy::object();
        return;
    }

    bool is_image = false;
    switch(data_format)
    {
    case Tango::SCALAR:
        if(data_type == Tango::DEV_ENCODED)
        {
            switch(extract_as)
            {
            default:
            case PyTango::ExtractAsNumpy:
            case PyTango::ExtractAsTuple:
            case PyTango::ExtractAsList:
                TANGO_CALL_ON_ATTRIBUTE_DATA_TYPE_ID(data_type, _update_scalar_values, self, py_value);
                break;
            case PyTango::ExtractAsBytes:
                TANGO_CALL_ON_ATTRIBUTE_DATA_TYPE_ID(data_type, _update_value_as_bin, self, py_value, true);
                break;
            case PyTango::ExtractAsByteArray:
                TANGO_CALL_ON_ATTRIBUTE_DATA_TYPE_ID(data_type, _update_value_as_bin, self, py_value, false);
                break;
            case PyTango::ExtractAsString:
                TANGO_CALL_ON_ATTRIBUTE_DATA_TYPE_ID(data_type, _update_value_as_string, self, py_value);
                break;
            case PyTango::ExtractAsNothing:
                break;
            }
        }
        else
        {
            if(extract_as != PyTango::ExtractAsNothing)
            {
                TANGO_CALL_ON_ATTRIBUTE_DATA_TYPE_ID(data_type, _update_scalar_values, self, py_value);
            }
        }
        break;
    case Tango::IMAGE:
        is_image = true;
    case Tango::SPECTRUM:
        switch(extract_as)
        {
        default:
        case PyTango::ExtractAsNumpy:
            TANGO_CALL_ON_ATTRIBUTE_DATA_TYPE_ID(data_type, _update_array_values, self, is_image, py_value);
            break;
        case PyTango::ExtractAsTuple:
            TANGO_CALL_ON_ATTRIBUTE_DATA_TYPE_ID(data_type, _update_array_values_as_tuples, self, is_image, py_value);
            break;
        case PyTango::ExtractAsList:
            TANGO_CALL_ON_ATTRIBUTE_DATA_TYPE_ID(data_type, _update_array_values_as_lists, self, is_image, py_value);
            break;
        case PyTango::ExtractAsBytes:
            TANGO_CALL_ON_ATTRIBUTE_DATA_TYPE_ID(data_type, _update_value_as_bin, self, py_value, true);
            break;
        case PyTango::ExtractAsByteArray:
            TANGO_CALL_ON_ATTRIBUTE_DATA_TYPE_ID(data_type, _update_value_as_bin, self, py_value, false);
            break;
        case PyTango::ExtractAsString:
            TANGO_CALL_ON_ATTRIBUTE_DATA_TYPE_ID(data_type, _update_value_as_string, self, py_value);
            break;
        case PyTango::ExtractAsNothing:
            break;
        }
        break;
    case Tango::FMT_UNKNOWN:
    default:
        raise_(PyExc_ValueError, "Can't extract data because: self.get_data_format()=FMT_UNKNOWN");
        assert(false);
    }
}

template <long tangoTypeConst>
static inline void
    _fill_list_attribute(Tango::DeviceAttribute &dev_attr, const bool isImage, const bopy::object &py_value)
{
    typedef typename TANGO_const2type(tangoTypeConst) TangoScalarType;
    typedef typename TANGO_const2arraytype(tangoTypeConst) TangoArrayType;

    CORBA::ULong dim_x, dim_y, nelems;

    // -- Check the dimensions
    if(isImage)
    {
        dim_y = static_cast<CORBA::ULong>(bopy::len(py_value));
        dim_x = static_cast<CORBA::ULong>(bopy::len(py_value[0]));
        nelems = dim_x * dim_y;
    }
    else
    {
        dim_x = static_cast<CORBA::ULong>(bopy::len(py_value));
        dim_y = 0;
        nelems = dim_x;
    }

    // -- Allocate memory
    unique_pointer<TangoArrayType> value;
    TangoScalarType *buffer = TangoArrayType::allocbuf(nelems);
    try
    {
        value.reset(new TangoArrayType(nelems, nelems, buffer, true));
    }
    catch(...)
    {
        TangoArrayType::freebuf(buffer);
        throw;
    }

    // -- Copy the sequence to the newly created buffer
    if(isImage)
    {
        for(CORBA::ULong y = 0; y < dim_y; ++y)
        {
            bopy::object py_sub = py_value[y];
            CORBA::ULong len_py_sub = static_cast<CORBA::ULong>(bopy::len(py_sub));
            if(len_py_sub != dim_x)
            {
                raise_(PyExc_TypeError, non_valid_image);
            }
            for(CORBA::ULong x = 0; x < dim_x; ++x)
            {
                python_tangocpp<tangoTypeConst>::to_cpp(py_sub[x], buffer[x + y * dim_x]);
            }
        }
    }
    else
    {
        for(CORBA::ULong x = 0; x < dim_x; ++x)
        {
            python_tangocpp<tangoTypeConst>::to_cpp(py_value[x], buffer[x]);
        }
    }

    // -- Insert it into the dev_attr
    dev_attr.insert(value.get(), dim_x, dim_y);

    // -- Final cleaning
    value.release(); // Do not delete value, it is handled by dev_attr now!
}

template <>
inline void _fill_list_attribute<Tango::DEV_ENCODED>(Tango::DeviceAttribute &dev_attr,
                                                     const bool isImage,
                                                     const bopy::object &py_value)
{
    /// @todo really? This is really not gonna happen?
    // Unsupported
    assert(false);
}

template <long tangoTypeConst>
static inline void _fill_scalar_attribute(Tango::DeviceAttribute &dev_attr, const bopy::object &py_value)
{
    typedef typename TANGO_const2type(tangoTypeConst) TangoScalarType;

    TangoScalarType value;
    from_py<tangoTypeConst>::convert(py_value.ptr(), value);
    dev_attr << const_cast<TangoScalarType &>(value);
}

template <>
inline void _fill_scalar_attribute<Tango::DEV_STRING>(Tango::DeviceAttribute &dev_attr, const bopy::object &py_value)
{
    Tango::DevString value = from_str_to_char(py_value.ptr());
    dev_attr << value;
    delete[] value;
}

template <>
inline void _fill_scalar_attribute<Tango::DEV_ENCODED>(Tango::DeviceAttribute &dev_attr, const bopy::object &py_value)
{
    if(bopy::len(py_value) != 2)
    {
        raise_(PyExc_TypeError, "Expecting a tuple of strings: encoded_format, encoded_data");
    }

    bopy::object encoded_format_str = py_value[0];
    bopy::object encoded_data_str = py_value[1];

    // todo second parameter of insert is a reference, and it does not take ownership of the pointer
    // so to be 100% sure, we have to copy data. However, in this case we have to have an option to control release
    // parameter. At the moment (cppTango 9.4.1) it is not realized, so we pass pointer to data and Python's gb destroys
    // object this is a source of bugs. Somehow it works, but no idea why.

    char *encoded_format = const_cast<char *>((bopy::extract<const char *>(encoded_format_str)()));

    Py_ssize_t encoded_data_len = bopy::len(encoded_data_str);
    PyObject *encoded_data_obj = encoded_data_str.ptr();
    unsigned char *encoded_data;

    if(PyUnicode_Check(encoded_data_obj))
    {
        Py_ssize_t size;
        encoded_data = reinterpret_cast<unsigned char *>((char *) PyUnicode_AsUTF8AndSize(encoded_data_obj, &size));
        dev_attr.insert(encoded_format, encoded_data, static_cast<unsigned int>(size));
    }
    else if(PyBytes_Check(encoded_data_obj) || PyByteArray_Check(encoded_data_obj))
    {
        Py_buffer view;

        if(PyObject_GetBuffer(encoded_data_obj, &view, PyBUF_FULL_RO) < 0)
        {
            raise_(PyExc_TypeError, "Cannot convert encoded data");
        }

        encoded_data = reinterpret_cast<unsigned char *>((char *) view.buf);
        dev_attr.insert(encoded_format, encoded_data, static_cast<unsigned int>(encoded_data_len));
        PyBuffer_Release(&view);
    }
    else
    {
        raise_(PyExc_TypeError, "Encoded_data can be str, bytes or bytearray");
    }
}

static inline bopy::object undefined_attribute(Tango::DeviceAttribute *self)
{
    return bopy::object(); // None
}

void reset_values(Tango::DeviceAttribute &self, int data_type, Tango::AttrDataFormat data_format, bopy::object py_value)
{
    bool isImage = false;
    switch(data_format)
    {
    case Tango::SCALAR:
        TANGO_CALL_ON_ATTRIBUTE_DATA_TYPE_ID(data_type, _fill_scalar_attribute, self, py_value);
        break;
    case Tango::IMAGE:
        isImage = true;
    case Tango::SPECTRUM:
        // Why on earth? Why do we define _fill_numpy_attribute instead
        // of just using _fill_list_attribute, if the latter accepts
        // anything with operators "[]" and "len" defined?
        // Well it seems that PyArray_GETITEM does something diferent
        // and I get a value transformed into a python basic type,
        // while py_value[y][x] gives me a numpy type (ej: numpy.bool_).
        // Then the conversions between numpy types to c++ are not
        // defined by boost while the conversions between python
        // standard types and C++ are.
        if(PyArray_Check(py_value.ptr()))
        {
            TANGO_CALL_ON_ATTRIBUTE_DATA_TYPE_ID(data_type, _fill_numpy_attribute, self, isImage, py_value);
        }
        else
        {
            TANGO_CALL_ON_ATTRIBUTE_DATA_TYPE_ID(data_type, _fill_list_attribute, self, isImage, py_value);
        }
        break;
    default:
        raise_(PyExc_TypeError, "unsupported data_format.");
    }
}

void reset(Tango::DeviceAttribute &self, const Tango::AttributeInfo &attr_info, bopy::object py_value)
{
    self.set_name(attr_info.name.c_str());
    reset_values(self, attr_info.data_type, attr_info.data_format, py_value);
}

void reset(Tango::DeviceAttribute &self,
           const std::string &attr_name,
           Tango::DeviceProxy &dev_proxy,
           bopy::object py_value)
{
    self.set_name(attr_name.c_str());
    Tango::AttributeInfoEx attr_info;
    {
        AutoPythonAllowThreads guard;
        try
        {
            attr_info = dev_proxy.get_attribute_config(attr_name);
        }
        catch(...)
        {
        }
    }
    reset_values(self, attr_info.data_type, attr_info.data_format, py_value);
}
}; // namespace PyDeviceAttribute

void export_device_attribute()
{
    bopy::class_<Tango::DeviceAttribute> DeviceAttribute("DeviceAttribute", bopy::init<>());

    bopy::scope da_scope = DeviceAttribute;

    bopy::enum_<Tango::DeviceAttribute::except_flags>("except_flags")
        .value("isempty_flag", Tango::DeviceAttribute::isempty_flag)
        .value("wrongtype_flag", Tango::DeviceAttribute::wrongtype_flag)
        .value("failed_flag", Tango::DeviceAttribute::failed_flag)
        .value("numFlags", Tango::DeviceAttribute::numFlags);

    DeviceAttribute.def(bopy::init<const Tango::DeviceAttribute &>())
        .def_readwrite("name", &Tango::DeviceAttribute::name)
        .def_readwrite("quality", &Tango::DeviceAttribute::quality)
        .def_readwrite("time", &Tango::DeviceAttribute::time)
        .add_property("dim_x", &Tango::DeviceAttribute::get_dim_x)
        .add_property("dim_y", &Tango::DeviceAttribute::get_dim_y)
        .add_property("w_dim_x", &Tango::DeviceAttribute::get_written_dim_x)
        .add_property("w_dim_y", &Tango::DeviceAttribute::get_written_dim_y)
        .add_property("r_dimension", &Tango::DeviceAttribute::get_r_dimension)
        .add_property("w_dimension", &Tango::DeviceAttribute::get_w_dimension)
        .add_property("nb_read", &Tango::DeviceAttribute::get_nb_read)
        .add_property("nb_written", &Tango::DeviceAttribute::get_nb_written)
        .add_property("data_format", &Tango::DeviceAttribute::get_data_format)
        .def("get_date", &Tango::DeviceAttribute::get_date, bopy::return_internal_reference<>())
        .def("get_err_stack",
             &Tango::DeviceAttribute::get_err_stack,
             bopy::return_value_policy<bopy::copy_const_reference>())
        .def("set_w_dim_x", &Tango::DeviceAttribute::set_w_dim_x)
        .def("set_w_dim_y", &Tango::DeviceAttribute::set_w_dim_y);
}
