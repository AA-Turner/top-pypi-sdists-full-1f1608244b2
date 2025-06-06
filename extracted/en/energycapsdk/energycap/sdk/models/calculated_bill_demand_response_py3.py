# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CalculatedBillDemandResponse(Model):
    """CalculatedBillDemandResponse.

    :param readings_from_channel:
    :type readings_from_channel:
     ~energycap.sdk.models.ChannelChildWithObservationType
    :param fixed_demand:
    :type fixed_demand: ~energycap.sdk.models.FixedAmountResponse
    :param readings_from_wattics_data_point:
    :type readings_from_wattics_data_point:
     ~energycap.sdk.models.WatticsDataPointChild
    """

    _attribute_map = {
        'readings_from_channel': {'key': 'readingsFromChannel', 'type': 'ChannelChildWithObservationType'},
        'fixed_demand': {'key': 'fixedDemand', 'type': 'FixedAmountResponse'},
        'readings_from_wattics_data_point': {'key': 'readingsFromWatticsDataPoint', 'type': 'WatticsDataPointChild'},
    }

    def __init__(self, *, readings_from_channel=None, fixed_demand=None, readings_from_wattics_data_point=None, **kwargs) -> None:
        super(CalculatedBillDemandResponse, self).__init__(**kwargs)
        self.readings_from_channel = readings_from_channel
        self.fixed_demand = fixed_demand
        self.readings_from_wattics_data_point = readings_from_wattics_data_point
