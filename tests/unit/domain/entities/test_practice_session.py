import datetime
from datetime import datetime

import pytest

from src.domain.entities.practice_session import PracticeSession
from src.domain.value_objects.session_state import SessionState


@pytest.fixture
def session():
    return PracticeSession("session_123", "cellist_456")


def test_cannot_stop_session_before_starting(session):
    result = session.stop()
    assert result is False
    assert session.state == SessionState.NOT_STARTED


def test_can_start_session(session):
    result = session.start()

    assert result is True
    assert session.state == SessionState.ACTIVE


def test_cannot_start_already_started_session(session):
    session.start()

    result = session.start()
    assert result is False
    assert session.state == SessionState.ACTIVE


def test_cannot_restart_stopped_session(session):
    session.start()
    session.stop()

    result = session.start()
    assert result is False
    assert session.state == SessionState.STOPPED


def test_can_stop_active_session(session):
    session.start()

    result = session.stop()
    assert result is True
    assert session.state == SessionState.STOPPED


def test_can_add_piece_to_inactive_session(session):
    result = session.add_piece("Fur Elise")
    assert result is True
    assert "Fur Elise" in session.get_pieces()


def test_can_add_piece_to_active_session(session):
    session.start()

    result = session.add_piece("Fur Elise")
    assert result is True
    assert "Fur Elise" in session.get_pieces()


def test_cannot_add_piece_to_stopped_session(session):
    session.start()
    session.stop()

    result = session.add_piece("Fur Elise")
    assert result is False
    assert "Fur Elise" not in session.get_pieces()


def test_adding_existing_piece_succeeds(session):
    session.start()
    session.add_piece("Fur Elise")

    result = session.add_piece("Fur Elise")
    assert result is True
    assert len(session.get_pieces()) == 1


def test_cam_get_pieces_from_session(session):
    session.start()
    session.add_piece("bach_suite_1")
    session.add_piece("dvorak_concerto")

    pieces = session.get_pieces()
    assert len(pieces) == 2
    assert "bach_suite_1" in pieces
    assert "dvorak_concerto" in pieces


def test_start_time_set_when_session_starts(session):
    assert session.start_time is None

    session.start()
    assert session.start_time is not None
    assert isinstance(session.start_time, datetime)


def test_session_belongs_to_specific_cellist(session):
    assert session.cellist_id == "cellist_456"
