#
# Copyright (c) 2009-2022 CERN. All rights nots expressly granted are
# reserved.
#
# This file is part of iLCDirac
# (see ilcdirac.cern.ch, contact: ilcdirac-support@cern.ch).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# In applying this licence, CERN does not waive the privileges and
# immunities granted to it by virtue of its status as an
# Intergovernmental Organization or submit itself to any jurisdiction.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
"""unit tests for resolvePathsAndNames module."""

from __future__ import print_function
from __future__ import absolute_import
import unittest
import os
import tempfile
import shutil

from parameterized import parameterized, param

from ILCDIRAC.Core.Utilities.resolvePathsAndNames import getProdFilename, resolveIFpaths, getProdFilenameFromInput


class ResolvePathsAndNamesTests(unittest.TestCase):
  """Test resolvePathsAndNames."""

  def setUp(self):
    """Make fake files for the test."""
    self.inputfiles = ["toto_gen_12345_123.txt"]
    self.orgDir = os.getcwd()
    self.tempDir = tempfile.mkdtemp(dir=os.getcwd())
    os.chdir(self.tempDir)
    tempDir2 = tempfile.mkdtemp(dir=os.getcwd())
    self.realloc = os.path.join(tempDir2, 'toto_gen_12345_123.txt')
    with open(self.realloc, "w") as inputf:
      inputf.write("fake file")

  def tearDown(self):
    """Remove the fake files."""
    os.chdir(self.orgDir)
    try:
      shutil.rmtree(self.tempDir)
    except OSError:
      print('Failed to remove tempDir')

  def test_getnames(self):
    """test ResolvePathsAndNames getNames..........................................................."""
    res = getProdFilename("toto_gen.stdhep", 12345, 123)
    self.assertEqual(res, 'toto_gen_12345_123.stdhep')

  @parameterized.expand([
      param([]),
      param(['']),
      param(['noSuchFile'], ok=False),
      param(['suchFile'], createFile=True),
      ])
  def test_resolvepaths(self, extraInputs, ok=True, createFile=False):
    """test ResolvePathsAndNames resolvePaths......................................................."""
    extraPaths = []
    if createFile:
      tempfile.mkdtemp(dir=os.getcwd())  # create another empty folder for one path in the function
      for fileName in extraInputs:
        fullPath = os.path.join(self.tempDir, fileName)
        extraPaths.append(fullPath)
        with open(fullPath, 'w') as aFile:
          aFile.write(fullPath)
    res = resolveIFpaths(self.inputfiles + extraInputs)
    assert 'OK' in res
    assert res['OK'] == ok, res
    if ok:
      self.assertTrue('Value' in res, list(res.keys()))
      self.assertEqual(res['Value'], [os.path.abspath(self.realloc)] + extraPaths)

  def test_ildprod_sim(self):
    """test getOridFilenameFromInput Sim ..........................................................."""
    indir = "/ilc/prod/ilc/ild/test/temp1/gensplit/500-TDR_ws/3f/run001/"
    outdir = "/ilc/prod/ilc/test/ild/sim/500-TDR_ws/3f/ILD_o1_v05/v01-19_lcgeo/00001234/000/"
    input_file = indir + "E0500-TDR_ws.Pae_ell.Gwhizard-1.95.eW.pL.I37537.01_002.stdhep"
    outfile_original = outdir + "sv01-19_lcgeo.mILD_o1_v05.E500-TDR_ws_sim_400859_4.slcio"
    prodid = 1234
    jobid = 321
    outfile_new = outdir + "sv01-19_lcgeo.mILD_o1_v05.E500-TDR_ws.I37537.Pae_ell.eW.pL.n01_002.d_sim_00001234_321.slcio"
    out_lfn = getProdFilenameFromInput(input_file, outfile_original, prodid, jobid)
    self.assertEqual(out_lfn, outfile_new)

  def test_ildprod_rec(self):
    """test getProdFilenameFromInput Rec ..........................................................."""
    indir = "/ilc/prod/ilc/test/ild/sim/500-TDR_ws/3f/ILD_o1_v05/v01-19_lcgeo/00001234/000/"
    outdir = "/ilc/prod/ilc/test/ild/rec/500-TDR_ws/3f/ILD_o1_v05/v01-19_lcgeo/00001235/000/"
    input_file = indir + "sv01-19_lcgeo.mILD_o1_v05.E500-TDR_ws.I37540.Pae_ell.eB.pR.n01_002.d_sim_00001234_12.slcio"  # LFN
    outfile_original = outdir + "rv01-19_lcgeo.sv01-19_lcgeo.mILD_o1_v05.E500-TDR_ws_rec_1235_321.slcio"
    prodid = 1235
    jobid = 321
    outfile_new = outdir + "rv01-19_lcgeo.sv01-19_lcgeo.mILD_o1_v05.E500-TDR_ws.I37540.Pae_ell.eB.pR.n01_002.d_rec_00001235_321.slcio"
    out_lfn = getProdFilenameFromInput(input_file, outfile_original, prodid, jobid)
    self.assertEqual(out_lfn, outfile_new)

  def test_ildprod_rec_mcopt(self):
    """test getProdFilenameFromInput Rec, when sim model and rec model is different.........................."""
    indir = "/ilc/prod/ilc/mc-opt/ild/sim/500-TDR_ws/3f/ILD_l5_v02/v01-19-05/00001234/000/"
    outdir = "/ilc/prod/ilc/mc-opt/ild/rec/500-TDR_ws/3f/ILD_l5_o1_v02/v01-19-05/00001235/000/"
    input_file = indir + "sv01-19-05.mILD_l5_v02.E500-TDR_ws.I37540.Pae_ell.eB.pR.n01_002.d_sim_00001234_62.slcio"  # LFN
    outfile_original = outdir + "rv01-19-05.sv01-19-05.mILD_l5_o1_v02.E500-TDR_ws_rec_1235_421.slcio"
    prodid = 1235
    jobid = 421
    outfile_new = outdir + "rv01-19-05.sv01-19-05.mILD_l5_o1_v02.E500-TDR_ws.I37540.Pae_ell.eB.pR.n01_002.d_rec_00001235_421.slcio"
    out_lfn = getProdFilenameFromInput(input_file, outfile_original, prodid, jobid)
    self.assertEqual(out_lfn, outfile_new)

  def test_ildprod_dbdrec(self):
    """test getProdFilenameFromInput Rec for DBD Sim data .........................................."""
    indir = "/ilc/prod/ilc/mc-dbd/ild/sim/250-TDR_ws/4f_WW_semileptonic/ILD_o1_v05/v01-14-01-p00/"
    outdir = "/ilc/prod/ilc/mc-dbd/ild/250-TDR_ws/4f_WW_semileptonic/ILD_o1_v05/v01-16-02-p01/00001235/000/"
    input_file = indir + "sv01-14-01-p00.mILD_o1_v05.E250-TDR_ws.I106577.P4f_ww_sl.eL.pR-01935.slcio"  # LFN
    outfile_original = outdir + "rv01-16-01-p01.sv01-14-01-p00.mILD_o1_v05.E250-TDR_ws_rec_1235_783.slcio"
    prodid = 1235
    jobid = 783
    outfile_new = outdir + "rv01-16-01-p01.sv01-14-01-p00.mILD_o1_v05.E250-TDR_ws.I106577.P4f_ww_sl.eL.pR.n01935.d_rec_00001235_783.slcio"
    out_lfn = getProdFilenameFromInput(input_file, outfile_original, prodid, jobid)
    self.assertEqual(out_lfn, outfile_new)

  def test_ildprod_dst(self):
    """test getProdFilenameFromInput DST ..........................................................."""
    indir = "/ilc/prod/ilc/test/ild/sim/500-TDR_ws/3f/ILD_o1_v05/v01-19_lcgeo/00001234/000/"
    outdir = "/ilc/prod/ilc/test/ild/dst/500-TDR_ws/3f/ILD_o1_v05/v01-19_lcgeo/00001235/000/"
    input_file = indir + "sv01-19_lcgeo.mILD_o1_v05.E500-TDR_ws.I37540.Pae_ell.eB.pR.n01_002.d_sim_00001234_12.slcio"  # LFN
    outfile_original = outdir + "rv01-19_lcgeo.sv01-19_lcgeo.mILD_o1_v05.E500-TDR_ws_dst_00001235_321.slcio"
    prodid = 1235
    jobid = 321
    outfile_new = outdir + "rv01-19_lcgeo.sv01-19_lcgeo.mILD_o1_v05.E500-TDR_ws.I37540.Pae_ell.eB.pR.n01_002.d_dst_00001235_321.slcio"
    out_lfn = getProdFilenameFromInput(input_file, outfile_original, prodid, jobid)
    self.assertEqual(out_lfn, outfile_new)

  def test_ildprod_stdhepsplit(self):
    """test getProdFilenameFromInput Generator stdhep  ..........................................................."""
    indir = "/ilc/prod/ilc/mc-dbd/generated/500-TDR_ws/higgs/"
    outdir = "/ilc/prod/ilc/ild/test/temp1/mc-dbd.disk/ild/splitted/500-TDR_ws/higgs_ffh/00400922/000/"
    input_file = indir + "E500-TDR_ws.Pqqh_ww_4q.Gwhizard-1_95.eL.pR.I106730.001.stdhep"
    outfile_original = outdir + "E500-TDR_ws.I106730.Pqqh_ww_4q.eL.pR_gen_400922_1_035.stdhep"
    prodid = 400922
    jobid = 87
    outfile_new = outdir + "E500-TDR_ws.Pqqh_ww_4q.Gwhizard-1_95.eL.pR.I106730.n001_035.d_gen_00400922_87.stdhep"
    out_lfn = getProdFilenameFromInput(input_file, outfile_original, prodid, jobid)
    self.assertEqual(out_lfn, outfile_new)

  def test_ildprod_stdhepsplit2(self):
    """test getProdFilenameFromInput Generator stdhep 2..........................................................."""
    indir = "/ilc/prod/ilc/mc-dbd/generated/500-TDR_ws/4f/"
    outdir = "/ilc/prod/ilc/ild/test/temp1/mc-dbd.generated/ild/splitted/500-TDR_ws/4f/00008147/000/"
    input_file = indir + "E500-TDR_ws.P4f_zz_sl.Gwhizard-1_95.eL.pR.I250014.031.stdhep"
    outfile_original = outdir + "E500-TDR_ws_gen_8147_1_012.stdhep"
    prodid = 8147
    jobid = 87
    outfile_new = outdir + "E500-TDR_ws.P4f_zz_sl.Gwhizard-1_95.eL.pR.I250014.n031_012.d_gen_00008147_87.stdhep"
    out_lfn = getProdFilenameFromInput(input_file, outfile_original, prodid, jobid)
    self.assertEqual(out_lfn, outfile_new)

  def test_ildprod_stdhepsplit3(self):
    """test getProdFilenameFromInput Generator stdhep 3..........................................................."""
    indir = "/ilc/prod/ilc/mc-dbd/generated/500-TDR_ws/4f/"
    outdir = "/ilc/prod/ilc/ild/test/temp1/mc-dbd.generated/ild/splitted/500-TDR_ws/4f/00008147/000/"
    input_file = indir + "E500-TDR_ws.P4f_zz_sl.Gwhizard-1_95.eR.pL.I250016.004.stdhep"
    outfile_original = outdir + "E500-TDR_ws_gen_8147_2_065.stdhep"
    prodid = 8147
    jobid = 125
    outfile_new = outdir + "E500-TDR_ws.P4f_zz_sl.Gwhizard-1_95.eR.pL.I250016.n004_065.d_gen_00008147_125.stdhep"
    out_lfn = getProdFilenameFromInput(input_file, outfile_original, prodid, jobid)
    self.assertEqual(out_lfn, outfile_new)

  def test_ildprod_stdhepsplit_slcio(self):
    """test getProdFilenameFromInput Generator slcio  ..........................................................."""
    indir = "/ilc/prod/ilc/mc-dbd/generated/500-TDR_ws/4f/"
    outdir = "/ilc/prod/ilc/ild/test/temp1/mc-dbd.generated/ild/splitted/500-TDR_ws/4f/00008147/000/"
    input_file = indir + "E500-TDR_ws.P4f_zz_sl.Gwhizard-1_95.eR.pL.I250016.004.slcio"
    outfile_original = outdir + "E500-TDR_ws_gen_8147_2_065.slcio"
    prodid = 8147
    jobid = 125
    outfile_new = outdir + "E500-TDR_ws.P4f_zz_sl.Gwhizard-1_95.eR.pL.I250016.n004_065.d_gen_00008147_125.slcio"
    out_lfn = getProdFilenameFromInput(input_file, outfile_original, prodid, jobid)
    self.assertEqual(out_lfn, outfile_new)

  def test_ildprod_undef_format(self):
    """test getProdFilenameFromInput Undefined file name ( 1st caharacter is not "E", nor "s" nor "r" .........."""
    indir = "/ilc/user/a/amiyamot/mygen/single_particles/jeans/"
    outdir = "/ilc/user/a/amiyamot/splitted/single_particles/jeans/"
    input_file = indir + "mcparticles_PDG130_MOM20GeV.slcio"
    outfile_original = outdir + "mcparticles_PDG130_MOM20GeV_gen_11520_1_093.slcio"
    prodid = 11520
    jobid = 93
    outfile_new = outdir + "mcparticles_PDG130_MOM20GeV_gen_11520_1_093.slcio"
    out_lfn = getProdFilenameFromInput(input_file, outfile_original, prodid, jobid)
    self.assertEqual(out_lfn, outfile_new)


if __name__ == "__main__":
  SUITE = unittest.defaultTestLoader.loadTestsFromTestCase(ResolvePathsAndNamesTests)
  TESTRESULT = unittest.TextTestRunner(verbosity=2).run(SUITE)
