from src.domain.story.story_fragment import StoryFragment
from src.domain.story.unlock_result import UnlockResult


class TestUnlockResult:
    def test_successful_unlock_result_contains_story_fragment(self):
        story_fragment = StoryFragment(content="The spirit smiled...")

        result = UnlockResult.successful(story_fragment)

        assert result.is_eligible() is True
        assert result.get_story_fragment() == story_fragment

    def test_unsuccessful_unlock_result_is_not_eligible(self):
        result = UnlockResult.unsuccessful()

        assert result.is_eligible() is False
        assert result.get_story_fragment() is None
