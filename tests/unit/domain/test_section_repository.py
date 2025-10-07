from src.domain.story.section import Section
from src.domain.story.story_fragment import StoryFragment
from src.domain.story.technical_goal import TechnicalGoal
from src.domain.story.unlock_conditions import UnlockConditions
from src.infrastructure.repositories.sqlalchemy_section_repository import \
    SQLAlchemySectionRepository


class TestSQLAlchemySectionRepository:
    def test_save_and_get_by_id_persists_section_data(self):
        goals = [
            TechnicalGoal("bow_hold", completed=False),
            TechnicalGoal("intonation", completed=False),
        ]
        unlock_conditions = UnlockConditions(required_goals_count=2)
        story_fragment = StoryFragment("The spirit smiled...")
        section = Section(
            section_id="section_123",
            technical_goals=goals,
            unlock_conditions=unlock_conditions,
            story_fragment=story_fragment,
        )

        repository = SQLAlchemySectionRepository()
        repository.save(section)

        retrieved_section = repository.get_by_id("section_123")

        assert retrieved_section.technical_goals[0].name == "bow_hold"
        assert retrieved_section.unlock_conditions.required_goals_count == 2
        assert retrieved_section.story_fragment.content == "The spirit smiled..."
