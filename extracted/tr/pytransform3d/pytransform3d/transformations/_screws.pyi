import numpy as np
import numpy.typing as npt
from typing import Tuple

def check_screw_parameters(
    q: npt.ArrayLike, s_axis: npt.ArrayLike, h: float
) -> Tuple[np.ndarray, np.ndarray, float]: ...
def check_screw_axis(screw_axis: npt.ArrayLike) -> np.ndarray: ...
def check_exponential_coordinates(Stheta: npt.ArrayLike) -> np.ndarray: ...
def check_screw_matrix(
    screw_matrix: npt.ArrayLike,
    tolerance: float = ...,
    strict_check: bool = ...,
) -> np.ndarray: ...
def check_transform_log(
    transform_log: npt.ArrayLike,
    tolerance: float = ...,
    strict_check: bool = ...,
) -> np.ndarray: ...
def norm_exponential_coordinates(Stheta: npt.ArrayLike) -> np.ndarray: ...
def assert_exponential_coordinates_equal(
    Stheta1: npt.ArrayLike, Stheta2: npt.ArrayLike
): ...
def assert_screw_parameters_equal(
    q1: npt.ArrayLike,
    s_axis1: npt.ArrayLike,
    h1: float,
    theta1: float,
    q2: npt.ArrayLike,
    s_axis2: npt.ArrayLike,
    h2: float,
    theta2: float,
    *args,
    **kwargs,
): ...
def screw_parameters_from_screw_axis(
    screw_axis: npt.ArrayLike,
) -> Tuple[np.ndarray, np.ndarray, float]: ...
def screw_axis_from_screw_parameters(
    q: npt.ArrayLike, s_axis: npt.ArrayLike, h: float
) -> np.ndarray: ...
def screw_axis_from_exponential_coordinates(
    Stheta: npt.ArrayLike,
) -> Tuple[np.ndarray, float]: ...
def screw_axis_from_screw_matrix(screw_matrix: npt.ArrayLike) -> np.ndarray: ...
def exponential_coordinates_from_screw_axis(
    screw_axis: npt.ArrayLike, theta: float
) -> np.ndarray: ...
def exponential_coordinates_from_transform_log(
    transform_log: npt.ArrayLike, check: bool = ...
) -> np.ndarray: ...
def screw_matrix_from_screw_axis(screw_axis: npt.ArrayLike) -> np.ndarray: ...
def screw_matrix_from_transform_log(
    transform_log: npt.ArrayLike,
) -> np.ndarray: ...
def transform_log_from_exponential_coordinates(
    Stheta: npt.ArrayLike,
) -> np.ndarray: ...
def transform_log_from_screw_matrix(
    screw_matrix: npt.ArrayLike, theta: float
) -> np.ndarray: ...
def transform_from_exponential_coordinates(
    Stheta: npt.ArrayLike, check: bool = ...
) -> np.ndarray: ...
def transform_from_transform_log(
    transform_log: npt.ArrayLike,
) -> np.ndarray: ...
def dual_quaternion_from_screw_parameters(
    q: npt.ArrayLike, s_axis: npt.ArrayLike, h: float, theta: float
) -> np.ndarray: ...
