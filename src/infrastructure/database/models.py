"""SQLAlchemy ORM models for story domain."""

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class SectionModel(Base):
    __tablename__ = "sections"

    id = Column(String, primary_key=True)
    required_goals_count = Column(Integer, nullable=False)
    story_content = Column(Text, nullable=False)

    technical_goals = relationship("TechnicalGoalModel", back_populates="section")


class TechnicalGoalModel(Base):
    __tablename__ = "technical_goals"

    id = Column(Integer, primary_key=True, autoincrement=True)
    section_id = Column(String, ForeignKey("sections.id"), nullable=False)
    name = Column(String, nullable=False)
    completed = Column(Boolean, nullable=False, default=False)

    section = relationship("SectionModel", back_populates="technical_goals")
