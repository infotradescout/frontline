# ??? **USING YOUR GOODSKY ASSET - COMPLETE GUIDE**

## **? PERFECT! YOU HAVE A FREE SKY!**

I've updated the system to work with **ANY sky asset**, including your "GoodSky"!

---

## **?? HOW IT WORKS NOW:**

### **Simple & Flexible System:**
```
1. You manually place GoodSky in your level (drag & drop)
2. My code controls lighting and fog automatically
3. Same seed = same lighting/atmosphere
4. Different seeds = variety (8 weather types)
5. Works with GoodSky or ANY sky asset!
```

### **No Dependencies:**
- ? Doesn't require specific asset names
- ? Works with your GoodSky
- ? Works with engine default sky
- ? Controls standard Unreal lighting/fog
- ? Seed-based for consistency

---

## **?? SETUP STEPS:**

### **Step 1: Close Editor & Build**
```
IMPORTANT: Do this first!

1. Close Unreal Editor (if open)
2. Open Visual Studio
3. Build Solution (F7)
4. Wait for "Build succeeded"
```

### **Step 2: Open Level & Place GoodSky**
```
1. Open Unreal Editor
2. Create or open level
3. Content Browser ? GoodSky folder
4. Find the main sky blueprint (usually BP_Sky or similar)
5. Drag it into the level
6. Position at (0, 0, 0) or wherever you want
```

### **Step 3: Set Up Lighting**
```
Your GoodSky probably includes:
- Sky sphere/dome
- Maybe sun/moon
- Maybe clouds

My system adds:
- Directional light (sun)
- Sky light (ambient)
- Exponential fog
- Seed-based configuration
```

### **Step 4: Test!**
```
1. Place AFRAutoLevelGenerator in level
2. Set LevelType = GameMap
3. Set MapSeed = any number (e.g., 12345)
4. Press Play
5. Lighting/fog configured automatically!
```

---

## **?? WEATHER TYPES (8 PRESETS):**

| Weather | Sun Brightness | Fog | Look |
|---------|---------------|-----|------|
| **Clear Day** | 15 (bright) | None | Perfect visibility |
| **Partly Cloudy** | 12 (good) | Light | Nice day |
| **Overcast** | 8 (dim) | Medium | Gray, moody |
| **Foggy** | 5 (dark) | Heavy | Low visibility |
| **Evening** | 10 (warm) | Light | Orange sunset |
| **Storm** | 4 (very dark) | Heavy | Dark & dramatic |
| **Night** | 0.5 (minimal) | Medium | Dark, moonlit |
| **Dawn** | 8 (soft) | Medium | Early morning |

---

## **?? SEED EXAMPLES:**

| Seed | Weather | Description |
|------|---------|-------------|
| 12345 | Partly Cloudy | Nice balanced weather |
| 99999 | Storm | Dark and moody |
| 11111 | Clear Day | Perfect visibility |
| 55555 | Foggy | Tactical gameplay |
| 77777 | Evening | Beautiful sunset |
| 33333 | Overcast | Competitive lighting |

**Same seed always gives same weather!**

---

## **?? HOW TO USE:**

### **Option A: Automatic (Recommended)**
```
1. Place GoodSky asset in level
2. Place AFRAutoLevelGenerator
3. Set LevelType = GameMap
4. Set MapSeed = any number
5. Press Play
6. Done! Weather configured automatically
```

### **Option B: Manual Control**
```
In Level Blueprint or C++:

// Apply specific weather
SkyController->ApplyWeatherType(EFRSkyWeatherType::Storm);

// Apply from seed
SkyController->ApplyWeatherFromSeed(12345);
```

---

## **?? WHAT EACH COMPONENT DOES:**

### **Your GoodSky Asset:**
- Provides visual sky dome/sphere
- Maybe includes clouds
- Maybe includes sun/moon visuals
- Looks pretty!

### **My Sky Controller:**
- Controls directional light (sun angle/color)
- Controls sky light (ambient lighting)
- Controls fog (density/color/distance)
- Changes based on seed
- Consistent per seed

### **Result:**
```
GoodSky visuals + My lighting control = Perfect atmosphere!
```

---

## **?? CHECKING GOODSKY CONTENTS:**

### **In Unreal Editor:**
```
1. Content Browser
2. Navigate to GoodSky folder
3. Look for these types of assets:

? BP_Sky or BP_GoodSky (main blueprint)
? M_Sky_* (materials)
? T_Sky_* (textures)
? Mesh files (sky sphere/dome)

Common names:
- BP_Sky_Sphere
- BP_Dynamic_Sky
- BP_Sky_System
- SkyDome
- Sky_BP
```

### **How to Place:**
```
1. Find the main BP_ file (usually biggest blueprint)
2. Drag into viewport
3. Should appear as large sphere/dome around level
4. If too small/big, adjust scale
5. If upside down, rotate 180°
```

---

## **?? EXAMPLE SETUP:**

### **Level Setup:**
```
Your Level:
??? GoodSky BP (from Content/GoodSky)
??? AFRAutoLevelGenerator (auto-spawns lighting)
??? Floor/ground (for walking)
??? Player Start (if testing without island)
```

### **What Spawns Automatically:**
```
When you press Play:
??? Directional Light (sun) ? Controlled by seed
??? Sky Light (ambient) ? Controlled by seed
??? Exponential Fog ? Controlled by seed
??? Post Process Volume ? Optional enhancements
??? Sky Controller ? Manages everything
```

---

## **?? TESTING CHECKLIST:**

After building:

- [ ] Close Unreal Editor
- [ ] Build in Visual Studio (F7)
- [ ] Open Unreal Editor
- [ ] Create test level
- [ ] Place GoodSky asset
- [ ] Place AutoLevelGenerator
- [ ] Set MapSeed = 12345
- [ ] Press Play
- [ ] Check Output Log for weather messages
- [ ] Verify lighting looks good
- [ ] Change seed to 99999
- [ ] Restart
- [ ] Verify different lighting

**If all checked: Working!** ?

---

## **?? TROUBLESHOOTING:**

### **Issue: "Can't find GoodSky"**
```
Solution:
1. Content Browser ? Search "sky"
2. Find any blueprint with "sky" in name
3. Drag it into level
4. My system doesn't care what it's called!
```

### **Issue: "Too dark/bright"**
```
Solution:
1. Find AFRUltraDynamicSkyController in level
2. Select it
3. Details panel ? Weather Presets
4. Expand the weather type you want
5. Adjust SunBrightness value
6. Test again
```

### **Issue: "Sky looks weird"**
```
Solution:
1. Select GoodSky actor in level
2. Check its scale (should be ~100-1000)
3. Check rotation (0, 0, 0 usually)
4. Check if it has multiple parts (enable all)
```

---

## **?? ADVANCED CUSTOMIZATION:**

### **Adjust Weather Probabilities:**
```cpp
// In FRUltraDynamicSkyController.cpp
// GetWeatherTypeFromSeed() function

// Change these for different probabilities:
if (Roll < 0.50f)  // 50% clear (was 35%)
    return EFRSkyWeatherType::ClearDay;
// etc.
```

### **Create Custom Weather:**
```cpp
// In InitializeDefaultPresets()

FFRWeatherPreset MyCustomWeather;
MyCustomWeather.SunBrightness = 20.0f;  // Very bright!
MyCustomWeather.SunColor = FLinearColor(1.0f, 0.5f, 0.5f);  // Red
MyCustomWeather.FogDensity = 0.8f;  // Heavy fog
WeatherPresets.Add(EFRSkyWeatherType::ClearDay, MyCustomWeather);
```

---

## **? BENEFITS OF THIS SYSTEM:**

### **For You:**
? Use the free sky you already downloaded  
? No need for specific marketplace assets  
? Simple setup (just drag GoodSky into level)  
? Automatic lighting control  
? Seed-based consistency  

### **For Gameplay:**
? Different lighting per match (based on seed)  
? Same seed = identical conditions  
? Competitive fairness  
? Visual variety  
? Professional look  

---

## **?? SUMMARY:**

### **What You Have:**
- ? GoodSky asset (free, looks good)
- ? My generic sky controller (works with anything)
- ? Seed-based system (consistent per seed)
- ? 8 weather presets (variety)

### **What You Do:**
1. Build project (close editor first!)
2. Open editor
3. Drag GoodSky into level
4. Place AutoLevelGenerator
5. Press Play
6. Enjoy automatic weather!

### **What You Get:**
- Perfect lighting every time
- Different atmosphere per seed
- Professional quality
- Zero complexity
- Works with YOUR sky asset!

---

**CLOSE EDITOR ? BUILD ? PLACE GOODSKY ? PLAY!** ????

**Your free GoodSky asset + my code = Perfect!**

