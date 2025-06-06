from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    ForeignKey,
    Boolean,
)

from ...database import Base


class PubmedUserDocumentModel(Base):
    __tablename__ = "pubmed_user_documents"

    id = Column(Integer, primary_key=True)
    pubmed_id = Column(
        Integer,
        ForeignKey('pubmed.id'),
        nullable=False,
    )
    user_document_id = Column(
        Integer,
        ForeignKey('user_documents.id'),
        nullable=False,
    )
    is_deleted = Column(Boolean, nullable=True)
    updated_at = Column(
        DateTime,
        nullable=False,
        # https://stackoverflow.com/questions/58776476/why-doesnt-freezegun-work-with-sqlalchemy-default-values
        default=lambda: datetime.utcnow(),
        onupdate=lambda: datetime.utcnow(),
    )
