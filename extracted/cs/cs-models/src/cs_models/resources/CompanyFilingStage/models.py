from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    ForeignKey,
    Boolean,
)

from ...database import Base


class CompanyFilingStageModel(Base):
    __tablename__ = "company_filing_stage"

    id = Column(Integer, primary_key=True)
    company_filing_id = Column(
        Integer,
        ForeignKey('company_filings.id'),
        nullable=False,
    )
    stage = Column(
        Integer,
        nullable=False,
    )
    preferred = Column(Boolean, nullable=True)
    updated_at = Column(
        DateTime,
        nullable=False,
        # https://stackoverflow.com/questions/58776476/why-doesnt-freezegun-work-with-sqlalchemy-default-values
        default=lambda: datetime.utcnow(),
        onupdate=lambda: datetime.utcnow(),
    )
