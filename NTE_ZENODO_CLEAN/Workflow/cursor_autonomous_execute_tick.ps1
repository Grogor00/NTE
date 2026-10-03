# Execute one CR2 autonomous tick for a stream (mechanical + agent inbox)
param(
  [Parameter(Mandatory = $true)]
  [ValidateSet('main', 'ac_jammer', 'pc_scratch')]
  [string]$Stream,
  [string]$HandoffFile = ''
)

. (Join-Path $PSScriptRoot 'Resolve-NteRoots.ps1')
$root = $NteCorpusRoot
$script:NTEInboundRoot = $NteCorpusRoot

$ErrorActionPreference = 'Stop'

$wf = Join-Path $root 'Workflow'
$queuePath = Join-Path $root 'Working\NTE_CR2_Execution_Queue.json'
$inboxDir = Join-Path $wf '.cursor_autonomous_agent_inbox'
$logPath = Join-Path $wf '.cursor_autonomous_execute.log'
$togglePath = Join-Path $wf '.cursor_autonomous_toggle.json'
$chainDir = Join-Path $wf '.cursor_autonomous_chain'
$inboundLib = Join-Path $wf 'cursor_autonomous_inbound.ps1'
if (Test-Path $inboundLib) { . $inboundLib }

if (-not (Test-Path $inboxDir)) { New-Item -ItemType Directory -Path $inboxDir -Force | Out-Null }
if (-not (Test-Path $chainDir)) { New-Item -ItemType Directory -Path $chainDir -Force | Out-Null }

function Write-Log([string]$Msg) {
  $line = ('{0} [{1}] {2}' -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $Stream, $Msg)
  try { Add-Content -Path $logPath -Value $line -Encoding UTF8 -ErrorAction Stop } catch { }
}

function Stream-Enabled {
  if (-not (Test-Path $togglePath)) { return $true }
  try {
    $t = Get-Content $togglePath -Raw | ConvertFrom-Json
    if (-not $t.enabled) { return $false }
    if ($t.streams.$Stream) { return [bool]$t.streams.$Stream.enabled }
    return $true
  } catch { return $true }
}

if (-not (Stream-Enabled)) {
  Write-Log 'skip (stream disabled)'
  exit 0
}

function Write-Chain([string]$ItemId, [string]$Title, [string]$PromptText) {
  $chainFile = Join-Path $chainDir ("{0}.json" -f $Stream)
  @{
    requested_at = (Get-Date -Format 'o')
    stream = $Stream
    item_id = $ItemId
    title = $Title
    prompt = $PromptText
  } | ConvertTo-Json | Set-Content $chainFile -Encoding UTF8
}

function Get-IdentityFooter([string]$StreamName) {
  $map = @{
    main = 'Cursor Main'
    ac_jammer = 'Cursor AC or Cursor Jammer (AC/CR inbound -> Cursor AC; Jammer inbound -> Cursor Jammer)'
    pc_scratch = 'Cursor PC or Cursor Scratch (PC inbound -> Cursor PC; Scratch inbound -> Cursor Scratch)'
  }
  $label = $map[$StreamName]
  return "**Corpus identity:** Sign all handoffs, memos, and stream-note entries as **$label**. Never bare Cursor or bare specialist names without the Cursor prefix. Standard: Workflow/NTE_Cursor_Agent_Identity_Standard_v0_1_20260601.md"
}

# HARDENING 2026-09-26: HandoffFile (Directive_/ALL) MUST run before ledger early-exit.
# Prior bug: existing main.json caused exit 0 and skipped the new handoff entirely.
if ($HandoffFile) {
  if (Get-Command Test-KsipHandoffBlocked -ErrorAction SilentlyContinue) {
    if (Test-KsipHandoffBlocked $HandoffFile) {
      Write-Log ("handoff blocked (KSIP quarantined): {0}" -f $HandoffFile)
      exit 0
    }
  }
  $targetStream = if (Get-Command Get-InboundTargetStream -ErrorAction SilentlyContinue) {
    Get-InboundTargetStream $HandoffFile
  } else { $Stream }

  if (Get-Command Promote-InboundHandoffToLedger -ErrorAction SilentlyContinue) {
    $promotedIds = Promote-InboundHandoffToLedger $HandoffFile
    if ($promotedIds.Count -gt 0) {
      Write-Log ("handoff promoted to ledger: " + ($promotedIds -join ', '))
      $drain = Join-Path $wf 'cursor_autonomous_drain_ledger.ps1'
      if (Test-Path $drain) {
        & $drain -Stream $targetStream 2>&1 | ForEach-Object { Write-Log $_; Write-Output $_ }
        $chainFile = Join-Path $chainDir ("{0}.json" -f $targetStream)
        if (Test-Path $chainFile) {
          Write-Log "handoff->ledger queued to $targetStream.json"
          exit 0
        }
      }
    }
  }

  $handoffPath = Join-Path $root "Handoffs\$HandoffFile"
  if (Test-Path $handoffPath) {
    $txt = Get-Content $handoffPath -Raw
    $idFooter = Get-IdentityFooter $Stream
    $prompt = "CR2 $Stream handoff received: $HandoffFile`n`n$idFooter`n`nExecute this handoff now.`n`n---`n`n$txt"
    $inboxFile = Join-Path $inboxDir ("{0}.md" -f $Stream)
    Set-Content -Path $inboxFile -Value $prompt -Encoding UTF8
    Write-Chain 'HANDOFF' $HandoffFile $prompt
    Write-Log ("handoff queued: {0}" -f $HandoffFile)
    Write-Output ("AGENT_INBOX_{0} handoff={1}" -f $Stream, $HandoffFile)
  }
  exit 0
}

# Ledger-first drain for main (WORK source of truth; seen != done)
if ($Stream -eq 'main' -and (Get-Command Scan-AndPromoteMandatoryInbounds -ErrorAction SilentlyContinue)) {
  $promoted = Scan-AndPromoteMandatoryInbounds -Stream main
  if ($promoted.Count -gt 0) {
    Write-Log ("mandatory promote: " + ($promoted -join ', '))
  }
}
if ($Stream -eq 'ac_jammer' -and (Get-Command Scan-AndPromoteMandatoryInbounds -ErrorAction SilentlyContinue)) {
  $promoted = Scan-AndPromoteMandatoryInbounds -Stream ac_jammer
  if ($promoted.Count -gt 0) {
    Write-Log ("jammer promote: " + ($promoted -join ', '))
  }
}

if ($Stream -eq 'main' -or $Stream -eq 'ac_jammer' -or $Stream -eq 'pc_scratch') {
  $drain = Join-Path $wf 'cursor_autonomous_drain_ledger.ps1'
  if (Test-Path $drain) {
    & $drain -Stream $Stream 2>&1 | ForEach-Object { Write-Log $_; Write-Output $_ }
    $chainFile = Join-Path $chainDir ("{0}.json" -f $Stream)
    if (Test-Path $chainFile) {
      Write-Log "ledger work queued to $Stream.json"
      exit 0
    }
  }
}

if (-not (Test-Path $queuePath)) {
  Write-Log 'no queue file'
  exit 0
}

$registryPath = Join-Path $root 'Working\NTE_CR2_Open_Work_Registry.json'
function Test-PcLaneFirst {
  if (-not (Test-Path $registryPath)) { return $false }
  try {
    $reg = Get-Content $registryPath -Raw | ConvertFrom-Json
    $pc = @($reg.backlog | Where-Object { $_.status -eq 'pending' -and $_.lane -eq 'pc' })
    return ($pc.Count -gt 0)
  } catch { return $false }
}
function Test-SunshineRabbitHoleFirst {
  if (Test-PcLaneFirst) { return $true }
  if (-not (Test-Path $registryPath)) { return $false }
  try {
    $reg = Get-Content $registryPath -Raw | ConvertFrom-Json
    $ahead = @($reg.backlog | Where-Object {
        $_.status -eq 'pending' -and (
          ($_.lane -and $_.lane -ne 'bridge' -and $_.lane -ne 'pc' -and $_.lane -ne 'ksip') -or ([int]$_.priority -le 1)
        )
      })
    return ($ahead.Count -gt 0)
  } catch { return $false }
}
function Test-BridgeOutreachSuspended {
  if (-not (Test-Path $registryPath)) { return $false }
  try {
    $reg = Get-Content $registryPath -Raw | ConvertFrom-Json
    return ($reg.queue_policy -match 'bridge.*SUSPENDED')
  } catch { return $false }
}
function Test-KsipQuarantined {
  if (-not (Test-Path $registryPath)) { return $false }
  try {
    $reg = Get-Content $registryPath -Raw | ConvertFrom-Json
    return ($reg.queue_policy -match 'KSIP.*(QUARANTINED|TERMINATED)')
  } catch { return $false }
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
function Test-KsipHandoffBlocked([string]$HandoffName) {
  if (-not (Test-KsipQuarantined)) { return $false }
  return ($HandoffName -match 'KSIP|Kletetschka')
}
function Test-ItemBlockedBySunshinePolicy([object]$Item) {
  if (Test-IsKsipRelated $Item -and (Test-KsipQuarantined)) { return $true }
  if ($Item.lane -eq 'bridge' -and (Test-BridgeOutreachSuspended)) { return $true }
  if (Test-PcLaneFirst) {
    if ($Item.lane -ne 'pc') { return $true }
    return $false
  }
  if (-not (Test-SunshineRabbitHoleFirst)) { return $false }
  if ($Item.lane -eq 'bridge') { return $true }
  if ($null -ne $Item.priority -and [int]$Item.priority -ge 3) { return $true }
  return $false
}

$queue = Get-Content $queuePath -Raw | ConvertFrom-Json
$busy = $queue.items | Where-Object { $_.stream -eq $Stream -and $_.status -eq 'in_progress' } | Select-Object -First 1
if ($busy) {
  Write-Log ("skip queue (in progress: {0})" -f $busy.id)
  if ($busy.prompt) { Write-Chain $busy.id $busy.title $busy.prompt }
  exit 0
}
$next = $queue.items |
  Where-Object { $_.stream -eq $Stream -and $_.status -eq 'pending' -and -not (Test-ItemBlockedBySunshinePolicy $_) } |
  Sort-Object priority, id |
  Select-Object -First 1

if (-not $next) {
  $refillScript = Join-Path $wf 'cursor_autonomous_refill_queue.ps1'
  if (Test-Path $refillScript) {
    & $refillScript -Stream $Stream 2>&1 | ForEach-Object { Write-Output $_ }
    $queue = Get-Content $queuePath -Raw | ConvertFrom-Json
    $next = $queue.items |
      Where-Object { $_.stream -eq $Stream -and $_.status -eq 'pending' -and -not (Test-ItemBlockedBySunshinePolicy $_) } |
      Sort-Object priority, id |
      Select-Object -First 1
  }
}

if (-not $next) {
  Write-Log 'idle (no pending work for stream; registry empty or programme closed)'
  exit 0
}

# Mechanical pre-steps where applicable
if ($next.id -eq 'MAIN-01') {
  $camp = Join-Path $root 'Outreach\Distribution_Campaign_v1_20260530.md'
  if (Test-Path $camp) {
    $hits = Select-String -Path $camp -Pattern '0\.997|simultaneous sub-1%|simultaneous NuFIT' -AllMatches -ErrorAction SilentlyContinue
    Write-Log ('campaign grep residual hits: ' + @($hits).Count)
  }
}

if ($next.id -eq 'MAIN-03') {
  $script = Join-Path $root 'Working\cr2_s2_a4_gilkey_check.py'
  if (Test-Path $script) {
    $out = python $script 2>&1 | Out-String
    $compact = ($out -replace '\s+', ' ').Trim()
    if ($compact.Length -gt 0) {
      Write-Log ('Gilkey check: ' + $compact.Substring(0, [Math]::Min(120, $compact.Length)))
    }
  }
}

# Queue agent work into inbox for Cursor stop-hook chain
$inboxFile = Join-Path $inboxDir ("{0}.md" -f $Stream)
$idFooter = Get-IdentityFooter $Stream
$body = @"
# Autonomous inbox — $Stream

**Item:** $($next.id) — $($next.title)
**Queued:** $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')

$idFooter

---

$($next.prompt)

---

Execute now. When done: mark item $($next.id) completed in Working/NTE_CR2_Execution_Queue.json, log stream notes, clear this inbox file if no further pending items for this stream.
"@
Set-Content -Path $inboxFile -Value $body -Encoding UTF8

# Mark in-progress (single-flight per stream)
$next.status = 'in_progress'
$next | Add-Member -NotePropertyName started_at -NotePropertyValue (Get-Date -Format 'yyyy-MM-dd HH:mm:ss') -Force
$queue | ConvertTo-Json -Depth 6 | Set-Content $queuePath -Encoding UTF8

Write-Chain $next.id $next.title $next.prompt

Write-Log ("queued agent: {0} - {1}" -f $next.id, $next.title)
Write-Output ("AGENT_INBOX_{0} item={1} title={2}" -f $Stream, $next.id, $next.title)

. (Join-Path $PSScriptRoot 'Resolve-NteRoots.ps1')

$wfRoot = $NteWorkflowRoot
