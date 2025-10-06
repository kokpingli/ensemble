from .story_fragment import StoryFragment


class UnlockResult:
    def __init__(self, eligible: bool, story_fragment: StoryFragment = None):
        self._eligible = eligible
        self._story_fragment = story_fragment

    @classmethod
    def successful(cls, story_fragment: StoryFragment):
        return cls(eligible=True, story_fragment=story_fragment)

    @classmethod
    def unsuccessful(cls):
        return cls(eligible=False, story_fragment=None)

    def is_eligible(self) -> bool:
        return self._eligible

    def get_story_fragment(self) -> StoryFragment:
        return self._story_fragment
