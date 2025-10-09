from fastapi import APIRouter, Depends

from src.application.unlock_story_use_case import UnlockStoryUseCase

from ..dependencies import get_unlock_story_use_case

router = APIRouter()


@router.post("/sections/{section_id}/unlock")
def unlock_story(
    section_id: str,
    request: dict,
    use_case: UnlockStoryUseCase = Depends(get_unlock_story_use_case),
):
    result = use_case.execute(section_id, request["goal_updates"])
    return {
        "eligible": result.is_eligible(),
        "story_fragment": result.get_story_fragment().content,
    }
