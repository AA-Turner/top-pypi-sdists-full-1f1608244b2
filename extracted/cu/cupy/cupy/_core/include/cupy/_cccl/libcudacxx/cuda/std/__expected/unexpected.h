//===----------------------------------------------------------------------===//
//
// Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
// SPDX-FileCopyrightText: Copyright (c) 2022 NVIDIA CORPORATION & AFFILIATES.
//
//===----------------------------------------------------------------------===//

#ifndef _LIBCUDACXX___EXPECTED_UNEXPECTED_H
#define _LIBCUDACXX___EXPECTED_UNEXPECTED_H

#include <cuda/std/detail/__config>

#if defined(_CCCL_IMPLICIT_SYSTEM_HEADER_GCC)
#  pragma GCC system_header
#elif defined(_CCCL_IMPLICIT_SYSTEM_HEADER_CLANG)
#  pragma clang system_header
#elif defined(_CCCL_IMPLICIT_SYSTEM_HEADER_MSVC)
#  pragma system_header
#endif // no system header

#include <cuda/std/__concepts/concept_macros.h>
#include <cuda/std/__type_traits/integral_constant.h>
#include <cuda/std/__type_traits/is_array.h>
#include <cuda/std/__type_traits/is_const.h>
#include <cuda/std/__type_traits/is_constructible.h>
#include <cuda/std/__type_traits/is_nothrow_constructible.h>
#include <cuda/std/__type_traits/is_object.h>
#include <cuda/std/__type_traits/is_same.h>
#include <cuda/std/__type_traits/is_swappable.h>
#include <cuda/std/__type_traits/is_volatile.h>
#include <cuda/std/__type_traits/remove_cvref.h>
#include <cuda/std/__utility/forward.h>
#include <cuda/std/__utility/in_place.h>
#include <cuda/std/__utility/move.h>
#include <cuda/std/initializer_list>

_LIBCUDACXX_BEGIN_NAMESPACE_STD

#if _CCCL_STD_VER > 2011

template <class _Err>
class unexpected;

namespace __unexpected
{
template <class _Tp>
_CCCL_INLINE_VAR constexpr bool __is_unexpected = false;

template <class _Err>
_CCCL_INLINE_VAR constexpr bool __is_unexpected<unexpected<_Err>> = true;

template <class _Tp>
_CCCL_INLINE_VAR constexpr bool __valid_unexpected =
  _CCCL_TRAIT(is_object, _Tp) && !_CCCL_TRAIT(is_array, _Tp) && !__is_unexpected<_Tp> && !_CCCL_TRAIT(is_const, _Tp)
  && !_CCCL_TRAIT(is_volatile, _Tp);
} // namespace __unexpected

// [expected.un.general]
template <class _Err>
class unexpected
{
  static_assert(__unexpected::__valid_unexpected<_Err>,
                "[expected.un.general] states a program that instantiates std::unexpected for a non-object type, an "
                "array type, a specialization of unexpected, or a cv-qualified type is ill-formed.");

  template <class, class>
  friend class expected;

public:
  // [expected.un.ctor]
  _CCCL_HIDE_FROM_ABI unexpected(const unexpected&) = default;
  _CCCL_HIDE_FROM_ABI unexpected(unexpected&&)      = default;

  _CCCL_EXEC_CHECK_DISABLE
  _CCCL_TEMPLATE(class _Error = _Err)
  _CCCL_REQUIRES((!_CCCL_TRAIT(is_same, remove_cvref_t<_Error>, unexpected)
                  && !_CCCL_TRAIT(is_same, remove_cvref_t<_Error>, in_place_t)
                  && _CCCL_TRAIT(is_constructible, _Err, _Error)))
  _LIBCUDACXX_HIDE_FROM_ABI constexpr explicit unexpected(_Error&& __error) noexcept(
    _CCCL_TRAIT(is_nothrow_constructible, _Err, _Error))
      : __unex_(_CUDA_VSTD::forward<_Error>(__error))
  {}

  _CCCL_EXEC_CHECK_DISABLE
  _CCCL_TEMPLATE(class... _Args)
  _CCCL_REQUIRES(_CCCL_TRAIT(is_constructible, _Err, _Args...))
  _LIBCUDACXX_HIDE_FROM_ABI constexpr explicit unexpected(in_place_t, _Args&&... __args) noexcept(
    _CCCL_TRAIT(is_nothrow_constructible, _Err, _Args...))
      : __unex_(_CUDA_VSTD::forward<_Args>(__args)...)
  {}

  _CCCL_EXEC_CHECK_DISABLE
  _CCCL_TEMPLATE(class _Up, class... _Args)
  _CCCL_REQUIRES(_CCCL_TRAIT(is_constructible, _Err, initializer_list<_Up>&, _Args...))
  _LIBCUDACXX_HIDE_FROM_ABI constexpr explicit unexpected(
    in_place_t,
    initializer_list<_Up> __il,
    _Args&&... __args) noexcept(_CCCL_TRAIT(is_nothrow_constructible, _Err, initializer_list<_Up>&, _Args...))
      : __unex_(__il, _CUDA_VSTD::forward<_Args>(__args)...)
  {}

  _CCCL_HIDE_FROM_ABI constexpr unexpected& operator=(const unexpected&) = default;
  _CCCL_HIDE_FROM_ABI constexpr unexpected& operator=(unexpected&&)      = default;

  // [expected.un.obs]
  _CCCL_NODISCARD _LIBCUDACXX_HIDE_FROM_ABI constexpr const _Err& error() const& noexcept
  {
    return __unex_;
  }

  _CCCL_NODISCARD _LIBCUDACXX_HIDE_FROM_ABI constexpr _Err& error() & noexcept
  {
    return __unex_;
  }

  _CCCL_NODISCARD _LIBCUDACXX_HIDE_FROM_ABI constexpr const _Err&& error() const&& noexcept
  {
    return _CUDA_VSTD::move(__unex_);
  }

  _CCCL_NODISCARD _LIBCUDACXX_HIDE_FROM_ABI constexpr _Err&& error() && noexcept
  {
    return _CUDA_VSTD::move(__unex_);
  }

  // [expected.un.swap]
  _CCCL_EXEC_CHECK_DISABLE
  _LIBCUDACXX_HIDE_FROM_ABI constexpr void swap(unexpected& __other) noexcept(_CCCL_TRAIT(is_nothrow_swappable, _Err))
  {
    static_assert(_CCCL_TRAIT(is_swappable, _Err), "E must be swappable");
    using _CUDA_VSTD::swap;
    swap(__unex_, __other.__unex_);
  }

  _CCCL_EXEC_CHECK_DISABLE
  _CCCL_TEMPLATE(class _Err2 = _Err)
  _CCCL_REQUIRES(_CCCL_TRAIT(is_swappable, _Err2))
  friend _LIBCUDACXX_HIDE_FROM_ABI constexpr void
  swap(unexpected& __lhs, unexpected& __rhs) noexcept(_CCCL_TRAIT(is_nothrow_swappable, _Err2))
  {
    __lhs.swap(__rhs);
    return;
  }

  // [expected.un.eq]
  _CCCL_EXEC_CHECK_DISABLE
  template <class _UErr>
  _CCCL_NODISCARD_FRIEND _LIBCUDACXX_HIDE_FROM_ABI constexpr bool
  operator==(const unexpected& __lhs,
             const unexpected<_UErr>& __rhs) noexcept(noexcept(static_cast<bool>(__lhs.error() == __rhs.error())))
  {
    return __lhs.error() == __rhs.error();
  }
#  if _CCCL_STD_VER < 2020
  _CCCL_EXEC_CHECK_DISABLE
  template <class _UErr>
  _CCCL_NODISCARD_FRIEND _LIBCUDACXX_HIDE_FROM_ABI constexpr bool
  operator!=(const unexpected& __lhs,
             const unexpected<_UErr>& __rhs) noexcept(noexcept(static_cast<bool>(__lhs.error() != __rhs.error())))
  {
    return __lhs.error() != __rhs.error();
  }
#  endif

private:
  _Err __unex_;
};

#  if !defined(_CCCL_NO_DEDUCTION_GUIDES)
template <class _Err>
unexpected(_Err) -> unexpected<_Err>;
#  endif // !defined(_CCCL_NO_DEDUCTION_GUIDES)

#endif // _CCCL_STD_VER > 2011

_LIBCUDACXX_END_NAMESPACE_STD

#endif // _LIBCUDACXX___EXPECTED_UNEXPECTED_H
