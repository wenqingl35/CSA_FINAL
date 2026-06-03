def detect_mistakes(equity, played_action, hero_hand, board, pot_size):
    """
    Simple rule-based poker mistake detector.
    NOT AI — deterministic logic for project credibility.
    """

    mistakes = []

    if played_action is None:
        return ["No hero action detected"]

    action = played_action.lower()

    # ----------------------------
    # RULE 1: Too weak to call
    # ----------------------------
    if action == "call" and equity < 0.45:
        mistakes.append(
            "Calling with weak equity (<45%) is usually -EV. Consider folding or re-evaluating pot odds."
        )

    # ----------------------------
    # RULE 2: Strong hand not aggressive
    # ----------------------------
    if action == "call" and equity > 0.70:
        mistakes.append(
            "You have strong equity but only called. Consider raising for value."
        )

    # ----------------------------
    # RULE 3: Folding strong hands (approx heuristic)
    # ----------------------------
    if action == "fold" and equity > 0.65:
        mistakes.append(
            "Folding strong equity hand may be too tight. Consider continuing in the hand."
        )

    # ----------------------------
    # RULE 4: Weak aggression
    # ----------------------------
    if action in ["raise", "bet"] and equity < 0.40:
        mistakes.append(
            "Aggressive action with weak equity can be high risk unless bluffing intentionally."
        )

    # ----------------------------
    # RULE 5: Default safe message
    # ----------------------------
    if not mistakes:
        mistakes.append("No obvious rule-based mistakes detected")

    return mistakes