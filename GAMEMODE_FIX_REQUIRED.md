# ?? **BLACK SCREEN FIX - GAMEMODE NOT LOADING!**

## **?? PROBLEM IDENTIFIED:**

Your logs show:
```
LogLoad: Game class is 'GameModeBase'
```

**This means `AFRGameMode` is NOT loading!** Without it:
- ? No lighting fixes run
- ? No emergency light spawns
- ? Screen stays black

---

## **? FIX - SET GAMEMODE IN WORLD SETTINGS:**

### **Step 1: Open FrontlineMap**
1. In Unreal Editor, open `Content/Maps/FrontlineMap`

### **Step 2: Open World Settings**
1. In the menu bar: **Settings** ? **World Settings**
2. Or press: **Alt + 8**

### **Step 3: Set GameMode Override**
1. In World Settings panel, find **Game Mode**
2. Look for **GameMode Override**
3. **SET IT TO:** `AFRGameMode`
4. Save the map (Ctrl+S)

---

## **?? BEFORE vs AFTER:**

### **Before (Current):**
```
World Settings:
  GameMode Override: None (or GameModeBase)
  
Result:
  ? Uses default GameModeBase
  ? No custom code runs
  ? Black screen
```

### **After (Fixed):**
```
World Settings:
  GameMode Override: AFRGameMode
  
Result:
  ? Uses your AFRGameMode
  ? Emergency lighting spawns
  ? Rendering fixes apply
  ? VISIBLE!
```

---

## **?? ALTERNATIVE FIX (If World Settings doesn't work):**

### **Edit DefaultEngine.ini:**

Add this line to force the GameMode:

```ini
[/Script/EngineSettings.GameMapsSettings]
GameDefaultMap=/Game/Maps/FrontlineMap
EditorStartupMap=/Game/Maps/FrontlineMap
GlobalDefaultGameMode=/Script/Frontline.AFRGameMode
ServerDefaultMap=/Game/Maps/FrontlineMap
```

---

## **?? AFTER APPLYING FIX:**

When you press Play, you should see in the logs:

```
LogFrontline: [GameMode] ? Forced rendering settings + BLACK SCREEN FIXES
LogFrontline: [GameMode] ? EMERGENCY LIGHT spawned at 300m high!
LogTemp: Warning: [GameMode] ?? ISLAND SPAWNED AT: (X, Y, Z)
```

If you see those logs, the GameMode is working and lighting should appear!

---

## **?? QUICK TEST:**

1. Open map in editor
2. Open World Settings (Alt+8)
3. Set GameMode Override = AFRGameMode
4. Save (Ctrl+S)
5. Press Play
6. **CHECK OUTPUT LOG** for "GameMode" messages

If you see GameMode logs, it's working!

---

**DO THIS NOW AND REPORT BACK!** ???

