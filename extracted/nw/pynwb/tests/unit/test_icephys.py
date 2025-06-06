import numpy as np

from pynwb.icephys import (
    PatchClampSeries,
    CurrentClampSeries,
    IZeroClampSeries,
    CurrentClampStimulusSeries,
    VoltageClampSeries,
    VoltageClampStimulusSeries,
    IntracellularElectrode,
    SweepTable,
)
from pynwb.device import Device
from pynwb.testing import TestCase
from pynwb.file import NWBFile  # Needed to test icephys functionality defined on NWBFile
from datetime import datetime
from dateutil.tz import tzlocal


def GetElectrode():
    device = Device(name='device_name')
    elec = IntracellularElectrode(
        name='test_iS',
        device=device,
        description='description',
        slice='slice',
        seal='seal',
        location='location',
        resistance='resistance',
        filtering='filtering',
        initial_access_resistance='initial_access_resistance',
        cell_id='this_cell',
    )
    return elec


class NWBFileICEphys(TestCase):
    """Test ICEphys-specific functionality on NWBFile"""
    def setUp(self):
        self.icephys_electrode = GetElectrode()

    def test_sweep_table_deprecation_warn(self):
        msg = ("SweepTable is deprecated. Use the IntracellularRecordingsTable instead. "
               "See also the NWBFile.add_intracellular_recordings function.")
        
        with self.assertRaisesWith(ValueError, msg):
            SweepTable()

        # create object in construct mode, modeling the behavior of the ObjectMapper on read
        # should not raise error or warning
        sweepT = SweepTable.__new__(SweepTable, in_construct_mode=True)
        sweepT.__init__()
        
        kwargs = dict(session_description='NWBFile icephys test',
                identifier='NWB123',  # required
                session_start_time=datetime(2017, 4, 3, 11, tzinfo=tzlocal()),
                icephys_electrodes=[self.icephys_electrode, ],
                sweep_table=sweepT)
        
        with self.assertRaisesWith(ValueError, msg):
            NWBFile(**kwargs)

        # create object in construct mode, modeling the behavior of the ObjectMapper on read
        # should not warn or error
        nwbfile = NWBFile.__new__(NWBFile, in_construct_mode=True)
        nwbfile.__init__(**kwargs)

    def test_icephys_electrodes_parameter(self):
        nwbfile = NWBFile(
                session_description='NWBFile icephys test',
                identifier='NWB123',  # required
                session_start_time=datetime(2017, 4, 3, 11, tzinfo=tzlocal()),
                icephys_electrodes=[self.icephys_electrode, ])
        self.assertEqual(nwbfile.get_icephys_electrode('test_iS'), self.icephys_electrode)

    def test_ic_electrodes_attribute_deprecation(self):
        nwbfile = NWBFile(
            session_description='NWBFile icephys test',
            identifier='NWB123',  # required
            session_start_time=datetime(2017, 4, 3, 11, tzinfo=tzlocal()),
            icephys_electrodes=[self.icephys_electrode, ])

        # make sure NWBFile.get_ic_electrode warns
        msg = "'NWBFile' object has no attribute 'get_ic_electrode'"
        with self.assertRaisesWith(AttributeError, msg):
            nwbfile.get_ic_electrode(self.icephys_electrode.name)


class IntracellularElectrodeConstructor(TestCase):

    def test_constructor(self):
        device = Device(name='device_name')
        elec = IntracellularElectrode(name='test_iS',
                                      device=device,
                                      description='description',
                                      slice='slice',
                                      seal='seal',
                                      location='location',
                                      resistance='resistance',
                                      filtering='filtering',
                                      initial_access_resistance='initial_access_resistance',
                                      cell_id='this_cell')
        self.assertEqual(elec.name, 'test_iS')
        self.assertEqual(elec.device, device)
        self.assertEqual(elec.description, 'description')
        self.assertEqual(elec.slice, 'slice')
        self.assertEqual(elec.seal, 'seal')
        self.assertEqual(elec.location, 'location')
        self.assertEqual(elec.resistance, 'resistance')
        self.assertEqual(elec.filtering, 'filtering')
        self.assertEqual(elec.initial_access_resistance, 'initial_access_resistance')
        self.assertEqual(elec.cell_id, 'this_cell')


class PatchClampSeriesConstructor(TestCase):

    def test_default(self):
        electrode_name = GetElectrode()

        pCS = PatchClampSeries(name='test_pCS', 
                               data=list(), 
                               unit='unit',
                               electrode=electrode_name, 
                               gain=1.0, 
                               timestamps=list())
        self.assertEqual(pCS.name, 'test_pCS')
        self.assertEqual(pCS.unit, 'unit')
        self.assertEqual(pCS.electrode, electrode_name)
        self.assertEqual(pCS.gain, 1.0)

    def test_gain_optional(self):
        electrode_name = GetElectrode()

        pCS = PatchClampSeries(name='test_pCS',
                               data=list(),
                               unit='unit',
                               electrode=electrode_name,
                               timestamps=list())
        self.assertIsNone(pCS.gain)

    def test_sweepNumber_valid(self):
        electrode_name = GetElectrode()

        pCS = PatchClampSeries(name='test_pCS', 
                               data=list(), 
                               unit='unit',
                               electrode=electrode_name, 
                               gain=1.0, 
                               timestamps=list(), 
                               sweep_number=4711)
        self.assertEqual(pCS.name, 'test_pCS')
        self.assertEqual(pCS.unit, 'unit')
        self.assertEqual(pCS.electrode, electrode_name)
        self.assertEqual(pCS.gain, 1.0)
        self.assertEqual(pCS.sweep_number, 4711)

    def test_sweepNumber_valid_np(self):
        electrode_name = GetElectrode()

        pCS = PatchClampSeries(name='test_pCS', 
                               data=list(), 
                               unit='unit',
                               electrode=electrode_name, 
                               gain=1.0, 
                               timestamps=list(), 
                               sweep_number=1)
        self.assertEqual(pCS.name, 'test_pCS')
        self.assertEqual(pCS.unit, 'unit')
        self.assertEqual(pCS.electrode, electrode_name)
        self.assertEqual(pCS.gain, 1.0)
        self.assertEqual(pCS.sweep_number, np.uint32(1))

    def test_sweepNumber_large_and_valid(self):
        electrode_name = GetElectrode()

        pCS = PatchClampSeries(name='test_pCS', 
                               data=list(), 
                               unit='unit',
                               electrode=electrode_name, 
                               gain=1.0, 
                               timestamps=list(), 
                               sweep_number=np.uint64(2**63-1))
        self.assertEqual(pCS.name, 'test_pCS')
        self.assertEqual(pCS.unit, 'unit')
        self.assertEqual(pCS.electrode, electrode_name)
        self.assertEqual(pCS.gain, 1.0)
        self.assertEqual(pCS.sweep_number, 2**63-1)

    def test_sweepNumber_throws_with_negative(self):
        electrode_name = GetElectrode()

        with self.assertRaises(ValueError):
            PatchClampSeries(name='test_pCS', 
                             data=list(), 
                             unit='unit',
                             electrode=electrode_name, 
                             gain=1.0, 
                             timestamps=list(), 
                             sweep_number=-1)

    def test_sweepNumber_throws_with_NaN(self):
        electrode_name = GetElectrode()

        with self.assertRaises(TypeError):
            PatchClampSeries(name='test_pCS', 
                             data=list(), 
                             unit='unit',
                             electrodes=electrode_name, 
                             gain=1.0, 
                             timestamps=list(), 
                             sweep_number=float('nan'))

    def test_sweepNumber_throws_with_Float(self):
        electrode_name = GetElectrode()

        with self.assertRaises(TypeError):
            PatchClampSeries(name='test_pCS', 
                             data=list(), 
                             unit='unit',
                             electrodes=electrode_name, 
                             gain=1.0, 
                             timestamps=list(),
                             sweep_number=1.5)

    def test_data_shape(self):
        electrode_name = GetElectrode()

        with self.assertRaises(ValueError):
            PatchClampSeries(
                name="test_pCS",
                data=np.ones((30, 2)),
                unit="unit",
                electrode=electrode_name,
                gain=1.0,
                rate=100_000.,
            )


class CurrentClampSeriesConstructor(TestCase):

    def test_init(self):
        electrode_name = GetElectrode()

        cCS = CurrentClampSeries(name='test_cCS', 
                                 data=list(), 
                                 electrode=electrode_name, 
                                 gain=1.0, 
                                 stimulus_description="stimset", 
                                 bias_current=2.0, 
                                 bridge_balance=3.0, 
                                 capacitance_compensation=4.0,
                                 timestamps=list())
        self.assertEqual(cCS.name, 'test_cCS')
        self.assertEqual(cCS.unit, 'volts')
        self.assertEqual(cCS.electrode, electrode_name)
        self.assertEqual(cCS.stimulus_description, "stimset")
        self.assertEqual(cCS.gain, 1.0)
        self.assertEqual(cCS.bias_current, 2.0)
        self.assertEqual(cCS.bridge_balance, 3.0)
        self.assertEqual(cCS.capacitance_compensation, 4.0)

    def test_unit_warning(self):
        electrode_name = GetElectrode()

        msg = "Unit 'unit' for CurrentClampSeries 'test_cCS' is ignored and will be set to 'volts' as per NWB 2.1.0."
        with self.assertWarnsWith(UserWarning, msg):
            cCS = CurrentClampSeries('test_cCS', list(), electrode_name, 1.0, "stimset", 2.0, 3.0, 4.0,
                                     timestamps=list(), unit='unit')
        self.assertEqual(cCS.unit, 'volts')


class IZeroClampSeriesConstructor(TestCase):

    def test_init(self):
        electrode_name = GetElectrode()

        iZCS = IZeroClampSeries(name='test_iZCS', 
                                data=list(), 
                                electrode=electrode_name, 
                                gain=1.0, 
                                timestamps=list())
        self.assertEqual(iZCS.name, 'test_iZCS')
        self.assertEqual(iZCS.unit, 'volts')
        self.assertEqual(iZCS.electrode, electrode_name)
        self.assertEqual(iZCS.gain, 1.0)
        self.assertEqual(iZCS.bias_current, 0.0)
        self.assertEqual(iZCS.bridge_balance, 0.0)
        self.assertEqual(iZCS.capacitance_compensation, 0.0)
        self.assertEqual(iZCS.stimulus_description, 'N/A')

    def test_unit_warning(self):
        electrode_name = GetElectrode()

        msg = "Unit 'unit' for IZeroClampSeries 'test_iZCS' is ignored and will be set to 'volts' as per NWB 2.1.0."
        with self.assertWarnsWith(UserWarning, msg):
            iZCS = IZeroClampSeries('test_iZCS', list(), electrode_name, 1.0, timestamps=list(), unit='unit')
        self.assertEqual(iZCS.unit, 'volts')

    def test_stim_desc_warning(self):
        electrode_name = GetElectrode()

        msg = ("Stimulus description 'desc' for IZeroClampSeries 'test_iZCS' is ignored and will be set to 'N/A' "
               "as per NWB 2.3.0.")
        with self.assertWarnsWith(UserWarning, msg):
            iZCS = IZeroClampSeries('test_iZCS', list(), electrode_name, 1.0, timestamps=list(),
                                    stimulus_description='desc')
        self.assertEqual(iZCS.stimulus_description, 'N/A')


class CurrentClampStimulusSeriesConstructor(TestCase):

    def test_init(self):
        electrode_name = GetElectrode()

        cCSS = CurrentClampStimulusSeries(name='test_cCSS', 
                                          data=list(), 
                                          electrode=electrode_name, 
                                          gain=1.0, 
                                          timestamps=list())
        self.assertEqual(cCSS.name, 'test_cCSS')
        self.assertEqual(cCSS.unit, 'amperes')
        self.assertEqual(cCSS.electrode, electrode_name)
        self.assertEqual(cCSS.gain, 1.0)

    def test_unit_warning(self):
        electrode_name = GetElectrode()

        msg = ("Unit 'unit' for CurrentClampStimulusSeries 'test_cCSS' is ignored and will be set "
               "to 'amperes' as per NWB 2.1.0.")
        with self.assertWarnsWith(UserWarning, msg):
            cCSS = CurrentClampStimulusSeries('test_cCSS', list(), electrode_name, 1.0, timestamps=list(), unit='unit')
        self.assertEqual(cCSS.unit, 'amperes')


class VoltageClampSeriesConstructor(TestCase):

    def test_init(self):
        electrode_name = GetElectrode()

        vCS = VoltageClampSeries(name='test_vCS', 
                                 data=list(), 
                                 electrode=electrode_name,
                                 gain=1.0, 
                                 stimulus_description="stimset", 
                                 capacitance_fast=2.0, 
                                 capacitance_slow=3.0, 
                                 resistance_comp_bandwidth=4.0, 
                                 resistance_comp_correction=5.0, 
                                 resistance_comp_prediction=6.0, 
                                 whole_cell_capacitance_comp=7.0, 
                                 whole_cell_series_resistance_comp=8.0, 
                                 timestamps=list())
        self.assertEqual(vCS.name, 'test_vCS')
        self.assertEqual(vCS.unit, 'amperes')
        self.assertEqual(vCS.electrode, electrode_name)
        self.assertEqual(vCS.stimulus_description, "stimset")
        self.assertEqual(vCS.gain, 1.0)
        self.assertEqual(vCS.capacitance_fast, 2.0)
        self.assertEqual(vCS.capacitance_slow, 3.0)
        self.assertEqual(vCS.resistance_comp_bandwidth, 4.0)
        self.assertEqual(vCS.resistance_comp_correction, 5.0)
        self.assertEqual(vCS.resistance_comp_prediction, 6.0)
        self.assertEqual(vCS.whole_cell_capacitance_comp, 7.0)
        self.assertEqual(vCS.whole_cell_series_resistance_comp, 8.0)

    def test_unit_warning(self):
        electrode_name = GetElectrode()

        msg = "Unit 'unit' for VoltageClampSeries 'test_vCS' is ignored and will be set " \
              "to 'amperes' as per NWB 2.1.0."
        with self.assertWarnsWith(UserWarning, msg):
            vCS = VoltageClampSeries(name='test_vCS', 
                                     data=list(), 
                                     electrode=electrode_name,
                                     gain=1.0, 
                                     stimulus_description="stimset", 
                                     capacitance_fast=2.0, 
                                     capacitance_slow=3.0, 
                                     resistance_comp_bandwidth=4.0, 
                                     resistance_comp_correction=5.0, 
                                     resistance_comp_prediction=6.0, 
                                     whole_cell_capacitance_comp=7.0, 
                                     whole_cell_series_resistance_comp=8.0, 
                                     timestamps=list(), 
                                     unit='unit')
        self.assertEqual(vCS.unit, 'amperes')


class VoltageClampStimulusSeriesConstructor(TestCase):

    def test_init(self):
        electrode_name = GetElectrode()

        vCSS = VoltageClampStimulusSeries(name='test_vCSS', data=list(), electrode=electrode_name, gain=1.0, 
                                          timestamps=list())
        self.assertEqual(vCSS.name, 'test_vCSS')
        self.assertEqual(vCSS.unit, 'volts')
        self.assertEqual(vCSS.electrode, electrode_name)

    def test_unit_warning(self):
        electrode_name = GetElectrode()

        msg = "Unit 'unit' for VoltageClampStimulusSeries 'test_vCSS' is ignored and will be set " \
              "to 'volts' as per NWB 2.1.0."
        with self.assertWarnsWith(UserWarning, msg):
            vCSS = VoltageClampStimulusSeries('test_vCSS', list(), electrode_name, 1.0, timestamps=list(), unit='unit')
        self.assertEqual(vCSS.unit, 'volts')
