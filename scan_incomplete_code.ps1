# ?? Quick Incomplete Code Scanner
# Run this in PowerShell from your project root

$projectRoot = "C:\Users\FlavorGood\Documents\Unreal Projects\Frontline\Source\Frontline"

Write-Host "?? SCANNING FOR INCOMPLETE CODE..." -ForegroundColor Yellow
Write-Host ""

# Count TODO comments
$todos = Get-ChildItem -Path $projectRoot -Recurse -Include *.cpp,*.h | Select-String -Pattern "TODO|FIXME|NOT IMPLEMENTED|STUB" -CaseSensitive:$false
$todoCount = ($todos | Measure-Object).Count

Write-Host "?? TODO/FIXME Comments: $todoCount" -ForegroundColor Cyan
if ($todoCount -gt 0) {
    Write-Host "   Top 10 files with TODOs:" -ForegroundColor Gray
    $todos | Group-Object Filename | Sort-Object Count -Descending | Select-Object -First 10 | ForEach-Object {
        Write-Host "   - $($_.Name): $($_.Count) TODOs" -ForegroundColor DarkGray
    }
}
Write-Host ""

# Find stub implementations
$stubs = Get-ChildItem -Path $projectRoot -Recurse -Filter *.cpp | Select-String -Pattern "Stub Implementation" -CaseSensitive:$false
$stubCount = ($stubs | Measure-Object).Count

Write-Host "?? Stub Implementation Files: $stubCount" -ForegroundColor Red
if ($stubCount -gt 0) {
    $stubs | ForEach-Object {
        Write-Host "   ? $($_.Filename)" -ForegroundColor Red
    }
}
Write-Host ""

# Find empty returns
$emptyReturns = Get-ChildItem -Path $projectRoot -Recurse -Filter *.cpp | Select-String -Pattern "return\s+(false|nullptr|0|TArray|FString\(\))" 
$emptyReturnCount = ($emptyReturns | Measure-Object).Count

Write-Host "?? Potentially Empty Returns: $emptyReturnCount" -ForegroundColor Yellow
Write-Host ""

# Calculate completion percentage
$totalFiles = (Get-ChildItem -Path $projectRoot -Recurse -Include *.cpp | Measure-Object).Count
$completeFiles = $totalFiles - $stubCount
$completionPercent = [math]::Round(($completeFiles / $totalFiles) * 100, 2)

Write-Host "?? PROJECT COMPLETION STATUS:" -ForegroundColor Green
Write-Host "   Total Source Files: $totalFiles" -ForegroundColor White
Write-Host "   Complete Files: $completeFiles" -ForegroundColor Green
Write-Host "   Stub Files: $stubCount" -ForegroundColor Red
Write-Host "   Completion: $completionPercent%" -ForegroundColor $(if ($completionPercent -gt 80) { "Green" } elseif ($completionPercent -gt 50) { "Yellow" } else { "Red" })
Write-Host ""

Write-Host "?? PRIORITY FIXES NEEDED:" -ForegroundColor Cyan
Write-Host "   1. FRPlayerCharacterCreatorSystem.cpp (STUB)" -ForegroundColor Red
Write-Host "   2. FRProceduralCharacterSystem.cpp (STUB)" -ForegroundColor Red
Write-Host "   3. FRBattlePassSystem.cpp (12 TODOs)" -ForegroundColor Yellow
Write-Host "   4. FRBuyStationSystem.cpp (8 TODOs)" -ForegroundColor Yellow
Write-Host "   5. FRContentCreatorSystem.cpp (8 TODOs)" -ForegroundColor Yellow
Write-Host ""

Write-Host "? NEXT STEPS:" -ForegroundColor Green
Write-Host "   1. Read INCOMPLETE_CODE_AUDIT.md for full analysis"
Write-Host "   2. Choose implementation priority (Option A/B/C)"
Write-Host "   3. Start with critical revenue systems"
Write-Host "   4. Then tackle character generation systems"
Write-Host ""

Write-Host "?? DETAILED REPORT: See INCOMPLETE_CODE_AUDIT.md" -ForegroundColor Magenta
Write-Host ""

# Save summary to file
$summaryFile = "C:\Users\FlavorGood\Documents\Unreal Projects\Frontline\CODE_STATUS_SUMMARY.txt"
@"
FRONTLINE PROJECT - CODE COMPLETION SUMMARY
Generated: $(Get-Date)

METRICS:
- Total Source Files: $totalFiles
- Complete Files: $completeFiles  
- Stub Files: $stubCount
- TODO Comments: $todoCount
- Empty Returns: $emptyReturnCount
- Completion: $completionPercent%

CRITICAL ISSUES:
- FRPlayerCharacterCreatorSystem.cpp: 100% STUB
- FRProceduralCharacterSystem.cpp: 100% STUB
- FRBattlePassSystem.cpp: 12 TODOs
- FRBuyStationSystem.cpp: 8 TODOs
- FRContentCreatorSystem.cpp: 8 TODOs

STATUS: $(if ($completionPercent -gt 80) { "READY FOR LAUNCH" } elseif ($completionPercent -gt 50) { "NEEDS WORK" } else { "CRITICAL - NOT LAUNCH READY" })

RECOMMENDATION: $(if ($completionPercent -lt 60) { "Implement Phase 1 & 2 (Revenue + Character Systems) - 25-35 days" } elseif ($completionPercent -lt 80) { "Implement remaining TODOs - 10-15 days" } else { "Polish and test - 5-7 days" })

See INCOMPLETE_CODE_AUDIT.md for full details and action plan.
"@ | Out-File -FilePath $summaryFile -Encoding UTF8

Write-Host "?? Summary saved to: CODE_STATUS_SUMMARY.txt" -ForegroundColor Green
