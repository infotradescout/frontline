# ============================================================================
# Frontline — Remove Starter Content
#
# Use only if Unreal forced Starter Content ON during project creation.
# Safe to run multiple times.
# ============================================================================

$ErrorActionPreference = 'Stop'

$repoRoot    = Split-Path -Parent $PSScriptRoot
$projectRoot = Join-Path $repoRoot 'UnrealProject\Frontline'
$starterPath = Join-Path $projectRoot 'Content\StarterContent'

Write-Host ''
Write-Host '================================================================' -ForegroundColor Cyan
Write-Host ' Frontline — Starter Content Cleanup' -ForegroundColor Cyan
Write-Host '================================================================' -ForegroundColor Cyan
Write-Host ''

if (-not (Test-Path $projectRoot)) {
    Write-Host '❌ Unreal project folder not found:' -ForegroundColor Red
    Write-Host "   $projectRoot" -ForegroundColor Red
    Write-Host 'Create the project first, then run this script.' -ForegroundColor Red
    exit 1
}

if (-not (Test-Path $starterPath)) {
    Write-Host '✅ StarterContent folder is already absent. Nothing to remove.' -ForegroundColor Green
    exit 0
}

Remove-Item -Path $starterPath -Recurse -Force
Write-Host '✅ StarterContent removed.' -ForegroundColor Green
Write-Host ''
Write-Host 'Next:' -ForegroundColor White
Write-Host '  1. Re-open Frontline.uproject' -ForegroundColor White
Write-Host '  2. If prompted to save anything related to StarterContent, choose Skip/No' -ForegroundColor White
Write-Host '  3. Tell Copilot "it works" and I will commit/push for you.' -ForegroundColor White
Write-Host ''
