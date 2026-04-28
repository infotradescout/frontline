# ============================================================================
# Frontline — Unreal Project Setup Script
#
# Run this AFTER you've created the Unreal project via the Epic Launcher
# (see Docs/Systems/CREATE_PROJECT_WALKTHROUGH.md).
#
# What this does:
#   1. Verifies UnrealProject/Frontline/Frontline.uproject exists
#   2. Copies our locked rendering config into the project's Config/ folder
#   3. Verifies Git LFS is installed and tracking
#   4. Reports status
#
# Safe to run multiple times.
# ============================================================================

$ErrorActionPreference = 'Stop'

# Resolve paths relative to repo root (script lives in Tools/)
$repoRoot     = Split-Path -Parent $PSScriptRoot
$projectDir   = Join-Path $repoRoot 'UnrealProject\Frontline'
$uprojectPath = Join-Path $projectDir 'Frontline.uproject'
$configDir    = Join-Path $projectDir 'Config'
$srcConfig    = Join-Path $PSScriptRoot 'UnrealConfig'

Write-Host ''
Write-Host '================================================================' -ForegroundColor Cyan
Write-Host ' Frontline — Unreal Project Setup' -ForegroundColor Cyan
Write-Host '================================================================' -ForegroundColor Cyan
Write-Host ''

# --- Step 1: Verify .uproject exists ---
Write-Host '[1/4] Looking for Frontline.uproject ...' -ForegroundColor Yellow
if (-not (Test-Path $uprojectPath)) {
    Write-Host ''
    Write-Host '❌ Frontline.uproject NOT FOUND at:' -ForegroundColor Red
    Write-Host "    $uprojectPath" -ForegroundColor Red
    Write-Host ''
    Write-Host 'Did you create the Unreal project yet?' -ForegroundColor Red
    Write-Host 'Follow Docs/Systems/CREATE_PROJECT_WALKTHROUGH.md first.' -ForegroundColor Red
    Write-Host ''
    exit 1
}
Write-Host "      ✅ Found: $uprojectPath" -ForegroundColor Green

# --- Step 2: Ensure Config/ exists ---
Write-Host ''
Write-Host '[2/4] Ensuring Config\ folder exists ...' -ForegroundColor Yellow
if (-not (Test-Path $configDir)) {
    New-Item -ItemType Directory -Force -Path $configDir | Out-Null
    Write-Host "      ✅ Created: $configDir" -ForegroundColor Green
} else {
    Write-Host "      ✅ Exists: $configDir" -ForegroundColor Green
}

# --- Step 3: Copy locked config files ---
Write-Host ''
Write-Host '[3/4] Copying locked rendering config ...' -ForegroundColor Yellow

$files = @('DefaultEngine.ini', 'DefaultGame.ini')
foreach ($f in $files) {
    $src = Join-Path $srcConfig $f
    $dst = Join-Path $configDir $f

    if (-not (Test-Path $src)) {
        Write-Host "      ❌ Source missing: $src" -ForegroundColor Red
        exit 1
    }

    # Back up existing file before overwriting
    if (Test-Path $dst) {
        $backup = "$dst.before-frontline-setup.bak"
        if (-not (Test-Path $backup)) {
            Copy-Item $dst $backup
            Write-Host "      ℹ  Backed up existing $f -> $f.before-frontline-setup.bak" -ForegroundColor DarkGray
        }
    }

    Copy-Item $src $dst -Force
    Write-Host "      ✅ Installed: Config\$f" -ForegroundColor Green
}

# --- Step 4: Verify Git LFS ---
Write-Host ''
Write-Host '[4/4] Verifying Git LFS ...' -ForegroundColor Yellow
try {
    $lfsVersion = (& git lfs version 2>$null) -join ''
    if ($lfsVersion -match 'git-lfs') {
        Write-Host "      ✅ $lfsVersion" -ForegroundColor Green
    } else {
        Write-Host '      ⚠  Git LFS not detected. Install from https://git-lfs.com' -ForegroundColor Yellow
    }
} catch {
    Write-Host '      ⚠  Git LFS check failed. Install from https://git-lfs.com' -ForegroundColor Yellow
}

# Confirm tracked patterns
$attrPath = Join-Path $repoRoot '.gitattributes'
if (Test-Path $attrPath) {
    $tracked = (Select-String -Path $attrPath -Pattern 'filter=lfs' -SimpleMatch).Count
    Write-Host "      ✅ .gitattributes tracks $tracked binary patterns via LFS" -ForegroundColor Green
} else {
    Write-Host '      ❌ .gitattributes missing — LFS will not work correctly.' -ForegroundColor Red
}

# --- Summary ---
Write-Host ''
Write-Host '================================================================' -ForegroundColor Cyan
Write-Host ' ✅ Setup complete' -ForegroundColor Green
Write-Host '================================================================' -ForegroundColor Cyan
Write-Host ''
Write-Host 'Next steps:' -ForegroundColor White
Write-Host '  1. Double-click UnrealProject\Frontline\Frontline.uproject' -ForegroundColor White
Write-Host '  2. Wait for shaders to recompile (one-time, ~3-10 min)' -ForegroundColor White
Write-Host '  3. Hit Play (green arrow). WASD + mouse + left-click should work.' -ForegroundColor White
Write-Host '  4. Tell Copilot "it works" — I will commit and push for you.' -ForegroundColor White
Write-Host ''
