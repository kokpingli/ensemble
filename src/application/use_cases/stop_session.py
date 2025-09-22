"""Use case for stopping a practice session."""

import logging

from src.domain.exceptions.domain_exceptions import (
    SessionNotFound,
    UnauthorizedSessionAccess
)

logger = logging.getLogger(__name__)


class StopSessionUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, session_id: str, cellist_id: str) -> bool:
        try:
            session = self.repository.get_by_id(session_id)

            if session.cellist_id != cellist_id:
                raise UnauthorizedSessionAccess(
                    f"Session {session_id} belongs to different user"
                )

            success = session.stop()
            if success:
                self.repository.save(session)

            return success

        except (SessionNotFound, UnauthorizedSessionAccess) as e:
            logger.warning(f"Stop session failed: {e}")
            return False
