# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from braket.parametric.free_parameter import FreeParameter
from braket.parametric.free_parameter_expression import FreeParameterExpression


class Parameterizable(ABC):
    """A parameterized object is the abstract definition of an object
    that can take in FreeParameterExpressions.
    """

    @property
    @abstractmethod
    def parameters(self) -> list[FreeParameterExpression | FreeParameter | float]:
        """Get the parameters.

        Returns:
            list[Union[FreeParameterExpression, FreeParameter, float]]: The parameters associated
            with the object, either unbound free parameter expressions or bound values. The order
            of the parameters is determined by the subclass.
        """

    @abstractmethod
    def bind_values(self, **kwargs: FreeParameter | str) -> Any:
        """Takes in parameters and returns an object with specified parameters
        replaced with their values.

        Args:
            **kwargs (Union[FreeParameter, str]): Arbitrary keyword arguments.

        Returns:
            Any: The result object will depend on the implementation of the object being bound.
        """
