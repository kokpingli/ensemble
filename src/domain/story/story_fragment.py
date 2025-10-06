class StoryFragment:
    def __init__(self, content: str):
        self.content = content

    def __eq__(self, other):
        if not isinstance(other, StoryFragment):
            return False
        return self.content == other.content
