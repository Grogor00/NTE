# Hourly supervisor poll — keeps main/ac_jammer/pc_scratch alive; PDF + corpus hygiene
param(
  [int]$TickMinutes = 0
)

. (Join-Path $PSScriptRoot 'Resolve-NteRoots.ps1')
$root = $NteWorkflowRoot


$ErrorActionPreference = 'Continue'

$togglePath = Join-Path $root '.cursor_autonomous_toggle.json'
$tickScript = Join-Path $root 'cursor_autonomous_supervisor_tick.ps1'

function Get-SupervisorTickMinutes {
  if ($TickMinutes -gt 0) { return $TickMinutes }
  if (Test-Path $togglePath) {
    try {
      $t = Get-Content $togglePath -Raw | ConvertFrom-Json
      if ($t.streams.supervisor.tick_minutes) { return [int]$t.streams.supervisor.tick_minutes }
    } catch { }
  }
  return 60
}

$interval = Get-SupervisorTickMinutes
Write-Output "AGENT_LOOP_TICK_cursor_supervisor {`"event`":`"start`",`"tick_min`":$interval}"

& $tickScript

while ($true) {
  $enabled = $true
  if (Test-Path $togglePath) {
    try {
      $t = Get-Content $togglePath -Raw | ConvertFrom-Json
      if (-not $t.enabled) { $enabled = $false }
      if ($t.streams.supervisor -and -not $t.streams.supervisor.enabled) { $enabled = $false }
      if ($t.streams.supervisor.tick_minutes) { $interval = [int]$t.streams.supervisor.tick_minutes }
    } catch { }
  }
  if (-not $enabled) {
    Write-Output 'AGENT_LOOP_TICK_cursor_supervisor {"event":"stopped","reason":"toggle off"}'
    break
  }
  Start-Sleep -Seconds ($interval * 60)
  try {
    & $tickScript
  } catch {
    Write-Output ("AGENT_LOOP_TICK_cursor_supervisor {`"event`":`"error`",`"error`":`"" + $_.Exception.Message + "`"}")
    Start-Sleep -Seconds 120
  }
}

. (Join-Path $PSScriptRoot 'Resolve-NteRoots.ps1')

$wfRoot = $NteWorkflowRoot
