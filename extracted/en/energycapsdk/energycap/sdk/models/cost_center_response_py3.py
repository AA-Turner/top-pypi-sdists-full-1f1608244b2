# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CostCenterResponse(Model):
    """CostCenterResponse.

    :param cost_center_id: The cost center identifier
    :type cost_center_id: int
    :param cost_center_code: The cost center code
    :type cost_center_code: str
    :param cost_center_info: The cost center info
    :type cost_center_info: str
    :param parent:
    :type parent: ~energycap.sdk.models.CostCenterChild
    :param cost_centers: An array of child cost centers
    :type cost_centers: list[~energycap.sdk.models.CostCenterChild]
    :param accounts: An array of child accounts
    :type accounts: list[~energycap.sdk.models.CostCenterAccountChild]
    """

    _attribute_map = {
        'cost_center_id': {'key': 'costCenterId', 'type': 'int'},
        'cost_center_code': {'key': 'costCenterCode', 'type': 'str'},
        'cost_center_info': {'key': 'costCenterInfo', 'type': 'str'},
        'parent': {'key': 'parent', 'type': 'CostCenterChild'},
        'cost_centers': {'key': 'costCenters', 'type': '[CostCenterChild]'},
        'accounts': {'key': 'accounts', 'type': '[CostCenterAccountChild]'},
    }

    def __init__(self, *, cost_center_id: int=None, cost_center_code: str=None, cost_center_info: str=None, parent=None, cost_centers=None, accounts=None, **kwargs) -> None:
        super(CostCenterResponse, self).__init__(**kwargs)
        self.cost_center_id = cost_center_id
        self.cost_center_code = cost_center_code
        self.cost_center_info = cost_center_info
        self.parent = parent
        self.cost_centers = cost_centers
        self.accounts = accounts
