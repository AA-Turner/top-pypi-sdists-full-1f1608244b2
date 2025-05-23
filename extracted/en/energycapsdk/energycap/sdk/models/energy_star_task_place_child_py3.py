# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EnergyStarTaskPlaceChild(Model):
    """EnergyStarTaskPlaceChild.

    :param building:
    :type building: ~energycap.sdk.models.PlaceChild
    :param task_periods: The list of submission or metrics periods for the
     task
    :type task_periods: list[~energycap.sdk.models.NamedPeriod]
    """

    _attribute_map = {
        'building': {'key': 'building', 'type': 'PlaceChild'},
        'task_periods': {'key': 'taskPeriods', 'type': '[NamedPeriod]'},
    }

    def __init__(self, *, building=None, task_periods=None, **kwargs) -> None:
        super(EnergyStarTaskPlaceChild, self).__init__(**kwargs)
        self.building = building
        self.task_periods = task_periods
