param(
    [string]$ProjectRoot = "C:\Users\flavo\Documents\Unreal Projects\FrontlineWarfare",
    [string]$EngineExe = "D:\UE_5.7\Engine\Binaries\Win64\UnrealEditor.exe"
)

$ErrorActionPreference = 'Stop'
$cfg = Join-Path $ProjectRoot 'Config\DefaultEngine.ini'
$uproject = Join-Path $ProjectRoot 'FrontlineWarfare.uproject'

if (-not (Test-Path $cfg)) { throw "Missing config: $cfg" }
if (-not (Test-Path $uproject)) { throw "Missing uproject: $uproject" }
if (-not (Test-Path $EngineExe)) { throw "Missing editor exe: $EngineExe" }

$raw = Get-Content $cfg -Raw
$pattern = '(?ms)^\[/Script/EngineSettings\.GameMapsSettings\][\s\S]*?(?=^\[|\z)'
$clean = [regex]::Replace($raw, $pattern, '')
$block = @"
[/Script/EngineSettings.GameMapsSettings]
EditorStartupMap=/Game/Variant_Shooter/Lvl_ArenaShooter
GameDefaultMap=/Game/Variant_Shooter/Lvl_ArenaShooter
ServerDefaultMap=/Game/Variant_Shooter/Lvl_ArenaShooter
GlobalDefaultGameMode=/Game/Variant_Shooter/Blueprints/BP_ShooterGameMode.BP_ShooterGameMode_C
GlobalDefaultServerGameMode=/Game/Variant_Shooter/Blueprints/BP_ShooterGameMode.BP_ShooterGameMode_C
"@
Set-Content $cfg (($clean.TrimEnd()+"`r`n`r`n"+$block+"`r`n")) -Encoding UTF8

Get-Process -Name UnrealEditor -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
Start-Process -FilePath $EngineExe -ArgumentList ('"'+$uproject+'"')
Write-Output 'M2_GAMEPLAY_LOOP_APPLIED_AND_PROJECT_OPENED'
