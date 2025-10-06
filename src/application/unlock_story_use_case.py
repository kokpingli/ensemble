"""Use case for unlocking story content based on practice goals."""


class UnlockStoryUseCase:
    def __init__(self, section_repository):
        self.section_repository = section_repository

    def execute(self, section_id: str, goal_updates: dict):
        section = self.section_repository.get_by_id(section_id)
        section.update_goal_completion(goal_updates)
        return section.unlock_story()
