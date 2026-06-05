// Valid ranks and suits
const RANKS = "23456789TJQKA";
const SUITS = "shdc";

/**
 * Format a single card like:
 *   "aS" → "As"
 *   "td" → "Td"
 *   "7H" → "7h"
 *
 * Returns null if invalid.
 */
export function formatCard(card) {
  if (!card || card.length !== 2) return null;

  const rank = card[0].toUpperCase();
  const suit = card[1].toLowerCase();

  if (!RANKS.includes(rank) || !SUITS.includes(suit)) return null;

  return rank + suit;
}

/**
 * Parse a string like:
 *   "As Kd" → ["As", "Kd"]
 *   "askd" → ["As", "Kd"]
 *   "  As   Kd  " → ["As", "Kd"]
 *
 * Returns [] if invalid.
 */
export function parseCardInput(input) {
  if (!input) return [];

  // Remove spaces, split into 2‑char chunks
  const cleaned = input.replace(/\s+/g, "").match(/.{1,2}/g) || [];

  return cleaned.map(formatCard).filter(Boolean);
}

/**
 * Detect duplicate cards across multiple groups.
 *
 * Example:
 *   hasDuplicateCards(heroHand, board)
 *   hasDuplicateCards(heroHand, board, showdown)
 *
 * Returns true if ANY card appears more than once.
 */
export function hasDuplicateCards(...cardGroups) {
  const seen = new Set();

  for (const group of cardGroups) {
    if (!group) continue;

    for (const card of group) {
      if (seen.has(card)) return true;
      seen.add(card);
    }
  }

  return false;
}