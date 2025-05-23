# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EnergyStarMeterLinkChild(Model):
    """EnergyStarMeterLinkChild.

    :param meter:
    :type meter: ~energycap.sdk.models.MeterChild
    :param pm_meter_id: The Portfolio Manager meter identifier
    :type pm_meter_id: long
    :param use_per_day: The meter's average use per day
    :type use_per_day: float
    :param use_unit:
    :type use_unit: ~energycap.sdk.models.UnitChild
    :param cost_per_day: The meter's average cost per day
    :type cost_per_day: float
    :param cost_unit:
    :type cost_unit: ~energycap.sdk.models.UnitChild
    :param energy_star_compatible: Is this meter's commodity ENERGY
     STAR-compatible?
    :type energy_star_compatible: bool
    """

    _attribute_map = {
        'meter': {'key': 'meter', 'type': 'MeterChild'},
        'pm_meter_id': {'key': 'pmMeterId', 'type': 'long'},
        'use_per_day': {'key': 'usePerDay', 'type': 'float'},
        'use_unit': {'key': 'useUnit', 'type': 'UnitChild'},
        'cost_per_day': {'key': 'costPerDay', 'type': 'float'},
        'cost_unit': {'key': 'costUnit', 'type': 'UnitChild'},
        'energy_star_compatible': {'key': 'energyStarCompatible', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(EnergyStarMeterLinkChild, self).__init__(**kwargs)
        self.meter = kwargs.get('meter', None)
        self.pm_meter_id = kwargs.get('pm_meter_id', None)
        self.use_per_day = kwargs.get('use_per_day', None)
        self.use_unit = kwargs.get('use_unit', None)
        self.cost_per_day = kwargs.get('cost_per_day', None)
        self.cost_unit = kwargs.get('cost_unit', None)
        self.energy_star_compatible = kwargs.get('energy_star_compatible', None)
