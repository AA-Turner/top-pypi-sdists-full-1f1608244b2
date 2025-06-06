import os
import pickle
import tempfile
import warnings

import numpy as np
import pytest
from numpy.testing import assert_array_almost_equal

import pytransform3d.rotations as pr
import pytransform3d.transformations as pt
from pytransform3d import transform_manager
from pytransform3d.transform_manager import TransformManager


def test_request_added_transform():
    """Request an added transform from the transform manager."""
    rng = np.random.default_rng(0)
    A2B = pt.random_transform(rng)

    tm = TransformManager()
    assert len(tm.transforms) == 0
    tm.add_transform("A", "B", A2B)
    assert len(tm.transforms) == 1
    A2B_2 = tm.get_transform("A", "B")
    assert_array_almost_equal(A2B, A2B_2)


def test_remove_frame():
    """Test removing a frame from the transform manager."""
    tm = TransformManager()

    rng = np.random.default_rng(0)

    A2B = pt.random_transform(rng)
    A2D = pt.random_transform(rng)
    B2C = pt.random_transform(rng)
    D2E = pt.random_transform(rng)

    tm.add_transform("A", "B", A2B)
    tm.add_transform("A", "D", A2D)
    tm.add_transform("B", "C", B2C)
    tm.add_transform("D", "E", D2E)

    assert tm.has_frame("B")

    A2E = tm.get_transform("A", "E")

    # Check that connections are correctly represented in self.i and self.j
    assert tm.i == [
        tm.nodes.index("A"),
        tm.nodes.index("A"),
        tm.nodes.index("B"),
        tm.nodes.index("D"),
    ]
    assert tm.j == [
        tm.nodes.index("B"),
        tm.nodes.index("D"),
        tm.nodes.index("C"),
        tm.nodes.index("E"),
    ]

    tm.remove_frame("B")
    assert not tm.has_frame("B")

    # Ensure connections involving "B" are removed and the remaining
    # connections are correctly represented.
    assert tm.i == [tm.nodes.index("A"), tm.nodes.index("D")]
    assert tm.j == [tm.nodes.index("D"), tm.nodes.index("E")]

    with pytest.raises(KeyError, match="Unknown frame"):
        tm.get_transform("A", "B")
    with pytest.raises(KeyError, match="Unknown frame"):
        tm.get_transform("B", "C")

    assert tm.has_frame("A")
    assert tm.has_frame("C")
    assert tm.has_frame("D")
    assert tm.has_frame("E")

    # Ensure we cannot retrieve paths involving the removed frame
    with pytest.raises(KeyError, match="Cannot compute path"):
        tm.get_transform("A", "C")

    tm.get_transform("A", "D")
    tm.get_transform("D", "E")

    assert_array_almost_equal(A2E, tm.get_transform("A", "E"))


def test_remove_frame_does_not_exist():
    tm = TransformManager()
    with pytest.raises(KeyError, match="not in the graph"):
        tm.remove_frame("Any")


def test_request_inverse_transform():
    """Request an inverse transform from the transform manager."""
    rng = np.random.default_rng(0)
    A2B = pt.random_transform(rng)

    tm = TransformManager()
    tm.add_transform("A", "B", A2B)
    A2B_2 = tm.get_transform("A", "B")
    assert_array_almost_equal(A2B, A2B_2)

    B2A = tm.get_transform("B", "A")
    B2A_2 = pt.invert_transform(A2B)
    assert_array_almost_equal(B2A, B2A_2)


def test_has_frame():
    """Check if frames have been registered with transform."""
    tm = TransformManager()
    tm.add_transform("A", "B", np.eye(4))
    assert tm.has_frame("A")
    assert tm.has_frame("B")
    assert not tm.has_frame("C")


def test_transform_not_added():
    """Test request for transforms that have not been added."""
    rng = np.random.default_rng(0)
    A2B = pt.random_transform(rng)
    C2D = pt.random_transform(rng)

    tm = TransformManager()
    tm.add_transform("A", "B", A2B)
    tm.add_transform("C", "D", C2D)

    with pytest.raises(KeyError, match="Unknown frame"):
        tm.get_transform("A", "G")
    with pytest.raises(KeyError, match="Unknown frame"):
        tm.get_transform("G", "D")
    with pytest.raises(KeyError, match="Cannot compute path"):
        tm.get_transform("A", "D")


def test_request_concatenated_transform():
    """Request a concatenated transform from the transform manager."""
    rng = np.random.default_rng(0)
    A2B = pt.random_transform(rng)
    B2C = pt.random_transform(rng)
    F2A = pt.random_transform(rng)

    tm = TransformManager()
    tm.add_transform("A", "B", A2B)
    tm.add_transform("B", "C", B2C)
    tm.add_transform("D", "E", np.eye(4))
    tm.add_transform("F", "A", F2A)

    A2C = tm.get_transform("A", "C")
    assert_array_almost_equal(A2C, pt.concat(A2B, B2C))

    C2A = tm.get_transform("C", "A")
    assert_array_almost_equal(
        C2A, pt.concat(pt.invert_transform(B2C), pt.invert_transform(A2B))
    )

    F2B = tm.get_transform("F", "B")
    assert_array_almost_equal(F2B, pt.concat(F2A, A2B))


def test_update_transform():
    """Update an existing transform."""
    rng = np.random.default_rng(0)
    A2B1 = pt.random_transform(rng)
    A2B2 = pt.random_transform(rng)

    tm = TransformManager()
    tm.add_transform("A", "B", A2B1)
    tm.add_transform("A", "B", A2B2)
    A2B = tm.get_transform("A", "B")

    # Hack: test depends on internal member
    assert_array_almost_equal(A2B, A2B2)
    assert len(tm.i) == 1
    assert len(tm.j) == 1


def test_pickle():
    """Test if a transform manager can be pickled."""
    rng = np.random.default_rng(1)
    A2B = pt.random_transform(rng)
    tm = TransformManager()
    tm.add_transform("A", "B", A2B)

    _, filename = tempfile.mkstemp(".pickle")
    try:
        with open(filename, "wb") as f:
            pickle.dump(tm, f)
        with open(filename, "rb") as f:
            tm2 = pickle.load(f)
    finally:
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except OSError:
                pass  # workaround for permission problem on Windows
    A2B2 = tm2.get_transform("A", "B")
    assert_array_almost_equal(A2B, A2B2)


def test_whitelist():
    """Test correct handling of whitelists for plotting."""
    rng = np.random.default_rng(2)
    A2B = pt.random_transform(rng)
    tm = TransformManager()
    tm.add_transform("A", "B", A2B)

    nodes = tm._whitelisted_nodes(None)
    assert {"A", "B"} == nodes
    nodes = tm._whitelisted_nodes(["A"])
    assert {"A"} == nodes
    with pytest.raises(KeyError, match="unknown nodes"):
        tm._whitelisted_nodes(["C"])


def test_check_consistency():
    """Test correct detection of inconsistent graphs."""
    rng = np.random.default_rng(2)

    tm = TransformManager()

    A2B = pt.random_transform(rng)
    tm.add_transform("A", "B", A2B)
    B2A = pt.random_transform(rng)
    tm.add_transform("B", "A", B2A)
    assert not tm.check_consistency()

    tm = TransformManager()

    A2B = pt.random_transform(rng)
    tm.add_transform("A", "B", A2B)
    assert tm.check_consistency()

    C2D = pt.random_transform(rng)
    tm.add_transform("C", "D", C2D)
    assert tm.check_consistency()

    B2C = pt.random_transform(rng)
    tm.add_transform("B", "C", B2C)
    assert tm.check_consistency()

    A2D_over_path = tm.get_transform("A", "D")

    A2D = pt.random_transform(rng)
    tm.add_transform("A", "D", A2D)
    assert not tm.check_consistency()

    tm.add_transform("A", "D", A2D_over_path)
    assert tm.check_consistency()


def test_connected_components():
    """Test computation of connected components in the graph."""
    tm = TransformManager()
    tm.add_transform("A", "B", np.eye(4))
    assert tm.connected_components() == 1
    tm.add_transform("D", "E", np.eye(4))
    assert tm.connected_components() == 2
    tm.add_transform("B", "C", np.eye(4))
    assert tm.connected_components() == 2
    tm.add_transform("D", "C", np.eye(4))
    assert tm.connected_components() == 1


def test_png_export():
    """Test if the graph can be exported to PNG."""
    rng = np.random.default_rng(0)

    ee2robot = pt.transform_from_pq(
        np.hstack((np.array([0.4, -0.3, 0.5]), pr.random_quaternion(rng)))
    )
    cam2robot = pt.transform_from_pq(
        np.hstack((np.array([0.0, 0.0, 0.8]), pr.q_id))
    )
    object2cam = pt.transform_from(
        pr.active_matrix_from_intrinsic_euler_xyz(np.array([0.0, 0.0, 0.5])),
        np.array([0.5, 0.1, 0.1]),
    )

    tm = TransformManager()
    tm.add_transform("end-effector", "robot", ee2robot)
    tm.add_transform("camera", "robot", cam2robot)
    tm.add_transform("object", "camera", object2cam)

    _, filename = tempfile.mkstemp(".png")
    try:
        tm.write_png(filename)
        assert os.path.exists(filename)
    except ImportError:
        pytest.skip("pydot is required for this test")
    finally:
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except OSError:
                pass  # workaround for permission problem on Windows


def test_png_export_without_pydot_fails():
    """Test graph export without pydot."""
    pydot_available = transform_manager._transform_manager.PYDOT_AVAILABLE
    tm = TransformManager()
    try:
        transform_manager._transform_manager.PYDOT_AVAILABLE = False
        with pytest.raises(
            ImportError, match="pydot must be installed to use this feature."
        ):
            tm.write_png("bla")
    finally:
        transform_manager._transform_manager.PYDOT_AVAILABLE = pydot_available


def test_deactivate_transform_manager_precision_error():
    A2B = np.eye(4)
    A2B[0, 0] = 2.0
    A2B[3, 0] = 3.0
    tm = TransformManager()
    with pytest.raises(ValueError, match="Expected rotation matrix"):
        tm.add_transform("A", "B", A2B)

    n_expected_warnings = 6
    try:
        warnings.filterwarnings("always", category=UserWarning)
        with warnings.catch_warnings(record=True) as w:
            tm = TransformManager(strict_check=False)
            tm.add_transform("A", "B", A2B)
            tm.add_transform("B", "C", np.eye(4))
            tm.get_transform("C", "A")
            assert len(w) == n_expected_warnings
    finally:
        warnings.filterwarnings("default", category=UserWarning)


def test_deactivate_checks():
    tm = TransformManager(check=False)
    tm.add_transform("A", "B", np.zeros((4, 4)))
    tm.add_transform("B", "C", np.zeros((4, 4)))
    A2B = tm.get_transform("A", "C")
    assert_array_almost_equal(A2B, np.zeros((4, 4)))


def test_remove_transform():
    tm = TransformManager()
    tm.add_transform("A", "B", np.eye(4))
    tm.add_transform("C", "D", np.eye(4))

    with pytest.raises(KeyError, match="Cannot compute path"):
        tm.get_transform("A", "D")

    tm.add_transform("B", "C", np.eye(4))
    tm.get_transform("A", "C")

    tm.remove_transform("B", "C")
    tm.remove_transform("B", "C")  # nothing should happen
    with pytest.raises(KeyError, match="Cannot compute path"):
        tm.get_transform("A", "D")
    tm.get_transform("B", "A")
    tm.get_transform("D", "C")


def test_from_to_dict():
    rng = np.random.default_rng(2323)
    tm = TransformManager()
    A2B = pt.random_transform(rng)
    tm.add_transform("A", "B", A2B)
    B2C = pt.random_transform(rng)
    tm.add_transform("B", "C", B2C)
    C2D = pt.random_transform(rng)
    tm.add_transform("C", "D", C2D)

    tm_dict = tm.to_dict()
    tm2 = TransformManager.from_dict(tm_dict)
    tm2_dict = tm2.to_dict()

    assert_array_almost_equal(
        tm.get_transform("D", "A"), tm2.get_transform("D", "A")
    )

    assert tm_dict == tm2_dict


def test_remove_twice():
    tm = TransformManager()
    tm.add_transform("a", "b", np.eye(4))
    tm.add_transform("c", "d", np.eye(4))
    tm.remove_transform("a", "b")
    tm.remove_transform("c", "d")


def test_remove_and_add_connection():
    rng = np.random.default_rng(5)
    A2B = pt.random_transform(rng)
    B2C = pt.random_transform(rng)
    C2D = pt.random_transform(rng)
    D2E = pt.random_transform(rng)

    tm = TransformManager()
    tm.add_transform("a", "b", A2B)
    tm.add_transform("b", "c", B2C)
    tm.add_transform("c", "d", C2D)
    tm.add_transform("d", "e", D2E)
    measurement1 = tm.get_transform("a", "e")

    tm.remove_transform("b", "c")
    tm.remove_transform("c", "d")
    tm.add_transform("b", "c", B2C)
    tm.add_transform("c", "d", C2D)
    measurement2 = tm.get_transform("a", "e")

    assert_array_almost_equal(measurement1, measurement2)
