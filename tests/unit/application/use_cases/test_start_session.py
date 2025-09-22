from datetime import datetime
from unittest.mock import Mock, patch

from src.application.use_cases.start_session import StartSessionUseCase


@patch("src.application.use_cases.start_session.datetime")
def test_creates_and_saves_session_with_pieces(mock_datetime):
    mock_datetime.now.return_value = datetime(2024, 12, 21, 14, 30, 52)

    mock_repository = Mock()
    use_case = StartSessionUseCase(mock_repository)

    session_id = use_case.execute("cellist_123", ["bach_suite_1", "dvorak"])

    mock_repository.save.assert_called_once()
    assert session_id is not None

    saved_session = mock_repository.save.call_args[0][0]
    assert saved_session.cellist_id == "cellist_123"
    assert session_id == "cellist_123_20241221_143052"
    assert len(saved_session.pieces) == 2


@patch("src.application.use_cases.start_session.datetime")
def test_can_start_session_without_pieces(mock_datetime):
    mock_datetime.now.return_value = datetime(2024, 12, 21, 14, 30, 52)

    mock_repository = Mock()
    use_case = StartSessionUseCase(mock_repository)

    session_id = use_case.execute("cellist_789", [])

    mock_repository.save.assert_called_once()
    assert session_id is not None

    saved_session = mock_repository.save.call_args[0][0]
    assert saved_session.cellist_id == "cellist_789"
    assert session_id == "cellist_789_20241221_143052"
    assert len(saved_session.pieces) == 0
