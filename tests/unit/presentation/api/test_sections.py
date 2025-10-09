from unittest.mock import Mock

from fastapi.testclient import TestClient


class TestSectionsAPI:
    def test_unlock_story_returns_successful_response_when_eligible(self):
        mock_use_case = Mock()
        mock_unlock_result = Mock()
        mock_unlock_result.is_eligible.return_value = True
        mock_story_fragment = Mock()
        mock_story_fragment.content = "The spirit smiled..."
        mock_unlock_result.get_story_fragment.return_value = mock_story_fragment
        mock_use_case.execute.return_value = mock_unlock_result

        from src.presentation.dependencies import get_unlock_story_use_case
        from src.presentation.main import app

        # Override the dependency with our mock
        app.dependency_overrides[get_unlock_story_use_case] = lambda: mock_use_case
        client = TestClient(app)

        goal_updates = {
            "bow_hold": True,
            "intonation": True,
            "rhythm": True,
            "dynamics": False,
        }

        response = client.post(
            "/api/sections/section_123/unlock", json={"goal_updates": goal_updates}
        )

        assert response.status_code == 200
        assert response.json() == {
            "eligible": True,
            "story_fragment": "The spirit smiled...",
        }
