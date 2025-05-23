# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GHGGas(Model):
    """GHGGas.

    :param gas_id: Gas identifier
    :type gas_id: int
    :param gas_info: Gas descrption
    :type gas_info: str
    :param gas_amount: Gas amount
    :type gas_amount: float
    :param co2_evalue: Co2Evalue
    :type co2_evalue: float
    """

    _attribute_map = {
        'gas_id': {'key': 'gasId', 'type': 'int'},
        'gas_info': {'key': 'gasInfo', 'type': 'str'},
        'gas_amount': {'key': 'gasAmount', 'type': 'float'},
        'co2_evalue': {'key': 'co2Evalue', 'type': 'float'},
    }

    def __init__(self, *, gas_id: int=None, gas_info: str=None, gas_amount: float=None, co2_evalue: float=None, **kwargs) -> None:
        super(GHGGas, self).__init__(**kwargs)
        self.gas_id = gas_id
        self.gas_info = gas_info
        self.gas_amount = gas_amount
        self.co2_evalue = co2_evalue
