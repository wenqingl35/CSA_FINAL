def build_poker_prompt(data):

    # Build opponent descriptions
    opponents_info = "\n".join([
        f"- {op['name']} (Pos: {op['position']}, Stack: {op['stack']}, Notes: {op.get('notes', 'None')})"
        for op in data.get('opponents', [])
    ])

    # Find Hero's most recent action
    played_action = None

    actions = data.get("action_history", [])

    for action in reversed(actions):
        if action.get("player", "").lower() == "hero":
            played_action = action.get("action")
            break

    return f"""
You are a professional poker coach.

Analyze this poker hand and provide coaching.

Requirements:
- Estimate Hero's equity versus likely opponent ranges.
- Estimate opponent ranges based on positions, stack sizes, notes, and action history.
- Compare Hero's actual action to the strategically preferred action.
- Determine whether Hero made any mistakes.
- Explain optimal strategy.
- Give actionable coaching advice.
- You must use computed equity when forming recommendations.
- Return ONLY valid JSON.

HAND INFORMATION

Game Type: {data.get('game_type')}
Hero Hand: {data.get('hero_hand')}
Board: {data.get('board')}
Hero Position: {data.get('hero_position')}
Hero Stack: {data.get('hero_stack')}
Pot Size: {data.get('pot_size')}
Computed Equity (engine-based): {data.get('computed_equity')}

Opponents at Table:
{opponents_info}

Action History:
{data.get('action_history')}

Hero Actual Action:
{played_action}

Return ONLY valid JSON in exactly this format:

{{
  "played_action": "",
  "estimated_equity": 0.0,
  "recommended_action": "",
  "opponent_ranges": {{}},
  "mistakes": [],
  "strategy_explanation": "",
  "coach_advice": "",
  "confidence": 0.0
}}
"""