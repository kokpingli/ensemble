"""Pydantic schemas for section-related API requests and responses."""

from pydantic import BaseModel


class UnlockStoryRequest(BaseModel):
    goal_updates: dict[str, bool]


class UnlockStoryResponse(BaseModel):
    eligible: bool
    story_fragment: str
