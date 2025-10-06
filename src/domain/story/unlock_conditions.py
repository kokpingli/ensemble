class UnlockConditions:
    def __init__(self, required_goals_count: int):
        self.required_goals_count = required_goals_count

    def is_satisfied(self, goals_met: int) -> bool:
        return goals_met >= self.required_goals_count
