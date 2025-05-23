from typing import Union

from mpl_toolkits.mplot3d import Axes3D

def make_3d_axis(
    ax_s: float,
    pos: int = ...,
    unit: Union[str, None] = ...,
    n_ticks: int = ...,
) -> Axes3D: ...
def remove_frame(
    ax: Axes3D,
    left: float = ...,
    bottom: float = ...,
    right: float = ...,
    top: float = ...,
): ...
