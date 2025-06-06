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

"""GAP is a gender-balanced text data set."""

from __future__ import annotations

import csv

from etils import epath
import numpy as np
from tensorflow_datasets.core.utils import bool_utils
import tensorflow_datasets.public_api as tfds

_CITATION = """
@article{DBLP:journals/corr/abs-1810-05201,
  author    = {Kellie Webster and
               Marta Recasens and
               Vera Axelrod and
               Jason Baldridge},
  title     = {Mind the {GAP:} {A} Balanced Corpus of Gendered Ambiguous Pronouns},
  journal   = {CoRR},
  volume    = {abs/1810.05201},
  year      = {2018},
  url       = {http://arxiv.org/abs/1810.05201},
  archivePrefix = {arXiv},
  eprint    = {1810.05201},
  timestamp = {Tue, 30 Oct 2018 20:39:56 +0100},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1810-05201},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""

_DESCRIPTION = """
GAP is a gender-balanced dataset containing 8,908 coreference-labeled pairs of 
(ambiguous pronoun, antecedent name), sampled from Wikipedia and released by 
Google AI Language for the evaluation of coreference resolution in practical 
applications.
"""

_TRAINURL = 'https://raw.githubusercontent.com/google-research-datasets/gap-coreference/master/gap-development.tsv'
_VALIDATIONURL = 'https://raw.githubusercontent.com/google-research-datasets/gap-coreference/master/gap-validation.tsv'
_TESTURL = 'https://raw.githubusercontent.com/google-research-datasets/gap-coreference/master/gap-test.tsv'


class Gap(tfds.core.GeneratorBasedBuilder):
  """GAP is a gender-balanced dataset.

  It contains 8,908 coreference-labeled pairs
  of (ambiguous pronoun, antecedent name), sampled from Wikipedia.
  """

  VERSION = tfds.core.Version('0.1.1')
  RELEASE_NOTES = {
      '0.1.1': 'Fixes parsing of boolean field `A-coref` and `B-coref`.',
      '0.1.0': 'Initial release.',
  }

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'ID': tfds.features.Text(),
            'Text': tfds.features.Text(),
            'Pronoun': tfds.features.Text(),
            'Pronoun-offset': np.int32,
            'A': tfds.features.Text(),
            'A-offset': np.int32,
            'A-coref': np.bool_,
            'B': tfds.features.Text(),
            'B-offset': np.int32,
            'B-coref': np.bool_,
            'URL': tfds.features.Text(),
        }),
        supervised_keys=None,
        homepage='https://github.com/google-research-datasets/gap-coreference',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    directory = dl_manager.download_and_extract(
        {'train': _TRAINURL, 'validation': _VALIDATIONURL, 'test': _TESTURL}
    )
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={'filepath': directory['train']},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={'filepath': directory['validation']},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={'filepath': directory['test']},
        ),
    ]

  def _generate_examples(self, filepath):
    """Yields examples."""
    with epath.Path(filepath).open() as tsvfile:
      reader = csv.DictReader(tsvfile, dialect='excel-tab')
      for i, row in enumerate(reader):
        row['A-coref'] = bool_utils.parse_bool(row['A-coref'])
        row['B-coref'] = bool_utils.parse_bool(row['B-coref'])
        yield i, row
