"""Value object representing a piece of story content."""


class StoryFragment:
    def __init__(self, content: str):
        self.content = content

    def __eq__(self, other):
        if not isinstance(other, StoryFragment):
            return False
        return self.content == other.content
