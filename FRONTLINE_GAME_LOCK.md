# FRONTLINE GAME LOCK

Frontline is an FPS battle royale prototype where every match generates a new battlefield.

## Core Rule

Every feature must support the first playable loop:
generate map, spawn player, loot, fight, survive zone, win.

## Performance Rule

Build for low-end hardware first, then scale visuals up later.

Initial rendering and content constraints:

- Forward rendering path
- No Lumen in Prototype 0.1
- No Nanite in Prototype 0.1
- Low-poly modular environment pieces
- Simple lighting and shadow setup

Primary target:

- Stable 60 FPS on weak hardware (GTX 1050 / integrated graphics class) in performance mode

## First Playable Scope

- FPS controller
- One weapon
- Seeded generated arena
- Loot spawn system
- Basic bots
- Shrinking danger zone
- Win/loss condition

## Forbidden Until Prototype 0.1

- Full multiplayer
- Ranked mode
- Battle pass
- Cosmetics
- Account system
- Large open world
- Complex inventory
- Vehicles
- Crafting
- Base building
- Story mode
- Marketplace
- Web dashboard
- External backend
- Graphics-first development with optimization later
