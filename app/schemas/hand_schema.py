from pydantic import BaseModel, Field
from typing import List, Optional

class OpponentSchema(BaseModel):
    name: str
    position: str
    stack: float
    notes: Optional[str] = "None"

class ActionHistorySchema(BaseModel):
    player: str
    action: str
    amount: Optional[float] = 0.0

class HandCreateSchema(BaseModel):
    game_type: str
    hero_hand: List[str]
    board: List[str]
    hero_position: str
    hero_stack: float
    pot_size: float
    action_history: List[ActionHistorySchema]
    opponents: List[OpponentSchema]