// SPDX-License-Identifier: MIT
// Copyright (c) 2024, Advanced Micro Devices, Inc. All rights reserved.

#include "ck/library/tensor_operation_instance/gpu/grouped_conv_bwd_weight/device_grouped_conv_bwd_weight_xdl_bilinear_instance.hpp"
#include "ck/library/tensor_operation_instance/add_device_operation_instance.hpp"

namespace ck {
namespace tensor_operation {
namespace device {
namespace instance {

void add_device_grouped_conv3d_bwd_weight_xdl_bilinear_ndhwgc_gkzyxc_ndhwgk_f16_comp_bf8_f8_instances(
    std::vector<std::unique_ptr<DeviceGroupedConvBwdWeightMultipleD<3,
                                                                    NDHWGC,
                                                                    GKZYXC,
                                                                    NDHWGK,
                                                                    Tuple<GKZYXC>,
                                                                    F16,
                                                                    F16,
                                                                    F16,
                                                                    Tuple<F16>,
                                                                    PassThrough,
                                                                    Bilinear,
                                                                    PassThrough,
                                                                    BF8,
                                                                    F8>>>& instances)
{
    // 1. Default
    add_device_operation_instances(
        instances,
        device_grouped_conv_bwd_weight_xdl_c_shuffle_f16_comp_bf8_f8_bilinear_instances<
            3,
            NDHWGC,
            GKZYXC,
            NDHWGK,
            ConvBwdWeightDefault>{});
    // 2. Filter1x1Stride1Pad0
    add_device_operation_instances(
        instances,
        device_grouped_conv_bwd_weight_xdl_c_shuffle_f16_comp_bf8_f8_bilinear_instances<
            3,
            NDHWGC,
            GKZYXC,
            NDHWGK,
            ConvBwdWeightFilter1x1Stride1Pad0>{});
}

} // namespace instance
} // namespace device
} // namespace tensor_operation
} // namespace ck
