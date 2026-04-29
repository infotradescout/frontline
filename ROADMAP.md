# Solo-Dev Roadmap

## North Star

Frontline is a solo-dev battle royale built in scaling rings:

- First: one complete offline match with bots.
- Then: 2-4 live players.
- Then: 8-16 live players plus bots.
- Then: 24-40 live players plus bots.
- Finally: architecture-proven 60-100 live players plus bots.

The goal is not to copy AAA scope. The goal is AAA discipline on a narrow,
repeatable battle royale loop: generate map, spawn, loot, fight, survive zone,
last player or squad wins.

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

Build:
- Server-authoritative health, damage, ammo, loot, and zone
- Listen server first
- Dedicated server smoke test
- Replicated PlayerState and GameState match data
- No gameplay authority in widgets

Rule:
- Start this only after the solo prototype works and passes the Phase 6
  readiness gate in Docs/TechLaws/MULTIPLAYER_RULES.md.

## Phase 7: Small Battle Royale Slice

KPI: 8-16 live players plus bots can finish a match.

Build:
- Lobby-free quick join or direct connect
- Spawn selection rules
- Replicated loot and pickup ownership
- Shrinking zone visible to all players
- Bot fill for missing player slots
- Match end and clean server restart

## Phase 8: Mid-Scale Battle Royale

KPI: 24-40 live players plus bots is stable.

Build:
- Dedicated server as default test target
- Replication graph or equivalent relevancy strategy
- Bandwidth budget per player
- Server-only bot perception and decision throttling
- Cheap projectiles or server-side hitscan validation
- Map streaming and spawn-area performance pass

## Phase 9: Large-Scale Battle Royale Target

KPI: 60-100 live players plus bots is technically proven.

Build:
- Load test harness
- Automated soak tests
- Server frame-time budget enforcement
- Network packet/bandwidth profiling
- Production-style deployment path
- Anti-cheat posture and exploit review

Rule:
- 100 players is a proof target, not a promise, until 40-player matches are fun,
  stable, and measurable.
