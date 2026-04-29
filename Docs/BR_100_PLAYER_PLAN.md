# Frontline 100-Player Battle Royale Plan

## Target

Build toward battle royale matches with up to 100 live players plus bots, while
keeping the solo-dev path survivable.

The production target is earned in stages:

- Offline bot match
- 2-4 player multiplayer match
- 8-16 player BR slice
- 24-40 player mid-scale match
- 60-100 player large-scale proof

## Product Shape

Frontline should not try to be "AAA by size." It should feel high quality
because the core loop is clear, fast, and polished:

- short match startup
- readable combat
- understandable loot
- fair zone pressure
- generated arenas that create new decisions
- bots that fill matches without feeling expensive
- strong audio and hit feedback
- clean menus and restart flow

## Current Position

The project is currently in the offline combat-loop stage:

- bots exist
- bots respawn
- first-person foundation exists
- Unreal project and helper tools are committed

The next job is to turn bot combat into a complete micro battle royale match.

## Next Milestone: Offline BR Micro-Match

KPI: one player and bots can finish a complete match in 5 minutes or less.

Required:

- player health, damage, death, and respawn or spectate choice
- bot health, damage, death, and respawn
- one weapon path that reliably damages player and bots
- match state machine: Warmup, Live, End
- shrinking danger zone
- last-survivor or score-based win/loss condition
- restart flow
- seed or layout variation on new match

Definition of done:

- a match can start, play, end, and restart without editor intervention
- the player can win
- the player can lose
- bots do not pile up, leak, or stop respawning after repeated deaths
- no major frame spike occurs during bot respawn or zone updates

## Multiplayer Scaling Rings

### Ring 1: Listen Server, 2 Players

Goal: prove the gameplay code is authority-safe.

- server owns health, damage, ammo, loot, zone, match phase, and winner
- client sends input and requests
- UI reads replicated state
- no direct widget ownership of gameplay state

### Ring 2: Dedicated Server, 2-4 Players

Goal: prove the game can run without a host player.

- dedicated server build starts a match
- clients connect by IP or simple session
- bots run server-side
- match end resets cleanly

### Ring 3: Small BR, 8-16 Players Plus Bots

Goal: prove the battle royale design works with real people.

- basic spawn rules
- replicated loot ownership
- zone pressure
- bot fill
- winner calculation

### Ring 4: Mid-Scale BR, 24-40 Players Plus Bots

Goal: make performance and networking measurable.

- relevancy strategy
- bandwidth budget
- server frame-time budget
- bot AI throttling
- projectile/hitscan validation
- load-test routine

### Ring 5: Large BR, 60-100 Players Plus Bots

Goal: prove the dream is technically possible.

- soak tests
- network profiling
- server deployment plan
- anti-cheat posture
- failure recovery

## Technical Laws

- Server is authoritative for all gameplay.
- Bots are server-only decision makers.
- Clients never decide damage, loot ownership, score, zone state, or winners.
- UI never owns gameplay state.
- Replicate state changes, not noisy per-frame values.
- Prefer fewer, clearer systems over flexible mega-systems.
- Every new feature must survive the question: will this still work with 40
  players and bots?

## Solo-Dev Constraints

Avoid until the offline micro-match is fun:

- ranked matchmaking
- accounts
- cosmetics
- battle pass
- vehicles
- squads
- complex inventory grids
- building/crafting
- huge maps
- multiple weapon classes

Add only when the current ring is stable:

- menus
- settings
- import pipeline
- better art
- multiple arenas
- more weapons
- matchmaking

## The Real AAA Path

AAA feel comes from:

- responsive combat
- reliable networking
- strong sound
- clear UI
- stable performance
- consistent art direction
- fast iteration

AAA scale comes last.
