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

import pytest

from ansys.fluent.core import MeshingEvent
from ansys.fluent.core.examples.downloads import download_file


@pytest.mark.nightly
@pytest.mark.fluent_version("latest")
@pytest.mark.codegen_required
def test_launch_pure_meshing(mixing_elbow_watertight_pure_meshing_session):
    pure_meshing_session = mixing_elbow_watertight_pure_meshing_session
    assert pure_meshing_session.is_server_healthy()
    file_name = "launch_pure_meshing_journal.py"
    pure_meshing_session.journal.start(file_name)
    session_dir = dir(pure_meshing_session)
    for attr in ("fields", "meshing", "workflow"):
        assert attr in session_dir
    workflow = pure_meshing_session.workflow
    workflow.TaskObject["Import Geometry"].Execute()

    add_local_sizing = workflow.TaskObject["Add Local Sizing"]
    add_local_sizing.AddChildToTask()
    add_local_sizing.Execute()

    surface_mesh_gen = workflow.TaskObject["Generate the Surface Mesh"]
    surface_mesh_gen.Arguments = {"CFDSurfaceMeshControls": {"MaxSize": 0.3}}
    surface_mesh_gen.Execute()

    describe_geo = workflow.TaskObject["Describe Geometry"]
    describe_geo.UpdateChildTasks(SetupTypeChanged=False)
    describe_geo.Arguments = dict(
        SetupType="The geometry consists of only fluid regions with no voids"
    )
    describe_geo.UpdateChildTasks(SetupTypeChanged=True)
    describe_geo.Execute()

    boundary_update = workflow.TaskObject["Update Boundaries"]
    boundary_update.Arguments = {
        "BoundaryLabelList": ["wall-inlet"],
        "BoundaryLabelTypeList": ["wall"],
        "OldBoundaryLabelList": ["wall-inlet"],
        "OldBoundaryLabelTypeList": ["velocity-inlet"],
    }
    boundary_update.Execute()

    workflow.TaskObject["Update Regions"].Execute()

    add_boundary_layers = workflow.TaskObject["Add Boundary Layers"]
    add_boundary_layers.AddChildToTask()
    add_boundary_layers.InsertCompoundChildTask()
    smooth_transition_1 = workflow.TaskObject["smooth-transition_1"]
    smooth_transition_1.Arguments = {
        "BLControlName": "smooth-transition_1",
    }
    add_boundary_layers.Arguments = {}
    smooth_transition_1.Execute()
    volume_mesh_gen = workflow.TaskObject["Generate the Volume Mesh"]
    volume_mesh_gen.Arguments = {
        "VolumeFill": "poly-hexcore",
        "VolumeFillControls": {
            "HexMaxCellLength": 0.3,
        },
    }
    volume_mesh_gen.Execute()

    pure_meshing_session.journal.stop()
    with pytest.raises(AttributeError):
        pure_meshing_session.switch_to_solver()
    pure_meshing_session.workflow.InitializeWorkflow(WorkflowType="Watertight Geometry")
    geom_name = download_file("mixing_elbow.pmdb", "pyfluent/mixing_elbow")
    pure_meshing_session.workflow.TaskObject["Import Geometry"].Arguments = dict(
        FileName=geom_name, LengthUnit="in"
    )
    pure_meshing_session.tui.file.read_journal(file_name)
    if os.path.exists(file_name):
        os.remove(file_name)


@pytest.mark.fluent_version("latest")
@pytest.mark.codegen_required
def test_launch_meshing_and_switch(new_meshing_session_wo_exit, capsys):
    meshing = new_meshing_session_wo_exit
    assert meshing.is_server_healthy()
    assert meshing.is_active() is True
    capsys.readouterr()
    help(meshing)
    captured = capsys.readouterr()
    assert "Encapsulates a Fluent meshing session." in captured.out
    solver = meshing.switch_to_solver()
    assert meshing.is_active() is False
    for attr in ("tui", "meshing", "workflow", "watertight"):
        with pytest.raises(AttributeError):
            getattr(meshing, attr)
    capsys.readouterr()
    help(meshing)
    captured = capsys.readouterr()
    assert (
        "The meshing session is no longer usable after switching to solution mode."
        in captured.out
    )
    solver.exit()


@pytest.mark.fluent_version("latest")
@pytest.mark.codegen_required
def test_meshing_streaming_and_switch(new_meshing_session_wo_exit):

    def on_case_loaded(session, event_info):
        on_case_loaded.loaded = True

    on_case_loaded.loaded = False

    def on_trancript(transcript):
        on_trancript.called = True

    on_trancript.called = False

    meshing = new_meshing_session_wo_exit

    meshing.events.register_callback(MeshingEvent.CASE_LOADED, on_case_loaded)
    meshing.transcript.register_callback(on_trancript)

    solver = meshing.switch_to_solver()

    on_trancript.called = False

    case_file_name = download_file("mixing_elbow.cas.h5", "pyfluent/mixing_elbow")

    try:
        solver.settings.file.read_case(file_name=case_file_name)
    except AttributeError:
        solver.tui.file.read_case(case_file_name)

    assert not on_trancript.called
    assert not on_case_loaded.loaded
    solver.exit()


@pytest.mark.fluent_version("latest")
@pytest.mark.codegen_required
def test_meshing_no_foreign_objects(new_meshing_session):
    meshing = new_meshing_session
    with pytest.raises(AttributeError):
        meshing.monitors


def test_fake_session():

    class fake_session_base:

        def bar(self):
            pass

    class fake_session(fake_session_base):

        def __init__(self) -> None:
            self._switched = False

        def __getattribute__(self, item: str):
            if item == "_switched":
                return super(fake_session, self).__getattribute__(item)

            if self._switched:
                return None

            return super(fake_session, self).__getattribute__(item)

        def foo(self):
            return 42

    f = fake_session()

    assert f.foo() == 42

    f._switched = True

    assert f.foo is None

    assert f.bar is None
