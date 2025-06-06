# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PlaceDigestEnergyUseIntensityEuiEnergyProject(Model):
    """PlaceDigestEnergyUseIntensityEuiEnergyProject.

    :param energy_project_id: The energy project identifier
    :type energy_project_id: int
    :param energy_project_code: The energy project code
    :type energy_project_code: str
    :param energy_project_info: The energy project info
    :type energy_project_info: str
    :param installation_cost: The energy project installation cost
    :type installation_cost: float
    """

    _attribute_map = {
        'energy_project_id': {'key': 'energyProjectId', 'type': 'int'},
        'energy_project_code': {'key': 'energyProjectCode', 'type': 'str'},
        'energy_project_info': {'key': 'energyProjectInfo', 'type': 'str'},
        'installation_cost': {'key': 'installationCost', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(PlaceDigestEnergyUseIntensityEuiEnergyProject, self).__init__(**kwargs)
        self.energy_project_id = kwargs.get('energy_project_id', None)
        self.energy_project_code = kwargs.get('energy_project_code', None)
        self.energy_project_info = kwargs.get('energy_project_info', None)
        self.installation_cost = kwargs.get('installation_cost', None)
