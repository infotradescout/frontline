# Last Alive Wins C++ Setup

This project now includes a native runtime module with a server-authoritative
battle royale match loop:

- `AFrontlineBRGameMode`
- `AFrontlineBRGameState`
- Match phases: `Warmup -> Live -> Ended`
- Win rule: last alive pawn wins
- Time cap fallback: match ends when live timer expires
- Auto-restart: level reopens after end delay

## Files Added

- `UnrealProject/FrontlineWarfare/Source/FrontlineWarfare/Public/FrontlineBRGameMode.h`
- `UnrealProject/FrontlineWarfare/Source/FrontlineWarfare/Private/FrontlineBRGameMode.cpp`
- `UnrealProject/FrontlineWarfare/Source/FrontlineWarfare/Public/FrontlineBRGameState.h`
- `UnrealProject/FrontlineWarfare/Source/FrontlineWarfare/Private/FrontlineBRGameState.cpp`
- Build/target files under `UnrealProject/FrontlineWarfare/Source`

## One-Time Build Step

1. Open `UnrealProject/FrontlineWarfare/FrontlineWarfare.uproject`.
2. When prompted to build missing modules, click **Yes**.
3. Wait for compile to finish and project reload.

## Assign Game Mode

In Unreal Editor:

1. Open your active map (currently `/Game/FirstPerson/Lvl_FirstPerson`).
2. Open **World Settings**.
3. Set **GameMode Override** to `FrontlineBRGameMode`.
4. Save the map.

## Tunables (in FrontlineBRGameMode defaults)

- `WarmupSeconds` default: `10`
- `LiveMatchSeconds` default: `300`
- `RestartDelaySeconds` default: `8`

## Notes

- This logic is authoritative and server-side by design.
- If bots are runtime-spawned by blueprint, they will still count as alive when
  they possess a pawn with an AI controller.
- If your current bot pipeline force-respawns forever, the match may not end.
  In that case, disable infinite bot respawn during the `Live` phase.
