# ?? QUICK START - Make It Playable NOW (2 Hours)

## **Goal: Playable Game in 2 Hours**

This is the fastest path to a working game. We'll use placeholders and get you playing ASAP.

---

## ? **Step 1: Create Game Instance (5 min)**

### **In Unreal Editor:**

1. **Create Blueprint:**
   ```
   Content Browser ? Right Click ? Blueprint Class
   ? Search: "FRGameInstanceBase"
   ? Name: "BP_FRGameInstance"
   ```

2. **Set as Default:**
   ```
   Edit ? Project Settings
   ? Maps & Modes
   ? Game Instance Class: BP_FRGameInstance
   ```

3. **Configure:**
   ```
   Open BP_FRGameInstance
   
   Settings:
   ?? Only Starting Pistol At Spawn: TRUE
   ?? Max Players: 10 (for testing)
   ?? Min Players To Start: 1
   ?? Lobby Duration: 10.0
   ?? Pregame Duration: 5.0
   ```

---

## ? **Step 2: Create Starter Pistol (10 min)**

### **A. Create Data Asset:**

```
Content Browser ? Right Click
? Miscellaneous ? Data Asset
? Class: FREnhancedWeaponData
? Name: "DA_Pistol_Starter"
```

### **B. Configure Pistol:**

```
Open DA_Pistol_Starter

Weapon Info:
?? Weapon ID: Pistol_Starter
?? Weapon Name: "Starter Pistol"
?? Weapon Type: Pistol
?? Ammo Type: LightAmmo

Firing:
?? Fire Mode: SemiAuto
?? Fire Rate: 0.15
?? Burst Count: 1
?? Pellets Per Shot: 1

Magazine:
?? Magazine Size: 15
?? Max Ammo: 90
?? Reload Time: 1.5

Damage Data ? Expand:
?? Base Damage: 35
?? Headshot Multiplier: 2.0
?? Limb Multiplier: 0.9
?? Optimal Range: 2000
?? Max Range: 5000

Ballistics Data ? Expand:
?? Muzzle Velocity: 30000
?? Bullet Drop: 0.0 (hitscan)
?? Can Penetrate: FALSE
?? Can Ricochet: FALSE

Accuracy:
?? Hipfire Spread: 2.0
?? ADS Spread: 0.5
?? Movement Spread Multiplier: 1.5

ADS:
?? ADS Time: 0.3
?? ADS Zoom: 1.5
?? ADS Movement Speed: 0.7
```

---

## ? **Step 3: Create Unlock Database (5 min)**

```
Content Browser ? Right Click
? Miscellaneous ? Data Asset
? Class: FRUnlockDatabase
? Name: "DA_UnlockDatabase"
```

### **Configure:**

```
Open DA_UnlockDatabase

Settings:
?? Default Starting Pistol ID: Pistol_Starter
?
?? All Unlockable Items ? Add Element:
   ?? Item ID: Pistol_Starter
   ?? Item Name: "Starter Pistol"
   ?? Item Type: Weapon
   ?? Compatible Slots: [Pistol]
   ?? Item Asset: DA_Pistol_Starter
   ?? Unlock Method: LevelUp
   ?? Required Level: 1
   ?? Rarity: 1
```

### **Link to Game Instance:**

```
Open BP_FRGameInstance
Settings:
?? Unlock Database: DA_UnlockDatabase
```

---

## ? **Step 4: Create Test Map (15 min)**

### **A. New Level:**

```
File ? New Level ? Empty Level
Save As: Content/Maps/TestMap
```

### **B. Add Ground:**

```
Place Actors ? Basic ? Plane
?? Scale: (200, 200, 1)
?? Location: (0, 0, 0)
?? Enable collision
```

### **C. Add Lighting:**

```
Place Actors ? Lights ? Directional Light
?? Rotation: (-45, 0, 0)
?? Intensity: 3.0

Place Actors ? Lights ? Sky Light
?? Intensity: 1.0

Place Actors ? Visual Effects ? Sky Atmosphere
```

### **D. Add Player Starts:**

```
Place Actors ? Basic ? Player Start
Duplicate 4 times (Ctrl+W)
Spread them around (500 units apart)
```

### **E. Add Post Process Volume:**

```
Place Actors ? Visual ? Post Process Volume
?? Scale to cover map
?? Infinite Extent: TRUE
```

---

## ? **Step 5: Create Game Mode (10 min)**

```
Content Browser ? Blueprint Class
? Parent: AFRGameMode
? Name: "BP_FRGameMode"
```

### **Configure:**

```
Open BP_FRGameMode

Class Defaults:
?? Default Pawn Class: (leave as AFRCharacter)
?? Player Controller: AFRPlayerController
?? Game State: AFRGameState
?? Player State: AFRPlayerState
```

### **Set as Map Default:**

```
Window ? World Settings
? Game Mode Override: BP_FRGameMode
```

---

## ? **Step 6: Create Minimal HUD (20 min)**

### **A. Create Widget:**

```
Content Browser ? User Interface ? Widget Blueprint
? Parent: FRMainHUDWidget
? Name: "WBP_MainHUD"
```

### **B. Add Health Bar:**

```
Designer:

1. Add Canvas Panel (root)

2. Add Progress Bar:
   ?? Anchors: Bottom-Right
   ?? Position: (-220, -100)
   ?? Size: (200, 30)
   ?? Fill Type: Left to Right
   ?? Fill Color: Green
   ?? Name: "HealthBar"

3. Add Text above health bar:
   ?? Text: "HEALTH"
   ?? Size: 12
   ?? Color: White
```

### **C. Add Ammo Counter:**

```
4. Add Text Block:
   ?? Anchors: Bottom-Right
   ?? Position: (-220, -60)
   ?? Text: "15 / 90"
   ?? Font Size: 24
   ?? Name: "AmmoText"
```

### **D. Add Crosshair:**

```
5. Add Image (center of screen):
   ?? Anchors: Center
   ?? Position: (0, 0)
   ?? Size: (32, 32)
   ?? Alignment: 0.5, 0.5
   ?? Brush: Simple crosshair texture
```

### **E. Graph - Bind Events:**

```
Event Graph:

Event OnHealthChanged (HealthPercent):
  ? Set HealthBar Percent = HealthPercent
  ? If HealthPercent < 0.3:
       Set Fill Color = Red
     Else:
       Set Fill Color = Green

Event OnAmmoChanged (Current, Max, Reserve):
  ? Format String: "{0} / {1}"
  ? Set AmmoText = Formatted String
```

### **F. Set in Game Mode:**

```
Open BP_FRGameMode
Settings:
?? HUD Class: WBP_MainHUD
```

---

## ? **Step 7: Basic Input Setup (15 min)**

### **A. Create Input Actions:**

```
Edit ? Project Settings ? Input

Enhanced Input:

1. Input Mapping Context: IMC_Default
   
2. Input Actions:
   ?? IA_Move (Vector2D)
   ?? IA_Look (Vector2D)
   ?? IA_Jump (Button)
   ?? IA_Fire (Button)
   ?? IA_Sprint (Button)
   ?? IA_Reload (Button)

3. Map Keys:
   IA_Move:
   ?? W: (0, 1)
   ?? S: (0, -1)
   ?? A: (-1, 0)
   ?? D: (1, 0)
   
   IA_Look:
   ?? Mouse XY 2D-Axis
   
   IA_Jump:
   ?? Space Bar
   
   IA_Fire:
   ?? Left Mouse Button
   
   IA_Sprint:
   ?? Left Shift
   
   IA_Reload:
   ?? R
```

### **B. Create Character Blueprint:**

```
Content Browser ? Blueprint Class
? Parent: AFRCharacter
? Name: "BP_FRCharacter"
```

### **C. Setup Input:**

```
Open BP_FRCharacter

Event Graph:

Event BeginPlay:
  ? Get Player Controller
  ? Get Enhanced Input Component
  ? Bind Input Actions

IA_Move:
  ? Add Movement Input (Forward/Right)

IA_Look:
  ? Add Controller Pitch/Yaw Input

IA_Jump:
  ? Jump()

IA_Sprint (Started):
  ? Get Character Movement
  ? Set Max Walk Speed = 600

IA_Sprint (Completed):
  ? Set Max Walk Speed = 400
```

### **D. Set as Default Pawn:**

```
Open BP_FRGameMode
Settings:
?? Default Pawn Class: BP_FRCharacter
```

---

## ? **Step 8: Simple Weapon System (20 min)**

For now, we'll create a basic Blueprint weapon system:

### **A. Create Weapon Blueprint:**

```
Content Browser ? Blueprint ? Actor
? Name: "BP_WeaponBase"
```

### **B. Add Components:**

```
Add Components:
?? Static Mesh (cube for now)
?? Audio Component
?? Arrow Component (muzzle socket)
```

### **C. Fire Function:**

```
Event Graph:

Custom Event: Fire

1. Check Current Ammo > 0
   
2. Line Trace from Camera:
   ?? Start: Camera Location
   ?? End: Camera Forward * 10000
   ?? Channel: Visibility
   
3. If Hit Actor:
   ?? Apply Damage (35)
   ?? Spawn Impact Particle
   ?? Play Impact Sound
   
4. Spawn Muzzle Flash at Arrow Location

5. Play Fire Sound

6. Decrease Current Ammo

7. Apply Camera Shake (recoil)
```

### **D. Reload Function:**

```
Custom Event: Reload

1. Check Reserve Ammo > 0

2. Delay 1.5 seconds

3. Calculate Ammo Needed = MagSize - CurrentAmmo

4. If Reserve >= AmmoNeeded:
   ?? Current = MagSize
   ?? Reserve -= AmmoNeeded
   Else:
   ?? Current += Reserve
   ?? Reserve = 0
```

### **E. Add to Character:**

```
Open BP_FRCharacter

Variables:
?? Current Weapon (BP_WeaponBase reference)
?? Current Ammo (int)
?? Reserve Ammo (int)

Event BeginPlay:
  ? Spawn BP_WeaponBase
  ? Attach to Socket (RightHandSocket)
  ? Set Current Weapon

IA_Fire:
  ? Current Weapon -> Fire()

IA_Reload:
  ? Current Weapon -> Reload()
```

---

## ? **Step 9: Configure Spawn System (10 min)**

### **In BP_FRGameMode:**

```
Event Graph:

Event PostLogin (Player Controller):
  1. Get World Subsystem (FRSpawnSystem)
  
  2. Get Game Instance -> GetLoadoutSubsystem()
  
  3. Get Active Loadout
  
  4. Call SpawnPlayerWithLoadout(Controller, Loadout)
```

---

## ? **Step 10: Test Play (5 min)**

### **Run the Game:**

```
1. Open TestMap

2. Click Play ? New Editor Window (PIE)
   Settings:
   ?? Number of Players: 2
   ?? Run Dedicated Server: FALSE

3. Test Controls:
   ?? WASD to move ?
   ?? Mouse to look ?
   ?? Space to jump ?
   ?? Shift to sprint ?
   ?? LMB to fire ?
   ?? R to reload ?

4. Verify HUD:
   ?? Health bar visible ?
   ?? Ammo counter updates ?
   ?? Crosshair shows ?
```

---

## ? **YOU'RE NOW PLAYABLE!**

**What Works:**
- ? Can move around
- ? Can shoot starter pistol
- ? Can reload
- ? HUD shows health/ammo
- ? Multiple players can join
- ? Basic combat functional

---

## ?? **Next Steps (Optional)**

### **To Add More Weapons (30 min each):**

1. Duplicate `DA_Pistol_Starter`
2. Change weapon stats
3. Add to Unlock Database
4. Test

### **To Add Loot (15 min):**

1. Place `AFRLootContainer` actors in map
2. Configure rarity
3. Test pickup

### **To Add Extraction (10 min):**

1. Place `AFRExtractionZone` actor
2. Configure extraction time
3. Test extraction flow

### **To Improve HUD (1 hour):**

1. Add player count
2. Add match timer
3. Add weapon slots (1-8)
4. Style everything

---

## ?? **Congratulations!**

**You now have a playable FPS!**

From here, you can:
- Add more weapons
- Create better maps
- Add more gameplay mechanics
- Polish UI/UX
- Add more content

**The systems are all there - now it's just content creation!**

---

**Total Time:** ~2 hours  
**Result:** Playable extraction shooter with solid foundation!
