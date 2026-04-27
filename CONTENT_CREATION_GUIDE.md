# ?? CONTENT CREATION GUIDE - Making Frontline Playable

## **Goal: Transform Systems into Playable Game**

Current Status: **55% Complete (Systems Done)**  
Target: **75% Complete (Playable Alpha)**  
Time Estimate: **10-15 hours**

---

## ?? **Phase 1: Essential Data Assets (2-3 hours)**

### **1.1 Weapon Data Assets** ??

Create these in Unreal Editor:

#### **A. Starter Pistol (Default Loadout)**
**Path:** `Content/Data/Weapons/DA_Pistol_Starter`

```
Create ? Miscellaneous ? Data Asset ? FREnhancedWeaponData

Settings:
?? Info
?  ?? Weapon ID: "Pistol_Starter"
?  ?? Weapon Name: "Starter Pistol"
?  ?? Weapon Type: Pistol
?  ?? Ammo Type: LightAmmo
?
?? Firing
?  ?? Fire Mode: SemiAuto
?  ?? Fire Rate: 0.15 (400 RPM)
?  ?? Burst Count: 1
?  ?? Pellets Per Shot: 1
?
?? Magazine
?  ?? Magazine Size: 15
?  ?? Max Ammo: 90
?  ?? Reload Time: 1.5s
?
?? Damage Data
?  ?? Base Damage: 35
?  ?? Headshot Multiplier: 2.0
?  ?? Limb Multiplier: 0.9
?  ?? Optimal Range: 2000cm
?  ?? Max Range: 5000cm
?
?? Ballistics Data
?  ?? Muzzle Velocity: 30000
?  ?? Bullet Drop: 1.0
?  ?? Drag Coefficient: 0.1
?  ?? Can Penetrate: false
?  ?? Can Ricochet: false
?
?? Recoil Pattern
?  ?? Vertical: [1.0, 1.2, 1.5]
?  ?? Horizontal: [0.0, -0.3, 0.3]
?  ?? Recovery Time: 0.2s
?  ?? ADS Multiplier: 0.7
?
?? Accuracy
   ?? Hipfire Spread: 2.0
   ?? ADS Spread: 0.5
   ?? Movement Multiplier: 1.5
```

#### **B. Assault Rifle (Lootable)**
**Path:** `Content/Data/Weapons/DA_AR_M4`

```
Settings:
?? Weapon ID: "AR_M4"
?? Weapon Name: "M4 Assault Rifle"
?? Fire Mode: FullAuto
?? Fire Rate: 0.08 (750 RPM)
?? Magazine Size: 30
?? Base Damage: 32
?? Optimal Range: 5000cm
?? Muzzle Velocity: 90000
```

#### **C. SMG (Lootable)**
**Path:** `Content/Data/Weapons/DA_SMG_MP5`

```
Settings:
?? Weapon ID: "SMG_MP5"
?? Weapon Name: "MP5 SMG"
?? Fire Mode: FullAuto
?? Fire Rate: 0.067 (900 RPM)
?? Magazine Size: 30
?? Base Damage: 25
?? Optimal Range: 3000cm
?? High horizontal recoil
```

#### **D. Shotgun (Lootable)**
**Path:** `Content/Data/Weapons/DA_Shotgun_Pump`

```
Settings:
?? Weapon ID: "Shotgun_Pump"
?? Fire Mode: SemiAuto
?? Fire Rate: 1.0 (60 RPM)
?? Magazine Size: 8
?? Pellets Per Shot: 8
?? Base Damage: 15 (per pellet)
?? Optimal Range: 1500cm
?? Wide spread
```

#### **E. Sniper Rifle (Lootable)**
**Path:** `Content/Data/Weapons/DA_Sniper_AWM`

```
Settings:
?? Weapon ID: "Sniper_AWM"
?? Fire Mode: Bolt
?? Fire Rate: 1.5 (40 RPM)
?? Magazine Size: 5
?? Base Damage: 120
?? Headshot Multiplier: 4.0
?? Optimal Range: 10000cm
?? Can Penetrate: true
?? Max Penetration: 100cm
```

---

### **1.2 Equipment Items** ??

#### **A. Medkit**
**Path:** `Content/Data/Equipment/DA_Medkit`

```
Create ? Data Asset ? FRUnlockableItem

Settings:
?? Item ID: "Medkit_Large"
?? Item Name: "Large Medkit"
?? Item Type: Consumable
?? Compatible Slots: [Gear1, Gear2]
?? Rarity: 3 (Rare)
?? Unlock Method: ExtractionReward
```

#### **B. Armor Plates**
**Path:** `Content/Data/Equipment/DA_ArmorPlate`

```
Settings:
?? Item ID: "Armor_Plate"
?? Item Name: "Armor Plate"
?? Item Type: Consumable
?? Compatible Slots: [Gear1, Gear2]
?? Rarity: 2 (Uncommon)
```

#### **C. Frag Grenade**
**Path:** `Content/Data/Equipment/DA_FragGrenade`

```
Settings:
?? Item ID: "Frag_Grenade"
?? Item Name: "Frag Grenade"
?? Item Type: Lethal
?? Compatible Slots: [Lethal]
?? Unlock Method: LevelUp (Level 3)
```

#### **D. Smoke Grenade**
**Path:** `Content/Data/Equipment/DA_SmokeGrenade`

```
Settings:
?? Item ID: "Smoke_Grenade"
?? Item Name: "Smoke Grenade"
?? Item Type: Tactical
?? Compatible Slots: [Tactical]
?? Unlock Method: LevelUp (Level 2)
```

#### **E. Combat Knife**
**Path:** `Content/Data/Equipment/DA_CombatKnife`

```
Settings:
?? Item ID: "Knife_Combat"
?? Item Name: "Combat Knife"
?? Item Type: Melee
?? Compatible Slots: [Melee]
?? Unlock Method: LevelUp (Level 1)
```

---

### **1.3 Unlock Database** ??

**Path:** `Content/Data/DA_UnlockDatabase`

```
Create ? Data Asset ? FRUnlockDatabase

Settings:
?? Default Starting Pistol ID: "Pistol_Starter"
?? All Unlockable Items:
?  ?? Pistol_Starter (Always unlocked)
?  ?? AR_M4 (Level 5)
?  ?? SMG_MP5 (Level 3)
?  ?? Shotgun_Pump (Level 7)
?  ?? Sniper_AWM (Level 10)
?  ?? Knife_Combat (Level 1)
?  ?? Frag_Grenade (Level 3)
?  ?? Smoke_Grenade (Level 2)
?  ?? Medkit_Large (Extraction)
?  ?? Armor_Plate (Extraction)
?
?? Default Loadout:
   ?? Loadout Name: "Default"
   ?? Starting Pistol: "Pistol_Starter"
   ?? All other slots: Empty
```

---

## ?? **Phase 2: Simple Test Map (2-3 hours)**

### **2.1 Create Basic Arena Map**

**Path:** `Content/Maps/TestArena`

#### **Map Layout:**
```
Size: 2000m x 2000m

Required Elements:
?? Ground (Landscape or BSP)
?? 10x Player Start Actors
?? 5x Loot Container Spawn Points
?? 1x Extraction Zone
?? Basic lighting
?? Collision volumes
```

#### **Setup Steps:**

**A. Create New Level**
```
File ? New Level ? Empty Level
Save As: Content/Maps/TestArena
```

**B. Add Ground**
```
Place Actors ? Geometry ? Plane
Scale: 200, 200, 1
Material: M_Ground (create simple gray material)
Enable Collision
```

**C. Add Lighting**
```
Place Actors ? Directional Light
Rotation: -45°, 0°, 0°
Intensity: 3.0

Place Actors ? Sky Light
Intensity: 1.0
```

**D. Add Player Starts**
```
Place Actors ? Basic ? Player Start
Duplicate 10 times
Spread around map (minimum 50m apart)
```

**E. Add Loot Containers**
```
Place Actors ? All Classes ? FRLootContainer
Count: 5
Spread around map
Set Rarity to 3 (Rare) for guaranteed weapons
```

**F. Add Extraction Zone**
```
Place Actors ? All Classes ? FRExtractionZone
Location: Center of map
Scale: 5, 5, 3 (50m radius)
Extraction Time: 10s
```

**G. Add Nav Mesh**
```
Place Actors ? Navigation ? Nav Mesh Bounds Volume
Cover entire playable area
```

---

### **2.2 Configure Game Mode**

**Path:** `Content/Blueprints/BP_FRGameMode`

```
Create ? Blueprint Class ? AFRGameMode

Settings:
?? Default Pawn Class: BP_FRCharacter
?? Player Controller Class: AFRPlayerController
?? Game State Class: AFRGameState
?? Player State Class: AFRPlayerState
?? HUD Class: BP_MainHUD (we'll create this)
```

Set as default for TestArena:
```
World Settings ? Game Mode Override ? BP_FRGameMode
```

---

## ?? **Phase 3: Basic UI Implementation (3-4 hours)**

### **3.1 Main HUD Widget**

**Path:** `Content/UI/WBP_MainHUD`

```
Create ? User Interface ? Widget Blueprint
Parent Class: FRMainHUDWidget

Canvas Layout:
???????????????????????????????????????
? [Player Count: 45/100]   [03:45]   ? Top Bar
?                                     ?
?                                     ?
?                                     ?
?                            Health:  ?
?                            [?????]  ? Bottom Right
?                            Ammo:    ?
?                            [25/30]  ?
?                                     ?
? [1][2][3][4][5][6][7][8]           ? Bottom Center (8 Slots)
???????????????????????????????????????
```

#### **Widgets to Add:**

**A. Health Bar**
```
Progress Bar
?? Fill Color: Green ? Red (based on health)
?? Size: 200x30
?? Bind Percent to: HealthPercent variable
```

**B. Ammo Display**
```
Text Block
?? Text: "25 / 30"
?? Font Size: 24
?? Bind to: CurrentAmmo/MaxAmmo
```

**C. Player Count**
```
Text Block
?? Text: "Players: 45/100"
?? Bind to: PlayersAlive/TotalPlayers
```

**D. Match Timer**
```
Text Block
?? Text: "03:45"
?? Font Size: 32
?? Bind to: FormatTime(TimeRemaining)
```

**E. Weapon Slots (1-8)**
```
For each slot:
?? Border (outline when empty)
?? Image (weapon icon)
?? Text (slot number)
?? Highlight when selected
```

#### **Blueprint Events to Implement:**

```cpp
Event OnHealthChanged(float HealthPercent)
  ? Update health bar fill percent
  ? Change color based on health

Event OnAmmoChanged(int Current, int Max, int Reserve)
  ? Update ammo text display

Event OnPlayerCountUpdated(int Alive, int Total)
  ? Update player count text

Event OnMatchTimerUpdated(string TimeText)
  ? Update timer display

Event OnWeaponSlotChanged(SlotType, WeaponName, bIsActive)
  ? Update slot icon
  ? Highlight if active
```

---

### **3.2 Inventory Widget**

**Path:** `Content/UI/WBP_Inventory`

```
Parent Class: FRInventoryWidget

Layout: 2x4 Grid
?????????????
?  1  ?  2  ?  (Primary, Secondary)
?????????????
?  3  ?  4  ?  (Pistol-Locked, Melee)
?????????????
?  5  ?  6  ?  (Tactical, Lethal)
?????????????
?  7  ?  8  ?  (Gear1, Gear2)
?????????????

Each Slot Shows:
?? Icon/image
?? Item name
?? Quantity (if stacks)
?? Lock icon (for pistol)
?? Empty state
```

#### **Binding:**
```
Event OnSlotUpdated(SlotType, SlotData)
  ? Find corresponding widget
  ? Update icon/name/quantity
  ? Show/hide lock icon
```

---

### **3.3 Simple Crosshair**

**Path:** `Content/UI/WBP_Crosshair`

```
Canvas Panel
?? Image (crosshair)
   ?? Size: 32x32
   ?? Center of screen
   ?? Color: White with opacity

Bind Color:
  ? Red when aiming at enemy
  ? White normally
```

---

## ?? **Phase 4: Character Blueprint Setup (2-3 hours)**

### **4.1 Player Character Blueprint**

**Path:** `Content/Blueprints/BP_FRCharacter`

```
Create ? Blueprint Class ? AFRCharacter

Components to Verify:
? Skeletal Mesh
? Camera Component
? Spring Arm Component
? FRAdvancedMovementComponent
? FRServerValidationComponent
? FRFootstepComponent
? FRBallisticsComponent
```

#### **Input Setup:**

**A. Movement**
```
Input Action: IA_Move
Mapping: WASD

Event:
  Get Input Vector
  ? Add Movement Input
```

**B. Look**
```
Input Action: IA_Look
Mapping: Mouse

Event:
  Get Input Vector
  ? Add Controller Pitch/Yaw
```

**C. Jump**
```
Input Action: IA_Jump
Mapping: Space

Event:
  ? Jump()
```

**D. Crouch**
```
Input Action: IA_Crouch
Mapping: C (toggle)

Event:
  ? Crouch() / UnCrouch()
```

**E. Sprint**
```
Input Action: IA_Sprint
Mapping: Left Shift (hold)

Event Started:
  ? Set Max Walk Speed = 600

Event Completed:
  ? Set Max Walk Speed = 400
```

**F. Slide**
```
Input Action: IA_Slide
Mapping: Ctrl (while sprinting)

Event:
  ? AdvancedMovement->TrySlide()
```

**G. Weapon Slots (1-8)**
```
Input Actions: IA_Slot1 through IA_Slot8
Mappings: 1, 2, 3, 4, 5, 6, 7, 8

Event:
  ? SwitchToWeaponSlot(SlotType)
```

**H. Reload**
```
Input Action: IA_Reload
Mapping: R

Event:
  ? ReloadCurrentWeapon()
```

**I. Fire**
```
Input Action: IA_Fire
Mapping: Left Mouse (hold for auto)

Event:
  ? FireWeapon()
```

**J. Aim Down Sights**
```
Input Action: IA_ADS
Mapping: Right Mouse (hold)

Event Started:
  ? Enable ADS (zoom camera, reduce spread)

Event Completed:
  ? Disable ADS
```

**K. Inventory**
```
Input Action: IA_Inventory
Mapping: Tab (toggle)

Event:
  ? Toggle Inventory Widget
```

---

### **4.2 Simple Weapon System**

For initial playability, create a basic weapon actor:

**Path:** `Content/Blueprints/BP_Weapon`

```
Create ? Blueprint Class ? Actor

Components:
?? Skeletal Mesh (weapon model)
?? Audio Component (fire sound)
?? Particle System (muzzle flash)

Functions:

Fire():
  1. Check ammo > 0
  2. Line trace from camera
  3. If hit:
     - Apply damage
     - Spawn impact VFX
     - Play impact sound
  4. Spawn muzzle flash
  5. Play fire sound
  6. Decrease ammo
  7. Apply recoil to camera

Reload():
  1. Play reload animation
  2. Wait for animation
  3. Refill ammo from reserve
  4. Play reload sound
```

---

## ?? **Phase 5: Quick Content (1-2 hours)**

### **5.1 Placeholder Assets**

Use Unreal Engine starter content:

**Weapon Meshes:**
```
Use simple cubes/cylinders for now:
?? Pistol: Small cube with handle
?? Rifle: Long cylinder
?? SMG: Short cylinder
?? Shotgun: Thick cylinder
```

**Sounds:**
```
Use Starter Content sounds:
?? Fire: Explosion sound
?? Reload: Metal sound
?? Footsteps: Footstep sounds
?? UI: Click sounds
```

**Materials:**
```
?? Weapon: M_Metal_Brushed
?? Loot Box: M_Metal_Gold
?? Ground: M_Ground_Grass
?? Extraction: M_Tech_Panel
```

---

## ?? **Phase 6: Integration & Testing (1-2 hours)**

### **6.1 Configure Subsystems**

**A. Loadout Subsystem**
```
In GameInstance Blueprint:
Event Init:
  ? Get LoadoutSubsystem
  ? LoadPlayerUnlockData()
  ? Create default loadout if none exists
```

**B. Audio Manager**
```
In GameInstance:
  ? Load audio settings
  ? Set default volumes
```

**C. Match Flow Controller**
```
In GameMode BeginPlay:
  ? Spawn MatchFlowController
  ? Set match settings
  ? Start in Lobby phase
```

**D. Spawn System**
```
In GameMode PostLogin:
  ? Get active loadout
  ? Spawn player with loadout
  ? (Only pistol in extraction mode)
```

---

### **6.2 Test Checklist**

Run in PIE (Play In Editor) with 2+ players:

**Basic Functionality:**
- [ ] Can move (WASD)
- [ ] Can look (Mouse)
- [ ] Can jump (Space)
- [ ] Can sprint (Shift)
- [ ] Can crouch (C)

**Combat:**
- [ ] Can fire weapon (LMB)
- [ ] Can reload (R)
- [ ] Can switch weapons (1-8)
- [ ] Damage registers
- [ ] Ammo decreases

**UI:**
- [ ] HUD shows health
- [ ] HUD shows ammo
- [ ] HUD shows player count
- [ ] HUD shows timer
- [ ] Inventory opens (Tab)
- [ ] 8 slots visible

**Match Flow:**
- [ ] Lobby countdown works
- [ ] Match starts after countdown
- [ ] Player count updates
- [ ] Victory on last player
- [ ] Rewards calculated

**Extraction:**
- [ ] Loot containers spawn items
- [ ] Can pick up items
- [ ] Extraction zone works
- [ ] Progress bar shows
- [ ] Items saved on extraction

---

## ?? **Quick Start Implementation**

### **Option A: Minimum Playable (4 hours)**

Focus on absolute essentials:
1. ? Starter pistol data asset
2. ? Basic HUD (health, ammo only)
3. ? Simple test map
4. ? Basic movement input
5. ? Fire/reload functionality

**Result:** Can run around and shoot

---

### **Option B: Full Alpha (10-15 hours)**

Complete everything above:
1. ? All 5 weapon data assets
2. ? All equipment items
3. ? Complete HUD with 8 slots
4. ? Inventory UI
5. ? Test map with loot/extraction
6. ? Full input setup
7. ? Match flow working

**Result:** Playable extraction shooter

---

## ?? **Priority Order**

If time-constrained, do in this order:

**Critical (Must Have):**
1. Starter pistol data
2. Test map with spawns
3. Basic HUD (health/ammo)
4. Fire weapon functionality
5. Movement input

**Important (Should Have):**
6. AR and SMG data
7. Loot containers
8. Inventory UI
9. Extraction zone
10. Match timer

**Nice to Have:**
11. Shotgun and Sniper
12. Equipment items
13. Full 8-slot UI
14. Advanced movement input
15. Footstep sounds

---

## ?? **Next Steps**

**Which path do you want to take?**

**A. Guided Creation** - I'll walk you through creating each asset step-by-step
**B. Blueprint Templates** - I'll create Blueprint base classes you can extend
**C. Quick Prototypes** - I'll make simple placeholder versions to get playing ASAP

**Just tell me which approach you prefer and we'll start making your game playable!**
