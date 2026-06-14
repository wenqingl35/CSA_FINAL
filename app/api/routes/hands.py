from fastapi import APIRouter

from app.engine.game_state_manager import game_state
from app.schemas.hand_schema import HandCreateSchema
from app.services.analysis_service import analyze_spot

router = APIRouter()


@router.post("/hand/start")
async def start_hand(hand_data: HandCreateSchema):

    game_state.start_hand(hand_data.dict())

    return {
        "success": True,
        "message": "Hand started"
    }


@router.post("/hand/update")
async def update_hand(data: dict):

    game_state.update_state (
    board=data.get("board"),
    actions = data.get("actions") or data.get("action_history")
    )

    return {
        "success": True,
        "current_hand": game_state.get_hand()
    }


@router.get("/hand/current")
async def current_hand():

    hand = game_state.get_hand()

    if not hand:
        return {
            "success": False,
            "error": "No active hand"
        }

    return await analyze_spot(hand)


@router.post("/hand/reset")
async def reset_hand():

    game_state.reset()

    return {
        "success": True,
        "message": "Hand reset"
    }