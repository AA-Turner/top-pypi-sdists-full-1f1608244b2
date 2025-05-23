from openfisca_us.model_api import *


class hud_ttp_income_share(Variable):
    value_type = float
    entity = SPMUnit
    label = "HUD income share for total tenant payment"
    unit = USD
    documentation = "HUD income share for Total Tenant Payment"
    definition_period = YEAR
    reference = "https://www.law.cornell.edu/cfr/text/24/5.628#a_2"

    def formula(spm_unit, period, parameters):
        share = parameters(period).gov.hud.total_tenant_payment.income_share
        income = spm_unit("hud_annual_income", period)
        return share * income
