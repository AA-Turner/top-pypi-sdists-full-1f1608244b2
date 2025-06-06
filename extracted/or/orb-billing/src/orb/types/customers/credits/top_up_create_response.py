# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["TopUpCreateResponse", "InvoiceSettings"]


class InvoiceSettings(BaseModel):
    auto_collection: bool
    """
    Whether the credits purchase invoice should auto collect with the customer's
    saved payment method.
    """

    net_terms: int
    """
    The net terms determines the difference between the invoice date and the issue
    date for the invoice. If you intend the invoice to be due on issue, set this
    to 0.
    """

    memo: Optional[str] = None
    """An optional memo to display on the invoice."""

    require_successful_payment: Optional[bool] = None
    """
    When true, credit blocks created by this top-up will require that the
    corresponding invoice is paid before they are drawn down from. If any topup
    block is pending payment, further automatic top-ups will be paused until the
    invoice is paid or voided.
    """


class TopUpCreateResponse(BaseModel):
    id: str

    amount: str
    """The amount to increment when the threshold is reached."""

    currency: str
    """The currency or custom pricing unit to use for this top-up.

    If this is a real-world currency, it must match the customer's invoicing
    currency.
    """

    invoice_settings: InvoiceSettings
    """Settings for invoices generated by triggered top-ups."""

    per_unit_cost_basis: str
    """How much, in the customer's currency, to charge for each unit."""

    threshold: str
    """The threshold at which to trigger the top-up.

    If the balance is at or below this threshold, the top-up will be triggered.
    """

    expires_after: Optional[int] = None
    """The number of days or months after which the top-up expires.

    If unspecified, it does not expire.
    """

    expires_after_unit: Optional[Literal["day", "month"]] = None
    """The unit of expires_after."""
