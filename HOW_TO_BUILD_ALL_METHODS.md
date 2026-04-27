# ?? **HOW TO BUILD - ALL METHODS**

## **? QUICK BUILD (Easiest):**

### **Method 1: Visual Studio (Recommended)**
```
1. Make sure Unreal Editor is CLOSED
2. Open Visual Studio
3. Press F7 (or Build ? Build Solution)
4. Wait for "Build succeeded"
```

---

## **?? ALTERNATIVE METHODS:**

### **Method 2: From Unreal Editor**
```
1. Open Frontline.uproject (double-click it)
2. Editor will auto-compile on startup
3. Wait for "Compiling..." to finish
4. Press Play when ready
```

### **Method 3: Right-Click Project File**
```
1. Find Frontline.uproject in Windows Explorer
2. Right-click on it
3. Select "Generate Visual Studio project files"
4. Wait for completion
5. Open Frontline.sln in Visual Studio
6. Press F7 to build
```

### **Method 4: PowerShell (Correct Syntax)**
```powershell
# Run these commands one at a time:

# Step 1: Navigate to project folder
Set-Location "C:\Users\FlavorGood\Documents\Unreal Projects\Frontline"

# Step 2: Run build
& "D:\UE_5.7\Engine\Build\BatchFiles\Build.bat" FrontlineEditor Win64 Development "-Project=C:\Users\FlavorGood\Documents\Unreal Projects\Frontline\Frontline.uproject"
```

### **Method 5: Command Prompt (Not PowerShell)**
```cmd
cd /d "C:\Users\FlavorGood\Documents\Unreal Projects\Frontline"
"D:\UE_5.7\Engine\Build\BatchFiles\Build.bat" FrontlineEditor Win64 Development -Project="C:\Users\FlavorGood\Documents\Unreal Projects\Frontline\Frontline.uproject"
```

---

## **? COMMON ERRORS & FIXES:**

### **Error: "Build failed - Editor is running"**
```
Solution:
1. Close Unreal Editor COMPLETELY
2. Check Task Manager (Ctrl+Shift+Esc)
3. End any "UnrealEditor.exe" processes
4. Try building again
```

### **Error: "Unable to build while Live Coding is active"**
```
Solution:
Same as above - close the editor!
```

### **Error: PowerShell syntax error (&&)**
```
Solution:
Don't use && in PowerShell!
Use ; instead, or run commands separately
Or use Command Prompt (cmd) instead
```

---

## **? WHAT'S BEING BUILT:**

When you build, you're compiling:
- ? All your C++ code changes
- ? 719 environmental objects system
- ? Gravity fix (GravityScale = 1.0)
- ? Smaller barrier (0.25km)
- ? Trees, buildings, props, lights
- ? All game systems

---

## **?? EXPECTED BUILD TIME:**

- **First build:** 5-10 minutes (compiling everything)
- **Incremental builds:** 1-3 minutes (only changed files)
- **Clean rebuild:** 5-10 minutes (recompile all)

---

## **?? AFTER BUILD SUCCEEDS:**

1. **Open Frontline.uproject**
2. **Press Alt+P** to play
3. **You should see:**
   - 200 trees
   - 50 buildings
   - 150 rocks
   - 100 crates
   - 30 vehicles
   - 80 cover objects
   - 40 street lights
   - 60 barrels
   - Normal gravity (not floaty)
   - Smaller barrier (250m wide)

---

## **?? BUILD OUTPUT TO CHECK:**

### **Success looks like:**
```
========== Build: 52 succeeded, 0 failed, 1 skipped ==========
Result: Succeeded
Total execution time: XXX.XX seconds
```

### **Failure looks like:**
```
========== Build: XX succeeded, 1 failed, 1 skipped ==========
Result: Failed
Errors: [error messages]
```

---

## **?? TROUBLESHOOTING:**

### **Build Keeps Failing?**
1. Make sure editor is closed
2. Delete these folders:
   - `Binaries`
   - `Intermediate`
   - `Saved`
3. Right-click Frontline.uproject
4. Select "Generate Visual Studio project files"
5. Open Frontline.sln
6. Build ? Rebuild Solution

### **Still Having Issues?**
Try a clean rebuild:
```
Visual Studio ? Build ? Clean Solution
Then: Build ? Rebuild Solution
```

---

## **?? CHECKLIST BEFORE BUILDING:**

```
? Unreal Editor is CLOSED
? No UnrealEditor.exe in Task Manager
? Visual Studio has Frontline.sln open
? You're on "Development Editor" configuration
? You saved all your files (Ctrl+Shift+S)
```

---

## **?? RECOMMENDED BUILD METHOD:**

**Use Visual Studio (Method 1):**
1. ? Easiest
2. ? Shows errors clearly
3. ? Fastest
4. ? Best debugging
5. ? Most reliable

**Just press F7!**

---

## **?? BUILD CONFIGURATIONS:**

### **Development Editor (Use This):**
- For testing in editor
- Has debug symbols
- Best for development

### **DebugGame Editor:**
- More debug info
- Slower performance
- Only use for deep debugging

### **Shipping:**
- Final release build
- No debug info
- Maximum performance
- Don't use for testing

**Always use "Development Editor" for now!**

---

## **?? SUMMARY:**

**Easiest way to build:**
1. Close Unreal Editor
2. Open Visual Studio
3. Press F7
4. Wait
5. Done!

**That's it!** ???
