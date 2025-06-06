# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ReportSubscriptionDayIndicatorChild(Model):
    """ReportSubscriptionDayIndicatorChild.

    :param day_indicator_value: Indicates when to send the report for the
     given schedule type
     Values may be:
     Daily: 0
     Weekly: Day of Week - 0 (Sunday) to 6 (Saturday)
     Monthly: Day of Month - 1 to 28
     Quarterly: Month in Quarter - 1, 2, or 3
    :type day_indicator_value: int
    :param day_indicator_info: Name of the day indicator
     Daily: None
     Weekly: One of Sunday to Saturday
     Monthly: One of 1 to 28
     Quarterly: 1st day of month 1 of calendar quarter, 1st day of month 2 of
     calendar quarter, 1st day of month 3 of calendar quarter
    :type day_indicator_info: str
    """

    _attribute_map = {
        'day_indicator_value': {'key': 'dayIndicatorValue', 'type': 'int'},
        'day_indicator_info': {'key': 'dayIndicatorInfo', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ReportSubscriptionDayIndicatorChild, self).__init__(**kwargs)
        self.day_indicator_value = kwargs.get('day_indicator_value', None)
        self.day_indicator_info = kwargs.get('day_indicator_info', None)
