from pydantic import BaseModel


class HandAnalysisRequest(BaseModel):

    game_type: str

    hero_hand: str

    board: str

    hero_position: str

    villain_position: str

    hero_stack: float

    villain_stack: float

    pot_size: float

    action_history: str

    villain_notes: str