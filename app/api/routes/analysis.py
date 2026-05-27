from fastapi import APIRouter

from app.ai.coaching_engine import CoachingEngine
from app.schemas.analysis_schema import (
    HandAnalysisRequest
)

router = APIRouter()

coach = CoachingEngine()


@router.post("/analyze")
async def analyze_hand(
    hand: HandAnalysisRequest
):

    result = await coach.analyze_hand(
        hand.dict()
    )

    return result