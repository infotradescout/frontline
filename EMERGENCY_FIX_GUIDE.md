# ?? **EMERGENCY FIX GUIDE - CAN'T SEE/MOVE**

## **IMMEDIATE FIXES APPLIED:**

### **? Fix #1: Lighting Restored**
- Added directional light (sun) at intensity 10
- Added sky light at intensity 2
- Should now be BRIGHT and visible

### **? Fix #2: Island Spawns Closer**
- Changed spawn distance: 10km-30km ? 0km-5km
- Lowered height: 1000 ? 500
- Should now be RIGHT NEXT TO YOU

### **? Fix #3: Build Required**
```
STOP! REBUILD THE PROJECT NOW!
1. Close Unreal Editor (if open)
2. Open Visual Studio
3. Build Solution (F7)
4. Wait for success
5. Launch Unreal Editor
```

---

## **?? TEST PROCEDURE (DO THIS NOW):**

### **Step 1: Create Test Level**
```
1. Open Unreal Editor
2. File ? New Level ? Basic
3. Save As: Content/Maps/TestLevel
```

### **Step 2: Set Game Mode**
```
1. World Settings (top toolbar)
2. GameMode Override: AFRGameMode
3. Default Pawn Class: (whatever character you have)
```

### **Step 3: Add Basic Floor**
```
1. Place Actors panel ? search "Cube"
2. Drag into viewport
3. Scale: X=100, Y=100, Z=1
4. Position: X=0, Y=0, Z=0
```

### **Step 4: Add Player Start**
```
1. Place Actors ? search "Player Start"
2. Drag into viewport
3. Position: X=0, Y=0, Z=200
```

### **Step 5: PRESS PLAY**
```
Press F key

You should see:
? Bright lighting
? Gray floor
? Can move with WASD
? Can look with mouse
```

---

## **?? EXPECTED OUTPUT LOG:**

```
LogFrontline: ?? Spawned directional light
LogFrontline: ??? Spawned sky light
LogFrontline: ?? Generated island location at distance X from center
LogFrontline: ? Pregame island spawned
LogFrontline: ? Created 20 player spawners
LogFrontline: ? Created island barrier
LogFrontline: ??? Warmup started
```

---

## **? IF STILL CAN'T SEE:**

### **Issue: Pitch Black**
```
Open console (~)
Type: r.SetNearClipPlane 1
Type: r.TonemapperFilm 1
Type: stat fps
```

If you see FPS counter, lighting is working but something else is wrong.

### **Issue: Can't Move**
```
Problem: No input bindings

Fix:
1. Edit ? Project Settings ? Input
2. Check for these Action Mappings:
   - MoveForward (W, S keys)
   - MoveRight (A, D keys)
   - Turn (Mouse X)
   - LookUp (Mouse Y)
   - Jump (Space)

If missing, add them:
- Action Mappings ? +
- Name: MoveForward
- Key: W, Scale: 1.0
- Add another: S, Scale: -1.0
- Repeat for others
```

### **Issue: Still Spawning Wrong**
```
Override GameMode spawn:

In Level Blueprint (Blueprints ? Open Level Blueprint):

Event BeginPlay
? Get Player Pawn (index 0)
? Set Actor Location
   Location: (0, 0, 200)
```

---

## **?? NUCLEAR OPTION (IF NOTHING WORKS):**

### **Create Minimal Test:**
```
1. File ? New Level ? Basic
2. Don't add anything
3. Press Play
4. Console: Ghost (enables flying through walls)
5. Console: Slomo 0.1 (slow motion)
6. Look around

If you can see ANYTHING (sky, fog, etc):
   ? Lighting works, problem is level/spawn
   
If you see NOTHING (pitch black):
   ? Lighting broken, more serious issue
```

---

## **?? TELL ME:**

After rebuilding and testing, report:

1. **Can you see anything?**
   - Yes/No
   - What do you see?

2. **What color is the screen?**
   - Black?
   - Gray?
   - Blue?

3. **Can you move at all?**
   - WASD?
   - Mouse?
   - Nothing?

4. **What's in Output Log?**
   - Copy the lighting messages
   - Any errors?

---

## **? QUICK FIX COMMANDS:**

**In-game console (press ~ ):**
```
# Fix lighting
r.SetNearClipPlane 1
stat fps
viewmode lit

# Enable movement
Ghost
Fly

# Check position
getall PlayerStart Location

# Teleport to origin
Teleport 0 0 200

# Spawn light manually
summon DirectionalLight
```

---

**REBUILD NOW AND TRY THE TEST LEVEL!** ?????

**Then tell me EXACTLY what happens!**
