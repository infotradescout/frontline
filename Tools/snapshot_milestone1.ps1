param(
    [string]$ProjectRoot = "C:\Users\flavo\Documents\Unreal Projects\FrontlineWarfare"
)

$ErrorActionPreference = 'Stop'

if (-not (Test-Path $ProjectRoot)) {
    throw "Project root not found: $ProjectRoot"
}

$stamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$snapshotRoot = Join-Path $ProjectRoot "Saved\Milestones\M1_Playable_$stamp"
New-Item -ItemType Directory -Path $snapshotRoot -Force | Out-Null

$pathsToCopy = @('Config', 'Content', '*.uproject')
foreach ($p in $pathsToCopy) {
    $src = Join-Path $ProjectRoot $p
    if (Test-Path $src) {
        if ((Get-Item $src).PSIsContainer) {
            Copy-Item $src (Join-Path $snapshotRoot (Split-Path $src -Leaf)) -Recurse -Force
        }
        else {
            Copy-Item $src $snapshotRoot -Force
        }
    }
}

Write-Output "SNAPSHOT_CREATED=$snapshotRoot"
