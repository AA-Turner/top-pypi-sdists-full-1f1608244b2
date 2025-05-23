# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ReportEdit(Model):
    """ReportEdit.

    All required parameters must be populated in order to send to Azure.

    :param report_code: Required. New specific report code <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 16 characters</span>
    :type report_code: str
    :param report_info: Required. New specific report name <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 255 characters</span>
    :type report_info: str
    :param report_description: Required. New specific report description <span
     class='property-internal'>Required</span>
    :type report_description: str
    """

    _validation = {
        'report_code': {'required': True, 'max_length': 16, 'min_length': 0},
        'report_info': {'required': True, 'max_length': 255, 'min_length': 0},
        'report_description': {'required': True},
    }

    _attribute_map = {
        'report_code': {'key': 'reportCode', 'type': 'str'},
        'report_info': {'key': 'reportInfo', 'type': 'str'},
        'report_description': {'key': 'reportDescription', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ReportEdit, self).__init__(**kwargs)
        self.report_code = kwargs.get('report_code', None)
        self.report_info = kwargs.get('report_info', None)
        self.report_description = kwargs.get('report_description', None)
