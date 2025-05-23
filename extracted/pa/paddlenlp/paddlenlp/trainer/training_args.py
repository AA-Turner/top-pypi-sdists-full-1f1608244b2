# Copyright 2020-present the HuggingFace Inc. team.
# Copyright 2020 The HuggingFace Team. All rights reserved.
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

# This file is modified from
#  https://github.com/huggingface/transformers/blob/main/src/transformers/training_args.py

import contextlib
import json
import math
import os
import types
import warnings
from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional

import paddle
import paddle.distributed as dist
from paddle.distributed import fleet

from ..utils.log import logger
from .trainer_utils import (
    IntervalStrategy,
    OptimizerNames,
    SchedulerType,
    ShardingOption,
)

__all__ = [
    "default_logdir",
    "TrainingArguments",
]


def default_logdir() -> str:
    """
    Same default
    """
    import socket
    from datetime import datetime

    current_time = datetime.now().strftime("%b%d_%H-%M-%S")
    return os.path.join("runs", current_time + "_" + socket.gethostname())


@dataclass
class TrainingArguments:
    """
    TrainingArguments is the subset of the arguments we use in our example scripts **which relate to the training loop
    itself**.

    Using [`PdArgumentParser`] we can turn this class into
    [argparse](https://docs.python.org/3/library/argparse#module-argparse) arguments that can be specified on the
    command line.

    Parameters:
        output_dir (`str`):
            The output directory where the model predictions and checkpoints will be written.
        overwrite_output_dir (`bool`, *optional*, defaults to `False`):
            If `True`, overwrite the content of the output directory. Use this to continue training if `output_dir`
            points to a checkpoint directory.
        do_train (`bool`, *optional*, defaults to `False`):
            Whether to run training or not. This argument is not directly used by [`Trainer`], it's intended to be used
            by your training/evaluation scripts instead. See the [example
            scripts](https://github.com/PaddlePaddle/PaddleNLP/tree/develop/examples) for more details.
        do_eval (`bool`, *optional*):
            Whether to run evaluation on the validation set or not. Will be set to `True` if `evaluation_strategy` is
            different from `"no"`. This argument is not directly used by [`Trainer`], it's intended to be used by your
            training/evaluation scripts instead. See the [example
            scripts](https://github.com/PaddlePaddle/PaddleNLP/tree/develop/examples) for more details.
        do_predict (`bool`, *optional*, defaults to `False`):
            Whether to run predictions on the test set or not. This argument is not directly used by [`Trainer`], it's
            intended to be used by your training/evaluation scripts instead. See the [example
            scripts](https://github.com/PaddlePaddle/PaddleNLP/tree/develop/examples) for more details.
        do_export (`bool`, *optional*, defaults to `False`):
            Whether to export inference model or not. This argument is not directly used by [`Trainer`], it's
            intended to be used by your training/evaluation scripts instead.
        evaluation_strategy (`str` or [`~trainer_utils.IntervalStrategy`], *optional*, defaults to `"no"`):
            The evaluation strategy to adopt during training. Possible values are:

                - `"no"`: No evaluation is done during training.
                - `"steps"`: Evaluation is done (and logged) every `eval_steps`.
                - `"epoch"`: Evaluation is done at the end of each epoch.

        prediction_loss_only (`bool`, *optional*, defaults to `False`):
            When performing evaluation and generating predictions, only returns the loss.
        per_device_train_batch_size (`int`, *optional*, defaults to 8):
            The batch size per GPU core/CPU for training.
        per_device_eval_batch_size (`int`, *optional*, defaults to 8):
            The batch size per GPU core/CPU for evaluation.
        gradient_accumulation_steps (`int`, *optional*, defaults to 1):
            Number of updates steps to accumulate the gradients for, before performing a backward/update pass.

            <Tip warning={true}>

            When using gradient accumulation, one step is counted as one step with backward pass. Therefore, logging,
            evaluation, save will be conducted every `gradient_accumulation_steps * xxx_step` training examples.

            </Tip>

        eval_accumulation_steps (`int`, *optional*):
            Number of predictions steps to accumulate the output tensors for, before moving the results to the CPU. If
            left unset, the whole predictions are accumulated on GPU/TPU before being moved to the CPU (faster but
            requires more memory).
        learning_rate (`float`, *optional*, defaults to 5e-5):
            The initial learning rate for [`AdamW`] optimizer.
        weight_decay (`float`, *optional*, defaults to 0):
            The weight decay to apply (if not zero) to all layers except all bias and LayerNorm weights in [`AdamW`]
            optimizer.
        adam_beta1 (`float`, *optional*, defaults to 0.9):
            The beta1 hyperparameter for the [`AdamW`] optimizer.
        adam_beta2 (`float`, *optional*, defaults to 0.999):
            The beta2 hyperparameter for the [`AdamW`] optimizer.
        adam_epsilon (`float`, *optional*, defaults to 1e-8):
            The epsilon hyperparameter for the [`AdamW`] optimizer.
        max_grad_norm (`float`, *optional*, defaults to 1.0):
            Maximum gradient norm (for gradient clipping).
        num_train_epochs(`float`, *optional*, defaults to 1.0):
            Total number of training epochs to perform (if not an integer, will perform the decimal part percents of
            the last epoch before stopping training).
        max_steps (`int`, *optional*, defaults to -1):
            If set to a positive number, the total number of training steps to perform. Overrides `num_train_epochs`.
            In case of using a finite iterable dataset the training may stop before reaching the set number of steps
            when all data is exhausted
        lr_scheduler_type (`str` or [`SchedulerType`], *optional*, defaults to `"linear"`):
            The scheduler type to use. See the documentation of [`SchedulerType`] for all possible values.
        warmup_ratio (`float`, *optional*, defaults to 0.0):
            Ratio of total training steps used for a linear warmup from 0 to `learning_rate`.
        warmup_steps (`int`, *optional*, defaults to 0):
            Number of steps used for a linear warmup from 0 to `learning_rate`. Overrides any effect of `warmup_ratio`.
        num_cycles (`float`, *optional*, defaults to 0.5):
            The number of waves in the cosine scheduler.
        lr_end (`float`, *optional*, defaults to 1e-7):
            The end LR used in the polynomial scheduler.
        power (`float`, *optional*, defaults to 1.0):
            The power factor used in the polynomial scheduler.

        log_on_each_node (`bool`, *optional*, defaults to `True`):
            In multinode distributed training, whether to log using `log_level` once per node, or only on the main
            node.
        logging_dir (`str`, *optional*):
            log directory. Will default to *output_dir/runs/**CURRENT_DATETIME_HOSTNAME***.
        logging_strategy (`str` or [`~trainer_utils.IntervalStrategy`], *optional*, defaults to `"steps"`):
            The logging strategy to adopt during training. Possible values are:

                - `"no"`: No logging is done during training.
                - `"epoch"`: Logging is done at the end of each epoch.
                - `"steps"`: Logging is done every `logging_steps`.

        logging_first_step (`bool`, *optional*, defaults to `False`):
            Whether to log and evaluate the first `global_step` or not.
        logging_steps (`int`, *optional*, defaults to 500):
            Number of update steps between two logs if `logging_strategy="steps"`.
        save_strategy (`str` or [`~trainer_utils.IntervalStrategy`], *optional*, defaults to `"steps"`):
            The checkpoint save strategy to adopt during training. Possible values are:

                - `"no"`: No save is done during training.
                - `"epoch"`: Save is done at the end of each epoch.
                - `"steps"`: Save is done every `save_steps`.
        save_steps (`int`, *optional*, defaults to 500):
            Number of updates steps before two checkpoint saves if `save_strategy="steps"`.
        save_total_limit (`int`, *optional*):
            If a value is passed, will limit the total amount of checkpoints. Deletes the older checkpoints in
            `output_dir`.
        save_on_each_node (`bool`, *optional*, defaults to `False`):
            When doing multi-node distributed training, whether to save models and checkpoints on each node, or only on
            the main one.

            This should not be activated when the different nodes use the same storage as the files will be saved with
            the same names for each node.
        no_cuda (`bool`, *optional*, defaults to `False`):
            Whether to not use CUDA even when it is available or not.
        seed (`int`, *optional*, defaults to 42):
            Random seed that will be set at the beginning of training. To ensure reproducibility across runs, use the
            [`~Trainer.model_init`] function to instantiate the model if it has some randomly initialized parameters.
        fp16 (`bool`, *optional*, defaults to `False`):
            Whether to use fp16 16-bit (mixed) precision training instead of 32-bit training.
        fp16_opt_level (`str`, *optional*, defaults to 'O1'):
            For `fp16` training,  AMP optimization level selected in ['O0', 'O1', 'O2']. See details at
            https://www.paddlepaddle.org.cn/documentation/docs/zh/develop/api/paddle/amp/auto_cast_cn.html
        amp_custom_black_list (`List[str]`, *optional*, defaults to `None`):
            The custom black_list. The set of ops that support fp16/bf16 calculation and are considered numerically-dangerous
            and whose effects may also be observed in downstream ops. These ops will not be converted to fp16/bf16.
        amp_custom_white_list (`List[str]`, *optional*, defaults to `None`):
            The custom white_list. It’s the set of ops that support fp16/bf16 calculation and are considered numerically-safe and
             performance-critical. These ops will be converted to fp16/bf16.
        amp_master_grad (`bool`, *optional*, defaults to `False`):
            For amp opt level=’O2’, whether to use float32 weight gradients
            for calculations such as gradient clipping, weight decay, and weight updates. If master_grad is enabled,
            the weight gradients will be float32 dtype after the backpropagation. Default is False, there is only float16 weight gradients.
            Note: only support model parallel and pipeline parallel for now !!!
        sharding (`str`, *optional*, defaults to ``):
            Whether or not to use Paddle Sharding Data Parallel training (in distributed training
            only). The base option should be `stage1`, `stage2` or `stage3` and you can add
            CPU-offload to `stage2` or `stage3` like this: `stage2 offload` or `stage3 offload`.
            Each stage means:
                stage1 : optimizer state segmentation
                stage2 : optimizer state + gradient segmentation
                stage3 : parameter + gradient + optimizer state segmentation
                offload : offload parameters to cpu
        sharding_parallel_degree (`int`, *optional*, defaults to `-1`)
            Sharding parameter in certain cards group. For example, aussume we use 2 machines each with 8 cards,
            then set sharding_parallel_degree=8, sharding will only communication inside machine.
            default -1 means sharding parameters between all workers.
        tensor_parallel_degree (`int`, *optional*, defaults to `-1`)
            Tensor parallelism is parallel technique proposed in (https://arxiv.org/pdf/2104.04473.pdf see 2.3 Tensor Model Parallelism).
            This technique splits one transformer layer into multi-cards (For examples, tensor_parallel_degree=4, will split a layer to 4-parts)
            tensor_parallel_degree means split the transformer layer to how many parts.
            default -1 for not use tensor parallel,  Suggest tensor_parallel_degree<=8 for better proformance.
            Note, this need model support in source code, currently GPT/BLOOM/LLAMA/BLOOM/CLM/CHATGLM is supported.
        pipeline_parallel_degree (`int`, *optional*, defaults to `-1`)
            Pipeline parallelism is parallel technique proposed in (https://arxiv.org/pdf/2104.04473.pdf see 2.2 Pipeline Model Parallelism).
            Pipeline parallelism assigns multi-transformer layers to different cards, the micro batch data stream passed between cards like pipelines.
            pipeline_parallel_degree means split all transformer layers to how many stages.
            default -1 for not use pipeline parallel.
            Note. this need model support in source code, see llama modeling_pp.py file
        sep_parallel_degree (`int`, *optional*, defaults to `-1`)(
            The paddle sequence parallel strategy. It can reduce the GPU memory of activation to 1/sep, and it is orthogonal to
            data parallel, sharding stage1, tensor parallel and pipeline parallel strategy.
        )
        data_parallel_config (`str`, *optional*)(
            Some additional configs which affect data parallel performance, we provide some option to config it.
            following config is support:
              enable_allreduce_avg_in_gradinent_scale, it replace `allreduce_sum + scale` pattern with `allreduce_avg` when scale gradient in data_parallel, which improve the performance. ONLY supported for auto mode now.
              gradient_sync_after_accumulate, move gradient sync operations from backward into optimizer step when gradient accumulate enabling, which reduce the sync times to improve performance, but will increase the memory usage. ONLY supported for auto mode now.
        tensor_parallel_config (`str`, *optional*)(
            Some additional configs which affect model parallel performance, we provide some option to config it.
            following config is support:
              enable_mp_async_allreduce, it supports all_reduce(dx) overlap with matmul(dw) in ColumnParallelLinear backward when it set True, which can accelerate model parallel performance.
              enable_mp_skip_c_identity, it supports skip c_identity in ColumnParallelLinear and RowParallelLinear. It only works when set mp_async_allreduce is True. It can accelerate model parallel further.
              enable_mp_fused_linear_param_grad_add, it supports fused_linear_param_grad_add in ColumnParallelLinear (cuda >= 11.6). It only works when mp_async_allreduce is true. It can accelerate model parallel further.
              enable_delay_scale_loss, accumulate gradients util optimizer step, all gradients div by accumute step. instead of div accumute step on loss directly.
        pipeline_parallel_config (`str`, *optional*)(
            Some additional config it highly affect the useage of pipeline parallel, we provide some option to config it.
            following config is support:
              disable_p2p_cache_shape, if you max sequence length is varying, please set disable_p2p_cache_shape.
              disable_partial_send_recv, optmize send speed for tensor parallel.
              enable_delay_scale_loss, accumulate gradients util optimizer step, all gradients div by inner pipeline accumute step. instead of div accumute step on loss directly.
              enable_dp_comm_overlap, fuse data parallel gradient communication.
              enable_sharding_comm_overlap, fuse sharding stage 1 parallel gradient communication.
              enable_release_grads, reduce peak memory usage by releasing gradients after each iteration. The creation of gradients will be postponed until backward propagation of the next iteration.
              enable_overlap_p2p_comm, overlap p2p communication with computation.
              enable_clear_every_step_cache, clear every step cache for pipeline parallel.
              disable_non_batch_p2p_comm, disable batched send/recv in pipeline parallel mode.
        sharding_parallel_config (`str`, *optional*)(
            Some additional config it highly affect the useage of sharding parallel, we provide some option to config it.
            following config is support:
              enable_stage1_tensor_fusion, fuse small tensors into big tensor chunks to accelerate communications, may increase memory occupation
              enable_stage1_overlap, fuse small tensors into big tensor chunks to accelerate communications and do communication overlap with backward computation, may harm the backward speed
              enable_stage2_overlap, overlap stage2 NCCL communication with computation. There are some constraints for the overlap, such as the logging_step should be bigger than 1 for broadcast overlap and no other sync could be called during the training for broadcast overlap.
              disable_stage1_reduce_avg, replace reduce_avg with original reduce_sum+scale in stage1, which can be used for accuracy verification.
        recompute (`bool`, *optional*, defaults to `False`):
            Recompute the forward pass to calculate gradients. Used for saving memory.
            Only support for networks with transformer blocks.
        scale_loss (`float`,  *optional*, defaults to 32768):
            The value of initial scale_loss for fp16. (default: 32768)
        local_rank (`int`, *optional*, defaults to -1):
            Rank of the process during distributed training.
        dataloader_drop_last (`bool`, *optional*, defaults to `False`):
            Whether to drop the last incomplete batch (if the length of the dataset is not divisible by the batch size)
            or not.
        eval_steps (`int`, *optional*):
            Number of update steps between two evaluations if `evaluation_strategy="steps"`. Will default to the same
            value as `logging_steps` if not set.
        max_evaluate_steps (`int`, *optional*, defaults to -1):
            If set to a positive number, the total number of evaluation steps to perform.
        dataloader_num_workers (`int`, *optional*, defaults to 0):
            Number of subprocesses to use for data loading. 0 means that the data will be loaded in the
            main process.
        past_index (`int`, *optional*, defaults to -1):
            Some models like TransformerXL or XLNet can make use of the past hidden states for their predictions.
            If this argument is set to a positive int, the `Trainer` will use the corresponding output (usually index 2) as
            the past state and feed it to the model at the next training step under the keyword argument `mems`.
        run_name (`str`, *optional*):
            A descriptor for the run. Typically used for logging.
        disable_tqdm (`bool`, *optional*):
            Whether or not to disable the tqdm progress bars and table of metrics. Will default to `True` if the logging
            level is set to warn or lower (default), `False` otherwise.
        remove_unused_columns (`bool`, *optional*, defaults to `True`):
            If using `datasets.Dataset` datasets, whether or not to automatically remove the columns unused by the
            model forward method.
        label_names (`List[str]`, *optional*):
            The list of keys in your dictionary of inputs that correspond to the labels.
            Will eventually default to `["labels"]` except if the model used is one of the `XxxForQuestionAnswering` in
            which case it will default to `["start_positions", "end_positions"]`.
        load_best_model_at_end (`bool`, *optional*, defaults to `False`):
            Whether or not to load the best model found during training at the end of training.

            <Tip>

            When set to `True`, the parameters `save_strategy` needs to be the same as `eval_strategy`, and in the case
            it is "steps", `save_steps` must be a round multiple of `eval_steps`.

            </Tip>

        metric_for_best_model (`str`, *optional*):
            Use in conjunction with `load_best_model_at_end` to specify the metric to use to compare two different
            models. Must be the name of a metric returned by the evaluation with or without the prefix `"eval_"`. Will
            default to `"loss"` if unspecified and `load_best_model_at_end=True` (to use the evaluation loss).

            If you set this value, `greater_is_better` will default to `True`. Don't forget to set it to `False` if
            your metric is better when lower.
        greater_is_better (`bool`, *optional*):
            Use in conjunction with `load_best_model_at_end` and `metric_for_best_model` to specify if better models
            should have a greater metric or not. Will default to:

            - `True` if `metric_for_best_model` is set to a value that isn't `"loss"` or `"eval_loss"`.
            - `False` if `metric_for_best_model` is not set, or set to `"loss"` or `"eval_loss"`.
        ignore_data_skip (`bool`, *optional*, defaults to `False`):
            When resuming training, whether or not to skip the epochs and batches to get the data loading at the same
            stage as in the previous training. If set to `True`, the training will begin faster (as that skipping step
            can take a long time) but will not yield the same results as the interrupted training would have.
        optim (`str` or [`training_args.OptimizerNames`], *optional*, defaults to `"adamw"`):
            The optimizer to use: adamw, or adafactor.
        length_column_name (`str`, *optional*, defaults to `"length"`):
            Column name for precomputed lengths. If the column exists, grouping by length will use these values rather
            than computing them on train startup. Ignored unless `group_by_length` is `True` and the dataset is an
            instance of `Dataset`.
        report_to (`str` or `List[str]`, *optional*, defaults to `"visualdl"`):
            The list of integrations to report the results and logs to.
            Supported platforms are `"visualdl"`/`"wandb"`/`"tensorboard"`.
            `"none"` for no integrations.
        wandb_api_key (`str`, *optional*):
            Weights & Biases (WandB) API key(s) for authentication with the WandB service.
        resume_from_checkpoint (`str`, *optional*):
            The path to a folder with a valid checkpoint for your model. This argument is not directly used by
            [`Trainer`], it's intended to be used by your training/evaluation scripts instead. See the [example
            scripts](https://github.com/PaddlePaddle/PaddleNLP/tree/develop/examples) for more details.
        flatten_param_grads (`bool`, *optional*):
            Whether use flatten_param_grads method in optimizer, only used on NPU devices. Default is `False`.
        skip_profile_timer (`bool`, *optional*):
            Whether skip profile timer, timer will record time usage of forward/ backward/ step, etc.
        distributed_dataloader (`bool`, *optional*):
            Whether to use distributed dataloader. Default is `False`.
    """

    output_dir: str = field(
        metadata={"help": "The output directory where the model predictions and checkpoints will be written."},
    )
    overwrite_output_dir: bool = field(
        default=False,
        metadata={
            "help": (
                "Overwrite the content of the output directory. "
                "Use this to continue training if output_dir points to a checkpoint directory."
            )
        },
    )

    do_train: bool = field(default=False, metadata={"help": "Whether to run training."})
    do_eval: bool = field(default=False, metadata={"help": "Whether to run eval on the dev set."})
    do_predict: bool = field(default=False, metadata={"help": "Whether to run predictions on the test set."})
    do_export: bool = field(default=False, metadata={"help": "Whether to export infernece model."})
    evaluation_strategy: IntervalStrategy = field(
        default="no",
        metadata={"help": "The evaluation strategy to use."},
    )
    prediction_loss_only: bool = field(
        default=False,
        metadata={"help": "When performing evaluation and predictions, only returns the loss."},
    )

    per_device_train_batch_size: int = field(default=8, metadata={"help": "Batch size per GPU core/CPU for training."})
    per_device_eval_batch_size: int = field(
        default=8, metadata={"help": "Batch size per GPU core/CPU for evaluation."}
    )

    gradient_accumulation_steps: int = field(
        default=1,
        metadata={"help": "Number of updates steps to accumulate before performing a backward/update pass."},
    )
    eval_accumulation_steps: Optional[int] = field(
        default=None,
        metadata={"help": "Number of predictions steps to accumulate before moving the tensors to the CPU."},
    )

    learning_rate: float = field(default=5e-5, metadata={"help": "The initial learning rate for AdamW."})
    weight_decay: float = field(default=0.0, metadata={"help": "Weight decay for AdamW if we apply some."})
    adam_beta1: float = field(default=0.9, metadata={"help": "Beta1 for AdamW optimizer"})
    adam_beta2: float = field(default=0.999, metadata={"help": "Beta2 for AdamW optimizer"})
    adam_epsilon: float = field(default=1e-8, metadata={"help": "Epsilon for AdamW optimizer."})
    max_grad_norm: float = field(default=1.0, metadata={"help": "Max gradient norm."})

    num_train_epochs: float = field(default=1.0, metadata={"help": "Total number of training epochs to perform."})
    max_steps: int = field(
        default=-1,
        metadata={"help": "If > 0: set total number of training steps to perform. Override num_train_epochs."},
    )
    lr_scheduler_type: str = field(
        default="linear",
        metadata={"help": "The scheduler type to use. suppor linear, cosine, constant, constant_with_warmup"},
    )
    warmup_ratio: float = field(
        default=0.0, metadata={"help": "Linear warmup over warmup_ratio fraction of total steps."}
    )
    warmup_steps: int = field(default=0, metadata={"help": "Linear warmup over warmup_steps."})
    num_cycles: float = field(default=0.5, metadata={"help": "The number of waves in the cosine scheduler."})
    lr_end: float = field(default=1e-7, metadata={"help": "The end LR in the polynomial scheduler."})
    power: float = field(default=1.0, metadata={"help": "The power factor in the polynomial scheduler."})

    log_on_each_node: bool = field(
        default=True,
        metadata={
            "help": "When doing a multinode distributed training, whether to log once per node or just once on the main node."
        },
    )
    logging_dir: Optional[str] = field(default=None, metadata={"help": "VisualDL log dir."})
    logging_strategy: IntervalStrategy = field(
        default="steps",
        metadata={"help": "The logging strategy to use."},
    )
    logging_first_step: bool = field(default=False, metadata={"help": "Log the first global_step"})
    logging_steps: int = field(default=500, metadata={"help": "Log every X updates steps."})

    save_strategy: IntervalStrategy = field(
        default="steps",
        metadata={"help": "The checkpoint save strategy to use."},
    )
    save_steps: int = field(default=500, metadata={"help": "Save checkpoint every X updates steps."})
    save_total_limit: Optional[int] = field(
        default=None,
        metadata={
            "help": (
                "Limit the total amount of checkpoints. "
                "Deletes the older checkpoints in the output_dir. Default is unlimited checkpoints"
            )
        },
    )
    save_on_each_node: bool = field(
        default=False,
        metadata={
            "help": "When doing multi-node distributed training, whether to save models and checkpoints on each node, or only on the main one"
        },
    )
    no_cuda: bool = field(default=False, metadata={"help": "Do not use CUDA even when it is available"})
    seed: int = field(default=42, metadata={"help": "Random seed that will be set at the beginning of training."})

    bf16: bool = field(
        default=False,
        metadata={
            "help": (
                "Whether to use bf16 (mixed) precision instead of 32-bit. Requires Ampere or higher NVIDIA"
                " architecture or using CPU (no_cuda). This is an experimental API and it may change."
            )
        },
    )
    fp16: bool = field(
        default=False,
        metadata={"help": "Whether to use fp16 (mixed) precision instead of 32-bit"},
    )
    fp16_opt_level: str = field(
        default="O1",
        metadata={
            "help": (
                "For fp16: AMP optimization level selected in ['O0', 'O1', and 'O2']. "
                "See details at https://www.paddlepaddle.org.cn/documentation/docs/zh/develop/api/paddle/amp/auto_cast_cn.html"
            )
        },
    )
    amp_master_grad: bool = field(
        default=False,
        metadata={
            "help": "amp_master_grad (bool, optional) – For amp opt level=’O2’, whether to use float32 weight gradients "
            " for calculations such as gradient clipping, weight decay, and weight updates. If master_grad is enabled,"
            " the weight gradients will be float32 dtype after the backpropagation. Default is False, there is only float16 weight gradients."
            "Note: only support model parallel and pipeline parallel for now !!!"
        },
    )
    bf16_full_eval: bool = field(
        default=False,
        metadata={
            "help": (
                "Whether to use full bfloat16 evaluation instead of 32-bit. This is an experimental API and it may"
                " change."
            )
        },
    )
    fp16_full_eval: bool = field(
        default=False,
        metadata={"help": "Whether to use full float16 evaluation instead of 32-bit"},
    )

    amp_custom_black_list: Optional[List[str]] = field(
        default=None,
        metadata={
            "help": "The set of ops that support fp16/bf16 calculation and are considered numerically-dangerous and whose effects may also be observed in downstream ops."
        },
    )
    amp_custom_white_list: Optional[List[str]] = field(
        default=None,
        metadata={
            "help": "The the set of ops that support fp16/bf16 calculation and are considered numerically-safe and performance-critical. These ops will be converted to fp16/bf16."
        },
    )

    sharding: str = field(
        default="",
        metadata={
            "help": (
                "Whether or not to use Paddle Sharding Data Parallel training (in distributed training"
                " only). The base option should be `stage1`, `stage2` or `stage3` and you can add"
                " CPU-offload to `stage2` or `stage3` like this: stage2 offload` or `stage3"
                " offload`. "
            )
        },
    )
    sharding_degree: int = field(  # Alias for sharding_parallel_degree
        default=-1,
        metadata={"help": ("@deprecated Please use sharding_parallel_degree. ")},
    )
    sharding_parallel_degree: int = field(
        default=-1,
        metadata={
            "help": (
                "Sharding parameter in certain cards group. For example, aussume we use 2 machines each with 8 cards, "
                "then set sharding_degree=8, sharding will only communication inside machine. "
                "default -1 means sharding parameters between all workers."
            )
        },
    )
    save_sharded_model: bool = field(
        default=False,
        metadata={
            "help": (
                "When use sharding stage1 and set save_sharded_model True, each shanding rank only save part of the model. It reduce time to save the model."
            )
        },
    )

    load_sharded_model: bool = field(
        default=False,
        metadata={
            "help": (
                "When use sharding stage1 and set load_sharded_model True, it means loading the sharded model. The sharded model is saved when we set save_sharded_model True."
            )
        },
    )
    tensor_parallel_degree: int = field(
        default=-1,
        metadata={
            "help": (
                "Tensor parallelism is parallel technique proposed in (https://arxiv.org/pdf/2104.04473.pdf see 2.3 Tensor Model Parallelism). "
                "This techique splits one transformer layer into multi-cards (For examples, tensor_parallel_degree=4, will split a layer to 4-parts) "
                "tensor_parallel_degree means split the transformer layer to how many parts."
                "default -1 for not use tensor parallel,  Suggest tensor_parallel_degree<=8 for better proformance."
                "Note, this need model support in source code, currently GPT/BLOOM/LLAMA/BLOOM/CLM/CHATGLM is supported. "
            )
        },
    )
    pipeline_parallel_degree: int = field(
        default=-1,
        metadata={
            "help": (
                "Pipeline parallelism is parallel technique proposed in (https://arxiv.org/pdf/2104.04473.pdf see 2.2 Pipeline Model Parallelism). "
                "Pipeline parallelism assigns multi-transformer layers to different cards, the micro batch data stream passed between cards like pipelines."
                "pipeline_parallel_degree means split all transformer layers to how many stages."
                "default -1 for not use pipeline parallel."
                "Note. this need model support in source code, see llama modeling_pp.py file"
            )
        },
    )
    sep_parallel_degree: int = field(
        default=-1,
        metadata={
            "help": (
                "The paddle sequence parallel strategy. It can reduce the GPU memory of activation to 1/sep, and it is orthogonal to "
                "data parallel, sharding stage1, tensor parallel and pipeline parallel strategy. "
            )
        },
    )
    data_parallel_config: str = field(
        default="",
        metadata={
            "help": (
                "Some additional configs which affect data parallel performance, we provide some option to config it."
                "following config is support:\n"
                "enable_allreduce_avg_in_gradinent_scale, it replace `allreduce_sum + scale` pattern with `allreduce_avg` when scale gradient in data_parallel, which improve the performance. ONLY supported for auto mode now. \n"
                "gradient_sync_after_accumulate, move gradient sync operations from backward into optimizer step when gradient accumulate enabling, which reduce the sync times to improve performance, but will increase the memory usage. ONLY supported for auto mode now. \n"
            )
        },
    )
    tensor_parallel_config: str = field(
        default="",
        metadata={
            "help": (
                "Some additional configs which affect model parallel performance, we provide some option to config it."
                "following config is support:\n"
                "enable_mp_async_allreduce, it supports all_reduce(dx) overlap with matmul(dw) in ColumnParallelLinear backward when it set True, which can accelerate model parallel performance. \n"
                "enable_mp_skip_c_identity, it supports skip c_identity in ColumnParallelLinear and RowParallelLinear. It only works when set mp_async_allreduce is True. It can accelerate model parallel further.\n"
                "enable_mp_fused_linear_param_grad_add, it supports fused_linear_param_grad_add in ColumnParallelLinear (cuda >= 11.6). It only works when mp_async_allreduce is true.  It can accelerate model parallel further.\n"
                "enable_delay_scale_loss, accumulate gradients util optimizer step, all gradients div by accumute step. instead of div accumute step on loss directly.\n"
            )
        },
    )
    pipeline_parallel_config: str = field(
        default="",
        metadata={
            "help": (
                "Some additional config it highly affect the useage of pipeline parallel, we provide some option to config it."
                "following config is support:\n"
                "disable_p2p_cache_shape, if you max sequence length is varying, please set disable_p2p_cache_shape. \n"
                "disable_partial_send_recv, optmize send speed for tensor parallel.\n"
                "enable_delay_scale_loss, accumulate gradients util optimizer step, all gradients div by inner pipeline accumute step. instead of div accumute step on loss directly.\n"
                "enable_dp_comm_overlap, fuse data parallel gradient communication. \n"
                "enable_sharding_comm_overlap, fuse sharding stage 1 parallel gradient communication. \n"
                "enable_overlap_p2p_comm, overlap p2p communication with computation. \n"
                "enable_clear_every_step_cache, clear every step cache for pipeline parallel. \n"
                "disable_batch_p2p_comm, disable batched send/recv in pipeline parallel mode. \n"
            )
        },
    )
    sharding_parallel_config: str = field(
        default="",
        metadata={
            "help": (
                "Some additional config it highly affect the useage of sharding parallel, we provide some option to config it."
                "following config is support: \n"
                "enable_stage1_tensor_fusion, fuse small tensors into big tensor chunks to accelerate communications, may increase memory occupation\n"
                "enable_stage1_overlap, fuse small tensors into big tensor chunks to accelerate communications and do communication overlap with backward computation, may harm the backward speed\n"
                "disable_stage1_reduce_avg, replace reduce_avg with original reduce_sum+scale in stage1, which can be used for accuracy verification.\n"
                "enable_stage2_overlap, overlap stage2 NCCL communication with computation. There are some constraints for the overlap, such as the logging_step should be bigger than 1 for broadcast overlap and no other sync could be called during the training for broadcast overlap"
            )
        },
    )
    hybrid_parallel_topo_order: str = field(
        default=None,
        metadata={
            "help": (
                "In hybrid parallelism, the order of communication groups may affect efficiency.\n"
                "Following options are supported:\n"
                "- pp_first. the topo order is dp, pp, sharding, mp \n"
                "- sharding_first. the topo order is dp, sharding, pp, mp \n"
                "Defalut is None, for pp_first"
            )
        },
    )
    recompute: bool = field(
        default=False,
        metadata={
            "help": "Recompute the forward pass to calculate gradients. Used for saving memory. "
            "Only support for networks with transformer blocks."
        },
    )

    scale_loss: float = field(default=2**15, metadata={"help": "The value of initial scale_loss for fp16."})

    minimum_eval_times: int = field(
        default=None,
        metadata={
            "help": "If under eval_steps, the valid time is less then minimum_eval_times, the config of override eval_steps."
        },
    )

    local_rank: int = field(default=-1, metadata={"help": "For distributed training: local_rank"})

    dataloader_drop_last: bool = field(
        default=False, metadata={"help": "Drop the last incomplete batch if it is not divisible by the batch size."}
    )
    eval_steps: int = field(default=None, metadata={"help": "Run an evaluation every X steps."})
    max_evaluate_steps: int = field(
        default=-1, metadata={"help": "If set to a positive number, the total number of evaluation steps to perform."}
    )
    dataloader_num_workers: int = field(
        default=0,
        metadata={
            "help": "Number of subprocesses to use for data loading. 0 means that the data will be loaded in the main process."
        },
    )

    past_index: int = field(
        default=-1,
        metadata={"help": "If >=0, uses the corresponding part of the output as the past state for next step."},
    )

    run_name: Optional[str] = field(default=None, metadata={"help": "An optional descriptor for the run."})

    device: Optional[str] = field(default="gpu", metadata={"help": "select cpu, gpu, xpu, npu devices."})

    disable_tqdm: Optional[bool] = field(
        default=None, metadata={"help": "Whether or not to disable the tqdm progress bars."}
    )

    remove_unused_columns: Optional[bool] = field(
        default=True, metadata={"help": "Remove columns not required by the model when using an nlp.Dataset."}
    )

    label_names: Optional[List[str]] = field(
        default=None, metadata={"help": "The list of keys in your dictionary of inputs that correspond to the labels."}
    )

    load_best_model_at_end: Optional[bool] = field(
        default=False,
        metadata={"help": "Whether or not to load the best model found during training at the end of training."},
    )
    metric_for_best_model: Optional[str] = field(
        default=None, metadata={"help": "The metric to use to compare two different models."}
    )
    greater_is_better: Optional[bool] = field(
        default=None, metadata={"help": "Whether the `metric_for_best_model` should be maximized or not."}
    )
    ignore_data_skip: bool = field(
        default=False,
        metadata={
            "help": "When resuming training, whether or not to skip the first epochs and batches to get to the same training data."
        },
    )
    optim: str = field(
        default="adamw",
        metadata={"help": "The optimizer to use."},
    )
    report_to: Optional[List[str]] = field(
        default=None, metadata={"help": "The list of integrations to report the results and logs to."}
    )
    wandb_api_key: Optional[str] = field(
        default=None,
        metadata={"help": "Weights & Biases (WandB) API key(s) for authentication with the WandB service."},
    )
    resume_from_checkpoint: Optional[str] = field(
        default=None,
        metadata={"help": "The path to a folder with a valid checkpoint for your model."},
    )
    skip_memory_metrics: bool = field(
        default=True, metadata={"help": "Whether or not to skip adding of memory profiler reports to metrics."}
    )
    flatten_param_grads: Optional[bool] = field(
        default=False,
        metadata={"help": "Whether use flatten_param_grads method in optimizer, only used on NPU devices."},
    )
    lazy_data_processing: Optional[bool] = field(
        default=True,
        metadata={"help": "Whether use lazy data processing."},
    )
    skip_profile_timer: Optional[bool] = field(
        default=True,
        metadata={"help": "enable framework timer, will output timeline informatoin in logging and visualdl."},
    )
    distributed_dataloader: Optional[bool] = field(
        default=False, metadata={"help": "Whether to use distributed dataloader."}
    )
    unified_checkpoint: Optional[bool] = field(
        default=False,
        metadata={"help": "Whether to unify hybrid parallel checkpoint."},
    )
    to_static: Optional[bool] = field(
        default=False,
        metadata={"help": ("Whether to train model under static mode by jit.to_static or distributed.to_static.")},
    )
    unified_checkpoint_config: Optional[str] = field(
        default="",
        metadata={
            "help": (
                "Configs to unify hybrid parallel checkpoint.\n"
                "Following options are supports:\n"
                "- skip_save_model_weight: do not save model weights when the masters weight exist\n"
                "- master_weight_compatible: 1. if the master weights exist, only load when needed\n"
                "                            2. if master weights does not exist, convert model weights to master weights when needed\n"
                "- async_save: enable asynchronous saving checkpoints to disk\n"
                "- enable_all_options: enable all optimization configurations\n"
            )
        },
    )
    ignore_load_lr_and_optim: Optional[bool] = field(
        default=False,
        metadata={"help": "whether to ignore load optimizer and scheduler."},
    )
    ignore_save_lr_and_optim: Optional[bool] = field(
        default=False,
        metadata={"help": "whether to ignore save optimizer and scheduler."},
    )
    force_reshard_pp: Optional[bool] = field(
        default=False,
        metadata={"help": "reshard pp even if pp degree in the model and pp degree in script match"},
    )
    enable_auto_parallel: Optional[bool] = field(
        default=False,
        metadata={"help": "whether to run distributed training in auto parallel mode"},
    )
    use_expert_parallel: Optional[bool] = field(
        default=False,
        metadata={"help": "Enable MoE (Mixture of Experts) expert parallel training"},
    )

    def __post_init__(self):
        env_local_rank = int(os.environ.get("PADDLE_RANK_IN_NODE", -1))
        if env_local_rank != -1 and env_local_rank != self.local_rank and paddle.distributed.get_world_size() > 1:
            self.local_rank = env_local_rank

        # NOTE(gongenlei): new add, disable sharding when we have only single gpu
        if paddle.distributed.get_world_size() <= 1:
            self.sharding = ""
            self.sharding_degree = -1
            self.sharding_parallel_degree = -1
            self.tensor_parallel_degree = -1
            self.pipeline_parallel_degree = -1

        # convert to int
        self.log_level = -1
        self.log_level_replica = -1

        # expand paths, if not os.makedirs("~/bar") will make directory
        # in the current directory instead of the actual home
        if self.output_dir is not None:
            self.output_dir = os.path.expanduser(self.output_dir)
        if self.logging_dir is None and self.output_dir is not None:
            self.logging_dir = os.path.join(self.output_dir, default_logdir())
        if self.logging_dir is not None:
            self.logging_dir = os.path.expanduser(self.logging_dir)

        if self.disable_tqdm is None:
            self.disable_tqdm = False  # logger.getEffectiveLevel() > logging.WARN

        self.evaluation_strategy = IntervalStrategy(self.evaluation_strategy)
        self.logging_strategy = IntervalStrategy(self.logging_strategy)
        self.save_strategy = IntervalStrategy(self.save_strategy)

        self.lr_scheduler_type = SchedulerType(self.lr_scheduler_type)
        if self.do_eval is False and self.evaluation_strategy != IntervalStrategy.NO:
            self.do_eval = True

        if self.do_eval and self.evaluation_strategy == IntervalStrategy.NO:
            logger.warning(
                "evaluation_strategy reset to IntervalStrategy.STEPS for do_eval is True. you can also set evaluation_strategy='epoch'."
            )
            self.evaluation_strategy = IntervalStrategy.STEPS

        # eval_steps has to be defined and non-zero, fallbacks to logging_steps if the latter is non-zero
        if self.evaluation_strategy == IntervalStrategy.STEPS and (self.eval_steps is None or self.eval_steps == 0):
            if self.logging_steps > 0:
                logger.info(f"using `logging_steps` to initialize `eval_steps` to {self.logging_steps}")
                self.eval_steps = self.logging_steps
            else:
                raise ValueError(
                    f"evaluation strategy {self.evaluation_strategy} requires either non-zero --eval_steps or --logging_steps"
                )

        # logging_steps must be non-zero for logging_strategy that is other than 'no'
        if self.logging_strategy == IntervalStrategy.STEPS and self.logging_steps == 0:
            raise ValueError(f"logging strategy {self.logging_strategy} requires non-zero --logging_steps")

        # Sanity checks for load_best_model_at_end: we require save and eval strategies to be compatible.
        if self.load_best_model_at_end:
            if self.evaluation_strategy != self.save_strategy:
                raise ValueError(
                    "--load_best_model_at_end requires the save and eval strategy to match, but found\n- Evaluation "
                    f"strategy: {self.evaluation_strategy}\n- Save strategy: {self.save_strategy}"
                )
            if self.evaluation_strategy == IntervalStrategy.STEPS and self.save_steps % self.eval_steps != 0:
                raise ValueError(
                    "--load_best_model_at_end requires the saving steps to be a round multiple of the evaluation "
                    f"steps, but found {self.save_steps}, which is not a round multiple of {self.eval_steps}."
                )

        if self.load_best_model_at_end and self.metric_for_best_model is None:
            self.metric_for_best_model = "loss"
        if self.greater_is_better is None and self.metric_for_best_model is not None:
            self.greater_is_better = self.metric_for_best_model not in ["loss", "eval_loss"]
        if self.run_name is None:
            self.run_name = self.output_dir

        if self.fp16 and self.bf16:
            raise ValueError("At most one of fp16 and bf16 can be True, but not both")

        if self.fp16_full_eval and self.bf16_full_eval:
            raise ValueError("At most one of fp16 and bf16 can be True for full eval, but not both")

        self.optim = OptimizerNames(self.optim)

        self.use_hybrid_parallel = False

        if isinstance(self.sharding, bool):
            self.sharding = "stage1" if self.sharding else ""
        if isinstance(self.sharding, str):
            self.sharding = [ShardingOption(s) for s in self.sharding.split()]
        if self.sharding == [ShardingOption.OFFLOAD]:
            raise ValueError(
                "`--sharding offload` can't work on its own. It needs to be added to `--sharding stage2` or "
                '`--sharding stage3`. For example, `--sharding "stage2 offload"`.'
            )
        elif len(self.sharding) > (ShardingOption.OFFLOAD in self.sharding) + 1:
            raise ValueError("`--sharding` recived too many arguments.")

        if self.sharding_degree > 0:
            warnings.warn("`sharding_degree` is deprecated, please use `sharding_parallel_degree`")
            self.sharding_parallel_degree = max(self.sharding_degree, self.sharding_parallel_degree)

        delattr(self, "sharding_degree")

        if len(self.sharding) == 0 and self.sharding_parallel_degree > 0:
            warnings.warn("`--sharding_parallel_degree` is useful only when `--sharding` is specified.")

        world_size = paddle.distributed.get_world_size()

        if world_size > 1:
            tensor_parallel_degree = max(self.tensor_parallel_degree, 1)
            sep_parallel_degree = max(self.sep_parallel_degree, 1)
            pipeline_parallel_degree = max(self.pipeline_parallel_degree, 1)

            assert (
                world_size % (self.tensor_parallel_degree * self.pipeline_parallel_degree) == 0
            ), f"Total world_size:{world_size} shoule be devided by tensor_parallel_degree: {self.tensor_parallel_degree} and pipeline_parallel_degree: {self.pipeline_parallel_degree}."

            if self.sharding_parallel_degree == -1:
                if len(self.sharding) > 0:
                    self.sharding_parallel_degree = world_size // (
                        tensor_parallel_degree * sep_parallel_degree * pipeline_parallel_degree
                    )

            sharding_parallel_degree = max(self.sharding_parallel_degree, 1)
            if sharding_parallel_degree == 1 and len(self.sharding) > 0:
                logger.warning("sharding_parallel_degree=1 means no sharding, please set sharding to empty!")
                self.sharding = []

            self.data_parallel_degree = world_size // (
                sharding_parallel_degree * tensor_parallel_degree * sep_parallel_degree * pipeline_parallel_degree
            )

            if (
                sharding_parallel_degree > 1
                or tensor_parallel_degree > 1
                or pipeline_parallel_degree > 1
                or self.sep_parallel_degree > 1
            ):
                self.use_hybrid_parallel = True
                self.sharding_parallel_degree = sharding_parallel_degree
                self.tensor_parallel_degree = tensor_parallel_degree
                self.pipeline_parallel_degree = pipeline_parallel_degree
                self.sep_parallel_degree = sep_parallel_degree

            if not self.use_hybrid_parallel:
                self.sharding = []
                self.sharding_parallel_degree = -1
                self.tensor_parallel_degree = -1
                self.pipeline_parallel_degree = -1
                self.sep_parallel_degree = -1

        if self.hybrid_parallel_topo_order is None:
            self.hybrid_parallel_topo_order = "pp_first"
        assert self.hybrid_parallel_topo_order in ["pp_first", "sharding_first"]

        if self.use_hybrid_parallel and self.enable_auto_parallel:
            self.use_hybrid_parallel = False

        if self.to_static:
            assert world_size == 1 or self.enable_auto_parallel, (
                "It's not supported for training in static mode except the following cases : "
                "1. world_size == 1, which means single-card training while no parallelism is used; "
                "2. enable_auto_parallel is set to True, which means the training will be executed in static mode of auto parallel."
            )

        if self.distributed_dataloader and not (self.tensor_parallel_degree > 1 or self.pipeline_parallel_degree > 1):
            warnings.warn("We set `distributed_dataloader` to False if tp_degree <= 1 and pp_degree <= 1")
            self.distributed_dataloader = False

        if self.amp_master_grad:
            if not (self.bf16 or self.fp16):
                logger.warning("set amp_master_grad to false since amp is disabled.")
                self.amp_master_grad = False

        # use_hybrid_parallel
        if self.use_hybrid_parallel:

            if ShardingOption.OFFLOAD in self.sharding:
                warnings.warn("`offload` is not supported NOW!")

            if self.pipeline_parallel_degree > 1:
                if ShardingOption.FULL_SHARD in self.sharding or ShardingOption.SHARD_GRAD_OP in self.sharding:
                    raise ValueError(
                        "pipeline parallel is not compatible for sharding stage2 or stage3, please using sharding stage1"
                    )

            # TODO use paddle.distributed.is_initialized() after paddle 2.4rc
            if not paddle.distributed.parallel.parallel_helper._is_parallel_ctx_initialized():
                strategy = fleet.DistributedStrategy()
                assert self.data_parallel_config == "", "data_parallle_config is not supported in hybrid parallel"
                if self.pipeline_parallel_degree > 1:
                    pipeline_parallel_config = set(self.pipeline_parallel_config.split(" "))
                    for x in pipeline_parallel_config:
                        if len(x) > 0:
                            if x not in [
                                "disable_p2p_cache_shape",
                                "disable_partial_send_recv",
                                "enable_delay_scale_loss",
                                "enable_dp_comm_overlap",
                                "enable_sharding_comm_overlap",
                                "enable_timer",
                                "enable_release_grads",
                                "enable_dp_comm_overlap",
                                "enable_clear_every_step_cache",
                                "enable_overlap_p2p_comm",
                                "disable_batch_p2p_comm",
                            ]:
                                raise ValueError(
                                    f"Found unknown pipeline mode config {x}, accpet config is disable_p2p_cache_shape, disable_partial_send_recv."
                                )

                    strategy.pipeline_configs = {
                        "accumulate_steps": self.gradient_accumulation_steps,
                        "micro_batch_size": self.per_device_train_batch_size,
                        "enable_partial_send_recv": "disable_partial_send_recv" not in pipeline_parallel_config,
                        "p2p_cache_shape": False if "disable_p2p_cache_shape" in pipeline_parallel_config else True,
                        # "delay_scale_loss": True, Fix ME
                    }
                    logger.info(f"PP configs:{strategy.pipeline_configs}, use master_grad: {self.amp_master_grad}")

                    using_comm_overlap = (
                        "enable_sharding_comm_overlap" in pipeline_parallel_config
                        or "enable_dp_comm_overlap" in pipeline_parallel_config
                    )
                    enable_dp_comm_overlap = using_comm_overlap and self.data_parallel_degree > 1
                    enable_sharding_comm_overlap = using_comm_overlap and self.sharding_parallel_degree > 1
                    assert not (
                        enable_dp_comm_overlap and enable_sharding_comm_overlap
                    ), "dp_comm_overlap and sharding_comm_overlap cannot be enabled at the same time"

                    if enable_sharding_comm_overlap and not self.amp_master_grad:
                        raise ValueError(
                            "If `enable_sharding_comm_overlap` in pipeline_parallel_configs, `amp_master_grad` must be True."
                        )

                    dygraph_pp_configs = {
                        "delay_scale_loss": True if "enable_delay_scale_loss" in pipeline_parallel_config else False,
                        "dp_comm_overlap": enable_dp_comm_overlap,
                        "sharding_comm_overlap": enable_sharding_comm_overlap,
                        "enable_timer": "enable_timer" in pipeline_parallel_config,
                        "release_gradients": "enable_release_grads" in pipeline_parallel_config,
                        "overlap_p2p_comm": "enable_overlap_p2p_comm" in pipeline_parallel_config,
                        "clear_every_step_cache": "enable_clear_every_step_cache" in pipeline_parallel_config,
                        "use_batch_p2p_comm": "disable_batch_p2p_comm" not in pipeline_parallel_config,
                    }
                    if dygraph_pp_configs["dp_comm_overlap"]:
                        raise ValueError("overlap has accuracy issue")  # TODO: fix `overalap` + `delay_scale` issue

                    if self.do_eval:
                        if (
                            self.per_device_train_batch_size * self.gradient_accumulation_steps
                            != self.per_device_eval_batch_size
                        ):
                            logger.warning(
                                "In pipeline model, the evaluation also shares same setting with training. "
                                "We will enforce that per_device_eval_batch_size=per_device_train_batch_size * gradient_accumulation_steps."
                            )

                            self.per_device_eval_batch_size = (
                                self.per_device_train_batch_size * self.gradient_accumulation_steps
                            )

                if self.tensor_parallel_degree > 1:
                    strategy.tensor_parallel_configs = {"tensor_init_seed": self.seed}

                    if " " in self.tensor_parallel_config:
                        mp_config = set(self.tensor_parallel_config.split(" "))
                    else:
                        mp_config = set(self.tensor_parallel_config.split(","))

                    for x in mp_config:
                        if len(x) > 0:
                            if x not in [
                                "enable_mp_async_allreduce",
                                "enable_mp_skip_c_identity",
                                "enable_mp_fused_linear_param_grad_add",
                                "enable_delay_scale_loss",
                            ]:
                                raise ValueError(
                                    f"Found unknown tensor parallell config {x}, "
                                    f"accept config is enable_mp_async_allreduce, enable_mp_skip_c_identity and enable_mp_fused_linear_param_grad_add"
                                )
                    try:
                        if "enable_mp_async_allreduce" in mp_config:
                            strategy.hybrid_configs["mp_configs"].mp_async_allreduce = True
                            if "enable_mp_skip_c_identity" in mp_config:
                                strategy.hybrid_configs["mp_configs"].mp_skip_c_identity = True
                            if "enable_mp_fused_linear_param_grad_add" in mp_config:
                                strategy.hybrid_configs["mp_configs"].mp_fused_linear_param_grad_add = True
                        else:
                            if "enable_mp_skip_c_identity" in mp_config:
                                warnings.warn(
                                    "enable_mp_skip_c_identity only works with enable_mp_async_allreduce. It will not work."
                                )
                            if "enable_mp_fused_linear_param_grad_add" in mp_config:
                                warnings.warn(
                                    "enable_mp_fused_linear_param_grad_add only works with enable_mp_async_allreduce. It will not work."
                                )
                    except:
                        warnings.warn(
                            "The enable_mp_async_allreduce, enable_mp_skip_c_identity and enable_mp_fused_linear_param_grad_add are not supported "
                            "by current version of Paddle. Please try latest develop Paddle."
                        )

                def is_segment_parallel_supported():
                    import inspect

                    members = [name for (name, date) in inspect.getmembers(fleet.HybridCommunicateGroup)]
                    support_sep = "get_sep_parallel_world_size" in members
                    if not support_sep:
                        logger.warning("segment parallel is not supported!!!, Ignore it.")
                    return support_sep

                if self.hybrid_parallel_topo_order == "pp_first":
                    if is_segment_parallel_supported():
                        order = ["dp", "pp", "sharding", "sep", "mp"]
                    else:
                        order = ["dp", "pp", "sharding", "mp"]
                if self.hybrid_parallel_topo_order == "sharding_first":
                    if is_segment_parallel_supported():
                        order = ["dp", "sharding", "pp", "sep", "mp"]
                    else:
                        order = ["dp", "sharding", "pp", "mp"]
                if self.use_expert_parallel:
                    order = order[1:-1] + ["dp", "mp"]

                if is_segment_parallel_supported():
                    hybrid_configs = {
                        "dp_degree": self.data_parallel_degree,
                        "mp_degree": self.tensor_parallel_degree,
                        "pp_degree": self.pipeline_parallel_degree,
                        "sharding_degree": self.sharding_parallel_degree,
                        "sep_degree": self.sep_parallel_degree,
                        "order": order,
                    }
                else:
                    hybrid_configs = {
                        "dp_degree": self.data_parallel_degree,
                        "mp_degree": self.tensor_parallel_degree,
                        "pp_degree": self.pipeline_parallel_degree,
                        "sharding_degree": self.sharding_parallel_degree,
                        "order": order,
                    }

                if self.pipeline_parallel_degree > 1:
                    hybrid_configs["pp_configs"] = dygraph_pp_configs
                    logger.info(f"using pipeline configs:{dygraph_pp_configs}")

                # setter once https://github.com/PaddlePaddle/Paddle/blob/b7295120b0e78b293cd7ae29706e21769d06a3cc/python/paddle/distributed/fleet/base/distributed_strategy.py#L1692
                strategy.hybrid_configs = hybrid_configs

                if self.sharding_parallel_degree > 1:
                    sharding_parallel_config = set(self.sharding_parallel_config.split(" "))
                    for x in sharding_parallel_config:
                        if len(x) > 0:
                            if x not in [
                                "enable_stage1_tensor_fusion",
                                "enable_stage1_overlap",
                                "enable_stage2_overlap",
                                "split_param",
                                "disable_stage1_reduce_avg",
                            ]:
                                raise ValueError(
                                    f"Found unknown pipeline mode config {x}, "
                                    f"accpet config is enable_stage1_tensor_fusion, enable_stage1_overlap, enable_stage2_overlap."
                                )
                    if "disable_stage1_reduce_avg" in sharding_parallel_config:
                        assert self.sharding == [
                            ShardingOption.SHARD_OP
                        ], "Only sharding stage1 supports to disable reduce_avg strategy."
                        try:
                            strategy.hybrid_configs["sharding_configs"].use_reduce_avg = False
                        except:
                            warnings.warn(
                                "The reduce_avg strategy is not supported by current version of Paddle so you don't need to disable it. The nccl comm in sharding still use reduce_sum and scale of gradients."
                            )

                    try:
                        if "split_param" in sharding_parallel_config:
                            strategy.hybrid_configs["sharding_configs"].split_param = True

                        if self.pipeline_parallel_degree == 1:
                            strategy.hybrid_configs["sharding_configs"].tensor_fusion = (
                                True if "enable_stage1_tensor_fusion" in sharding_parallel_config else False
                            )
                            if "enable_stage1_overlap" in sharding_parallel_config:
                                strategy.hybrid_configs["sharding_configs"].comm_overlap = True
                                strategy.hybrid_configs[
                                    "sharding_configs"
                                ].accumulate_steps = self.gradient_accumulation_steps

                        else:
                            warnings.warn(
                                "For pipeline parallel with sharding, the sharding overlap and tensor fusion "
                                "should be configured in pipeline_parallel_config."
                                '"enable_stage1_tensor_fusion" and "enable_stage1_overlap" in sharding_parallel_config will be ignored.'
                            )
                    except (KeyError, AttributeError):
                        warnings.warn(
                            "The enable_stage1_tensor_fusion or enable_stage1_overlap is not supported "
                            "by current version of Paddle. Please try latest develop Paddle."
                        )
                    if "enable_stage2_overlap" in sharding_parallel_config:
                        assert (
                            ShardingOption.SHARD_GRAD_OP in self.sharding
                        ), f"enable_stage2_overlap expects sharding=stage2, but got {self.sharding}."
                        assert self.logging_steps > 1, (
                            "The logging_steps should be greater than 1 for stage2 overlap, "
                            f"but got logging_steps={self.logging_steps}."
                        )
                fleet.init(is_collective=True, strategy=strategy)
                logger.info(strategy)

        elif self.enable_auto_parallel:
            self.tensor_parallel_degree = max(self.tensor_parallel_degree, 1)
            self.sep_parallel_degree = max(self.sep_parallel_degree, 1)
            self.pipeline_parallel_degree = max(self.pipeline_parallel_degree, 1)

            assert (
                world_size % (self.tensor_parallel_degree * self.pipeline_parallel_degree) == 0
            ), f"Total world_size:{world_size} shoule be devided by tensor_parallel_degree: {self.tensor_parallel_degree} and pipeline_parallel_degree: {self.pipeline_parallel_degree}."

            if self.sharding_parallel_degree == -1:
                if len(self.sharding) > 0:
                    self.sharding_parallel_degree = world_size // (
                        self.tensor_parallel_degree * self.sep_parallel_degree * self.pipeline_parallel_degree
                    )

            self.sharding_parallel_degree = max(self.sharding_parallel_degree, 1)
            if self.sharding_parallel_degree == 1 and len(self.sharding) > 0:
                logger.warning("sharding_parallel_degree=1 means no sharding, please set sharding to empty!")
                self.sharding = []

            self.data_parallel_degree = world_size // (
                self.sharding_parallel_degree
                * self.tensor_parallel_degree
                * self.sep_parallel_degree
                * self.pipeline_parallel_degree
            )

            if ShardingOption.OFFLOAD in self.sharding:
                warnings.warn("`offload` is not supported NOW!")

            strategy = fleet.auto.Strategy()
            if self.dataset_world_size > 1:
                data_parallel_config = set(self.data_parallel_config.split(" "))
                for x in data_parallel_config:
                    if len(x) > 0:
                        if x not in ["enable_allreduce_avg_in_gradinent_scale", "gradient_sync_after_accumulate"]:
                            raise ValueError(
                                f"Found unknown data parallel config {x}, accpet config is enable_allreduce_avg_in_gradinent_scale."
                            )
                if "enable_allreduce_avg_in_gradinent_scale" in data_parallel_config:
                    strategy.gradient_scale_using_allreduce_avg = True
                if "gradient_sync_after_accumulate" in data_parallel_config:
                    strategy.dp_optimization.gradient_sync_after_accumulate = True

            # navie-pp: pipeline_parallel_degree > 1 and gradient_accumulation_steps == 1
            if self.pipeline_parallel_degree > 1 and self.gradient_accumulation_steps > 1:
                pipeline_parallel_config = set(self.pipeline_parallel_config.split(" "))
                for x in pipeline_parallel_config:
                    if len(x) > 0:
                        if x not in [
                            "enable_send_recv_overlap",
                            # "disable_p2p_cache_shape",      # no need for auto_parallel
                            # "disable_partial_send_recv",    # no implemenation for auto_parallel
                            # "enable_delay_scale_loss",      # default True in auto_parallel, non-configurable
                            # "enable_dp_comm_overlap",       # no implemenation for auto_parallel
                            # "enable_sharding_comm_overlap", # no implemenation for auto_parallel
                            # "enable_timer",                 # no implemenation for auto_parallel
                            # "disable_batch_p2p_comm",       # no implemenation for auto_parallel
                        ]:
                            raise ValueError(
                                f"Found unknown pipeline mode config {x}, accpet config is enable_send_recv_overlap."
                            )

                pipeline = strategy.pipeline
                pipeline.enable = True
                pipeline.enable_send_recv_overlap = "enable_send_recv_overlap" in pipeline_parallel_config
                pipeline.accumulate_steps = self.gradient_accumulation_steps
                pipeline.micro_batch_size = self.per_device_train_batch_size
                pipeline.schedule_mode = self.pipeline_schedule_mode

                logger.info(f"PP configs:{strategy.pipeline}, use master_grad: {self.amp_master_grad}")

                if self.do_eval:
                    if (
                        self.per_device_train_batch_size * self.gradient_accumulation_steps
                        != self.per_device_eval_batch_size
                    ):
                        logger.warning(
                            "In pipeline model, the evaluation also shares same setting with training. "
                            "We will enforce that per_device_eval_batch_size=per_device_train_batch_size * gradient_accumulation_steps."
                        )
                        self.per_device_eval_batch_size = (
                            self.per_device_train_batch_size * self.gradient_accumulation_steps
                        )

            elif self.gradient_accumulation_steps > 1:
                gradient_merge = strategy.gradient_merge
                gradient_merge.enable = True
                gradient_merge.k_steps = self.gradient_accumulation_steps
                gradient_merge.avg = True

            if self.tensor_parallel_degree > 1:
                mp_optimization = strategy.mp_optimization

                if " " in self.tensor_parallel_config:
                    mp_config = set(self.tensor_parallel_config.split(" "))
                else:
                    mp_config = set(self.tensor_parallel_config.split(","))

                for x in mp_config:
                    if len(x) > 0:
                        if x not in [
                            "enable_mp_async_allreduce",  # allreduce_matmul_grad_overlapping in auto_parallel
                            # "enable_mp_skip_c_identity",
                            # "enable_mp_fused_linear_param_grad_add",
                        ]:
                            raise ValueError(
                                f"Found unknown tensor parallell config {x}, "
                                f"accept config is enable_mp_async_allreduce, enable_mp_skip_c_identity and enable_mp_fused_linear_param_grad_add"
                            )
                try:
                    if "enable_mp_async_allreduce" in mp_config:
                        mp_optimization.allreduce_matmul_grad_overlapping = True
                except:
                    warnings.warn(
                        "The enable_mp_async_allreduce, enable_mp_skip_c_identity and enable_mp_fused_linear_param_grad_add are not supported "
                        "by current version of Paddle. Please try latest develop Paddle."
                    )

            if self.sharding_parallel_degree > 1:
                sharding = strategy.sharding
                sharding.enable = True
                sharding.degree = self.sharding_parallel_degree
                if ShardingOption.SHARD_OP in self.sharding:
                    sharding.stage = 1
                elif ShardingOption.SHARD_GRAD_OP in self.sharding:
                    sharding.stage = 2
                elif ShardingOption.FULL_SHARD in self.sharding:
                    sharding.stage = 3

                sharding_parallel_config = set(self.sharding_parallel_config.split(" "))
                for x in sharding_parallel_config:
                    if len(x) > 0:
                        if x not in [
                            "enable_stage1_tensor_fusion",
                            "enable_stage1_overlap",
                            "enable_stage2_overlap",
                        ]:
                            raise ValueError(
                                f"Found unknown pipeline mode config {x}, " f"accpet config is reduce_overlap."
                            )

                    if (
                        "enable_stage1_overlap" in sharding_parallel_config
                        or "enable_stage2_overlap" in sharding_parallel_config
                    ):
                        sharding.enable_overlap = True

                    if "enable_stage1_tensor_fusion" in sharding_parallel_config:
                        sharding.grad_bucket_size_numel = 210355872

            if self.bf16 or self.fp16:
                amp = strategy.amp
                amp.enable = True
                amp.dtype = "bfloat16" if self.bf16 else "float16"
                amp.level = self.fp16_opt_level.lower()
                amp.use_master_grad = self.amp_master_grad
                amp.init_loss_scaling = self.scale_loss
                amp.custom_black_list = self.amp_custom_black_list if self.amp_custom_black_list is not None else []
                amp.custom_white_list = self.amp_custom_white_list if self.amp_custom_white_list is not None else []

            if self.recompute:
                recompute = strategy.recompute
                recompute.enable = True
                recompute.sr = self.sr if self.sr is not None else 0
                recompute.refined_ops_patterns = []
                if self.refined_ops_patterns is not None:
                    for pattern in self.refined_ops_patterns:
                        recompute.refined_ops_patterns.append(eval(pattern))

            self.strategy = strategy
            if self.hybrid_parallel_topo_order == "pp_first":
                order = ["pp", "dp", "mp"]
                degree = [self.pipeline_parallel_degree, self.dataset_world_size, self.tensor_parallel_degree]
            elif self.hybrid_parallel_topo_order == "sharding_first":
                order = ["dp", "pp", "mp"]
                degree = [self.dataset_world_size, self.pipeline_parallel_degree, self.tensor_parallel_degree]
            mesh_dims = list(zip(order, degree))
            fleet.auto.create_mesh(mesh_dims)

            # init hcg for communication in trainer
            if self.hybrid_parallel_topo_order == "pp_first":
                order = ["pp", "dp", "sharding", "sep", "mp"]
            elif self.hybrid_parallel_topo_order == "sharding_first":
                order = ["dp", "sharding", "pp", "sep", "mp"]

            strategy = fleet.DistributedStrategy()
            strategy.hybrid_configs = {
                "dp_degree": self.dataset_world_size,
                "mp_degree": self.tensor_parallel_degree,
                "pp_degree": self.pipeline_parallel_degree,
                "order": order,
            }
            fleet.init(is_collective=True, strategy=strategy)

        else:
            if world_size > 1:
                if not paddle.distributed.parallel.parallel_helper._is_parallel_ctx_initialized():
                    if self.unified_checkpoint:
                        # DP use hybrid group
                        strategy = fleet.DistributedStrategy()
                        fleet.init(is_collective=True, strategy=strategy)
                    else:
                        paddle.distributed.init_parallel_env()

        if (
            self.unified_checkpoint
            and self.sharding_parallel_degree > 0
            and ShardingOption.FULL_SHARD in self.sharding
        ):
            logger.warning(
                "Unified checkpoint currently do not support sharding stage3, set `unified_checkpoint` to False."
            )
            self.unified_checkpoint = False

        if self.unified_checkpoint:
            if self.ignore_save_lr_and_optim:
                self.unified_checkpoint_config = ""
                logger.info("Setting unified_checkpoint_config to empty for using ignore_save_lr_and_optim.")
            else:
                unified_checkpoint_config = set(self.unified_checkpoint_config.split(" "))
                for x in unified_checkpoint_config:
                    if len(x) > 0:
                        if x not in [
                            "skip_save_model_weight",
                            "master_weight_compatible",
                            "async_save",
                            "enable_all_options",
                        ]:
                            raise ValueError(
                                f"Found unknown unified_checkpoint config {x}, accpet config is skip_save_model_weight, "
                                + "master_weight_compatible, async_save, enable_all_options."
                            )
                if "enable_all_options" in unified_checkpoint_config:
                    self.unified_checkpoint_config = [
                        "skip_save_model_weight",
                        "master_weight_compatible",
                        # "async_save",
                    ]
                else:
                    self.unified_checkpoint_config = self.unified_checkpoint_config.split(" ")

        if self.report_to is None:
            logger.info(
                "The default value for the training argument `--report_to` will change in v5 (from all installed "
                "integrations to none). In v5, you will need to use `--report_to all` to get the same behavior as "
                "now. You should start updating your code and make this info disappear :-)."
            )
            self.report_to = "visualdl"
        if self.report_to == "all" or self.report_to == ["all"]:
            # Import at runtime to avoid a circular import.
            from .integrations import get_available_reporting_integrations

            self.report_to = get_available_reporting_integrations()
        elif self.report_to == "none" or self.report_to == ["none"]:
            self.report_to = []
        elif not isinstance(self.report_to, list):
            self.report_to = [self.report_to]

        if self.warmup_ratio < 0 or self.warmup_ratio > 1:
            raise ValueError("warmup_ratio must lie in range [0,1]")
        elif self.warmup_ratio > 0 and self.warmup_steps > 0:
            logger.info(
                "Both warmup_ratio and warmup_steps given, warmup_steps will override any effect of warmup_ratio during training"
            )

        if self.flatten_param_grads and self.device != "npu":
            raise ValueError("flatten_param_grads can only be used on npu devices in temporary.")

        if self.world_size != paddle.distributed.get_world_size():
            raise ValueError(
                f"The local_ran: {self.local_rank} should be consistent with the world size: {paddle.distributed.get_world_size()}."
            )

    def __str__(self):
        self_as_dict = asdict(self)
        self_as_dict = {k: f"<{k.upper()}>" if k.endswith("_token") else v for k, v in self_as_dict.items()}

        attrs_as_str = [f"{k}={v},\n" for k, v in sorted(self_as_dict.items())]
        return f"{self.__class__.__name__}(\n{''.join(attrs_as_str)})"

    __repr__ = __str__

    @property
    def train_batch_size(self) -> int:
        """
        The actual batch size for training.
        """
        train_batch_size = self.per_device_train_batch_size
        return train_batch_size

    @property
    def eval_batch_size(self) -> int:
        """
        The actual batch size for evaluation.
        """
        eval_batch_size = self.per_device_eval_batch_size
        return eval_batch_size

    @property
    def current_device(self) -> "paddle.device":
        """
        The device used by this process.
        """
        return paddle.device.get_device()

    @property
    def world_size(self):
        """
        The number of processes used in parallel.
        """
        if self.local_rank != -1:
            return paddle.distributed.get_world_size()
        return 1

    @property
    def data_parallel_rank(self):
        if self.use_hybrid_parallel:
            hcg = fleet.get_hybrid_communicate_group()
            dp_group = hcg.get_data_parallel_group()
            if dp_group.rank == -1:
                return 0
            return dp_group.rank
        elif self.enable_auto_parallel:
            mesh = fleet.auto.get_mesh()
            return mesh.get_rank_by_dim_and_process_id("dp", dist.get_rank())
        else:
            return paddle.distributed.get_rank()

    @property
    def dataset_rank(self):
        if self.use_hybrid_parallel:
            return max(self.sharding_parallel_degree, 1) * self.data_parallel_rank + self.sharding_parallel_rank
        elif self.enable_auto_parallel:
            return self.data_parallel_rank
        else:
            return paddle.distributed.get_rank()

    @property
    def dataset_world_size(self):
        if self.use_hybrid_parallel:
            return max(self.sharding_parallel_degree, 1) * max(self.data_parallel_degree, 1)
        elif self.enable_auto_parallel:
            return max(self.sharding_parallel_degree, 1) * max(self.data_parallel_degree, 1)
        else:
            return paddle.distributed.get_world_size()

    @property
    def sharding_parallel_rank(self):
        if self.use_hybrid_parallel:
            hcg = fleet.get_hybrid_communicate_group()
            sharding_group = hcg.get_sharding_parallel_group()
            return max(sharding_group.rank, 0)
        else:
            return 0

    @property
    def tensor_parallel_rank(self):
        if self.use_hybrid_parallel:
            hcg = fleet.get_hybrid_communicate_group()
            tp_group = hcg.get_model_parallel_group()
            return max(tp_group.rank, 0)
        elif self.enable_auto_parallel:
            mesh = fleet.auto.get_mesh()
            return mesh.get_rank_by_dim_and_process_id("mp", dist.get_rank())
        else:
            return 0

    @property
    def pipeline_parallel_rank(self):
        if self.use_hybrid_parallel:
            hcg = fleet.get_hybrid_communicate_group()
            rank = hcg.get_stage_id()
            return max(rank, 0)
        elif self.enable_auto_parallel:
            mesh = fleet.auto.get_mesh()
            return mesh.get_rank_by_dim_and_process_id("pp", dist.get_rank())
        else:
            return 0

    @property
    def optimizer_name_suffix(self):
        if self.use_hybrid_parallel:
            name = []
            if self.tensor_parallel_degree > 1:
                assert self.tensor_parallel_degree < 100, "tensor parallel degree should be less than 100."
                name.append(f"tp{self.tensor_parallel_rank:0>2d}")
            if self.pipeline_parallel_degree > 1:
                assert self.pipeline_parallel_degree < 100, "pipeline parallel degree should be less than 100."
                name.append(f"pp{self.pipeline_parallel_rank:0>2d}")
            if self.sharding_parallel_degree > 1:
                assert self.sharding_parallel_degree < 100, "sharding parallel degree should be less than 100."
                name.append(f"shard{self.sharding_parallel_rank:0>2d}")
            if self.use_expert_parallel:
                name.append(f"moe{self.data_parallel_rank:0>2d}")
            return "_".join(name)
        else:
            if self.use_expert_parallel:
                return f"moe{self.data_parallel_rank:0>2d}"
            return None

    @property
    def weight_name_suffix(self):
        if self.use_hybrid_parallel:
            name = []
            if self.tensor_parallel_degree > 1:
                assert self.tensor_parallel_rank < 100, "tensor parallel rank should be less than 100."
                name.append(f"tp{self.tensor_parallel_rank:0>2d}")
            if self.pipeline_parallel_degree > 1:
                assert self.pipeline_parallel_degree < 100, "tensor parallel rank should be less than 100."
                name.append(f"pp{self.pipeline_parallel_rank:0>2d}")
            if self.use_expert_parallel:
                name.append(f"moe{self.data_parallel_rank:0>2d}")
            return "_".join(name)

        else:
            if self.use_expert_parallel:
                return f"moe{self.data_parallel_rank:0>2d}"
            return None

    def sharded_name_suffix(self, shard_id=None, pp_id=None, moe_id=None):
        if self.use_hybrid_parallel:
            name = []
            if self.tensor_parallel_degree > 1:
                assert self.tensor_parallel_rank < 100, "tensor parallel rank should be less than 100."
                name.append(f"tp{self.tensor_parallel_rank:0>2d}")
            if self.pipeline_parallel_degree > 1:
                if pp_id is None:
                    pp_id = self.pipeline_parallel_rank
                assert isinstance(pp_id, int)
                assert pp_id < 100, "pp_id should be less than 100."
                name.append(f"pp{pp_id:0>2d}")
            if self.sharding_parallel_degree > 1:
                if shard_id is None:
                    shard_id = self.sharding_parallel_rank
                assert isinstance(shard_id, int)
                assert shard_id < 100, "shard_id should be less than 100."
                name.append(f"shard{shard_id:0>2d}")
            if self.use_expert_parallel:
                if moe_id is None:
                    moe_id = self.data_parallel_rank
                assert isinstance(moe_id, int)
                name.append(f"moe{moe_id:0>2d}")
            return "_".join(name)
        else:
            if self.use_expert_parallel:
                if moe_id is None:
                    moe_id = self.data_parallel_rank
                return self._format_name("moe", moe_id, self.data_parallel_degree)
            return None

    @property
    def process_index(self):
        """
        The index of the current process used.
        """
        if self.local_rank != -1:
            return paddle.distributed.get_rank()
        return 0

    @property
    def logical_process_index(self):
        """
        The index of the current process used.
        """
        if self.local_rank != -1:
            sd_size = max(self.sharding_parallel_degree, 1)
            pp_size = max(self.pipeline_parallel_degree, 1)
            tp_size = max(self.tensor_parallel_degree, 1)

            dp_rank = max(self.data_parallel_rank, 0)
            sd_rank = max(self.sharding_parallel_rank, 0)
            pp_rank = max(self.pipeline_parallel_rank, 0)
            tp_rank = max(self.tensor_parallel_rank, 0)

            rank = (
                dp_rank * (sd_size * pp_size * tp_size) + sd_rank * (pp_size * tp_size) + pp_rank * tp_size + tp_rank
            )

            return rank
        return 0

    @property
    def local_process_index(self):
        """
        The index of the local process used.
        """
        if self.local_rank != -1:
            return self.local_rank
        return 0

    @property
    def should_log(self):
        """
        Whether or not the current process should produce log.
        """
        if self.enable_auto_parallel:
            return True
        elif self.log_on_each_node:
            return self.local_process_index == 0
        else:
            return self.process_index == 0

    @property
    def should_save(self):
        """
        Whether or not the current process should write to disk, e.g., to save models and checkpoints.

        For model state:
            work for data parallel, tensor parallel, sharding
        For optimizer state:
            work for data parallel, tensor parallel
            not work for sharding
        """
        if self.save_on_each_node:
            return self.local_process_index == 0
        else:
            if self.enable_auto_parallel:
                return True
            return self.process_index == 0

    @property
    def should_save_model_state(self):
        """
        Whether or not the current process should write to disk, e.g., to save models and checkpoints.

        For model state:
            work for data parallel, tensor parallel, sharding
        For optimizer state:
            work for data parallel, tensor parallel
            not work for sharding
        """
        if self.save_on_each_node:
            return self.local_process_index == 0
        else:
            if self.should_save_sharding_stage1_model:
                return True
            elif self.enable_auto_parallel:
                return True
            elif self.use_hybrid_parallel:
                # save on dataset rank 0
                return self.sharding_parallel_rank == 0 and (self.data_parallel_rank == 0 or self.use_expert_parallel)
            else:
                return self.process_index == 0 or self.use_expert_parallel

    @property
    def _no_sync_in_gradient_accumulation(self):
        """
        Whether or not to use no_sync for the gradients when doing gradient accumulation.
        """
        return True

    @property
    def should_save_sharding_stage1_model(self):
        if self.enable_auto_parallel:
            return False
        return (
            ShardingOption.SHARD_OP in self.sharding and self.sharding_parallel_degree > 1 and self.save_sharded_model
        )

    @property
    def should_load_sharding_stage1_model(self):
        if self.enable_auto_parallel:
            return False
        return (
            ShardingOption.SHARD_OP in self.sharding and self.sharding_parallel_degree > 1 and self.load_sharded_model
        )

    @property
    def should_load_dataset(self):
        if not self.distributed_dataloader:
            return True
        else:
            if self.tensor_parallel_rank == 0 and self.pipeline_parallel_rank == 0:
                return True
            else:
                return False

    @contextlib.contextmanager
    def main_process_first(self, local=True, desc="work"):
        """
        A context manager for paddle distributed environment where on needs to do something on the main process, while
        blocking replicas, and when it's finished releasing the replicas.

        One such use is for `datasets`'s `map` feature which to be efficient should be run once on the main process,
        which upon completion saves a cached version of results and which then automatically gets loaded by the
        replicas.

        Args:
            local (`bool`, *optional*, defaults to `True`):
                if `True` first means process of rank 0 of each node if `False` first means process of rank 0 of node
                rank 0 In multi-node environment with a shared filesystem you most likely will want to use
                `local=False` so that only the main process of the first node will do the processing. If however, the
                filesystem is not shared, then the main process of each node will need to do the processing, which is
                the default behavior.
            desc (`str`, *optional*, defaults to `"work"`):
                a work description to be used in debug logs

        """
        if self.world_size > 1:
            if local:
                is_main_process = self.local_process_index == 0
                main_process_desc = "main local process"
            else:
                is_main_process = self.process_index == 0
                main_process_desc = "main process"

            try:
                if not is_main_process:
                    # tell all replicas to wait
                    logger.debug(f"{self.process_index}: waiting for the {main_process_desc} to perform {desc}")
                    paddle.distributed.barrier()
                yield
            finally:
                if is_main_process:
                    # the wait is over
                    logger.debug(f"{self.process_index}: {main_process_desc} completed {desc}, releasing all replicas")
                    paddle.distributed.barrier()
        else:
            yield

    def get_warmup_steps(self, num_training_steps: int):
        """
        Get number of steps used for a linear warmup.
        """
        warmup_steps = (
            self.warmup_steps if self.warmup_steps > 0 else math.ceil(num_training_steps * self.warmup_ratio)
        )
        return warmup_steps

    def to_dict(self):
        """
        Serializes this instance while replace `Enum` by their values (for JSON serialization support). It obfuscates
        the token values by removing their value.
        """
        d = asdict(self)
        for k, v in d.items():
            if isinstance(v, Enum):
                d[k] = v.value
            if isinstance(v, list) and len(v) > 0 and isinstance(v[0], Enum):
                d[k] = [x.value for x in v]
            if k.endswith("_token"):
                d[k] = f"<{k.upper()}>"
        return d

    def to_json_string(self):
        """
        Serializes this instance to a JSON string.
        """
        return json.dumps(self.to_dict(), indent=2)

    def to_sanitized_dict(self) -> Dict[str, Any]:
        """
        Sanitized serialization
        """
        d = self.to_dict()
        d = {**d, **{"train_batch_size": self.train_batch_size, "eval_batch_size": self.eval_batch_size}}

        valid_types = [bool, int, float, str]
        valid_types.append(paddle.Tensor)

        return {k: v if type(v) in valid_types else str(v) for k, v in d.items()}

    def print_config(self, args=None, key=""):
        """
        print all config values.
        """
        logger.debug("=" * 60)
        if args is None:
            args = self
            key = "Training"

        import paddlenlp

        logger.debug("{:^40}".format("{} Configuration Arguments".format(key)))
        logger.debug("{:30}: {}".format("paddle commit id", paddle.version.commit))
        logger.debug("{:30}: {}".format("paddlenlp commit id", paddlenlp.version.commit))

        for a in dir(args):
            if a[:2] != "__":  # don't print double underscore methods
                v = getattr(args, a)
                if not isinstance(v, types.MethodType):
                    logger.debug("{:30}: {}".format(a, v))

        logger.debug("")
