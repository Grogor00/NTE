# Refill execution queue from CR2 open-work registry when a stream queue is empty
# Greg directive: no idle until programme exit criteria met or auto off
param(
  [Parameter(Mandatory = $true)]
  [ValidateSet('main', 'ac_jammer', 'pc_scratch')]
  [string]$Stream
)

. (Join-Path $PSScriptRoot 'Resolve-NteRoots.ps1')
$root = $NteCorpusRoot



$registryPath = Join-Path $root 'Working\NTE_CR2_Open_Work_Registry.json'
$queuePath = Join-Path $root 'Working\NTE_CR2_Execution_Queue.json'
$logPath = Join-Path $root 'Workflow\.cursor_autonomous_execute.log'

function Write-Log([string]$Msg) {
  $line = ('{0} [refill/{1}] {2}' -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $Stream, $Msg)
  try { Add-Content -Path $logPath -Value $line -Encoding UTF8 } catch { }
}

if (-not (Test-Path $registryPath)) {
  Write-Log 'no registry file'
  exit 0
}

$registry = Get-Content $registryPath -Raw | ConvertFrom-Json
if ($registry.programme_closed) {
  Write-Log 'programme closed — no refill'
  exit 0
}

function Test-PcLaneFirst([object]$Reg) {
  $pcAhead = @($Reg.backlog | Where-Object {
      $_.status -eq 'pending' -and $_.lane -eq 'pc'
    })
  return ($pcAhead.Count -gt 0)
}
function Test-SunshineRabbitHoleFirst([object]$Reg) {
  if (Test-PcLaneFirst $Reg) { return $true }
  $ahead = @($Reg.backlog | Where-Object {
      $_.status -eq 'pending' -and (
        ($_.lane -and $_.lane -ne 'bridge' -and $_.lane -ne 'pc' -and $_.lane -ne 'ksip') -or ([int]$_.priority -le 1)
      )
    })
  return ($ahead.Count -gt 0)
}
function Test-IsKsipRelated([object]$Item) {
  if ($null -eq $Item) { return $false }
  if ($Item.lane -eq 'ksip') { return $true }
  foreach ($prop in @('id', 'title', 'prompt')) {
    $val = [string]$Item.$prop
    if ($val -match 'KSIP|Kletetschka') { return $true }
  }
  return $false
}
function Test-BacklogItemBlocked([object]$B, [object]$Reg) {
  if (Test-IsKsipRelated $B -and $Reg.queue_policy -match 'KSIP.*(QUARANTINED|TERMINATED)') {
    return $true
  }
  if ($B.lane -eq 'bridge' -and $Reg.queue_policy -match 'bridge.*SUSPENDED') {
    return $true
  }
  if (Test-PcLaneFirst $Reg) {
    if ($B.lane -ne 'pc') { return $true }
    return $false
  }
  if (-not (Test-SunshineRabbitHoleFirst $Reg)) { return $false }
  if ($B.lane -eq 'bridge') { return $true }
  if ($null -ne $B.priority -and [int]$B.priority -ge 3) { return $true }
  return $false
}

if (-not (Test-Path $queuePath)) {
  @{ version = 2; items = @() } | ConvertTo-Json -Depth 6 | Set-Content $queuePath -Encoding UTF8
}

$queue = Get-Content $queuePath -Raw | ConvertFrom-Json
$existingIds = @{}
foreach ($item in $queue.items) { $existingIds[$item.id] = $true }

$added = 0
foreach ($b in $registry.backlog) {
  if ($b.stream -ne $Stream) { continue }
  if ($b.status -ne 'pending') { continue }
  if (Test-BacklogItemBlocked $b $registry) { continue }
  if ($existingIds.ContainsKey($b.id)) { continue }
  $queue.items += [pscustomobject]@{
    id = $b.id
    stream = $b.stream
    priority = $b.priority
    status = 'pending'
    kind = 'agent'
    title = $b.title
    prompt = $b.prompt
    phase = $b.phase
    lane = $b.lane
    from_registry = $true
  }
  $existingIds[$b.id] = $true
  $added++
}

if ($added -gt 0) {
  $queue | ConvertTo-Json -Depth 6 | Set-Content $queuePath -Encoding UTF8
  Write-Log ("refilled {0} item(s) from registry" -f $added)
  Write-Output ("REFILL_{0} count={1}" -f $Stream, $added)
} else {
  Write-Log 'registry has no new items for stream'
  $pendingAll = @($registry.backlog | Where-Object { $_.status -eq 'pending' })
  if ($pendingAll.Count -eq 0) {
    $replenishScript = Join-Path $root 'Workflow\cursor_autonomous_replenish_registry.ps1'
    if (Test-Path $replenishScript) {
      & $replenishScript 2>&1 | ForEach-Object { Write-Output $_ }
      $registry = Get-Content $registryPath -Raw | ConvertFrom-Json
      $added = 0
      foreach ($b in $registry.backlog) {
        if ($b.stream -ne $Stream) { continue }
        if ($b.status -ne 'pending') { continue }
        if (Test-BacklogItemBlocked $b $registry) { continue }
        if ($existingIds.ContainsKey($b.id)) { continue }
        $queue.items += [pscustomobject]@{
          id = $b.id
          stream = $b.stream
          priority = $b.priority
          status = 'pending'
          kind = 'agent'
          title = $b.title
          prompt = $b.prompt
          phase = $b.phase
          lane = $b.lane
          from_registry = $true
        }
        $existingIds[$b.id] = $true
        $added++
      }
      if ($added -gt 0) {
        $queue | ConvertTo-Json -Depth 6 | Set-Content $queuePath -Encoding UTF8
        Write-Log ("post-replenish refilled {0} item(s)" -f $added)
        Write-Output ("REFILL_{0} count={1} replenish=1" -f $Stream, $added)
      }
    }
  }
}

exit 0

. (Join-Path $PSScriptRoot 'Resolve-NteRoots.ps1')

$wfRoot = $NteWorkflowRoot
