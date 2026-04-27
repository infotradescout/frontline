# ?? **CRASH FIX SCRIPT**

## **Run this to fix the crash:**

### **Step 1: Clean Project**
```
1. Close ALL instances of Unreal Editor
2. Close Visual Studio
3. Run this in PowerShell:
```

```powershell
# Navigate to project
cd "C:\Users\FlavorGood\Documents\Unreal Projects\Frontline\"

# Delete cache folders
Remove-Item -Path "Saved" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "Intermediate" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "DerivedDataCache" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path ".vs" -Recurse -Force -ErrorAction SilentlyContinue

Write-Host "? Cleaned project folders" -ForegroundColor Green
```

### **Step 2: Regenerate Project**
```
Right-click Frontline.uproject
? "Generate Visual Studio project files"
Wait for completion
```

### **Step 3: Build**
```
Open Frontline.sln in Visual Studio
Set configuration to: Development Editor | Win64
Press F7 (Build)
Wait for "Build succeeded"
```

### **Step 4: Launch Editor**
```
Double-click Frontline.uproject
Should open without crash!
```

---

## **If Still Crashes:**

### **Disable Web Browser:**

Edit `Config/DefaultEngine.ini`, add at end:
```ini
[WebBrowser]
bEnabled=false
```

This disables the web browser plugin (the thing that crashed).

---

## **Your Game Code is FINE!**

The crash is in Unreal's web browser, not your floating island code.
After cleaning and rebuilding, your game will work!

