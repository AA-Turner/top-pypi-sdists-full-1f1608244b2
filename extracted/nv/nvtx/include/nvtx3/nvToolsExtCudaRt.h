/*
 * SPDX-FileCopyrightText: Copyright (c) 2009-2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
 * SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * Licensed under the Apache License v2.0 with LLVM Exceptions.
 * See https://nvidia.github.io/NVTX/LICENSE.txt for license information.
 */

#if defined(NVTX_AS_SYSTEM_HEADER)
#if defined(__clang__)
#pragma clang system_header
#elif defined(__GNUC__) || defined(__NVCOMPILER)
#pragma GCC system_header
#elif defined(_MSC_VER)
#pragma system_header
#endif
#endif

#include "nvToolsExt.h"

#include "cuda.h"
#include "driver_types.h"

#ifndef NVTOOLSEXT_CUDART_V3
#define NVTOOLSEXT_CUDART_V3

#ifdef __cplusplus
extern "C" {
#endif /* __cplusplus */

/* ========================================================================= */
/** \name Functions for CUDA Resource Naming
*/
/** \addtogroup RESOURCE_NAMING
 * \section RESOURCE_NAMING_CUDART CUDA Runtime Resource Naming
 *
 * This section covers the API functions that allow to annotate CUDA resources
 * with user-provided names.
 *
 * @{
 */

/*  ------------------------------------------------------------------------- */
/* \cond SHOW_HIDDEN
* \brief Used to build a non-colliding value for resource types separated class
* \version NVTX_VERSION_2
*/
#define NVTX_RESOURCE_CLASS_CUDART 5
/** \endcond */

/*  ------------------------------------------------------------------------- */
/** \brief Resource types for CUDART
*/
typedef enum nvtxResourceCUDARTType_t
{
    NVTX_RESOURCE_TYPE_CUDART_DEVICE = NVTX_RESOURCE_MAKE_TYPE(CUDART, 0), /* int device */
    NVTX_RESOURCE_TYPE_CUDART_STREAM = NVTX_RESOURCE_MAKE_TYPE(CUDART, 1), /* cudaStream_t */
    NVTX_RESOURCE_TYPE_CUDART_EVENT = NVTX_RESOURCE_MAKE_TYPE(CUDART, 2) /* cudaEvent_t */
} nvtxResourceCUDARTType_t;


/* ------------------------------------------------------------------------- */
/** \brief Annotates a CUDA device.
 *
 * Allows the user to associate a CUDA device with a user-provided name.
 *
 * \param device - The id of the CUDA device to name.
 * \param name   - The name of the CUDA device.
 *
 * \version NVTX_VERSION_1
 * @{ */
NVTX_DECLSPEC void NVTX_API nvtxNameCudaDeviceA(int device, const char* name);
NVTX_DECLSPEC void NVTX_API nvtxNameCudaDeviceW(int device, const wchar_t* name);
/** @} */

/* ------------------------------------------------------------------------- */
/** \brief Annotates a CUDA stream.
 *
 * Allows the user to associate a CUDA stream with a user-provided name.
 *
 * \param stream - The handle of the CUDA stream to name.
 * \param name   - The name of the CUDA stream.
 *
 * \version NVTX_VERSION_1
 * @{ */
NVTX_DECLSPEC void NVTX_API nvtxNameCudaStreamA(cudaStream_t stream, const char* name);
NVTX_DECLSPEC void NVTX_API nvtxNameCudaStreamW(cudaStream_t stream, const wchar_t* name);
/** @} */

/* ------------------------------------------------------------------------- */
/** \brief Annotates a CUDA event.
 *
 * Allows the user to associate a CUDA event with a user-provided name.
 *
 * \param event - The handle of the CUDA event to name.
 * \param name  - The name of the CUDA event.
 *
 * \version NVTX_VERSION_1
 * @{ */
NVTX_DECLSPEC void NVTX_API nvtxNameCudaEventA(cudaEvent_t event, const char* name);
NVTX_DECLSPEC void NVTX_API nvtxNameCudaEventW(cudaEvent_t event, const wchar_t* name);
/** @} */

/** @} */ /* END RESOURCE_NAMING */

/* ========================================================================= */
#ifdef UNICODE
  #define nvtxNameCudaDevice nvtxNameCudaDeviceW
  #define nvtxNameCudaStream nvtxNameCudaStreamW
  #define nvtxNameCudaEvent  nvtxNameCudaEventW
#else
  #define nvtxNameCudaDevice nvtxNameCudaDeviceA
  #define nvtxNameCudaStream nvtxNameCudaStreamA
  #define nvtxNameCudaEvent  nvtxNameCudaEventA
#endif

#ifdef __cplusplus
}
#endif /* __cplusplus */

#ifndef NVTX_NO_IMPL
#define NVTX_IMPL_GUARD_CUDART /* Ensure other headers cannot be included directly */
#include "nvtxDetail/nvtxImplCudaRt_v3.h"
#undef NVTX_IMPL_GUARD_CUDART
#endif /*NVTX_NO_IMPL*/

#endif /* NVTOOLSEXT_CUDART_V3 */
