# ?? **COMPLETE UNREAL EDITOR SETUP GUIDE**

## **FOLLOW THESE STEPS EXACTLY - 60 MINUTES TO PLAYABLE GAME**

---

## **? STEP 1: BUILD THE PROJECT (5 minutes)**

1. **Open Visual Studio**
2. **Build Solution** (F7)
3. **Wait for compile** (should succeed - all C++ is ready!)
4. **Close Visual Studio**

---

## **? STEP 2: LAUNCH UNREAL EDITOR (2 minutes)**

1. **Find** `Frontline.uproject` in `C:\Users\FlavorGood\Documents\Unreal Projects\Frontline\`
2. **Double-click** to open
3. **Wait** for Unreal Editor to load (first time takes 2-5 minutes)
4. **If prompted:** "Would you like to rebuild?" ? Click **YES**

---

## **? STEP 3: CREATE MAIN MENU LEVEL (5 minutes)**

### **A. Create Level**
```
1. File ? New Level ? Empty Level
2. Save As ? Content/Maps/MainMenu.umap
```

### **B. Add Basic Lighting**
```
1. Place Actors panel (left side) ? search "Directional Light"
2. Drag into viewport
3. Leave default settings
```

### **C. Add Player Start**
```
1. Place Actors ? search "Player Start"
2. Drag into viewport (anywhere)
```

### **D. Create Level Blueprint**
```
1. Blueprints menu (top toolbar) ? Open Level Blueprint
2. In the blueprint graph:
   - Right-click ? Add Event ? Event BeginPlay
   - From BeginPlay, drag out ? search "Create Widget"
   - Class dropdown ? select "WBP_MainMenu" 
     (if not visible, compile your C++ first!)
   - From Create Widget output ? search "Add to Viewport"
   - From Add to Viewport ? search "Get Player Controller"
   - From Get Player Controller ? search "Set Show Mouse Cursor"
   - Check the box next to "Show Mouse Cursor"
   - From Get Player Controller ? search "Set Input Mode UI Only"
3. Compile (green checkmark)
4. Save
5. Close blueprint editor
```

---

## **? STEP 4: CREATE MAIN MENU WIDGET (10 minutes)**

### **A. Create Widget Blueprint**
```
1. Content Browser (bottom panel) ? Right-click ? User Interface ? Widget Blueprint
2. Name: WBP_MainMenu
3. Parent Class: WBP_MainMenu (the C++ class we created)
4. Open it (double-click)
```

### **B. Build the UI (Drag from Palette panel on left)**

**Root Structure:**
```
1. Drag "Canvas Panel" to hierarchy (top-right panel)
2. Select Canvas Panel ? Details panel ? check "Is Variable" box
```

**Add Background:**
```
1. Drag "Image" onto Canvas Panel
2. Rename to "Background"
3. In Details panel:
   - Anchors: Full screen (bottom-right option)
   - Brush Color: Black (R=0, G=0, B=0, A=1)
```

**Add Title:**
```
1. Drag "Text Block" onto Canvas Panel
2. Rename to "Text_Title"
3. In Details panel:
   - Anchors: Top-center
   - Position: X=0, Y=100
   - Size: X=800, Y=100
   - Text: "FRONTLINE: THE CAUSAL WAR"
   - Font Size: 48
   - Justification: Center Aligned
   - Color: Orange (R=1, G=0.6, B=0, A=1)
   - Shadow Offset: X=2, Y=2
```

**Add Play Button:**
```
1. Drag "Button" onto Canvas Panel
2. Rename to "Button_Play"
3. In Details panel:
   - Check "Is Variable" box (IMPORTANT!)
   - Anchors: Center
   - Position: X=0, Y=-50
   - Size: X=400, Y=80
   - Style ? Normal:
     - Tint: Dark Gray (R=0.1, G=0.1, B=0.1)
   - Style ? Hovered:
     - Tint: Medium Gray (R=0.3, G=0.3, B=0.3)
   - Style ? Pressed:
     - Tint: Light Gray (R=0.5, G=0.5, B=0.5)
4. Drag "Text Block" ONTO Button_Play (make it a child)
5. In Details:
   - Text: "PLAY GAME"
   - Font Size: 32
   - Justification: Center
   - Color: White
```

**Add Settings Button:**
```
1. Duplicate Button_Play (Ctrl+D)
2. Rename to "Button_Settings"
3. Check "Is Variable" box
4. Position: X=0, Y=50
5. Change button text to "SETTINGS"
```

**Add Quit Button:**
```
1. Duplicate Button_Settings (Ctrl+D)
2. Rename to "Button_Quit"
3. Check "Is Variable" box (already checked if duplicated)
4. Position: X=0, Y=150
5. Change button text: "QUIT GAME"
```

**Add Currency Display (Optional):**
```
1. Drag "Text Block" onto Canvas Panel
2. Rename: "Text_Credits"
3. Check "Is Variable" box
4. Anchors: Top-right
5. Position: X=-200, Y=50
6. Text: "Credits: 0"
7. Font Size: 24

8. Duplicate for "Text_Gold"
9. Position: X=-200, Y=80
10. Text: "Gold: 0"
```

### **C. Compile & Save**
```
1. Click green "Compile" button (top-right)
2. Save (Ctrl+S)
3. Close widget editor
```

---

## **? STEP 5: CREATE LOBBY LEVEL (10 minutes)**

### **A. Create Level**
```
1. File ? New Level ? Empty Level
2. Save As ? Content/Maps/Lobby.umap
```

### **B. Add Floor**
```
1. Place Actors ? search "Cube"
2. Drag into viewport
3. In Details panel:
   - Location: X=0, Y=0, Z=0
   - Scale: X=100, Y=100, Z=1
4. Select Material ? M_Basic_Floor (or leave default gray)
```

### **C. Add Walls (Optional)**
```
1. Place 4 more cubes for walls:
   - Front: Scale (100, 1, 10), Location (0, -5000, 500)
   - Back: Scale (100, 1, 10), Location (0, 5000, 500)
   - Left: Scale (1, 100, 10), Location (-5000, 0, 500)
   - Right: Scale (1, 100, 10), Location (5000, 0, 500)
```

### **D. Add Spawn Points**
```
1. Place Actors ? Player Start
2. Place 10-20 around the floor
3. Quick way:
   - Place one
   - Select it
   - Alt+Drag to duplicate
   - Spread them out (Z height should be ~200)
```

### **E. Add Lighting**
```
1. Place Actors ? Directional Light
   - Rotation: (0, -45, 0)
   - Intensity: 5

2. Place Actors ? Sky Light
   - Intensity: 1

3. Place Actors ? Sky Atmosphere
   (gives you a nice sky automatically)
```

### **F. Create Lobby HUD**
```
1. Content Browser ? Right-click ? Widget Blueprint
2. Name: WBP_LobbyHUD
3. Parent: WBP_LobbyHUD (C++ class)
4. Open it
5. Add these widgets:
   - Canvas Panel (root)
   - Text Block: "Text_Status" 
     - Text: "Waiting for players..."
     - Anchors: Top-center
     - Font Size: 36
   - Text Block: "Text_PlayerCount"
     - Text: "Players: 0/100"
     - Check "Is Variable"
     - Anchors: Top-left
   - Text Block: "Text_Countdown"
     - Text: "01:30"
     - Check "Is Variable"
     - Anchors: Center
     - Font Size: 72
6. Compile & Save
```

### **G. Add HUD to Level Blueprint**
```
1. Blueprints ? Open Level Blueprint
2. Add nodes:
   - Event BeginPlay
   ? Create Widget (WBP_LobbyHUD)
   ? Add to Viewport
3. Compile & Save
```

---

## **? STEP 6: CREATE GAME MAP (15 minutes)**

### **A. Create Level**
```
1. File ? New Level ? Empty Level
2. Save As ? Content/Maps/GameMap_Test.umap
```

### **B. Option 1: Simple Floor (EASY)**
```
1. Place Actors ? Cube
2. Scale: X=1000, Y=1000, Z=1
3. Material: Dark gray or leave default
```

### **B. Option 2: Landscape (REALISTIC but slower)**
```
1. Mode panel (left) ? Landscape
2. Click "Create New"
3. Settings:
   - Section Size: 63x63
   - Sections Per Component: 1
   - Number of Components: 8x8
4. Click "Create"
5. Wait 10-30 seconds for generation
```

### **C. Add Cover Objects (Basic Boxes)**
```
1. Place Actors ? Cube
2. Random scales: X=2-5, Y=2-5, Z=3-8
3. Place 20-30 around map
4. For variation:
   - Select cube
   - Details ? Materials ? Element 0
   - Change color (brown, gray, red)
5. Quick duplicate: Select cube ? Alt+Drag
```

### **D. Add 100 Spawn Points**
```
1. Place Actors ? Player Start
2. Place first one
3. Select it ? Alt+Drag to duplicate
4. Keep duplicating until you have 100
5. Spread evenly across map
6. Z height should be ~200 (above ground)
```

### **E. Add Lighting**
```
1. Place Actors ? Directional Light
2. Place Actors ? Sky Light
3. Place Actors ? Exponential Height Fog
4. Place Actors ? Post Process Volume
   - In Details: Check "Infinite Extent (Unbound)"
```

### **F. Create Game HUD**
```
1. Content Browser ? Widget Blueprint
2. Name: WBP_GameHUD
3. Parent: WBP_GameHUD (C++ class)
4. Open it
5. Add these widgets:

Canvas Panel (root)
??? Text Block: "Text_PlayersAlive"
?   - Text: "100 Alive"
?   - Anchors: Top-left
?   - Check "Is Variable"
??? Text Block: "Text_Health"
?   - Text: "HP: 100/100"
?   - Anchors: Bottom-left
?   - Check "Is Variable"
??? Progress Bar: "ProgressBar_Health"
?   - Anchors: Bottom-left (below health text)
?   - Size: 200x20
?   - Check "Is Variable"
??? Text Block: "Text_Ammo"
?   - Text: "30 / 120"
?   - Anchors: Bottom-center
?   - Font Size: 32
?   - Check "Is Variable"
??? Crosshair (4 borders):
    - Border: "Crosshair_Top" (2x10, white, center)
    - Border: "Crosshair_Bottom" (2x10, white, center)
    - Border: "Crosshair_Left" (10x2, white, center)
    - Border: "Crosshair_Right" (10x2, white, center)
    - Check "Is Variable" for all

6. Compile & Save
```

### **G. Add HUD to GameMode or PlayerController**

**Easy Way (Level Blueprint):**
```
1. Blueprints ? Open Level Blueprint
2. Add nodes:
   - Event BeginPlay
   ? Delay (0.1 seconds)
   ? Create Widget (WBP_GameHUD)
   ? Add to Viewport
3. Compile & Save
```

---

## **? STEP 7: SET DEFAULT MAPS (2 minutes)**

```
1. Edit ? Project Settings
2. Search for "Maps & Modes"
3. Set:
   - Editor Startup Map: MainMenu
   - Game Default Map: MainMenu
   - Server Default Map: Lobby
4. Save
5. Close Project Settings
```

---

## **? STEP 8: TEST THE GAME! (5 minutes)**

### **A. Test Main Menu**
```
1. Close all open levels
2. Open: Content/Maps/MainMenu
3. Press Play (Alt+P or F key)
4. Should see:
   - Black background
   - "FRONTLINE" title in orange
   - Three buttons (Play, Settings, Quit)
5. Click "Play" ? Should load Lobby
```

### **B. Test Lobby**
```
1. In Lobby level
2. Should see:
   - Gray floor
   - "Waiting for players..." text
   - Countdown timer
3. Open console (~ key)
4. Type: open GameMap_Test
5. Press Enter
```

### **C. Test Game Map**
```
1. Should spawn in game map
2. Should see:
   - HUD with health/ammo
   - Crosshair in center
   - Can move (WASD)
   - Can look (mouse)
```

---

## **? STEP 9: ADD PROCEDURAL MAP GENERATION (5 minutes)**

### **Open AFRMapGenerator Blueprint (if exists) or Add to GameMode**

```
1. In Game Map level:
2. Place Actors ? search "AFRMapGenerator"
3. If found, place it
4. In Details panel:
   - Seed: 12345 (or any number)
5. Press Play
6. Should generate procedural buildings and cover!
```

**If AFRMapGenerator doesn't appear:**
```
You may need to create it in Blueprints:
1. Content Browser ? Blueprints ? Right-click ? Blueprint Class
2. Parent: Actor
3. Name: BP_MapGenerator
4. Open it
5. Add Component: AFRMapGenerator (if available)
6. Or call GenerateMap() function in BeginPlay
```

---

## **? STEP 10: BUILD & PACKAGE (Optional - For Testing)**

### **Quick Test Build**
```
1. File ? Package Project ? Windows ? Windows (64-bit)
2. Choose output folder
3. Wait 10-30 minutes for cooking/packaging
4. Run the .exe to test standalone
```

---

## **?? CONGRATULATIONS!**

### **You Now Have:**
? Functional main menu
? Lobby system
? Playable game map
? HUD with health/ammo/crosshair
? Level transitions working
? All C++ systems integrated
? Ready for playtesting!

### **Next Steps:**
1. **Add bots** (place FRBotSpawner actor)
2. **Test multiplayer** (Play in Editor ? Net Mode: Listen Server)
3. **Add more polish** (post processing, better lighting)
4. **Integrate operators** (hook up operator selection UI)
5. **Test full match flow** (warmup ? play ? end)

---

## **?? TROUBLESHOOTING**

### **"Widget class not found in dropdown"**
```
- Make sure you compiled C++ code first
- Restart Unreal Editor
- File ? Refresh C++ project
```

### **"Black screen when playing"**
```
- Check Level Blueprint has Create Widget + Add to Viewport
- Make sure widget is compiled
- Check Output Log for errors
```

### **"Can't move character"**
```
- Make sure Game Mode is set correctly
- Check Project Settings ? Input has WASD bindings
- Try using default Third Person template controls
```

### **"Widgets don't show"**
```
- Check "Is Variable" box is checked for all widgets you reference
- Compile widget blueprint
- Check Level Blueprint logic
```

---

## **?? QUICK TIPS**

### **Faster Iteration:**
```
- Use "Simulate" (Alt+S) instead of "Play" for testing
- Alt+P opens in new window (faster than PIE)
- Keep Output Log open (Window ? Developer Tools ? Output Log)
```

### **Better Visuals (Free):**
```
- Add Post Process Volume ? Infinite Extent
- Tweak: Vignette, Film Grain, Bloom
- Use different directional light colors for mood
- Add fog (Exponential Height Fog)
```

### **Performance:**
```
- Keep poly count low on procedural meshes
- Use simple collision on cover objects
- LOD settings for distant objects
- Build lighting (Build ? Build Lighting) for better FPS
```

---

**FOLLOW THIS GUIDE STEP-BY-STEP AND YOU'LL HAVE A PLAYABLE GAME IN 1 HOUR!** ?????
