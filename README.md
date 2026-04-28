# frontline-reboot

Frontline reboot is a solo-dev Unreal Engine 5 project focused on one core differentiator:

Every match is a new battlefield.

## Stack

- Engine: Unreal Engine 5.4/5.5+
- Implementation path: Blueprints first, C++ only when needed
- Procedural generation: UE5 PCG + Landscape + seed-driven rules
- Asset sourcing: controlled use of Fab/Marketplace packs
- Source control: GitHub + Git LFS (for large binary assets)

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

## Development Rule

Do not add features that violate FRONTLINE_GAME_LOCK.md.
