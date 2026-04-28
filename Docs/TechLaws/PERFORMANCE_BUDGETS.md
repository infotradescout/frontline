# Performance Budgets — Prototype 0.1

> **This document saves games.** Every system MUST fit inside these limits.
> If a feature cannot ship inside the budget, the feature is cut — not the budget.

---

## Target Hardware

- **Primary baseline**: GTX 1050 / Intel Iris Xe (integrated graphics)
- **Target framerate**: Stable 60 FPS in Performance Mode
- **Resolution baseline**: 1080p, scalability `Low`
- **Frame time budget**: 16.6 ms (game thread + render thread + GPU)

---

## Hard Runtime Limits

| Resource                          | Limit              |
|-----------------------------------|--------------------|
| Bots on map (total alive)         | **12**             |
| Active AI ticking at once         | **6**              |
| Dynamic shadow-casting lights     | **1**              |
| Draw calls per frame              | **< 1500**         |
| Triangles on screen               | **< 1.5M**         |
| Texture resolution cap            | **1024 px**        |
| Skeletal meshes visible           | **< 20**           |
| Particle systems active           | **< 8**            |
| Physics-simulated rigid bodies    | **< 30**           |
| Audio voices simultaneous         | **< 24**           |
| Match duration                    | **5 minutes max**  |
| Arena footprint                   | **Small / Medium** |
| Memory budget (Content)           | **< 2 GB RAM**     |

---

## Forbidden in Prototype 0.1

- Runtime Global Illumination (Lumen)
- Nanite virtualized geometry
- Ray tracing of any kind
- Screen-space reflections at quality > Low
- Volumetric fog / volumetric clouds
- Heavy post-processing (DoF, motion blur, chromatic aberration, bloom > minimal)
- Physics-heavy destruction (Chaos at runtime)
- Realtime cloth on more than the player
- Cinematic sequences during gameplay

---

## Required Defaults

- **Renderer**: Forward shading
- **Lighting**: Static or Stationary only; bake whenever possible
- **Shadows**: CSM only on the sun, distance ≤ 4000 uu
- **Anti-aliasing**: FXAA (cheapest); TAA only if free
- **LODs**: Mandatory on every static mesh ≥ 1000 tris
- **Instancing**: Use HISM/ISM for cover, walls, props placed by PCG
- **Materials**: Master material + instances; no unique materials per asset

---

## Profiling Cadence

- `stat unit`, `stat scenerendering`, `stat game` open at all times during dev
- Profile on the **lowest-spec test box**, not the dev machine
- Record baseline FPS at end of each phase; regressions block the phase exit

---

## Budget Violation Protocol

1. Identify the offending system.
2. Cut, simplify, or pool. Do **not** raise the budget.
3. If the budget MUST move, document it here with date and reason.
4. No silent budget changes. Ever.
