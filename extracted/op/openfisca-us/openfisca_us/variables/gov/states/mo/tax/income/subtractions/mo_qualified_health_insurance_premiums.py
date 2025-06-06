from openfisca_us.model_api import *


class mo_qualified_health_insurance_premiums(Variable):
    value_type = float
    entity = Person
    label = "MO qualified healh insurance premiums"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://dor.mo.gov/forms/5695.pdf",  # Form MO 5695
        "https://www.irs.gov/pub/irs-pdf/f1040sa.pdf",  # Federal Form 1040 Schedule A
        "https://www.irs.gov/pub/irs-pdf/f1040.pdf",  # Federal Form 1040
    )
    defined_for = StateCode.MO

    def formula(person, period, parameters):
        # Variable involves person- and tax unit-level variables.
        tax_unit = person.tax_unit

        # total_health_insurance_premiums is also a primary input to the MO side of calculation, MO Form 5695, Line 8
        # Federal Schedule A, Line 4
        med_expense_deduction = add(
            tax_unit, period, ["medical_expense_deduction"]
        )

        # the ratio of federal medical expense deduction to total medical expenses (out of pocket + premiums)
        # need division because med_dental_out_of_pocket is in federal tax, but no MO tax
        # this ratio is then used to scale the health_insurance_premium amount that can be claimed
        # IRS Schedule A Line 1
        tax_unit_health_expenses = add(
            tax_unit,
            period,
            ["medical_out_of_pocket_expenses", "health_insurance_premiums"],
        )
        # Apply a where statement to avoid division by zero.
        med_expense_deducted_ratio = where(
            tax_unit_health_expenses > 0,
            med_expense_deduction / tax_unit_health_expenses,
            0,
        )

        person_premiums = person("health_insurance_premiums", period)
        tax_unit_premiums = tax_unit.sum(person_premiums)

        # Line 13 of MO Form 5695, represents the portion of medical expenses already deducted via federal tax itemization
        deducted_portion = tax_unit_premiums * med_expense_deducted_ratio
        # subtracts the portion of premiums already deducted from federal tax
        itemized_premiums_amount = tax_unit_premiums - deducted_portion
        itemizes = tax_unit("tax_unit_itemizes", period)
        # Cap at federal taxable income.
        taxable_income = tax_unit("taxable_income", period)
        # Allocate proportionally across people in the tax unit based on share
        # of premiums. Use where statement to avoid dividing by zero.
        person_share_of_tax_unit_premiums = where(
            tax_unit_premiums > 0, person_premiums / tax_unit_premiums, 0
        )

        return person_share_of_tax_unit_premiums * where(
            itemizes,
            min_(itemized_premiums_amount, taxable_income),
            min_(tax_unit_premiums, taxable_income),
        )
