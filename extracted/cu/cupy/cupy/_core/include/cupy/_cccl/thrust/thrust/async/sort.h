/*
 *  Copyright 2008-2021 NVIDIA Corporation
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

/*! \file
 *  \brief Algorithms for asynchronously sorting a range.
 */

#pragma once

#include <thrust/detail/config.h>

#if defined(_CCCL_IMPLICIT_SYSTEM_HEADER_GCC)
#  pragma GCC system_header
#elif defined(_CCCL_IMPLICIT_SYSTEM_HEADER_CLANG)
#  pragma clang system_header
#elif defined(_CCCL_IMPLICIT_SYSTEM_HEADER_MSVC)
#  pragma system_header
#endif // no system header
#include <thrust/detail/cpp14_required.h>

#if _CCCL_STD_VER >= 2014

#  include <thrust/detail/select_system.h>
#  include <thrust/detail/static_assert.h>
#  include <thrust/event.h>
#  include <thrust/system/detail/adl/async/sort.h>
#  include <thrust/type_traits/is_execution_policy.h>
#  include <thrust/type_traits/logical_metafunctions.h>

#  include <cuda/std/type_traits>

THRUST_NAMESPACE_BEGIN

namespace async
{

/*! \cond
 */

namespace unimplemented
{

_CCCL_SUPPRESS_DEPRECATED_PUSH
template <typename DerivedPolicy, typename ForwardIt, typename Sentinel, typename StrictWeakOrdering>
CCCL_DEPRECATED _CCCL_HOST event<DerivedPolicy>
async_stable_sort(thrust::execution_policy<DerivedPolicy>&, ForwardIt, Sentinel, StrictWeakOrdering)
{
  THRUST_STATIC_ASSERT_MSG((thrust::detail::depend_on_instantiation<ForwardIt, false>::value),
                           "this algorithm is not implemented for the specified system");
  return {};
}
_CCCL_SUPPRESS_DEPRECATED_POP

} // namespace unimplemented

namespace stable_sort_detail
{

using thrust::async::unimplemented::async_stable_sort;

// clang-format off
struct stable_sort_fn final
{
  _CCCL_SUPPRESS_DEPRECATED_PUSH
  template <
    typename DerivedPolicy
  , typename ForwardIt, typename Sentinel, typename StrictWeakOrdering
  >
  _CCCL_HOST

  static auto call(
    thrust::detail::execution_policy_base<DerivedPolicy> const& exec
  , ForwardIt&& first, Sentinel&& last
  , StrictWeakOrdering&& comp
  )
  // ADL dispatch.
  THRUST_RETURNS(
    async_stable_sort(
      thrust::detail::derived_cast(thrust::detail::strip_const(exec))
    , THRUST_FWD(first), THRUST_FWD(last)
    , THRUST_FWD(comp)
    )
  )
  _CCCL_SUPPRESS_DEPRECATED_POP

_CCCL_SUPPRESS_DEPRECATED_PUSH
  template <
    typename DerivedPolicy
  , typename ForwardIt, typename Sentinel
  >
  _CCCL_HOST

  static auto call(
    thrust::detail::execution_policy_base<DerivedPolicy> const& exec
  , ForwardIt&& first, Sentinel&& last
  )
  // ADL dispatch.
  THRUST_RETURNS(
    async_stable_sort(
      thrust::detail::derived_cast(thrust::detail::strip_const(exec))
    , THRUST_FWD(first), THRUST_FWD(last)
    , thrust::less<
        typename iterator_traits<::cuda::std::remove_cvref_t<ForwardIt>>::value_type
      >{}
    )
  )
  _CCCL_SUPPRESS_DEPRECATED_POP

  template <typename ForwardIt, typename Sentinel, typename StrictWeakOrdering>
  _CCCL_HOST
  static auto call(ForwardIt&& first, Sentinel&& last, StrictWeakOrdering&& comp)
  THRUST_RETURNS(
    stable_sort_fn::call(
      thrust::detail::select_system(
        typename iterator_system<::cuda::std::remove_cvref_t<ForwardIt>>::type{}
      )
    , THRUST_FWD(first), THRUST_FWD(last)
    , THRUST_FWD(comp)
    )
  )

  template <typename ForwardIt, typename Sentinel>
  _CCCL_HOST
  static auto call(ForwardIt&& first, Sentinel&& last)
  THRUST_RETURNS(
    stable_sort_fn::call(
      THRUST_FWD(first), THRUST_FWD(last)
    , thrust::less<
        typename iterator_traits<::cuda::std::remove_cvref_t<ForwardIt>>::value_type
      >{}
    )
  )

  template <typename... Args>
  #if !_CCCL_CUDA_COMPILER(CLANG)
  // clang in CUDA mode can only handle one attribute
  _CCCL_NODISCARD _CCCL_HOST
  #endif
 CCCL_DEPRECATED auto operator()(Args&&... args) const
  THRUST_RETURNS(
    call(THRUST_FWD(args)...)
  )
};
// clang-format on

} // namespace stable_sort_detail

// note: cannot add a CCCL_DEPRECATED here because the global variable is emitted into cudafe1.stub.c and we cannot
// suppress the warning there
//! deprecated [Since 2.8.0]
_CCCL_GLOBAL_CONSTANT stable_sort_detail::stable_sort_fn stable_sort{};

namespace fallback
{

_CCCL_SUPPRESS_DEPRECATED_PUSH
template <typename DerivedPolicy, typename ForwardIt, typename Sentinel, typename StrictWeakOrdering>
CCCL_DEPRECATED _CCCL_HOST event<DerivedPolicy>
async_sort(thrust::execution_policy<DerivedPolicy>& exec, ForwardIt&& first, Sentinel&& last, StrictWeakOrdering&& comp)
{
  return async_stable_sort(thrust::detail::derived_cast(exec), THRUST_FWD(first), THRUST_FWD(last), THRUST_FWD(comp));
}
_CCCL_SUPPRESS_DEPRECATED_POP

} // namespace fallback

namespace sort_detail
{

using thrust::async::fallback::async_sort;

// clang-format off
struct sort_fn final
{
  _CCCL_SUPPRESS_DEPRECATED_PUSH
  template <
    typename DerivedPolicy
  , typename ForwardIt, typename Sentinel, typename StrictWeakOrdering
  >
  _CCCL_HOST
  static auto call(
    thrust::detail::execution_policy_base<DerivedPolicy> const& exec
  , ForwardIt&& first, Sentinel&& last
  , StrictWeakOrdering&& comp
  )
  // ADL dispatch.
  THRUST_RETURNS(
    async_sort(
      thrust::detail::derived_cast(thrust::detail::strip_const(exec))
    , THRUST_FWD(first), THRUST_FWD(last)
    , THRUST_FWD(comp)
    )
  )
  _CCCL_SUPPRESS_DEPRECATED_POP

  template <
    typename DerivedPolicy
  , typename ForwardIt, typename Sentinel
  >
  _CCCL_HOST
  static auto call3(
    thrust::detail::execution_policy_base<DerivedPolicy> const& exec
  , ForwardIt&& first, Sentinel&& last
  , thrust::true_type
  )
  THRUST_RETURNS(
    sort_fn::call(
      exec
    , THRUST_FWD(first), THRUST_FWD(last)
    , thrust::less<
        typename iterator_traits<::cuda::std::remove_cvref_t<ForwardIt>>::value_type
      >{}
    )
  )

  template <typename ForwardIt, typename Sentinel, typename StrictWeakOrdering>
  _CCCL_HOST
  static auto call3(ForwardIt&& first, Sentinel&& last,
                    StrictWeakOrdering&& comp,
                    thrust::false_type)
  THRUST_RETURNS(
    sort_fn::call(
      thrust::detail::select_system(
        typename iterator_system<::cuda::std::remove_cvref_t<ForwardIt>>::type{}
      )
    , THRUST_FWD(first), THRUST_FWD(last)
    , THRUST_FWD(comp)
    )
  )

  // MSVC WAR: MSVC gets angsty and eats all available RAM when we try to detect
  // if T1 is an execution_policy by using SFINAE. Switching to a static
  // dispatch pattern to prevent this.
  template <typename T1, typename T2, typename T3>
  _CCCL_HOST
  static auto call(T1&& t1, T2&& t2, T3&& t3)
  THRUST_RETURNS(
    sort_fn::call3(THRUST_FWD(t1), THRUST_FWD(t2), THRUST_FWD(t3),
                   thrust::is_execution_policy<::cuda::std::remove_cvref_t<T1>>{})
  )

  template <typename ForwardIt, typename Sentinel>
  _CCCL_HOST
  static auto call(ForwardIt&& first, Sentinel&& last)
  THRUST_RETURNS(
    sort_fn::call(
      thrust::detail::select_system(
        typename iterator_system<::cuda::std::remove_cvref_t<ForwardIt>>::type{}
      )
    , THRUST_FWD(first), THRUST_FWD(last)
    , thrust::less<
        typename iterator_traits<::cuda::std::remove_cvref_t<ForwardIt>>::value_type
      >{}
    )
  )

  template <typename... Args>
  #if !_CCCL_CUDA_COMPILER(CLANG)
  // clang in CUDA mode can only handle one attribute
  _CCCL_NODISCARD _CCCL_HOST
  #endif
 CCCL_DEPRECATED auto operator()(Args&&... args) const
  THRUST_RETURNS(
    call(THRUST_FWD(args)...)
  )
};
// clang-format on

} // namespace sort_detail

// note: cannot add a CCCL_DEPRECATED here because the global variable is emitted into cudafe1.stub.c and we cannot
// suppress the warning there
//! deprecated [Since 2.8.0]
_CCCL_GLOBAL_CONSTANT sort_detail::sort_fn sort{};

/*! \endcond
 */

} // namespace async

THRUST_NAMESPACE_END

#endif
