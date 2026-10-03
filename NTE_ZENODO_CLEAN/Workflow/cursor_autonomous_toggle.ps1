# Per-stream or all-stream toggle for NTE Cursor autonomous polls
# Examples:
#   .\cursor_autonomous_toggle.ps1 -Status
#   .\cursor_autonomous_toggle.ps1 -On
#   .\cursor_autonomous_toggle.ps1 -Off
#   .\cursor_autonomous_toggle.ps1 -Stream ac_jammer -Off
#   .\cursor_autonomous_toggle.ps1 -Stream main -On

param(
  [ValidateSet('main', 'ac_jammer', 'pc_scratch', 'supervisor', 'all')]
  [string]$Stream = 'all',
  [switch]$On,
  [switch]$Off,
  [switch]$Status
)

. (Join-Path $PSScriptRoot 'Resolve-NteRoots.ps1')
# Always launch from Google Drive Workflow — never Desktop/OneDrive junctions.
$root = $NteWorkflowRoot
if ($root -notmatch '(?i)\\NTE_ZENODO_CLEAN\\Workflow$') {
  $root = 'C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Workflow'
}



$togglePath = Join-Path $root '.cursor_autonomous_toggle.json'
$poll = Join-Path $root 'cursor_autonomous_poll.ps1'
$supervisorPoll = Join-Path $root 'cursor_autonomous_supervisor_poll.ps1'
$pidFile = Join-Path $root '.cursor_autonomous_pids.json'
$allStreams = @('main', 'ac_jammer', 'pc_scratch')
$supervisorStream = 'supervisor'

function Get-ToggleObj {
  if (Test-Path $togglePath) {
    try { return Get-Content $togglePath -Raw | ConvertFrom-Json } catch { }
  }
  return [pscustomobject]@{
    enabled = $true
    streams = [pscustomobject]@{
      main = [pscustomobject]@{ enabled = $true; tick_minutes = 3 }
      ac_jammer = [pscustomobject]@{ enabled = $true; tick_minutes = 5 }
      pc_scratch = [pscustomobject]@{ enabled = $true; tick_minutes = 7 }
    }
  }
}

function Save-ToggleObj($t) {
  $t | ConvertTo-Json -Depth 5 | Set-Content $togglePath -Encoding UTF8
}

function Stop-StreamWorker([string]$Name) {
  $pattern = if ($Name -eq 'supervisor') { '*cursor_autonomous_supervisor_poll.ps1*' } else { "*cursor_autonomous_poll.ps1*$Name*" }
  Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" -ErrorAction SilentlyContinue |
    Where-Object { $_.CommandLine -like $pattern } |
    ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
}

function Start-StreamWorker([string]$Name) {
  Stop-StreamWorker $Name
  Start-Sleep -Milliseconds 300
  $scriptPath = if ($Name -eq 'supervisor') { $supervisorPoll } else { $poll }
  $args = if ($Name -eq 'supervisor') {
    @('-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', $scriptPath)
  } else {
    @('-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', $scriptPath, '-Stream', $Name)
  }
  $p = Start-Process -FilePath 'powershell.exe' -PassThru -WorkingDirectory $root -WindowStyle Minimized -ArgumentList $args
  Start-Sleep -Milliseconds 500
  if (-not (Get-Process -Id $p.Id -ErrorAction SilentlyContinue)) {
    Write-Warning "$Name poll worker exited immediately (PID $($p.Id))"
  }
  return $p.Id
}

function Test-StreamRunning([string]$Name) {
  return ($null -ne (Get-StreamPid $Name))
}

function Get-StreamPid([string]$Name) {
  $hit = if ($Name -eq 'supervisor') {
    Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" -ErrorAction SilentlyContinue |
      Where-Object { $_.CommandLine -like '*cursor_autonomous_supervisor_poll.ps1*' } |
      Select-Object -First 1
  } else {
    Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" -ErrorAction SilentlyContinue |
      Where-Object { $_.CommandLine -like '*cursor_autonomous_poll.ps1*' -and $_.CommandLine -like "*-Stream $Name*" } |
      Select-Object -First 1
  }
  if ($hit) { return $hit.ProcessId }
  return $null
}

function Show-Status {
  $t = Get-ToggleObj
  Write-Host 'NTE Cursor autonomous streams'
  Write-Host "  master enabled: $($t.enabled)"
  $refreshed = @{}
  foreach ($s in ($allStreams + @($supervisorStream))) {
    $en = $true
    if ($t.streams.$s) { $en = [bool]$t.streams.$s.enabled }
    $defaults = @{ main = 3; ac_jammer = 5; pc_scratch = 7; supervisor = 60 }
    $tick = $defaults[$s]
    if ($t.streams.$s.tick_minutes) { $tick = $t.streams.$s.tick_minutes }
    $streamPid = Get-StreamPid $s
    if ($streamPid) { $refreshed[$s] = $streamPid }
    $runLabel = if (Test-StreamRunning $s) { 'RUNNING' } else { 'stopped' }
    $pidNote = if ($streamPid) { " PID $streamPid" } else { '' }
    Write-Host "  $s : enabled=$en tick=${tick}m $runLabel$pidNote"
  }
  if ($refreshed.Count -gt 0) { $refreshed | ConvertTo-Json | Set-Content $pidFile -Encoding UTF8 }
}

if ($Status -or (-not $On -and -not $Off)) {
  Show-Status
  if (-not $On -and -not $Off) {
    Write-Host ''
    Write-Host 'Usage: -On | -Off  [-Stream main|ac_jammer|pc_scratch|all]'
  }
  exit 0
}

$targets = if ($Stream -eq 'all') { $allStreams + @($supervisorStream) } else { @($Stream) }
$t = Get-ToggleObj
$pids = @{}
if (Test-Path $pidFile) {
  try {
    $loaded = Get-Content $pidFile -Raw | ConvertFrom-Json
    $loaded.PSObject.Properties | ForEach-Object { $pids[$_.Name] = $_.Value }
  } catch { }
}

$execScript = Join-Path $root 'cursor_autonomous_execute_tick.ps1'

foreach ($s in $targets) {
    $defaults = @{ main = 3; ac_jammer = 5; pc_scratch = 7; supervisor = 60 }
    if (-not $t.streams.$s) {
      $t.streams | Add-Member -NotePropertyName $s -NotePropertyValue ([pscustomobject]@{ enabled = $true; tick_minutes = $defaults[$s] }) -Force
  }
  $t.streams.$s.enabled = [bool]$On
  if ($Off) {
    Stop-StreamWorker $s
    if ($pids.ContainsKey($s)) { $pids.Remove($s) }
    Write-Host "$s OFF"
  } elseif ($On) {
    $procId = Start-StreamWorker $s
    $pids[$s] = $procId
    if ($s -ne 'supervisor' -and (Test-Path $execScript)) {
      & $execScript -Stream $s 2>&1 | ForEach-Object { Write-Host $_ }
    } elseif ($s -eq 'supervisor') {
      $supTick = Join-Path $root 'cursor_autonomous_supervisor_tick.ps1'
      if (Test-Path $supTick) { & $supTick 2>&1 | ForEach-Object { Write-Host $_ } }
    }
    Write-Host "$s ON (PID $procId)"
  }
}

$t.enabled = (($allStreams + @($supervisorStream)) | Where-Object { $t.streams.$_.enabled }).Count -gt 0
Save-ToggleObj $t
if ($pids.Count -gt 0) { $pids | ConvertTo-Json | Set-Content $pidFile -Encoding UTF8 }
Show-Status

. (Join-Path $PSScriptRoot 'Resolve-NteRoots.ps1')

$wfRoot = $NteWorkflowRoot
