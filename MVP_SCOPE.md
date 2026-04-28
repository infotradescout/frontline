# MVP Scope: Frontline Prototype 0.1

## Goal

Deliver one playable generated combat match.

## Required Features

- FPS movement
- One rifle
- One generated arena
- Randomized cover
- Random loot spawn
- Basic bots
- Shrinking storm circle
- Win/loss screen
- New match creates a new layout
- Performance mode as default configuration

## Non-Goals

- Accounts
- Cosmetics
- Online matchmaking
- Lore/story campaign
- Huge open world

## Acceptance Criteria

- A match starts in under 30 seconds in editor PIE
- Restarting creates a different playable layout using a seed
- One complete match loop can finish in 5 minutes or less
- Player can win or lose and cleanly return to restart flow
- Performance mode runs at stable 60 FPS on weak hardware target
- No major frame spikes during spawn, zone updates, or combat moments
