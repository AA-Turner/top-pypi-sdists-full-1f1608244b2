# SPDX-FileCopyrightText: All Contributors to the PyTango project
# SPDX-License-Identifier: LGPL-3.0-or-later
"""
Basic unit test for a PowerSupply device.  Requires pytest.
"""

from tango.test_utils import DeviceTestContext

from ps0a import PowerSupply


def test_calibrate():
    """Test device calibration and voltage reading."""
    with DeviceTestContext(PowerSupply, process=True) as proxy:
        proxy.calibrate()
        assert proxy.voltage == 1.5
