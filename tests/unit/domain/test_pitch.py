from unittest.mock import Mock
from src.domain.pitch import Pitch


def test_pitch_converts_using_injected_converter():
    mock_converter = Mock()
    mock_converter.to_note.return_value = "A4"

    pitch = Pitch(frequency=440.0, confidence=0.95, converter=mock_converter)
    note = pitch.to_note()
    
    assert note == "A4"
    mock_converter.to_note.assert_called_with(440.0)