"""Retrieve MIP peak ratios (Ring/Other to EndCap) for HCal from Calibration.txt file."""

from __future__ import print_function
from __future__ import absolute_import
import sys
from Helper_Functions import find_between


Calibration_File_And_Path = sys.argv[1]
Energy_To_Calibrate = sys.argv[2]

# Mean is the last value for mean of Gaussian fit written to the Calibration.txt file.

Ring_MIP_Peak = ''
EndCap_MIP_Peak = ''

with open(Calibration_File_And_Path, 'r') as f:
    searchlines = f.readlines()
    for line in searchlines:
        if 'HCal Ring MIP Peak' in line:
            Ring_MIP_Peak = float(find_between(line, ' : ', ' :'))
        if 'HCal EndCap MIP Peak' in line:
            EndCap_MIP_Peak = float(find_between(line, ' : ', ' :'))

Calibration_Text = '_____________________________________________________________________________________' + '\n'

Calibration_Text += 'HCal_Ring_Digi_Extract.py finding MIP peak ratios (Ring/Other to EndCap) for HCal' + '\n'

Calibration_Text += 'For Muons with energy                              :' + str(Energy_To_Calibrate) + ' /GeV \n\n'

Calibration_Text += 'Ring MIP Peak                                      :' + str(Ring_MIP_Peak) + ' /ADC Units \n\n'

Calibration_Text += 'EndCap MIP Peak                                    :' + str(EndCap_MIP_Peak) + ' /ADC Units \n\n'

with open(Calibration_File_And_Path, 'a') as myfile:
    myfile.write(Calibration_Text)

print(str(float(EndCap_MIP_Peak) / float(Ring_MIP_Peak)))
