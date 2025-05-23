"""Utilities for plotting."""

import warnings

try:
    import matplotlib.pyplot as plt  # noqa: F401
    from ._artists import (
        Arrow3D,
        Frame,
        LabeledFrame,
        Trajectory,
        Camera,
    )
    from ._layout import (
        make_3d_axis,
        remove_frame,
    )
    from ._plot_geometries import (
        plot_box,
        plot_sphere,
        plot_spheres,
        plot_cylinder,
        plot_mesh,
        plot_ellipsoid,
        plot_capsule,
        plot_cone,
    )
    from ._plot_helpers import (
        plot_vector,
        plot_length_variable,
    )

    __all__ = [
        "Arrow3D",
        "Frame",
        "LabeledFrame",
        "Trajectory",
        "Camera",
        "make_3d_axis",
        "remove_frame",
        "plot_box",
        "plot_sphere",
        "plot_spheres",
        "plot_cylinder",
        "plot_mesh",
        "plot_ellipsoid",
        "plot_capsule",
        "plot_cone",
        "plot_vector",
        "plot_length_variable",
    ]
except ImportError as e:
    if e.name == "matplotlib":
        warnings.warn(
            "Matplotlib is not installed, visualization is not " "available",
            ImportWarning,
            stacklevel=2,
        )
    else:
        raise e
