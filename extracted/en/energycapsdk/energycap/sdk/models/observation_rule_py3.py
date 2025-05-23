# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ObservationRule(Model):
    """ObservationRule.

    :param observation_rule_id: The observation rule identifier
    :type observation_rule_id: int
    :param observation_rule_code: The observation rule code
    :type observation_rule_code: str
    :param observation_rule_info: The observation rule info
    :type observation_rule_info: str
    """

    _attribute_map = {
        'observation_rule_id': {'key': 'observationRuleId', 'type': 'int'},
        'observation_rule_code': {'key': 'observationRuleCode', 'type': 'str'},
        'observation_rule_info': {'key': 'observationRuleInfo', 'type': 'str'},
    }

    def __init__(self, *, observation_rule_id: int=None, observation_rule_code: str=None, observation_rule_info: str=None, **kwargs) -> None:
        super(ObservationRule, self).__init__(**kwargs)
        self.observation_rule_id = observation_rule_id
        self.observation_rule_code = observation_rule_code
        self.observation_rule_info = observation_rule_info
