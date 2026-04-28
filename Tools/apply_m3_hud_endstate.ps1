param(
    [string]$ProjectRoot = "C:\Users\flavo\Documents\Unreal Projects\FrontlineWarfare",
    [string]$EngineCmdExe = "D:\UE_5.7\Engine\Binaries\Win64\UnrealEditor-Cmd.exe"
)

$ErrorActionPreference = 'Stop'
$uproject = Join-Path $ProjectRoot 'FrontlineWarfare.uproject'
if (-not (Test-Path $uproject)) { throw "Missing uproject: $uproject" }
if (-not (Test-Path $EngineCmdExe)) { throw "Missing commandlet exe: $EngineCmdExe" }

$scriptPath = Join-Path (Split-Path $PSScriptRoot -Parent) 'Tools\ue_apply_hud_defaults.py'
if (-not (Test-Path $scriptPath)) { throw "Missing python tool: $scriptPath" }

$log = Join-Path (Split-Path $PSScriptRoot -Parent) 'Tools\last_m3_hud_apply.log'
& $EngineCmdExe $uproject -run=pythonscript ("-script=" + $scriptPath) -unattended -nosplash -nop4 *> $log

Get-Content $log | Select-String -Pattern 'HUD_APPLY|HUD_CHECK|Traceback|Python script executed with errors' | ForEach-Object { $_.Line }
Write-Output 'M3_HUD_ENDSTATE_APPLY_COMPLETE'
