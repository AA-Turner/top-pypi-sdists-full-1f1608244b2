import warnings

import numpy as np
import numpy.testing as npt

from dipy.core.sphere_stats import angular_similarity
from dipy.core.subdivide_octahedron import create_unit_sphere
from dipy.data import default_sphere, get_3shell_gtab, get_isbi2013_2shell_gtab
from dipy.direction.peaks import peak_directions
from dipy.reconst.odf import gfa
from dipy.reconst.shm import descoteaux07_legacy_msg, sh_to_sf
from dipy.reconst.shore import ShoreModel, shore_matrix
from dipy.reconst.tests.test_dsi import sticks_and_ball_dummies
from dipy.sims.voxel import sticks_and_ball
from dipy.testing.decorators import set_random_number_generator


def test_shore_odf():
    gtab = get_isbi2013_2shell_gtab()

    # load repulsion 724 sphere
    sphere = default_sphere

    # load icosahedron sphere
    sphere2 = create_unit_sphere(recursion_level=5)
    data, golden_directions = sticks_and_ball(
        gtab, d=0.0015, S0=100, angles=[(0, 0), (90, 0)], fractions=[50, 50], snr=None
    )
    asm = ShoreModel(gtab, radial_order=6, zeta=700, lambdaN=1e-8, lambdaL=1e-8)
    # repulsion724
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            message=descoteaux07_legacy_msg,
            category=PendingDeprecationWarning,
        )
        asmfit = asm.fit(data)
        odf = asmfit.odf(sphere)
    odf_sh = asmfit.odf_sh()
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            message=descoteaux07_legacy_msg,
            category=PendingDeprecationWarning,
        )
        odf_from_sh = sh_to_sf(
            odf_sh, sphere, sh_order_max=6, basis_type=None, legacy=True
        )
    npt.assert_almost_equal(odf, odf_from_sh, 10)

    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            message=descoteaux07_legacy_msg,
            category=PendingDeprecationWarning,
        )
        expected_phi = shore_matrix(radial_order=6, zeta=700, gtab=gtab)
    npt.assert_array_almost_equal(
        np.dot(expected_phi, asmfit.shore_coeff), asmfit.fitted_signal()
    )

    directions, _, _ = peak_directions(
        odf, sphere, relative_peak_threshold=0.35, min_separation_angle=25
    )
    npt.assert_equal(len(directions), 2)
    npt.assert_almost_equal(angular_similarity(directions, golden_directions), 2, 1)

    # 5 subdivisions
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            message=descoteaux07_legacy_msg,
            category=PendingDeprecationWarning,
        )
        odf = asmfit.odf(sphere2)
    directions, _, _ = peak_directions(
        odf, sphere2, relative_peak_threshold=0.35, min_separation_angle=25
    )
    npt.assert_equal(len(directions), 2)
    npt.assert_almost_equal(angular_similarity(directions, golden_directions), 2, 1)

    sb_dummies = sticks_and_ball_dummies(gtab)
    for sbd in sb_dummies:
        data, golden_directions = sb_dummies[sbd]
        asmfit = asm.fit(data)
        odf = asmfit.odf(sphere2)
        directions, _, _ = peak_directions(
            odf, sphere2, relative_peak_threshold=0.35, min_separation_angle=25
        )
        if len(directions) <= 3:
            npt.assert_equal(len(directions), len(golden_directions))
        if len(directions) > 3:
            npt.assert_equal(gfa(odf) < 0.1, True)


@set_random_number_generator()
def test_multivox_shore(rng):
    gtab = get_3shell_gtab()

    data = rng.random([20, 30, 1, gtab.gradients.shape[0]])
    radial_order = 4
    zeta = 700
    asm = ShoreModel(
        gtab, radial_order=radial_order, zeta=zeta, lambdaN=1e-8, lambdaL=1e-8
    )
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            message=descoteaux07_legacy_msg,
            category=PendingDeprecationWarning,
        )
        asmfit = asm.fit(data)
    c_shore = asmfit.shore_coeff
    npt.assert_equal(c_shore.shape[0:3], data.shape[0:3])
    npt.assert_equal(np.all(np.isreal(c_shore)), True)
