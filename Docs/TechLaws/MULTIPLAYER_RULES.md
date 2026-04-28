# Multiplayer Rules

> Multiplayer ships in Phase 6+. **The architecture is enforced from day one.**
> Following these rules now costs nothing. Ignoring them costs a rewrite later.

---

## Authority model (locked)

- **Listen-server first.** Host plays the game and is the authority.
- Dedicated server is a future option, not a constraint right now — but nothing may *prevent* it.
- The **server is authoritative** for: health, damage, ammo, loot ownership, zone state, match state, bot AI, scoring, win/loss.
- The **client is authoritative** only for: input, camera/look, UI state, cosmetic FX prediction.

---

## Hard rules — apply to every gameplay system

### DO

- Build every gameplay actor as if it will replicate. Set `bReplicates = true` on actors that affect other players.
- Route gameplay state changes through **Server RPCs** even in single-player. Use `Switch Has Authority` early.
- Use `Replicated` / `ReplicatedUsing` variables for shared state (Health, Ammo, MatchPhase, ZoneRadius).
- Drive UI from **PlayerState / GameState**, not from PlayerController locals.
- Put authoritative gameplay logic in: `GameMode`, `GameState`, server-side `Pawn`, `PlayerController` (server side), and `ActorComponents` on those.
- Use **Gameplay Tags** for state flags that may need to replicate later.
- Keep cosmetic effects (muzzle flash, sound, decals) on `Multicast` or local-only paths.

### DO NOT

- Hardcode `GetPlayerCharacter(0)` / `GetPlayerController(0)` outside of UI bootstrap.
- Assume `GetWorld()->GetFirstPlayerController()` is "the" player.
- Store **authoritative state in Widgets**. Widgets read state, they don't own it.
- Tightly couple UI to gameplay logic. UI listens to GameState/PlayerState delegates.
- Use `Set Timer by Function Name` for gameplay-critical timers without thinking about which machine runs it.
- Spawn gameplay actors from the client.
- Trust the client for damage, score, position validation, or loot pickups.
- Use singleton-style "Manager" actors that assume one instance per process.

---

## Replication checklist (apply when building any gameplay actor)

1. Does this affect other players? → `bReplicates = true`.
2. Does it move? → `bReplicateMovement = true` or use a `MovementComponent`.
3. Does it expose state to UI? → mark variable `Replicated` or `ReplicatedUsing=OnRep_X`.
4. Is the action triggered by input? → `Server_DoX` (Reliable for gameplay, Unreliable for cosmetics).
5. Is the result seen by everyone? → `Multicast_OnXHappened` for cosmetic broadcast.
6. Is this an FX or sound only the local player needs? → run locally, no replication.

---

## UI ↔ gameplay boundary

- UI **never** writes gameplay state.
- UI **subscribes** to `GameState` / `PlayerState` / component delegates.
- UI **requests** actions via the local `PlayerController`, which forwards to a Server RPC.
- A widget destroyed mid-match must not break gameplay. If it does, gameplay logic was in the widget.

---

## Tick & cost discipline (matters more in MP)

- Bot AI ticks on the **server only**.
- Pickups update on the **server only**; clients see replicated visibility/interaction state.
- Zone shrink runs on the **server**, replicates `Center`, `Radius`, `Phase` only.
- Avoid replicating per-frame floats. Replicate intent + interpolate locally.

---

## Phase 6 readiness gate

Before networking work begins, the following must be true:

- [ ] Every gameplay component compiles with `bReplicates = true` without behaviour changes.
- [ ] No widget owns gameplay-authoritative state.
- [ ] Damage, ammo, loot, and zone all flow through server-side code paths even in single-player.
- [ ] Bot AI runs cleanly when forced server-only.
- [ ] Match state machine (Pre-match → Live → Zone → End) lives in `GameMode` / `GameState`.

If any box is unchecked, networking is not started. Fix the architecture first.
