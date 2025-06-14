#include <flashinfer/attention_impl.cuh>

namespace flashinfer {

using Params = BatchPrefillPagedParams<half, __nv_fp8_e5m2, half, int32_t>;

using AttentionVariant1 = DefaultAttention<true, /*use_sliding_window=*/true, /*use_logits_soft_cap=*/false, /*use_alibi_bias=*/false>;

template cudaError_t BatchPrefillWithPagedKVCacheDispatched<128, 128, 128, PosEncodingMode::kNone, 0, MaskMode::kCustom, AttentionVariant1, Params>(
    Params params,
    half* tmp_v,
    float* tmp_s, cudaStream_t stream);
    
template cudaError_t BatchPrefillWithPagedKVCacheDispatched<64, 128, 128, PosEncodingMode::kNone, 0, MaskMode::kCustom, AttentionVariant1, Params>(
    Params params,
    half* tmp_v,
    float* tmp_s, cudaStream_t stream);
    
template cudaError_t BatchPrefillWithPagedKVCacheDispatched<16, 128, 128, PosEncodingMode::kNone, 0, MaskMode::kCustom, AttentionVariant1, Params>(
    Params params,
    half* tmp_v,
    float* tmp_s, cudaStream_t stream);
    

using AttentionVariant2 = DefaultAttention<true, /*use_sliding_window=*/true, /*use_logits_soft_cap=*/true, /*use_alibi_bias=*/false>;

template cudaError_t BatchPrefillWithPagedKVCacheDispatched<128, 128, 128, PosEncodingMode::kNone, 0, MaskMode::kCustom, AttentionVariant2, Params>(
    Params params,
    half* tmp_v,
    float* tmp_s, cudaStream_t stream);
    
template cudaError_t BatchPrefillWithPagedKVCacheDispatched<64, 128, 128, PosEncodingMode::kNone, 0, MaskMode::kCustom, AttentionVariant2, Params>(
    Params params,
    half* tmp_v,
    float* tmp_s, cudaStream_t stream);
    
template cudaError_t BatchPrefillWithPagedKVCacheDispatched<16, 128, 128, PosEncodingMode::kNone, 0, MaskMode::kCustom, AttentionVariant2, Params>(
    Params params,
    half* tmp_v,
    float* tmp_s, cudaStream_t stream);
    

using AttentionVariant3 = DefaultAttention<true, /*use_sliding_window=*/false, /*use_logits_soft_cap=*/false, /*use_alibi_bias=*/false>;

template cudaError_t BatchPrefillWithPagedKVCacheDispatched<128, 128, 128, PosEncodingMode::kNone, 0, MaskMode::kCustom, AttentionVariant3, Params>(
    Params params,
    half* tmp_v,
    float* tmp_s, cudaStream_t stream);
    
template cudaError_t BatchPrefillWithPagedKVCacheDispatched<64, 128, 128, PosEncodingMode::kNone, 0, MaskMode::kCustom, AttentionVariant3, Params>(
    Params params,
    half* tmp_v,
    float* tmp_s, cudaStream_t stream);
    
template cudaError_t BatchPrefillWithPagedKVCacheDispatched<16, 128, 128, PosEncodingMode::kNone, 0, MaskMode::kCustom, AttentionVariant3, Params>(
    Params params,
    half* tmp_v,
    float* tmp_s, cudaStream_t stream);
    

using AttentionVariant4 = DefaultAttention<true, /*use_sliding_window=*/false, /*use_logits_soft_cap=*/true, /*use_alibi_bias=*/false>;

template cudaError_t BatchPrefillWithPagedKVCacheDispatched<128, 128, 128, PosEncodingMode::kNone, 0, MaskMode::kCustom, AttentionVariant4, Params>(
    Params params,
    half* tmp_v,
    float* tmp_s, cudaStream_t stream);
    
template cudaError_t BatchPrefillWithPagedKVCacheDispatched<64, 128, 128, PosEncodingMode::kNone, 0, MaskMode::kCustom, AttentionVariant4, Params>(
    Params params,
    half* tmp_v,
    float* tmp_s, cudaStream_t stream);
    
template cudaError_t BatchPrefillWithPagedKVCacheDispatched<16, 128, 128, PosEncodingMode::kNone, 0, MaskMode::kCustom, AttentionVariant4, Params>(
    Params params,
    half* tmp_v,
    float* tmp_s, cudaStream_t stream);
    

}