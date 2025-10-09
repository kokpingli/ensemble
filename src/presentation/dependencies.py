from src.application.unlock_story_use_case import UnlockStoryUseCase
from src.infrastructure.repositories.sqlalchemy_section_repository import \
    SQLAlchemySectionRepository


def get_unlock_story_use_case() -> UnlockStoryUseCase:
    repository = SQLAlchemySectionRepository()
    return UnlockStoryUseCase(repository)
