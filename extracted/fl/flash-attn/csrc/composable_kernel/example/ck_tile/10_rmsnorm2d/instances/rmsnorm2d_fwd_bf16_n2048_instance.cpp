
// SPDX-License-Identifier: MIT
// Copyright (c) 2018-2024, Advanced Micro Devices, Inc. All rights reserved.

#include "rmsnorm2d_fwd_instance_common.hpp"

// clang-format off
//                                                       rm  rn  tm  tn  vn  pd    rms     2p
template float rmsnorm2d_fwd_<trait_<ck_tile::bf16_t,  1, 1, 1,  256, 8,  true,  false, false>>(const S&, A);
template float rmsnorm2d_fwd_<trait_<ck_tile::bf16_t,  1, 2, 1,  256, 4,  true,  false, false>>(const S&, A);
template float rmsnorm2d_fwd_<trait_<ck_tile::bf16_t,  1, 4, 1,  256, 2,  true,  false, false>>(const S&, A);
template float rmsnorm2d_fwd_<trait_<ck_tile::bf16_t,  1, 8, 1,  256, 1,  true,  false, false>>(const S&, A);

// clang-format on
