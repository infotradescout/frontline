# Create the Unreal Project — Plain-English Walkthrough

> No coding here. Just clicks. Follow exactly. Don't improvise.
> Time required: ~10 minutes (plus install time if you don't have UE 5.7.4 yet).

---

## Before you start

- ✅ You have Epic Games Launcher installed.
- ✅ You have Unreal Engine **5.7.4** installed (you said you do).
- ✅ This repo lives at: `D:\AAATraderCorner\TradeScout\Frontline\`
- ✅ The `UnrealProject\` folder inside it is currently empty.

---

## Step 1 — Open Epic Games Launcher

1. Open the **Epic Games Launcher** (Start menu → "Epic Games Launcher").
2. Left sidebar → click **Unreal Engine**.
3. Top tab → click **Library**.
4. Find **5.7.4** in your installed engines. Click the yellow **Launch** button.

A loading window appears. Wait. It can take 30–60 seconds.

---

## Step 2 — Project Browser opens

You'll see a window titled **Unreal Project Browser**.

### Top section: Recent / New Project

- Click **GAMES** (a category tab on the left).
- A grid of templates appears.
- Click the **First Person** template (it shows a hand holding a gun).
- Click the yellow **Next** button (bottom right).

---

## Step 3 — Project Defaults screen

This screen has 5 settings. **Set them EXACTLY as listed below. This matters.**

| Setting                | What to choose            | Why                                            |
|------------------------|---------------------------|------------------------------------------------|
| **Project Type**       | **Blueprint**             | We're not writing C++ yet                      |
| **Target Platform**    | **Desktop**               | PC only for now                                |
| **Quality Preset**     | **Scalable**              | Low-spec-first doctrine                        |
| **Starter Content**    | **OFF (unchecked)**       | We don't want Epic's filler assets             |
| **Raytracing**         | **OFF (unchecked)**       | Forbidden in Prototype 0.1                     |

If Unreal does **not** let you uncheck Starter Content (some template/version combinations lock it):

- Keep going. Create the project anyway.
- We'll remove Starter Content right after setup with one command.
- This is normal and does **not** break the plan.

---

## Step 4 — Project Location & Name

Bottom of the same screen:

1. **Project Location**: click the **`...`** browse button.
   - Navigate to: `D:\AAATraderCorner\TradeScout\Frontline\UnrealProject\`
   - Click **Select Folder**.
2. **Project Name**: type exactly: `Frontline`
   - (Capital F, no spaces, no version number.)

Bottom right → click yellow **Create**.

Unreal will now build the project. This takes **2–5 minutes**. The editor opens automatically when done.

---

## Step 5 — When the editor opens, DON'T TOUCH ANYTHING

A 3D viewport with a small room and some white blocks appears. There's a hand holding a gun in the play preview.

**Just close the editor.** File → Exit. Or click the X.

You'll see a "Save?" prompt. Click **Don't Save**.

> Why close it? Because we're going to drop our pre-built config files into the project folder *before* opening it again. That way, the engine reads our locked-down settings on the next launch instead of Epic's defaults.

---

## Step 6 — Run the setup script

1. Open **PowerShell** in the repo folder. Easiest way:
   - Open **File Explorer**.
   - Navigate to `D:\AAATraderCorner\TradeScout\Frontline\`
   - Click in the address bar at the top, type `powershell`, press **Enter**.
2. A blue PowerShell window appears, already in the right folder.
3. Type this and press Enter:

   ```powershell
   .\Tools\setup_unreal_project.ps1
   ```

4. The script will:
   - Confirm `UnrealProject\Frontline\Frontline.uproject` exists
   - Copy the locked rendering config into the project's `Config\` folder
   - Verify Git LFS is active
   - Show you what it did

5. If you see a green **"✅ Setup complete"** message, you're done.
6. If you see a red **"❌"** message, copy the error and tell me — I'll fix it.

### If Starter Content was forced ON

Run this extra command in the same PowerShell window:

```powershell
.\Tools\remove_starter_content.ps1
```

If you see **"✅ StarterContent removed"**, you are clean.

---

## Step 7 — Open the project ONE more time to verify

1. Go to `D:\AAATraderCorner\TradeScout\Frontline\UnrealProject\Frontline\`
2. Double-click **`Frontline.uproject`**.
3. Editor opens. You may see a "Convert Project" prompt — click **More Options → Convert in-place** (or just **Open**, since you're already on 5.7.4).
4. You may see a **"Shaders are recompiling"** progress bar at the bottom. Wait for it (~3–10 minutes the first time — this is the engine rebuilding everything for forward shading).
5. When it's done, hit **Play** (the green arrow at the top, or Alt+P).
6. You should be in a small white room. **WASD moves. Mouse looks. Left-click shoots a yellow ball.**

That's it. Day 1 KPI met.

---

## Step 8 — Tell me, and I'll commit

Once the play test works, just tell me **"it works"**. I'll commit and push the project skeleton with the message **"Initial UE5 low-spec-first foundation"**.

---

## What if something breaks

- **Editor crashes on launch** → Tell me. Likely a forward-shading shader compile issue I can fix in the config.
- **No First Person template visible** → Your engine install is missing the templates. Re-install from Epic Launcher with "Templates" enabled.
- **Script says "Frontline.uproject not found"** → You probably created it with a different name or in a different folder. Tell me the exact path you used.
- **Anything else** → Screenshot the error and tell me.

---

## What you should NOT do

- ❌ Don't browse the Marketplace / Fab.
- ❌ Don't import any assets.
- ❌ Don't try to "improve" the white room.
- ❌ Don't start a new Blueprint.
- ❌ Don't watch tutorials and copy random things in.

The room is ugly on purpose. The next phase is building the real systems on top of it. Stay disciplined.
