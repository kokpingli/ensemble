from unittest.mock import Mock

from src.application.unlock_story_use_case import UnlockStoryUseCase


class TestUnlockStoryUseCase:
    def test_unlock_story_updates_goals_and_calls_section_unlock(self):
        goal_updates = {
            "bow_hold": True,
            "intonation": True,
            "rhythm": True,
            "dynamics": False,
        }
        mock_section_repository = Mock()
        mock_section = Mock()
        mock_section_repository.get_by_id.return_value = mock_section
        use_case = UnlockStoryUseCase(mock_section_repository)

        use_case.execute(section_id="section456", goal_updates=goal_updates)

        mock_section_repository.get_by_id.assert_called_once_with("section456")
        mock_section.update_goal_completion.assert_called_once_with(goal_updates)
        mock_section.unlock_story.assert_called_once()
