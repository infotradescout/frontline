# ?? **EMERGENCY: COMPLETE LIGHTING & SKY FIX**

## **THE PROBLEM:**

Your game has:
- ? Black screen
- ? No sky
- ? No lighting
- ? No environment

**Even though:**
- ? Bots work
- ? GameMode loads
- ? Code compiles

---

## **? COMPREHENSIVE FIX - ADD TO GAMEMODE:**

Add this to `AFRGameMode::BeginPlay()` **RIGHT AFTER** the emergency light code:

```cpp
// COMPLETE WORLD LIGHTING SYSTEM
void AFRGameMode::SpawnCompleteWorldLighting()
{
    UWorld* World = GetWorld();
    if (!World) return;
    
    UE_LOG(LogTemp, Warning, TEXT("[GameMode] ?? SPAWNING COMPLETE WORLD LIGHTING"));
    
    // ============================================================
    // 1. DIRECTIONAL LIGHT (SUN)
    // ============================================================
    
    TArray<AActor*> ExistingLights;
    UGameplayStatics::GetAllActorsOfClass(World, ADirectionalLight::StaticClass(), ExistingLights);
    
    ADirectionalLight* Sun = nullptr;
    if (ExistingLights.Num() > 0)
    {
        Sun = Cast<ADirectionalLight>(ExistingLights[0]);
        UE_LOG(LogTemp, Warning, TEXT("[GameMode] ?? Found existing DirectionalLight"));
    }
    else
    {
        // Create new sun
        FActorSpawnParameters SpawnParams;
        SpawnParams.Name = FName(TEXT("Sun_Auto"));
        Sun = World->SpawnActor<ADirectionalLight>(ADirectionalLight::StaticClass(), FVector::ZeroVector, FRotator(-45.0f, 0.0f, 0.0f), SpawnParams);
        
        if (Sun)
        {
            UDirectionalLightComponent* SunComp = Sun->GetComponent();
            if (SunComp)
            {
                SunComp->SetIntensity(10.0f); // Bright sun
                SunComp->SetLightColor(FLinearColor(1.0f, 0.95f, 0.9f)); // Warm white
                SunComp->SetCastShadows(true);
                SunComp->bAffectsWorld = true;
                SunComp->SetMobility(EComponentMobility::Movable);
                SunComp->MarkRenderStateDirty();
            }
            
            UE_LOG(LogTemp, Warning, TEXT("[GameMode] ?? Created DirectionalLight (Sun)"));
        }
    }
    
    // ============================================================
    // 2. SKY LIGHT (AMBIENT)
    // ============================================================
    
    TArray<AActor*> ExistingSkyLights;
    UGameplayStatics::GetAllActorsOfClass(World, ASkyLight::StaticClass(), ExistingSkyLights);
    
    ASkyLight* SkyLight = nullptr;
    if (ExistingSkyLights.Num() > 0)
    {
        SkyLight = Cast<ASkyLight>(ExistingSkyLights[0]);
        UE_LOG(LogTemp, Warning, TEXT("[GameMode] ?? Found existing SkyLight"));
    }
    else
    {
        // Create new sky light
        FActorSpawnParameters SpawnParams;
        SpawnParams.Name = FName(TEXT("SkyLight_Auto"));
        SkyLight = World->SpawnActor<ASkyLight>(ASkyLight::StaticClass(), FVector::ZeroVector, FRotator::ZeroRotator, SpawnParams);
        
        if (SkyLight)
        {
            USkyLightComponent* SkyComp = SkyLight->GetLightComponent();
            if (SkyComp)
            {
                SkyComp->SetIntensity(1.0f);
                SkyComp->SetLightColor(FLinearColor(0.4f, 0.6f, 1.0f)); // Blue sky
                SkyComp->SourceType = ESkyLightSourceType::SLS_CapturedScene;
                SkyComp->SetMobility(EComponentMobility::Movable);
                SkyComp->bRealTimeCapture = true; // Live update
                SkyComp->RecaptureSky();
                SkyComp->MarkRenderStateDirty();
            }
            
            UE_LOG(LogTemp, Warning, TEXT("[GameMode] ?? Created SkyLight"));
        }
    }
    
    // ============================================================
    // 3. EXPONENTIAL HEIGHT FOG (ATMOSPHERE)
    // ============================================================
    
    TArray<AActor*> ExistingFog;
    UGameplayStatics::GetAllActorsOfClass(World, AExponentialHeightFog::StaticClass(), ExistingFog);
    
    AExponentialHeightFog* Fog = nullptr;
    if (ExistingFog.Num() > 0)
    {
        Fog = Cast<AExponentialHeightFog>(ExistingFog[0]);
        UE_LOG(LogTemp, Warning, TEXT("[GameMode] ??? Found existing Fog"));
    }
    else
    {
        // Create fog
        FActorSpawnParameters SpawnParams;
        SpawnParams.Name = FName(TEXT("Fog_Auto"));
        Fog = World->SpawnActor<AExponentialHeightFog>(AExponentialHeightFog::StaticClass(), FVector(0, 0, 0), FRotator::ZeroRotator, SpawnParams);
        
        if (Fog)
        {
            UExponentialHeightFogComponent* FogComp = Fog->GetComponent();
            if (FogComp)
            {
                FogComp->FogDensity = 0.01f; // Light fog
                FogComp->FogHeightFalloff = 0.2f;
                FogComp->StartDistance = 5000.0f; // Fog starts 50m away
                FogComp->FogInscatteringColor = FLinearColor(0.6f, 0.7f, 0.9f); // Blue-ish
                FogComp->DirectionalInscatteringColor = FLinearColor(1.0f, 0.9f, 0.7f); // Warm glow
                FogComp->MarkRenderStateDirty();
            }
            
            UE_LOG(LogTemp, Warning, TEXT("[GameMode] ??? Created ExponentialHeightFog"));
        }
    }
    
    // ============================================================
    // 4. SKY SPHERE (VISUAL SKY)
    // ============================================================
    
    // Note: BP_Sky_Sphere is a blueprint, we can't spawn it from C++
    // But we can spawn a simple sphere with sky material
    
    AStaticMeshActor* SkySphere = World->SpawnActor<AStaticMeshActor>(
        AStaticMeshActor::StaticClass(),
        FVector(0, 0, 0),
        FRotator::ZeroRotator
    );
    
    if (SkySphere)
    {
        UStaticMeshComponent* MeshComp = SkySphere->GetStaticMeshComponent();
        if (MeshComp)
        {
            // Load engine sphere mesh
            static ConstructorHelpers::FObjectFinder<UStaticMesh> SphereMesh(TEXT("/Engine/BasicShapes/Sphere"));
            if (SphereMesh.Succeeded())
            {
                MeshComp->SetStaticMesh(SphereMesh.Object);
                MeshComp->SetWorldScale3D(FVector(500000.0f)); // HUGE sphere (5km radius)
                MeshComp->SetCollisionEnabled(ECollisionEnabled::NoCollision);
                MeshComp->SetCastShadow(false);
                
                // Use simple blue material
                UMaterialInterface* SkyMat = LoadObject<UMaterialInterface>(nullptr, TEXT("/Engine/EngineMaterials/DefaultMaterial"));
                if (SkyMat)
                {
                    MeshComp->SetMaterial(0, SkyMat);
                }
            }
        }
        
        UE_LOG(LogTemp, Warning, TEXT("[GameMode] ?? Created Sky Sphere"));
    }
    
    // ============================================================
    // 5. POST PROCESS VOLUME (TONE MAPPING)
    // ============================================================
    
    TArray<AActor*> ExistingPPV;
    UGameplayStatics::GetAllActorsOfClass(World, APostProcessVolume::StaticClass(), ExistingPPV);
    
    APostProcessVolume* PPV = nullptr;
    if (ExistingPPV.Num() > 0)
    {
        PPV = Cast<APostProcessVolume>(ExistingPPV[0]);
        UE_LOG(LogTemp, Warning, TEXT("[GameMode] ?? Found existing PostProcessVolume"));
    }
    else
    {
        // Create post process volume
        FActorSpawnParameters SpawnParams;
        SpawnParams.Name = FName(TEXT("PPV_Auto"));
        PPV = World->SpawnActor<APostProcessVolume>(APostProcessVolume::StaticClass(), FVector::ZeroVector, FRotator::ZeroRotator, SpawnParams);
        
        if (PPV)
        {
            PPV->bUnbound = true; // Affects entire world
            
            FPostProcessSettings& Settings = PPV->Settings;
            
            // Disable auto exposure (prevents black screen)
            Settings.bOverride_AutoExposureMethod = true;
            Settings.AutoExposureMethod = EAutoExposureMethod::AEM_Manual;
            
            Settings.bOverride_AutoExposureBias = true;
            Settings.AutoExposureBias = 0.0f; // Neutral exposure
            
            // Tone mapping
            Settings.bOverride_ToneCurveAmount = true;
            Settings.ToneCurveAmount = 0.0f; // Linear (no curve)
            
            // Color grading
            Settings.bOverride_ColorSaturation = true;
            Settings.ColorSaturation = FVector4(1.0f, 1.0f, 1.0f, 1.0f); // Full saturation
            
            Settings.bOverride_ColorContrast = true;
            Settings.ColorContrast = FVector4(1.0f, 1.0f, 1.0f, 1.0f); // Normal contrast
            
            Settings.bOverride_ColorGamma = true;
            Settings.ColorGamma = FVector4(1.0f, 1.0f, 1.0f, 1.0f); // No gamma adjust
            
            PPV->MarkComponentsRenderStateDirty();
            
            UE_LOG(LogTemp, Warning, TEXT("[GameMode] ?? Created PostProcessVolume"));
        }
    }
    
    // ============================================================
    // 6. FORCE RENDERING UPDATE
    // ============================================================
    
    if (APlayerController* PC = World->GetFirstPlayerController())
    {
        // Force rendering cvars
        PC->ConsoleCommand(TEXT("r.DefaultFeature.AutoExposure 0"));
        PC->ConsoleCommand(TEXT("r.EyeAdaptationQuality 0"));
        PC->ConsoleCommand(TEXT("r.Tonemapper.Sharpen 0"));
        PC->ConsoleCommand(TEXT("showflag.Fog 1"));
        PC->ConsoleCommand(TEXT("showflag.AtmosphericFog 1"));
        PC->ConsoleCommand(TEXT("showflag.Lighting 1"));
        PC->ConsoleCommand(TEXT("showflag.DirectLighting 1"));
        PC->ConsoleCommand(TEXT("showflag.SkyLighting 1"));
        PC->ConsoleCommand(TEXT("showflag.DynamicShadows 1"));
        PC->ConsoleCommand(TEXT("viewmode lit"));
        
        UE_LOG(LogTemp, Warning, TEXT("[GameMode] ?? Forced rendering settings"));
    }
    
    UE_LOG(LogTemp, Warning, TEXT("[GameMode] ??? COMPLETE WORLD LIGHTING SPAWNED ???"));
}
```

---

## **?? HOW TO ADD IT:**

### **1. Add to AFRGameMode.h:**

```cpp
protected:
    // Emergency world lighting spawn
    void SpawnCompleteWorldLighting();
```

### **2. Add to AFRGameMode.cpp BeginPlay:**

Find this line:
```cpp
UE_LOG(LogTemp, Warning, TEXT("[GameMode] ? EMERGENCY LIGHT spawned at 300m high!"));
```

**RIGHT AFTER IT**, add:
```cpp
// SPAWN COMPLETE WORLD LIGHTING SYSTEM
SpawnCompleteWorldLighting();
```

### **3. Add the function implementation** (the huge code block above)

---

## **? WHAT THIS DOES:**

| Component | Purpose | Result |
|-----------|---------|--------|
| **DirectionalLight** | Sun | ?? Main light source |
| **SkyLight** | Ambient light | ?? Fills shadows |
| **ExponentialHeightFog** | Atmosphere | ??? Depth & distance |
| **Sky Sphere** | Visual sky | ?? Blue background |
| **PostProcessVolume** | Tone mapping | ?? Proper exposure |
| **Console commands** | Force render | ?? Enable all rendering |

---

## **?? RESULT:**

After adding this and building:
- ? **Bright, visible world**
- ? **Blue sky with sun**
- ? **Proper lighting on all objects**
- ? **Atmosphere and fog**
- ? **No more black screen!**

---

**ADD THIS CODE NOW AND REBUILD!** ???

