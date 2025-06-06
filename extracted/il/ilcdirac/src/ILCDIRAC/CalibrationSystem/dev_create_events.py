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
"""Python script to generate 10x100 events for each of the required particles."""
# !/usr/bin/env python

from __future__ import print_function

from __future__ import absolute_import
from six.moves import range
ILCSOFT_DIR = ''


def main():
  """Run the generation process.

  :returns: exit status. 0 on success, 1 on failure
  :rtype: int
  """
  # Form: (particle_name, energy_in_gev), both strings
  particles = [('gamma', '10'), ('mu-', '10'), ('kaon0L', '50')]
  number_of_iterations = 10  # 10 will generate 1000 = 10 x 100 events per particle
  for (particle_name, particle_energy) in particles:
    for i in range(0, number_of_iterations):
      run_script(particle_name, particle_energy, i)
  return 0


def run_script(particle_name, particle_energy, index):
  """Run the script using the passed parameters.

  :param str particle_name: Name of the particle
  :param str particle_energy: Energy of the particle
  :param int index: index of the inner loop, used to index the file
  :returns: None
  :rtype: None
  """
  import subprocess
  res = subprocess.check_output(
      ['ddsim', '--steeringFile', '%s/ClicPerformance/HEAD/examples/clic_steer.py' % ILCSOFT_DIR,
       '--compactFile', ('/cvmfs/clicdp.cern.ch/iLCSoft/builds/2017-02-17/x86_64-slc6-gcc62-opt/lcgeo/HEAD/CLIC/compact'
                         '/CLIC_o3_v08/CLIC_o3_v08.xml'),
       '--enableGun', '--gun.particle', particle_name, '--gun.energy',
       '%s*GeV' % particle_energy, '--gun.distribution', 'uniform',
       '--outputFile', ('/afs/cern.ch/user/j/jebbing/particles/CLIC_o3_v08/%s/%s/event_%d.slcio'
                        % (particle_name, particle_energy, index)),
       '--numberOfEvents', '100'])
  print(res)


if __name__ == '__main__':
  import os
  if 'ILCSOFT' not in os.environ:
    print('Environment variable ILCSOFT not set, please run init_ilcsoft.sh')
    exit(1)
  ILCSOFT_DIR = os.environ['ILCSOFT']

  exit(main())
