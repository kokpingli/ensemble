"""Story section entity with unlock logic."""

from typing import List

from .story_fragment import StoryFragment
from .technical_goal import TechnicalGoal
from .unlock_conditions import UnlockConditions
from .unlock_result import UnlockResult


class Section:
    def __init__(
        self,
        section_id: str,
        technical_goals: List[TechnicalGoal],
        unlock_conditions: UnlockConditions,
        story_fragment: StoryFragment,
    ):
        self.id = section_id
        self.technical_goals = technical_goals
        self.unlock_conditions = unlock_conditions
        self.story_fragment = story_fragment

    def update_goal_completion(self, goal_updates: dict):
        for goal in self.technical_goals:
            if goal.name in goal_updates:
                goal.completed = goal_updates[goal.name]

    def unlock_story(self) -> UnlockResult:
        if self._is_unlocked():
            return UnlockResult.successful(self.story_fragment)
        return UnlockResult.unsuccessful()

    def _is_unlocked(self) -> bool:
        goals_met = sum(1 for goal in self.technical_goals if goal.is_completed())
        return self.unlock_conditions.is_satisfied(goals_met)
