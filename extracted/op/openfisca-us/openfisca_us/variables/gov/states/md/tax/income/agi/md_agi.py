from openfisca_us.model_api import *


class md_agi(Variable):
    value_type = float
    entity = TaxUnit
    label = "MD AGI"
    unit = USD
    definition_period = YEAR
    reference = "https://govt.westlaw.com/mdc/Browse/Home/Maryland/MarylandCodeCourtRules?guid=NAE804370A64411DBB5DDAC3692B918BC&transitionType=Default&contextData=%28sc.Default%29"
    defined_for = StateCode.MD

    def formula(tax_unit, period, parameters):
        with_additions = add(
            tax_unit, period, ["adjusted_gross_income", "md_total_additions"]
        )
        return with_additions - tax_unit("md_total_subtractions", period)
