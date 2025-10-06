from src.domain.story.unlock_conditions import UnlockConditions


class TestUnlockConditions:
    def test_is_satisfied_when_goals_met_equals_required_count(self):
        unlock_conditions = UnlockConditions(required_goals_count=3)

        result = unlock_conditions.is_satisfied(goals_met=3)

        assert result is True

    def test_is_not_satisfied_when_goals_less_than_required_count(self):
        unlock_conditions = UnlockConditions(required_goals_count=3)

        result = unlock_conditions.is_satisfied(goals_met=2)

        assert result is False
