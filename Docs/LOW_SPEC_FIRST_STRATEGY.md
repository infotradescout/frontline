# Low-Spec-First Strategy

## Rule

Build for low-end hardware first, then scale up visuals later.

If performance is not stable early, polish work is deferred.

## Why This Exists

Most projects fail performance because they build high-end visuals first and try to optimize late.
This project does the opposite:

1. Gameplay clarity
2. Performance stability
3. Procedural variation
4. Replayability
5. Visual polish

## Baseline Technical Profile (Prototype 0.1)

- Renderer: Forward
- Lumen: Off
- Nanite: Off
- Environment style: low-poly modular
- Lighting: simple and cheap
- Shadows: constrained and aggressively profiled
- Physics: minimal
- AI: cheap behavior focused on gameplay loop

## Dual-Mode Plan

### Mode A: Performance Mode (default)

- Low-poly meshes
- Simplified shadows
- Baked/simple lighting
- Aggressive culling
- Lowest stable GPU/CPU load

### Mode B: High-Quality Mode (later)

- Improved lighting and detail
- Optional quality features
- Never required for core gameplay loop

## Build Order

## Phase 1: Low-End Core

- FPS controller
- One weapon
- Flat map test space
- Basic bots
- No lighting complexity

Test only on low settings.

## Phase 2: Procedural Gameplay

- Random cover
- Random loot
- Random spawn
- Shrinking zone

This is the core game identity.

## Phase 3: Optimization Lock

Before visual polish:

- Stable 60 FPS on weak hardware target
- No major stutters
- No severe frame-time spikes

## Phase 4: Visual Scale-Up

Only after performance lock:

- Better lighting
- Better detail
- Optional high-quality mode improvements

## Practical System Design Rules

Prefer:

- Instanced meshes
- Simple collision
- Minimal always-on physics
- Controlled AI complexity

Avoid early:

- Heavy real-time shadow usage
- Expensive global illumination
- Large counts of dynamic physics objects
- Graphics-first milestone planning

## MVP Definition

Success means:

A playable FPS match with a different map every time, running smoothly on weak hardware.
