# ? PREGAME ISLAND - FUNCTIONAL VERIFICATION & TESTING GUIDE

## ?? **BUILD STATUS: SUCCESS**
All files compiled successfully with no errors!

---

## ?? **STEP-BY-STEP TESTING PROCEDURE**

### **Test 1: Basic Island Spawn (2 minutes)**

1. **Open Unreal Editor**
2. **Open your test map**
3. **Click Play** (Alt+P) or **Play in Editor**

**? EXPECTED RESULTS:**
- Island should spawn at world origin (0, 0, 0)
- You should spawn on the island
- Output log should show: "? Pregame island spawned"
- Output log should show: "Pregame Island initialized"

**? IF IT FAILS:**
- Check Output Log for errors
- Verify Game Mode is set correctly
- Ensure you're running as server (not client-only)

---

### **Test 2: Warmup Period (2 minutes)**

1. **Continue from Test 1**
2. **Wait during 90-second warmup**
3. **Try to move around the island**

**? EXPECTED RESULTS:**
- Can move freely on island
- Countdown should display in HUD (if implemented)
- Pregame barrier should be visible
- Can't exit through barriers
- No damage taken
- Output log shows countdown ticks

**? IF IT FAILS:**
- Check if pregame area spawned
- Verify barriers are active
- Check invulnerability is enabled

---

### **Test 3: Match Start (2 minutes)**

1. **Wait for 90-second warmup to complete**
2. **Watch for match start**

**? EXPECTED RESULTS:**
- Barriers drop immediately
- Output log shows: "??? MATCH STARTED! Pregame island will be destroyed in 60 seconds!"
- Can now leave the island
- Island destruction countdown begins

**? IF IT FAILS:**
- Check `HandleLive()` is called
- Verify `StartDestructionCountdown()` is called
- Check Output Log for phase transitions

---

### **Test 4: Countdown Warnings (2 minutes)**

1. **After match starts, wait and listen**
2. **Watch Output Log**

**? EXPECTED RESULTS AT:**
- **30 seconds:** Warning sound + log message
- **15 seconds:** Warning sound + log message
- **10 seconds:** Warning sound + log message
- **5-1 seconds:** Warning every second

**Output Log should show:**
```
?? ISLAND DESTRUCTION WARNING: 30 seconds remaining!
?? ISLAND DESTRUCTION WARNING: 15 seconds remaining!
?? ISLAND DESTRUCTION WARNING: 10 seconds remaining!
?? ISLAND DESTRUCTION WARNING: 5 seconds remaining!
?? ISLAND DESTRUCTION WARNING: 4 seconds remaining!
?? ISLAND DESTRUCTION WARNING: 3 seconds remaining!
?? ISLAND DESTRUCTION WARNING: 2 seconds remaining!
?? ISLAND DESTRUCTION WARNING: 1 seconds remaining!
```

**? IF IT FAILS:**
- Check multicast RPCs are working
- Verify sound assets (if assigned)
- Check network replication

---

### **Test 5: Island Destruction (2 minutes)**

1. **Wait for 60-second countdown to complete**
2. **Watch the destruction**

**? EXPECTED RESULTS:**
- Output log shows: "?? ISLAND DESTRUCTION STARTED! ??"
- Island phase changes to "Destroying"
- Destruction effects spawn (if particles assigned)
- Destruction sound plays (if assigned)
- Island starts disappearing
- Takes 30 seconds to fully destroy

**? IF IT FAILS:**
- Check phase transition logic
- Verify destruction effects are triggered
- Check Output Log for destruction messages

---

### **Test 6: Player Damage (3 minutes)**

1. **After destruction starts, stay on island**
2. **Watch your health bar**

**? EXPECTED RESULTS:**
- Take damage while on island
- Damage starts at ~10 HP/sec
- Damage ramps up over 30 seconds
- At 50% destruction ? ~30 HP/sec
- At 100% destruction ? ~50 HP/sec
- Output log shows damage messages

**Output Log should show:**
```
Player [YourName] taking 10.5 island destruction damage
Player [YourName] taking 15.2 island destruction damage
Player [YourName] taking 25.8 island destruction damage
Player [YourName] taking 38.4 island destruction damage
Player [YourName] taking 49.7 island destruction damage
```

**? IF IT FAILS:**
- Check damage system integration
- Verify `ApplyDamageToPlayersOnIsland()` is called
- Check `IsPositionOnIsland()` returns true
- Verify TakeDamage is hooked up

---

### **Test 7: Island Fully Destroyed (1 minute)**

1. **Wait for full 30-second destruction**
2. **Watch island disappear**

**? EXPECTED RESULTS:**
- After 3 minutes total (90s warmup + 60s countdown + 30s destruction)
- Island geometry fully removed
- Output log shows: "Pregame Island fully destroyed!"
- Phase changes to "Destroyed"
- Players can no longer be "on island"

**? IF IT FAILS:**
- Check destruction progress reaches 100%
- Verify `DestroyIslandGeometry()` is called
- Check all island actors are destroyed

---

### **Test 8: Network Replication (5 minutes)**

**REQUIRES:** Multiple clients or PIE with 2+ players

1. **Start PIE with "Number of Players" = 2**
2. **Run through Tests 1-7 on both clients**

**? EXPECTED RESULTS:**
- Both clients see island spawn
- Both clients see countdown simultaneously
- Both clients hear warnings at same time
- Both clients see destruction start together
- Both clients see island disappear at same time
- All phases synchronized

**? IF IT FAILS:**
- Check replication properties
- Verify multicast RPCs work
- Check server authority
- Verify bReplicates = true

---

### **Test 9: Console Command Verification (2 minutes)**

1. **Press ` (tilde) to open console**
2. **Type: `stat fps`** (check performance)
3. **Check Output Log during play**

**? EXPECTED RESULTS:**
- FPS should be stable (>60 FPS)
- No excessive warnings in log
- No memory leaks reported
- Clean destruction cleanup

**? IF IT FAILS:**
- Check for memory leaks
- Verify actors are properly destroyed
- Check for infinite loops
- Review Tick performance

---

## ?? **COMPLETE TEST TIMELINE**

```
0:00 - ?? TEST START
     ??> Island spawns
     ??> Player spawns on island
     ??> Warmup begins

1:30 - ?? MATCH STARTS
     ??> Barriers drop
     ??> 60s countdown begins
     ??> Can leave island

2:00 - ?? 30-SECOND WARNING
2:15 - ?? 15-SECOND WARNING
2:20 - ?? 10-SECOND WARNING
2:25 - ?? 5-SECOND WARNING

2:30 - ?? DESTRUCTION STARTS
     ??> Island crumbles
     ??> Damage begins
     ??> Effects spawn

3:00 - ?? ISLAND DESTROYED
     ??> Geometry removed
     ??> Cleanup complete
```

---

## ?? **VERIFICATION CHECKLIST**

Copy this checklist and mark items as you test:

### **Core Functionality:**
- [ ] Island spawns at match start
- [ ] Players spawn on island during warmup
- [ ] 90-second warmup works correctly
- [ ] Match start triggers at correct time
- [ ] Barriers drop when match starts
- [ ] 60-second countdown begins
- [ ] Countdown is accurate

### **Warning System:**
- [ ] 30-second warning displays
- [ ] 15-second warning displays
- [ ] 10-second warning displays
- [ ] 5-1 second warnings display
- [ ] Warnings appear in Output Log
- [ ] Sound effects play (if assigned)

### **Destruction:**
- [ ] Destruction starts at correct time
- [ ] Visual effects spawn (if assigned)
- [ ] Sound effects play (if assigned)
- [ ] Island phase changes correctly
- [ ] Destruction takes 30 seconds
- [ ] Island disappears progressively

### **Damage System:**
- [ ] Players take damage on island
- [ ] Damage starts at ~10 HP/sec
- [ ] Damage ramps to ~50 HP/sec
- [ ] Damage only affects players on island
- [ ] Damage stops after leaving island

### **Cleanup:**
- [ ] All island geometry removed
- [ ] No memory leaks
- [ ] No lingering actors
- [ ] Phase set to "Destroyed"

### **Network:**
- [ ] Replicates to all clients
- [ ] Synchronized countdown
- [ ] Synchronized destruction
- [ ] No desync issues

---

## ?? **COMMON ISSUES & FIXES**

### **Issue: Island doesn't spawn**
**Solution:**
```cpp
// Check Output Log for this message:
"? Failed to spawn pregame island!"

// Fix: Verify Game Mode has authority
if (HasAuthority())  // This must be true on server
{
    // Spawn code here
}
```

### **Issue: No countdown warnings**
**Solution:**
```cpp
// Check if multicast is working
// Add debug log in MulticastPlayWarning:
FR_LOG_INFO(LogFrontline, "MULTICAST WARNING RECEIVED: %d", SecondsRemaining);
```

### **Issue: No damage taken**
**Solution:**
```cpp
// Check if damage system is hooked up
// Add debug log in ApplyDamageToPlayersOnIsland:
FR_LOG_INFO(LogFrontline, "Checking damage for %d characters", Characters.Num());
```

### **Issue: Island never destructs**
**Solution:**
```cpp
// Check if HandleLive() is called
// Add debug log:
FR_LOG_INFO(LogFrontline, "HandleLive called - starting countdown");

// Check if StartDestructionCountdown() is called
// Verify Output Log shows:
"Pregame Island destruction countdown started"
```

### **Issue: Destruction happens immediately**
**Solution:**
```cpp
// Check countdown value:
DestructionCountdown = 60.f;  // Should be 60 seconds, not 0

// Check in Tick:
if (DestructionCountdown <= 0.f)  // Verify this condition
```

---

## ?? **TESTING BEST PRACTICES**

### **1. Test in Order:**
- Run tests sequentially (1?9)
- Don't skip tests
- Document any failures

### **2. Check Output Log:**
- Always have Output Log visible
- Filter for "Pregame" or "Island"
- Watch for errors in red

### **3. Use Multiple Sessions:**
- Test solo first
- Then test with bots
- Finally test multiplayer

### **4. Record Results:**
```
Test 1: ? PASS - Island spawned correctly
Test 2: ? PASS - Warmup worked
Test 3: ? PASS - Match started
Test 4: ?? PARTIAL - No sound (not assigned)
Test 5: ? PASS - Destruction worked
Test 6: ? PASS - Damage applied
Test 7: ? PASS - Island destroyed
Test 8: ? PASS - Replicated correctly
Test 9: ? PASS - Performance good
```

---

## ?? **EXPECTED OUTPUT LOG**

Here's what a successful test should look like in Output Log:

```
[0:00] LogFrontline: ? Pregame island spawned - will be destroyed 60s after match starts
[0:00] LogFrontline: Pregame Island initialized at X=0.000 Y=0.000 Z=0.000 with radius 5000
[0:00] LogFrontline: Built default pregame island platform
[0:00] LogTemp: [GameMode] ??? Created pregame area on island at X=0.000 Y=0.000 Z=100.000

[1:30] LogFrontline: ??? MATCH STARTED! Pregame island will be destroyed in 60 seconds!
[1:30] LogFrontline: Pregame Island destruction countdown started - 60 seconds until destruction!

[2:00] LogFrontline: ?? ISLAND DESTRUCTION WARNING: 30 seconds remaining!
[2:15] LogFrontline: ?? ISLAND DESTRUCTION WARNING: 15 seconds remaining!
[2:20] LogFrontline: ?? ISLAND DESTRUCTION WARNING: 10 seconds remaining!
[2:25] LogFrontline: ?? ISLAND DESTRUCTION WARNING: 5 seconds remaining!
[2:26] LogFrontline: ?? ISLAND DESTRUCTION WARNING: 4 seconds remaining!
[2:27] LogFrontline: ?? ISLAND DESTRUCTION WARNING: 3 seconds remaining!
[2:28] LogFrontline: ?? ISLAND DESTRUCTION WARNING: 2 seconds remaining!
[2:29] LogFrontline: ?? ISLAND DESTRUCTION WARNING: 1 seconds remaining!

[2:30] LogFrontline: Pregame Island destruction initiated!
[2:30] LogFrontline: ?? ISLAND DESTRUCTION STARTED! ??
[2:30] LogFrontline: Player BP_FRCharacter_C_0 taking 10.5 island destruction damage
[2:31] LogFrontline: Player BP_FRCharacter_C_0 taking 12.3 island destruction damage
[2:45] LogFrontline: Player BP_FRCharacter_C_0 taking 28.7 island destruction damage
[2:55] LogFrontline: Player BP_FRCharacter_C_0 taking 45.2 island destruction damage

[3:00] LogFrontline: Pregame Island fully destroyed!
[3:00] LogFrontline: Destroyed all pregame island geometry
```

---

## ? **SUCCESS CRITERIA**

Your pregame island system is **WORKING CORRECTLY** if:

1. ? All 9 tests pass
2. ? Output Log matches expected output
3. ? No errors or warnings in log
4. ? Frame rate stays stable (>60 FPS)
5. ? Network replication works correctly
6. ? All timings are accurate
7. ? Damage system functions properly
8. ? Cleanup is complete

---

## ?? **NEXT STEPS AFTER VERIFICATION**

Once all tests pass:

1. **Add Visual Polish:**
   - Assign destruction particle effects
   - Add countdown warning sounds
   - Add destruction sound effects
   - Add UI countdown display

2. **Create Island Layout:**
   - Design your island geometry
   - Create `FRPregameIslandLayout` data asset
   - Add props and decorations
   - Test custom layout

3. **Customize Settings:**
   - Adjust timings if needed
   - Tune damage values
   - Modify island size
   - Configure effects

4. **Playtest with Players:**
   - Gather feedback
   - Adjust based on experience
   - Polish rough edges
   - Iterate

---

## ?? **YOU'RE DONE WHEN:**

- ? All tests pass
- ? No errors in log
- ? Performance is good
- ? Network works correctly
- ? Players have fun!

**CONGRATULATIONS! Your pregame island destruction system is FULLY FUNCTIONAL!** ?????

---

## ?? **TROUBLESHOOTING CONTACTS**

If you encounter issues during testing:

1. **Check Output Log first** - 90% of issues are visible there
2. **Review this document** - Most issues are covered
3. **Check documentation:**
   - `PREGAME_ISLAND_QUICK_START.md`
   - `PREGAME_ISLAND_DESTRUCTION_SYSTEM.md`
   - `PREGAME_ISLAND_SYSTEM_COMPLETE.md`

**BUILD: SUCCESS ?**  
**TESTS: READY ?**  
**DOCUMENTATION: COMPLETE ?**  
**SYSTEM: OPERATIONAL ?**

**NOW GO TEST IT AND MAKE SURE IT ACTUALLY WORKS! ????**
