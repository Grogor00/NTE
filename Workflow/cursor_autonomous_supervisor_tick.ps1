# One supervisor pass: health-check workers, PDF staleness, corpus grep, AC status handoff
param(
  [switch]$Quiet
)

. (Join-Path $PSScriptRoot 'Resolve-NteRoots.ps1')
$root = $NteCorpusRoot


$ErrorActionPreference = 'Continue'

$wf = Join-Path $root 'Workflow'
$handoffs = Join-Path $root 'Handoffs'
$togglePath = Join-Path $wf '.cursor_autonomous_toggle.json'
$toggleScript = Join-Path $wf 'cursor_autonomous_toggle.ps1'
$logPath = Join-Path $wf '.cursor_autonomous_supervisor.log'
$chainDir = Join-Path $wf '.cursor_autonomous_chain'
$buildPs1 = Join-Path $root 'paper-build\build-pdfs.ps1'
$bookBuildPs1 = Join-Path $root 'Book\paper-build\build-pdfs.ps1'
$pyGrep = Join-Path $root 'Working\supervisor_corpus_grep_gates.py'
$pyPdf = Join-Path $root 'Working\supervisor_pdf_staleness.py'
$allStreams = @('main', 'ac_jammer', 'pc_scratch')

function Write-Log([string]$Msg) {
  $line = ('{0} [supervisor] {1}' -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $Msg)
  try {
    [System.IO.File]::AppendAllText($logPath, $line + [Environment]::NewLine)
  } catch { }
  if (-not $Quiet) { Write-Output $line }
}

function Get-StreamPid([string]$Name) {
  $hit = Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" -ErrorAction SilentlyContinue |
    Where-Object { $_.CommandLine -like '*cursor_autonomous_poll.ps1*' -and $_.CommandLine -like "*-Stream $Name*" } |
    Select-Object -First 1
  if ($hit) { return $hit.ProcessId }
  return $null
}

function Restart-StreamIfDown([string]$Name) {
  $streamPid = Get-StreamPid $Name
  if ($streamPid) { return @{ stream = $Name; status = 'running'; pid = $streamPid; restarted = $false } }
  Write-Log "RESTART $Name (worker missing)"
  & $toggleScript -Stream $Name -On 2>&1 | Out-Null
  Start-Sleep -Seconds 2
  $newPid = Get-StreamPid $Name
  return @{ stream = $Name; status = if ($newPid) { 'restarted' } else { 'failed' }; pid = $newPid; restarted = $true }
}

# --- 1. Worker health ---
$health = @()
foreach ($s in $allStreams) {
  $health += Restart-StreamIfDown $s
}

# --- 2. PDF staleness ---
$stalePapers = @()
$staleBooks = @()
if (Test-Path $pyPdf) {
  $pdfOut = python $pyPdf 2>&1 | Out-String
  Write-Log "pdf_scan: $($pdfOut.Trim())"
  if ($pdfOut -match 'STALE_PAPERS:(.*)') { $stalePapers = ($Matches[1].Trim() -split ';' | Where-Object { $_ }) }
  if ($pdfOut -match 'STALE_BOOKS:(.*)') { $staleBooks = ($Matches[1].Trim() -split ';' | Where-Object { $_ }) }
}

$pdfRebuilt = @()
if ($stalePapers.Count -gt 0 -and (Test-Path $buildPs1)) {
  Write-Log "rebuild papers: $($stalePapers -join ', ')"
  & powershell -NoProfile -ExecutionPolicy Bypass -File $buildPs1 -Only $stalePapers 2>&1 | ForEach-Object { Write-Log $_ }
  $pdfRebuilt += $stalePapers
}
if ($staleBooks.Count -gt 0 -and (Test-Path $bookBuildPs1)) {
  Write-Log "rebuild book chapters: $($staleBooks -join ', ')"
  & powershell -NoProfile -ExecutionPolicy Bypass -File $bookBuildPs1 -Only $staleBooks 2>&1 | ForEach-Object { Write-Log $_ }
  $pdfRebuilt += $staleBooks
}

# --- 3. Corpus grep gates ---
$grepReport = 'skipped'
if (Test-Path $pyGrep) {
  $grepReport = python $pyGrep 2>&1 | Out-String
  Write-Log "grep_gates done"
}

# --- 4. Unactioned Claude→Cursor handoffs (heuristic) ---
$pendingInbound = @()
$cutoff = (Get-Date).AddDays(-14)
$ledgerPathEarly = Join-Path $root 'Working\cursor_task_ledger.json'
$ledgerTasksEarly = @()
if (Test-Path $ledgerPathEarly) {
  try { $ledgerTasksEarly = @((Get-Content $ledgerPathEarly -Raw | ConvertFrom-Json).tasks) } catch { }
}
# Canonical patterns that MUST flag until a matching Cursor completion exists (Greg P0 2026-06-21)
$mandatoryInboundPatterns = @(
  'Handoff_Claude_Jammer_to_.*Cursor',
  'Handoff_Claude_Jammer_to_AC_Cursor',
  'SEED_.*Cursor_(Jammer|Main|ac_jammer)',
  'SEED_REISSUE_.*Cursor',
  '^P0_.*Cursor',
  '^CONSOLIDATED_.*Cursor',
  '^PRIORITY_.*Cursor',
  '^DIRECTIVE_.*Cursor'
)
$inboundLib = Join-Path $wf 'cursor_autonomous_inbound.ps1'
if (Test-Path $inboundLib) { . $inboundLib }
Get-ChildItem -Path $handoffs -File -ErrorAction SilentlyContinue |
  Where-Object {
    $_.LastWriteTime -ge $cutoff -and
    (
      $_.Name -match '^Handoff_(AC|Jammer|PC|Scratch|CR|Claude(?:_[A-Za-z]+)?)_to_.*Cursor' -or
      ($_.Name -match '^SEED_(REISSUE_)?AC_to_Cursor')
    ) -and
    $_.Name -notmatch 'CLOSED|HOLD|TERMINATED|VERIFIED|Verification|INSTRUCTION_Greg'
  } |
  Sort-Object LastWriteTime -Descending |
  Select-Object -First 20 |
  ForEach-Object {
    $inbound = $_
    # Ledger-aware clearance: drained programme work is done even if handoff file was re-touched
    if ($inbound.Name -match '4pi|Farnsworth|Associator|Stream1') {
      $s4done = $ledgerTasksEarly | Where-Object {
        $_.id -eq 'FARNSWORTH-S4FULL-ASSOCIATOR-STREAM1' -and $_.state -eq 'VERIFIED'
      }
      if ($s4done) { return }
    }
    $doneCandidates = @(Get-ChildItem -Path $handoffs -File -ErrorAction SilentlyContinue |
      Where-Object { $_.Name -match '^Handoff_Cursor' })
    # Topic tokens for completion matching
    $topicTokens = @()
    if ($inbound.Name -match 'CPN') { $topicTokens += 'CPN' }
    if ($inbound.Name -match 'KPhi|K_Phi') { $topicTokens += 'KPhi' }
    if ($inbound.Name -match 'PackageE[0-9]') { $topicTokens += 'PackageE' }
    if ($inbound.Name -match 'Supervisor') { $topicTokens += 'Supervisor' }
    if ($inbound.Name -match 'S2') { $topicTokens += 'S2' }
    if ($inbound.Name -match 'Farnsworth|4pi|8pi|Associator|Stream1|Stream2') {
      $topicTokens += 'Farnsworth'; $topicTokens += '4pi'; $topicTokens += 'Associator'
    }
    if ($inbound.Name -match 'Heuristic|Jammer') { $topicTokens += 'Jammer'; $topicTokens += 'Heuristic' }
    if ($inbound.Name -match 'SEED_REISSUE|SEED_AC') { $topicTokens += 'SEED' }

    $isMandatory = $false
    foreach ($pat in $mandatoryInboundPatterns) {
      if ($inbound.Name -match $pat) { $isMandatory = $true; break }
    }

    $done = @()
    if ($topicTokens.Count -gt 0) {
      $done = @($doneCandidates | Where-Object {
        $name = $_.Name
        $matchesToken = $false
        foreach ($tok in $topicTokens) {
          if ($name -match [regex]::Escape($tok)) { $matchesToken = $true; break }
        }
        $matchesToken
      })
    } elseif (-not $isMandatory) {
      # Legacy: non-mandatory inbounds with no token map stay unflagged if no tokens
      $done = @($doneCandidates)
    }
    # Mandatory patterns stay pending until token-matched completion (never auto-clear)
    if ($isMandatory -and $topicTokens.Count -gt 0 -and $done.Count -eq 0) {
      $pendingInbound += $inbound.Name
    } elseif (-not $isMandatory -and $done.Count -eq 0) {
      $pendingInbound += $inbound.Name
    } elseif ($isMandatory -and $topicTokens.Count -eq 0) {
      $pendingInbound += $inbound.Name
    }
  }

if (Get-Command Get-UnfulfilledMandatoryInbounds -ErrorAction SilentlyContinue) {
  foreach ($name in (Get-UnfulfilledMandatoryInbounds)) {
    if ($pendingInbound -notcontains $name) { $pendingInbound += $name }
  }
}

# --- 5. AC status handoff ---
$ts = Get-Date -Format 'yyyyMMdd_HHmmss'
$statusPath = Join-Path $handoffs "Handoff_Cursor_Main_to_AC_Supervisor_Hourly_Status_$ts.md"
$healthBlock = ($health | ForEach-Object { "- **$($_.stream):** $($_.status)$(if ($_.pid) { " (PID $($_.pid))" } else { '' })" }) -join "`n"
$pendingBlock = if ($pendingInbound.Count -gt 0) {
  ($pendingInbound | ForEach-Object { "- ``$_``" }) -join "`n"
} else { '- (none flagged by heuristic --- verify manually if needed)' }

$grepShort = if ($grepReport.Length -gt 3500) { $grepReport.Substring(0, 3500) + "`n... (truncated)" } else { $grepReport }


# 2026-09-27: escalate sticky heuristic-pending (identical backlog ≠ healthy)
$pendingStatePath = Join-Path $wf '.cursor_supervisor_pending_state.json'
$pendingHash = (($pendingInbound | Sort-Object) -join '|')
$stuckHours = 0
$pipelineHealthBlock = '- pending inbound: none --- pipeline clear'
if ($pendingInbound.Count -gt 0) {
  $prev = $null
  if (Test-Path $pendingStatePath) {
    try { $prev = Get-Content $pendingStatePath -Raw | ConvertFrom-Json } catch { $prev = $null }
  }
  if ($prev -and $prev.hash -eq $pendingHash) {
    $first = [datetime]$prev.first_seen
    $stuckHours = [math]::Round(((Get-Date) - $first).TotalHours, 1)
  } else {
    @{ hash = $pendingHash; first_seen = (Get-Date -Format 'o'); count = $pendingInbound.Count } |
      ConvertTo-Json | Set-Content -Path $pendingStatePath -Encoding utf8
    $stuckHours = 0
  }
  if ($stuckHours -ge 2 -or $pendingInbound.Count -ge 5) {
    $pipelineHealthBlock = "- **PIPELINE STUCK** --- heuristic-pending count=$($pendingInbound.Count); same-list age ~${stuckHours}h. This is NOT healthy. Promote/drain repair required; do not hand-carry forever."
  } else {
    $pipelineHealthBlock = "- pending inbound: $($pendingInbound.Count) (tracking; escalate if unchanged >=2h)"
  }
} else {
  if (Test-Path $pendingStatePath) { Remove-Item $pendingStatePath -Force -ErrorAction SilentlyContinue }
}

$body = @"
# Handoff --- Cursor Main → AC: Supervisor hourly status

**From:** Cursor Main  
**To:** AC (gate authority)  
**Cc:** Greg  
**Date:** $(Get-Date -Format 'yyyy-MM-dd HH:mm')  
**Re:** Autonomous supervisor tick --- worker health, PDF sync, corpus grep, inbound triage

---

## Worker health

$healthBlock

## PDF sync

- **Stale rebuilt (papers):** $(if ($stalePapers.Count) { ($stalePapers -join ', ') } else { 'none' })
- **Stale rebuilt (book):** $(if ($staleBooks.Count) { "$($staleBooks.Count) chapter(s)" } else { 'none' })

## Corpus grep gates

``````
$grepShort
``````

## Inbound Claude→Cursor (heuristic pending)

$pendingBlock

## Cursor actions this tick

- Restarted any stopped poll workers
- Rebuilt stale PDFs when detected
- **When ANY grep hit or tier doubt:** AC sight required before external deposit --- do not self-ratify

## Pipeline health

$pipelineHealthBlock

## Suggested AC actions

1. Ratify or redirect any flagged grep hits above
2. Close or re-queue stale inbound handoffs if already done
3. Reply via ``Handoff_AC_to_Cursor_*`` for any supervisor-flagged corpus fix
4. If pipeline health says STUCK: do not treat this tick as green --- promote/drain repair owed

--- Cursor Main, $(Get-Date -Format 'yyyy-MM-dd HH:mm').
"@
[System.IO.File]::WriteAllText($statusPath, $body, [System.Text.UTF8Encoding]::new($false))

Write-Log "status -> $statusPath"

# --- 6. Queue ledger drain (never self-supervision when work pending) ---
$ledgerPath = Join-Path $root 'Working\cursor_task_ledger.json'
$drainScript = Join-Path $wf 'cursor_autonomous_drain_ledger.ps1'
$hasQueuedLedger = $false
$ledgerStreamsPending = @()
if (Test-Path $ledgerPath) {
  try {
    $ledger = Get-Content $ledgerPath -Raw | ConvertFrom-Json
    foreach ($s in $allStreams) {
      $n = @($ledger.tasks | Where-Object { $_.state -in @('QUEUED', 'TODO') -and $_.stream -eq $s }).Count
      if ($n -gt 0) { $ledgerStreamsPending += $s }
    }
    $hasQueuedLedger = $ledgerStreamsPending.Count -gt 0
  } catch { }
}
foreach ($drainStream in $ledgerStreamsPending) {
  if (Test-Path $drainScript) {
    & $drainScript -Stream $drainStream 2>&1 | ForEach-Object { Write-Log $_ }
  }
}
if ($hasQueuedLedger -and (Test-Path $drainScript)) {
  # main already drained above if pending; keep legacy single-stream call for main-only fallback
  if ($ledgerStreamsPending -notcontains 'main') {
    # no-op: per-stream drain above
  }
} elseif (($grepReport -match 'FAIL|HIT|FLAG') -or ($pendingInbound.Count -gt 0)) {
  if (-not (Test-Path $chainDir)) { New-Item -ItemType Directory -Path $chainDir -Force | Out-Null }
  $prompt = @"
NTE supervisor tick ($(Get-Date -Format 'yyyy-MM-dd HH:mm')). **Sign as Cursor Main.**

1. Read ``$($statusPath | Split-Path -Leaf)`` (just filed).
2. Action any grep FAIL/HIT items you can fix without AC physics call; **escalate to AC** when unsure.
3. Triage pending inbound handoffs; execute or file completion handoff.
4. Run ``cursor_autonomous_complete_item.ps1`` only if matching queue ItemId exists.
5. Log ``Workflow/NTE_Stream_Notes_Cursor.md``.
"@
  @{
    requested_at = (Get-Date -Format 'o')
    stream = 'main'
    item_id = 'SUPERVISOR'
    title = 'Supervisor hourly tick follow-up'
    prompt = $prompt
  } | ConvertTo-Json | Set-Content (Join-Path $chainDir 'main.json') -Encoding UTF8
  Write-Log 'chain -> main.json (inbound/grep only; ledger takes priority)'
}

Write-Output "SUPERVISOR_TICK_OK health=$($health.Count) stale_papers=$($stalePapers.Count) status=$($statusPath | Split-Path -Leaf)"

. (Join-Path $PSScriptRoot 'Resolve-NteRoots.ps1')

$wfRoot = $NteWorkflowRoot
