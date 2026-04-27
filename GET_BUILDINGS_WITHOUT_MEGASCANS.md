# ?? **GET BUILDINGS WITHOUT MEGASCANS - COMPLETE GUIDE**

## **?? YOU DON'T HAVE MEGASCANS? NO PROBLEM!**

Multiple free alternatives to get buildings in your project!

---

## **? OPTION 1: UNREAL MARKETPLACE - FREE ASSETS**

### **Best Free Building Packs:**

**1. City Sample Crowds (Epic's FREE Pack):**
```
What: Epic's official city environment
Contains: Buildings, roads, props, vehicles
Quality: AAA (used in Matrix demo)
Size: Large (5+ GB)

How to Get:
1. Open Epic Games Launcher
2. Unreal Engine ? Marketplace
3. Search: "City Sample"
4. Look for "City Sample Crowds" or "City Sample"
5. Click "Free"
6. Click "Add to Project"
7. Select: Frontline
8. Click "Add to Project"
9. Wait for download (may take 10-30 minutes)

Result: Professional city buildings!
```

**2. Modular Sci-Fi Season 1:**
```
What: Modular building pieces
Contains: Walls, floors, props
Quality: High
Size: ~1 GB

How to Get:
1. Marketplace ? Search: "Modular Sci-Fi Season 1"
2. Should be FREE
3. Add to Frontline project
4. Great for testing!
```

**3. Other Free Packs to Try:**
```
Search in Marketplace:
?? "Urban City" (filter: Free)
?? "Building Pack" (filter: Free)
?? "Environment" (filter: Free)
?? "Modular" (filter: Free)

Many packs go on sale or free monthly!
```

---

## **? OPTION 2: FREE 3D MODEL WEBSITES**

### **1. Sketchfab (Best for Quick Assets):**

**How to Use:**
```
1. Go to: sketchfab.com

2. Search: "building" or "house"

3. Filter:
   ?? Downloadable: ?
   ?? Animated: ?
   ?? License: CC BY (can use commercially)

4. Find a building you like

5. Click "Download 3D Model"

6. Select format: FBX or glTF

7. Download (usually 10-50 MB)

8. Import to Unreal:
   - Open Unreal Editor
   - Content Browser ? Right-click
   - Import to /Game/Buildings/
   - Browse to downloaded FBX
   - Click Open
   - Accept default settings
   - Click Import All

9. Building appears in Content Browser!
```

**Good Searches on Sketchfab:**
```
- "low poly building" (easier to run)
- "pbr building" (better materials)
- "modular building"
- "house exterior"
- "warehouse"
- "factory building"
```

**Recommended Sketchfab Models:**
```
Look for:
? "PBR" in title (good materials)
? "Game Ready" tag
? Low-poly counts (under 50k tris)
? CC BY or CC0 license

Avoid:
? Very high poly (over 100k tris)
? No textures
? "For rendering only"
```

---

### **2. CGTrader Free Section:**

```
1. Go to: cgtrader.com

2. Click "Free 3D Models"

3. Search: "building"

4. Filter:
   ?? Price: Free
   ?? File Format: FBX
   ?? Purpose: Game

5. Download

6. Import to Unreal (same process as Sketchfab)
```

---

### **3. TurboSquid Free:**

```
1. Go to: turbosquid.com

2. Search: "building free"

3. Filter: Free

4. Download FBX format

5. Import to Unreal
```

---

### **4. Free3D:**

```
1. Go to: free3d.com

2. Browse: Buildings category

3. Download FBX files

4. Import to Unreal

Note: Quality varies, but all FREE!
```

---

## **? OPTION 3: CREATE SIMPLE TEST BUILDINGS**

### **Use Unreal's Modeling Tools:**

**Quick Building Creation (10 minutes):**

```
In Unreal Editor:

1. Mode Panel ? Modeling

2. Select "Box" tool

3. Create basic box (drag in viewport)

4. Adjust dimensions:
   X: 1000 (width)
   Y: 800 (depth)
   Z: 600 (height)

5. This is your building!

6. Apply material:
   - Content Browser ? StarterContent ? Materials
   - Drag M_Brick_Clay_New onto your box

7. Duplicate for more buildings:
   - Select building
   - Alt+Drag to duplicate
   - Vary sizes

8. Save as Static Mesh:
   - Select your box
   - Right-click ? Convert ? Create Static Mesh
   - Name: SM_Building_01
   - Location: /Game/Buildings/

9. Repeat for 5-10 different sizes

Result: Simple but functional test buildings!
```

---

## **? OPTION 4: STARTER CONTENT (IF YOU HAVE IT)**

**If you enabled Starter Content when creating project:**

```
Content Browser:
?? StarterContent/
   ?? Architecture/
   ?  ?? Wall pieces
   ?  ?? Floor pieces
   ?  ?? Pillar pieces
   ?? Props/
      ?? Various props

Use These:
1. Drag wall pieces into level
2. Combine to make rooms
3. Use as temporary buildings
4. Good for testing!
```

---

## **? OPTION 5: PROCEDURAL GENERATION (USE EXISTING SHAPES)**

### **Test with Basic Shapes:**

```
In Content Browser:

1. Engine Content ? BasicShapes

2. You'll find:
   ?? Cube
   ?? Cylinder
   ?? Cone
   ?? Sphere

3. Use these as placeholder buildings:
   - Cube = Building base
   - Cylinder = Tower
   - Cone = Roof

4. Scale them up (R key):
   - X: 10, Y: 10, Z: 6 for building
   - X: 3, Y: 3, Z: 15 for tower

5. Place multiple to create "buildings"

6. Your asset library will detect them!

Result: Can test system immediately!
```

---

## **?? RECOMMENDED APPROACH (FASTEST):**

### **Hybrid Method - Mix Sources:**

```
Day 1 (Today - 1 hour):
?? Download 3-5 buildings from Sketchfab (Free)
?? Create 3-5 simple box buildings in Unreal
?? Total: 8-10 test buildings

Day 2 (Tomorrow - 2 hours):
?? Browse Marketplace for free packs
?? Download 1 free pack (if available)
?? Import more Sketchfab buildings

Week 1 (Ongoing):
?? Check Marketplace monthly free offers
?? Download more Sketchfab buildings
?? Build comprehensive library

Result: Functional library NOW, improves over time!
```

---

## **?? STEP-BY-STEP: SKETCHFAB METHOD**

**Detailed walkthrough (most reliable free method):**

**Step 1: Find Buildings**
```
1. Open browser ? sketchfab.com

2. Click search bar

3. Type: "low poly building"

4. Press Enter

5. On left sidebar, click:
   - Downloadable
   - Animated: OFF
   - Rigged: OFF

6. Scroll through results

7. Look for:
   ? Buildings with textures
   ? "PBR" in title
   ? Simple geometry
   ? CC BY or CC0 license
```

**Step 2: Download**
```
1. Click on a building model

2. Check license (bottom right):
   ? CC BY = Can use (give credit in game)
   ? CC0 = Can use (no credit needed)
   ? Standard = Need permission

3. Click "Download 3D Model" button

4. Login/Create free account (one time)

5. Select format: "Autoconverted format (FBX)"

6. Click Download

7. Save to desktop or Downloads folder

8. Extract ZIP file
```

**Step 3: Import to Unreal**
```
1. Open Unreal Editor

2. Content Browser ? Navigate to /Game/

3. Create folder: Buildings
   - Right-click ? New Folder
   - Name: Buildings

4. Open Buildings folder

5. Right-click in empty space

6. Import to /Game/Buildings/

7. Browse to extracted FBX file

8. Click Open

9. Import Options dialog appears:
   - Skeletal Mesh: ? (unchecked)
   - Import Meshes: ? (checked)
   - Import Textures: ? (checked)
   - Import Materials: ? (checked)
   - Auto Generate Collision: ? (checked)

10. Click "Import All"

11. Wait 5-30 seconds

12. Building appears in Content Browser!

13. Double-click to preview

14. Drag into viewport to test
```

**Step 4: Repeat**
```
Download 5-10 buildings
Each takes 2-5 minutes
Total time: 30 minutes
Result: Functional building library!
```

---

## **?? QUALITY EXPECTATIONS:**

**Sketchfab Free Models:**
```
Quality: ????? to ????? (varies)
Pros:
? 100% Free
? Immediate download
? Large variety
? Many game-ready

Cons:
? Quality varies
? May need material fixes
? Some need cleanup

Perfect for: Testing, prototypes, placeholders
```

**Marketplace Free Packs:**
```
Quality: ????? to ?????
Pros:
? Professional quality
? Auto-imports
? Tested for Unreal
? Complete materials

Cons:
? Limited free selection
? Large downloads
? Specific styles

Perfect for: Final quality, themed environments
```

**Basic Shapes/Self-Made:**
```
Quality: ????? (simple)
Pros:
? Instant
? No download
? Full control
? Lightweight

Cons:
? Very basic
? Time to make complex buildings
? Need artistic skills

Perfect for: Testing, learning, placeholders
```

---

## **?? AFTER IMPORTING:**

**Configure Your Asset Library:**

```
1. Open DA_AssetLibrary (if created)

2. Add Scan Path:
   - Click + next to Scan Paths
   - Type: /Game/Buildings/
   - Press Enter

3. Click "Scan And Populate Library"

4. Output Log shows:
   Scanning: /Game/Buildings/ (5 assets)
     + building_01 (StaticMesh, Category: Building_Urban_Modern)
     + warehouse_02 (StaticMesh, Category: Building_Urban_Industrial)
   ...

5. Your imported buildings auto-categorized!

6. Check Assets array to verify
```

---

## **?? PRO TIPS:**

### **Naming Downloaded Files:**

**Before importing, rename FBX files:**
```
Downloaded as:
?? "Building.fbx"
?? "model_3456.fbx"
?? "download.fbx"

Rename to:
?? "urban_building_modern_01.fbx"
?? "warehouse_industrial_02.fbx"
?? "factory_building_03.fbx"

Result: Better auto-categorization!
```

### **Start Small:**
```
Don't download 50 buildings at once!

Start with:
- 3 buildings from Sketchfab
- 2 created in Unreal
- Test the system works
- Then expand

Easier to manage and test!
```

### **Mix Quality Levels:**
```
Use mix of sources:
?? 2-3 high quality (Marketplace/good Sketchfab)
?? 5-7 medium quality (Sketchfab)
?? 3-5 simple shapes (Unreal basic shapes)

Tests system with variety!
```

---

## **?? DO THIS RIGHT NOW:**

**30-Minute Quick Start:**

```
STEP 1 (10 min):
?? Go to sketchfab.com
?? Search "low poly building"
?? Download 3 buildings
?? Save to desktop

STEP 2 (5 min):
?? Create simple box building in Unreal
?? Convert to static mesh
?? Save 3 variations

STEP 3 (10 min):
?? Import Sketchfab buildings
?? Place in /Game/Buildings/
?? Verify import

STEP 4 (5 min):
?? Open DA_AssetLibrary
?? Add /Game/Buildings/ to scan paths
?? Click Scan
?? See buildings categorized!

TOTAL: 30 minutes
RESULT: 6-8 test buildings ready!
```

---

## **?? CHECKLIST:**

**Getting Buildings Without Megascans:**

- [ ] Try Sketchfab (free, immediate)
- [ ] Check Marketplace for free packs
- [ ] Create simple test buildings in Unreal
- [ ] Download 3-5 buildings from any source
- [ ] Import to /Game/Buildings/
- [ ] Add scan path to DA_AssetLibrary
- [ ] Scan library
- [ ] Verify detection
- [ ] Test place in level

---

## **? TROUBLESHOOTING:**

### **Import fails:**
```
1. Make sure FBX format (not OBJ or GLTF)
2. Check file isn't corrupted (re-download)
3. Try different model
4. Check file size (keep under 100 MB)
```

### **Materials missing:**
```
1. Check if textures downloaded with FBX
2. Look for .jpg or .png files in same folder
3. Import them separately if needed
4. Apply to material in Unreal
```

### **Model too big/small:**
```
1. Select in viewport
2. Press R key for scale mode
3. Type scale value (0.1 = smaller, 10 = bigger)
4. Test until looks right
```

---

## **?? RECOMMENDED FIRST STEPS:**

```
RIGHT NOW (Choose one):

OPTION A - Sketchfab (30 min):
?? Best for immediate buildings

OPTION B - Create Basic (15 min):
?? Best for testing system quickly

OPTION C - Marketplace (1 hour):
?? Best for quality (if packs available)

THEN:
?? Import/create buildings
?? Scan library
?? Test in level
?? Success! ??
```

---

**Start with Sketchfab - it's free, fast, and has thousands of buildings! ??**

**Link: https://sketchfab.com/search?q=building&type=models**

You'll have buildings in 30 minutes!
