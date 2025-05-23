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
"""This module contains the definition of the different applications that can be used to create jobs.

Example usage:

>>> from ILCDIRAC.Interfaces.API.NewInterface.Applications import *
>>> from ILCDIRAC.Interfaces.API.NewInterface.UserJob import *
>>> from ILCDIRAC.Interfaces.API.DiracILC import DiracILC
>>> dirac = DiracILC()
>>> job = UserJob()
>>> ga = GenericApplication()
>>> ga.setScript("myscript.py")
>>> ga.setArguments("some arguments")
>>> ga.setDependency({"mokka":"v0706P08","marlin":"v0111Prod"})
>>> job.append(ga)
>>> job.submit(dirac)

It's also possible to set all the application's properties in the constructor

>>> ga = GenericApplication({"Script":"myscript.py", "Arguments":"some arguments", \
         "Dependency":{"mokka":"v0706P08","marlin":"v0111Prod"}})

but this is more an expert's functionality.

Running:

>>> help(GenericApplication)

prints out all the available methods.

:author: Stephane Poss
:author: Remi Ete
:author: Ching Bon Lam
"""
from __future__ import absolute_import
__RCSID__ = "$Id$"

__all__ = ['GenericApplication', 'GetSRMFile', '_Root', 'RootScript', 'RootMacro',
           'Whizard', 'Pythia', 'PostGenSelection', 'StdhepCut', 'StdhepCutJava',
           'Mokka', 'SLIC', 'OverlayInput', 'Marlin', 'LCSIM', 'SLICPandora',
           'CheckCollections', 'SLCIOConcatenate', 'SLCIOSplit', 'StdHepSplit',
           'Tomato', 'CheckWNs', 'DDSim', 'Fcc', 'FccSw', 'FccAnalysis', 'Whizard2',
           'KKMC',
           'GaudiApp',
           'DelphesApp',
           'Babayaga',
           'Bhlumi',
           ]

from ILCDIRAC.Interfaces.API.NewInterface.Applications.GenericApplication import GenericApplication
from ILCDIRAC.Interfaces.API.NewInterface.Applications.GetSRMFile import GetSRMFile
from ILCDIRAC.Interfaces.API.NewInterface.Applications._Root import _Root
from ILCDIRAC.Interfaces.API.NewInterface.Applications.RootScript import RootScript
from ILCDIRAC.Interfaces.API.NewInterface.Applications.RootMacro import RootMacro
from ILCDIRAC.Interfaces.API.NewInterface.Applications.Whizard import Whizard
from ILCDIRAC.Interfaces.API.NewInterface.Applications.Pythia import Pythia
from ILCDIRAC.Interfaces.API.NewInterface.Applications.PostGenSelection import PostGenSelection
from ILCDIRAC.Interfaces.API.NewInterface.Applications.StdhepCut import StdhepCut
from ILCDIRAC.Interfaces.API.NewInterface.Applications.StdhepCutJava import StdhepCutJava
from ILCDIRAC.Interfaces.API.NewInterface.Applications.Mokka import Mokka
from ILCDIRAC.Interfaces.API.NewInterface.Applications.SLIC import SLIC
from ILCDIRAC.Interfaces.API.NewInterface.Applications.OverlayInput import OverlayInput
from ILCDIRAC.Interfaces.API.NewInterface.Applications.Marlin import Marlin
from ILCDIRAC.Interfaces.API.NewInterface.Applications.LCSIM import LCSIM
from ILCDIRAC.Interfaces.API.NewInterface.Applications.SLICPandora import SLICPandora
from ILCDIRAC.Interfaces.API.NewInterface.Applications.CheckCollections import CheckCollections
from ILCDIRAC.Interfaces.API.NewInterface.Applications.SLCIOConcatenate import SLCIOConcatenate
from ILCDIRAC.Interfaces.API.NewInterface.Applications.SLCIOSplit import SLCIOSplit
from ILCDIRAC.Interfaces.API.NewInterface.Applications.StdHepSplit import StdHepSplit
from ILCDIRAC.Interfaces.API.NewInterface.Applications.Tomato import Tomato
from ILCDIRAC.Interfaces.API.NewInterface.Applications.CheckWNs import CheckWNs
from ILCDIRAC.Interfaces.API.NewInterface.Applications.DDSim import DDSim
from ILCDIRAC.Interfaces.API.NewInterface.Applications.Fcc import Fcc
from ILCDIRAC.Interfaces.API.NewInterface.Applications.Fcc import FccSw
from ILCDIRAC.Interfaces.API.NewInterface.Applications.Fcc import FccAnalysis
from ILCDIRAC.Interfaces.API.NewInterface.Applications.Whizard2 import Whizard2
from ILCDIRAC.Interfaces.API.NewInterface.Applications.KKMC import KKMC
from ILCDIRAC.Interfaces.API.NewInterface.Applications.GaudiApp import GaudiApp
from ILCDIRAC.Interfaces.API.NewInterface.Applications.DelphesApp import DelphesApp
from ILCDIRAC.Interfaces.API.NewInterface.Applications.Babayaga import Babayaga
from ILCDIRAC.Interfaces.API.NewInterface.Applications.Bhlumi import Bhlumi
