from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    String,
    Float,
    Boolean,
)

from ...database import Base


class InsightsRawModel(Base):
    __tablename__ = "insights_raw"

    id = Column(Integer, primary_key=True)
    source_type = Column(
        String(50),
        nullable=False
    )
    source_id = Column(Integer, nullable=False)
    insight_type = Column(
        String(50), nullable=False,
    )
    insight_name = Column(
        String(191),
    )
    score = Column(Float, nullable=True)
    preferred = Column(Boolean, nullable=True)
    linked = Column(Boolean, nullable=True)
    count = Column(Integer, nullable=True)
    date = Column(DateTime, nullable=True)
    updated_at = Column(
        DateTime,
        nullable=False,
        # https://stackoverflow.com/questions/58776476/why-doesnt-freezegun-work-with-sqlalchemy-default-values
        default=lambda: datetime.utcnow(),
        onupdate=lambda: datetime.utcnow(),
    )
