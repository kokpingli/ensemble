"""SQLAlchemy implementation of SectionRepository."""

from src.domain.story.section import Section
from src.domain.story.section_repository import SectionRepository
from src.domain.story.story_fragment import StoryFragment
from src.domain.story.technical_goal import TechnicalGoal
from src.domain.story.unlock_conditions import UnlockConditions
from src.infrastructure.database.connection import DatabaseConnection
from src.infrastructure.database.models import SectionModel, TechnicalGoalModel


class SQLAlchemySectionRepository(SectionRepository):
    def __init__(self, db_connection: DatabaseConnection = None):
        self.db = db_connection or DatabaseConnection()
        self.db.create_tables()

    def get_by_id(self, section_id: str) -> Section:
        session = self.db.get_session()
        try:
            section_model = (
                session.query(SectionModel)
                .filter(SectionModel.id == section_id)
                .first()
            )
            if not section_model:
                return None

            goals = [
                TechnicalGoal(goal_model.name, goal_model.completed)
                for goal_model in section_model.technical_goals
            ]
            unlock_conditions = UnlockConditions(section_model.required_goals_count)
            story_fragment = StoryFragment(section_model.story_content)

            return Section(section_id, goals, unlock_conditions, story_fragment)
        finally:
            session.close()

    def save(self, section: Section) -> None:
        session = self.db.get_session()
        try:
            section_model = SectionModel(
                id=section.id,
                required_goals_count=section.unlock_conditions.required_goals_count,
                story_content=section.story_fragment.content,
            )
            session.add(section_model)
            session.flush()

            for goal in section.technical_goals:
                goal_model = TechnicalGoalModel(
                    section_id=section.id, name=goal.name, completed=goal.completed
                )
                session.add(goal_model)

            session.commit()
        finally:
            session.close()
