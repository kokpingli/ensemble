from fastapi import APIRouter, Depends

from src.application.unlock_story_use_case import UnlockStoryUseCase

from ..dependencies import get_unlock_story_use_case
from ..schemas.section import UnlockStoryRequest, UnlockStoryResponse

router = APIRouter()


@router.post("/sections/{section_id}/unlock", response_model=UnlockStoryResponse)
def unlock_story(
    section_id: str,
    request: UnlockStoryRequest,
    use_case: UnlockStoryUseCase = Depends(get_unlock_story_use_case),
) -> UnlockStoryResponse:
    result = use_case.execute(section_id, request.goal_updates)
    return UnlockStoryResponse(
        eligible=result.is_eligible(),
        story_fragment=result.get_story_fragment().content,
    )
