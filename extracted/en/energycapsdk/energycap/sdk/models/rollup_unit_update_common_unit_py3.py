# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RollupUnitUpdateCommonUnit(Model):
    """RollupUnitUpdateCommonUnit.

    :param commodity_id: The commodity identifier <span
     class='property-internal'>Required (defined)</span>
    :type commodity_id: int
    :param common_rollup_unit_id: The unit identifier that this commodity will
     roll up to <span class='property-internal'>Required (defined)</span>
    :type common_rollup_unit_id: int
    """

    _attribute_map = {
        'commodity_id': {'key': 'commodityId', 'type': 'int'},
        'common_rollup_unit_id': {'key': 'commonRollupUnitId', 'type': 'int'},
    }

    def __init__(self, *, commodity_id: int=None, common_rollup_unit_id: int=None, **kwargs) -> None:
        super(RollupUnitUpdateCommonUnit, self).__init__(**kwargs)
        self.commodity_id = commodity_id
        self.common_rollup_unit_id = common_rollup_unit_id
