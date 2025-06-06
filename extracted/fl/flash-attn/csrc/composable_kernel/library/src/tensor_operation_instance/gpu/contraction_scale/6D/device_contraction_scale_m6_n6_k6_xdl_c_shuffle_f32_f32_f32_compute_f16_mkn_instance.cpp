// SPDX-License-Identifier: MIT
// Copyright (c) 2024, Advanced Micro Devices, Inc. All rights reserved.

// This (ifndef) is a hack to use customized behavior for buffer load rather than using default
// setting Don't use this hack unless absolutely necessary!
// FIXME: make the behavior of buffer load a configurable (template) parameter of each device op
#define CK_EXPERIMENTAL_USE_BUFFER_LOAD_OOB_CHECK_OFFSET_TRICK 1

#include <cstdlib>

#include "ck/ck.hpp"
#include "ck/tensor_operation/gpu/device/device_contraction_multiple_d.hpp"
#include "ck/tensor_operation/gpu/element/element_wise_operation.hpp"
#include "ck/library/tensor_operation_instance/gpu/contraction/device_contraction_instance.hpp"
#include "ck/library/tensor_operation_instance/add_device_operation_instance.hpp"

namespace ck {
namespace tensor_operation {
namespace device {
namespace instance {

// A[m0, m1, k0, k1] * B[n0, n1, k0, k1] + D[m0, m1, n0, n1] = E[m0, m1, n0, n1]
// m/k/n/n are the fast changing dimension for A/B/D/E
using device_contraction_scale_m6_n6_k6_xdl_c_shuffle_f32_f32_f32_compute_f16_mkn_instance =
    device_contraction_mk_instance<F32,
                                   F32,
                                   F32,
                                   F32,
                                   Empty_Tuple,
                                   F32,
                                   F16,
                                   PassThrough,
                                   PassThrough,
                                   Scale,
                                   6>;

void add_device_contraction_scale_m6_n6_k6_xdl_c_shuffle_f32_f32_f32_compute_f16_mkn_instance(
    std::vector<std::unique_ptr<DeviceContractionMultipleD<6,
                                                           6,
                                                           6,
                                                           F32,
                                                           F32,
                                                           Empty_Tuple,
                                                           F32,
                                                           PassThrough,
                                                           PassThrough,
                                                           Scale,
                                                           F16>>>& instances)
{
    add_device_operation_instances(
        instances,
        device_contraction_scale_m6_n6_k6_xdl_c_shuffle_f32_f32_f32_compute_f16_mkn_instance{});
}

} // namespace instance
} // namespace device
} // namespace tensor_operation
} // namespace ck
