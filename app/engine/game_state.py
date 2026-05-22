from dataclasses import dataclass
from typing import List, Optional

@dataclass
class PlayerState:
    name: str
    stack: float
    position: str
    bet: float
    has_folded: bool

@dataclass
class GameState:
    hero_hand: List[str]
    board: List[str]

    pot_size: float
    current_bet: float

    hero_position: str
    villain_position: str

    stack_hero: float
    stack_villain: float

    street: str  # preflop/flop/turn/river

    action_history: List[str]

    players: List[PlayerState]