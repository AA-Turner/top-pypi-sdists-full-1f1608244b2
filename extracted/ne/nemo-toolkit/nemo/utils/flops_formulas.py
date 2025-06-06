# Copyright (c) 2024, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass
from typing import List, Optional, Union

from nemo.collections.common.parts.perf_metrics_utils import LLM_VOCAB_SIZE_MAP


@dataclass
class FLOPSConfig:
    """Contains the model hparams needed for FLOPS computations"""

    gbs: int
    enc_seq_len: Optional[int] = None
    hs: Optional[int] = None
    layers: Optional[int] = None
    ffn_hs: Optional[int] = None
    attention_heads: Optional[int] = None
    moe_router_topk: Optional[int] = None
    query_groups: Optional[int] = None
    img_seq_len: Optional[int] = None
    img_h: Optional[int] = None
    img_w: Optional[int] = None
    in_channels: Optional[int] = None
    patch_dim: Optional[int] = None
    class_token_len: Optional[int] = None
    projector_type: Optional[str] = None
    inp_s: Optional[int] = None
    model_pattern: Optional[str] = None
    vocab_size: Optional[int] = None
    model_channels: Optional[int] = None
    vec_in_dim: Optional[int] = None
    q_lora_rank: Optional[int] = None
    kv_lora_rank: Optional[int] = None
    qk_head_dim: Optional[int] = None
    qk_pos_emb_head_dim: Optional[int] = None
    v_head_dim: Optional[int] = None
    moe_layer_freq: Union[int, List[int]] = None
    moe_shared_expert_intermediate_size: Optional[int] = None
    moe_ffn_hidden_size: Optional[int] = None
    mtp_num_layers: Optional[int] = None
    causal_self_attn: Optional[bool] = None


def gpt3(config: FLOPSConfig):
    """Model FLOPs for GPT3 family"""

    vocab_size = LLM_VOCAB_SIZE_MAP["gpt3"]

    return (
        24 * config.gbs * config.enc_seq_len * config.hs * config.hs
        + 4 * config.gbs * config.enc_seq_len * config.enc_seq_len * config.hs
    ) * (3 * config.layers) + (6 * config.gbs * config.enc_seq_len * config.hs * vocab_size)


def llama2(config: FLOPSConfig):
    """Model FLOPs for llama2 family"""
    vocab_size = LLM_VOCAB_SIZE_MAP["llama2"]

    return (
        config.gbs
        * config.enc_seq_len
        * config.layers
        * config.hs
        * config.hs
        * (
            12
            + (12 * config.query_groups / config.attention_heads)
            + (18 * config.ffn_hs / config.hs)
            + (12 * config.enc_seq_len / config.hs)
            + (6 * vocab_size / (config.layers * config.hs))
        )
    )


def llama3(config: FLOPSConfig):
    """Model FLOPs for llama3 family"""
    vocab_size = LLM_VOCAB_SIZE_MAP["llama3"]

    return (
        config.gbs
        * config.enc_seq_len
        * config.layers
        * config.hs
        * config.hs
        * (
            12
            + (12 * config.query_groups / config.attention_heads)
            + (18 * config.ffn_hs / config.hs)
            + (12 * config.enc_seq_len / config.hs)
            + (6 * vocab_size / (config.layers * config.hs))
        )
    )


def nemotron(config: FLOPSConfig):
    """Model FLOPs for nemotron family"""
    vocab_size = LLM_VOCAB_SIZE_MAP["nemotron"]

    return (
        config.gbs
        * config.enc_seq_len
        * config.layers
        * config.hs
        * config.hs
        * (
            12
            + (12 * config.query_groups / config.attention_heads)
            + (12 * config.ffn_hs / config.hs)
            + (12 * config.enc_seq_len / config.hs)
            + (6 * vocab_size / (config.layers * config.hs))
        )
    )


def mixtral(config: FLOPSConfig):
    """Model FLOPs for mixtral family"""
    vocab_size = LLM_VOCAB_SIZE_MAP["mixtral"]

    return (
        config.gbs
        * config.enc_seq_len
        * config.layers
        * config.hs
        * config.hs
        * (
            12
            + (12 * config.query_groups / config.attention_heads)
            + (18 * config.moe_router_topk * config.ffn_hs / config.hs)
            + (12 * config.enc_seq_len / config.hs)
            + (6 * vocab_size / (config.layers * config.hs))
        )
    )


def bert(config: FLOPSConfig):
    """Model FLOPs for BERT family"""
    vocab_size = LLM_VOCAB_SIZE_MAP["bert"]

    return (
        72
        * config.gbs
        * config.layers
        * config.enc_seq_len
        * config.hs
        * config.hs
        * (1 + (config.enc_seq_len / (6 * config.hs)) + (vocab_size / (12 * config.hs * config.layers)))
    )


def clip_vit_l(config: FLOPSConfig):
    """Model FLOPs for CLIP ViT"""

    if config.img_seq_len is None:
        config.img_seq_len = (config.img_h * config.img_w) / (
            config.patch_dim * config.patch_dim
        ) + config.class_token_len
    return config.gbs * config.layers * config.hs * config.hs * config.img_seq_len * (
        24 + (4 * config.img_seq_len / config.hs)
    ) + (2 * config.gbs * config.hs * config.in_channels * config.img_h * config.img_w)


def neva_projection(config: FLOPSConfig):
    """Model FLOPs for NeVA Projection"""

    if "mlp" in config.projector_type:
        return 6 * config.gbs * config.img_seq_len * config.ffn_hs * (config.inp_s + config.hs)
    elif config.projector_type == "affine":
        return 6 * config.gbs * config.img_seq_len * config.inp_s * config.hs
    else:
        raise ValueError(
            f"NeVA Projections FLOPs calculator only supports 'mlp', 'mcore_mlp'"
            f" or 'affine' projector_type but found {config.projector_type}"
        )


def flux(config: FLOPSConfig):
    """Model FLOPs for FLUX"""

    hs = config.hs
    seq_len = config.model_channels + config.inp_s
    base_factor = 6 * config.gbs  # common multiplier for most terms

    # Joint layer computations
    joint_layer_flops = (
        base_factor
        * config.layers[0]
        * (
            10 * hs * hs  # hidden size operations
            + 2 * hs * (config.model_channels + config.inp_s) * (1 + hs * 5)  # channel and context joint attention
            + 2 * (config.model_channels + config.inp_s) * hs  # final projection
        )
    )

    # Single layer computations
    single_layer_flops = (
        base_factor
        * config.layers[1]
        * seq_len
        * hs
        * (
            3  # linear Y
            + 1  # Modulation
            + 4 * hs  # Linear computations
            + (3 * hs + 2 * seq_len)  # attention operations
            + 5 * hs  # feed-forward
            + 1  # Modulation
        )
    )

    # Embedding and projection layers
    other_flops = base_factor * (
        config.inp_s * config.in_channels * hs  # image embedding
        + config.inp_s * hs * config.model_channels  # text embedding
        + config.vec_in_dim * hs
        + hs * hs  # vector embedding
        + 2 * (config.model_channels * hs + hs * hs)  # guidance + timestep embedding
        + (config.inp_s * config.in_channels * hs) / config.gbs  # final projection
    )

    return joint_layer_flops + single_layer_flops + other_flops


def deepseekv3(config: FLOPSConfig):
    """Model FLOPs for DeepSeek V3"""

    # self-attention flops
    bmm1_flops = (
        0.5 * (config.qk_head_dim + config.qk_pos_emb_head_dim) * config.attention_heads * (config.enc_seq_len**2)
    )
    bmm2_flops = 0.5 * config.v_head_dim * config.attention_heads * (config.enc_seq_len**2)
    per_input_attention_flops = 6 * (bmm1_flops + bmm2_flops) * config.layers
    if config.mtp_num_layers is not None:
        per_input_attention_flops += 6 * (bmm1_flops + bmm2_flops) * config.mtp_num_layers

    # linear layer flops
    per_layer_mla_params = config.hs * config.q_lora_rank + config.q_lora_rank * (
        (config.qk_head_dim + config.qk_pos_emb_head_dim) * config.attention_heads
    )  # Q
    per_layer_mla_params += config.hs * config.qk_pos_emb_head_dim  # K^R
    per_layer_mla_params += config.hs * config.kv_lora_rank + config.kv_lora_rank * (
        (config.qk_head_dim + config.v_head_dim) * config.attention_heads
    )  # K^C and V^C
    per_layer_mla_params += config.v_head_dim * config.attention_heads * config.hs  # Proj
    mla_params = per_layer_mla_params * config.layers
    if config.mtp_num_layers is not None:
        mla_params += per_layer_mla_params * config.mtp_num_layers

    dense_layer_ffn_params = config.hs * config.ffn_hs * 3  # gated linear unit
    per_shared_expert_params = config.hs * config.moe_shared_expert_intermediate_size * 3
    per_selected_expert_params = config.hs * config.moe_ffn_hidden_size * 3
    ffn_params = 0

    if isinstance(config.moe_layer_freq, int):
        moe_layer_pattern = [1 if (i % config.moe_layer_freq == 0) else 0 for i in range(config.layers)]
    else:
        moe_layer_pattern = config.moe_layer_freq
    for i in moe_layer_pattern:
        if i == 0:
            ffn_params += dense_layer_ffn_params
        else:
            ffn_params += per_shared_expert_params + (per_selected_expert_params * config.moe_router_topk)
    if config.mtp_num_layers is not None:
        for i in range(config.mtp_num_layers):
            ffn_params += per_shared_expert_params + (per_selected_expert_params * config.moe_router_topk)
    per_input_params = mla_params + ffn_params
    per_input_linear_flops = 6 * per_input_params * config.enc_seq_len

    # vocab flops
    per_input_vocab_flops = 6 * config.vocab_size * config.hs * config.enc_seq_len
    if config.mtp_num_layers is not None:
        for i in range(config.mtp_num_layers):
            per_input_vocab_flops += 6 * config.vocab_size * config.hs * config.enc_seq_len
            per_input_vocab_flops += 6 * config.hs * 2 * config.hs * config.enc_seq_len

    return (per_input_attention_flops + per_input_linear_flops + per_input_vocab_flops) * config.gbs
