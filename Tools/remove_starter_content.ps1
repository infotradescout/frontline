# ============================================================================
# Frontline — Remove Starter Content
#
# Use only if Unreal forced Starter Content ON during project creation.
# Safe to run multiple times.
# ============================================================================

param(
    [string]$ProjectName = ''
)

$ErrorActionPreference = 'Stop'

$repoRoot    = Split-Path -Parent $PSScriptRoot
$unrealRoot  = Join-Path $repoRoot 'UnrealProject'

Write-Host ''
Write-Host '================================================================' -ForegroundColor Cyan
Write-Host ' Frontline — Starter Content Cleanup' -ForegroundColor Cyan
Write-Host '================================================================' -ForegroundColor Cyan
Write-Host ''

if (-not (Test-Path $unrealRoot)) {
    Write-Host '❌ UnrealProject folder not found:' -ForegroundColor Red
    Write-Host "   $unrealRoot" -ForegroundColor Red
    Write-Host 'Create your Unreal project in this repo first.' -ForegroundColor Red
    exit 1
}

$projectRoot = $null
if (-not [string]::IsNullOrWhiteSpace($ProjectName)) {
    $candidate = Join-Path $unrealRoot $ProjectName
    if (Test-Path $candidate) { $projectRoot = $candidate }
}

if (-not $projectRoot) {
    $uprojects = Get-ChildItem -Path $unrealRoot -Recurse -Filter *.uproject -File
    if ($uprojects.Count -eq 1) {
        $projectRoot = Split-Path -Parent $uprojects[0].FullName
    } elseif ($uprojects.Count -gt 1) {
        Write-Host '❌ Multiple projects found. Run with -ProjectName.' -ForegroundColor Red
        $uprojects | ForEach-Object { Write-Host "   $($_.FullName)" -ForegroundColor Red }
        exit 1
    }
}

if (-not $projectRoot) {
    Write-Host '❌ No Unreal project found under UnrealProject\' -ForegroundColor Red
    Write-Host 'Create/open your project once, then re-run this script.' -ForegroundColor Red
    exit 1
}

$starterPath = Join-Path $projectRoot 'Content\StarterContent'

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
