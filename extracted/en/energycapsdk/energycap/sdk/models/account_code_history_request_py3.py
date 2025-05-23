# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AccountCodeHistoryRequest(Model):
    """AccountCodeHistoryRequest.

    All required parameters must be populated in order to send to Azure.

    :param new_account_code: Required. Account code that will replace the
     existing one <span class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 50 characters</span>
    :type new_account_code: str
    :param new_account_info: Account info that can replace the existing info
     <span class='property-internal'>Must be between 0 and 50 characters</span>
     <span class='property-internal'>Required (defined)</span>
    :type new_account_info: str
    :param code_change_date: Date that the account code was changed <span
     class='property-internal'>Required (defined)</span>
    :type code_change_date: datetime
    """

    _validation = {
        'new_account_code': {'required': True, 'max_length': 50, 'min_length': 0},
        'new_account_info': {'max_length': 50, 'min_length': 0},
    }

    _attribute_map = {
        'new_account_code': {'key': 'newAccountCode', 'type': 'str'},
        'new_account_info': {'key': 'newAccountInfo', 'type': 'str'},
        'code_change_date': {'key': 'codeChangeDate', 'type': 'iso-8601'},
    }

    def __init__(self, *, new_account_code: str, new_account_info: str=None, code_change_date=None, **kwargs) -> None:
        super(AccountCodeHistoryRequest, self).__init__(**kwargs)
        self.new_account_code = new_account_code
        self.new_account_info = new_account_info
        self.code_change_date = code_change_date
