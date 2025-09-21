from datetime import datetime

from src.domain.entities.practice_session import PracticeSession


class StartSessionUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, cellist_id: str, piece_ids: list[str]) -> str:

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        session_id = f"{cellist_id}_{timestamp}"

        session = PracticeSession(session_id, cellist_id)
        for piece_id in piece_ids:
            session.add_piece(piece_id)
        session.start()

        self.repository.save(session)
        return session_id