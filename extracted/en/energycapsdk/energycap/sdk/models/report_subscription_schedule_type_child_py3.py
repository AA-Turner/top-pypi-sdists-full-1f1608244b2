# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ReportSubscriptionScheduleTypeChild(Model):
    """ReportSubscriptionScheduleTypeChild.

    :param report_subscription_schedule_type_id: The identifier of the
     subscription schedule type
    :type report_subscription_schedule_type_id: int
    :param report_subscription_schedule_type_name: The name of the
     subscription schedule type
    :type report_subscription_schedule_type_name: str
    """

    _attribute_map = {
        'report_subscription_schedule_type_id': {'key': 'reportSubscriptionScheduleTypeId', 'type': 'int'},
        'report_subscription_schedule_type_name': {'key': 'reportSubscriptionScheduleTypeName', 'type': 'str'},
    }

    def __init__(self, *, report_subscription_schedule_type_id: int=None, report_subscription_schedule_type_name: str=None, **kwargs) -> None:
        super(ReportSubscriptionScheduleTypeChild, self).__init__(**kwargs)
        self.report_subscription_schedule_type_id = report_subscription_schedule_type_id
        self.report_subscription_schedule_type_name = report_subscription_schedule_type_name
