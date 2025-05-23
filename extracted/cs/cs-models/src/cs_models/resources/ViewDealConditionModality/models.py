from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    ForeignKey,
    String,
)

from ...database import Base


class ViewDealConditionModalityModel(Base):
    __tablename__ = "_view_deal_conditions_modalities"

    id = Column(Integer, primary_key=True)
    deal_id = Column(
        Integer,
        ForeignKey('deals.id'),
        nullable=False,
    )
    condition_id = Column(
        Integer,
        ForeignKey('conditions.id'),
        nullable=False,
    )
    modality = Column(
        String(191),
        nullable=True,
        index=True,
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        # https://stackoverflow.com/questions/58776476/why-doesnt-freezegun-work-with-sqlalchemy-default-values
        default=lambda: datetime.utcnow(),
        onupdate=lambda: datetime.utcnow(),
    )
