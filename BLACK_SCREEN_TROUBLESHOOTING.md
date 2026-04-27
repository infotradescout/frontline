# ?? **BLACK SCREEN FIX - STEP BY STEP**

## **?? THE PROBLEM:**

Your logs show everything is working:
- ? Map generated (terrain, buildings, lights)
- ? Lighting created (Brightness: 10.0)
- ? Spawn points created
- ? Camera system added to character

**But the screen is still black!**

## **?? POSSIBLE CAUSES:**

1. **Viewport is in "Unlit" mode** (most common)
2. **Editor viewport settings**
3. **Camera not activating in PIE**
4. **Exposure settings**

---

## **? FIX 1: CHECK VIEWPORT MODE (Do This First!)**

### **Before Pressing Play:**

1. **Look at the top-left of the viewport**
2. **Find the dropdown that says "Lit"** (or might say "Unlit")
3. **Click it**
4. **Select "Lit"**
5. **Now press Play (Alt+P)**

```
Top-left corner:
???????????????????
? [Lit ?]        ?  ? Click here!
? Perspective ?  ?
???????????????????

Make sure it says "Lit" not:
? Unlit
? Wireframe  
? Detail Lighting
? Lighting Only
```

---

## **? FIX 2: EDITOR VIEWPORT SETTINGS**

If Fix 1 didn't work:

1. **In the editor (not PIE)**
2. **Top menu ? Window ? Developer Tools ? Output Log**
3. **Keep Output Log visible**
4. **Press Play (Alt+P)**
5. **Check Output Log for:**

```
? Should see:
[Frontline] ? Directional light created (Brightness: 10.0)
[Frontline] ? Sky light created (Intensity: 1.5)
PIE: Server logged in
PIE: Play in editor total start time X.XXX seconds

? Should NOT see:
Errors about lighting
Errors about camera
Errors about pawn spawning
```

---

## **? FIX 3: VERIFY CAMERA IS ACTIVE**

While playing (screen is black):

1. **Press F8** (this ejects you from the pawn)
2. **Can you now see the scene?**

### **If YES (you can see after pressing F8):**
**Problem:** Camera isn't activating correctly

**Solution:**
1. Stop playing
2. Open **AFRCharacter** Blueprint (or check C++ code)
3. Make sure **FollowCamera** component exists
4. Make sure **CameraBoom** component exists
5. Make sure **FollowCamera** is attached to **CameraBoom**

### **If NO (still black after F8):**
**Problem:** Lighting or rendering issue

**Solution:** Continue to Fix 4

---

## **? FIX 4: PROJECT SETTINGS CHECK**

1. **Edit ? Project Settings**
2. **Engine ? Rendering**

### **Check these settings:**

```
? Dynamic Global Illumination Method: Lumen (or Screen Space)
? Reflection Method: Lumen (or Screen Space)
? Allow Static Lighting: OFF (unchecked)

Exposure:
? Apply Pre-Exposure before writing to the scene color: ON
? Extend default luminance range in Auto Exposure settings: ON
```

3. **Click "Restart Editor" if you changed anything**
4. **Reopen and test**

---

## **? FIX 5: MANUAL LIGHT TEST**

Let's test if any light works at all:

1. **Open FrontlineMap in editor** (not PIE)
2. **World Outliner ? Search for "DirectionalLight"**
3. **Click on it**
4. **Details Panel ? Light:**
   - Intensity: **10.0** (increase if needed)
   - Light Color: **White**
   - Visible: **ON** (checkmark)
5. **Press Alt+P to play**

### **Still black?**

Try adding a **Point Light** right where the player spawns:

1. **Place Actors panel ? Lights ? Point Light**
2. **Drag into viewport**
3. **Move it to player spawn location** (around 0,0,200)
4. **Set Intensity to 10000.0** (yes, ten thousand!)
5. **Press Play**

**If you can see the light:** Lighting works, camera might be the issue
**If still black:** Continue to Fix 6

---

## **? FIX 6: CAMERA ACTIVATION IN C++**

Let me verify the camera is active. Check this in your character:

### **In AFRCharacter.cpp, BeginPlay:**

Add this debug code temporarily:

```cpp
void AFRCharacter::BeginPlay() {
	Super::BeginPlay();
	
	// Debug camera
	if (FollowCamera)
	{
		UE_LOG(LogTemp, Warning, TEXT("Camera exists!"));
		FollowCamera->SetActive(true); // Force activate
		
		if (APlayerController* PC = Cast<APlayerController>(GetController()))
		{
			PC->SetViewTarget(this);
			UE_LOG(LogTemp, Warning, TEXT("View target set!"));
		}
	}
	else
	{
		UE_LOG(LogTemp, Error, TEXT("NO CAMERA COMPONENT!"));
	}
	
	// ... rest of your code
}
```

**Rebuild and test.** Check Output Log for the warnings.

---

## **? FIX 7: VIEWPORT EXPOSURE**

The scene might be overexposed or underexposed:

### **While playing (PIE):**

1. **Press ~ (tilde) to open console**
2. **Type:** `r.DefaultFeature.AutoExposure 0`
3. **Press Enter**
4. **Type:** `r.Tonemapper.GrainIntensity 0`
5. **Press Enter**

**Can you see anything now?**

### **If yes:**
Exposure settings were wrong. Fix permanently:

1. **Stop playing**
2. **Edit ? Project Settings ? Engine ? Rendering**
3. **Default Settings:**
   - Extend default luminance range in Auto Exposure settings: **ON**
4. **Save and restart editor**

---

## **? FIX 8: EMERGENCY SUPER BRIGHT TEST**

Let's make EVERYTHING bright:

### **In editor console (not PIE), type:**

```
r.SetRes 1280x720w
r.BloomQuality 0
r.DepthOfFieldQuality 0
r.MotionBlurQuality 0
r.LightFunctionQuality 0
r.ShadowQuality 0
r.Tonemapper.GrainIntensity 0
r.SceneColorFormat 4
r.PostProcessAAQuality 0
```

**Then press Alt+P**

---

## **? FIX 9: CHECK IF MESH IS BLOCKING CAMERA**

The character mesh might be in front of the camera:

1. **While playing (screen black)**
2. **Press ~ (console)**
3. **Type:** `Camera`
4. **Look for current camera location**

Or try:

1. **Stop playing**
2. **Open AFRCharacter.cpp**
3. **In constructor, change:**

```cpp
CameraBoom->TargetArmLength = 300.0f;
// Change to:
CameraBoom->TargetArmLength = 1000.0f; // Much farther back
```

**Rebuild and test**

---

## **?? MOST LIKELY FIX:**

Based on your issue, **Fix 1** (Viewport Mode) is 99% likely to be the problem.

### **Quick Test:**

1. **Close PIE if playing**
2. **Look at top-left of viewport**
3. **Click the dropdown**
4. **Select "Lit"**
5. **Press Alt+P**

**You should see everything now!**

---

## **?? WHAT YOU SHOULD SEE WHEN FIXED:**

```
? Bright environment
? Terrain (natural hills and valleys)
? Buildings (105 buildings)
? Sky with clouds
? Water bodies
? Ground with textures
? Your character (capsule)
? Can move (WASD)
? Can look around (mouse)
```

---

## **?? IF NOTHING WORKS:**

1. **Send me your Output Log** (the full log when you press Play)
2. **Take a screenshot** of:
   - The black screen
   - Top-left viewport mode dropdown
   - World Outliner showing DirectionalLight
3. **Try creating a NEW map:**
   - File ? New Level ? Empty Level
   - Place Actors ? Light ? Directional Light
   - Place Actors ? Light ? Sky Light
   - Place Actors ? Basic ? Player Start
   - Press Play
   - **Can you see the grid?**

---

## **?? DEBUGGING CHECKLIST:**

```
? Viewport mode is "Lit" (not Unlit)
? Output Log shows lighting created
? Output Log shows no errors
? Camera components exist in AFRCharacter
? DefaultPawnClass is AFRCharacter
? Project settings: Allow Static Lighting = OFF
? Project settings: DGI Method = Lumen
? F8 eject test (can see scene when ejected?)
? Console command: r.DefaultFeature.AutoExposure 0
? Directional Light intensity = 10.0
```

---

**START WITH FIX 1 - IT'S ALMOST ALWAYS THE VIEWPORT MODE!** ???

The viewport mode "Unlit" shows everything as black because it removes all lighting calculations!
