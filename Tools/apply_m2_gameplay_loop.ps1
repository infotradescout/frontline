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
EditorStartupMap=/Game/FirstPerson/Lvl_FirstPerson
GameDefaultMap=/Game/FirstPerson/Lvl_FirstPerson
ServerDefaultMap=/Game/FirstPerson/Lvl_FirstPerson
GlobalDefaultGameMode=/Game/FirstPerson/Blueprints/BP_FirstPersonGameMode.BP_FirstPersonGameMode_C
GlobalDefaultServerGameMode=/Game/FirstPerson/Blueprints/BP_FirstPersonGameMode.BP_FirstPersonGameMode_C
"@
Set-Content $cfg (($clean.TrimEnd()+"`r`n`r`n"+$block+"`r`n")) -Encoding UTF8

Get-Process -Name UnrealEditor -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
Start-Process -FilePath $EngineExe -ArgumentList ('"'+$uproject+'"')
Write-Output 'M2_GAMEPLAY_LOOP_APPLIED_AND_PROJECT_OPENED'
