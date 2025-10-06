from unittest.mock import Mock, patch

from src.domain.story.section import Section
from src.domain.story.story_fragment import StoryFragment
from src.domain.story.technical_goal import TechnicalGoal
from src.domain.story.unlock_conditions import UnlockConditions


class TestSection:
    def test_unlock_story_calls_successful_factory_when_conditions_met(self):
        goals = [
            TechnicalGoal("bow_hold", completed=True),
            TechnicalGoal("intonation", completed=True),
            TechnicalGoal("rhythm", completed=True),
            TechnicalGoal("dynamics", completed=False),
        ]
        unlock_conditions = UnlockConditions(required_goals_count=3)
        story_fragment = StoryFragment("The spirit smiled...")
        section = Section(
            technical_goals=goals,
            unlock_conditions=unlock_conditions,
            story_fragment=story_fragment,
        )

        with patch(
            "src.domain.story.unlock_result.UnlockResult.successful"
        ) as mock_successful:
            mock_successful.return_value = Mock()

            section.unlock_story()

            mock_successful.assert_called_once_with(story_fragment)

    def test_unlock_story_calls_unsuccessful_factory_when_conditions_not_met(self):
        goals = [
            TechnicalGoal("bow_hold", completed=True),
            TechnicalGoal("intonation", completed=True),
            TechnicalGoal("rhythm", completed=False),
            TechnicalGoal("dynamics", completed=False),
        ]
        unlock_conditions = UnlockConditions(required_goals_count=3)
        story_fragment = StoryFragment("The spirit smiled...")
        section = Section(
            technical_goals=goals,
            unlock_conditions=unlock_conditions,
            story_fragment=story_fragment,
        )

        with patch(
            "src.domain.story.unlock_result.UnlockResult.unsuccessful"
        ) as mock_unsuccessful:
            mock_unsuccessful.return_value = Mock()

            section.unlock_story()

            mock_unsuccessful.assert_called_once()

    def test_update_goal_completion_updates_matching_goals(self):
        goals = [
            TechnicalGoal("bow_hold", completed=False),
            TechnicalGoal("intonation", completed=False),
            TechnicalGoal("rhythm", completed=False),
            TechnicalGoal("dynamics", completed=False),
        ]
        unlock_conditions = UnlockConditions(required_goals_count=3)
        story_fragment = StoryFragment("The spirit smiled...")
        section = Section(
            technical_goals=goals,
            unlock_conditions=unlock_conditions,
            story_fragment=story_fragment,
        )
        goal_updates = {"bow_hold": True, "intonation": True}

        section.update_goal_completion(goal_updates)

        assert goals[0].is_completed() is True
        assert goals[1].is_completed() is True
        assert goals[2].is_completed() is False
        assert goals[3].is_completed() is False
