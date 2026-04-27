# ?? **PLAY YOUR GAME IN 2 HOURS - QUICK WIN GUIDE**

## **GOAL: Get from "code complete" to "playable prototype" in ONE session**

---

## **?? HOUR 1: BASIC LEVELS**

### **Minute 0-15: Main Menu Level**

1. **Open Unreal Editor**
2. **File** ? **New Level** ? **Empty Level**
3. **Save As:** `Content/Maps/MainMenu.umap`
4. **Add:**
   - `Player Start` actor (anywhere)
   - `DirectionalLight` (for visibility)
   - `SkyLight` (for ambient light)
   - `PostProcessVolume` (infinite extent = yes)
5. **Open Level Blueprint:**
   - Right-click ? **Open Level Blueprint**
   - Add nodes:
   ```
   Event BeginPlay
   ? Create Widget (select: WBP_MainMenu - we'll make this next)
   ? Add to Viewport
   ? Set Input Mode UI Only
   ? Show Mouse Cursor
   ```
6. **Test:** Press Play (F key) - you'll see nothing yet, but level loads!

### **Minute 15-30: Main Menu Widget**

1. **Content Browser** ? Right-click ? **User Interface** ? **Widget Blueprint**
2. **Name:** `WBP_MainMenu`
3. **Open** the widget
4. **Add widgets:**
   - Drag `Canvas Panel` to hierarchy (root)
   - Drag `Vertical Box` onto Canvas Panel
   - Inside Vertical Box:
     - Add `Text` ? Change to "FRONTLINE: THE CAUSAL WAR" (size 48)
     - Add `Button` ? Name it "Button_Play"
       - Inside button, add `Text` ? "PLAY GAME"
     - Add `Button` ? "Button_Quit"
       - Inside button, add `Text` ? "QUIT"
5. **Hook up Play button:**
   - Select `Button_Play` in hierarchy
   - In Details panel, scroll to **Events** section
   - Click **+ On Clicked**
   - This opens **Graph** view
   - Add node: `Open Level` (by Name)
   - Connect to OnClicked
   - Level Name = `Lobby`
6. **Hook up Quit button:**
   - Same process
   - Add node: `Quit Game`
7. **Compile & Save**

### **Minute 30-45: Lobby Level**

1. **File** ? **New Level** ? **Empty Level**
2. **Save As:** `Content/Maps/Lobby.umap`
3. **Add:**
   - `Player Start` (multiple - place 10+ around)
   - `DirectionalLight`
   - `SkyLight`
   - `Floor` (just a big plane or landscape)
4. **Add your systems:**
   - Place `AFRPregameIsland` actor (if it shows in Content Browser)
   - If not, we'll spawn it via code
5. **Test:** Change **Project Settings** ? **Maps & Modes** ? **Default Maps** ? **Editor Startup Map** = `MainMenu`
6. **Press Play:** Main menu should appear, clicking Play goes to Lobby!

### **Minute 45-60: Game Map**

1. **File** ? **New Level** ? **Empty Level**
2. **Save As:** `Content/Maps/TIZ_Test_01.umap`
3. **Quick environment:**
   - Add **Landscape** (Landscape Mode ? Create New)
   - Size: 63x63 (small for testing)
   - Click **Create**
4. **Add spawns:**
   - Place `Player Start` actors (50+ scattered across landscape)
5. **Add actors:**
   - `AFRGameMode` (should auto-spawn if set as default Game Mode)
   - `AFRGameState` (auto-created by Game Mode)
   - `AFRZoneController` (for zone shrinking)

---

## **?? HOUR 2: MAKE IT PLAYABLE**

### **Minute 60-75: Set Up Game Mode**

1. **Edit** ? **Project Settings**
2. **Maps & Modes** section:
   - **Default GameMode:** Select `AFRGameMode`
   - **Default Pawn Class:** Use `AFRCharacter` (if you have one) or `Character` (Unreal default)
3. **Game Mode settings:**
   - Open `AFRGameMode` Blueprint (if exists) or create new one
   - Set player count, match duration, etc.

### **Minute 75-90: Basic HUD**

1. **Create:** `WBP_InGameHUD` widget
2. **Add simple elements:**
   - Canvas Panel (root)
   - Text (top-left) ? "Health: 100"
   - Text (bottom-center) ? "Ammo: 30/120"
   - Text (top-right) ? "Players Alive: 100"
3. **Make it show:**
   - Open `AFRGameMode` (or PlayerController)
   - In **BeginPlay:**
   ```
   Create Widget (WBP_InGameHUD)
   ? Add to Viewport
   ```

### **Minute 90-105: Test Full Flow**

1. **Set startup map:** `MainMenu`
2. **Press Play (F)**
3. **Click "PLAY GAME"**
4. **Should load Lobby**
5. **Manually travel to game:** Open console (`~` key)
   - Type: `open TIZ_Test_01`
   - Press Enter
6. **You should spawn in game map!**

### **Minute 105-120: Add Bots**

1. **In game map level:**
2. **Open Level Blueprint**
3. **Add nodes:**
   ```
   Event BeginPlay
   ? Get Game Mode
   ? Cast to AFRGameMode
   ? Get Subsystem (FRBotSpawner)
   ? Spawn Bots (count: 10)
   ```
4. **Or in C++** (already have this):
   - `AFRGameMode::BeginPlay()` ? `BotSpawner->SpawnBots(99);`

5. **Test:** Should see bots running around!

---

## **?? RESULT AFTER 2 HOURS:**

? Main menu that works
? Lobby level (basic)
? Game map (playable)
? Bots spawning
? Can shoot and play!

**Not perfect, but PLAYABLE!**

---

## **?? NEXT STEPS (After Your First Play Session):**

### **Polish Pass 1 (Next Session):**
- Make main menu prettier (add background image)
- Add actual operator selection screen
- Show currency in UI
- Make HUD look better

### **Polish Pass 2 (Week 2):**
- Add weapon models
- Add animations
- Add sound effects
- Make lobby countdown work

### **Polish Pass 3 (Week 3):**
- Add all 20 operators
- Implement abilities
- Add Battle Pass UI
- Add marketplace

---

## **?? DEBUGGING TIPS**

### **If Main Menu doesn't show:**
```
Check:
1. Level Blueprint has "Create Widget" node
2. Widget is added to viewport
3. Input mode set to UI Only
4. Mouse cursor is visible
```

### **If "Play" button doesn't work:**
```
Check:
1. OnClicked event is bound
2. "Open Level" node has correct name ("Lobby")
3. Lobby.umap exists in Content/Maps/
```

### **If Lobby is black:**
```
Check:
1. Lobby has DirectionalLight
2. Lobby has SkyLight
3. Build Lighting (Build ? Build Lighting)
```

### **If Game crashes on Play:**
```
Check:
1. Game Mode is set correctly
2. Player Start actors exist
3. No missing references in blueprints
```

---

## **?? KEYBOARD SHORTCUTS**

```
F = Play in Editor
Esc = Stop playing
Alt+P = Play in new window
~ = Open console
Tab = Toggle mouse cursor in game
```

---

## **?? CHECKLIST**

- [ ] Main Menu level created
- [ ] Main Menu widget created
- [ ] Play button works
- [ ] Lobby level created
- [ ] Game map created
- [ ] Player can spawn
- [ ] Bots spawn (even if just standing)
- [ ] Can move and look around
- [ ] HUD shows basic info
- [ ] Match starts and runs

**When all checked:** YOU HAVE A PLAYABLE GAME! ??

---

## **?? FINAL NOTE**

**This is a PROTOTYPE.** It won't be pretty, polished, or perfect. But it will be **PLAYABLE**.

And once it's playable, you can:
- Show friends
- Get feedback
- Iterate
- Polish
- Add content
- Make it beautiful

**The hardest part (systems code) is DONE. Now you're just making it look good!**

---

**Ready? Open Unreal and start the timer!** ????

**See you on the battlefield, Commander!** ????
