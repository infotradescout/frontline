# PCG Ruleset — The Soul of Frontline

> The procedural generator IS the game design. Every match is born here.
> If a generated arena fails any rule below, the seed is rejected and re-rolled.

---

## North Star

**Every match must feel like a fresh, fair, readable battlefield in under 5 minutes.**

If a generated arena is unreadable, unfair, or boring — the generator is broken, not the game.

---

## Required ingredients (every arena, every seed)

Every generated arena MUST contain at least:

| Element            | Min count | Notes                                                      |
|--------------------|-----------|------------------------------------------------------------|
| High ground        | 2         | Vantage points overlooking ≥ 30% of the playable area      |
| Low ground         | 1         | Sunken / valley pocket forcing risk to traverse            |
| Cover clusters     | 6         | 3–6 cover pieces grouped into a defensible pocket          |
| Loot hotspots      | 3         | High-value loot zones that pull players together           |
| Dead zones         | 2         | Open ground with no cover — risk corridors                 |
| Long sightlines    | 2         | Lanes ≥ 60 m clear, supporting rifle engagements           |
| Close-quarter zones| 2         | Tight rooms / corridors ≤ 8 m wide for pistol/melee fights |
| Player spawn pads  | N+2       | At least N+2 viable spawns for N players                   |

---

## Hard rules (any failure → reject seed and re-roll)

### Fairness

- **No unwinnable spawns.** Spawn pads must have ≥ 1 cover piece within 5 m.
- **No spawn camping geometry.** No spawn pad may be visible from another spawn pad.
- **No spawns inside or under the storm circle's first ring.**
- **No spawns on or adjacent to a high-ground vantage** (no king-of-the-hill freebies).
- **Loot hotspots must be roughly equidistant** from all spawn clusters (±20%).

### Readability

- **Silhouette test**: From any spawn, the player can identify ≥ 1 landmark to navigate by.
- **No identical 50 m × 50 m tiles.** Local variation is mandatory.
- **No invisible walls.** All blocked paths must be visually communicated by geometry.
- **Cover is obvious.** No "is this cover?" geometry. Cover reads as cover at a glance.

### Flow

- **Connectivity**: every region of the arena is reachable on foot from every spawn within 60 s of normal movement.
- **No dead-end traps**: every cover cluster has at least 2 escape vectors.
- **Choke points exist but never single-thread** the only path between two zones.

### Performance (cross-cutting with [PERFORMANCE_BUDGETS.md](PERFORMANCE_BUDGETS.md))

- Generated arena draw calls **< 1500**.
- Cover and props placed via **HISM/ISM**, never one-actor-per-piece.
- Generated colliders **simplified** — no per-triangle collision on cover meshes.
- Generated arena footprint stays inside the small/medium budget.

---

## Generation flow (high level)

```
Seed
  ↓
Layout pass        → high ground, low ground, region partitioning
  ↓
Pathing pass       → guarantee connectivity + escape vectors
  ↓
Cover pass         → place cover clusters in valid pockets
  ↓
Loot pass          → place hotspots, validate equidistance
  ↓
Spawn pass         → place spawn pads, validate fairness rules
  ↓
Validation pass    → run all "Hard rules" checks
  ↓
Accept  OR  Reject + re-roll (max 5 retries before logging seed)
```

A rejected seed that retries 5× is logged to `Saved/PCG/RejectedSeeds.log` for offline analysis.

---

## Tunables (live in `DA_Arena_*` data assets)

- `ArenaSize` — Small / Medium
- `CoverDensity` — 0.0 – 1.0
- `LootHotspotCount` — 3 – 6
- `BotCount` — 1 – 12 (capped by [PERFORMANCE_BUDGETS.md](PERFORMANCE_BUDGETS.md))
- `BiomePalette` — which mesh/material set the arena pulls from
- `Seed` — 64-bit integer, displayed in dev HUD for reproducibility

---

## Forbidden in Prototype 0.1

- Runtime mesh generation (no procedural meshes built per-frame)
- Boolean CSG / runtime destruction
- Navmesh rebuilds mid-match (build once at match start, freeze)
- PCG graphs that depend on world streaming
- Generators that take > 3 seconds wall-clock to produce a valid arena on the low-spec target

---

## Definition of "the generator works"

A 100-seed batch produces:

- **100 / 100** arenas pass all hard rules
- **0 / 100** unwinnable or unreadable layouts
- **Median generation time** under 1.5 s on the low-spec target
- **Every arena feels different** in a blind playtest of 10 sequential seeds

Until that bar is met, no other Phase 2 work ships.
