# Blueprint Standards

> Without these, the project rots. Apply from Blueprint #1.

---

## Naming

### Asset prefixes

| Type                  | Prefix     | Example                  |
|-----------------------|------------|--------------------------|
| Blueprint Class       | `BP_`      | `BP_Player`              |
| Actor Component       | `BPC_`     | `BPC_Health`             |
| Interface             | `BPI_`     | `BPI_Damageable`         |
| Game Mode             | `GM_`      | `GM_Frontline`           |
| Game State            | `GS_`      | `GS_Frontline`           |
| Player State          | `PS_`      | `PS_Frontline`           |
| Player Controller     | `PC_`      | `PC_Player`              |
| Widget                | `WBP_`     | `WBP_HUD`                |
| Enum                  | `E_`       | `E_WeaponType`           |
| Struct                | `S_`       | `S_LootEntry`            |
| Data Asset            | `DA_`      | `DA_Weapon_Rifle`        |
| Data Table            | `DT_`      | `DT_Loot`                |
| Static Mesh           | `SM_`      | `SM_CoverWall_01`        |
| Skeletal Mesh         | `SK_`      | `SK_Player`              |
| Material              | `M_`       | `M_Master_Opaque`        |
| Material Instance     | `MI_`      | `MI_CoverWall_Concrete`  |
| Texture               | `T_`       | `T_CoverWall_D`          |
| Sound Cue             | `SC_`      | `SC_Rifle_Fire`          |
| Niagara System        | `NS_`      | `NS_Muzzle_Rifle`        |
| Animation Blueprint   | `ABP_`     | `ABP_Player`             |
| Animation Montage     | `AM_`      | `AM_Rifle_Fire`          |

### Domain prefixes (for gameplay BPs)

```
BP_Player
BP_Bot_Grunt
BP_Weapon_Rifle
BP_Pickup_Ammo
BP_LootSpawner
BP_Zone_Storm
BP_Arena_Generator
```

---

## Function & variable naming

- **Functions**: `Verb_Object` — `Fire_Weapon`, `Spawn_Loot`, `Generate_Arena`, `Apply_Damage`
- **Events (custom)**: same `Verb_Object` rule
- **Booleans**: `b` prefix — `bIsAiming`, `bCanFire`
- **Variables**: `PascalCase` — `CurrentHealth`, `MaxAmmo`
- **Local variables**: same as variables, no Hungarian noise
- **Categories**: required on every public variable and function — `Stats`, `Combat`, `Movement`, `Loot`, `AI`, `PCG`, `UI`, `Debug`

---

## Folder structure (Content/)

```
Content/
├── Frontline/                  ← all project content lives under one root
│   ├── Core/                   ← GameMode, GameState, GameInstance
│   ├── Characters/
│   │   ├── Player/
│   │   └── Bots/
│   ├── Weapons/
│   ├── PCG/                    ← procedural generation graphs + rules
│   ├── Arena/                  ← static pieces consumed by PCG
│   ├── Loot/
│   ├── Zone/                   ← storm / shrinking circle
│   ├── AI/                     ← Behavior Trees, Blackboards, EQS
│   ├── UI/                     ← Widgets only
│   ├── FX/                     ← Niagara, decals
│   ├── Audio/
│   └── Debug/                  ← test maps, dev-only BPs
└── ThirdParty/                 ← marketplace / Fab assets, untouched
```

**Never** dump assets at `Content/` root. Never move `ThirdParty` content into project folders.

---

## Blueprint hygiene rules

- One responsibility per Blueprint. If a BP exceeds ~300 nodes, split.
- Prefer **Actor Components** for reusable behaviour (Health, Inventory, Aim).
- Prefer **Interfaces** for cross-actor communication. No casting up class hierarchies you don't own.
- No logic in **Construction Scripts** that touches the world at runtime.
- No `Tick` unless justified — comment why above the event.
- No hard references between unrelated systems. Use **soft references** + async load for content.
- Comment boxes are mandatory on any graph with > 20 nodes.
- Reroute nodes for clean wiring. Crossed wires = rewrite.
- Variables exposed to designer/level use `Instance Editable` + tooltip.

---

## Data-driven by default

- Weapon stats → `DA_Weapon_*` (Primary Data Assets)
- Loot tables → `DT_Loot`
- Bot archetypes → `DA_Bot_*`
- Arena rules → `DA_Arena_*`

Never hardcode tunable numbers inside Blueprint logic. Tunables live in Data Assets.

---

## C++ usage policy (Prototype 0.1)

- Default to Blueprint.
- Promote to C++ **only** when:
  - the system is profiled and Blueprint is the bottleneck, **or**
  - the engine API is not exposed to Blueprint, **or**
  - a base class needs to be inheritable across many BPs.
- C++ class prefix follows Unreal convention: `AFrontlinePlayer`, `UHealthComponent`.
