from typing import Dict, Any


def build_coaching_prompt(data: Dict[str, Any]) -> str:

    return f"""
Analyze this poker hand in detail.

========================
GAME INFORMATION
========================

Game Type:
{data.get('game_type', 'Unknown')}

Stakes:
{data.get('stakes', 'Unknown')}

Street:
{data.get('street', 'Unknown')}

========================
POSITIONS
========================

Hero Position:
{data.get('hero_position', 'Unknown')}

Villain Position:
{data.get('villain_position', 'Unknown')}

========================
STACKS
========================

Hero Stack:
{data.get('hero_stack', 'Unknown')}

Villain Stack:
{data.get('villain_stack', 'Unknown')}

SPR:
{data.get('spr', 'Unknown')}

========================
BOARD
========================

Board:
{data.get('board', 'Unknown')}

Hero Hand:
{data.get('hero_hand', 'Unknown')}

========================
ACTION HISTORY
========================

{data.get('action_history', 'Unknown')}

========================
ANALYSIS
========================

Equity:
{data.get('equity', 'Unknown')}

Pot Odds:
{data.get('pot_odds', 'Unknown')}

Solver Recommendation:
{data.get('recommendation', 'Unknown')}

Actual Action:
{data.get('played_action', 'Unknown')}

========================
VILLAIN PROFILE
========================

VPIP:
{data.get('vpip', 'Unknown')}

PFR:
{data.get('pfr', 'Unknown')}

Aggression Factor:
{data.get('aggression_factor', 'Unknown')}

Fold To CBet:
{data.get('fold_to_cbet', 'Unknown')}

Notes:
{data.get('villain_notes', 'Unknown')}

========================
YOUR TASK
========================

Return ONLY valid JSON.

Required JSON structure:

{{
  "summary": "Short overview of the hand",

  "street_analysis": {{
    "preflop": {{
      "mistake": true,
      "severity": "low",
      "explanation": "",
      "better_action": ""
    }},
    "flop": {{
      "mistake": false,
      "severity": "none",
      "explanation": "",
      "better_action": ""
    }},
    "turn": {{
      "mistake": false,
      "severity": "none",
      "explanation": "",
      "better_action": ""
    }},
    "river": {{
      "mistake": true,
      "severity": "high",
      "explanation": "",
      "better_action": ""
    }}
  }},

  "gto_analysis": "",

  "exploitative_adjustments": [
    "",
    ""
  ],

  "leaks_detected": [
    "",
    ""
  ],

  "recommended_next_move": "",

  "confidence": 0.0,

  "coach_advice": ""
}}

Rules:
- Be concise
- Be strategically accurate
- Explain WHY actions are good/bad
- Include exploitative adjustments
- Focus on poker EV
- Do not include markdown
- Do not include commentary outside JSON
"""