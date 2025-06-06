# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr 

class CashFlowLineage(BaseModel):
    """
    Lineage for cash flow value  # noqa: E501
    """
    instrument_type:  Optional[StrictStr] = Field(None,alias="instrumentType", description="The instrument type of the instrument to which the cash flow belongs to. When upserting CashFlowValues, this  should be null.") 
    cash_flow_type:  Optional[StrictStr] = Field(None,alias="cashFlowType", description="The cashflow type.When upserting CashFlowValues, this should be null, or one of [Unknown, Coupon, Notional,  Premium, Principal, Protection, Cash]") 
    instrument_id:  Optional[StrictStr] = Field(None,alias="instrumentId", description="The LUID of the instrument to which the cash flow belongs to. When upserting this should be null.") 
    leg_id:  Optional[StrictStr] = Field(None,alias="legId", description="The leg id to which the cash flow belongs to.") 
    source_transaction_id:  Optional[StrictStr] = Field(None,alias="sourceTransactionId", description="The source transaction of the instrument to which the cash flow belongs to. When upserting this should be null") 
    pay_receive:  Optional[StrictStr] = Field(None,alias="payReceive", description="Does the cash flow belong to the Pay or Receive leg. When upserting this should either be null or one of [Pay, Receive, NotApplicable]") 
    __properties = ["instrumentType", "cashFlowType", "instrumentId", "legId", "sourceTransactionId", "payReceive"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def __str__(self):
        """For `print` and `pprint`"""
        return pprint.pformat(self.dict(by_alias=False))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CashFlowLineage:
        """Create an instance of CashFlowLineage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if instrument_type (nullable) is None
        # and __fields_set__ contains the field
        if self.instrument_type is None and "instrument_type" in self.__fields_set__:
            _dict['instrumentType'] = None

        # set to None if cash_flow_type (nullable) is None
        # and __fields_set__ contains the field
        if self.cash_flow_type is None and "cash_flow_type" in self.__fields_set__:
            _dict['cashFlowType'] = None

        # set to None if instrument_id (nullable) is None
        # and __fields_set__ contains the field
        if self.instrument_id is None and "instrument_id" in self.__fields_set__:
            _dict['instrumentId'] = None

        # set to None if leg_id (nullable) is None
        # and __fields_set__ contains the field
        if self.leg_id is None and "leg_id" in self.__fields_set__:
            _dict['legId'] = None

        # set to None if source_transaction_id (nullable) is None
        # and __fields_set__ contains the field
        if self.source_transaction_id is None and "source_transaction_id" in self.__fields_set__:
            _dict['sourceTransactionId'] = None

        # set to None if pay_receive (nullable) is None
        # and __fields_set__ contains the field
        if self.pay_receive is None and "pay_receive" in self.__fields_set__:
            _dict['payReceive'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CashFlowLineage:
        """Create an instance of CashFlowLineage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CashFlowLineage.parse_obj(obj)

        _obj = CashFlowLineage.parse_obj({
            "instrument_type": obj.get("instrumentType"),
            "cash_flow_type": obj.get("cashFlowType"),
            "instrument_id": obj.get("instrumentId"),
            "leg_id": obj.get("legId"),
            "source_transaction_id": obj.get("sourceTransactionId"),
            "pay_receive": obj.get("payReceive")
        })
        return _obj
