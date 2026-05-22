from pydantic import BaseModel
from typing import List, Optional

class Action(BaseModel):
   street: str
   player: str
   action: str
   amount: Optional[float] = None

class AnalysisRequest(BaseModel):
   hero_cards: List[str]
   board: List[str]
   pot: float
   actions: List[Action]
