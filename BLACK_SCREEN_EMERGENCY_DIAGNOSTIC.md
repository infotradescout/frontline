# ?? **BLACK SCREEN EMERGENCY DIAGNOSTIC**

## **? IMMEDIATE ACTIONS:**

### **Step 1: Open Console & Run Diagnostics**

**Press ~ (tilde key)** in the black viewport, then type each command:

```
stat fps
```
**? Can you see FPS counter?**
- ? YES = Rendering works, lighting broken
- ? NO = Rendering completely broken

```
viewmode unlit
```
**? Can you see anything now?**
- ? YES = Lighting is the problem
- ? NO = Something else broken

```
showlog
```
**? Copy the LAST 50 LINES and send them to me**

---

### **Step 2: Check Player Position**

Type in console:
```
getall PlayerStart Location
```

Copy the output - this shows where spawn points are.

---

### **Step 3: Teleport Test**

Type in console:
```
Ghost
Teleport 0 0 30000
```

**Can you see the floating island now?**

---

## **?? DIAGNOSTIC CHECKLIST:**

Answer these questions:

### **A. What You See:**
- [ ] Pitch black (nothing at all)
- [ ] Very dark gray
- [ ] Black with UI visible
- [ ] Black with cursor visible

### **B. What You Hear:**
- [ ] Nothing (silence)
- [ ] Menu music
- [ ] Ambient sounds
- [ ] Character breathing/footsteps

### **C. Input Response:**
- [ ] Can move mouse
- [ ] Can press keys (W,A,S,D)
- [ ] Can open console (~)
- [ ] Nothing responds

### **D. Before Going Black:**
- [ ] Saw loading screen
- [ ] Saw "Waiting for players..."
- [ ] Saw countdown (90 seconds)
- [ ] Went black immediately

---

## **?? LIKELY CAUSES:**

### **Cause 1: Player Underground (80% likely)**
**Symptom:** Black screen immediately
**Why:** Spawn point at Z=0, but island at Z=30000
**Fix:** Teleport up

### **Cause 2: No Lighting (15% likely)**
**Symptom:** Black screen but can see UI
**Why:** Lights didn't spawn
**Fix:** Add lights manually

### **Cause 3: Camera Buried (5% likely)**
**Symptom:** Dark gray, can't move
**Why:** Camera inside geometry
**Fix:** Ghost mode

---

## **??? MANUAL FIXES:**

### **Fix A: Emergency Lighting**

Press ~ and type:
```
summon PointLight
```

Repeat 3-4 times. You should see lights appear around you.

### **Fix B: Force Bright**

Press ~ and type:
```
r.DefaultFeature.AutoExposure 0
r.Tonemapper.Sharpen 0
PostProcessVolume_DebugOverride 1
```

### **Fix C: See Through Walls**

Press ~ and type:
```
viewmode wireframe
```

You'll see the wireframe of everything.

---

## **?? REPORT BACK:**

**Send me this info:**

1. **Output of `stat fps`:** (FPS number or "nothing")
2. **Output of `getall PlayerStart Location`:** (coordinates)
3. **Can you see anything in `viewmode wireframe`?** (yes/no)
4. **Last 20 lines from `showlog`:** (copy/paste)

**With this info, I can give you the EXACT fix!**

---

## **?? MOST LIKELY FIX:**

Based on your floating island setup, you're probably **spawning at ground level (Z=0)** but the **island is at Z=30000** (300m high).

**Quick Fix:**
```
~ (open console)
Ghost
Teleport 0 0 30000
```

You should see the island and lighting!

