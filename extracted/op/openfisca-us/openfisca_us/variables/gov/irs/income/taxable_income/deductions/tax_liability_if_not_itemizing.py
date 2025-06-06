from openfisca_us.model_api import *
from openfisca_core.tracers import SimpleTracer


class tax_liability_if_not_itemizing(Variable):
    value_type = float
    entity = TaxUnit
    label = "Tax liability if not itemizing"
    unit = USD
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        with BranchedSimulation(tax_unit) as simulation_if_not_itemizing:
            simulation_if_not_itemizing.set_input(
                "tax_unit_itemizes",
                period,
                np.zeros((tax_unit.count,), dtype=bool),
            )
            values = simulation_if_not_itemizing.calculate(
                "federal_state_income_tax", period
            )
        return values
