#  Copyright 2022 The HuggingFace Team. All rights reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import logging
import os
from pathlib import Path
from typing import Dict, Optional, Union

import openvino
from huggingface_hub import hf_hub_download
from huggingface_hub.constants import HUGGINGFACE_HUB_CACHE
from openvino._offline_transformations import apply_moc_transformations, compress_model_transformation
from transformers import GenerationConfig, PretrainedConfig
from transformers.file_utils import add_start_docstrings

from ...exporters.openvino import main_export
from ...exporters.openvino.stateful import model_has_state
from ..utils.import_utils import is_transformers_version
from .configuration import OVConfig, OVWeightQuantizationConfig
from .modeling_base import OVBaseModel
from .utils import (
    ONNX_DECODER_NAME,
    ONNX_DECODER_WITH_PAST_NAME,
    ONNX_ENCODER_NAME,
    OV_DECODER_NAME,
    OV_DECODER_WITH_PAST_NAME,
    OV_ENCODER_NAME,
    TemporaryDirectory,
)


logger = logging.getLogger(__name__)


@add_start_docstrings(
    """
    Base OVModelForSeq2SeqLM class.
    """,
)
class OVBaseModelForSeq2SeqLM(OVBaseModel):
    export_feature = "text2text-generation"

    def __init__(
        self,
        encoder: openvino.runtime.Model,
        decoder: openvino.runtime.Model,
        decoder_with_past: openvino.runtime.Model = None,
        config: PretrainedConfig = None,
        device: str = "CPU",
        dynamic_shapes: bool = True,
        ov_config: Optional[Dict[str, str]] = None,
        model_save_dir: Optional[Union[str, Path, TemporaryDirectory]] = None,
        quantization_config: Union[OVWeightQuantizationConfig, Dict] = None,
        **kwargs,
    ):
        self.config = config
        self.use_cache = decoder_with_past is not None or model_has_state(decoder)
        self.model_save_dir = model_save_dir
        self._compile_only = kwargs.get("compile_only", False)
        self._device = device.upper()
        self.is_dynamic = dynamic_shapes
        self.ov_config = {} if ov_config is None else {**ov_config}
        self.preprocessors = kwargs.get("preprocessors", [])

        if self.is_dynamic and not self._compile_only:
            encoder = self._reshape(encoder, -1, -1, is_decoder=False)
            decoder = self._reshape(decoder, -1, -1)
            if decoder_with_past is not None:
                decoder_with_past = self._reshape(decoder_with_past, -1, -1) if self.use_cache else None
        self.encoder_model = encoder
        self.decoder_model = decoder
        self.decoder_with_past_model = decoder_with_past

        generation_config = kwargs.get("generation_config", None)
        self.generation_config = generation_config or GenerationConfig.from_model_config(config)

        if is_transformers_version(">=", "4.44.99"):
            # some model configs may have issues with loading without parameters initialization
            try:
                misplaced_generation_parameters = self.config._get_non_default_generation_parameters()
            except (KeyError, TypeError):
                misplaced_generation_parameters = {}
            if len(misplaced_generation_parameters) > 0:
                logger.warning(
                    "Moving the following attributes in the config to the generation config: "
                    f"{misplaced_generation_parameters}. You are seeing this warning because you've set "
                    "generation parameters in the model config, as opposed to in the generation config.",
                )
                for param_name, param_value in misplaced_generation_parameters.items():
                    setattr(self.generation_config, param_name, param_value)
                    setattr(self.config, param_name, None)

        self._openvino_config = None
        if quantization_config:
            self._openvino_config = OVConfig(quantization_config=quantization_config)
        self._set_ov_config_parameters()

    def _save_pretrained(self, save_directory: Union[str, Path]):
        """
        Saves the model to the OpenVINO IR format so that it can be re-loaded using the
        [`~optimum.intel.openvino.modeling.OVModel.from_pretrained`] class method.

        Arguments:
            save_directory (`str` or `Path`):
                The directory where to save the model files.
        """
        src_files = [self.encoder_model, self.decoder_model]
        dst_file_names = [OV_ENCODER_NAME, OV_DECODER_NAME]
        if self.decoder_with_past_model is not None:
            src_files.append(self.decoder_with_past_model)
            dst_file_names.append(OV_DECODER_WITH_PAST_NAME)

        for src_file, dst_file_name in zip(src_files, dst_file_names):
            dst_path = os.path.join(save_directory, dst_file_name)
            openvino.save_model(src_file, dst_path, compress_to_fp16=False)

        self._save_openvino_config(save_directory)
        if self.generation_config is not None:
            try:
                self.generation_config.save_pretrained(save_directory)
            except Exception as exception:
                logger.warning(
                    f"The generation config will not be saved, saving failed with following error:\n{exception}"
                )

    @classmethod
    def _from_pretrained(
        cls,
        model_id: Union[str, Path],
        config: PretrainedConfig,
        token: Optional[Union[bool, str]] = None,
        revision: Optional[str] = None,
        force_download: bool = False,
        cache_dir: str = HUGGINGFACE_HUB_CACHE,
        encoder_file_name: Optional[str] = None,
        decoder_file_name: Optional[str] = None,
        decoder_with_past_file_name: Optional[str] = None,
        local_files_only: bool = False,
        use_cache: bool = True,
        from_onnx: bool = False,
        load_in_8bit: bool = False,
        quantization_config: Union[OVWeightQuantizationConfig, Dict] = None,
        **kwargs,
    ):
        """
        Loads a model and its configuration file from a directory or the HF Hub.

        Arguments:
            model_id (`str` or `Path`):
                The directory from which to load the model.
                Can be either:
                    - The model id of a pretrained model hosted inside a model repo on huggingface.co.
                    - The path to a directory containing the model weights.
            token (Optional[Union[bool, str]], defaults to `None`):
                The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated
                when running `huggingface-cli login` (stored in `~/.huggingface`).
            revision (`str`):
                The specific model version to use. It can be a branch name, a tag name, or a commit id.
            force_download (`bool`, *optional*, defaults to `False`):
                Whether or not to force the (re-)download of the model weights and configuration files, overriding the
                cached versions if they exist.
            cache_dir (`Union[str, Path]`, *optional*):
                The path to a directory in which a downloaded pretrained model configuration should be cached if the
                standard cache should not be used.
            encoder_file_name(`str`, *optional*):
                The encoder model file name. Overwrites the default file name openvino_encoder_model.xml and allows one to
                load the encoder model with a different name.
            decoder_file_name(`str`, *optional*):
                The decoder model file name. Overwrites the default file name openvino_decoder_model.xml and allows one to
                load the decoder model with a different name.
            decoder_with_past_file_name(`str`, *optional*):
                The decoder with past key values model file name overwriting the default file name
                openvino_decoder_with_past_model.xml, allowing to load the decoder model with a different name.
            local_files_only(`bool`, *optional*, defaults to `False`):
                Whether or not to only look at local files (i.e., do not try to download the model).
        """
        generation_config = kwargs.pop("generation_config", None)
        subfolder = kwargs.pop("subfolder", "")

        default_encoder_file_name = ONNX_ENCODER_NAME if from_onnx else OV_ENCODER_NAME
        default_decoder_file_name = ONNX_DECODER_NAME if from_onnx else OV_DECODER_NAME
        default_decoder_with_past_file_name = ONNX_DECODER_WITH_PAST_NAME if from_onnx else OV_DECODER_WITH_PAST_NAME
        encoder_file_name = encoder_file_name or default_encoder_file_name
        decoder_file_name = decoder_file_name or default_decoder_file_name
        decoder_with_past_file_name = decoder_with_past_file_name or default_decoder_with_past_file_name
        decoder_with_past = None

        quantization_config = cls._prepare_weight_quantization_config(quantization_config, load_in_8bit)

        compile_only = kwargs.get("compile_only", False)

        # Load model from a local directory
        if os.path.isdir(model_id):
            model_save_dir = Path(model_id)
            if not compile_only:
                encoder = cls.load_model(os.path.join(model_id, encoder_file_name), quantization_config)
                decoder = cls.load_model(os.path.join(model_id, decoder_file_name), quantization_config)
                if (
                    use_cache
                    and not model_has_state(decoder)
                    and os.path.exists(os.path.join(model_id, decoder_with_past_file_name))
                ):
                    decoder_with_past = cls.load_model(
                        os.path.join(model_id, decoder_with_past_file_name), quantization_config
                    )
            else:
                encoder = cls._compile_model(
                    os.path.join(model_id, encoder_file_name),
                    kwargs.get("device", "CPU"),
                    kwargs.get("ov_config"),
                    model_save_dir,
                )
                decoder = cls._compile_model(
                    os.path.join(model_id, decoder_file_name),
                    kwargs.get("device", "CPU"),
                    kwargs.get("ov_config"),
                    model_save_dir,
                )
                if (
                    use_cache
                    and not model_has_state(decoder)
                    and os.path.exists(os.path.join(model_id, decoder_with_past_file_name))
                ):
                    decoder_with_past = cls._compile_model(
                        os.path.join(model_id, decoder_with_past_file_name),
                        kwargs.get("device", "CPU"),
                        kwargs.get("ov_config"),
                        model_save_dir,
                    )

        # Load model from hub
        else:
            model_file_names = {"encoder": encoder_file_name, "decoder": decoder_file_name}

            # If not ONNX then OpenVINO IR : adds binary files
            if not from_onnx:
                for key in list(model_file_names.keys()):
                    model_file_names[key + "_bin"] = model_file_names[key].replace(".xml", ".bin")
            file_names = model_file_names.copy()
            for name, file_name in model_file_names.items():
                model_cache_path = hf_hub_download(
                    repo_id=model_id,
                    filename=file_name,
                    token=token,
                    revision=revision,
                    cache_dir=cache_dir,
                    force_download=force_download,
                    local_files_only=local_files_only,
                    subfolder=subfolder,
                )
                file_names[name] = model_cache_path

            model_save_dir = Path(model_cache_path).parent
            if not compile_only:
                encoder = cls.load_model(file_names["encoder"], quantization_config)
                decoder = cls.load_model(file_names["decoder"], quantization_config)
                if use_cache and not model_has_state(decoder):
                    model_file_names["decoder_with_past"] = decoder_with_past_file_name
                    with_past_files = ["decoder_with_past"]
                    if not from_onnx:
                        with_past_files.append("decoder_with_past_bin")
                        model_file_names["decoder_with_past_bin"] = decoder_with_past_file_name.replace(".xml", ".bin")
                    for name in with_past_files:
                        model_cache_path = hf_hub_download(
                            repo_id=model_id,
                            filename=model_file_names[name],
                            token=token,
                            revision=revision,
                            cache_dir=cache_dir,
                            force_download=force_download,
                            local_files_only=local_files_only,
                            subfolder=subfolder,
                        )
                        file_names[name] = model_cache_path
                    decoder_with_past = cls.load_model(file_names["decoder_with_past"], quantization_config)
            else:
                encoder = cls._compile_model(
                    file_names["encoder"], kwargs.get("device", "CPU"), kwargs.get("ov_config"), model_save_dir
                )
                decoder = cls._compile_model(
                    file_names["decoder"], kwargs.get("device", "CPU"), kwargs.get("ov_config"), model_save_dir
                )
                if use_cache and not model_has_state(decoder):
                    model_file_names["decoder_with_past"] = decoder_with_past_file_name
                    with_past_files = ["decoder_with_past"]
                    if not from_onnx:
                        with_past_files.append("decoder_with_past_bin")
                        model_file_names["decoder_with_past_bin"] = decoder_with_past_file_name.replace(".xml", ".bin")
                    for name in with_past_files:
                        model_cache_path = hf_hub_download(
                            repo_id=model_id,
                            filename=model_file_names[name],
                            token=token,
                            revision=revision,
                            cache_dir=cache_dir,
                            force_download=force_download,
                            local_files_only=local_files_only,
                            subfolder=subfolder,
                        )
                        file_names[name] = model_cache_path
                    decoder_with_past = cls._compile_model(
                        file_names["decoder_with_past"],
                        kwargs.get("device", "CPU"),
                        kwargs.get("ov_config"),
                        model_save_dir,
                    )

        if generation_config is None:
            try:
                generation_config = GenerationConfig.from_pretrained(
                    model_id,
                    cache_dir=cache_dir,
                    force_download=force_download,
                    local_files_only=local_files_only,
                    token=token,
                    revision=revision,
                    subfolder=subfolder,
                )
                if getattr(generation_config, "cache_implementation", None) is not None:
                    generation_config.cache_implementation = None
            except OSError:
                logger.info(
                    "Generation config file not found, using a generation config created from the model config."
                )

        return cls(
            encoder=encoder,
            decoder=decoder,
            decoder_with_past=decoder_with_past,
            config=config,
            model_save_dir=model_save_dir,
            quantization_config=quantization_config,
            generation_config=generation_config,
            **kwargs,
        )

    @classmethod
    def _from_transformers(
        cls,
        model_id: str,
        config: PretrainedConfig,
        token: Optional[Union[bool, str]] = None,
        revision: Optional[str] = None,
        force_download: bool = False,
        cache_dir: str = HUGGINGFACE_HUB_CACHE,
        subfolder: str = "",
        local_files_only: bool = False,
        task: Optional[str] = None,
        use_cache: bool = True,
        trust_remote_code: bool = False,
        load_in_8bit: Optional[bool] = None,
        quantization_config: Union[OVWeightQuantizationConfig, Dict] = None,
        **kwargs,
    ):
        """
        Export a vanilla Transformers model into an ONNX model using `transformers.onnx.export_onnx`.

        Arguments:
            model_id (`str` or `Path`):
                The directory from which to load the model.
                Can be either:
                    - The model id of a pretrained model hosted inside a model repo on huggingface.co.
                    - The path to a directory containing the model weights.
            save_dir (`str` or `Path`):
                The directory where the exported ONNX model should be saved, defaults to
                `transformers.file_utils.default_cache_path`, which is the cache directory for transformers.
            token (Optional[Union[bool, str]], defaults to `None`):
                The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated
                when running `huggingface-cli login` (stored in `~/.huggingface`).
            revision (`str`):
                Revision is the specific model version to use. It can be a branch name, a tag name, or a commit id
            kwargs (`Dict`, *optional*):
                kwargs will be passed to the model during initialization
        """
        save_dir = TemporaryDirectory()
        save_dir_path = Path(save_dir.name)

        # This attribute is needed to keep one reference on the temporary directory, since garbage collecting
        # would end-up removing the directory containing the underlying OpenVINO model
        cls._model_save_dir_tempdirectory_instance = save_dir

        if task is None:
            task = cls.export_feature
            if use_cache:
                task = task + "-with-past"

        compile_only = kwargs.pop("compile_only", False)
        if compile_only:
            logger.warning(
                "`compile_only` mode will be disabled because it does not support model export."
                "Please provide openvino model obtained using optimum-cli or saved on disk using `save_pretrained`"
            )
            compile_only = False
        # If load_in_8bit and quantization_config not specified then ov_config is set to None and will be set by default in convert depending on the model size
        if load_in_8bit is None and not quantization_config:
            ov_config = None
        else:
            ov_config = OVConfig(dtype="fp32")
        stateful = kwargs.get("stateful", True)
        variant = kwargs.pop("variant", None)

        main_export(
            model_name_or_path=model_id,
            output=save_dir_path,
            task=task,
            subfolder=subfolder,
            revision=revision,
            cache_dir=cache_dir,
            token=token,
            local_files_only=local_files_only,
            force_download=force_download,
            trust_remote_code=trust_remote_code,
            ov_config=ov_config,
            stateful=stateful,
            variant=variant,
        )

        return cls._from_pretrained(
            model_id=save_dir_path,
            config=config,
            use_cache=use_cache,
            load_in_8bit=load_in_8bit,
            quantization_config=quantization_config,
            compile_only=compile_only,
            **kwargs,
        )

    def _reshape(self, model: openvino.runtime.Model, batch_size: int, sequence_length: int, is_decoder=True):
        shapes = {}
        for inputs in model.inputs:
            shapes[inputs] = inputs.get_partial_shape()
            shapes[inputs][0] = batch_size if not is_decoder else -1
            if inputs.get_any_name().startswith("past_key_values"):
                shapes[inputs][2] = -1
            elif inputs.get_any_name().startswith("cache_position"):
                shapes[inputs][0] = sequence_length
            elif is_decoder and not inputs.get_any_name().startswith("encoder"):
                if not inputs.get_any_name().startswith("beam_idx"):
                    shapes[inputs][1] = -1
            else:
                shapes[inputs][1] = sequence_length
        model.reshape(shapes)
        return model

    def reshape(self, batch_size: int, sequence_length: int):
        """
        Propagates the given input shapes on the model's layers, fixing the inputs shapes of the model.

        Arguments:
            batch_size (`int`):
                The batch size.
            sequence_length (`int`):
                The sequence length.
        """
        if self._compile_only:
            raise ValueError(
                "`reshape()` is not supported with `compile_only` mode, please intialize model without this option"
            )
        logger.warning("Some part of the model's decoder do not support static shapes and will be kept dynamic.")
        self.is_dynamic = True if batch_size == -1 and sequence_length == -1 else False
        self.encoder_model = self._reshape(self.encoder_model, batch_size, sequence_length, is_decoder=False)
        self.decoder_model = self._reshape(self.decoder_model, batch_size, sequence_length)
        if self.decoder_with_past_model is not None:
            self.decoder_with_past_model = self._reshape(self.decoder_with_past_model, batch_size, sequence_length)

    def half(self):
        """
        Converts all the model weights to FP16 for more efficient inference on GPU.
        """
        if self._compile_only:
            raise ValueError(
                "`half()` is not supported with `compile_only` mode, please intialize model without this option"
            )
        apply_moc_transformations(self.encoder_model, cf=False)
        apply_moc_transformations(self.decoder_model, cf=False)
        compress_model_transformation(self.encoder_model)
        compress_model_transformation(self.decoder_model)
        if self.decoder_with_past_model is not None:
            apply_moc_transformations(self.decoder_with_past_model, cf=False)
            compress_model_transformation(self.decoder_with_past_model)
        return self

    def forward(self, *args, **kwargs):
        raise NotImplementedError
