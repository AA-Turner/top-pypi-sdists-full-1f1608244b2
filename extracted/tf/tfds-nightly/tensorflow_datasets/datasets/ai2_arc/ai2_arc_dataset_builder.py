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

"""ai2_arc dataset."""

import json
import os

from etils import epath
import tensorflow_datasets.public_api as tfds

_HOMEPAGE = "https://allenai.org/data/arc"
_URL = "https://ai2-public-datasets.s3-us-west-2.amazonaws.com/arc/ARC-V1-Feb2018.zip"


class Ai2ArcConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Ai2ARC."""

  def __init__(self, **kwargs):
    """BuilderConfig for Ai2Arc.

    Args:
      **kwargs: keyword arguments forwarded to super.
    """
    super(Ai2ArcConfig, self).__init__(
        version=tfds.core.Version("1.0.0"), **kwargs
    )


class Builder(tfds.core.GeneratorBasedBuilder):
  """The AI2 ARC dataset."""

  BUILDER_CONFIGS = [
      Ai2ArcConfig(
          name="ARC-Challenge",
          description="""\
          Challenge Set of 2590 "hard" questions (those that both a retrieval and a co-occurrence method fail to answer correctly)
          """,
      ),
      Ai2ArcConfig(
          name="ARC-Easy",
          description="""\
          Easy Set of 5197 questions for the ARC Challenge.
          """,
      ),
  ]

  def _info(self):
    # Most questions have four possible answers, but a few have five.
    options = ["A", "B", "C", "D", "E"]
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "id": tfds.features.Text(),
            "question": tfds.features.Text(),
            "choices": tfds.features.Sequence({
                "text": tfds.features.Text(),
                "label": tfds.features.ClassLabel(names=options),
            }),
            "answerKey": tfds.features.ClassLabel(names=options),
        }),
        supervised_keys=None,
        homepage=_HOMEPAGE,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_dir = dl_manager.download_and_extract(_URL)
    data_dir = os.path.join(dl_dir, "ARC-V1-Feb2018-2")
    base_path = os.path.join(data_dir, self.builder_config.name)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "filepath": os.path.join(
                    base_path, self.builder_config.name + "-Train.jsonl"
                )
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "filepath": os.path.join(
                    base_path, self.builder_config.name + "-Dev.jsonl"
                )
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "filepath": os.path.join(
                    base_path, self.builder_config.name + "-Test.jsonl"
                )
            },
        ),
    ]

  def _generate_examples(self, filepath: str):
    """Yields examples. Compatible with huggingface's `nlp` format."""
    # Generally labels are in the format "A", "B", "C", "D" but sometimes
    # they are in the format "1", "2", "3", "4". We convert the later to the
    # former for consistency.
    n_to_l = dict(zip("1 2 3 4 5".split(), "A B C D E".split()))
    with epath.Path(filepath).open() as f:
      for row in f:
        data = json.loads(row)
        answerkey = n_to_l.get(data["answerKey"], data["answerKey"])
        id_ = data["id"]
        question = data["question"]["stem"]
        choices = data["question"]["choices"]
        text_choices = [choice["text"] for choice in choices]
        label_choices = [
            n_to_l.get(choice["label"], choice["label"]) for choice in choices
        ]
        yield id_, {
            "id": id_,
            "answerKey": answerkey,
            "question": question,
            "choices": {"text": text_choices, "label": label_choices},
        }
