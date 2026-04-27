# ?? **VIEWPORT VISIBILITY - EMERGENCY FIXES**

## **? IMMEDIATE ACTIONS:**

### **1. Reset Camera (Most Common Fix):**
```
In Viewport:
1. Click anywhere in viewport
2. Press Home key
   OR
3. Right-click viewport ? "Focus on Selection"
   OR
4. Select any actor in Outliner
5. Press F key (focus on selected)
```

### **2. Check View Mode:**
```
Viewport top-left corner:
Click the eye icon ? Select "Lit"
(Should say "Lit" not "Wireframe" or "Unlit")
```

### **3. Console Commands:**
```
Press ~ (tilde key)
Type each command and press Enter:

viewmode lit
r.SetNearClipPlane 1
r.TonemapperFilm 1
showflag.postprocessing 1
stat fps
```

### **4. Lighting Check:**
```
If viewport is pitch black:
1. Window ? World Settings
2. Check "Force No Precomputed Lighting"
3. Or: Build ? Build Lighting Only
```

---

## **?? STEP-BY-STEP FIX:**

### **Step 1: Create Simple Test Level**
```
1. File ? New Level ? Empty Level
2. Should see gray void

If you see NOTHING (not even gray):
   ? Rendering issue (see below)
   
If you see GRAY:
   ? Just need to add objects
```

### **Step 2: Add Basic Objects**
```
1. Place Actors panel (left side)
2. Search "cube"
3. Drag "Cube" into viewport
4. Should appear somewhere

Can't see cube?
   ? Camera position issue (see below)
```

### **Step 3: Add Light**
```
1. Place Actors ? search "light"
2. Drag "Directional Light" into viewport
3. Should brighten scene

Still dark?
   ? Light settings issue (see below)
```

### **Step 4: Position Camera**
```
1. Select the cube you placed
2. Press F key (focus on cube)
3. Should zoom to cube

Still can't see?
   ? Serious issue (see nuclear options below)
```

---

## **?? SPECIFIC ISSUES & FIXES:**

### **Issue: Pitch Black Viewport**
```
Problem: No lighting

Fix:
1. Click "Lit" dropdown (viewport top-left)
2. Select "Unlit"
3. Can you see now?

If YES in Unlit but NO in Lit:
   ? Need to add lights (see Step 3 above)
   
If NO even in Unlit:
   ? Rendering broken (see nuclear options)
```

### **Issue: Can See Outliner But Not Viewport**
```
Problem: Viewport not rendering

Fix:
1. Click inside viewport
2. Press Alt+F4 to close editor
3. Reopen project
4. Check if viewport works now

If still broken:
   ? Graphics driver issue (see below)
```

### **Issue: Viewport Shows Only Sky**
```
Problem: Camera looking at empty space

Fix:
1. Window ? World Outliner
2. Find any actor (Floor, PlayerStart, etc.)
3. Double-click it
4. Should jump to that object

No actors in Outliner?
   ? Level is empty (see Step 2 above)
```

### **Issue: "Viewport [0]" Title But Black**
```
Problem: Viewport exists but not rendering

Fix:
1. Right-click viewport tab
2. Close tab
3. Window ? Viewports ? Viewport 1
4. Creates new viewport

Still black?
   ? Graphics driver issue (see below)
```

---

## **? NUCLEAR OPTIONS:**

### **Option 1: Reset Editor Layout**
```
1. Window ? Load Layout
2. Select "Default Editor Layout"
3. Confirm

This resets everything including viewport.
```

### **Option 2: Delete Editor Preferences**
```
CLOSES EDITOR FIRST!

Then delete:
C:\Users\[YourName]\AppData\Local\UnrealEngine\Editor

Reopen editor - will reset all settings.
```

### **Option 3: Update Graphics Drivers**
```
If nothing else works:

1. Open Device Manager
2. Display Adapters ? Your GPU
3. Right-click ? Update Driver
4. Restart computer
5. Try Unreal again
```

### **Option 4: Verify Engine Installation**
```
1. Epic Games Launcher
2. Library ? Unreal Engine
3. Click three dots next to 5.7
4. Verify
5. Wait for verification
6. Reopen project
```

---

## **?? DIAGNOSTIC INFO NEEDED:**

Please tell me:

### **1. What do you see?**
- [ ] Completely black
- [ ] Gray void
- [ ] Blue/sky color
- [ ] White
- [ ] Flickering
- [ ] Nothing at all (blank)

### **2. Can you see these UI elements?**
- [ ] Top menu bar (File, Edit, Window)
- [ ] Left panel (Place Actors)
- [ ] Right panel (Details)
- [ ] Bottom panel (Content Browser)
- [ ] World Outliner

### **3. When you press ~, can you type?**
- [ ] Yes, console opens
- [ ] No, nothing happens

### **4. Check this:**
```
Window ? Developer Tools ? Output Log

Do you see ANY text?
Copy the last 10-20 lines and send them.
```

---

## **?? MOST LIKELY CAUSES:**

### **Based on your previous issues:**

**1. Camera Position (80% chance):**
- You're spawning at island (Z=100)
- Camera might be underground or far away
- **Fix:** Press Home key or F to focus

**2. No Lighting (15% chance):**
- AutoLevelGenerator adds lighting but might have failed
- **Fix:** Manually add Directional Light

**3. Rendering Disabled (4% chance):**
- View mode set to wrong mode
- **Fix:** viewmode lit command

**4. Graphics Issue (1% chance):**
- Driver problem
- **Fix:** Update drivers

---

## **? QUICK TEST:**

### **Do This Right Now:**

```
1. Open Unreal Editor
2. File ? New Level ? Basic (NOT Empty!)
3. Press Play (F key)
4. Can you see anything?

Report back what you see!
```

The "Basic" level template includes:
- Floor
- Sky
- Player start
- Lights

If you CAN see in Basic level:
   ? Your game level has issue, not editor
   
If you CANNOT see in Basic level:
   ? Editor/graphics issue

---

## **?? AFTER YOU CAN SEE:**

Once viewport is working, we need to fix:
1. Spawn position (might be underground)
2. Island position (might be too high/far)
3. Camera setup
4. Level lighting

---

**REPORT BACK WITH:**
1. What you see (black/gray/nothing)
2. Can you see UI elements?
3. Result of "Basic" level test

**I'LL FIX IT IMMEDIATELY!** ???

