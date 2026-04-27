# Updated: 8-Slot Weapon System ?

## Slot Configuration

Your loadout system now has **8 specific weapon/equipment slots**:

### Weapon Slots (5)
1. **Primary** - Main weapon (AR, SMG, LMG, Sniper, DMR)
2. **Secondary** - Secondary weapon (any weapon type - flexibility)
3. **Pistol** - Starting pistol (LOCKED - always equipped, never changes)
4. **Melee** - Melee weapon (knife, axe, etc.)
5. **Lethal** - Lethal equipment (frag grenades, C4, mines, etc.)

### Equipment Slots (3)
6. **Tactical** - Tactical equipment (smoke, flash, stun, heartbeat sensor, etc.)
7. **Gear 1** - Healing/utility (medkit, bandages, armor plates, etc.)
8. **Gear 2** - Additional healing/utility

---

## How It Works

### Starting Loadout
```
Primary:    [EMPTY - Must Loot]
Secondary:  [EMPTY - Must Loot]
Pistol:     [Starter Pistol] ? LOCKED (Always Available)
Melee:      [EMPTY - Must Loot]
Tactical:   [EMPTY - Must Loot]
Lethal:     [EMPTY - Must Loot]
Gear 1:     [EMPTY - Must Loot]
Gear 2:     [EMPTY - Must Loot]
```

### Fully Equipped Loadout Example
```
Primary:    [AR-15] (Unlocked)
Secondary:  [MP5] (Extracted)
Pistol:     [Starter Pistol] ? LOCKED
Melee:      [Combat Knife] (Unlocked)
Tactical:   [Smoke Grenade] (Extracted)
Lethal:     [Frag Grenade] (Unlocked)
Gear 1:     [Medkit] (Extracted)
Gear 2:     [Armor Plate] (Unlocked)
```

---

## Slot System Features

### 1. Slot-Specific Compatibility
Items can only be equipped in compatible slots:

```cpp
// Weapon compatible with Primary and Secondary slots
FFRUnlockableItem AR15;
AR15.CompatibleSlots = { Primary, Secondary };

// Grenade only compatible with Lethal slot
FFRUnlockableItem FragGrenade;
FragGrenade.CompatibleSlots = { Lethal };

// Healing item compatible with both Gear slots
FFRUnlockableItem Medkit;
Medkit.CompatibleSlots = { Gear1, Gear2 };
```

### 2. Pistol Slot Special Rules
- **Always Locked**: Cannot be changed/cleared
- **Always Available**: Never lost, even on death
- **Starting Item**: Equipped with starter pistol by default
- **Fallback Weapon**: When all other weapons run out of ammo

### 3. Slot Usage in Match
```
Match Start:
- Spawn with ONLY starter pistol
- All other slots empty
- Must loot to fill slots

During Match:
- Loot weapons/equipment
- Temporarily fill slots
- Items only in match inventory

On Death:
- Drop ALL looted items (Primary through Gear2)
- Keep starter pistol
- Restart with empty slots + pistol

On Extraction:
- Keep all looted items as "extracted"
- Can use extracted items in future matches
- One-time use (consumed when used)
```

---

## API Usage

### Creating & Managing Loadouts

```cpp
UFRLoadoutSubsystem* LoadoutSystem = GetGameInstance()->GetSubsystem<UFRLoadoutSubsystem>();

// Create new loadout
int32 LoadoutIndex = LoadoutSystem->CreateLoadout(FName("Assault Build"));

// Equip items to specific slots
LoadoutSystem->EquipItemToSlot(LoadoutIndex, EFRWeaponSlotType::Primary, FName("AR_M4"));
LoadoutSystem->EquipItemToSlot(LoadoutIndex, EFRWeaponSlotType::Secondary, FName("SMG_MP5"));
LoadoutSystem->EquipItemToSlot(LoadoutIndex, EFRWeaponSlotType::Melee, FName("Knife_Combat"));
LoadoutSystem->EquipItemToSlot(LoadoutIndex, EFRWeaponSlotType::Tactical, FName("Smoke_Grenade"));
LoadoutSystem->EquipItemToSlot(LoadoutIndex, EFRWeaponSlotType::Lethal, FName("Frag_Grenade"));
LoadoutSystem->EquipItemToSlot(LoadoutIndex, EFRWeaponSlotType::Gear1, FName("Medkit_Large"));
LoadoutSystem->EquipItemToSlot(LoadoutIndex, EFRWeaponSlotType::Gear2, FName("Armor_Plate"));

// Cannot modify pistol slot (will fail)
bool bResult = LoadoutSystem->EquipItemToSlot(LoadoutIndex, EFRWeaponSlotType::Pistol, FName("SomePistol"));
// bResult = false, logs warning

// Clear a slot
LoadoutSystem->ClearSlot(LoadoutIndex, EFRWeaponSlotType::Primary); // OK
LoadoutSystem->ClearSlot(LoadoutIndex, EFRWeaponSlotType::Pistol);  // FAILS - pistol locked

// Set as active
LoadoutSystem->SetActiveLoadout(LoadoutIndex);
```

### Getting Available Items for Slot

```cpp
// Get all items that can go in Primary slot and are available
TArray<FFRUnlockableItem> PrimaryWeapons = LoadoutSystem->GetAvailableItemsForSlot(EFRWeaponSlotType::Primary);

// Get all available tactical equipment
TArray<FFRUnlockableItem> TacticalItems = LoadoutSystem->GetAvailableItemsForSlot(EFRWeaponSlotType::Tactical);

// Get healing items
TArray<FFRUnlockableItem> HealingItems = LoadoutSystem->GetAvailableItemsForSlot(EFRWeaponSlotType::Gear1);
```

### Checking Loadout

```cpp
FFRPlayerLoadout ActiveLoadout = LoadoutSystem->GetActiveLoadout();

// Get specific slot
const FFRLoadoutSlot* PrimarySlot = ActiveLoadout.GetSlot(EFRWeaponSlotType::Primary);
if (PrimarySlot && !PrimarySlot->EquippedItemID.IsNone())
{
    // Has primary weapon equipped
    FName WeaponID = PrimarySlot->EquippedItemID;
    TArray<FName> Attachments = PrimarySlot->EquippedAttachments;
}

// Check pistol slot (always has starting pistol)
const FFRLoadoutSlot* PistolSlot = ActiveLoadout.GetSlot(EFRWeaponSlotType::Pistol);
check(PistolSlot->bIsLockedSlot == true);
check(PistolSlot->bIsStartingItem == true);
check(!PistolSlot->EquippedItemID.IsNone());
```

---

## Item Definition Examples

### Primary Weapon (AR)
```cpp
FFRUnlockableItem AR_M4;
AR_M4.ItemID = FName("AR_M4");
AR_M4.ItemName = FText::FromString("M4A1 Assault Rifle");
AR_M4.ItemType = EFRUnlockType::Weapon;
AR_M4.CompatibleSlots = { EFRWeaponSlotType::Primary, EFRWeaponSlotType::Secondary };
AR_M4.Rarity = 3; // Rare
AR_M4.UnlockRequirement.UnlockMethod = EFRUnlockMethod::LevelUp;
AR_M4.UnlockRequirement.RequiredLevel = 5;
```

### Melee Weapon
```cpp
FFRUnlockableItem CombatKnife;
CombatKnife.ItemID = FName("Knife_Combat");
CombatKnife.ItemName = FText::FromString("Combat Knife");
CombatKnife.ItemType = EFRUnlockType::Melee;
CombatKnife.CompatibleSlots = { EFRWeaponSlotType::Melee };
CombatKnife.Rarity = 1; // Common
CombatKnife.UnlockRequirement.UnlockMethod = EFRUnlockMethod::LevelUp;
CombatKnife.UnlockRequirement.RequiredLevel = 1;
```

### Tactical Equipment
```cpp
FFRUnlockableItem SmokeGrenade;
SmokeGrenade.ItemID = FName("Smoke_Grenade");
SmokeGrenade.ItemName = FText::FromString("Smoke Grenade");
SmokeGrenade.ItemType = EFRUnlockType::Tactical;
SmokeGrenade.CompatibleSlots = { EFRWeaponSlotType::Tactical };
SmokeGrenade.Rarity = 2; // Uncommon
SmokeGrenade.UnlockRequirement.UnlockMethod = EFRUnlockMethod::ExtractionReward;
```

### Lethal Equipment
```cpp
FFRUnlockableItem FragGrenade;
FragGrenade.ItemID = FName("Frag_Grenade");
FragGrenade.ItemName = FText::FromString("Frag Grenade");
FragGrenade.ItemType = EFRUnlockType::Lethal;
FragGrenade.CompatibleSlots = { EFRWeaponSlotType::Lethal };
FragGrenade.Rarity = 2; // Uncommon
FragGrenade.UnlockRequirement.UnlockMethod = EFRUnlockMethod::LevelUp;
FragGrenade.UnlockRequirement.RequiredLevel = 3;
```

### Healing Item (Multiple Slots)
```cpp
FFRUnlockableItem Medkit;
Medkit.ItemID = FName("Medkit_Large");
Medkit.ItemName = FText::FromString("Large Medkit");
Medkit.ItemType = EFRUnlockType::Consumable;
Medkit.CompatibleSlots = { EFRWeaponSlotType::Gear1, EFRWeaponSlotType::Gear2 }; // Can go in either gear slot
Medkit.Rarity = 3; // Rare
Medkit.UnlockRequirement.UnlockMethod = EFRUnlockMethod::Purchase;
Medkit.UnlockRequirement.PurchaseCost = 500;
```

---

## Gameplay Loop with 8 Slots

### Pre-Match (Loadout Screen)
```
1. Player selects loadout
2. System checks each slot:
   - Primary: Equipped if unlocked/extracted
   - Secondary: Equipped if unlocked/extracted
   - Pistol: ALWAYS equipped (starting pistol)
   - Melee: Equipped if unlocked/extracted
   - Tactical: Equipped if unlocked/extracted
   - Lethal: Equipped if unlocked/extracted
   - Gear1: Equipped if unlocked/extracted
   - Gear2: Equipped if unlocked/extracted
3. Only pistol spawns with player
```

### In-Match
```
1. Spawn with starter pistol only
2. Loot containers for items
3. Pick up items that fit in any slot
4. Use items during match
5. Extract or die:
   - Extract: Keep items
   - Die: Drop all items (except pistol)
```

### Post-Match
```
If Extracted:
  - Items moved to "Extracted Items"
  - Can be used in next match
  - One-time use (consumed when equipped)
  - Can unlock permanently with XP/purchase

If Died:
  - All items lost
  - Keep XP/currency earned
  - Starting pistol still available
```

---

## Balance Considerations

### Slot Limitations
- **Primary/Secondary**: Usually weapons only
- **Pistol**: Locked starter (balance)
- **Melee**: Close-range options
- **Tactical**: Utility, not damage
- **Lethal**: Damage dealing throwables
- **Gear 1 & 2**: Healing/utility only

### Extracted Item Economy
- **One-time use**: Creates scarcity
- **Risk/Reward**: Must extract to keep
- **Progression path**: Extract ? Unlock permanently

### Starting Pistol Philosophy
- **Always available**: Never locked out of combat
- **Fair start**: Everyone has same weapon
- **Skill-based**: Can win with just pistol
- **Encourages looting**: Pistol is weak, need better gear

---

## Integration with Existing Systems

### Works With:
? **Loot System** - Looted items fill slots temporarily  
? **Extraction** - Extracted items available for slots  
? **Progression** - Unlocked items permanently fill slots  
? **Match Inventory** - Tracks what's in slots during match  
? **Save System** - Loadouts persist between sessions  

### Next Steps:
- [ ] Create actual weapon/item data assets
- [ ] Implement slot UI in loadout screen
- [ ] Hook up spawn system to equip items
- [ ] Create item pickup/equip logic
- [ ] Add slot hotkeys (1-8 for switching)

---

**Status:** ? COMPLETE  
**Build:** ? SUCCESSFUL  

Your loadout system now has the exact 8-slot structure you wanted!
