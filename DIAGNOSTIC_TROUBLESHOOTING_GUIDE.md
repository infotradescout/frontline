# ?? **GAME DIAGNOSTIC GUIDE - TROUBLESHOOTING**

## **?? COMMON ISSUES & FIXES**

### **Issue #1: Players Don't Spawn on Pregame Island**

**Symptoms:**
- Players spawn scattered across the map
- Players spawn at (0,0,0) and fall
- No pregame island visible

**Diagnosis:**
```
Check Output Log for:
? "Failed to spawn pregame island!"
? No "Pregame Island generated" message
```

**Fixes:**
1. **Island not spawning:**
   - Check GameMode is AFRGameMode
   - Verify HasAuthority() == true (server)
   - Check for conflicts with other pregame systems

2. **Players spawning wrong location:**
   - Verify `MatchPhase == EFRMatchPhase::Warmup`
   - Check `PregameIsland != nullptr`
   - Ensure `GetRandomSpawnLocation()` returns valid position

---

### **Issue #2: No Countdown Timer Visible**

**Symptoms:**
- No "00:90" countdown on screen
- Warmup never ends
- Match doesn't start

**Diagnosis:**
```
Check if:
? WarmupTimer not started
? TickWarmup() not being called
? HUD not created/visible
```

**Fixes:**
1. **Timer not starting:**
   - Check `StartWarmup(90)` is called in `HandleWarmup()`
   - Verify `GetWorld()->GetTimerManager()` is valid

2. **HUD not showing countdown:**
   - UI widgets not created (WBP_LobbyHUD doesn't exist)
   - `ClientUpdateCountdown()` not implemented
   - HUD widget not added to viewport

---

### **Issue #3: Island Doesn't Explode**

**Symptoms:**
- Match starts but island never destroys
- No damage to players on island
- No warnings at 30s, 15s, etc.

**Diagnosis:**
```
Check Output Log for:
? "MATCH STARTED! Pregame island will be destroyed..."
? "ISLAND DESTRUCTION WARNING: X seconds"
? "ISLAND DESTRUCTION STARTED!"
```

**Fixes:**
1. **Countdown not starting:**
   - Check `StartDestructionCountdown()` called in `HandleLive()`
   - Verify `CurrentPhase` changes to `MatchStarted`

2. **Damage not applying:**
   - Check `ApplyDamageToPlayersOnIsland()` is running
   - Verify `TakeDamage()` is being called
   - Check character has health component

---

### **Issue #4: Squads Not Forming**

**Symptoms:**
- All players show SquadId = -1
- Can't invite players
- No squad UI

**Diagnosis:**
```
Check Output Log for:
? "Squad Manager created"
? "Squads finalized for match start"
```

**Fixes:**
1. **Squad Manager not spawning:**
   - Check `SquadManager != nullptr` in GameMode
   - Verify `BeginPlay()` calls spawn code

2. **Squads not finalized:**
   - Check `FinalizeSquadsForMatch()` is called
   - Verify `AssignSquadsAndPOIs()` runs when warmup ends

---

### **Issue #5: No HUD/UI Visible**

**Symptoms:**
- Black screen (no UI)
- Can't see health, ammo, etc.
- No main menu

**Diagnosis:**
```
Check if:
? Widget Blueprints don't exist
? Widgets not added to viewport
? HUD class not set in GameMode
```

**Fixes:**
1. **Widgets don't exist:**
   - Create `WBP_MainMenu`, `WBP_LobbyHUD`, `WBP_GameHUD` in Unreal Editor
   - Set parent class to C++ base class

2. **Widgets not showing:**
   - Check `AddToViewport()` is called
   - Verify Z-order (some widgets might be behind others)
   - Check widget visibility settings

---

### **Issue #6: Game Crashes on Startup**

**Symptoms:**
- Unreal Editor crashes when pressing Play
- Fatal error / assertion failed

**Diagnosis:**
```
Check Crash Log for:
? Null pointer dereference
? Invalid cast
? Array out of bounds
```

**Fixes:**
1. **Common crash causes:**
   - `PregameIsland` is null but code tries to use it
   - Widget creation fails but code assumes success
   - Invalid spawn location (NaN, infinity)

2. **Add null checks:**
```cpp
if (PregameIsland)
{
    PregameIsland->StartDestructionCountdown();
}
```

---

### **Issue #7: Bots Don't Spawn**

**Symptoms:**
- Only human players in match
- No AI opponents
- Empty match

**Diagnosis:**
```
Check Output Log for:
? "Bot spawner created"
? "No bot spawner available!"
```

**Fixes:**
1. **Bot Spawner not created:**
   - Check `BotSpawner != nullptr`
   - Verify `AFRBotSpawner` class exists

2. **Bots not spawning:**
   - Call console command: `SpawnBots`
   - Check `SpawnBotsToFillMatch()` logic
   - Verify bot AI controller exists

---

### **Issue #8: Performance Issues / Low FPS**

**Symptoms:**
- Game runs at <30 FPS
- Stuttering / hitching
- High CPU/GPU usage

**Diagnosis:**
```
Check:
? Too many procedural buildings spawned
? Lighting not built
? Too many draw calls
```

**Fixes:**
1. **Reduce procedural generation:**
   - Lower `Settings.NumBuildings` (50 ? 20)
   - Lower `Settings.NumCoverObjects` (200 ? 50)

2. **Build lighting:**
   - Build menu ? Build Lighting
   - Wait for completion (5-30 minutes)

3. **Disable features for testing:**
   - Turn off auto-level generator
   - Reduce map size
   - Disable post-processing

---

### **Issue #9: Network/Multiplayer Issues**

**Symptoms:**
- Can't connect to server
- Desync between clients
- Squads don't replicate

**Diagnosis:**
```
Check:
? Replication not enabled
? Authority checks failing
? Client-side only code running
```

**Fixes:**
1. **Enable replication:**
   - `bReplicates = true` on actors
   - `DOREPLIFETIME()` on properties
   - `HasAuthority()` checks for server-only code

2. **Test locally first:**
   - PIE ? Net Mode: Standalone (test single player)
   - Then: Net Mode: Listen Server (test multiplayer)

---

### **Issue #10: Auto-Level Generator Not Working**

**Symptoms:**
- Empty level (no floor, no walls)
- No lighting
- No spawns

**Diagnosis:**
```
Check Output Log for:
? "Auto Level Generator starting..."
? "Level Type: X"
? "Auto Level Generation complete!"
```

**Fixes:**
1. **Generator not placed:**
   - Open level in Unreal Editor
   - Search for "AFRAutoLevelGenerator" in level
   - If not found, place one manually

2. **Generation not running:**
   - Check `BeginPlay()` is called
   - Verify `LevelType` is set correctly
   - Check for errors in generation functions

---

## **?? DIAGNOSTIC COMMANDS**

### **In-Game Console (Press ~):**

```
# Check if systems are running
stat fps                  // Show FPS
stat unit                 // Show frame time breakdown
stat game                 // Show game stats

# Game-specific commands
SpawnBots                 // Spawn AI bots
RemoveAllBots             // Remove all bots
StartScheduleConsole 30 0 // Start destruction schedule
DumpScheduleConsole       // Print destruction events

# Level transitions
open MainMenu             // Go to main menu
open Lobby                // Go to lobby
open GameMap              // Go to game map
```

### **Output Log Analysis:**

**What to look for:**
```
? Good signs:
   "? Pregame island spawned"
   "? Created 20 player spawners"
   "??? Warmup started"
   "Squad Manager created"
   "Bot spawner created"

? Bad signs:
   "? Failed to spawn pregame island!"
   "? No bot spawner available!"
   "Error:"
   "Warning:"
   "Assertion failed:"
```

---

## **?? STEP-BY-STEP TROUBLESHOOTING**

### **Step 1: Verify Build Success**
```
1. Open Visual Studio
2. Build Solution (F7)
3. Check for 0 errors
4. If errors, fix them first
```

### **Step 2: Check GameMode Setup**
```
1. Open Unreal Editor
2. Edit ? Project Settings ? Maps & Modes
3. Verify:
   - Default GameMode: AFRGameMode
   - Default Pawn Class: (your character)
   - HUD Class: AFRCanvasHUD
```

### **Step 3: Test Basic Level**
```
1. File ? New Level ? Empty Level
2. Place AFRAutoLevelGenerator
3. Set Level Type: Game Map
4. Press Play
5. Check Output Log for generation messages
```

### **Step 4: Test Pregame Island**
```
1. Create empty level
2. Let GameMode spawn island automatically
3. Press Play
4. Check Output Log for:
   - "Pregame Island generated"
   - "Created X player spawners"
   - "Created island barrier"
```

### **Step 5: Test Squad System**
```
1. Start match
2. Check Output Log for:
   - "Squad Manager created"
3. After warmup:
   - "Squads finalized for match start"
4. Check PlayerState.SquadId != -1
```

---

## **?? QUICK FIXES**

### **Fix #1: Game Won't Start**
```
Delete these if they exist:
- Intermediate folder
- Saved folder
- Binaries folder

Then:
1. Right-click .uproject
2. Generate Visual Studio project files
3. Build in Visual Studio
4. Launch Unreal Editor
```

### **Fix #2: Missing Classes in Editor**
```
1. File ? Refresh C++ project
2. Wait for compile
3. Restart Unreal Editor
4. Check if classes appear in dropdowns
```

### **Fix #3: Widgets Not Showing**
```
1. Create minimal widget in Editor:
   - Canvas Panel (root)
   - Text Block: "TEST"
2. Add to viewport in Level Blueprint
3. If visible, problem is widget design
4. If not visible, problem is viewport code
```

---

## **?? WHAT TO TELL ME**

**To help you faster, please provide:**

1. **What exactly happens when you press Play?**
   - Black screen?
   - Crash?
   - Spawns but broken?

2. **What does the Output Log say?**
   - Copy/paste relevant errors
   - Include ? and ? messages

3. **What level are you testing?**
   - MainMenu?
   - Lobby?
   - GameMap?

4. **Have you made any changes?**
   - Custom code?
   - Different settings?
   - Modified files?

5. **Screenshots or video?**
   - What you see vs what you expect
   - Error messages
   - Output Log

---

**WITH THIS INFORMATION, I CAN FIX YOUR SPECIFIC ISSUES!** ???
