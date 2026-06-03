from app.ai.coaching_engine import CoachingEngine
from app.engine.simple_evaluator import estimate_hand_strength
from app.engine.mistake_detector import detect_mistakes

mc = CoachingEngine()


async def analyze_spot(request: dict):

    # STEP 1: compute equity (deterministic poker logic)
    equity = estimate_hand_strength(
        request.get("hero_hand", []),
        request.get("board", [])
    )

    request["computed_equity"] = equity

    # STEP 2: AI analysis
    engine_result = await mc.analyze_hand(request)

    if not engine_result.get("success"):
        return {
            "success": False,
            "error": engine_result.get("error", "AI Analysis failed")
        }

    ai_data = engine_result.get("data", {})

    # STEP 3: find hero action
    played_action = None

    for action in reversed(request.get("action_history", [])):
        if action.get("player", "").lower() == "hero":
            played_action = action.get("action")
            break

    # STEP 4: rule-based mistake detection (NEW)
    rule_mistakes = detect_mistakes(
        equity,
        played_action,
        request.get("hero_hand", []),
        request.get("board", []),
        request.get("pot_size", 0)
    )

    # STEP 5: merge everything
    ai_data["played_action"] = played_action
    ai_data["computed_equity"] = equity
    ai_data["rule_based_mistakes"] = rule_mistakes

    return ai_data