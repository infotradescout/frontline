# Next Milestone: Offline Battle Royale Micro-Match

## Goal

Turn the current player-vs-respawning-bots setup into a complete offline battle
royale match.

## Build Order

1. Match state machine
2. Player and bot health/death consistency
3. Bot respawn limits and cleanup
4. Shrinking danger zone
5. Win/loss condition
6. Restart flow
7. Seeded layout variation
8. Performance check

## Automation

Run this from repo root to apply and verify baseline offline BR micro-match
settings in the Unreal project:

```powershell
.\Tools\apply_offline_br_micro_match.ps1 -ProjectRoot "D:\AAATraderCorner\TradeScout\Frontline\UnrealProject\FrontlineWarfare"
```

What it does:

- auto-detects a known map and shooter/first-person game mode path
- applies available GameMode tuning values
- repositions discovered bot spawners (up to 4 anchor points)
- ensures NavMesh bounds exists and covers the arena
- runs verification and prints key `BR_APPLY_*` and `BR_VERIFY_*` log lines

## Acceptance Criteria

- Press Play and enter Warmup or Live state.
- Bots spawn and respawn under server-side rules.
- Player can damage and kill bots.
- Bots can damage and kill player.
- The danger zone shrinks during the match.
- A winner is declared.
- The match can restart without reopening the editor.
- The match finishes in 5 minutes or less.

## Do Not Build Yet

- 100-player networking
- matchmaking
- accounts
- cosmetics
- battle pass
- vehicles
- squad logic
- complex inventory
- multiple maps

## Why

This is the smallest version of the final game. If this loop is not fun and
stable offline, multiplayer only makes the problems harder to see and slower to
fix.
