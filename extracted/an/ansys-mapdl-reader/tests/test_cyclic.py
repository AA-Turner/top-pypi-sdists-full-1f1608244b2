# Copyright (C) 2021 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import platform
import sys

import numpy as np
import pytest
import pyvista as pv
from pyvista.plotting import system_supports_plotting
from pyvista.plotting.renderer import CameraPosition
from vtkmodules.vtkCommonMath import vtkMatrix4x4

from ansys.mapdl import reader as pymapdl_reader
from ansys.mapdl.reader import examples
from ansys.mapdl.reader.cyclic_reader import CyclicResult

HAS_FFMPEG = True
try:
    import imageio_ffmpeg  # noqa: F401
except:
    HAS_FFMPEG = False


path = os.path.dirname(os.path.abspath(__file__))
testfiles_path = os.path.join(path, "testfiles")
cyclic_testfiles_path = os.path.join(path, "cyclic_reader")
cys12_path = os.path.join(testfiles_path, "cyc12")
academic_path = os.path.join(cyclic_testfiles_path, "academic_rotor")

# modal result z axis
try:
    result_z = examples.download_sector_modal()
    result_z.positive_cyclic_dir = True
except:
    result_z = None

IS_MAC = platform.system() == "Darwin"
skip_plotting = pytest.mark.skipif(
    not system_supports_plotting() or IS_MAC or sys.version_info >= (3, 13),
    reason="Plotting disabled for these tests",
)

skip_windows = pytest.mark.skipif(
    os.name == "nt", reason="Test fails due to OSMESA on Windows"
)


# static result x axis
@pytest.fixture(scope="module")
def academic_rotor():
    filename = os.path.join(academic_path, "academic_rotor.rst")
    return CyclicResult(filename)


# static result x axis
@pytest.fixture(scope="module")
def result_x():
    filename = os.path.join(testfiles_path, "cyc12.rst")
    return pymapdl_reader.read_binary(filename)


@pytest.fixture(scope="module")
def cyclic_v182_z():
    # static result z axis
    filename = os.path.join(cyclic_testfiles_path, "cyclic_v182.rst")
    return pymapdl_reader.read_binary(filename)


@pytest.fixture(scope="module")
def cyclic_v182_z_with_comp():
    # cyclic modal with component
    filename = os.path.join(cyclic_testfiles_path, "cyclic_v182_w_comp.rst")
    return pymapdl_reader.read_binary(filename)


@pytest.mark.parametrize("rtype", ["S", "EPEL", "S,PRIN"])
@pytest.mark.parametrize("load_step", [1, 2, 5, 13])  # fortran indexing
@pytest.mark.parametrize("sub_step", [1, 2])  # fortran indexing
def test_nodal_cyclic_modal(academic_rotor, load_step, sub_step, rtype):
    rnum = (load_step, sub_step)
    filename = "SET%d,%d_RSYS0_%s.npz" % (rnum[0], rnum[1], rtype)
    ans = np.load(os.path.join(academic_path, filename))
    nnum_ans = ans["nnum"]
    stress_ans = ans["data"]

    if rtype == "S":
        nnum, stress = academic_rotor.nodal_stress(rnum, full_rotor=True)
    elif rtype == "EPEL":
        nnum, stress = academic_rotor.nodal_elastic_strain(rnum, full_rotor=True)
    elif rtype == "S,PRIN":
        nnum, stress = academic_rotor.principal_nodal_stress(rnum, full_rotor=True)
    else:
        raise ValueError("rtype %s not configured in test" % rtype)

    # ANSYS doesn't include results for all nodes (i.e. sector nodes)
    mask = np.in1d(nnum, nnum_ans)
    stress = stress[:, mask, :6]  # pymapdl_reader strain includes eqv
    nnum = nnum[mask]
    assert np.allclose(nnum, nnum_ans)

    # ANSYS will not average across geometric discontinuities, pymapdl_reader
    # always does.  These 10 nodes are along the blade/sector interface
    dmask = np.ones(stress[0].shape[0], np.bool_)
    dmask[[99, 111, 115, 116, 117, 135, 142, 146, 147, 148]] = False

    # large atol due to the float32 encoding of the stress
    assert np.allclose(stress[:, dmask], stress_ans[:, dmask], atol=1)

    # pdiff = (strain[:, dmask] - strain_ans[:, dmask])/strain[:, dmask]
    # np.abs(pdiff).max()
    # this number is small (approx 0.0002%)

    # verify we can get complex results
    nnum, stress = academic_rotor.principal_nodal_stress(
        rnum,
        as_complex=False,
    )
    nnum_com, stress_com = academic_rotor.principal_nodal_stress(
        rnum,
        as_complex=True,
    )
    assert np.allclose(np.real(stress_com), stress)
    assert np.allclose(nnum, nnum_com)

    with pytest.raises(ValueError, match="cannot both be True"):
        academic_rotor.principal_nodal_stress(rnum, as_complex=True, full_rotor=True)


def test_non_cyclic():
    with pytest.raises(TypeError):
        CyclicResult(examples.rstfile)


@skip_windows
@skip_plotting
@pytest.mark.skipif(result_z is None, reason="Requires result file")
def test_plot_sectors(tmpdir):
    filename = str(tmpdir.mkdir("tmpdir").join("tmp.png"))
    cpos = result_z.plot_sectors(screenshot=filename)
    if cpos is not None:
        assert isinstance(cpos, CameraPosition)
    assert os.path.isfile(filename)


@skip_windows
@skip_plotting
def test_plot_sectors_x(result_x):
    cpos = result_x.plot_sectors()
    if cpos is not None:
        assert isinstance(cpos, CameraPosition)


@skip_windows
@skip_plotting
@pytest.mark.skipif(result_z is None, reason="Requires result file")
def test_plot_z_cyc():
    cpos = result_z.plot()
    if cpos is not None:
        assert isinstance(cpos, CameraPosition)


@skip_windows
@skip_plotting
def test_plot_x_cyc(result_x):
    cpos = result_x.plot()
    if cpos is not None:
        assert isinstance(cpos, CameraPosition)


@skip_windows
@skip_plotting
def test_plot_component_rotor(cyclic_v182_z_with_comp):
    cyclic_v182_z_with_comp.plot_nodal_solution(
        0, full_rotor=False, node_components="REFINE", sel_type_all=False
    )

    cyclic_v182_z_with_comp.plot_nodal_solution(
        0, full_rotor=True, node_components="REFINE", sel_type_all=False
    )

    # result_z.plot_nodal_stress(20, 'Sx', node_components='REFINE',
    #                            sel_type_all=False, off_screen=True)

    # result.plot_principal_nodal_stress(20, 'SEQV',
    #                                    node_components='REFINE',
    #                                    sel_type_all=False,
    #                                    off_screen=True)


def test_element_stress_v182_non_cyclic():
    """
    Generated ansys results with:
    ansys.Post1()
    ansys.Set(1, 1)
    ansys.Header('OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF')
    ansys.Format('', 'E', 80, 20)
    ansys.Page(1E9, '', -1)

    msg = ansys.Presol('S').splitlines()
    ansys_element_stress = []
    for line in msg:
        if len(line) == 201:
            ansys_element_stress.append(line)
    ansys_element_stress = np.genfromtxt(ansys_element_stress)
    ansys_enode = ansys_element_stress[:, 0].astype(np.int_)
    ansys_element_stress = ansys_element_stress[:, 1:]

    """
    ansys_result_file = os.path.join(cyclic_testfiles_path, "cyclic_v182.rst")
    result = pymapdl_reader.read_binary(ansys_result_file)

    elemnum, element_stress, enode = result.element_stress(0, False, False)
    assert np.allclose(np.sort(elemnum), elemnum), "elemnum must be sorted"

    element_stress = np.vstack(element_stress)
    enode = np.hstack(enode)

    # cyclic model will only output the master sector
    from_ansys = np.load(os.path.join(cyclic_testfiles_path, "v182_presol.npz"))
    assert np.allclose(from_ansys["enode"], enode)
    assert np.allclose(from_ansys["element_stress"], element_stress)


def test_nodal_stress_v182_non_cyclic():
    """
    Generated with:
    msg = ansys.Prnsol('s').splitlines()
    array = np.genfromtxt(msg[9:])
    ansys_nnum = array[:, 0].astype(np.int_)
    ansys_stress = array[:, 1:]
    """
    ansys_result_file = os.path.join(cyclic_testfiles_path, "cyclic_v182.rst")
    result = pymapdl_reader.rst.Result(ansys_result_file, ignore_cyclic=True)
    nnum, stress = result.nodal_stress(0)

    from_ansys = np.load(os.path.join(cyclic_testfiles_path, "v182_prnsol_s.npz"))
    assert np.allclose(from_ansys["nnum"][: nnum.size], nnum)
    assert np.allclose(from_ansys["stress"][: nnum.size], stress)


def test_full_x_nodal_solution(result_x):
    """need to open gui to output full rotor results"""
    from_ansys = np.load(
        os.path.join(cyclic_testfiles_path, "prnsol_d_cyclic_x_full_v182.npz")
    )

    ansys_nnum = from_ansys["nnum"]
    ansys_disp = from_ansys["disp"]

    rnum = 0
    nnum, disp = result_x.nodal_solution(
        rnum, phase=0, full_rotor=True, as_complex=False
    )

    assert np.allclose(np.sort(nnum), nnum), "nnum must be sorted"

    mask = np.in1d(nnum, ansys_nnum)
    n = mask.sum()
    tmp = ansys_disp.reshape(disp.shape[0], n, 3)
    assert np.allclose(nnum[mask], ansys_nnum[:n])
    assert np.allclose(disp[:, mask], tmp)

    nnum_alt, disp_alt = result_x.nodal_displacement(
        rnum, phase=0, full_rotor=True, as_complex=False
    )

    assert np.allclose(nnum_alt, nnum)
    assert np.allclose(disp_alt, disp)


def test_full_z_nodal_solution(cyclic_v182_z):
    """need to open gui to output full rotor results"""
    from_ansys = np.load(
        os.path.join(cyclic_testfiles_path, "prnsol_d_cyclic_z_full_v182.npz")
    )

    ansys_nnum = from_ansys["nnum"]
    ansys_disp = from_ansys["disp"]

    rnum = 0
    phase = 0
    nnum, disp = cyclic_v182_z.nodal_solution(
        rnum, phase, full_rotor=True, as_complex=False
    )

    mask = np.in1d(nnum, ansys_nnum)
    n = mask.sum()
    tmp = ansys_disp.reshape(disp.shape[0], n, 3)
    assert np.allclose(disp[:, mask], tmp)


def test_full_z_nodal_solution_phase(cyclic_v182_z):
    """need to open gui to output full rotor results"""
    from_ansys = np.load(
        os.path.join(cyclic_testfiles_path, "prnsol_d_cyclic_z_full_v182.npz")
    )

    ansys_nnum = from_ansys["nnum"]
    ansys_disp = from_ansys["disp"]

    rnum = 0
    phase = 0
    nnum, disp = cyclic_v182_z.nodal_solution(
        rnum, phase, full_rotor=True, as_complex=True
    )

    mask = np.in1d(nnum, ansys_nnum)
    n = mask.sum()
    tmp = ansys_disp.reshape(disp.shape[0], n, 3)
    assert np.allclose(disp[:, mask], tmp)


@skip_windows
@skip_plotting
def test_full_x_nodal_solution_plot(result_x):
    result_x.plot_nodal_solution(0)


def test_full_x_nodal_stress(result_x):
    """need to open gui to output full rotor results"""
    from_ansys = np.load(
        os.path.join(cyclic_testfiles_path, "prnsol_s_cyclic_x_full_v182.npz")
    )
    ansys_nnum = from_ansys["nnum"]
    ansys_stress = from_ansys["stress"]

    rnum = 0
    phase = 0
    nnum, stress = result_x.nodal_stress(rnum, phase, full_rotor=True)

    mask = np.in1d(nnum, ansys_nnum)
    n = mask.sum()
    tmp = ansys_stress.reshape(stress.shape[0], n, 6)

    np.abs(stress[:, mask] - tmp)

    assert np.allclose(stress[:, mask], tmp)
    assert np.allclose(nnum[mask], ansys_nnum[:n])


def test_mode_table(cyclic_v182_z, result_x):
    assert isinstance(cyclic_v182_z.mode_table, np.ndarray)
    assert isinstance(result_x.mode_table, np.ndarray)


@pytest.mark.skipif(result_z is None, reason="Requires result file")
def test_mode_table_result_z():
    assert isinstance(result_z.mode_table, np.ndarray)


@pytest.mark.skipif(result_z is None, reason="Requires result file")
def test_harmonic_index_to_cumulative():
    # harmonic_index_to_cumulative
    assert result_z.harmonic_index_to_cumulative(0, 0) == 0
    assert result_z.harmonic_index_to_cumulative(1, 0) == 6
    assert result_z.harmonic_index_to_cumulative(-7, 2) == 47

    with pytest.raises(Exception):
        result_z.harmonic_index_to_cumulative(10, 0)

    with pytest.raises(Exception):
        result_z.harmonic_index_to_cumulative(0, 6)


def test_full_x_principal_nodal_stress(result_x):
    """need to open gui to output full rotor results"""
    from_ansys = np.load(
        os.path.join(cyclic_testfiles_path, "prnsol_p_cyclic_x_full_v182.npz")
    )
    ansys_nnum = from_ansys["nnum"]
    ansys_stress = from_ansys["stress"]

    rnum = 0
    phase = 0
    nnum, stress = result_x.principal_nodal_stress(rnum, phase, full_rotor=True)

    mask = np.in1d(nnum, ansys_nnum)
    n = mask.sum()
    tmp = ansys_stress.reshape(stress.shape[0], n, 5)

    assert np.allclose(nnum[mask], ansys_nnum[:n])
    assert np.allclose(stress[:, mask], tmp, atol=4e-3)  # too loose


@skip_windows
@skip_plotting
@pytest.mark.skipif(not HAS_FFMPEG, reason="requires imageio_ffmpeg")
@pytest.mark.skipif(result_z is None, reason="Requires result file")
def test_animate_nodal_solution(tmpdir):
    temp_movie = str(tmpdir.mkdir("tmpdir").join("tmp.mp4"))
    result_z.animate_nodal_solution(
        0, n_frames=20, movie_filename=temp_movie, loop=False
    )
    assert os.path.isfile(temp_movie)


@pytest.mark.skipif(result_z is None, reason="Requires result file")
def test_cyclic_z_harmonic_displacement():
    from_ansys = np.load(
        os.path.join(cyclic_testfiles_path, "prnsol_u_cyclic_z_full_v182_set_4_2.npz")
    )
    ansys_nnum = from_ansys["nnum"]
    ansys_disp = from_ansys["disp"]

    unod, count = np.unique(ansys_nnum, return_counts=True)
    unod = np.setdiff1d(unod[count == result_z.n_sector], 32)
    mask = np.in1d(ansys_nnum, unod)
    ansys_nnum = ansys_nnum[mask]
    ansys_disp = ansys_disp[mask]

    nnum, disp = result_z.nodal_solution((4, 2), full_rotor=True)
    mask = np.in1d(nnum, ansys_nnum)
    tmp = ansys_disp.reshape(disp.shape[0], mask.sum(), 3)
    assert np.allclose(disp[:, mask], tmp, atol=1e-5)


@skip_windows
@skip_plotting
def test_plot_nodal_stress(result_x):
    result_x.plot_nodal_stress(0, "z")


@skip_windows
@skip_plotting
def test_plot_nodal_stress(result_x):
    result_x.plot_nodal_stress(0, "z")


@skip_windows
@skip_plotting
def test_plot_principal_nodal_stress(result_x):
    result_x.plot_principal_nodal_stress(0, "seqv")


def test_nodal_elastic_strain_cyclic(result_x):
    from_mapdl = np.load(os.path.join(cys12_path, "RSYS0_ROTOR_PRNSOL_EPEL.npz"))
    nnum_ans = from_mapdl["nnum"]
    stress_ans = from_mapdl["stress"]

    # get EPEL
    nnum, stress = result_x.nodal_elastic_strain(0, full_rotor=True)

    # include only common values
    mask = np.in1d(nnum, nnum_ans[0])
    stress = stress[:, mask, :6]  # stress includes eqv
    nnum = nnum[mask]
    assert np.allclose(nnum, nnum_ans)
    assert np.allclose(stress, stress_ans)


@skip_windows
@skip_plotting
def test_plot_nodal_elastic_strain(result_x):
    result_x.plot_nodal_elastic_strain(0, "X")


def test_nodal_temperature(result_x):
    from_mapdl = np.load(os.path.join(cys12_path, "RSYS0_ROTOR_PRNSOL_BFE.npz"))
    nnum_ans = from_mapdl["nnum"]
    temp_ans = from_mapdl["temp"]

    nnum, temp = result_x.nodal_temperature(0)

    # include only common values
    assert np.allclose(nnum, nnum_ans)

    # ignore nans from Ansys.  Reader now gets results for midside
    # nodes, cached results contain only edge
    mask = ~np.isnan(temp_ans[0])
    assert np.allclose(temp[mask], temp_ans[:, mask], equal_nan=True)


@skip_windows
@skip_plotting
def test_plot_nodal_nodal_temperature(result_x):
    result_x.plot_nodal_temperature(0)


def test_nodal_thermal_strain_cyclic(result_x):
    from_mapdl = np.load(os.path.join(cys12_path, "RSYS0_ROTOR_PRNSOL_EPTH_COMP.npz"))
    nnum_ans = from_mapdl["nnum"]
    strain_ans = from_mapdl["strain"]

    nnum, strain = result_x.nodal_thermal_strain(0, full_rotor=True)

    # include only common values
    mask = np.in1d(nnum, nnum_ans)
    strain = strain[:, mask, :6]  # strain includes eqv
    nnum = nnum[mask]
    assert np.allclose(nnum, nnum_ans)
    assert np.allclose(strain, strain_ans)


@skip_windows
@skip_plotting
def test_plot_nodal_thermal_strain(result_x):
    result_x.plot_nodal_thermal_strain(0, "X")


def test_cs_4x4(result_x):
    assert isinstance(result_x._c_systems, dict)

    # expect first CSYS to be cartesian
    assert np.allclose(result_x.cs_4x4(1), np.eye(4))
    assert isinstance(result_x.cs_4x4(1, as_vtk_matrix=True), vtkMatrix4x4)


@skip_plotting
def test_animate_academic(academic_rotor):
    _ = academic_rotor.animate_nodal_displacement(
        (3, 2),
        displacement_factor=0.03,
        n_frames=30,
        n_colors=128,
        show_axes=False,
        background="w",
        loop=False,
        add_text=False,
        show_scalar_bar=False,
    )


def test_save_as_vtk(academic_rotor, tmpdir):
    filename = tmpdir.mkdir("tmpdir").join("tmp.vtk")
    academic_rotor.save_as_vtk(filename, merge_sectors=False)
    grid = pv.read(filename)

    # verify for nodal diameter 0

    _, disp = academic_rotor.nodal_solution((1, 1), full_rotor=True)
    np.allclose(grid["Nodal solution (0, 0)"], np.vstack(disp))

    _, stress = academic_rotor.nodal_stress((1, 1), full_rotor=True)
    np.allclose(grid["Nodal stresses (0, 0)"], np.vstack(stress))

    # verify for nodal diameter 2

    _, disp = academic_rotor.nodal_solution((3, 1), full_rotor=True)
    np.allclose(grid["Nodal solution (0, -2)"], np.vstack(disp))

    _, stress = academic_rotor.nodal_stress((3, 1), full_rotor=True)
    np.allclose(grid["Nodal stresses (0, -2)"], np.vstack(stress))

    # verify sectors are isolated
    assert len(grid.split_bodies()) == academic_rotor.n_sector

    # merge, save, and read back in
    academic_rotor.save_as_vtk(filename, merge_sectors=True, progress_bar=False)
    grid = pv.read(filename)

    # verify sectors are not isolated
    assert len(grid.split_bodies()) == 1
