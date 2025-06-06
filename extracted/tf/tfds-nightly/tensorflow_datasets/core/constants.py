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

"""Default values for some parameters of the API when no values are passed."""

# IMPORTANT: when changing values here, update docstrings.

import os

# Directory in which datasets are declared within TFDS sources.
DATASETS_TFDS_SRC_DIR = 'datasets'

# Github base URL
SRC_BASE_URL = 'https://github.com/tensorflow/datasets/tree/master/'

# Directory where to store processed datasets.
# If modifying this, should also update `scripts/cli/build.py` `--data_dir`
DATA_DIR = os.environ.get(
    'TFDS_DATA_DIR',
    os.path.join(os.path.expanduser('~'), 'tensorflow_datasets'),
)

# Prefix of files / directories which aren't finished downloading / extracting.
INCOMPLETE_PREFIX = 'incomplete.'

# Note: GCS constants are defined in `core/utils/gcs_utils.py`

# Name of the file to output the features information.
FEATURES_FILENAME = 'features.json'

# Name of the file to output the DatasetInfo protobuf object.
DATASET_INFO_FILENAME = 'dataset_info.json'
LICENSE_FILENAME = 'LICENSE'
METADATA_FILENAME = 'metadata.json'
CHECKSUMS_FILENAME = 'checksums.tsv'

# Filepath for mapping between TFDS datasets and PapersWithCode entries.
PWC_FILENAME = 'tfds_to_pwc_links.json'
PWC_LINKS_PATH = f'scripts/documentation/{PWC_FILENAME}'

# Retry parameters. Delays are in seconds.
TFDS_RETRY_TRIES = int(os.environ.get('TFDS_RETRY_TRIES', 3))
TFDS_RETRY_INITIAL_DELAY = int(os.environ.get('TFDS_RETRY_INITIAL_DELAY', 1))
# How much to multiply the delay by for each subsequent try
TFDS_RETRY_DELAY_MULTIPLIER = int(
    os.environ.get('TFDS_RETRY_DELAY_MULTIPLIER', 2)
)
# Random noise to add to the delay (random pick between 0 and noise).
TFDS_RETRY_NOISE = float(os.environ.get('TFDS_RETRY_NOISE', 0.5))
# If the error message contains any of these substrings, retry.
TFDS_RETRY_MSG_SUBSTRINGS = os.environ.get(
    'TFDS_RETRY_MSG_SUBSTRINGS',
    (
        'deadline_exceeded,'
        '408 Request Timeout,'
        '429 Too Many Requests,'
        '500 Internal Server Error,'
        '502 Bad Gateway,'
        '503 Service Unavailable,'
        '504 Gateway Timeout,'
        '509 Bandwidth Limit Exceeded,'
        '599 Gateway Error'
    ),
).split(',')
