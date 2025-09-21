from unittest.mock import Mock

from src.application.use_cases.stop_session import StopSessionUseCase
from src.domain.entities.practice_session import PracticeSession
from src.domain.exceptions.domain_exceptions import SessionNotFound


def test_cannot_stop_session_that_does_not_exist():
    mock_repository = Mock()
    mock_repository.get_by_id.side_effect = SessionNotFound("Session not found")

    use_case = StopSessionUseCase(mock_repository)

    result = use_case.execute("nonexistent_session", "cellist_000")

    assert result is False
    mock_repository.get_by_id.assert_called_once_with("nonexistent_session")
    mock_repository.save.assert_not_called()

def test_can_stop_active_session():
    session = PracticeSession("session_001", "cellist_001")
    session.start()

    mock_repository = Mock()
    mock_repository.get_by_id.return_value = session

    use_case = StopSessionUseCase(mock_repository)
    result = use_case.execute("session_001", "cellist_001")

    assert result is True
    mock_repository.save.assert_called_once_with(session)

def test_cannot_stop_another_cellist_session():
    session = PracticeSession("session_002", "cellist_002")
    session.start()

    mock_repository = Mock()
    mock_repository.get_by_id.return_value = session

    use_case = StopSessionUseCase(mock_repository)
    result = use_case.execute("session_002", "cellist_999")

    assert result is False
    mock_repository.save.assert_not_called()

def test_cannot_stop_already_stopped_session():
    session = PracticeSession("session_003", "cellist_003")
    session.start()
    session.stop()

    mock_repository = Mock()
    mock_repository.get_by_id.return_value = session

    use_case = StopSessionUseCase(mock_repository)
    result = use_case.execute("session_003", "cellist_003")

    # Debug prints:
    print(f"Result: {result}")
    print(f"get_by_id called: {mock_repository.get_by_id.called}")
    print(f"save called: {mock_repository.save.called}")

    assert result is False
    mock_repository.save.assert_not_called()