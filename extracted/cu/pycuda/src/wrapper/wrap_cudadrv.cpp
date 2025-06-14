#define PY_ARRAY_UNIQUE_SYMBOL pycuda_ARRAY_API

#include <cuda.hpp>

#include <utility>
#include <numeric>
#include <algorithm>

#include "tools.hpp"
#include "wrap_helpers.hpp"
#include <boost/python/stl_iterator.hpp>

#if NPY_ABI_VERSION < 0x02000000
  #define PyDataType_ELSIZE(descr) ((descr)->elsize)
#endif



#if CUDAPP_CUDA_VERSION < 1010
#error PyCuda only works with CUDA 1.1 or newer.
#endif




using namespace pycuda;
using boost::shared_ptr;




namespace
{
  // {{{ error handling

  py::handle<>
    CudaError,
    CudaMemoryError,
    CudaLogicError,
    CudaRuntimeError,
    CudaLaunchError;




  void translate_cuda_error(const pycuda::error &err)
  {
    if (err.code() == CUDA_ERROR_LAUNCH_FAILED
        || err.code() == CUDA_ERROR_LAUNCH_OUT_OF_RESOURCES
        || err.code() == CUDA_ERROR_LAUNCH_TIMEOUT
        || err.code() == CUDA_ERROR_LAUNCH_INCOMPATIBLE_TEXTURING
       )
      PyErr_SetString(CudaLaunchError.get(), err.what());
    else if (err.code() == CUDA_ERROR_OUT_OF_MEMORY)
      PyErr_SetString(CudaMemoryError.get(), err.what());
    else if (err.code() == CUDA_ERROR_NO_DEVICE
        || err.code() == CUDA_ERROR_NO_BINARY_FOR_GPU
        || err.code() == CUDA_ERROR_NO_BINARY_FOR_GPU
        || err.code() == CUDA_ERROR_FILE_NOT_FOUND
        || err.code() == CUDA_ERROR_NOT_READY
#if CUDAPP_CUDA_VERSION >= 3000 && defined(CUDAPP_POST_30_BETA)
        || err.code() == CUDA_ERROR_ECC_UNCORRECTABLE
#endif
        )
      PyErr_SetString(CudaRuntimeError.get(), err.what());
    else if (err.code() == CUDA_ERROR_UNKNOWN)
      PyErr_SetString(CudaError.get(), err.what());
    else
      PyErr_SetString(CudaLogicError.get(), err.what());
  }

  // }}}

  py::tuple cuda_version()
  {
    return py::make_tuple(
        CUDAPP_CUDA_VERSION / 1000,
        (CUDAPP_CUDA_VERSION % 1000)/10,
        CUDAPP_CUDA_VERSION % 10);
  }



  class host_alloc_flags { };
  class mem_host_register_flags { };
  class mem_peer_register_flags { };
  class array3d_flags { };



  // {{{ "python-aware" wrappers

  py::object device_get_attribute(device const &dev, CUdevice_attribute attr)
  {
#if CUDAPP_CUDA_VERSION >= 2020
    if (attr == CU_DEVICE_ATTRIBUTE_COMPUTE_MODE)
      return py::object(CUcomputemode(dev.get_attribute(attr)));
    else
#endif
      return py::object(dev.get_attribute(attr));
  }



  device_allocation *mem_alloc_wrap(size_t bytes)
  {
    return new device_allocation(pycuda::mem_alloc_gc(bytes));
  }

  class pointer_holder_base_wrap
    : public pointer_holder_base,
    public py::wrapper<pointer_holder_base>
  {
    public:
      CUdeviceptr get_pointer() const
      {
        return this->get_override("get_pointer")();
      }
  };

  py::tuple mem_alloc_pitch_wrap(
      size_t width, size_t height, unsigned int access_size)
  {
    std::unique_ptr<device_allocation> da;
    Py_ssize_t pitch = mem_alloc_pitch(
        da, width, height, access_size);
    return py::make_tuple(
        handle_from_new_ptr(da.release()), pitch);
  }

  // {{{ memory set

  void  py_memset_d8(CUdeviceptr dst, unsigned char uc, size_t n )
  { CUDAPP_CALL_GUARDED_THREADED(cuMemsetD8, (dst, uc, n )); }
  void  py_memset_d16(CUdeviceptr dst, unsigned short us, size_t n )
  { CUDAPP_CALL_GUARDED_THREADED(cuMemsetD16, (dst, us, n )); }
  void  py_memset_d32(CUdeviceptr dst, unsigned int ui, size_t n )
  { CUDAPP_CALL_GUARDED_THREADED(cuMemsetD32, (dst, ui, n )); }

  void  py_memset_d2d8(CUdeviceptr dst, size_t dst_pitch,
      unsigned char uc, size_t width, size_t height )
  { CUDAPP_CALL_GUARDED_THREADED(cuMemsetD2D8, (dst, dst_pitch, uc, width, height)); }

  void  py_memset_d2d16(CUdeviceptr dst, size_t dst_pitch,
      unsigned short us, size_t width, size_t height )
  { CUDAPP_CALL_GUARDED_THREADED(cuMemsetD2D16, (dst, dst_pitch, us, width, height)); }

  void  py_memset_d2d32(CUdeviceptr dst, size_t dst_pitch,
      unsigned int ui, size_t width, size_t height )
  { CUDAPP_CALL_GUARDED_THREADED(cuMemsetD2D32, (dst, dst_pitch, ui, width, height)); }

  // }}}

  // {{{ memory set async

  void  py_memset_d8_async(CUdeviceptr dst, unsigned char uc, size_t n, py::object stream_py )
  {
      PYCUDA_PARSE_STREAM_PY;
      CUDAPP_CALL_GUARDED_THREADED(cuMemsetD8Async, (dst, uc, n, s_handle));
  }
  void  py_memset_d16_async(CUdeviceptr dst, unsigned short us, size_t n, py::object stream_py )
  {
      PYCUDA_PARSE_STREAM_PY;
      CUDAPP_CALL_GUARDED_THREADED(cuMemsetD16Async, (dst, us, n, s_handle));
  }
  void  py_memset_d32_async(CUdeviceptr dst, unsigned int ui, size_t n, py::object stream_py )
  {
      PYCUDA_PARSE_STREAM_PY;
      CUDAPP_CALL_GUARDED_THREADED(cuMemsetD32Async, (dst, ui, n, s_handle));
  }

  void  py_memset_d2d8_async(CUdeviceptr dst, size_t dst_pitch,
      unsigned char uc, size_t width, size_t height, py::object stream_py )
  {
      PYCUDA_PARSE_STREAM_PY;
      CUDAPP_CALL_GUARDED_THREADED(cuMemsetD2D8Async, (dst, dst_pitch, uc, width, height, s_handle));
  }

  void  py_memset_d2d16_async(CUdeviceptr dst, size_t dst_pitch,
      unsigned short us, size_t width, size_t height, py::object stream_py )
  {
      PYCUDA_PARSE_STREAM_PY;
      CUDAPP_CALL_GUARDED_THREADED(cuMemsetD2D16Async, (dst, dst_pitch, us, width, height, s_handle));
  }

  void  py_memset_d2d32_async(CUdeviceptr dst, size_t dst_pitch,
      unsigned int ui, size_t width, size_t height, py::object stream_py )
  {
      PYCUDA_PARSE_STREAM_PY;
      CUDAPP_CALL_GUARDED_THREADED(cuMemsetD2D32Async, (dst, dst_pitch, ui, width, height, s_handle));
  }

  // }}}

  // {{{ memory copies

  void py_memcpy_htod(CUdeviceptr dst, py::object src)
  {
    py_buffer_wrapper buf_wrapper;
    buf_wrapper.get(src.ptr(), PyBUF_ANY_CONTIGUOUS);

    CUDAPP_CALL_GUARDED_THREADED(cuMemcpyHtoD,
        (dst, buf_wrapper.m_buf.buf, buf_wrapper.m_buf.len));
  }




  void py_memcpy_htod_async(CUdeviceptr dst, py::object src, py::object stream_py)
  {
    py_buffer_wrapper buf_wrapper;
    buf_wrapper.get(src.ptr(), PyBUF_ANY_CONTIGUOUS);

    PYCUDA_PARSE_STREAM_PY;

    CUDAPP_CALL_GUARDED_THREADED(cuMemcpyHtoDAsync,
        (dst, buf_wrapper.m_buf.buf, buf_wrapper.m_buf.len, s_handle));
  }




  void py_memcpy_dtoh(py::object dest, CUdeviceptr src)
  {
    py_buffer_wrapper buf_wrapper;
    buf_wrapper.get(dest.ptr(), PyBUF_ANY_CONTIGUOUS | PyBUF_WRITABLE);

    CUDAPP_CALL_GUARDED_THREADED(cuMemcpyDtoH,
        (buf_wrapper.m_buf.buf, src, buf_wrapper.m_buf.len));
  }




  void py_memcpy_dtoh_async(py::object dest, CUdeviceptr src, py::object stream_py)
  {
    py_buffer_wrapper buf_wrapper;
    buf_wrapper.get(dest.ptr(), PyBUF_ANY_CONTIGUOUS | PyBUF_WRITABLE);

    PYCUDA_PARSE_STREAM_PY;

    CUDAPP_CALL_GUARDED_THREADED(cuMemcpyDtoHAsync,
        (buf_wrapper.m_buf.buf, src, buf_wrapper.m_buf.len, s_handle));
  }




  void py_memcpy_htoa(array const &ary, unsigned int index, py::object src)
  {
    py_buffer_wrapper buf_wrapper;
    buf_wrapper.get(src.ptr(), PyBUF_ANY_CONTIGUOUS);

    CUDAPP_CALL_GUARDED_THREADED(cuMemcpyHtoA,
        (ary.handle(), index, buf_wrapper.m_buf.buf, buf_wrapper.m_buf.len));
  }




  void py_memcpy_atoh(py::object dest, array const &ary, unsigned int index)
  {
    py_buffer_wrapper buf_wrapper;
    buf_wrapper.get(dest.ptr(), PyBUF_ANY_CONTIGUOUS | PyBUF_WRITABLE);

    CUDAPP_CALL_GUARDED_THREADED(cuMemcpyAtoH,
        (buf_wrapper.m_buf.buf, ary.handle(), index, buf_wrapper.m_buf.len));
  }




  void  py_memcpy_dtod(CUdeviceptr dest, CUdeviceptr src,
      size_t byte_count)
  { CUDAPP_CALL_GUARDED_THREADED(cuMemcpyDtoD, (dest, src, byte_count)); }




#if CUDAPP_CUDA_VERSION >= 3000
  void  py_memcpy_dtod_async(CUdeviceptr dest, CUdeviceptr src,
      size_t byte_count, py::object stream_py)
  {
    PYCUDA_PARSE_STREAM_PY;

    CUDAPP_CALL_GUARDED_THREADED(cuMemcpyDtoDAsync,
        (dest, src, byte_count, s_handle));
  }
#endif

#if CUDAPP_CUDA_VERSION >= 4000
  void  py_memcpy_peer(CUdeviceptr dest, CUdeviceptr src,
      size_t byte_count,
      py::object dest_context_py, py::object src_context_py
      )
  {
    boost::shared_ptr<context> dest_context = context::current_context();
    boost::shared_ptr<context> src_context = dest_context;

    if (dest_context_py.ptr() == Py_None)
      dest_context = py::extract<boost::shared_ptr<context> >(dest_context_py);

    if (src_context_py.ptr() == Py_None)
      src_context = py::extract<boost::shared_ptr<context> >(src_context_py);

    CUDAPP_CALL_GUARDED_THREADED(cuMemcpyPeer, (
          dest, dest_context->handle(),
          src, src_context->handle(),
          byte_count));
  }

  void  py_memcpy_peer_async(CUdeviceptr dest, CUdeviceptr src,
      size_t byte_count,
      py::object dest_context_py, py::object src_context_py,
      py::object stream_py)
  {
    boost::shared_ptr<context> dest_context = context::current_context();
    boost::shared_ptr<context> src_context = dest_context;

    if (dest_context_py.ptr() == Py_None)
      dest_context = py::extract<boost::shared_ptr<context> >(dest_context_py);

    if (src_context_py.ptr() == Py_None)
      src_context = py::extract<boost::shared_ptr<context> >(src_context_py);

    PYCUDA_PARSE_STREAM_PY

    CUDAPP_CALL_GUARDED_THREADED(cuMemcpyPeerAsync, (
          dest, dest_context->handle(),
          src, src_context->handle(),
          byte_count, s_handle));
  }
#endif

  // }}}

  // }}}

  void function_param_setv(function &f, int offset, py::object buffer)
  {
    py_buffer_wrapper buf_wrapper;
    buf_wrapper.get(buffer.ptr(), PyBUF_ANY_CONTIGUOUS);

    f.param_setv(
        offset,
        const_cast<void *>(buf_wrapper.m_buf.buf),
        buf_wrapper.m_buf.len);
  }




  // {{{ module_from_buffer

  module *module_from_buffer(py::object buffer, py::object py_options,
      py::object message_handler)
  {
    PYCUDA_BUFFER_SIZE_T len;
    py_buffer_wrapper py_buf;
    py_buf.get(buffer.ptr(), PyBUF_ANY_CONTIGUOUS);
    CUmodule mod;

#if CUDAPP_CUDA_VERSION >= 2010
    const size_t buf_size = 32768;
    char info_buf[buf_size], error_buf[buf_size];

    std::vector<CUjit_option> options;
    std::vector<void *> option_values;

#define ADD_OPTION_PTR(KEY, PTR) \
    { \
      options.push_back(KEY); \
      option_values.push_back(PTR); \
    }

    ADD_OPTION_PTR(CU_JIT_INFO_LOG_BUFFER, info_buf);
    ADD_OPTION_PTR(CU_JIT_INFO_LOG_BUFFER_SIZE_BYTES, (void *) buf_size);
    ADD_OPTION_PTR(CU_JIT_ERROR_LOG_BUFFER, error_buf);
    ADD_OPTION_PTR(CU_JIT_ERROR_LOG_BUFFER_SIZE_BYTES, (void *) buf_size);

    PYTHON_FOREACH(key_value, py_options)
      ADD_OPTION_PTR(
          py::extract<CUjit_option>(key_value[0]),
          (void *) py::extract<intptr_t>(key_value[1])());
#undef ADD_OPTION

    CUDAPP_PRINT_CALL_TRACE("cuModuleLoadDataEx");
    CUresult cu_status_code; \
    cu_status_code = cuModuleLoadDataEx(&mod, py_buf.m_buf.buf, (unsigned int) options.size(),
         const_cast<CUjit_option *>(&*options.begin()),
         const_cast<void **>(&*option_values.begin()));

    size_t info_buf_size = size_t(option_values[1]);
    size_t error_buf_size = size_t(option_values[3]);

    if (message_handler != py::object())
      message_handler(cu_status_code == CUDA_SUCCESS,
          std::string(info_buf, info_buf_size),
          std::string(error_buf, error_buf_size));

    if (cu_status_code != CUDA_SUCCESS)
      throw pycuda::error("cuModuleLoadDataEx", cu_status_code,
          std::string(error_buf, error_buf_size).c_str());
#else
    if (py::len(py_options))
      throw pycuda::error("module_from_buffer", CUDA_ERROR_INVALID_VALUE,
          "non-empty options argument only supported on CUDA 2.1 and newer");

    CUDAPP_CALL_GUARDED(cuModuleLoadData, (&mod, py_buf.buf));
#endif

    return new module(mod);
  }

  // }}}

  // {{{ linker

#if CUDAPP_CUDA_VERSION >= 5050
  class Linker : public boost::noncopyable
  {
    private:
      py::object m_message_handler;
      CUlinkState m_link_state;
      bool m_log_verbose;
      std::vector<CUjit_option> m_options;
      std::vector<void *> m_values;
      char m_info_buf[32768];
      char m_error_buf[32768];

      void close() {
        if (m_link_state != NULL) {
          cuLinkDestroy(m_link_state);
          m_link_state = NULL;
        }
      }

      template<typename T>
      void add_option(CUjit_option option, T value) {
        m_options.push_back(option);
        m_values.push_back(reinterpret_cast<void *>(value));
      }

      void check_cu_result(const char* cu_function_name, CUresult cu_result) const {
        if (cu_result != CUDA_SUCCESS) {
          call_message_handler(cu_result);
          throw pycuda::error(cu_function_name, cu_result, error_str().c_str());
        }
      }

      void call_message_handler(CUresult cu_result) const {
        if (m_message_handler != py::object()) {
          m_message_handler(cu_result == CUDA_SUCCESS, info_str(), error_str());
        }
      }

      const std::string info_str() const {
        return std::string(m_info_buf, size_t(m_values[1]));
      }

      const std::string error_str() const {
        return std::string(m_error_buf, size_t(m_values[3]));
      }

    public:
      Linker(py::object message_handler = py::object(),
             py::object py_options = py::object(),
             py::object py_log_verbose = py::object(false))
        : m_message_handler(message_handler),
          m_link_state(),
          m_log_verbose(py::extract<bool>(py_log_verbose))
      {
        add_option(CU_JIT_INFO_LOG_BUFFER, m_info_buf);
        add_option(CU_JIT_INFO_LOG_BUFFER_SIZE_BYTES, sizeof(m_info_buf));
        add_option(CU_JIT_ERROR_LOG_BUFFER, m_error_buf);
        add_option(CU_JIT_ERROR_LOG_BUFFER_SIZE_BYTES, sizeof(m_error_buf));
        add_option(CU_JIT_LOG_VERBOSE, m_log_verbose? 1ull : 0ull);

        if (py_options.ptr() != Py_None) {
          PYTHON_FOREACH(key_value, py_options) {
            add_option(
                py::extract<CUjit_option>(key_value[0]),
                py::extract<intptr_t>(key_value[1])());
          }
        }

        const CUresult cu_result = cuLinkCreate(
            (unsigned int) m_options.size(),
            const_cast<CUjit_option *>(&*m_options.begin()),
            const_cast<void **>(&*m_values.begin()),
            &m_link_state);
        check_cu_result("cuLinkCreate", cu_result);
      }

      ~Linker()
      {
        close();
      }

      void add_data(py::object py_data, CUjitInputType input_type, py::str py_name)
      {
	Py_buffer py_buf;
        PYCUDA_BUFFER_SIZE_T data_buf_len;
        if (PyObject_GetBuffer(py_data.ptr(), &py_buf, PyBUF_ANY_CONTIGUOUS)) {
          throw py::error_already_set();
        }
        const char* name = (py_name.ptr() != Py_None)?
            py::extract<const char*>(py_name) : NULL;
        const CUresult cu_result = cuLinkAddData(m_link_state, input_type, py_buf.buf,
            py_buf.len, name, 0, NULL, NULL);
	PyBuffer_Release(&py_buf);
        check_cu_result("cuLinkAddData", cu_result);
      }

      void add_file(py::str py_filename, CUjitInputType input_type)
      {
        const char* filename = py::extract<const char*>(py_filename);
        const CUresult cu_result = cuLinkAddFile(m_link_state, input_type,
            filename, 0, NULL, NULL);
        check_cu_result("cuLinkAddFile", cu_result);
      }

      module* link_module()
      {
        char* cubin_data = NULL;
        size_t cubin_size = 0;
        CUresult cu_result = cuLinkComplete(m_link_state,
            reinterpret_cast<void **>(&cubin_data), &cubin_size);
        check_cu_result("cuLinkComplete", cu_result);

        CUmodule cu_module = NULL;
        cu_result = cuModuleLoadData(&cu_module, cubin_data);
        check_cu_result("cuModuleLoadData", cu_result);

        call_message_handler(cu_result);
        close();

        return new module(cu_module);
      }
  };
#endif

  // }}}

  template <class T>
  PyObject *mem_obj_to_long(T const &mo)
  {
#if defined(_WIN32) && defined(_WIN64)
    return PyLong_FromUnsignedLongLong((CUdeviceptr) mo);
#else
    return PyLong_FromUnsignedLong((CUdeviceptr) mo);
#endif
  }

  // {{{ special host memory <-> numpy

  template <class Allocation>
  py::handle<> numpy_empty(py::object shape, py::object dtype,
      py::object order_py, unsigned par1)
  {
    PyArray_Descr *tp_descr;
    if (PyArray_DescrConverter(dtype.ptr(), &tp_descr) != NPY_SUCCEED)
      throw py::error_already_set();

    py::extract<npy_intp> shape_as_int(shape);
    std::vector<npy_intp> dims;

    if (shape_as_int.check())
      dims.push_back(shape_as_int());
    else
      std::copy(
          py::stl_input_iterator<npy_intp>(shape),
          py::stl_input_iterator<npy_intp>(),
          back_inserter(dims));

    std::unique_ptr<Allocation> alloc(
        new Allocation(
          PyDataType_ELSIZE(tp_descr)*pycuda::size_from_dims(dims.size(), &dims.front()),
          par1)
        );

    NPY_ORDER order = NPY_CORDER;
    PyArray_OrderConverter(order_py.ptr(), &order);

    int ary_flags = 0;
    if (order == NPY_FORTRANORDER)
      ary_flags |= NPY_ARRAY_FARRAY;
    else if (order == NPY_CORDER)
      ary_flags |= NPY_ARRAY_CARRAY;
    else
      throw pycuda::error("numpy_empty", CUDA_ERROR_INVALID_VALUE,
          "unrecognized order specifier");

    py::handle<> result = py::handle<>(PyArray_NewFromDescr(
        &PyArray_Type, tp_descr,
        int(dims.size()), &dims.front(), /*strides*/ NULL,
        alloc->data(), ary_flags, /*obj*/NULL));

    py::handle<> alloc_py(handle_from_new_ptr(alloc.release()));
    PyArray_SetBaseObject((PyArrayObject*)result.get(), alloc_py.get());
    Py_INCREF(alloc_py.get());

    return result;
  }

#if CUDAPP_CUDA_VERSION >= 4000
  py::handle<> register_host_memory(py::object ary, unsigned flags)
  {
    if (!PyArray_Check(ary.ptr()))
      throw pycuda::error("register_host_memory", CUDA_ERROR_INVALID_VALUE,
          "ary argument is not a numpy array");

    if (!PyArray_ISCONTIGUOUS((PyArrayObject*)ary.ptr()))
      throw pycuda::error("register_host_memory", CUDA_ERROR_INVALID_VALUE,
          "ary argument is not contiguous");

    std::unique_ptr<registered_host_memory> regmem(
        new registered_host_memory(
          PyArray_DATA((PyArrayObject*)ary.ptr()),
          PyArray_NBYTES((PyArrayObject*)ary.ptr()),
          flags, ary));

    PyObject *new_array_ptr = PyArray_FromInterface(ary.ptr());
    if (new_array_ptr == Py_NotImplemented)
      throw pycuda::error("register_host_memory", CUDA_ERROR_INVALID_VALUE,
          "ary argument does not expose array interface");

    py::handle<> result(new_array_ptr);

    py::handle<> regmem_py(handle_from_new_ptr(regmem.release()));
    // ValueError: Cannot set the NumPy array 'base' dependency more than once
    PyArray_SetBaseObject((PyArrayObject*)result.get(), regmem_py.get());
    Py_INCREF(regmem_py.get());

    return result;
  }
#endif

  // }}}

  // }}}




  bool have_gl_ext()
  {
#ifdef HAVE_GL
    return true;
#else
    return false;
#endif
  }
}




void pycuda_expose_tools();
void pycuda_expose_gl();
void pycuda_expose_curand();




static bool import_numpy_helper()
{
  import_array1(false);
  return true;
}


BOOST_PYTHON_MODULE(_driver)
{
  if (!import_numpy_helper())
    throw py::error_already_set();

  py::def("get_version", cuda_version);
#if CUDAPP_CUDA_VERSION >= 2020
  py::def("get_driver_version", pycuda::get_driver_version);
#endif

  // {{{ exceptions

#define DECLARE_EXC(NAME, BASE) \
  Cuda##NAME = py::handle<>(PyErr_NewException("pycuda._driver." #NAME, BASE, NULL)); \
  py::scope().attr(#NAME) = Cuda##NAME;

  {
    DECLARE_EXC(Error, NULL);
    DECLARE_EXC(MemoryError, CudaError.get());
    DECLARE_EXC(LogicError, CudaError.get());
    DECLARE_EXC(LaunchError, CudaError.get());
    DECLARE_EXC(RuntimeError, CudaError.get());

    py::register_exception_translator<pycuda::error>(translate_cuda_error);
  }

  // }}}

  // {{{ constants
#if CUDAPP_CUDA_VERSION >= 4010
  py::enum_<CUipcMem_flags>("ipc_mem_flags")
    .value("LAZY_ENABLE_PEER_ACCESS", CU_IPC_MEM_LAZY_ENABLE_PEER_ACCESS)
    ;
#endif

#if CUDAPP_CUDA_VERSION >= 2000
  py::enum_<CUctx_flags>("ctx_flags")
    .value("SCHED_AUTO", CU_CTX_SCHED_AUTO)
    .value("SCHED_SPIN", CU_CTX_SCHED_SPIN)
    .value("SCHED_YIELD", CU_CTX_SCHED_YIELD)
    .value("SCHED_MASK", CU_CTX_SCHED_MASK)
#if CUDAPP_CUDA_VERSION >= 2020 && CUDAPP_CUDA_VERSION < 4000
    .value("BLOCKING_SYNC", CU_CTX_BLOCKING_SYNC)
    .value("SCHED_BLOCKING_SYNC", CU_CTX_BLOCKING_SYNC)
#endif
#if CUDAPP_CUDA_VERSION >= 4000
    .value("BLOCKING_SYNC", CU_CTX_SCHED_BLOCKING_SYNC)
    .value("SCHED_BLOCKING_SYNC", CU_CTX_SCHED_BLOCKING_SYNC)
#endif
#if CUDAPP_CUDA_VERSION >= 2020
    .value("MAP_HOST", CU_CTX_MAP_HOST)
#endif
#if CUDAPP_CUDA_VERSION >= 3020
    .value("LMEM_RESIZE_TO_MAX", CU_CTX_LMEM_RESIZE_TO_MAX)
#endif
    .value("FLAGS_MASK", CU_CTX_FLAGS_MASK)
    ;
#endif

#if CUDAPP_CUDA_VERSION >= 2020
  py::enum_<CUevent_flags>("event_flags")
    .value("DEFAULT", CU_EVENT_DEFAULT)
    .value("BLOCKING_SYNC", CU_EVENT_BLOCKING_SYNC)
#if CUDAPP_CUDA_VERSION >= 3020
    .value("DISABLE_TIMING", CU_EVENT_DISABLE_TIMING)
#endif
#if CUDAPP_CUDA_VERSION >= 4010
    .value("INTERPROCESS", CU_EVENT_INTERPROCESS)
#endif
    ;
#endif

  py::enum_<CUarray_format>("array_format")
    .value("UNSIGNED_INT8", CU_AD_FORMAT_UNSIGNED_INT8)
    .value("UNSIGNED_INT16", CU_AD_FORMAT_UNSIGNED_INT16)
    .value("UNSIGNED_INT32", CU_AD_FORMAT_UNSIGNED_INT32)
    .value("SIGNED_INT8"   , CU_AD_FORMAT_SIGNED_INT8)
    .value("SIGNED_INT16"  , CU_AD_FORMAT_SIGNED_INT16)
    .value("SIGNED_INT32"  , CU_AD_FORMAT_SIGNED_INT32)
    .value("HALF"          , CU_AD_FORMAT_HALF)
    .value("FLOAT"         , CU_AD_FORMAT_FLOAT)
    ;

#if CUDAPP_CUDA_VERSION >= 3000
  {
    py::class_<array3d_flags> cls("array3d_flags", py::no_init);
    // deprecated
    cls.attr("ARRAY3D_2DARRAY") = CUDA_ARRAY3D_2DARRAY;
#if CUDAPP_CUDA_VERSION >= 4000
    cls.attr("ARRAY3D_LAYERED") = CUDA_ARRAY3D_LAYERED;
#endif

    cls.attr("2DARRAY") = CUDA_ARRAY3D_2DARRAY;
#if CUDAPP_CUDA_VERSION >= 3010
    cls.attr("SURFACE_LDST") = CUDA_ARRAY3D_SURFACE_LDST;
#endif
#if CUDAPP_CUDA_VERSION >= 4010
    cls.attr("CUBEMAP") = CUDA_ARRAY3D_CUBEMAP;
    cls.attr("TEXTURE_GATHER") = CUDA_ARRAY3D_TEXTURE_GATHER;
#endif
  }
#endif

  py::enum_<CUaddress_mode>("address_mode")
    .value("WRAP", CU_TR_ADDRESS_MODE_WRAP)
    .value("CLAMP", CU_TR_ADDRESS_MODE_CLAMP)
    .value("MIRROR", CU_TR_ADDRESS_MODE_MIRROR)
#if CUDAPP_CUDA_VERSION >= 3020
    .value("BORDER", CU_TR_ADDRESS_MODE_BORDER)
#endif
    ;

  py::enum_<CUfilter_mode>("filter_mode")
    .value("POINT", CU_TR_FILTER_MODE_POINT)
    .value("LINEAR", CU_TR_FILTER_MODE_LINEAR)
    ;
  py::enum_<CUdevice_attribute>("device_attribute")
    .value("MAX_THREADS_PER_BLOCK", CU_DEVICE_ATTRIBUTE_MAX_THREADS_PER_BLOCK)
    .value("MAX_BLOCK_DIM_X", CU_DEVICE_ATTRIBUTE_MAX_BLOCK_DIM_X)
    .value("MAX_BLOCK_DIM_Y", CU_DEVICE_ATTRIBUTE_MAX_BLOCK_DIM_Y)
    .value("MAX_BLOCK_DIM_Z", CU_DEVICE_ATTRIBUTE_MAX_BLOCK_DIM_Z)
    .value("MAX_GRID_DIM_X", CU_DEVICE_ATTRIBUTE_MAX_GRID_DIM_X)
    .value("MAX_GRID_DIM_Y", CU_DEVICE_ATTRIBUTE_MAX_GRID_DIM_Y)
    .value("MAX_GRID_DIM_Z", CU_DEVICE_ATTRIBUTE_MAX_GRID_DIM_Z)
#if CUDAPP_CUDA_VERSION >= 2000
    .value("MAX_SHARED_MEMORY_PER_BLOCK", CU_DEVICE_ATTRIBUTE_MAX_SHARED_MEMORY_PER_BLOCK)
#endif
    .value("SHARED_MEMORY_PER_BLOCK", CU_DEVICE_ATTRIBUTE_SHARED_MEMORY_PER_BLOCK)
    .value("TOTAL_CONSTANT_MEMORY", CU_DEVICE_ATTRIBUTE_TOTAL_CONSTANT_MEMORY)
    .value("WARP_SIZE", CU_DEVICE_ATTRIBUTE_WARP_SIZE)
    .value("MAX_PITCH", CU_DEVICE_ATTRIBUTE_MAX_PITCH)
#if CUDAPP_CUDA_VERSION >= 2000
    .value("MAX_REGISTERS_PER_BLOCK", CU_DEVICE_ATTRIBUTE_MAX_REGISTERS_PER_BLOCK)
#endif
    .value("REGISTERS_PER_BLOCK", CU_DEVICE_ATTRIBUTE_REGISTERS_PER_BLOCK)
    .value("CLOCK_RATE", CU_DEVICE_ATTRIBUTE_CLOCK_RATE)
    .value("TEXTURE_ALIGNMENT", CU_DEVICE_ATTRIBUTE_TEXTURE_ALIGNMENT)

    .value("GPU_OVERLAP", CU_DEVICE_ATTRIBUTE_GPU_OVERLAP)
#if CUDAPP_CUDA_VERSION >= 2000
    .value("MULTIPROCESSOR_COUNT", CU_DEVICE_ATTRIBUTE_MULTIPROCESSOR_COUNT)
#endif
#if CUDAPP_CUDA_VERSION >= 2020
    .value("KERNEL_EXEC_TIMEOUT", CU_DEVICE_ATTRIBUTE_KERNEL_EXEC_TIMEOUT)
    .value("INTEGRATED", CU_DEVICE_ATTRIBUTE_INTEGRATED)
    .value("CAN_MAP_HOST_MEMORY", CU_DEVICE_ATTRIBUTE_CAN_MAP_HOST_MEMORY)
    .value("COMPUTE_MODE", CU_DEVICE_ATTRIBUTE_COMPUTE_MODE)
#endif
#if CUDAPP_CUDA_VERSION >= 3000
    .value("MAXIMUM_TEXTURE1D_WIDTH", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE1D_WIDTH)
    .value("MAXIMUM_TEXTURE2D_WIDTH", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_WIDTH)
    .value("MAXIMUM_TEXTURE2D_HEIGHT", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_HEIGHT)
    .value("MAXIMUM_TEXTURE3D_WIDTH", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE3D_WIDTH)
    .value("MAXIMUM_TEXTURE3D_HEIGHT", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE3D_HEIGHT)
    .value("MAXIMUM_TEXTURE3D_DEPTH", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE3D_DEPTH)
    .value("MAXIMUM_TEXTURE2D_ARRAY_WIDTH", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_ARRAY_WIDTH)
    .value("MAXIMUM_TEXTURE2D_ARRAY_HEIGHT", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_ARRAY_HEIGHT)
    .value("MAXIMUM_TEXTURE2D_ARRAY_NUMSLICES", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_ARRAY_NUMSLICES)
#ifdef CUDAPP_POST_30_BETA
    .value("SURFACE_ALIGNMENT", CU_DEVICE_ATTRIBUTE_SURFACE_ALIGNMENT)
    .value("CONCURRENT_KERNELS", CU_DEVICE_ATTRIBUTE_CONCURRENT_KERNELS)
    .value("ECC_ENABLED", CU_DEVICE_ATTRIBUTE_ECC_ENABLED)
#endif
#endif
#if CUDAPP_CUDA_VERSION >= 4000
    .value("MAXIMUM_TEXTURE2D_LAYERED_WIDTH", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_LAYERED_WIDTH)
    .value("MAXIMUM_TEXTURE2D_LAYERED_HEIGHT",  CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_LAYERED_HEIGHT)
    .value("MAXIMUM_TEXTURE2D_LAYERED_LAYERS",  CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_LAYERED_LAYERS)
    .value("MAXIMUM_TEXTURE1D_LAYERED_WIDTH", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE1D_LAYERED_WIDTH)
    .value("MAXIMUM_TEXTURE1D_LAYERED_LAYERS",  CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE1D_LAYERED_LAYERS)
#endif
#if CUDAPP_CUDA_VERSION >= 3020
    .value("PCI_BUS_ID", CU_DEVICE_ATTRIBUTE_PCI_BUS_ID)
    .value("PCI_DEVICE_ID", CU_DEVICE_ATTRIBUTE_PCI_DEVICE_ID)
    .value("TCC_DRIVER", CU_DEVICE_ATTRIBUTE_TCC_DRIVER)
#endif
#if CUDAPP_CUDA_VERSION >= 4000
    .value("MEMORY_CLOCK_RATE", CU_DEVICE_ATTRIBUTE_MEMORY_CLOCK_RATE)
    .value("GLOBAL_MEMORY_BUS_WIDTH", CU_DEVICE_ATTRIBUTE_GLOBAL_MEMORY_BUS_WIDTH)
    .value("L2_CACHE_SIZE", CU_DEVICE_ATTRIBUTE_L2_CACHE_SIZE)
    .value("MAX_THREADS_PER_MULTIPROCESSOR", CU_DEVICE_ATTRIBUTE_MAX_THREADS_PER_MULTIPROCESSOR)
    .value("ASYNC_ENGINE_COUNT", CU_DEVICE_ATTRIBUTE_ASYNC_ENGINE_COUNT)
    .value("UNIFIED_ADDRESSING", CU_DEVICE_ATTRIBUTE_UNIFIED_ADDRESSING)
#endif
#if CUDAPP_CUDA_VERSION >= 4010
    .value("MAXIMUM_TEXTURE2D_GATHER_WIDTH", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_GATHER_WIDTH)
    .value("MAXIMUM_TEXTURE2D_GATHER_HEIGHT", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_GATHER_HEIGHT)
    .value("MAXIMUM_TEXTURE3D_WIDTH_ALTERNATE", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE3D_WIDTH_ALTERNATE)
    .value("MAXIMUM_TEXTURE3D_HEIGHT_ALTERNATE", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE3D_HEIGHT_ALTERNATE)
    .value("MAXIMUM_TEXTURE3D_DEPTH_ALTERNATE", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE3D_DEPTH_ALTERNATE)
    .value("PCI_DOMAIN_ID", CU_DEVICE_ATTRIBUTE_PCI_DOMAIN_ID)
    .value("TEXTURE_PITCH_ALIGNMENT", CU_DEVICE_ATTRIBUTE_TEXTURE_PITCH_ALIGNMENT)
    .value("MAXIMUM_TEXTURECUBEMAP_WIDTH", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURECUBEMAP_WIDTH)
    .value("MAXIMUM_TEXTURECUBEMAP_LAYERED_WIDTH", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURECUBEMAP_LAYERED_WIDTH)
    .value("MAXIMUM_TEXTURECUBEMAP_LAYERED_LAYERS", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURECUBEMAP_LAYERED_LAYERS)
    .value("MAXIMUM_SURFACE1D_WIDTH", CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACE1D_WIDTH)
    .value("MAXIMUM_SURFACE2D_WIDTH", CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACE2D_WIDTH)
    .value("MAXIMUM_SURFACE2D_HEIGHT", CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACE2D_HEIGHT)
    .value("MAXIMUM_SURFACE3D_WIDTH", CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACE3D_WIDTH)
    .value("MAXIMUM_SURFACE3D_HEIGHT", CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACE3D_HEIGHT)
    .value("MAXIMUM_SURFACE3D_DEPTH", CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACE3D_DEPTH)
    .value("MAXIMUM_SURFACE1D_LAYERED_WIDTH", CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACE1D_LAYERED_WIDTH)
    .value("MAXIMUM_SURFACE1D_LAYERED_LAYERS", CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACE1D_LAYERED_LAYERS)
    .value("MAXIMUM_SURFACE2D_LAYERED_WIDTH", CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACE2D_LAYERED_WIDTH)
    .value("MAXIMUM_SURFACE2D_LAYERED_HEIGHT", CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACE2D_LAYERED_HEIGHT)
    .value("MAXIMUM_SURFACE2D_LAYERED_LAYERS", CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACE2D_LAYERED_LAYERS)
    .value("MAXIMUM_SURFACECUBEMAP_WIDTH", CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACECUBEMAP_WIDTH)
    .value("MAXIMUM_SURFACECUBEMAP_LAYERED_WIDTH", CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACECUBEMAP_LAYERED_WIDTH)
    .value("MAXIMUM_SURFACECUBEMAP_LAYERED_LAYERS", CU_DEVICE_ATTRIBUTE_MAXIMUM_SURFACECUBEMAP_LAYERED_LAYERS)
    .value("MAXIMUM_TEXTURE1D_LINEAR_WIDTH", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE1D_LINEAR_WIDTH)
    .value("MAXIMUM_TEXTURE2D_LINEAR_WIDTH", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_LINEAR_WIDTH)
    .value("MAXIMUM_TEXTURE2D_LINEAR_HEIGHT", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_LINEAR_HEIGHT)
    .value("MAXIMUM_TEXTURE2D_LINEAR_PITCH", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_LINEAR_PITCH)
#endif
#if CUDAPP_CUDA_VERSION >= 5000
    .value("MAXIMUM_TEXTURE2D_MIPMAPPED_WIDTH", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_MIPMAPPED_WIDTH)
    .value("MAXIMUM_TEXTURE2D_MIPMAPPED_HEIGHT", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE2D_MIPMAPPED_HEIGHT)
    .value("COMPUTE_CAPABILITY_MAJOR", CU_DEVICE_ATTRIBUTE_COMPUTE_CAPABILITY_MAJOR)
    .value("COMPUTE_CAPABILITY_MINOR", CU_DEVICE_ATTRIBUTE_COMPUTE_CAPABILITY_MINOR)
    .value("MAXIMUM_TEXTURE1D_MIPMAPPED_WIDTH", CU_DEVICE_ATTRIBUTE_MAXIMUM_TEXTURE1D_MIPMAPPED_WIDTH)
#endif
#if CUDAPP_CUDA_VERSION >= 5050
    .value("STREAM_PRIORITIES_SUPPORTED", CU_DEVICE_ATTRIBUTE_STREAM_PRIORITIES_SUPPORTED)
#endif
#if CUDAPP_CUDA_VERSION >= 6000
    .value("GLOBAL_L1_CACHE_SUPPORTED", CU_DEVICE_ATTRIBUTE_GLOBAL_L1_CACHE_SUPPORTED)
    .value("LOCAL_L1_CACHE_SUPPORTED", CU_DEVICE_ATTRIBUTE_LOCAL_L1_CACHE_SUPPORTED)
    .value("MAX_SHARED_MEMORY_PER_MULTIPROCESSOR", CU_DEVICE_ATTRIBUTE_MAX_SHARED_MEMORY_PER_MULTIPROCESSOR)
    .value("MAX_REGISTERS_PER_MULTIPROCESSOR", CU_DEVICE_ATTRIBUTE_MAX_REGISTERS_PER_MULTIPROCESSOR)
    .value("MANAGED_MEMORY", CU_DEVICE_ATTRIBUTE_MANAGED_MEMORY)
    .value("MULTI_GPU_BOARD", CU_DEVICE_ATTRIBUTE_MULTI_GPU_BOARD)
    .value("MULTI_GPU_BOARD_GROUP_ID", CU_DEVICE_ATTRIBUTE_MULTI_GPU_BOARD_GROUP_ID)
#endif
#if CUDAPP_CUDA_VERSION >= 8000
    .value("HOST_NATIVE_ATOMIC_SUPPORTED", CU_DEVICE_ATTRIBUTE_HOST_NATIVE_ATOMIC_SUPPORTED)
    .value("SINGLE_TO_DOUBLE_PRECISION_PERF_RATIO", CU_DEVICE_ATTRIBUTE_SINGLE_TO_DOUBLE_PRECISION_PERF_RATIO)
    .value("PAGEABLE_MEMORY_ACCESS", CU_DEVICE_ATTRIBUTE_PAGEABLE_MEMORY_ACCESS)
    .value("CONCURRENT_MANAGED_ACCESS", CU_DEVICE_ATTRIBUTE_CONCURRENT_MANAGED_ACCESS)
    .value("COMPUTE_PREEMPTION_SUPPORTED", CU_DEVICE_ATTRIBUTE_COMPUTE_PREEMPTION_SUPPORTED)
    .value("CAN_USE_HOST_POINTER_FOR_REGISTERED_MEM", CU_DEVICE_ATTRIBUTE_CAN_USE_HOST_POINTER_FOR_REGISTERED_MEM)
#endif
#if CUDAPP_CUDA_VERSION >= 9000
    .value("MAX_SHARED_MEMORY_PER_BLOCK_OPTIN", CU_DEVICE_ATTRIBUTE_MAX_SHARED_MEMORY_PER_BLOCK_OPTIN)
#endif
#if CUDAPP_CUDA_VERSION >= 9020
    .value("PAGEABLE_MEMORY_ACCESS_USES_HOST_PAGE_TABLES", CU_DEVICE_ATTRIBUTE_PAGEABLE_MEMORY_ACCESS_USES_HOST_PAGE_TABLES)
    .value("DIRECT_MANAGED_MEM_ACCESS_FROM_HOST", CU_DEVICE_ATTRIBUTE_DIRECT_MANAGED_MEM_ACCESS_FROM_HOST)
#endif
#if CUDAPP_CUDA_VERSION >= 10020
    .value("HANDLE_TYPE_POSIX_FILE_DESCRIPTOR_SUPPORTED", CU_DEVICE_ATTRIBUTE_HANDLE_TYPE_POSIX_FILE_DESCRIPTOR_SUPPORTED)
    .value("HANDLE_TYPE_WIN32_HANDLE_SUPPORTED", CU_DEVICE_ATTRIBUTE_HANDLE_TYPE_WIN32_HANDLE_SUPPORTED)
    .value("HANDLE_TYPE_WIN32_KMT_HANDLE_SUPPORTED", CU_DEVICE_ATTRIBUTE_HANDLE_TYPE_WIN32_KMT_HANDLE_SUPPORTED)
#endif
#if CUDAPP_CUDA_VERSION >= 11000
    .value("MAX_PERSISTING_L2_CACHE_SIZE", CU_DEVICE_ATTRIBUTE_MAX_PERSISTING_L2_CACHE_SIZE)
    .value("MAX_BLOCKS_PER_MULTIPROCESSOR", CU_DEVICE_ATTRIBUTE_MAX_BLOCKS_PER_MULTIPROCESSOR)
    .value("GENERIC_COMPRESSION_SUPPORTED", CU_DEVICE_ATTRIBUTE_GENERIC_COMPRESSION_SUPPORTED)
    .value("RESERVED_SHARED_MEMORY_PER_BLOCK", CU_DEVICE_ATTRIBUTE_RESERVED_SHARED_MEMORY_PER_BLOCK)
#endif
#if CUDAPP_CUDA_VERSION >= 11020
    .value("READ_ONLY_HOST_REGISTER_SUPPORTED", CU_DEVICE_ATTRIBUTE_READ_ONLY_HOST_REGISTER_SUPPORTED)
    .value("MEMORY_POOLS_SUPPORTED", CU_DEVICE_ATTRIBUTE_MEMORY_POOLS_SUPPORTED)
#endif
    ;
#if CUDAPP_CUDA_VERSION >= 4000
  py::enum_<CUpointer_attribute>("pointer_attribute")
    .value("CONTEXT", CU_POINTER_ATTRIBUTE_CONTEXT)
    .value("MEMORY_TYPE", CU_POINTER_ATTRIBUTE_MEMORY_TYPE)
    .value("DEVICE_POINTER", CU_POINTER_ATTRIBUTE_DEVICE_POINTER)
    .value("HOST_POINTER", CU_POINTER_ATTRIBUTE_HOST_POINTER)
    ;
#endif

#if CUDAPP_CUDA_VERSION >= 4000
  py::enum_<CUoutput_mode>("profiler_output_mode")
    .value("KEY_VALUE_PAIR", CU_OUT_KEY_VALUE_PAIR)
    .value("CSV", CU_OUT_CSV)
    ;
#endif

#if CUDAPP_CUDA_VERSION >= 3000 && defined(CUDAPP_POST_30_BETA)
  py::enum_<CUfunc_cache_enum>("func_cache")
    .value("PREFER_NONE", CU_FUNC_CACHE_PREFER_NONE)
    .value("PREFER_SHARED", CU_FUNC_CACHE_PREFER_SHARED)
    .value("PREFER_L1", CU_FUNC_CACHE_PREFER_L1)
#if CUDAPP_CUDA_VERSION >= 4010
    .value("PREFER_EQUAL", CU_FUNC_CACHE_PREFER_EQUAL)
#endif
    ;
#endif

#if CUDAPP_CUDA_VERSION >= 4020
  py::enum_<CUsharedconfig_enum>("shared_config")
    .value("DEFAULT_BANK_SIZE", CU_SHARED_MEM_CONFIG_DEFAULT_BANK_SIZE)
    .value("FOUR_BYTE_BANK_SIZE", CU_SHARED_MEM_CONFIG_FOUR_BYTE_BANK_SIZE)
    .value("EIGHT_BYTE_BANK_SIZE", CU_SHARED_MEM_CONFIG_EIGHT_BYTE_BANK_SIZE)
    ;
#endif

#if CUDAPP_CUDA_VERSION >= 2020
  py::enum_<CUfunction_attribute>("function_attribute")
    .value("MAX_THREADS_PER_BLOCK", CU_FUNC_ATTRIBUTE_MAX_THREADS_PER_BLOCK)
    .value("SHARED_SIZE_BYTES", CU_FUNC_ATTRIBUTE_SHARED_SIZE_BYTES)
    .value("CONST_SIZE_BYTES", CU_FUNC_ATTRIBUTE_CONST_SIZE_BYTES)
    .value("LOCAL_SIZE_BYTES", CU_FUNC_ATTRIBUTE_LOCAL_SIZE_BYTES)
    .value("NUM_REGS", CU_FUNC_ATTRIBUTE_NUM_REGS)
#if CUDAPP_CUDA_VERSION >= 3000 && defined(CUDAPP_POST_30_BETA)
    .value("PTX_VERSION", CU_FUNC_ATTRIBUTE_PTX_VERSION)
    .value("BINARY_VERSION", CU_FUNC_ATTRIBUTE_BINARY_VERSION)
#endif
#if CUDAPP_CUDA_VERSION >= 10000 /* guessed */
    .value("CACHE_MODE_CA", CU_FUNC_ATTRIBUTE_CACHE_MODE_CA)
    .value("MAX_DYNAMIC_SHARED_SIZE_BYTES",
        CU_FUNC_ATTRIBUTE_MAX_DYNAMIC_SHARED_SIZE_BYTES)
    .value("PREFERRED_SHARED_MEMORY_CARVEOUT",
        CU_FUNC_ATTRIBUTE_PREFERRED_SHARED_MEMORY_CARVEOUT)
#endif
    .value("MAX", CU_FUNC_ATTRIBUTE_MAX)
    ;
#endif

  py::enum_<CUmemorytype>("memory_type")
    .value("HOST", CU_MEMORYTYPE_HOST)
    .value("DEVICE", CU_MEMORYTYPE_DEVICE)
    .value("ARRAY", CU_MEMORYTYPE_ARRAY)
#if CUDAPP_CUDA_VERSION >= 4000
    .value("UNIFIED", CU_MEMORYTYPE_UNIFIED)
#endif
    ;

#if CUDAPP_CUDA_VERSION >= 2020
  py::enum_<CUcomputemode>("compute_mode")
    .value("DEFAULT", CU_COMPUTEMODE_DEFAULT)
#if CUDAPP_CUDA_VERSION < 8000
    .value("EXCLUSIVE", CU_COMPUTEMODE_EXCLUSIVE)
#endif
    .value("PROHIBITED", CU_COMPUTEMODE_PROHIBITED)
#if CUDAPP_CUDA_VERSION >= 4000
    .value("EXCLUSIVE_PROCESS", CU_COMPUTEMODE_EXCLUSIVE_PROCESS)
#endif
    ;
#endif

#if CUDAPP_CUDA_VERSION >= 2010
  py::enum_<CUjit_option>("jit_option")
    .value("MAX_REGISTERS", CU_JIT_MAX_REGISTERS)
    .value("THREADS_PER_BLOCK", CU_JIT_THREADS_PER_BLOCK)
    .value("WALL_TIME", CU_JIT_WALL_TIME)
    .value("INFO_LOG_BUFFER", CU_JIT_INFO_LOG_BUFFER)
    .value("INFO_LOG_BUFFER_SIZE_BYTES", CU_JIT_INFO_LOG_BUFFER_SIZE_BYTES)
    .value("ERROR_LOG_BUFFER", CU_JIT_ERROR_LOG_BUFFER)
    .value("ERROR_LOG_BUFFER_SIZE_BYTES", CU_JIT_ERROR_LOG_BUFFER_SIZE_BYTES)
    .value("OPTIMIZATION_LEVEL", CU_JIT_OPTIMIZATION_LEVEL)
    .value("TARGET_FROM_CUCONTEXT", CU_JIT_TARGET_FROM_CUCONTEXT)
    .value("TARGET", CU_JIT_TARGET)
    .value("FALLBACK_STRATEGY", CU_JIT_FALLBACK_STRATEGY)
    ;

  py::enum_<CUjit_target>("jit_target")
#if CUDAPP_CUDA_VERSION <= 8000
    .value("COMPUTE_10", CU_TARGET_COMPUTE_10)
    .value("COMPUTE_11", CU_TARGET_COMPUTE_11)
    .value("COMPUTE_12", CU_TARGET_COMPUTE_12)
    .value("COMPUTE_13", CU_TARGET_COMPUTE_13)
#endif
// Aarch64 CUDA seems to have dropped these at CUDA 11.8 already.
// https://github.com/inducer/pycuda/issues/415
#if (CUDAPP_CUDA_VERSION >= 3000) && CUDAPP_CUDA_VERSION < 11080
    .value("COMPUTE_20", CU_TARGET_COMPUTE_20)
#endif
#if (CUDAPP_CUDA_VERSION >= 3020) && CUDAPP_CUDA_VERSION < 11080
    .value("COMPUTE_21", CU_TARGET_COMPUTE_21)
#endif
#if (CUDAPP_CUDA_VERSION >= 11000)
    .value("COMPUTE_30", CU_TARGET_COMPUTE_30)
    .value("COMPUTE_32", CU_TARGET_COMPUTE_32)
    .value("COMPUTE_35", CU_TARGET_COMPUTE_35)
    .value("COMPUTE_37", CU_TARGET_COMPUTE_37)

    .value("COMPUTE_50", CU_TARGET_COMPUTE_50)
    .value("COMPUTE_52", CU_TARGET_COMPUTE_52)
    .value("COMPUTE_53", CU_TARGET_COMPUTE_53)

    .value("COMPUTE_60", CU_TARGET_COMPUTE_60)
    .value("COMPUTE_61", CU_TARGET_COMPUTE_61)
    .value("COMPUTE_62", CU_TARGET_COMPUTE_62)

    .value("COMPUTE_70", CU_TARGET_COMPUTE_70)
    .value("COMPUTE_72", CU_TARGET_COMPUTE_72)
    .value("COMPUTE_75", CU_TARGET_COMPUTE_75)

    .value("COMPUTE_80", CU_TARGET_COMPUTE_80)
#endif
#if (CUDAPP_CUDA_VERSION >= 11060) /* approximate, precise version unknown */
    .value("COMPUTE_86", CU_TARGET_COMPUTE_86)
#endif
#if (CUDAPP_CUDA_VERSION >= 12000)
    .value("COMPUTE_90", CU_TARGET_COMPUTE_90)
    .value("COMPUTE_90A", CU_TARGET_COMPUTE_90A)
#endif
    ;

  py::enum_<CUjit_fallback>("jit_fallback")
    .value("PREFER_PTX", CU_PREFER_PTX)
    .value("PREFER_BINARY", CU_PREFER_BINARY)
    ;
#endif

#if CUDAPP_CUDA_VERSION >= 2020
  {
    py::class_<host_alloc_flags> cls("host_alloc_flags", py::no_init);
    cls.attr("PORTABLE") = CU_MEMHOSTALLOC_PORTABLE;
    cls.attr("DEVICEMAP") = CU_MEMHOSTALLOC_DEVICEMAP;
    cls.attr("WRITECOMBINED") = CU_MEMHOSTALLOC_WRITECOMBINED;
  }
#endif

#if CUDAPP_CUDA_VERSION >= 4000
  {
    py::class_<mem_host_register_flags> cls("mem_host_register_flags", py::no_init);
    cls.attr("PORTABLE") = CU_MEMHOSTREGISTER_PORTABLE;
    cls.attr("DEVICEMAP") = CU_MEMHOSTREGISTER_DEVICEMAP;
  }
#endif

#if CUDAPP_CUDA_VERSION >= 3010
  py::enum_<CUlimit>("limit")
    .value("STACK_SIZE", CU_LIMIT_STACK_SIZE)
    .value("PRINTF_FIFO_SIZE", CU_LIMIT_PRINTF_FIFO_SIZE)
#if CUDAPP_CUDA_VERSION >= 3020
    .value("MALLOC_HEAP_SIZE", CU_LIMIT_MALLOC_HEAP_SIZE)
#endif
#if CUDAPP_CUDA_VERSION >= 4010
    .value("DEV_RUNTIME_SYNC_DEPTH", CU_LIMIT_DEV_RUNTIME_SYNC_DEPTH)
    .value("DEV_RUNTIME_PENDING_LAUNCH_COUNT", CU_LIMIT_DEV_RUNTIME_PENDING_LAUNCH_COUNT)
#endif
    ;
#endif

#if CUDAPP_CUDA_VERSION >= 6000
  py::enum_<CUmemAttach_flags>("mem_attach_flags")
    .value("GLOBAL", CU_MEM_ATTACH_GLOBAL)
    .value("HOST", CU_MEM_ATTACH_HOST)
    .value("SINGLE", CU_MEM_ATTACH_SINGLE)
    ;
#endif

  // graphics enums -----------------------------------------------------------
#if CUDAPP_CUDA_VERSION >= 3000
  py::enum_<CUgraphicsRegisterFlags>("graphics_register_flags")
    .value("NONE", CU_GRAPHICS_REGISTER_FLAGS_NONE)
#if CUDAPP_CUDA_VERSION >= 4000
    .value("READ_ONLY", CU_GRAPHICS_REGISTER_FLAGS_READ_ONLY)
    .value("WRITE_DISCARD", CU_GRAPHICS_REGISTER_FLAGS_WRITE_DISCARD)
    .value("SURFACE_LDST", CU_GRAPHICS_REGISTER_FLAGS_SURFACE_LDST)
#endif
#if CUDAPP_CUDA_VERSION >= 4010
    .value("TEXTURE_GATHER", CU_GRAPHICS_REGISTER_FLAGS_TEXTURE_GATHER)
#endif
    ;

  py::enum_<CUarray_cubemap_face_enum>("array_cubemap_face")
    .value("POSITIVE_X", CU_CUBEMAP_FACE_POSITIVE_X)
    .value("NEGATIVE_X", CU_CUBEMAP_FACE_NEGATIVE_X)
    .value("POSITIVE_Y", CU_CUBEMAP_FACE_POSITIVE_Y)
    .value("NEGATIVE_Y", CU_CUBEMAP_FACE_NEGATIVE_Y)
    .value("POSITIVE_Z", CU_CUBEMAP_FACE_POSITIVE_Z)
    .value("NEGATIVE_Z", CU_CUBEMAP_FACE_NEGATIVE_Z)
    ;
#endif

  // }}}

  py::def("init", init,
      py::arg("flags")=0);

  // {{{ device
  {
    typedef device cl;
    py::class_<cl>("Device", py::no_init)
      .def("__init__", py::make_constructor(make_device))
#if CUDAPP_CUDA_VERSION >= 4010
      .def("__init__", py::make_constructor(make_device_from_pci_bus_id))
#endif
      .DEF_SIMPLE_METHOD(count)
      .staticmethod("count")
      .DEF_SIMPLE_METHOD(name)
#if CUDAPP_CUDA_VERSION >= 4010
      .DEF_SIMPLE_METHOD(pci_bus_id)
#endif
      .DEF_SIMPLE_METHOD(compute_capability)
      .DEF_SIMPLE_METHOD(total_memory)
      .def("get_attribute", device_get_attribute)
      .def(py::self == py::self)
      .def(py::self != py::self)
      .def("__hash__", &cl::hash)
      .def("make_context", &cl::make_context,
          (py::args("self"), py::args("flags")=0))
#if CUDAPP_CUDA_VERSION >= 4000
      .DEF_SIMPLE_METHOD(can_access_peer)
#endif
#if CUDAPP_CUDA_VERSION >= 7000
      .def("retain_primary_context", &cl::retain_primary_context,
          (py::args("self")))
#endif
      ;
  }
  // }}}

  // {{{ context
  {
    typedef context cl;
    py::class_<cl, shared_ptr<cl>, boost::noncopyable >("Context", py::no_init)
      .def(py::self == py::self)
      .def(py::self != py::self)
      .def("__hash__", &cl::hash)

      .def("attach", &cl::attach, (py::arg("flags")=0))
      .staticmethod("attach")
      .DEF_SIMPLE_METHOD(detach)

#if CUDAPP_CUDA_VERSION >= 2000
      .def("push", context_push)
      .DEF_SIMPLE_METHOD(pop)
      .staticmethod("pop")
      .DEF_SIMPLE_METHOD(get_device)
      .staticmethod("get_device")
#endif

      .DEF_SIMPLE_METHOD(synchronize)
      .staticmethod("synchronize")

      .def("get_current", (boost::shared_ptr<cl> (*)()) &cl::current_context)
      .staticmethod("get_current")

#if CUDAPP_CUDA_VERSION >= 3010
      .DEF_SIMPLE_METHOD(set_limit)
      .staticmethod("set_limit")
      .DEF_SIMPLE_METHOD(get_limit)
      .staticmethod("get_limit")
#endif
#if CUDAPP_CUDA_VERSION >= 3020
      .DEF_SIMPLE_METHOD(get_cache_config)
      .staticmethod("get_cache_config")
      .DEF_SIMPLE_METHOD(set_cache_config)
      .staticmethod("set_cache_config")
      .DEF_SIMPLE_METHOD(get_api_version)
#endif
#if CUDAPP_CUDA_VERSION >= 4000
      .def("enable_peer_access", &cl::enable_peer_access,
          (py::arg("peer"), py::arg("flags")=0))
      .staticmethod("enable_peer_access")
      .DEF_SIMPLE_METHOD(disable_peer_access)
      .staticmethod("disable_peer_access")
#endif
#if CUDAPP_CUDA_VERSION >= 4020
      .DEF_SIMPLE_METHOD(get_shared_config)
      .staticmethod("get_shared_config")
      .DEF_SIMPLE_METHOD(set_shared_config)
      .staticmethod("set_shared_config")
#endif
      .add_property("handle", &cl::handle_int)
      ;
  }
  // }}}

  // {{{ stream
  {
    typedef stream cl;
    py::class_<cl, boost::noncopyable, shared_ptr<cl> >
      ("Stream", py::init<unsigned int>(py::arg("flags")=0))
      .DEF_SIMPLE_METHOD(synchronize)
      .DEF_SIMPLE_METHOD(is_done)
#if CUDAPP_CUDA_VERSION >= 3020
      .DEF_SIMPLE_METHOD(wait_for_event)
#endif
      .add_property("handle", &cl::handle_int)
      ;
  }
  // }}}

  // {{{ module
  {
    typedef module cl;
    py::class_<cl, boost::noncopyable, shared_ptr<cl> >("Module", py::no_init)
      .def("get_function", &cl::get_function, (py::args("self", "name")),
          py::with_custodian_and_ward_postcall<0, 1>())
      .def("get_global", &cl::get_global, (py::args("self", "name")))
      .def("get_texref", module_get_texref,
          (py::args("self", "name")),
          py::return_value_policy<py::manage_new_object>())
#if CUDAPP_CUDA_VERSION >= 3010
      .def("get_surfref", module_get_surfref,
          (py::args("self", "name")),
          py::return_value_policy<py::manage_new_object>())
#endif
      ;
  }

  py::def("module_from_file", module_from_file, (py::arg("filename")),
      py::return_value_policy<py::manage_new_object>());
  py::def("module_from_buffer", module_from_buffer,
      (py::arg("buffer"),
       py::arg("options")=py::list(),
       py::arg("message_handler")=py::object()),
      py::return_value_policy<py::manage_new_object>());

  // }}}

  // {{{ linker

#if CUDAPP_CUDA_VERSION >= 5050
  py::enum_<CUjitInputType>("jit_input_type")
    .value("CUBIN", CU_JIT_INPUT_CUBIN)
    .value("PTX", CU_JIT_INPUT_PTX)
    .value("FATBINARY", CU_JIT_INPUT_FATBINARY)
    .value("OBJECT", CU_JIT_INPUT_OBJECT)
    .value("LIBRARY", CU_JIT_INPUT_LIBRARY);

  py::class_<Linker, boost::noncopyable, shared_ptr<Linker> >("Linker")
    .def(py::init<py::object>())
    .def(py::init<py::object, py::object>())
    .def(py::init<py::object, py::object, py::object>())
    .def("add_data", &Linker::add_data, (py::arg("data"), py::arg("input_type"), py::arg("name")=py::str("unknown")))
    .def("add_file", &Linker::add_file, (py::arg("filename"), py::arg("input_type")))
    .def("link_module", &Linker::link_module, py::return_value_policy<py::manage_new_object>());
#endif

  // }}}

  // {{{ function
  {
    typedef function cl;
    py::class_<cl>("Function", py::no_init)
      .def("_set_block_shape", &cl::set_block_shape)
      .def("_set_shared_size", &cl::set_shared_size)
      .def("_param_set_size", &cl::param_set_size)
      .def("_param_seti", (void (cl::*)(int, unsigned int)) &cl::param_set)
      .def("_param_setf", (void (cl::*)(int, float )) &cl::param_set)
      .def("_param_setv", function_param_setv)
      .DEF_SIMPLE_METHOD(param_set_texref)


      .def("_launch", &cl::launch)
      .def("_launch_grid", &cl::launch_grid,
          py::args("grid_width", "grid_height"))
      .def("_launch_grid_async", &cl::launch_grid_async,
          py::args("grid_width", "grid_height", "s"))

#if CUDAPP_CUDA_VERSION >= 2020
      .DEF_SIMPLE_METHOD(get_attribute)
#endif
#if CUDAPP_CUDA_VERSION >= 10000
      .DEF_SIMPLE_METHOD(set_attribute)
#endif
#if CUDAPP_CUDA_VERSION >= 3000 && defined(CUDAPP_POST_30_BETA)
      .DEF_SIMPLE_METHOD(set_cache_config)
#endif
#if CUDAPP_CUDA_VERSION >= 4000
      .def("_launch_kernel", &cl::launch_kernel)
#endif
      ;
  }

  // }}}

  // {{{ pointer holder

  {
    typedef pointer_holder_base cl;
    py::class_<pointer_holder_base_wrap, boost::noncopyable>(
        "PointerHolderBase")
      .def("get_pointer", py::pure_virtual(&cl::get_pointer))
      .def("as_buffer", &cl::as_buffer,
          (py::arg("size"), py::arg("offset")=0))
      .def("__int__", &cl::operator CUdeviceptr)
      .def("__long__", mem_obj_to_long<cl>)
      .def("__index__", mem_obj_to_long<cl>)
      ;

    py::implicitly_convertible<pointer_holder_base, CUdeviceptr>();
  }

  {
    typedef device_allocation cl;
    py::class_<cl, boost::noncopyable>("DeviceAllocation", py::no_init)
      .def("__int__", &cl::operator CUdeviceptr)
      .def("__long__", mem_obj_to_long<cl>)
      .def("__index__", mem_obj_to_long<cl>)
      .def("as_buffer", &cl::as_buffer,
          (py::arg("size"), py::arg("offset")=0))
      .DEF_SIMPLE_METHOD(free)
      ;

    py::implicitly_convertible<device_allocation, CUdeviceptr>();
  }

#if CUDAPP_CUDA_VERSION >= 4010 && PY_VERSION_HEX >= 0x02060000
  {
    typedef ipc_mem_handle cl;
    py::class_<cl, boost::noncopyable>("IPCMemoryHandle",
        py::init<py::object, py::optional<CUipcMem_flags> >())
      .def("__int__", &cl::operator CUdeviceptr)
      .def("__long__", mem_obj_to_long<cl>)
      .def("__index__", mem_obj_to_long<cl>)
      .DEF_SIMPLE_METHOD(close)
      ;

    py::implicitly_convertible<ipc_mem_handle, CUdeviceptr>();
  }

  DEF_SIMPLE_FUNCTION(mem_get_ipc_handle);
#endif

  // }}}

  // {{{ host memory

  {
    typedef host_pointer cl;
    py::class_<cl, boost::noncopyable>("HostPointer", py::no_init)
#if CUDAPP_CUDA_VERSION >= 2020
      .DEF_SIMPLE_METHOD(get_device_pointer)
#endif
      ;
  }

  {
    typedef pagelocked_host_allocation cl;
    py::class_<cl, boost::noncopyable, py::bases<host_pointer> > wrp(
        "PagelockedHostAllocation", py::no_init);

    wrp
      .DEF_SIMPLE_METHOD(free)
#if CUDAPP_CUDA_VERSION >= 3020
      .DEF_SIMPLE_METHOD(get_flags)
#endif
      ;
    py::scope().attr("HostAllocation") = wrp;
  }


  {
    typedef aligned_host_allocation cl;
    py::class_<cl, boost::noncopyable, py::bases<host_pointer> > wrp(
        "AlignedHostAllocation", py::no_init);

    wrp
      .DEF_SIMPLE_METHOD(free)
      ;
  }

#if CUDAPP_CUDA_VERSION >= 6000
  {
    typedef managed_allocation cl;
    py::class_<cl, boost::noncopyable, py::bases<device_allocation> > wrp(
        "ManagedAllocation", py::no_init);

    wrp
      .DEF_SIMPLE_METHOD(get_device_pointer)
      .def("attach", &cl::attach,
        (py::arg("mem_flags"), py::arg("stream")=py::object()))
      ;
  }
#endif

#if CUDAPP_CUDA_VERSION >= 4000
  {
    typedef registered_host_memory cl;
    py::class_<cl, boost::noncopyable, py::bases<host_pointer> >(
        "RegisteredHostMemory", py::no_init)
      .def("unregister", &cl::free)
      ;
  }
#endif

  py::def("pagelocked_empty", numpy_empty<pagelocked_host_allocation>,
      (py::arg("shape"), py::arg("dtype"), py::arg("order")="C",
       py::arg("mem_flags")=0));

  py::def("aligned_empty", numpy_empty<aligned_host_allocation>,
      (py::arg("shape"), py::arg("dtype"),
       py::arg("order")="C", py::arg("alignment")=4096));

#if CUDAPP_CUDA_VERSION >= 6000
  py::def("managed_empty", numpy_empty<managed_allocation>,
      (py::arg("shape"), py::arg("dtype"), py::arg("order")="C",
       py::arg("mem_flags")=0));
#endif

#if CUDAPP_CUDA_VERSION >= 4000
  py::def("register_host_memory", register_host_memory,
      (py::arg("ary"), py::arg("flags")=0));
#endif

  // }}}

  DEF_SIMPLE_FUNCTION(mem_get_info);
  py::def("mem_alloc", mem_alloc_wrap,
      py::return_value_policy<py::manage_new_object>());
  py::def("mem_alloc_pitch", mem_alloc_pitch_wrap,
      py::args("width", "height", "access_size"));
  DEF_SIMPLE_FUNCTION(mem_get_address_range);

  // {{{ memset/memcpy
  py::def("memset_d8",  py_memset_d8, py::args("dest", "data", "size"));
  py::def("memset_d16", py_memset_d16, py::args("dest", "data", "size"));
  py::def("memset_d32", py_memset_d32, py::args("dest", "data", "size"));

  py::def("memset_d2d8", py_memset_d2d8,
      py::args("dest", "pitch", "data", "width", "height"));
  py::def("memset_d2d16", py_memset_d2d16,
      py::args("dest", "pitch", "data", "width", "height"));
  py::def("memset_d2d32", py_memset_d2d32,
      py::args("dest", "pitch", "data", "width", "height"));

  py::def("memset_d8_async",  py_memset_d8_async,
      (py::args("dest", "data", "size"), py::arg("stream")=py::object()));
  py::def("memset_d16_async", py_memset_d16_async,
      (py::args("dest", "data", "size"), py::arg("stream")=py::object()));
  py::def("memset_d32_async", py_memset_d32_async,
      (py::args("dest", "data", "size"), py::arg("stream")=py::object()));

  py::def("memset_d2d8_async", py_memset_d2d8_async,
      (py::args("dest", "pitch", "data", "width", "height"),
       py::arg("stream")=py::object()));
  py::def("memset_d2d16_async", py_memset_d2d16_async,
      (py::args("dest", "pitch", "data", "width", "height"),
       py::arg("stream")=py::object()));
  py::def("memset_d2d32_async", py_memset_d2d32_async,
      (py::args("dest", "pitch", "data", "width", "height"),
       py::arg("stream")=py::object()));

  py::def("memcpy_htod", py_memcpy_htod,
      (py::args("dest"), py::arg("src")));
  py::def("memcpy_htod_async", py_memcpy_htod_async,
      (py::args("dest"), py::arg("src"), py::arg("stream")=py::object()));
  py::def("memcpy_dtoh", py_memcpy_dtoh,
      (py::args("dest"), py::arg("src")));
  py::def("memcpy_dtoh_async", py_memcpy_dtoh_async,
      (py::args("dest"), py::arg("src"), py::arg("stream")=py::object()));

  py::def("memcpy_dtod", py_memcpy_dtod, py::args("dest", "src", "size"));
#if CUDAPP_CUDA_VERSION >= 3000
  py::def("memcpy_dtod_async", py_memcpy_dtod_async,
      (py::args("dest", "src", "size"), py::arg("stream")=py::object()));
#endif
#if CUDAPP_CUDA_VERSION >= 4000
  py::def("memcpy_peer", py_memcpy_peer,
      (py::args("dest", "src", "size"),
       py::arg("dest_context")=py::object(),
       py::arg("src_context")=py::object()));

  py::def("memcpy_peer_async", py_memcpy_peer_async,
      (py::args("dest", "src", "size"),
       py::arg("dest_context")=py::object(),
       py::arg("src_context")=py::object(),
       py::arg("stream")=py::object()));
#endif

  DEF_SIMPLE_FUNCTION_WITH_ARGS(memcpy_dtoa,
      ("ary", "index", "src", "len"));
  DEF_SIMPLE_FUNCTION_WITH_ARGS(memcpy_atod,
      ("dest", "ary", "index", "len"));
  DEF_SIMPLE_FUNCTION_WITH_ARGS(py_memcpy_htoa,
      ("ary", "index", "src"));
  DEF_SIMPLE_FUNCTION_WITH_ARGS(py_memcpy_atoh,
      ("dest", "ary", "index"));

  DEF_SIMPLE_FUNCTION_WITH_ARGS(memcpy_atoa,
      ("dest", "dest_index", "src", "src_index", "len"));

#if CUDAPP_CUDA_VERSION >= 4000
#define WRAP_MEMCPY_2D_UNIFIED_SETTERS \
      .DEF_SIMPLE_METHOD(set_src_unified) \
      .DEF_SIMPLE_METHOD(set_dst_unified)
#else
#define WRAP_MEMCPY_2D_UNIFIED_SETTERS /* empty */
#endif

#define WRAP_MEMCPY_2D_PROPERTIES \
      .def_readwrite("src_x_in_bytes", &cl::srcXInBytes) \
      .def_readwrite("src_y", &cl::srcY) \
      .def_readwrite("src_memory_type", &cl::srcMemoryType) \
      .def_readwrite("src_device", &cl::srcDevice) \
      .def_readwrite("src_pitch", &cl::srcPitch) \
      \
      .DEF_SIMPLE_METHOD(set_src_host) \
      .DEF_SIMPLE_METHOD(set_src_array) \
      .DEF_SIMPLE_METHOD(set_src_device) \
      \
      .def_readwrite("dst_x_in_bytes", &cl::dstXInBytes) \
      .def_readwrite("dst_y", &cl::dstY) \
      .def_readwrite("dst_memory_type", &cl::dstMemoryType) \
      .def_readwrite("dst_device", &cl::dstDevice) \
      .def_readwrite("dst_pitch", &cl::dstPitch) \
      \
      .DEF_SIMPLE_METHOD(set_dst_host) \
      .DEF_SIMPLE_METHOD(set_dst_array) \
      .DEF_SIMPLE_METHOD(set_dst_device) \
      \
      .def_readwrite("width_in_bytes", &cl::WidthInBytes) \
      .def_readwrite("height", &cl::Height) \
      \
      WRAP_MEMCPY_2D_UNIFIED_SETTERS

  {
    typedef memcpy_2d cl;
    py::class_<cl>("Memcpy2D")
      WRAP_MEMCPY_2D_PROPERTIES

      .def("__call__", &cl::execute, py::args("self", "aligned"))
      .def("__call__", &cl::execute_async)
      ;
  }

#if CUDAPP_CUDA_VERSION >= 2000
#define WRAP_MEMCPY_3D_PROPERTIES \
      WRAP_MEMCPY_2D_PROPERTIES \
      .def_readwrite("src_z", &cl::srcZ) \
      .def_readwrite("src_lod", &cl::srcLOD) \
      .def_readwrite("src_height", &cl::srcHeight) \
      \
      .def_readwrite("dst_z", &cl::dstZ) \
      .def_readwrite("dst_lod", &cl::dstLOD) \
      .def_readwrite("dst_height", &cl::dstHeight) \
      \
      .def_readwrite("depth", &cl::Depth) \

  {
    typedef memcpy_3d cl;
    py::class_<cl>("Memcpy3D")
      WRAP_MEMCPY_3D_PROPERTIES

      .def("__call__", &cl::execute)
      .def("__call__", &cl::execute_async)
      ;
  }
#endif
#if CUDAPP_CUDA_VERSION >= 4000
  {
    typedef memcpy_3d_peer cl;
    py::class_<cl>("Memcpy3DPeer")
      WRAP_MEMCPY_3D_PROPERTIES

      .DEF_SIMPLE_METHOD(set_src_context)
      .DEF_SIMPLE_METHOD(set_dst_context)

      .def("__call__", &cl::execute)
      .def("__call__", &cl::execute_async)
      ;
  }
#endif
  // }}}

  // {{{ event
  {
    typedef event cl;
    py::class_<cl, boost::noncopyable>
      ("Event", py::init<py::optional<unsigned int> >(py::arg("flags")))
      .def("record", &cl::record,
          py::arg("stream")=py::object(), py::return_self<>())
      .def("synchronize", &cl::synchronize, py::return_self<>())
      .DEF_SIMPLE_METHOD(query)
      .DEF_SIMPLE_METHOD(time_since)
      .DEF_SIMPLE_METHOD(time_till)
#if CUDAPP_CUDA_VERSION >= 4010 && PY_VERSION_HEX >= 0x02060000
      .DEF_SIMPLE_METHOD(ipc_handle)
      .def("from_ipc_handle", event_from_ipc_handle,
          py::return_value_policy<py::manage_new_object>())
      .staticmethod("from_ipc_handle")
#endif
      ;
  }
  // }}}

  // {{{ arrays
  {
    typedef CUDA_ARRAY_DESCRIPTOR cl;
    py::class_<cl>("ArrayDescriptor")
      .def_readwrite("width", &cl::Width)
      .def_readwrite("height", &cl::Height)
      .def_readwrite("format", &cl::Format)
      .def_readwrite("num_channels", &cl::NumChannels)
      ;
  }

#if CUDAPP_CUDA_VERSION >= 2000
  {
    typedef CUDA_ARRAY3D_DESCRIPTOR cl;
    py::class_<cl>("ArrayDescriptor3D")
      .def_readwrite("width", &cl::Width)
      .def_readwrite("height", &cl::Height)
      .def_readwrite("depth", &cl::Depth)
      .def_readwrite("format", &cl::Format)
      .def_readwrite("num_channels", &cl::NumChannels)
      .def_readwrite("flags", &cl::Flags)
      ;
  }
#endif

  {
    typedef array cl;
    py::class_<cl, shared_ptr<cl>, boost::noncopyable>
      ("Array", py::init<const CUDA_ARRAY_DESCRIPTOR &>())
      .DEF_SIMPLE_METHOD(free)
      .DEF_SIMPLE_METHOD(get_descriptor)
#if CUDAPP_CUDA_VERSION >= 2000
      .def(py::init<const CUDA_ARRAY3D_DESCRIPTOR &>())
      .DEF_SIMPLE_METHOD(get_descriptor_3d)
#endif
      .add_property("handle", &cl::handle_int)
      ;
  }
  // }}}

  // {{{ texture reference
  {
    typedef texture_reference cl;
    py::class_<cl, boost::noncopyable>("TextureReference")
      .DEF_SIMPLE_METHOD(set_array)
      .def("set_address", &cl::set_address,
          (py::arg("devptr"), py::arg("bytes"), py::arg("allow_offset")=false))
#if CUDAPP_CUDA_VERSION >= 2020
      .DEF_SIMPLE_METHOD_WITH_ARGS(set_address_2d, ("devptr", "descr", "pitch"))
#endif
      .DEF_SIMPLE_METHOD_WITH_ARGS(set_format, ("format", "num_components"))
      .DEF_SIMPLE_METHOD_WITH_ARGS(set_address_mode, ("dim", "am"))
      .DEF_SIMPLE_METHOD(set_filter_mode)
      .DEF_SIMPLE_METHOD(set_flags)
      .DEF_SIMPLE_METHOD(get_address)
      .def("get_array", &cl::get_array,
          py::return_value_policy<py::manage_new_object>())
      .DEF_SIMPLE_METHOD(get_address_mode)
      .DEF_SIMPLE_METHOD(get_filter_mode)

#if CUDAPP_CUDA_VERSION >= 2000
      .DEF_SIMPLE_METHOD(get_format)
#endif

      .DEF_SIMPLE_METHOD(get_flags)
      ;
  }
  // }}}

  // {{{ surface reference
#if CUDAPP_CUDA_VERSION >= 3010
  {
    typedef surface_reference cl;
    py::class_<cl, boost::noncopyable>("SurfaceReference", py::no_init)
      .def("set_array", &cl::set_array,
          (py::arg("array"), py::arg("flags")=0))
      .def("get_array", &cl::get_array,
          py::return_value_policy<py::manage_new_object>())
      ;
  }
#endif
  // }}}

  // {{{ profiler control
#if CUDAPP_CUDA_VERSION >= 4000
  DEF_SIMPLE_FUNCTION(initialize_profiler);
  DEF_SIMPLE_FUNCTION(start_profiler);
  DEF_SIMPLE_FUNCTION(stop_profiler);
#endif
  // }}}

  py::scope().attr("TRSA_OVERRIDE_FORMAT") = CU_TRSA_OVERRIDE_FORMAT;
  py::scope().attr("TRSF_READ_AS_INTEGER") = CU_TRSF_READ_AS_INTEGER;
  py::scope().attr("TRSF_NORMALIZED_COORDINATES") = CU_TRSF_NORMALIZED_COORDINATES;
  py::scope().attr("TR_DEFAULT") = CU_PARAM_TR_DEFAULT;

  DEF_SIMPLE_FUNCTION(have_gl_ext);

  pycuda_expose_tools();
#ifdef HAVE_GL
  pycuda_expose_gl();
#endif
#ifdef HAVE_CURAND
  pycuda_expose_curand();
#endif
}

// vim: foldmethod=marker
