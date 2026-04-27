# ?? **BOT WEAPON INTEGRATION GUIDE**

## **? QUICK INTEGRATION:**

Your bots are smart and can aim, but they need to actually FIRE weapons. Here's how to connect them to your weapon system:

---

## **?? WHERE TO ADD WEAPON FIRING:**

In `FRAIBotController.cpp`, find this function:

```cpp
void AFRAIBotController::FireAtTarget(float DeltaTime)
{
	if (!CurrentTarget.IsValid() || !ControlledCharacter)
		return;

	AActor* Target = CurrentTarget.Get();

	// Check if we can see the target
	if (!CanSeeTarget(Target))
	{
		return;
	}

	// Get target location with prediction
	FVector TargetLocation = PredictTargetLocation(Target, 30000.0f);

	// Adjust for accuracy
	AdjustAimWithAccuracy(TargetLocation);

	// Look at target
	FVector Direction = (TargetLocation - ControlledCharacter->GetActorLocation()).GetSafeNormal();
	FRotator TargetRotation = Direction.Rotation();
	SetControlRotation(TargetRotation);

	// ??? ADD YOUR WEAPON FIRING HERE ???
	// Simulate firing (you'll need to implement actual weapon firing)
	// For now, just log
	// FR_LOG_INFO(LogFrontline, "[Bot %s] Firing at target", *GetName());
}
```

---

## **?? OPTION 1: Using Your Weapon Component**

If your character has a weapon component:

```cpp
void AFRAIBotController::FireAtTarget(float DeltaTime)
{
	if (!CurrentTarget.IsValid() || !ControlledCharacter)
		return;

	AActor* Target = CurrentTarget.Get();

	if (!CanSeeTarget(Target))
		return;

	// Aim at target
	FVector TargetLocation = PredictTargetLocation(Target, 30000.0f);
	AdjustAimWithAccuracy(TargetLocation);
	
	FVector Direction = (TargetLocation - ControlledCharacter->GetActorLocation()).GetSafeNormal();
	FRotator TargetRotation = Direction.Rotation();
	SetControlRotation(TargetRotation);

	// ? FIRE WEAPON ?
	// Get weapon component from character
	UYourWeaponComponent* WeaponComp = ControlledCharacter->FindComponentByClass<UYourWeaponComponent>();
	if (WeaponComp)
	{
		WeaponComp->Fire();  // Call your fire function
	}
}
```

---

## **?? OPTION 2: Using Inventory System**

If weapons are in inventory:

```cpp
void AFRAIBotController::FireAtTarget(float DeltaTime)
{
	if (!CurrentTarget.IsValid() || !ControlledCharacter || !InventoryComponent)
		return;

	AActor* Target = CurrentTarget.Get();

	if (!CanSeeTarget(Target))
		return;

	// Aim at target
	FVector TargetLocation = PredictTargetLocation(Target, 30000.0f);
	AdjustAimWithAccuracy(TargetLocation);
	
	FVector Direction = (TargetLocation - ControlledCharacter->GetActorLocation()).GetSafeNormal();
	FRotator TargetRotation = Direction.Rotation();
	SetControlRotation(TargetRotation);

	// ? FIRE WEAPON ?
	// Get equipped weapon from inventory
	AActor* EquippedWeapon = InventoryComponent->GetEquippedWeapon();
	if (EquippedWeapon)
	{
		// Cast to your weapon class
		AYourWeaponClass* Weapon = Cast<AYourWeaponClass>(EquippedWeapon);
		if (Weapon)
		{
			Weapon->Fire();  // Call fire function
		}
	}
}
```

---

## **?? OPTION 3: Using Input System**

If weapons fire via input:

```cpp
void AFRAIBotController::FireAtTarget(float DeltaTime)
{
	if (!CurrentTarget.IsValid() || !ControlledCharacter)
		return;

	AActor* Target = CurrentTarget.Get();

	if (!CanSeeTarget(Target))
		return;

	// Aim at target
	FVector TargetLocation = PredictTargetLocation(Target, 30000.0f);
	AdjustAimWithAccuracy(TargetLocation);
	
	FVector Direction = (TargetLocation - ControlledCharacter->GetActorLocation()).GetSafeNormal();
	FRotator TargetRotation = Direction.Rotation();
	SetControlRotation(TargetRotation);

	// ? FIRE WEAPON VIA INPUT ?
	// Simulate input press
	if (UEnhancedInputComponent* Input = Cast<UEnhancedInputComponent>(ControlledCharacter->InputComponent))
	{
		// Trigger fire action
		Input->TriggerActionValue(YourFireAction);  // Replace with your action
	}

	// Or call character's fire function directly:
	// ControlledCharacter->Fire();
}
```

---

## **?? OPTION 4: Server-Side Firing**

If using replicated weapons:

```cpp
void AFRAIBotController::FireAtTarget(float DeltaTime)
{
	if (!CurrentTarget.IsValid() || !ControlledCharacter)
		return;

	AActor* Target = CurrentTarget.Get();

	if (!CanSeeTarget(Target))
		return;

	// Aim at target
	FVector TargetLocation = PredictTargetLocation(Target, 30000.0f);
	AdjustAimWithAccuracy(TargetLocation);
	
	FVector Direction = (TargetLocation - ControlledCharacter->GetActorLocation()).GetSafeNormal();
	FRotator TargetRotation = Direction.Rotation();
	SetControlRotation(TargetRotation);

	// ? FIRE WEAPON (SERVER) ?
	if (HasAuthority())  // Server only
	{
		// Call your server fire RPC
		ControlledCharacter->ServerFire(TargetLocation);
		
		// Or directly fire
		// YourWeaponSystem->Fire(ControlledCharacter, TargetLocation);
	}
}
```

---

## **?? COMPLETE EXAMPLE (With Your Weapon System):**

```cpp
// In FRAIBotController.cpp

#include "YourWeaponComponent.h"  // Add your weapon header

void AFRAIBotController::FireAtTarget(float DeltaTime)
{
	if (!CurrentTarget.IsValid() || !ControlledCharacter)
		return;

	AActor* Target = CurrentTarget.Get();

	// Check line of sight
	if (!CanSeeTarget(Target))
	{
		return;
	}

	// Predict target movement
	FVector TargetLocation = PredictTargetLocation(Target, 30000.0f);
	
	// Apply accuracy/inaccuracy
	AdjustAimWithAccuracy(TargetLocation);

	// Aim at target
	FVector Direction = (TargetLocation - ControlledCharacter->GetActorLocation()).GetSafeNormal();
	FRotator TargetRotation = Direction.Rotation();
	SetControlRotation(TargetRotation);
	ControlledCharacter->SetActorRotation(TargetRotation);  // Make character face target

	// ??? WEAPON FIRING ???
	
	// Get weapon component
	UYourWeaponComponent* WeaponComp = ControlledCharacter->FindComponentByClass<UYourWeaponComponent>();
	
	if (WeaponComp && WeaponComp->CanFire())  // Check if can fire (ammo, cooldown, etc.)
	{
		// Fire the weapon
		WeaponComp->StartFire();
		
		// Optional: Stop firing after a burst
		if (FMath::FRand() < 0.3f)  // 30% chance to pause (burst fire)
		{
			WeaponComp->StopFire();
		}
	}
}
```

---

## **?? TESTING WEAPON FIRING:**

### **1. Add Debug Logging:**

```cpp
void AFRAIBotController::FireAtTarget(float DeltaTime)
{
	// ... existing code ...

	// Add debug log
	FR_LOG_INFO(LogFrontline, "[Bot %s] FIRING at %s (Distance: %.0f)", 
		*GetName(), 
		*Target->GetName(),
		FVector::Dist(ControlledCharacter->GetActorLocation(), Target->GetActorLocation())
	);

	// Fire weapon
	// ...
}
```

### **2. Add Debug Visualization:**

```cpp
void AFRAIBotController::FireAtTarget(float DeltaTime)
{
	// ... aim and fire code ...

	// Draw debug line to show where bot is aiming
	#if !UE_BUILD_SHIPPING
	DrawDebugLine(
		GetWorld(),
		ControlledCharacter->GetActorLocation(),
		TargetLocation,
		FColor::Red,
		false,  // Persistent
		0.1f,   // Lifetime
		0,      // Depth priority
		2.0f    // Thickness
	);
	#endif
}
```

---

## **?? BURST FIRE PATTERN:**

Make bots fire in bursts (more realistic):

```cpp
void AFRAIBotController::FireAtTarget(float DeltaTime)
{
	if (!CurrentTarget.IsValid() || !ControlledCharacter)
		return;

	// ... aim code ...

	// Burst fire logic
	static float BurstTimer = 0.0f;
	static bool bIsFiring = false;
	
	BurstTimer += DeltaTime;

	// Fire in bursts
	if (bIsFiring)
	{
		// Fire for 0.5 seconds
		if (BurstTimer < 0.5f)
		{
			WeaponComponent->Fire();
		}
		else
		{
			// Stop and wait
			bIsFiring = false;
			BurstTimer = 0.0f;
		}
	}
	else
	{
		// Wait for 0.3 seconds
		if (BurstTimer > 0.3f)
		{
			bIsFiring = true;
			BurstTimer = 0.0f;
		}
	}
}
```

---

## **?? AMMO MANAGEMENT:**

Check ammo before firing:

```cpp
void AFRAIBotController::FireAtTarget(float DeltaTime)
{
	// ... aim code ...

	// Check ammo
	if (InventoryComponent)
	{
		int32 Ammo = InventoryComponent->GetCurrentAmmo();
		
		if (Ammo <= 0)
		{
			// No ammo, reload or switch weapon
			if (InventoryComponent->HasWeaponWithAmmo())
			{
				InventoryComponent->SwitchToWeaponWithAmmo();
			}
			else
			{
				// Find ammo loot
				AActor* AmmoLoot = FindNearbyAmmo();
				if (AmmoLoot)
				{
					MoveToLocation(AmmoLoot->GetActorLocation());
				}
			}
			return;
		}
	}

	// Fire weapon
	WeaponComponent->Fire();
}
```

---

## **?? WEAPON SELECTION:**

Make bots choose appropriate weapons:

```cpp
void AFRAIBotController::SelectBestWeapon()
{
	if (!InventoryComponent)
		return;

	float DistanceToTarget = 0.0f;
	if (CurrentTarget.IsValid())
	{
		DistanceToTarget = FVector::Dist(
			ControlledCharacter->GetActorLocation(),
			CurrentTarget->GetActorLocation()
		);
	}

	// Select weapon based on range
	if (DistanceToTarget > 5000.0f)  // Long range (50m+)
	{
		InventoryComponent->EquipWeaponByType(EWeaponType::SniperRifle);
	}
	else if (DistanceToTarget > 2000.0f)  // Medium range (20-50m)
	{
		InventoryComponent->EquipWeaponByType(EWeaponType::AssaultRifle);
	}
	else  // Close range (< 20m)
	{
		InventoryComponent->EquipWeaponByType(EWeaponType::Shotgun);
	}
}
```

---

## **? CHECKLIST:**

After adding weapon firing:

- [ ] Bots aim at targets ?
- [ ] Bots fire weapons ? (needs implementation)
- [ ] Bots check ammo
- [ ] Bots reload when needed
- [ ] Bots use appropriate weapons for range
- [ ] Bots fire in bursts (realistic)
- [ ] Bots stop firing when target dies
- [ ] Debug visualization shows aim direction

---

## **?? TESTING:**

1. **Stand still in game**
2. **Let enemy bot see you**
3. **Bot should:**
   - Turn to face you ?
   - Aim at you ?
   - Start firing ? (after you add weapon code)
   - Hit you based on accuracy setting

---

**ADD YOUR WEAPON FIRING CODE TO `FireAtTarget()` AND REBUILD!** ???

The AI system is ready - it just needs to be connected to your weapon system!
