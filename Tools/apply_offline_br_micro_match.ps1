param(
    [string]$ProjectRoot = "C:\Users\flavo\Documents\Unreal Projects\FrontlineWarfare",
    [string]$EngineCmdExe = "D:\UE_5.7\Engine\Binaries\Win64\UnrealEditor-Cmd.exe"
)

$ErrorActionPreference = "Stop"

$uproject = Join-Path $ProjectRoot "FrontlineWarfare.uproject"
if (-not (Test-Path $uproject)) { throw "Missing uproject: $uproject" }
if (-not (Test-Path $EngineCmdExe)) { throw "Missing commandlet exe: $EngineCmdExe" }

$repoRoot = Split-Path $PSScriptRoot -Parent
$applyScript = Join-Path $repoRoot "Tools\ue_apply_offline_br_micro_match.py"
$verifyScript = Join-Path $repoRoot "Tools\ue_verify_offline_br_micro_match.py"

if (-not (Test-Path $applyScript)) { throw "Missing python tool: $applyScript" }
if (-not (Test-Path $verifyScript)) { throw "Missing python tool: $verifyScript" }

$applyLog = Join-Path $repoRoot "Tools\last_offline_br_apply.log"
$verifyLog = Join-Path $repoRoot "Tools\last_offline_br_verify.log"

& $EngineCmdExe $uproject -run=pythonscript ("-script=" + $applyScript) -unattended -nosplash -nop4 *> $applyLog
& $EngineCmdExe $uproject -run=pythonscript ("-script=" + $verifyScript) -unattended -nosplash -nop4 *> $verifyLog

Get-Content $applyLog | Select-String -Pattern "BR_APPLY_|Traceback|Python script executed with errors" | ForEach-Object { $_.Line }
Get-Content $verifyLog | Select-String -Pattern "BR_VERIFY_|Traceback|Python script executed with errors" | ForEach-Object { $_.Line }

Write-Output "OFFLINE_BR_MICRO_MATCH_APPLY_COMPLETE"
