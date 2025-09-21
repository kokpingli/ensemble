from datetime import datetime
from src.domain.value_objects.session_state import SessionState


class PracticeSession:
    def __init__(self, session_id: str, cellist_id: str):
        self.id = session_id
        self.cellist_id = cellist_id
        self.start_time = None
        self.state = SessionState.NOT_STARTED
        self.pieces = set()

    def start(self):
        if self.state != SessionState.NOT_STARTED:
            return False
        self.state = SessionState.ACTIVE
        self.start_time = datetime.now()
        return True

    def stop(self):
        if self.state != SessionState.ACTIVE:
            return False
        self.state = SessionState.STOPPED
        return True
    
    def add_piece(self, piece_name: str):
        if self.state == SessionState.STOPPED:
            return False
        # Logic to add the piece would go here
        self.pieces.add(piece_name)
        return True
    
    def get_pieces(self):
        return set(self.pieces)