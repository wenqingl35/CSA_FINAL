from fastapi import APIRouter, Depends
from app.schemas.hand_schema import HandCreateSchema
from app.services.analysis_service import analyze_spot

router = APIRouter()

@router.post("/analyze")
async def analyze_hand(hand_data: HandCreateSchema): # <-- FastAPI automatically validates your new JSON here
    # Pass the validated Pydantic model data down to your service layer
    result = await analyze_spot(hand_data.dict())
    return result