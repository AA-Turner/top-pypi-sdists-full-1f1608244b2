# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ReportSubscriptionChild(Model):
    """ReportSubscriptionChild.

    :param report_subscription_id: The identifier of the report subscription
    :type report_subscription_id: int
    :param user:
    :type user: ~energycap.sdk.models.UserChild
    :param email_recipient: The email address to send the report to
    :type email_recipient: str
    :param email_subject: The subject line of the email
    :type email_subject: str
    :param email_message: The body of the email
    :type email_message: str
    :param report_format: Format of the report (EnergyCAP currently supports
     PDF, Word, Excel, and CSV)
    :type report_format: str
    :param schedule_type:
    :type schedule_type:
     ~energycap.sdk.models.ReportSubscriptionScheduleTypeChild
    :param day_indicator:
    :type day_indicator:
     ~energycap.sdk.models.ReportSubscriptionDayIndicatorChild
    :param only_send_if_data: Indicates whether or not to email a report if it
     contains no data.
     When set to true, the subscribed report will not be emailed, if the report
     does not contain data.
     When set to false, if the requested report has no data, it will still be
     sent.
    :type only_send_if_data: bool
    """

    _attribute_map = {
        'report_subscription_id': {'key': 'reportSubscriptionId', 'type': 'int'},
        'user': {'key': 'user', 'type': 'UserChild'},
        'email_recipient': {'key': 'emailRecipient', 'type': 'str'},
        'email_subject': {'key': 'emailSubject', 'type': 'str'},
        'email_message': {'key': 'emailMessage', 'type': 'str'},
        'report_format': {'key': 'reportFormat', 'type': 'str'},
        'schedule_type': {'key': 'scheduleType', 'type': 'ReportSubscriptionScheduleTypeChild'},
        'day_indicator': {'key': 'dayIndicator', 'type': 'ReportSubscriptionDayIndicatorChild'},
        'only_send_if_data': {'key': 'onlySendIfData', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(ReportSubscriptionChild, self).__init__(**kwargs)
        self.report_subscription_id = kwargs.get('report_subscription_id', None)
        self.user = kwargs.get('user', None)
        self.email_recipient = kwargs.get('email_recipient', None)
        self.email_subject = kwargs.get('email_subject', None)
        self.email_message = kwargs.get('email_message', None)
        self.report_format = kwargs.get('report_format', None)
        self.schedule_type = kwargs.get('schedule_type', None)
        self.day_indicator = kwargs.get('day_indicator', None)
        self.only_send_if_data = kwargs.get('only_send_if_data', None)
