"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import TypedDict


class WebhooksMarketplacePurchaseType(TypedDict):
    """Marketplace Purchase"""

    account: WebhooksMarketplacePurchasePropAccountType
    billing_cycle: str
    free_trial_ends_on: Union[str, None]
    next_billing_date: Union[str, None]
    on_free_trial: bool
    plan: WebhooksMarketplacePurchasePropPlanType
    unit_count: int


class WebhooksMarketplacePurchasePropAccountType(TypedDict):
    """WebhooksMarketplacePurchasePropAccount"""

    id: int
    login: str
    node_id: str
    organization_billing_email: Union[str, None]
    type: str


class WebhooksMarketplacePurchasePropPlanType(TypedDict):
    """WebhooksMarketplacePurchasePropPlan"""

    bullets: list[Union[str, None]]
    description: str
    has_free_trial: bool
    id: int
    monthly_price_in_cents: int
    name: str
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"]
    unit_name: Union[str, None]
    yearly_price_in_cents: int


__all__ = (
    "WebhooksMarketplacePurchasePropAccountType",
    "WebhooksMarketplacePurchasePropPlanType",
    "WebhooksMarketplacePurchaseType",
)
