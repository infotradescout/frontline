# ?? **GET BUILDINGS NOW - SKETCHFAB METHOD (NO MARKETPLACE NEEDED)**

## **?? FASTEST & MOST RELIABLE FREE METHOD**

Since you can't access the Marketplace, we'll use **Sketchfab** - the best free 3D model website for game assets.

---

## **? STEP-BY-STEP GUIDE (30 MINUTES)**

### **Step 1: Go to Sketchfab (2 minutes)**

**1. Open Your Web Browser:**
```
Chrome, Firefox, Edge - any browser works
```

**2. Go to Sketchfab:**
```
URL: https://sketchfab.com

Or Google: "sketchfab"
Click first result
```

**3. Create Free Account (One Time):**
```
Top right: "Sign Up" button

Options:
?? Sign up with Google (fastest)
?? Sign up with Facebook
?? Sign up with email

Choose one and complete signup
Takes 1 minute
```

---

### **Step 2: Find Buildings (3 minutes)**

**1. Use Search Bar:**
```
At top of Sketchfab page:

Search bar: Type one of these:
?? "low poly building" (optimized for games)
?? "game ready building"
?? "pbr building" (good materials)
?? "modular building"

Press Enter
```

**2. Apply Filters:**
```
Left sidebar filters:

Click checkboxes:
?? Downloadable: ? (IMPORTANT!)
?? Animated: ? (leave unchecked)
?? Rigged: ? (leave unchecked)

Under "License" section:
?? CC BY: ? (can use with attribution)
?? CC0: ? (can use without attribution)

These filters show only free, downloadable, game-ready buildings!
```

**3. Browse Results:**
```
Scroll through thumbnails

Look for:
? Buildings with textures (colorful thumbnails)
? "PBR" in title (good quality materials)
? Low polygon count (check description)
? Clean, professional look

Avoid:
? Very detailed/realistic (too many polygons)
? "For rendering" in description
? No textures (gray models)
```

---

### **Step 3: Download Buildings (5 minutes per building)**

**For Each Building:**

**1. Click on Building Thumbnail:**
```
Opens the 3D viewer page
You can rotate the model to preview it
```

**2. Check License:**
```
Bottom right of page:

License shown:
?? CC BY = FREE (give credit in game credits)
?? CC0 = FREE (no credit needed)
?? Standard = Need to ask permission (avoid these)

Only download CC BY or CC0!
```

**3. Click Download Button:**
```
Right side of page: "Download 3D Model" button

If you see "Login to Download":
- Sign in with account you created
- Then click Download again
```

**4. Select Format:**
```
Download options appear:

Format dropdown:
Select: "Autoconverted format (FBX)"

FBX is best for Unreal Engine!

Click "Download" button
```

**5. Save File:**
```
Browser downloads ZIP file

Default location:
C:\Users\FlavorGood\Downloads\

File name like:
"building_model_1234.zip"

Let it complete download (5-30 seconds)
```

**6. Extract ZIP:**
```
Go to Downloads folder

Right-click ZIP file:
- Extract All...
- Or use 7-Zip / WinRAR

Creates folder with:
?? model.fbx (the 3D model)
?? textures folder
?  ?? diffuse.jpg
?  ?? normal.jpg
?  ?? etc...
?? readme.txt (license info)
```

---

### **Step 4: Rename for Better Categorization (2 minutes)**

**Before importing to Unreal:**

```
Rename the .fbx file with descriptive names:

Bad names (from download):
?? "model.fbx"
?? "building_3456.fbx"
?? "download.fbx"

Good names (for auto-categorization):
?? "urban_building_abandoned_01.fbx"
?? "warehouse_industrial_02.fbx"
?? "factory_building_03.fbx"
?? "brick_building_modern_04.fbx"
?? "concrete_building_05.fbx"

Keywords that help categorization:
?? "urban" ? Urban buildings
?? "abandoned" ? Abandoned category
?? "industrial" / "warehouse" / "factory" ? Industrial
?? "brick" / "concrete" ? Material type
?? "modern" / "old" ? Style
?? "building" ? Identifies as building

System reads filename to auto-categorize!
```

---

### **Step 5: Import to Unreal (5 minutes per building)**

**1. Open Unreal Editor:**
```
Double-click: Frontline.uproject
Wait for editor to load
```

**2. Create Buildings Folder:**
```
Content Browser (bottom panel):

1. Navigate to Content/

2. Right-click in empty space

3. New Folder

4. Name: Buildings

5. Press Enter

6. Double-click to open Buildings folder
```

**3. Import FBX File:**
```
In Content Browser (Buildings folder open):

1. Right-click in empty space

2. Click "Import to /Game/Buildings/..."

3. File browser opens

4. Navigate to:
   C:\Users\FlavorGood\Downloads\[extracted folder]/

5. Select the .fbx file
   (e.g., "urban_building_abandoned_01.fbx")

6. Click "Open"

7. Import Options dialog appears
```

**4. Configure Import Settings:**
```
Import Options dialog:

Mesh:
?? Import Mesh: ? (checked)
?? Skeletal Mesh: ? (unchecked - we want static)
?? Import as Skeletal: ? (unchecked)
?? Auto Generate Collision: ? (checked - important!)

Materials:
?? Import Materials: ? (checked)
?? Import Textures: ? (checked)

Advanced:
?? Combine Meshes: ? (usually unchecked)
?? Use T0 as Ref Pose: ? (unchecked)

Bottom:
Click "Import All" button
```

**5. Wait for Import:**
```
Progress bar shows import

Takes 5-30 seconds depending on model size

Console (Output Log) shows:
"Import successful"
"Created asset: SM_[building name]"
```

**6. Verify Import:**
```
Content Browser shows new assets:

Buildings folder now contains:
?? SM_urban_building_abandoned_01 (StaticMesh)
?? M_building_material (Material)
?? T_building_texture_* (Textures)

Double-click the StaticMesh to preview it
```

---

### **Step 6: Test in Level (2 minutes)**

**1. Drag Building into Viewport:**
```
In Content Browser:
- Click on SM_[building name]
- Hold left mouse button
- Drag into 3D viewport
- Release to place

Building appears in level!
```

**2. Move and Position:**
```
Select building (click on it)

Move: Press W key
- Drag arrows to move
- Red = X, Green = Y, Blue = Z

Rotate: Press E key
- Drag arcs to rotate

Scale: Press R key
- Drag to make bigger/smaller

Position building nicely in level
```

**3. Test Success:**
```
Press Play button (or Alt+P)

Walk around and see your building!

It works! ??
```

---

### **Step 7: Repeat for More Buildings (15 minutes)**

**Download 5-10 Buildings:**

```
Back to Sketchfab:

Search different terms:
1. "abandoned building" ? Download 2
2. "warehouse" ? Download 2
3. "factory building" ? Download 1
4. "brick building" ? Download 2
5. "concrete building" ? Download 2

Total: ~10 buildings
Time: 30-45 minutes
Result: Good starter library!
```

---

### **Step 8: Scan Asset Library (2 minutes)**

**1. Open Asset Library:**
```
Content Browser:

Navigate to: Content/Data/

Double-click: DA_AssetLibrary
(If you created it earlier)
```

**2. Add Scan Path:**
```
In DA_AssetLibrary details:

Scan Paths section:
- Click + button
- Type: /Game/Buildings/
- Press Enter
```

**3. Scan Buildings:**
```
Click button: "Scan And Populate Library"

Output Log shows:
???????????????????????????????????????
SCANNING ASSET LIBRARY
???????????????????????????????????????
Scanning: /Game/Buildings/ (10 assets)
  + urban_building_abandoned_01
    Category: Building_Urban_Abandoned ?
    Biomes: [Urban] ?
  + warehouse_industrial_02
    Category: Building_Urban_Industrial ?
    Biomes: [Urban] ?
  ...
???????????????????????????????????????
SCAN COMPLETE
Total Assets: 10
Meshes: 10
???????????????????????????????????????
```

**4. Verify Categories:**
```
In DA_AssetLibrary:

Expand "Assets" array

Each entry shows:
?? Asset Name
?? Category (auto-detected from filename!)
?? Biomes (auto-detected!)
?? Type: StaticMesh
?? Auto Detected: True ?

Perfect categorization with zero manual work!
```

---

## **?? COMPLETE CHECKLIST:**

**Before Starting:**
- [ ] Have web browser
- [ ] Have Unreal Editor installed
- [ ] Have internet connection
- [ ] 30-60 minutes available

**Getting Buildings:**
- [ ] Go to Sketchfab.com
- [ ] Create free account
- [ ] Search "low poly building"
- [ ] Apply filters (Downloadable, License)
- [ ] Download 5-10 buildings (FBX format)
- [ ] Extract ZIP files
- [ ] Rename FBX files with keywords

**Importing to Unreal:**
- [ ] Open Unreal Editor
- [ ] Create /Game/Buildings/ folder
- [ ] Import each FBX file
- [ ] Configure import settings
- [ ] Verify imports successful
- [ ] Test drag into level

**Setting Up Library:**
- [ ] Open DA_AssetLibrary
- [ ] Add /Game/Buildings/ to scan paths
- [ ] Click "Scan And Populate Library"
- [ ] Verify buildings detected
- [ ] Check auto-categorization worked

---

## **?? RECOMMENDED FIRST DOWNLOADS:**

**Starter Pack (10 Buildings):**

```
Download these search terms from Sketchfab:

1-2. "abandoned factory building"
?? Rename: urban_building_abandoned_01.fbx
?? Rename: factory_abandoned_02.fbx

3-4. "warehouse industrial"
?? Rename: warehouse_industrial_01.fbx
?? Rename: warehouse_industrial_02.fbx

5-6. "brick building"
?? Rename: brick_building_modern_01.fbx
?? Rename: brick_building_old_02.fbx

7-8. "concrete building"
?? Rename: concrete_building_01.fbx
?? Rename: urban_building_modern_02.fbx

9. "factory building"
?? Rename: factory_building_industrial_01.fbx

10. "office building"
?? Rename: office_building_modern_01.fbx

Total Download: ~300-500 MB
Total Time: 30-45 minutes
Perfect starter library!
```

---

## **?? PRO TIPS:**

### **Finding Best Quality:**

**On Sketchfab, look for:**
```
? "PBR" in title (physically-based rendering)
? "Game Ready" tag
? "Low Poly" or under 50,000 triangles
? Has textures (colorful preview)
? CC BY or CC0 license
? Recent upload date (2020+)
? Good ratings/likes

Avoid:
? "High Poly" or over 100k triangles
? "For Rendering" or "Not for games"
? Gray/untextured
? Standard license (need permission)
? Very old models (2015 or earlier)
```

### **Batch Download:**

```
Tips to speed up:
1. Open multiple tabs
2. Find 5-10 buildings you like
3. Download all at once
4. Extract all ZIPs
5. Rename all FBX files
6. Import all together to Unreal

Saves time!
```

### **Quality Check Before Import:**

```
After extracting ZIP:

Check folder contains:
?? .fbx file ? (the model)
?? textures folder ?
?  ?? diffuse/albedo ? (color)
?  ?? normal ? (detail)
?  ?? roughness/metallic ? (material)
?? readme.txt (license)

If missing textures:
- Model will be gray in Unreal
- Still works, but needs material
- Look for other downloads with textures
```

---

## **?? TROUBLESHOOTING:**

### **Problem: Download button says "Login"**

**Solution:**
```
You need a Sketchfab account (free):
1. Top right: "Sign Up"
2. Use Google/Facebook/Email
3. Confirm email if needed
4. Go back to model
5. Download button now works
```

### **Problem: Can't find FBX format**

**Solution:**
```
In download options:
1. Look for "Original Format"
2. OR "Autoconverted format"
3. Select FBX from dropdown
4. If no FBX option, skip that model
5. Find a different building
```

### **Problem: Import fails in Unreal**

**Solution:**
```
Common causes:
1. File corrupted ? Re-download
2. Wrong format ? Make sure it's FBX not OBJ
3. Too complex ? Find simpler model
4. Missing plugin ? Usually not the issue

Try:
- Different building from Sketchfab
- Check file size (keep under 100 MB)
- Make sure extracted from ZIP first
```

### **Problem: Building has no textures (gray)**

**Solution:**
```
1. Check if textures folder was in ZIP
2. If yes, import textures separately:
   - Content Browser ? Right-click
   - Import to /Game/Buildings/Textures/
   - Browse to texture folder
   - Import all .jpg/.png files

3. Apply to material:
   - Open M_building_material
   - Drag textures into material editor
   - Connect to Base Color, Normal, etc.
   - Save material

4. Or find a different model with better textures
```

### **Problem: Building too big/small in game**

**Solution:**
```
1. Select building in viewport
2. Press R key (scale mode)
3. Type scale value:
   - 0.1 = 10x smaller
   - 0.5 = 2x smaller
   - 2.0 = 2x bigger
   - 10.0 = 10x bigger

4. Or re-import with Transform settings:
   - Import options ? Transform
   - Set import scale (0.1 to 100)
```

---

## **?? TIME BREAKDOWN:**

```
Create Sketchfab account: 2 minutes
Find 5 buildings: 5 minutes
Download 5 buildings: 10 minutes
Extract & rename: 5 minutes
Import to Unreal: 15 minutes (3 min each)
Test in level: 3 minutes
Scan library: 2 minutes
??????????????????????????
TOTAL: 42 minutes

Result: 5 working buildings in your project!
```

---

## **?? DO THIS RIGHT NOW:**

**30-Minute Quick Start:**

```
STEP 1 (5 min): Sketchfab Setup
?? Go to sketchfab.com
?? Sign up (Google login fastest)
?? Search "low poly building"

STEP 2 (10 min): Download 3 Buildings
?? Find 3 you like
?? Download FBX format
?? Extract ZIPs
?? Rename files

STEP 3 (10 min): Import to Unreal
?? Open Unreal Editor
?? Create /Game/Buildings/ folder
?? Import 3 FBX files
?? Verify successful

STEP 4 (5 min): Test & Scan
?? Drag one into level
?? Open DA_AssetLibrary
?? Add /Game/Buildings/ to scan
?? Click Scan
?? See auto-categorization!

DONE! Working buildings in 30 minutes!
```

---

## **? SUCCESS CRITERIA:**

**You're successful when:**

- [ ] You can access Sketchfab
- [ ] Downloaded 3+ buildings (FBX format)
- [ ] Imported to /Game/Buildings/ in Unreal
- [ ] Can drag building into level and see it
- [ ] Buildings appear in DA_AssetLibrary scan
- [ ] Categories auto-assigned correctly
- [ ] Can test in Play mode

---

## **?? USEFUL LINKS:**

**Sketchfab:**
- Main site: https://sketchfab.com
- Buildings: https://sketchfab.com/search?q=building&type=models
- Low poly: https://sketchfab.com/search?q=low+poly+building
- Game ready: https://sketchfab.com/search?q=game+ready+building

**Other Free Sites (Backup):**
- CGTrader: cgtrader.com/free-3d-models
- Free3D: free3d.com
- TurboSquid: turbosquid.com/Search/3D-Models/free

---

**START NOW: Go to Sketchfab.com and download your first building! ??**

**This is the most reliable method without Marketplace access!**

**You'll have buildings in 30 minutes guaranteed! ??**
