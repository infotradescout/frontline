# Frontline Full Pipeline (Solo Dev to Store Release)

## Decision

Best path:

- Unreal Engine 5
- Blueprint-first development
- Low-end-first optimization
- Procedural gameplay as the core differentiator

Not the path:

- Cinematic-first UE5 demo workflows
- MMO-scale backend architecture
- Giant open-world scope
- AI-driven feature dumping

Core advantage:

- Every match feels new while still running smoothly on average PCs

## Core Law

1. Gameplay first
2. Performance second
3. Visuals third
4. Everything else last

## Phase 0: Foundation (1-3 days)

Goal:

- Create a project that does not bloat over time

Stack:

- Engine: Unreal Engine 5
- Logic: Blueprints
- Version control: GitHub + Git LFS
- IDE: Cursor
- AI planning: ChatGPT
- Procedural generation: UE5 PCG
- 3D edits: Blender
- Audio: Audacity
- Optional voice: ElevenLabs

Required Unreal setup:

Turn OFF:

- Lumen
- Nanite (early)
- Virtual Shadow Maps
- Raytracing

Turn ON:

- Forward Rendering

Set scalability:

- Low

## Phase 1: Core FPS (Week 1)

Goal:

- A playable shooter foundation, not live battle royale yet

Build only:

Player:

- Move
- Jump
- Crouch
- Aim
- Shoot

Weapon:

- One rifle
- Hitscan
- Ammo count

Combat:

- Damage
- Health
- Death

Environment:

- One empty test map

KPI:

- Run, shoot bots, and hold 60 FPS

If KPI fails:

- Fix performance first

## Phase 2: Procedural Core (Week 2-3)

This is the game identity.

Use UE5 PCG to generate:

- Cover
- Loot
- Terrain variation
- Spawn points
- Storm circles

Start with:

- Simple arena generation
- Modular, repeatable, lightweight systems

Avoid early:

- Giant cities
- Giant forests
- Heavy realistic terrain systems

KPI:

- Every match feels different

## Phase 3: Battle Royale Loop (Week 3-5)

Add:

Match flow:

- Spawn/drop
- Loot
- Shrinking zone
- Last player standing

Bots:

- Basic patrol
- Chase
- Shoot

Do not add:

- Advanced AI
- Vehicles
- Squads
- Skill trees
- Complex inventory

KPI:

- 5-minute matches are fun

## Phase 4: Performance Lock

This is the survival phase for the project.

Test on:

- Weak GPU
- Weak CPU
- Integrated graphics when possible

Rules:

Use:

- Forward rendering
- Baked lighting
- Low-poly assets
- Instanced meshes

Avoid:

- Excessive physics
- Dynamic lights everywhere
- Massive textures

Model:

- Keep a performance-focused mode as default, high-quality mode as optional

## Phase 5: Visual Identity (Week 5-8)

Only after performance lock.

Recommended style:

- Stylized tactical

Why:

- Cheaper
- More scalable
- More readable
- Easier to optimize

Asset strategy:

- Use curated free/affordable marketplace assets
- Modify in Blender

Avoid:

- Asset-pack hoarding
- Mixed incompatible art styles
- Realism chase

## Phase 6: Networking (after singleplayer loop works)

Start with:

- 2-player test
- Unreal replication
- Listen server
- Dedicated server smoke test after listen-server gameplay works

Do not build yet:

- Cloud backend
- Anti-cheat
- Matchmaking

Gate:

- Gameplay loop must already be fun in solo mode

## Phase 7: Content Pipeline

Keep it lightweight.

Environment:

- Modular assets
- Reusable materials
- Procedural placement

Weapons:

- Limit to 3-5 early

Animation:

- Mixamo and/or curated marketplace packs

## Phase 8: Audio

MVP audio set:

- Footsteps
- Gunshots
- Hit markers
- Storm ambience

Principle:

- Good audio beats high-end graphics for perceived quality

## Phase 9: Playtesting

Start testing early.

First testers:

- Friends only

Watch for:

- Confusion
- FPS drops
- Map frustration
- Repetitive generation patterns

KPI:

- Players ask for one more match

## Phase 10: Store Prep

First release platform:

- Steam

Steam page assets:

- Logo
- Capsule art
- Screenshots
- Gameplay trailer

Trailer rule:

- Show generated worlds changing each match

## Phase 11: Early Access

Launch strategy:

- Early Access, not 1.0

Why:

- Better tolerance for rough edges
- Faster iteration loop
- Faster feedback cycle

## Phase 12: Post-Launch

Add only after core loop proves durable:

- Squads
- Cosmetics
- Progression
- Ranking
- Advanced generation depth

## What to Avoid at All Costs

- AI-generated feature creep
- Performance-last architecture
- Gameplay-second planning

## Real Competition

Not:

- Fortnite
- Warzone
- Apex

Actual competition:

- Solo-dev burnout
- Scope creep

## Actual MVP Definition

A procedurally generated FPS arena with loot, bots, and shrinking zones that runs smoothly on average PCs.

## AI Usage Doctrine

Use AI for:

- Architecture
- Debugging
- Blueprint help
- Optimization decisions
- Procedural logic support
- Workflow acceleration

Do not use AI for:

- Full game generation
- Massive speculative systems
- Replacing design ownership

## Long-Term Strategy

Build simple and scalable.

Do not build complex and cinematic before the loop is proven.
