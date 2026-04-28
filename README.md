# frontline-reboot

Frontline reboot is a solo-dev Unreal Engine 5 project focused on one core differentiator:

Every match is a new battlefield.

## Stack

- Engine: Unreal Engine 5.4/5.5+
- Implementation path: Blueprints first, C++ only when needed
- Procedural generation: UE5 PCG + Landscape + seed-driven rules
- Asset sourcing: controlled use of Fab/Marketplace packs
- Source control: GitHub + Git LFS (for large binary assets)

## Technical Direction

- Low-spec first, scale visuals later
- Forward renderer first
- No Lumen/Nanite in Prototype 0.1
- Procedural match variation is the primary differentiator
- Performance mode is default

## First Playable Target

See FRONTLINE_GAME_LOCK.md and MVP_SCOPE.md.

Target is Frontline Prototype 0.1:

- FPS movement
- One weapon
- Generated arena
- Randomized cover and loot
- Basic bots
- Shrinking zone
- Win/loss state

## Repository Layout

- UnrealProject/
- Docs/
- Design/
- References/
- FRONTLINE_GAME_LOCK.md
- MVP_SCOPE.md
- ROADMAP.md
- CUT_LIST.md
- Docs/LOW_SPEC_FIRST_STRATEGY.md
- Docs/DAY1_EXACT_SETUP.md

## Execution Guides

- Day 1 setup sequence: Docs/DAY1_EXACT_SETUP.md
- Full solo-dev pipeline: Docs/FULL_PIPELINE_SOLO_DEV_TO_STORE_RELEASE.md

## Development Rule

Do not add features that violate FRONTLINE_GAME_LOCK.md.
