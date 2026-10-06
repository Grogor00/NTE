# When CR2 registry has zero pending items but programme is not closed, seed next wave from NTE_CR2_Registry_Waves.json
# Greg directive: no idle until exit criteria met or auto off
param(
  [switch]$ForceWave
)

. (Join-Path $PSScriptRoot 'Resolve-NteRoots.ps1')
$root = $NteCorpusRoot



$registryPath = Join-Path $root 'Working\NTE_CR2_Open_Work_Registry.json'
$wavesPath = Join-Path $root 'Working\NTE_CR2_Registry_Waves.json'
$logPath = Join-Path $root 'Workflow\.cursor_autonomous_execute.log'

function Write-Log([string]$Msg) {
  $line = ('{0} [replenish] {1}' -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $Msg)
  try { Add-Content -Path $logPath -Value $line -Encoding UTF8 } catch { }
}

if (-not (Test-Path $registryPath)) {
  Write-Log 'no registry file'
  exit 0
}

$registry = Get-Content $registryPath -Raw | ConvertFrom-Json
if ($registry.programme_closed) {
  Write-Log 'programme closed - no replenish'
  exit 0
}

$pending = @($registry.backlog | Where-Object { $_.status -eq 'pending' })
if ($pending.Count -gt 0 -and -not $ForceWave) {
  Write-Log ("skip - {0} pending item(s) already" -f $pending.Count)
  exit 0
}

if (-not (Test-Path $wavesPath)) {
  Write-Log 'no waves file - cannot replenish'
  exit 0
}

$wavesDoc = Get-Content $wavesPath -Raw | ConvertFrom-Json
if (-not $registry.replenished_waves) {
  $registry | Add-Member -NotePropertyName replenished_waves -NotePropertyValue @() -Force
}

$existingIds = @{}
foreach ($b in $registry.backlog) { $existingIds[$b.id] = $true }

$nextWave = $null
foreach ($w in $wavesDoc.waves) {
  $wn = [int]$w.wave
  if ($registry.replenished_waves -contains $wn) { continue }
  $nextWave = $w
  break
}

if (-not $nextWave) {
  # All defined waves consumed - re-seed sustain wave 4 if fully completed (48h cadence guard via item prompts)
  $w4 = $wavesDoc.waves | Where-Object { $_.wave -eq 4 } | Select-Object -First 1
  if ($w4) {
    $allW4Done = $true
    foreach ($it in $w4.items) {
      $b = $registry.backlog | Where-Object { $_.id -eq $it.id } | Select-Object -First 1
      if (-not $b -or $b.status -ne 'completed') { $allW4Done = $false; break }
    }
    if ($allW4Done) {
      foreach ($it in $w4.items) {
        $b = $registry.backlog | Where-Object { $_.id -eq $it.id } | Select-Object -First 1
        if ($b) {
          $b.status = 'pending'
          if ($b.PSObject.Properties['completed_at']) { $b.PSObject.Properties.Remove('completed_at') }
        } else {
          $registry.backlog += [pscustomobject]@{
            id = $it.id
            stream = $it.stream
            priority = $it.priority
            status = 'pending'
            phase = $it.phase
            title = $it.title
            prompt = $it.prompt
          }
        }
        $existingIds[$it.id] = $true
      }
      $registry | ConvertTo-Json -Depth 8 | Set-Content $registryPath -Encoding UTF8
      Write-Log ("re-seeded sustain wave {0} ({1} items)" -f $w4.wave, $w4.items.Count)
      Write-Output ("REPLENISH wave={0} count={1} sustain=1" -f $w4.wave, $w4.items.Count)
      exit 0
    }
  }
  Write-Log 'all waves consumed; sustain wave not ready for re-seed'
  exit 0
}

$added = 0
foreach ($it in $nextWave.items) {
  if ($existingIds.ContainsKey($it.id)) { continue }
  $registry.backlog += [pscustomobject]@{
    id = $it.id
    stream = $it.stream
    priority = $it.priority
    status = 'pending'
    phase = $it.phase
    title = $it.title
    prompt = $it.prompt
  }
  $existingIds[$it.id] = $true
  $added++
}

if ($added -eq 0) {
  Write-Log ("wave {0} - all IDs already in backlog; marking replenished" -f $nextWave.wave)
} else {
  Write-Log ("wave {0} - added {1} pending item(s)" -f $nextWave.wave, $added)
}

$wnDone = [int]$nextWave.wave
if ($registry.replenished_waves -notcontains $wnDone) {
  $registry.replenished_waves = @($registry.replenished_waves) + $wnDone
}

$registry | ConvertTo-Json -Depth 8 | Set-Content $registryPath -Encoding UTF8
Write-Output ("REPLENISH wave={0} count={1}" -f $nextWave.wave, $added)
exit 0

. (Join-Path $PSScriptRoot 'Resolve-NteRoots.ps1')

$wfRoot = $NteWorkflowRoot
