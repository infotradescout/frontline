# Solo-Dev Roadmap

## Phase 1: Low-End Core

KPI: playable test arena.

Build:
- Player movement
- Gun firing
- Health/damage
- Test enemy
- Flat map test space
- Forward rendering enabled
- No Lumen or Nanite
- Low scalability baseline

## Phase 2: Generated Match

KPI: every restart changes the map.

Build:
- Seed system
- Randomized cover
- Randomized loot
- Randomized spawns
- Safe zone/storm

## Phase 3: Optimization Lock

KPI: stable low-end runtime quality.

Build:
- Performance mode as default
- Aggressive culling and instancing
- Cheap AI and minimal physics
- Stable 60 FPS on weak hardware target
- Remove major frame spikes

## Phase 4: Combat Loop

KPI: 5-minute match is playable.

Build:
- Bots
- Loot pickup
- Ammo
- Damage zone
- Win/loss screen

## Phase 5: Visual Identity and High-Quality Mode

KPI: screenshots look like a real game.

Build:
- Stylized environment
- UI pass
- Weapon polish
- Sound
- Lighting
- Optional high-quality mode toggles

## Phase 6: Multiplayer Test

KPI: 2-4 players can join a generated match.

Rule:
- Start this only after the solo prototype works.
