# ?? **UNREAL ENGINE 5 - DEFAULT ASSETS REFERENCE**

## **EVERYTHING BUILT-IN YOU CAN USE FOR FREE**

---

## **?? MATERIALS (No Import Needed)**

### **Basic Materials (Engine Content):**
```
M_Basic_Floor
M_Basic_Wall  
M_Tech_Hex_Tile
M_Metal_Gold
M_Metal_Steel
M_Metal_Copper
M_Metal_Chrome
M_Metal_Rust
M_Concrete_Tiles
M_Brick_Clay_New
M_Glass
```

**How to Use:**
```
1. Select mesh in level
2. Details ? Materials ? Element 0
3. Click dropdown ? Search material name
```

### **Material Colors (Set Dynamically):**
```cpp
// In C++
UMaterialInstanceDynamic* Mat = UMaterialInstanceDynamic::Create(BaseMaterial, this);
Mat->SetVectorParameterValue("Color", FLinearColor(1, 0, 0, 1)); // Red
GetMesh()->SetMaterial(0, Mat);
```

---

## **?? BASIC SHAPES (Place Actors Panel)**

### **Available Shapes:**
```
Plane       - Flat surface
Cube        - Box/building
Sphere      - Round objects
Cylinder    - Pillars, tubes
Cone        - Pointy objects  
Torus       - Donut shape
```

### **Quick Level Building:**
```
Floor:  Plane (scale X=100, Y=100)
Walls:  Cube (scale to be thin/tall)
Cover:  Cubes (various sizes)
Props:  Cylinders + Spheres combo
```

---

## **?? LIGHTING (Free Polish)**

### **Essential Lights:**
```
Directional Light
- Sun/Moon
- Intensity: 3-10
- Temperature: 5500 (white), 3500 (warm), 7500 (cool)

Sky Light
- Ambient fill light
- Always use with Directional Light
- Intensity: 0.5-2

Point Light
- Lamps, fires, explosions
- Radius: 500-5000
- Intensity: 1000-50000

Spot Light
- Flashlights, stage lights
- Inner/Outer Cone Angle
```

### **Free Atmosphere:**
```
Atmospheric Fog
- Adds haze/depth
- Automatically creates sky

Exponential Height Fog
- Ground-level fog
- Density: 0.01-0.1

Sky Atmosphere
- Realistic sky
- Auto sun/cloud simulation
```

### **Time of Day Presets:**
```
Dawn:    Dir Light (0.9, 0.6, 0.3), Intensity 8
Noon:    Dir Light (1, 1, 1), Intensity 10  
Sunset:  Dir Light (1, 0.4, 0.1), Intensity 6
Night:   Dir Light (0.1, 0.2, 0.4), Intensity 2
```

---

## **?? POST PROCESSING (Instant Mood)**

### **Place Post Process Volume:**
```
1. Place Actors ? Post Process Volume
2. Details ? Infinite Extent = TRUE
```

### **Common Settings:**

#### **Tactical/Military Look:**
```
Exposure:
- Method: Manual
- Exposure Compensation: -0.5

Color Grading:
- Saturation: 0.7 (desaturated)
- Contrast: 1.1

Bloom:
- Intensity: 0.5
- Threshold: 1.0

Vignette:
- Intensity: 0.4
```

#### **Sci-Fi/Future Look:**
```
Color Grading:
- Global Tint: Light Blue (0.9, 0.95, 1)
- Saturation: 1.2

Bloom:
- Intensity: 1.0

Chromatic Aberration:
- Intensity: 0.3
```

#### **Horror/Dark Look:**
```
Exposure:
- Compensation: -1.0

Color Grading:
- Saturation: 0.5
- Shadows Tint: Blue-gray

Vignette:
- Intensity: 0.8
```

---

## **?? DEFAULT CHARACTER (Mannequin)**

### **Unreal Engine 5 Includes:**
```
Skeletal Mesh: SK_Mannequin
Animation Blueprint: ABP_Mannequin
Control Rig: Already rigged for animations
```

### **How to Use:**
```
1. Create Blueprint based on Character class
2. Details ? Mesh ? Skeletal Mesh = SK_Mannequin
3. Animation ? Anim Class = ABP_Mannequin
4. Done! Has idle, walk, run, jump animations
```

### **Color-Code Mannequins:**
```cpp
// Make teams visible
void AMyCharacter::SetTeamColor(FLinearColor Color)
{
    UMaterialInstanceDynamic* Mat = GetMesh()->CreateDynamicMaterialInstance(0);
    Mat->SetVectorParameterValue("BodyColor", Color);
}

// Call:
SetTeamColor(FLinearColor::Blue);  // Team 1
SetTeamColor(FLinearColor::Red);   // Team 2
```

---

## **?? DEFAULT SOUNDS (Engine Content)**

### **Built-In Sound Cues:**
```
Explosion_Cue
Footstep_Cue  
Jump_Cue
Land_Cue
Rifle_Fire_Cue
```

**How to Find:**
```
Content Browser ? Engine Content (check "Show Engine Content")
? EngineSounds folder
```

### **Play Sound in C++:**
```cpp
UGameplayStatics::PlaySoundAtLocation(
    GetWorld(), 
    ExplosionSound,
    GetActorLocation()
);
```

---

## **??? LANDSCAPE (Terrain)**

### **Quick Landscape:**
```
Landscape Mode (top toolbar)
- Section Size: 63x63 (small), 127x127 (medium), 255x255 (large)
- Sections per Component: 1 or 2
- Number of Components: 8x8 (creates ~2km map)
- Click "Create"
```

### **Sculpt Tools (Built-in):**
```
Sculpt:    Raise/lower terrain
Smooth:    Smooth rough areas  
Flatten:   Make flat surfaces
Ramp:      Create slopes
Erosion:   Natural weathering
```

### **Paint Textures:**
```
Landscape ? Paint Mode
- Layer 1: Grass (green)
- Layer 2: Rock (gray)
- Layer 3: Dirt (brown)
- Paint where you want each
```

---

## **?? UMG WIDGETS (UI) - BUILT-IN STYLES**

### **Default Widget Types:**
```
Button      - Interactive
Text Block  - Display text
Image       - Show pictures (or solid colors)
Progress Bar - Health, loading
Slider      - Settings (volume, etc.)
Border      - Container with styling
Canvas Panel - Root for absolute positioning
Vertical Box - Stack widgets vertically
Horizontal Box - Stack widgets horizontally
```

### **No Graphics? Use Colors!**

#### **Buttons:**
```
Normal State:   Dark Gray (0.1, 0.1, 0.1)
Hovered State:  Medium Gray (0.3, 0.3, 0.3)
Pressed State:  Light Gray (0.5, 0.5, 0.5)
```

#### **Faction Colors:**
```
Aegis Order:    Blue (0.2, 0.4, 1.0)
Rift Ops:       Orange (1.0, 0.6, 0.1)
Black Cell:     Red (0.8, 0.1, 0.1)
Independent:    Gray (0.5, 0.5, 0.5)
```

#### **Text Shadows (Free Depth):**
```
Text Block ? Appearance ? Shadow
- Offset: X=2, Y=2
- Color: Black
- Instant readability!
```

---

## **?? CROSSHAIRS (No Images)**

### **Method 1: Simple Cross**
```
4 Border widgets:
- Top line: 2x10px, white
- Bottom line: 2x10px, white
- Left line: 10x2px, white  
- Right line: 10x2px, white
Center them on screen
```

### **Method 2: Circle + Dot**
```
1 Border (circle outline):
- Size: 32x32px
- Border: 2px white
- Background: Transparent

1 Border (center dot):
- Size: 4x4px
- Background: White
```

### **Method 3: Dynamic (Code)**
```cpp
UFUNCTION(BlueprintCallable)
void UpdateCrosshairSpread(float Spread)
{
    // Spread crosshair when moving/shooting
    CrosshairTop->SetRenderTranslation(FVector2D(0, -Spread));
    CrosshairBottom->SetRenderTranslation(FVector2D(0, Spread));
    CrosshairLeft->SetRenderTranslation(FVector2D(-Spread, 0));
    CrosshairRight->SetRenderTranslation(FVector2D(Spread, 0));
}
```

---

## **??? QUICK ENVIRONMENT PRESETS**

### **Urban (City):**
```
Floor: Gray concrete material
Cover: Tall gray boxes (buildings)
Props: Small boxes (cars, debris)
Lighting: Harsh white directional light
Fog: Gray exponential height fog
```

### **Desert (Military Base):**
```
Floor: Tan/yellow material
Cover: Brown cubes (sandbags, walls)
Props: Metal-colored cylinders (barrels)
Lighting: Warm orange directional light  
Fog: Dusty orange atmospheric fog
```

### **Arctic (Frozen):**
```
Floor: White material
Cover: White/blue boxes (ice structures)
Props: Gray cylinders (equipment)
Lighting: Cool blue-white directional
Fog: White dense fog
```

### **Facility (Indoor Lab):**
```
Floor: Shiny metallic material
Cover: Tech hex tile boxes
Props: Cylinders (computers, tanks)
Lighting: Multiple bright point lights
Fog: None (clear indoor)
```

### **Jungle (Dense Forest):**
```
Floor: Green material
Cover: Brown/green boxes (foliage, huts)
Props: Cylinders (tree trunks)
Lighting: Filtered green directional  
Fog: Green atmospheric fog
```

---

## **? PARTICLES (Free VFX)**

### **Built-In Particle Systems:**
```
P_Explosion
P_Fire
P_Smoke  
P_Steam
P_Spark
P_Dust_Kickup
```

**How to Spawn:**
```cpp
UGameplayStatics::SpawnEmitterAtLocation(
    GetWorld(),
    ExplosionParticle,
    GetActorLocation()
);
```

---

## **?? AUDIO WITHOUT FILES**

### **Use Synthesized Sounds:**

```cpp
// Create beep/tone sound
USynthComponent* SynthComp = NewObject<USynthComponent>(this);
SynthComp->SetFrequency(440.0f); // A note
SynthComp->Play();
```

### **Or Just Use Silence:**
```
Many successful games have minimal sound
- Early versions of Among Us
- Minecraft before sound updates
- Text-based UI feedback instead
```

---

## **?? COMPLETE STARTER KIT CHECKLIST**

### **For Main Menu:**
- [ ] Canvas Panel (root)
- [ ] Vertical Box (layout)
- [ ] Text blocks (title, buttons)
- [ ] Buttons with hover states
- [ ] Black/dark gray background

### **For Lobby:**
- [ ] Large plane (floor)
- [ ] Directional Light + Sky Light
- [ ] 10+ Player Start actors
- [ ] Atmospheric Fog
- [ ] Basic HUD widget

### **For Game Map:**
- [ ] Landscape OR giant plane
- [ ] 100+ Player Start actors
- [ ] Cubes for cover (20+)
- [ ] Lights (sun + ambient)
- [ ] Post Process Volume
- [ ] Zone Controller actor (yours!)

### **For HUD:**
- [ ] Health text/bar
- [ ] Ammo counter
- [ ] Crosshair (borders)
- [ ] Player count
- [ ] Minimap (optional)

---

## **?? PRO TIPS**

### **Tip 1: Keyboard Shortcuts**
```
W/E/R - Move/Rotate/Scale
Alt+Drag - Duplicate actor
End - Snap to ground
G - Hide grid
L - Toggle lighting preview
```

### **Tip 2: Material Instances**
```
Don't modify base materials!
Right-click material ? Create Material Instance
Modify the instance (change color, etc.)
```

### **Tip 3: Viewport Show Flags**
```
Viewport ? Show ? uncheck:
- Navigation (for screenshots)
- Grid (cleaner view)
- Collision (unless debugging)
```

### **Tip 4: Build Lighting**
```
Build ? Build Lighting (Production)
Wait 1-5 minutes
Makes everything look 10x better!
```

---

## **?? YOU NOW HAVE:**

? Materials (20+)
? Shapes (6 types)
? Lights (4 types + atmosphere)
? Post processing (instant mood)
? Character (mannequin)
? Sounds (10+)
? Landscape tools
? UI widgets (all types)
? Particles (explosions, etc.)

**ALL FREE. ALL BUILT-IN. ZERO IMPORTS!**

---

**Now go make your game look tactical with just cubes and colors!** ??????
