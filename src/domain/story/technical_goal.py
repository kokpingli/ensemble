"""Value object representing a practice technical goal."""


class TechnicalGoal:
    def __init__(self, name: str, completed: bool):
        self.name = name
        self.completed = completed

    def is_completed(self) -> bool:
        return self.completed
