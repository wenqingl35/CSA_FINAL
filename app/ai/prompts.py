def build_poker_prompt(data):

    return f"""
You are a professional poker coach.

Analyze this poker hand.

You must:
- estimate equity
- estimate villain range
- determine if hero made mistakes
- suggest better actions
- explain the strategy
- give coaching advice

HAND INFORMATION

Game Type:
{data.get('game_type')}

Hero Hand:
{data.get('hero_hand')}

Board:
{data.get('board')}

Hero Position:
{data.get('hero_position')}

Villain Position:
{data.get('villain_position')}

Hero Stack:
{data.get('hero_stack')}

Villain Stack:
{data.get('villain_stack')}

Pot Size:
{data.get('pot_size')}

Action History:
{data.get('action_history')}

Villain Notes:
{data.get('villain_notes')}

Return ONLY valid JSON.

JSON format:

{{
    "estimated_equity": 0.0,
    "recommended_action": "",
    "villain_range": [],
    "mistakes": [],
    "strategy_explanation": "",
    "coach_advice": "",
    "confidence": 0.0
}}
"""