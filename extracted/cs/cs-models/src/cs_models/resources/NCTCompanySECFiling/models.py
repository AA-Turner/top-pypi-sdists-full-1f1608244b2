from sqlalchemy import (
    Integer,
    Column,
    Boolean,
    DateTime,
    ForeignKey
)
from datetime import datetime
from ...database import Base


class NCTCompanySECFilingModel(Base):
    __tablename__ = "nct_companies_sec_filings"

    id = Column(Integer, primary_key=True)
    nct_study_id = Column(
        Integer,
        ForeignKey('nct_study.id'),
        nullable=False,
    )
    sec_filing_id = Column(
        Integer,
        ForeignKey('companies_sec_filings.id'),
        nullable=False,
    )
    sec_filing_date = Column(DateTime, nullable=True)
    is_deleted = Column(
        Boolean,
        nullable=True
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        # https://stackoverflow.com/questions/58776476/why-doesnt-freezegun-work-with-sqlalchemy-default-values
        default=lambda: datetime.utcnow(),
        onupdate=lambda: datetime.utcnow(),
    )
