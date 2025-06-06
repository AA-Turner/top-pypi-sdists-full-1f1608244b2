"""
Miscellaneous math utilities module

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def clamp(value: float, min: float = 0, max: float = 1) -> float:
    """Clamps the float value between minimum and maximum. To avoid
    confusion, any call must use either one or all three arguments.

        :param value: The value to clamp.
        :type value: float
        :param min: The minimum value, defaults to 0.
        :type min: float
        :param max: The maximum value, defaults to 1.
        :type max: float
        :return: The clamped value.
        :rtype: float
    """

def lerp(from_value: float, to_value: float, factor: float) -> float:
    """Linearly interpolate between two float values based on factor.

    :param from_value: The value to return when factor is 0.
    :type from_value: float
    :param to_value: The value to return when factor is 1.
    :type to_value: float
    :param factor: The interpolation value, normally in [0.0, 1.0].
    :type factor: float
    :return: The interpolated value.
    :rtype: float
    """

def smoothstep(from_value: float, to_value: float, value) -> float:
    """Performs smooth interpolation between 0 and 1 as value changes between from and to values.
    Outside the range the function returns the same value as the nearest edge.

        :param from_value: The edge value where the result is 0.
        :type from_value: float
        :param to_value: The edge value where the result is 1.
        :type to_value: float
        :return: The interpolated value in [0.0, 1.0].
        :rtype: float
    """
