# coding=utf-8
# Copyright 2025 The TensorFlow Datasets Authors.
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

"""IMDB movie reviews dataset."""

import os
import re

import tensorflow_datasets.public_api as tfds

_DOWNLOAD_URL = "http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"


class IMDBReviewsConfig(tfds.core.BuilderConfig):
  """BuilderConfig for IMDBReviews Builder."""

  def __init__(self, *, text_encoder_config=None, **kwargs):
    """BuilderConfig for IMDBReviews Builder.

    Args:
      text_encoder_config: `tfds.deprecated.text.TextEncoderConfig`,
        configuration for the `tfds.deprecated.text.TextEncoder` used for the
        IMDB `"text"` feature.
      **kwargs: keyword arguments forwarded to super.
    """
    super(IMDBReviewsConfig, self).__init__(
        version=tfds.core.Version("1.0.0"),
        release_notes={
            "1.0.0": "New split API (https://tensorflow.org/datasets/splits)",
        },
        **kwargs,
    )
    self.text_encoder_config = (
        text_encoder_config or tfds.deprecated.text.TextEncoderConfig()
    )


class Builder(tfds.core.GeneratorBasedBuilder):
  """IMDB movie reviews dataset."""

  BUILDER_CONFIGS = [
      IMDBReviewsConfig(
          name="plain_text",
          description="Plain text",
      )
  ]

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "text": tfds.features.Text(
                encoder_config=self.builder_config.text_encoder_config
            ),
            "label": tfds.features.ClassLabel(names=["neg", "pos"]),
        }),
        supervised_keys=("text", "label"),
        homepage="http://ai.stanford.edu/~amaas/data/sentiment/",
    )

  def _vocab_text_gen(self, archive):
    for _, ex in self._generate_examples(
        archive, os.path.join("aclImdb", "train")
    ):
      yield ex["text"]

  def _split_generators(self, dl_manager):
    arch_path = dl_manager.download(_DOWNLOAD_URL)
    archive = lambda: dl_manager.iter_archive(arch_path)

    # Generate vocabulary from training data if SubwordTextEncoder configured
    self.info.features["text"].maybe_build_from_corpus(
        self._vocab_text_gen(archive())
    )

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "archive": archive(),
                "directory": os.path.join("aclImdb", "train"),
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "archive": archive(),
                "directory": os.path.join("aclImdb", "test"),
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split("unsupervised"),
            gen_kwargs={
                "archive": archive(),
                "directory": os.path.join("aclImdb", "train"),
                "labeled": False,
            },
        ),
    ]

  def _generate_examples(self, archive, directory, labeled=True):
    """Generate IMDB examples."""
    # For labeled examples, extract the label from the path.
    reg_path = "(?P<label>neg|pos)" if labeled else "unsup"
    reg = re.compile(
        os.path.join("^%s" % directory, reg_path, "").replace("\\", "\\\\")
    )
    for path, imdb_f in archive:
      res = reg.match(path)
      if not res:
        continue
      text = imdb_f.read().strip()
      label = res.groupdict()["label"] if labeled else -1
      yield path, {
          "text": text,
          "label": label,
      }
