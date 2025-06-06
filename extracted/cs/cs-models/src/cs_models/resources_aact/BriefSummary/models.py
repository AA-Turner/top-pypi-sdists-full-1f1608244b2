from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)

from ...aact_database import Base


class BriefSummaryModel(Base):
    __tablename__ = 'brief_summaries'
    __table_args__ = (
        {'schema': 'ctgov'},
    )

    id = Column(Integer, primary_key=True)
    nct_id = Column(
        String,
        ForeignKey('ctgov.studies.nct_id'),
        nullable=False,
    )
    description = Column(Text)

    def __repr__(self):
        return "<BriefSummary(id='{}', nct_id='{}', description='{}'>"\
            .format(self.id, self.nct_id, self.description)
