# FRONTLINE GAME LOCK

Frontline is an FPS battle royale prototype where every match generates a new battlefield.

## FUN in Minute 1 (placeholder — to be replaced)

> Players adapt every match because every battlefield is unfamiliar.

This is a working placeholder. It is not the final answer. Replace it once the
prototype is in hand and we know what actually feels fun in the first 60 seconds.

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

## Long-Term Multiplayer Target

The long-term target is battle royale matches with up to 100 live players plus
bots. This target is built in scaling rings:

- offline bot match
- 2-4 live players
- 8-16 live players plus bots
- 24-40 live players plus bots
- 60-100 live players plus bots

The project may prepare architecture for this from day one, but full live
multiplayer work starts only after Prototype 0.1 proves the complete solo match
loop.

## Forbidden Until Prototype 0.1

- Full live multiplayer implementation
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
