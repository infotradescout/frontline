# ? COMPLETE PLAYABILITY CHECKLIST

## **Transform Your Game from "Systems Work" to "Actually Playable"**

Use this checklist to track your progress making Frontline playable.

---

## ?? **Phase 1: Absolute Minimum (2-3 hours)**

**Goal:** Walk around and shoot something

### **Core Setup**
- [ ] Create `BP_FRGameInstance` from `FRGameInstanceBase`
- [ ] Set as default game instance in Project Settings
- [ ] Configure basic settings (player count, timers)

### **Content Creation**
- [ ] Create `DA_Pistol_Starter` weapon data asset
- [ ] Create `DA_UnlockDatabase` with starter pistol
- [ ] Link unlock database to game instance

### **Map Setup**
- [ ] Create `TestMap` with ground plane
- [ ] Add lighting (directional + sky)
- [ ] Place 4+ Player Start actors
- [ ] Set game mode to `BP_FRGameMode`

### **UI Creation**
- [ ] Create `WBP_MainHUD` from `FRMainHUDWidget`
- [ ] Add health bar
- [ ] Add ammo counter
- [ ] Add crosshair
- [ ] Bind events (OnHealthChanged, OnAmmoChanged)
- [ ] Set as HUD class in game mode

### **Character Setup**
- [ ] Create `BP_FRCharacter` from `AFRCharacter`
- [ ] Setup input mapping context
- [ ] Bind movement (WASD)
- [ ] Bind look (Mouse)
- [ ] Bind jump (Space)
- [ ] Bind sprint (Shift)
- [ ] Set as default pawn in game mode

### **Basic Combat**
- [ ] Create `BP_WeaponBase` actor
- [ ] Implement Fire() function (line trace + damage)
- [ ] Implement Reload() function
- [ ] Bind Fire to LMB
- [ ] Bind Reload to R
- [ ] Spawn weapon on character

### **Test**
- [ ] Play with 2 players in PIE
- [ ] Can move ?
- [ ] Can shoot ?
- [ ] Can see health/ammo ?
- [ ] Combat works ?

**Status:** **MINIMUM VIABLE PRODUCT** ?

---

## ?? **Phase 2: Core Gameplay (4-6 hours)**

**Goal:** Fun to play, basic loop works

### **More Weapons**
- [ ] Create `DA_AR_M4` (assault rifle)
- [ ] Create `DA_SMG_MP5` (SMG)
- [ ] Create `DA_Shotgun_Pump` (shotgun)
- [ ] Add all to unlock database
- [ ] Test each weapon

### **Weapon Switching**
- [ ] Bind keys 1-8 to weapon slots
- [ ] Implement SwitchWeapon() function
- [ ] Show active weapon in HUD
- [ ] Highlight current slot

### **Inventory System**
- [ ] Create `WBP_Inventory` from `FRInventoryWidget`
- [ ] Layout 2x4 grid for 8 slots
- [ ] Show weapon icons/names
- [ ] Show pistol as locked
- [ ] Bind Tab to toggle inventory
- [ ] Test open/close

### **Loot System**
- [ ] Place 5+ `AFRLootContainer` actors
- [ ] Configure rarity (3-5 for good loot)
- [ ] Test opening containers
- [ ] Test picking up weapons
- [ ] Verify items go to correct slots

### **Match Flow**
- [ ] Spawn `FRMatchFlowController` in game mode
- [ ] Configure match settings
- [ ] Add player count to HUD
- [ ] Add match timer to HUD
- [ ] Test full match cycle:
   - [ ] Lobby countdown
   - [ ] Pregame warmup
   - [ ] Main game
   - [ ] Victory screen
   - [ ] Rewards

### **Spawn System**
- [ ] Configure spawn points (10+ for good spread)
- [ ] Test spawning with loadout
- [ ] Verify only pistol spawns (extraction mode)
- [ ] Test weapon pickup during match

### **Test**
- [ ] Full match cycle works ?
- [ ] Can loot weapons ?
- [ ] Can switch weapons ?
- [ ] Inventory shows all items ?
- [ ] Match timer counts down ?
- [ ] Victory conditions trigger ?

**Status:** **CORE LOOP FUNCTIONAL** ?

---

## ?? **Phase 3: Extraction Mechanics (2-3 hours)**

**Goal:** Risk/reward extraction loop

### **Extraction Setup**
- [ ] Place `AFRExtractionZone` actor
- [ ] Configure extraction time (10s)
- [ ] Make visible (collision + visual)

### **HUD Updates**
- [ ] Add extraction progress bar
- [ ] Show "Extracting..." message
- [ ] Show time remaining
- [ ] Bind to OnExtractionProgressChanged

### **Integration**
- [ ] Test entering extraction zone
- [ ] Verify progress bar shows
- [ ] Test interruption (moving away)
- [ ] Test successful extraction
- [ ] Verify items saved to extracted inventory

### **Post-Match**
- [ ] Show items extracted on match end screen
- [ ] Verify extracted items available next match
- [ ] Test consuming extracted items (one-time use)
- [ ] Verify permanent unlocks still work

### **Test**
- [ ] Can extract successfully ?
- [ ] Progress bar accurate ?
- [ ] Items saved ?
- [ ] Can use extracted items next match ?
- [ ] Extracted items consumed when used ?

**Status:** **EXTRACTION LOOP COMPLETE** ?

---

## ?? **Phase 4: Polish & Feel (3-4 hours)**

**Goal:** Feels good to play

### **Audio**
- [ ] Add weapon fire sounds
- [ ] Add reload sounds
- [ ] Add footstep sounds (use Starter Content)
- [ ] Add UI click sounds
- [ ] Configure audio manager volumes
- [ ] Test 3D sound positioning

### **Visual Effects**
- [ ] Add muzzle flash particles
- [ ] Add bullet tracers
- [ ] Add impact effects (sparks, dust)
- [ ] Add hit markers
- [ ] Test all VFX

### **Movement Polish**
- [ ] Add camera bob while walking
- [ ] Add landing camera shake
- [ ] Add recoil camera shake on fire
- [ ] Smooth camera transitions
- [ ] Add crouch/prone animations (or transitions)

### **UI Polish**
- [ ] Style health bar (colors, borders)
- [ ] Style ammo counter (fonts, glow)
- [ ] Add weapon icons to slots
- [ ] Add slot backgrounds
- [ ] Add hover effects
- [ ] Add animations (fade in/out)

### **Feedback**
- [ ] Hit markers on successful hit
- [ ] Different hit marker for headshots
- [ ] Kill confirmation marker
- [ ] Damage numbers (optional)
- [ ] Low health warning (red screen pulse)

### **Test**
- [ ] Game feels responsive ?
- [ ] Audio enhances gameplay ?
- [ ] Visual feedback clear ?
- [ ] UI is polished ?
- [ ] Everything looks/sounds good ?

**Status:** **POLISHED ALPHA** ?

---

## ??? **Phase 5: Better Map (2-3 hours)**

**Goal:** Interesting environment

### **Map Design**
- [ ] Add cover objects (walls, crates, barriers)
- [ ] Add elevation changes (ramps, hills)
- [ ] Create 3-5 distinct areas
- [ ] Add visual landmarks
- [ ] Create chokepoints

### **Environment**
- [ ] Add props/decorations
- [ ] Add ambient sounds
- [ ] Add background music
- [ ] Add fog/atmosphere
- [ ] Polish lighting

### **Strategic Elements**
- [ ] Place loot in strategic locations
- [ ] Create high-risk/high-reward areas
- [ ] Add multiple extraction points (optional)
- [ ] Balance spawn locations
- [ ] Add navigation aids (signs, colors)

### **Test**
- [ ] Map is fun to navigate ?
- [ ] Combat areas work well ?
- [ ] Loot placement feels good ?
- [ ] Extraction zone is strategic ?
- [ ] Environment looks good ?

**Status:** **ENVIRONMENT COMPLETE** ?

---

## ?? **Phase 6: More Content (Variable time)**

**Goal:** Variety and replayability

### **Additional Weapons**
- [ ] Add sniper rifle
- [ ] Add LMG
- [ ] Add DMR
- [ ] Add rocket launcher (optional)
- [ ] Test balance

### **Equipment**
- [ ] Add frag grenades (lethal)
- [ ] Add smoke grenades (tactical)
- [ ] Add medkits (gear)
- [ ] Add armor plates (gear)
- [ ] Add combat knife (melee)

### **Attachments** (Optional)
- [ ] Create attachment data structure
- [ ] Add scopes (zoom)
- [ ] Add suppressors (reduce sound)
- [ ] Add extended mags (more ammo)
- [ ] Add grips (reduce recoil)

### **Progression**
- [ ] Configure unlock levels
- [ ] Test XP calculation
- [ ] Test level-up rewards
- [ ] Test purchase system
- [ ] Balance economy

### **Test**
- [ ] All weapons work ?
- [ ] All equipment functional ?
- [ ] Progression feels rewarding ?
- [ ] Economy balanced ?

**Status:** **CONTENT RICH** ?

---

## ?? **Phase 7: Advanced Features (Optional, 5+ hours)**

**Goal:** AAA polish

### **Advanced Movement**
- [ ] Implement sliding
- [ ] Implement vaulting
- [ ] Implement climbing
- [ ] Implement prone
- [ ] Test all mechanics

### **Advanced UI**
- [ ] Loadout customization screen (pre-match)
- [ ] Settings menu
- [ ] Scoreboard
- [ ] Death screen
- [ ] Victory screen
- [ ] Statistics screen

### **Network Features**
- [ ] Voice chat (if needed)
- [ ] Chat system
- [ ] Ping system
- [ ] Team indicators

### **Test**
- [ ] All features work ?
- [ ] Network stable ?
- [ ] Performance good ?

**Status:** **FEATURE COMPLETE** ?

---

## ?? **Final Verification**

### **Playability Test**

Play 3 full matches and verify:

**Match 1: Basic Gameplay**
- [ ] Match starts correctly
- [ ] Spawn with pistol only
- [ ] Can loot weapons
- [ ] Can switch weapons (1-8)
- [ ] Combat is fun
- [ ] HUD shows everything
- [ ] Victory conditions work
- [ ] Rewards calculated

**Match 2: Extraction Focus**
- [ ] Can find good loot
- [ ] Decide to extract or continue fighting
- [ ] Extraction zone works
- [ ] Progress bar accurate
- [ ] Successfully extract
- [ ] Items saved to profile
- [ ] Can use extracted items next match

**Match 3: Full Features**
- [ ] All weapons available
- [ ] Equipment works
- [ ] Movement feels good
- [ ] Audio enhances experience
- [ ] UI is clear
- [ ] Match flow is smooth
- [ ] Game is fun!

---

## ?? **COMPLETION MILESTONES**

### **25% Playable** (Phase 1 Complete)
- Can move, shoot, basic gameplay
- **Time:** 2-3 hours

### **50% Playable** (Phase 2 Complete)
- Core loop works, multiple weapons, loot
- **Time:** 6-9 hours total

### **75% Playable** (Phases 1-5 Complete)
- Extraction loop, polished, good map
- **Time:** 13-18 hours total

### **100% Playable** (All Phases Complete)
- Feature complete, AAA polish
- **Time:** 20+ hours total

---

## ?? **RECOMMENDED PATH**

**For Quick Testing:**
? Complete Phase 1 only (2-3 hours)

**For Playable Alpha:**
? Complete Phases 1-3 (8-12 hours)

**For Polished Demo:**
? Complete Phases 1-5 (15-20 hours)

**For Feature Complete:**
? Complete All Phases (25+ hours)

---

## ?? **PRO TIPS**

1. **Use Placeholder Assets First**
   - Don't wait for perfect art
   - Cubes and cylinders work fine
   - Focus on gameplay feel

2. **Test Early, Test Often**
   - Play after every major change
   - Get feedback from others
   - Iterate on fun factor

3. **One System at a Time**
   - Complete each phase fully
   - Don't jump ahead
   - Build solid foundations

4. **Leverage Blueprints**
   - C++ systems are done
   - Use Blueprints for content
   - Iterate faster

5. **Document As You Go**
   - Take notes on what works
   - Record bugs to fix
   - Track ideas for later

---

## ?? **CURRENT STATUS TRACKER**

Fill this out as you progress:

```
Phase 1 (Minimum):     [ ] 0% ? [ ] 100%
Phase 2 (Core Loop):   [ ] 0% ? [ ] 100%
Phase 3 (Extraction):  [ ] 0% ? [ ] 100%
Phase 4 (Polish):      [ ] 0% ? [ ] 100%
Phase 5 (Map):         [ ] 0% ? [ ] 100%
Phase 6 (Content):     [ ] 0% ? [ ] 100%
Phase 7 (Advanced):    [ ] 0% ? [ ] 100%

Overall Playability: ____%

Last Updated: _________
Next Goal: ___________
```

---

**Good luck making your game playable! You've got all the systems - now bring it to life! ????**
