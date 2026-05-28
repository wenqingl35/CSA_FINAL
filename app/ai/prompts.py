def build_poker_prompt(data):
    # Dynamically build opponent details for any number of players
    opponents_info = "\n".join([
        f"- {op['name']} (Pos: {op['position']}, Stack: {op['stack']}, Notes: {op.get('notes', 'None')})"
        for op in data.get('opponents', [])
    ])

    return f""" You are a professional poker coach. Analyze this poker hand. You must:
- estimate equity against opponents
- estimate opponent ranges
- determine if hero made mistakes
- suggest better actions
- explain the strategy
- give coaching advice

HAND INFORMATION
Game Type: {data.get('game_type')}
Hero Hand: {data.get('hero_hand')}
Board: {data.get('board')}
Hero Position: {data.get('hero_position')}
Hero Stack: {data.get('hero_stack')}
Pot Size: {data.get('pot_size')}
Opponents at Table:
{opponents_info}
Action History: {data.get('action_history')}

Return ONLY valid JSON. JSON format:
{{
  "estimated_equity": 0.0,
  "recommended_action": "",
  "opponent_ranges": {{}}, 
  "mistakes": [],
  "strategy_explanation": "",
  "coach_advice": "",
  "confidence": 0.0
}} """