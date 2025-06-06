#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from typing import Optional, Set

from airflow.exceptions import AirflowException
from airflow.providers.amazon.aws.hooks.sagemaker import SageMakerHook
from airflow.sensors.base_sensor_operator import BaseSensorOperator
from airflow.utils.decorators import apply_defaults


class SageMakerBaseSensor(BaseSensorOperator):
    """
    Contains general sensor behavior for SageMaker.
    Subclasses should implement get_sagemaker_response()
    and state_from_response() methods.
    Subclasses should also implement NON_TERMINAL_STATES and FAILED_STATE methods.
    """

    ui_color = '#ededed'

    @apply_defaults
    def __init__(self, *, aws_conn_id: str = 'aws_default', **kwargs):
        super().__init__(**kwargs)
        self.aws_conn_id = aws_conn_id
        self.hook: Optional[SageMakerHook] = None

    def get_hook(self) -> SageMakerHook:
        """Get SageMakerHook"""
        if self.hook:
            return self.hook

        self.hook = SageMakerHook(aws_conn_id=self.aws_conn_id)
        return self.hook

    def poke(self, context):
        response = self.get_sagemaker_response()

        if not response['ResponseMetadata']['HTTPStatusCode'] == 200:
            self.log.info('Bad HTTP response: %s', response)
            return False

        state = self.state_from_response(response)

        self.log.info('Job currently %s', state)

        if state in self.non_terminal_states():
            return False

        if state in self.failed_states():
            failed_reason = self.get_failed_reason_from_response(response)
            raise AirflowException(f'Sagemaker job failed for the following reason: {failed_reason}')
        return True

    def non_terminal_states(self) -> Set[str]:
        """Placeholder for returning states with should not terminate."""
        raise NotImplementedError('Please implement non_terminal_states() in subclass')

    def failed_states(self) -> Set[str]:
        """Placeholder for returning states with are considered failed."""
        raise NotImplementedError('Please implement failed_states() in subclass')

    def get_sagemaker_response(self) -> Optional[dict]:
        """Placeholder for checking status of a SageMaker task."""
        raise NotImplementedError('Please implement get_sagemaker_response() in subclass')

    def get_failed_reason_from_response(self, response: dict) -> str:  # pylint: disable=unused-argument
        """Placeholder for extracting the reason for failure from an AWS response."""
        return 'Unknown'

    def state_from_response(self, response: dict) -> str:
        """Placeholder for extracting the state from an AWS response."""
        raise NotImplementedError('Please implement state_from_response() in subclass')
