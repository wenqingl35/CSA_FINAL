import itertools

RANKS = "23456789TJQKA"


def _rank_value(card):
    """Convert card like 'Ah' -> rank value"""
    return RANKS.index(card[0])


def _is_pair(hero_hand):
    return hero_hand[0][0] == hero_hand[1][0]


def _is_suited(hero_hand):
    return hero_hand[0][1] == hero_hand[1][1]


def _hand_rank_score(hero_hand):
    """
    Preflop strength model (0–1 scale)
    Based on real poker heuristics.
    """

    r1 = _rank_value(hero_hand[0])
    r2 = _rank_value(hero_hand[1])

    high = max(r1, r2)
    low = min(r1, r2)

    # Pocket pairs
    if _is_pair(hero_hand):
        if high >= 11:      # JJ+
            return 0.85
        if high >= 8:       # 88–TT
            return 0.75
        return 0.65

    # Big cards
    if high >= 12 and low >= 11:  # AK
        return 0.80

    if high >= 12:  # AQ, AJ, KQ type
        score = 0.65
        if _is_suited(hero_hand):
            score += 0.05
        return score

    if high >= 10:  # JT, QJ, etc.
        score = 0.55
        if _is_suited(hero_hand):
            score += 0.05
        return score

    # Suited connectors
    if _is_suited(hero_hand) and abs(r1 - r2) == 1:
        return 0.60

    # Weak hands
    return 0.35


def _board_strength(board):
    """
    Simple board texture evaluation.
    """

    if not board:
        return 0.5

    ranks = [card[0] for card in board]

    # Paired board
    if len(set(ranks)) < len(ranks):
        return 0.65

    # High-card board
    high_cards = sum(RANKS.index(r) >= 10 for r in ranks)
    if high_cards >= 2:
        return 0.6

    # Connected-ish board (simplified)
    rank_values = sorted([RANKS.index(r) for r in ranks])
    if len(rank_values) >= 2:
        if max(rank_values) - min(rank_values) <= 4:
            return 0.6

    return 0.5


def estimate_hand_strength(hero_hand, board):
    """
    Final equity proxy (0–1)
    Combines:
    - hand strength
    - board texture adjustment
    """

    hand_score = _hand_rank_score(hero_hand)
    board_score = _board_strength(board)

    # weighted blend
    equity = (hand_score * 0.7) + (board_score * 0.3)

    # clamp between 0 and 1
    equity = max(0.0, min(1.0, equity))

    return round(equity, 2)