/**
 * Copyright 2022-2025, XGBoost Contributors
 */
#ifndef XGBOOST_COMMON_STATS_H_
#define XGBOOST_COMMON_STATS_H_
#include <algorithm>
#include <iterator>  // for distance
#include <limits>
#include <vector>

#include "algorithm.h"        // for StableSort
#include "optional_weight.h"  // OptionalWeights
#include "xgboost/context.h"  // Context
#include "xgboost/linalg.h"   // TensorView,VectorView
#include "xgboost/logging.h"  // CHECK_GE

#if !defined(XGBOOST_USE_CUDA)
#include "common.h"  // AssertGPUSupport
#endif

namespace xgboost {
namespace common {

/**
 * @brief Quantile using linear interpolation.
 *
 *   https://www.itl.nist.gov/div898/handbook/prc/section2/prc262.htm
 *
 * \param alpha Quantile, must be in range [0, 1].
 * \param begin Iterator begin for input array.
 * \param end   Iterator end for input array.
 *
 * \return The result of interpolation.
 */
template <typename Iter,
          typename R = std::remove_reference_t<typename std::iterator_traits<Iter>::value_type>>
[[nodiscard]] R Quantile(Context const* ctx, double alpha, Iter const& begin, Iter const& end) {
  CHECK(alpha >= 0 && alpha <= 1);
  auto n = static_cast<double>(std::distance(begin, end));
  if (n == 0) {
    return std::numeric_limits<float>::quiet_NaN();
  }

  std::vector<std::size_t> sorted_idx(n);
  std::iota(sorted_idx.begin(), sorted_idx.end(), 0);
  StableSort(ctx, sorted_idx.begin(), sorted_idx.end(),
             [&](std::size_t l, std::size_t r) { return *(begin + l) < *(begin + r); });

  auto val = [&](size_t i) {
    return *(begin + sorted_idx[i]);
  };
  static_assert(std::is_same_v<decltype(val(0)), float>);

  if (alpha <= (1 / (n + 1))) {
    return val(0);
  }
  if (alpha >= (n / (n + 1))) {
    return val(sorted_idx.size() - 1);
  }

  double x = alpha * static_cast<double>((n + 1));
  double k = std::floor(x) - 1;
  CHECK_GE(k, 0);
  double d = (x - 1) - k;

  auto v0 = val(static_cast<size_t>(k));
  auto v1 = val(static_cast<size_t>(k) + 1);
  return v0 + d * (v1 - v0);
}

/**
 * \brief Calculate the weighted quantile with step function. Unlike the unweighted
 *        version, no interpolation is used.
 *
 *   See https://aakinshin.net/posts/weighted-quantiles/ for some discussions on computing
 *   weighted quantile with interpolation.
 */
template <typename Iter, typename WeightIter,
          typename R = std::remove_reference_t<typename std::iterator_traits<Iter>::value_type>>
[[nodiscard]] R WeightedQuantile(Context const* ctx, double alpha, Iter begin, Iter end,
                                 WeightIter w_begin) {
  auto n = static_cast<double>(std::distance(begin, end));
  if (n == 0) {
    return std::numeric_limits<float>::quiet_NaN();
  }
  std::vector<size_t> sorted_idx(n);
  std::iota(sorted_idx.begin(), sorted_idx.end(), 0);
  StableSort(ctx, sorted_idx.begin(), sorted_idx.end(),
             [&](std::size_t l, std::size_t r) { return *(begin + l) < *(begin + r); });

  auto val = [&](size_t i) {
    return *(begin + sorted_idx[i]);
  };

  std::vector<float> weight_cdf(n);  // S_n
  // weighted cdf is sorted during construction
  weight_cdf[0] = *(w_begin + sorted_idx[0]);
  for (size_t i = 1; i < n; ++i) {
    weight_cdf[i] = weight_cdf[i - 1] + w_begin[sorted_idx[i]];
  }
  float thresh = weight_cdf.back() * alpha;
  std::size_t idx =
      std::lower_bound(weight_cdf.cbegin(), weight_cdf.cend(), thresh) - weight_cdf.cbegin();
  idx = std::min(idx, static_cast<size_t>(n - 1));
  return val(idx);
}

namespace cuda_impl {
void Median(Context const* ctx, linalg::TensorView<float const, 2> t, OptionalWeights weights,
            linalg::Tensor<float, 1>* out);

void Mean(Context const* ctx, linalg::VectorView<float const> v, linalg::VectorView<float> out);

void SampleMean(Context const* ctx, bool is_column_split, linalg::MatrixView<float const> d_v,
                linalg::VectorView<float> d_out);

void WeightedSampleMean(Context const* ctx, bool is_column_split,
                        linalg::MatrixView<float const> d_v, common::Span<float const> d_w,
                        linalg::VectorView<float> d_out);

#if !defined(XGBOOST_USE_CUDA)
inline void Median(Context const*, linalg::TensorView<float const, 2>, OptionalWeights,
                   linalg::Tensor<float, 1>*) {
  common::AssertGPUSupport();
}
inline void Mean(Context const*, linalg::VectorView<float const>, linalg::VectorView<float>) {
  common::AssertGPUSupport();
}

inline void SampleMean(Context const*, bool, linalg::MatrixView<float const>,
                       linalg::VectorView<float>) {
  common::AssertGPUSupport();
}

inline void WeightedSampleMean(Context const*, bool, linalg::MatrixView<float const>,
                               common::Span<float const>, linalg::VectorView<float>) {
  common::AssertGPUSupport();
}

#endif  // !defined(XGBOOST_USE_CUDA)
}  // namespace cuda_impl

/**
 * @brief Calculate medians for each column of the input matrix.
 */
void Median(Context const* ctx, linalg::Matrix<float> const& t,
            HostDeviceVector<float> const& weights, linalg::Tensor<float, 1>* out);

/**
 * @brief Calculate the mean value of a vector.
 */
void Mean(Context const* ctx, linalg::Vector<float> const& v, linalg::Vector<float>* out);

/**
 * @brief Calculate the mean value for the first axis.
 */
void SampleMean(Context const* ctx, bool is_column_split, linalg::Matrix<float> const& v,
                linalg::Vector<float>* out);

/**
 * @brief Calculate the weighted mean value for the first axis, weights are assumed to be
 *        equal to or greater than zero.
 */
void WeightedSampleMean(Context const* ctx, bool is_column_split, linalg::Matrix<float> const& v,
                        HostDeviceVector<float> const& w, linalg::Vector<float>* out);
}  // namespace common
}  // namespace xgboost
#endif  // XGBOOST_COMMON_STATS_H_
