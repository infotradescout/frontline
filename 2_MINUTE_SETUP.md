# ? **2-MINUTE SETUP - START PLAYING NOW!**

## **?? THE PROBLEM:**

You press Play ? Game loads Engine's default map ? Nothing happens

## **? THE FIX:**

### **I ALREADY DID THIS FOR YOU:**
```
? Updated Config/DefaultEngine.ini
? Configured to use AFRGameMode
? Configured to use UFRGameInstanceBase
```

### **YOU NEED TO DO THIS (2 minutes):**

---

## **?? STEP-BY-STEP:**

### **1. Open Unreal Editor**
```
Double-click: Frontline.uproject
Wait for it to load
```

### **2. Create Maps Folder**
```
In Content Browser (bottom panel):
? Right-click in Content folder
? New Folder
? Name it: Maps
? Press Enter
```

### **3. Create New Empty Level**
```
Top menu:
? File
? New Level
? Select: Empty Level (NOT Template!)
? Click "Create"
```

### **4. Save the Level**
```
Top menu:
? File
? Save Current Level As...

In the dialog:
? Navigate to: Content/Maps folder
? File name: FrontlineMap
? Click "Save"
```

### **5. Restart Unreal Editor**
```
? File
? Exit

Then double-click Frontline.uproject again
```

### **6. Press Play!**
```
? Click Play button (or press Alt+P)

Watch the Output Log:
? Window
? Developer Tools
? Output Log

Look for:
[Frontline] Auto Setup Manager initialized
[Frontline] ??? ALL SYSTEMS OPERATIONAL ???
[Frontline] Auto Content Generator starting...
[Frontline] === CONTENT GENERATION COMPLETE ===
```

---

## **?? WHAT YOU'LL SEE:**

```
Screen appears (may be dark at first)
?
Auto-generator runs (check Output Log)
?
Ground appears beneath you
?
Lighting turns on
?
You can move with WASD
?
You're inside pregame barrier
?
Wait 90 seconds for match to start
?
Barriers drop automatically
?
You can exit spawn area!
```

---

## **? VERIFICATION:**

**The game is working if you see in Output Log:**
```
[Frontline] Game Instance initializing...
[Frontline] Auto Setup Manager initialized
[Frontline] ? Starting currency granted (1000 credits, 100 gold)
[Frontline] ? Starter items unlocked
[Frontline] ??? ALL SYSTEMS OPERATIONAL ???
[Frontline] Auto Content Generator starting...
[Frontline] [Content Gen] Generating test map...
[Frontline] [Content Gen] ? Ground plane created
[Frontline] [Content Gen] Generating pregame area...
[Frontline] [Content Gen] ? Pregame barrier created
[Frontline] [Content Gen] ? 8 spawn points created
[Frontline] [Content Gen] ? 12 cover objects created
[Frontline] === CONTENT GENERATION COMPLETE ===
[Frontline] Game is ready to play!
```

---

## **? COMMON MISTAKES:**

### **Mistake 1: Using Template Level**
```
? File ? New Level ? Template
? File ? New Level ? Empty Level
```

### **Mistake 2: Wrong file name**
```
? Content/FrontlineMap.umap
? Content/Maps/FrontlineMap.umap
```

### **Mistake 3: Not restarting editor**
```
Config changes require restart!
Close and reopen Unreal Editor
```

---

## **?? THAT'S IT!**

**Total Time: 2 minutes**

**After these steps:**
- ? Game will use your custom systems
- ? Everything auto-generates
- ? You can play immediately
- ? All 9 systems working

---

## **?? VISUAL GUIDE:**

```
1. Content Browser
   ?? Content/
      ?? Maps/  ? CREATE THIS FOLDER
         ?? FrontlineMap.umap  ? SAVE LEVEL HERE

2. Config/DefaultEngine.ini  ? ALREADY UPDATED
   GameDefaultMap=/Game/Maps/FrontlineMap
   GlobalDefaultGameMode=/Script/Frontline.AFRGameMode
   GameInstanceClass=/Script/Frontline.UFRGameInstanceBase

3. Press Play
   ? Auto-setup runs
   ? Auto-generation runs
   ? Game starts!
```

---

## **?? TIME BREAKDOWN:**

```
Create Maps folder:        10 seconds
Create Empty Level:        20 seconds
Save as FrontlineMap:      20 seconds
Restart Unreal Editor:     60 seconds
Press Play:                10 seconds
?????????????????????????????????
TOTAL:                     2 minutes
```

---

## **?? SUCCESS LOOKS LIKE:**

When you press Play:

```
? Screen loads (even if dark initially)
? Output Log shows system initialization
? Ground appears
? Lighting appears
? You can move (WASD keys)
? You can look around (mouse)
? Pregame countdown starts
```

---

## **?? PRO TIP:**

Keep Output Log open while testing:
```
Window ? Developer Tools ? Output Log

This shows you:
- All system initialization
- Auto-generation progress
- Match flow phases
- Any errors or warnings
```

---

## **?? STILL NOT WORKING?**

**Check these:**

1. **Config file updated?**
   ```
   Open: Config/DefaultEngine.ini
   Look for: GameDefaultMap=/Game/Maps/FrontlineMap
   If not there, I'll update it again
   ```

2. **Map file exists?**
   ```
   Check: Content/Maps/FrontlineMap.umap
   If not there, create it (steps above)
   ```

3. **Editor restarted?**
   ```
   Config changes need restart
   Close and reopen editor
   ```

4. **Game compiled?**
   ```
   Should say "Compiled successfully"
   If errors, rebuild in Visual Studio
   ```

---

**DO THESE STEPS AND YOU'LL BE PLAYING IN 2 MINUTES!** ???

The game IS complete - we just need to create the map file that triggers everything!
