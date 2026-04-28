# Day 1 Exact Setup

Use this in order. Do not skip steps.

## 1. Create the project

In Unreal Engine:

- Games -> First Person -> Blueprint -> Desktop/Console -> Maximum Quality -> No Starter Content

Why:

- First Person saves weeks
- Blueprint gives fastest iteration
- No Starter Content avoids project bloat

## 2. Apply critical rendering settings immediately

Go to:

- Edit -> Project Settings -> Rendering

Turn ON:

- Forward Shading = True

Turn OFF:

- Lumen Global Illumination
- Lumen Reflections
- Virtual Shadow Maps
- Nanite (for now)

Why:

- Forward rendering is cheaper and faster for FPS gameplay
- Cinematic features are deferred until the game loop is stable

## 3. Set scalability baseline to low

Go to:

- Top right -> Settings -> Scalability

Set all quality groups to:

- Low

Why:

- This is your default performance mode baseline
- You are designing for weak PCs first

## 4. Cap editor performance

Go to:

- Edit -> Editor Preferences -> Performance

Set:

- Limit Editor Framerate = 60

Turn OFF:

- Realtime viewport (clock icon in viewport)

Why:

- Prevents background GPU/CPU burn while building systems
- Keeps development smooth and stable

## 5. Create the first map (minimal only)

Go to:

- File -> New Level -> Empty Level

Add only:

- Floor (scaled cube)
- One directional light
- One sky light
- Player spawn

Do not add anything else today.

## 6. Lock rendering philosophy

Non-negotiable rules for this project:

- Simple lighting
- Low poly
- Minimal shadows
- No heavy post-processing

## 7. Build the first system only

Today you only build this:

- Can I move and shoot?

Checklist:

- WASD movement
- Mouse look
- Shoot (line trace)
- Hit detection

If this works, Day 1 is a success.

## Day 1 KPI (win condition)

You can:

- Load the map
- Move around
- Shoot something
- See hit feedback

Nothing else matters on Day 1.

## Do not touch today

- Procedural generation
- Multiplayer
- Bots
- UI
- Inventory
- Asset shopping
- AI tools

## Why this setup is correct

- Forward rendering reduces cost and complexity
- Scalability tiers let you scale up later safely
- Unreal defaults are too heavy for low-end targets
- Most projects fail by starting high-end first

## Expected Day 1 outcome

If correct:

- Smooth editor
- Stable FPS
- No major spikes
- Clean scene and clear direction

If wrong:

- Stutter
- GPU spikes
- Heat/noise
- Scope confusion

## Tomorrow (not today)

- Day 2: damage system + basic enemy
- Day 3: procedural cover generation

## Hard truth

Success is not building fast.

Success is building a game that stays fast, simple, and maintainable.
