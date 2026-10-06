# Shared inbound-handoff detection, routing, and mandatory ledger promotion.
# Dot-source from poll / execute_tick / supervisor_tick / drain_ledger.
# Rule: seen_is_not_done — promotion to cursor_task_ledger.json is REQUIRED before drain.

. (Join-Path $PSScriptRoot 'Resolve-NteRoots.ps1')
$script:NTEInboundRoot = $NteCorpusRoot
$script:NTEInboundHandoffs = Join-Path $script:NTEInboundRoot 'Handoffs'
$script:NTEInboundLedgerPath = Join-Path $script:NTEInboundRoot 'Working\cursor_task_ledger.json'
$script:NTEInboundPromoteLog = Join-Path $script:NTEInboundRoot 'Workflow\.cursor_autonomous_inbound_promote.log'
$script:NTEInboundLockDir = Join-Path $script:NTEInboundRoot 'Workflow\.cursor_autonomous_locks'
$script:NTEInboundMaxTasks = 120
$script:NTEInboundMaxBytes = 1048576  # 2026-09-27: headroom; prune bloated titles on save

# Files matching these MUST NOT be init-seeded as seen-only; they require ledger promotion.
$script:NTEInboundMandatoryPrefixPattern = '^(?i)(P0_|CONSOLIDATED_|PRIORITY_|DIRECTIVE_|Directive_|SEED_REISSUE_|ROOT_P0_)'

# Poll/execute HANDOFF path: legacy Handoff_* only — never replay mandatory directives as inbox handoffs.
# Legacy Cursor-addressed handoff pattern (still used for promote filters).
$script:NTEInboundHandoffOnlyPattern = '^Handoff_(AC|Jammer|CR|Claude(?:_[A-Za-z]+)?|PC|Scratch)_to_.*Cursor.*\.md$'

# Greg 2026-09-25: inventory ALL handoff-class files (any To:). Cursor Main must not miss PC→Greg / AC→PC traffic.
$script:NTEInboundListenPatterns = @(
  '^P0_.*\.md$'
  '^ROOT_P0_.*\.md$'
  '^CONSOLIDATED_.*\.md$'
  '^PRIORITY_.*\.md$'
  '^DIRECTIVE_.*\.md$'
  '^Directive_.*\.md$'
  '^SEED_.*\.md$'
  '^Handoff_.*\.md$'
  '^Arbitration_.*\.md$'
  '^Register_.*\.md$'
)

# Text-mined / stale ids → canonical ledger row (work already done under canonical id).
$script:NTEInboundCanonicalAliases = @{
  'CONSOLIDATED-CLEAN-BUILD-2026-06-23' = 'CONSOLIDATED-CLEAN-BUILD-V02-TRIO'
  'F1-P4-CLEAN-PDF-BUILD'             = 'CONSOLIDATED-CLEAN-BUILD-V02-TRIO'
}

$script:NTEInboundTerminalStates = @('VERIFIED', 'SUPERSEDED', 'BLOCKED_AC', 'FAILED')

$script:NTEInboundSkipNamePattern = 'CLOSED|HOLD|TERMINATED|VERIFIED|Verification|INSTRUCTION_Greg|_DRAINED_|Tick_FollowUp|Supervisor_Hourly_Status'

function Write-InboundLog([string]$Msg) {
  $line = ('{0} [inbound] {1}' -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $Msg)
  try { [System.IO.File]::AppendAllText($script:NTEInboundPromoteLog, $line + [Environment]::NewLine) } catch { }
}

function Test-InboundSkipFile([string]$FileName) {
  if ($FileName -match $script:NTEInboundSkipNamePattern) { return $true }
  if ($FileName -match '^Handoff_Cursor') { return $true }
  return $false
}

function Test-InboundMandatoryPromote([string]$FileName) {
  return ($FileName -match $script:NTEInboundMandatoryPrefixPattern)
}

function Test-InboundHandoffPollCandidate([string]$FileName) {
  if (Test-InboundSkipFile $FileName) { return $false }
  if (Test-InboundMandatoryPromote $FileName) { return $false }
  if ($FileName -match '^SEED_') { return $false }
  return ($FileName -match $script:NTEInboundHandoffOnlyPattern)
}

function Test-InboundFileMatches([string]$FileName) {
  if (Test-InboundSkipFile $FileName) { return $false }
  foreach ($pat in $script:NTEInboundListenPatterns) {
    if ($FileName -match $pat) { return $true }
  }
  return $false
}

function Get-InboundPollPattern([string]$Stream) {
  switch ($Stream) {
    'main' {
      # All handoff-class artifacts — To: line is NOT a filter (Greg 2026-09-25)
      return '(?i)^((P0_|ROOT_P0_|CONSOLIDATED_|PRIORITY_|DIRECTIVE_|Directive_|SEED_|Handoff_|Arbitration_|Register_).*)\.md$'
    }
    'ac_jammer' {
      return '(?i)^((SEED_.*Jammer|Handoff_.*(AC|Jammer|Scratch|Cursor)|Directive_.*(AC|Jammer|Scratch)|Arbitration_.*).*)\.md$'
    }
    'pc_scratch' {
      return '(?i)^((Handoff_.*(PC|Scratch)|Directive_.*Scratch|Handoff_AC_to_PC|Handoff_PC_).*)\.md$'
    }
    default { return $null }
  }
}

function Get-InboundTargetStream([string]$FileName) {
  if ($FileName -match '(?i)^Handoff_(PC|Scratch)_to_') { return 'pc_scratch' }
  if ($FileName -match '(?i)Jammer' -and $FileName -match '(?i)^Handoff_') { return 'ac_jammer' }
  if ($FileName -match '(?i)^Handoff_(Jammer|CR)_to_') { return 'ac_jammer' }
  if ($FileName -match '(?i)^Handoff_Claude_Jammer_to_') { return 'ac_jammer' }
  if ($FileName -match '(?i)SEED_.*Jammer') { return 'ac_jammer' }
  return 'main'
}

function Resolve-CanonicalLedgerId([string]$Id) {
  if ($script:NTEInboundCanonicalAliases.ContainsKey($Id)) {
    return $script:NTEInboundCanonicalAliases[$Id]
  }
  return $Id
}

function Test-StrictLedgerId([string]$Id) {
  if ($Id -match '-\d{4}-\d{2}-\d{2}$') { return $false }
  if ($Id -match '^INBOUND-') { return $false }
  return ($Id -match '^[A-Z][A-Z0-9]*(-[A-Z0-9.]+)+$' -and $Id.Length -ge 5)
}

function Get-LedgerFromDisk() {
  if (-not (Test-Path $script:NTEInboundLedgerPath)) { return $null }
  try {
    $raw = Get-Content $script:NTEInboundLedgerPath -Raw -ErrorAction Stop
    if ($raw.Length -gt ($script:NTEInboundMaxBytes * 4)) {
      Write-InboundLog "ledger_read_abort size=$($raw.Length)"
      return $null
    }
    return ($raw | ConvertFrom-Json)
  } catch {
    Write-InboundLog "ledger_read_fail $($_.Exception.Message)"
    return $null
  }
}

function New-EmptyInboundLedger([string]$Note = 'auto-created for directive promote') {
  return [pscustomobject]@{
    version = 1
    updated_at = (Get-Date -Format 'o')
    note = $Note
    tasks = @()
  }
}

function Ensure-LedgerOnDisk() {
  $ledger = Get-LedgerFromDisk
  if ($null -ne $ledger) { return $ledger }
  Write-InboundLog 'ledger_missing — creating empty Working/cursor_task_ledger.json'
  $ledger = New-EmptyInboundLedger 'Recreated — inbound promote_skip no_ledger prevention (2026-09-26)'
  Save-LedgerInbound $ledger | Out-Null
  return (Get-LedgerFromDisk)
}

function Merge-LedgerTasksById($ledger) {
  $rank = @{ VERIFIED = 6; SUPERSEDED = 5; BLOCKED_AC = 4; FAILED = 4; CLAIMED = 3; IN_PROGRESS = 3; QUEUED = 2; TODO = 2 }
  $best = @{}
  foreach ($t in @($ledger.tasks)) {
    $id = $t.id
    if (-not $id) { continue }
    if (-not (Test-StrictLedgerId $id)) { continue }
    if (-not $best.ContainsKey($id)) {
      $best[$id] = $t
      continue
    }
    $cur = $best[$id]
    $curRank = if ($rank.ContainsKey($cur.state)) { $rank[$cur.state] } else { 0 }
    $newRank = if ($rank.ContainsKey($t.state)) { $rank[$t.state] } else { 0 }
    if ($newRank -gt $curRank) { $best[$id] = $t }
  }
  $ledger.tasks = @($best.Values)
  return $ledger
}

function Save-LedgerInbound($ledger) {
  if ($null -eq $ledger) { return $false }
  if (-not (Test-Path $script:NTEInboundLockDir)) {
    New-Item -ItemType Directory -Path $script:NTEInboundLockDir -Force | Out-Null
  }
  $lockPath = Join-Path $script:NTEInboundLockDir 'ledger.promote.lock'
  $lock = $null
  try {
    $lock = [System.IO.File]::Open($lockPath, [System.IO.FileMode]::OpenOrCreate, [System.IO.FileAccess]::ReadWrite, [System.IO.FileShare]::None)
  } catch {
    Write-InboundLog "ledger_save_lock_busy"
    return $false
  }
  try {
    $ledger = Merge-LedgerTasksById $ledger
    if (@($ledger.tasks).Count -gt $script:NTEInboundMaxTasks) {
      Write-InboundLog "ledger_save_abort task_count=$(@($ledger.tasks).Count)"
      return $false
    }
    $ledger.updated_at = (Get-Date -Format 'o')
    # 2026-09-27: prevent ledger_save_abort from bloated titles (SEQ-GB had ~1.5MB title)
    foreach ($task in @($ledger.tasks)) {
      if ($null -ne $task.title -and $task.title.Length -gt 400) {
        $task.title = ($task.title.Substring(0, 200) + ' ...[truncated]')
      }
    }
    $json = $ledger | ConvertTo-Json -Depth 10
    if ($json.Length -gt $script:NTEInboundMaxBytes) {
      Write-InboundLog "ledger_save_abort bytes=$($json.Length)"
      return $false
    }
    [System.IO.File]::WriteAllText($script:NTEInboundLedgerPath, $json, [System.Text.UTF8Encoding]::new($false))
    return $true
  } finally {
    if ($null -ne $lock) { $lock.Dispose() }
  }
}

function Get-LedgerSpecForHandoff([string]$FileName, [string]$Text) {
  $specs = @()
  $stream = Get-InboundTargetStream $FileName
  $handoffRel = "Handoffs/$FileName"

  # NO text-mining — explicit filename maps only (prevents duplicate/stale ids).

  if ($FileName -match 'P5_TWOBRANCH_KEYWORDS|P5-TWOBRANCH-KEYWORDS|masssaw') {
    $specs += [pscustomobject]@{
      id = 'P5-TWOBRANCH-KEYWORDS-FIX'; stream = 'main'; priority = 5
      title = 'P5 two-branch keywords fix + rebuild + gate'
      source_handoff = $handoffRel
    }
  }
  if ($FileName -match 'Kappa_Trilogy|KAPPA-CLEAN|Kappa_Trilogy') {
    $specs += [pscustomobject]@{
      id = 'KAPPA-CLEAN-TRILOGY-PDF-BUILD'; stream = 'main'; priority = 5
      title = 'κ trilogy clean standalones PDF build'
      source_handoff = $handoffRel
    }
  }
  if ($FileName -match 'P5_Flux_Dial|FLUX.DIAL') {
    $specs += [pscustomobject]@{
      id = 'P5-FLUX-DIAL-WORKSHEET'; stream = 'ac_jammer'; priority = 5
      title = 'P5 flux-dial worksheet (fractional J-admixture + null control)'
      source_handoff = $handoffRel
    }
  }
  if ($FileName -match '^CONSOLIDATED_') {
    $specs += [pscustomobject]@{
      id = 'CONSOLIDATED-CLEAN-BUILD-V02-TRIO'; stream = 'main'; priority = 5
      title = 'Consolidated queue §A: heat-kernel + octonion + P4 v0.2 PDF builds'
      source_handoff = $handoffRel
    }
    $specs += [pscustomobject]@{
      id = 'CONSOLIDATED-DISPOSITION-BCD'; stream = 'main'; priority = 6
      title = 'Consolidated queue §B–D: archive demotions, F1 pedagogical fold, populate folder'
      source_handoff = $handoffRel
      blocked_by = @('CONSOLIDATED-CLEAN-BUILD-V02-TRIO', 'KAPPA-CLEAN-TRILOGY-PDF-BUILD', 'P5-TWOBRANCH-KEYWORDS-FIX')
    }
  }
  if ($FileName -match 'F1_v0_3_P4|F1-P4-CLEAN') {
    $specs += [pscustomobject]@{
      id = 'F1-P4-CLEAN-PDF-BUILD'; stream = 'main'; priority = 5
      title = 'F1 v0.3 + P4 v0.1 clean PDF build (superseded by consolidated v0.2 where applicable)'
      source_handoff = $handoffRel
      alias_of = 'CONSOLIDATED-CLEAN-BUILD-V02-TRIO'
    }
  }

  # AC / Cursor Main sunshine directives (Greg mandate: poll ALL handoffs → executable ledger work)
  # HARDENING 2026-09-26: match ALL Directive_AC_* (not only Directive_AC_to_ALL|Cursor).
  # Fault: Directive_AC_Does_NTE_Need_Inflation_... hit promote_skip no_specs and never reached lanes.
  if ($FileName -match '^Directive_AC_to_ALL_Sequencing_Contradiction') {
    $specs += [pscustomobject]@{
      id = 'SEQ-GB-INFLATION-SUNSHINE'; stream = 'main'; priority = 0
      title = 'Sequencing contradiction GB vs inflation — Cursor Main + pseudo lanes'
      source_handoff = $handoffRel
    }
  }
  elseif ($FileName -match '^Directive_AC_Does_NTE_Need_Inflation') {
    $specs += [pscustomobject]@{
      id = 'NTE-NEED-INFLATION-R1-SPECTRUM'; stream = 'main'; priority = 0
      title = 'Does NTE need inflation? Primary discriminator = perturbation spectrum (R1 first)'
      source_handoff = $handoffRel
    }
  }
  elseif ($FileName -match '^Directive_AC_(to_)?(ALL|Cursor|Claude|Scratch|Jammer)') {
    $safe = ($FileName -replace '^Directive_|\.md$','' -replace '[^A-Za-z0-9]+','-').ToUpperInvariant()
    if ($safe.Length -gt 48) { $safe = $safe.Substring(0, 48).TrimEnd('-') }
    $specs += [pscustomobject]@{
      id = "AC-DIR-$safe"; stream = 'main'; priority = 1
      title = "AC directive: $FileName"
      source_handoff = $handoffRel
    }
  }
    elseif ($FileName -match '^Directive_REISSUE_') {
    # 2026-09-27: REISSUE_* was hitting promote_skip no_specs (not AC_|Cursor_ prefix after Directive_)
    $safe = ($FileName -replace '^Directive_|\.md$','' -replace '[^A-Za-z0-9]+','-').ToUpperInvariant()
    if ($safe.Length -gt 48) { $safe = $safe.Substring(0, 48).TrimEnd('-') }
    $specs += [pscustomobject]@{
      id = "AC-DIR-$safe"; stream = 'main'; priority = 0
      title = "REISSUE directive: $FileName"
      source_handoff = $handoffRel
    }
  }
  elseif ($FileName -match '^Directive_(REISSUE_|AC_|Cursor_)') {
    # Catch-all for REISSUE_ / AC_ / Cursor_ Directive_* (2026-09-27: REISSUE was no_specs)
    $safe = ($FileName -replace '^Directive_|\.md$','' -replace '[^A-Za-z0-9]+','-').ToUpperInvariant()
    if ($safe.Length -gt 48) { $safe = $safe.Substring(0, 48).TrimEnd('-') }
    $specs += [pscustomobject]@{
      id = "AC-DIR-$safe"; stream = 'main'; priority = 1
      title = "Directive: $FileName"
      source_handoff = $handoffRel
    }
  }

  $seen = @{}
  $out = @()
  foreach ($s in $specs) {
    if (-not $seen.ContainsKey($s.id)) { $seen[$s.id] = $true; $out += $s }
  }
  return $out
}

function Get-LedgerTaskById($ledger, [string]$TaskId) {
  $hits = @($ledger.tasks | Where-Object { $_.id -eq $TaskId })
  if ($hits.Count -eq 0) { return $null }
  return $hits[0]
}

function Test-LedgerTaskDone($ledger, [string]$TaskId) {
  if ($null -eq $ledger -or -not $TaskId) { return $false }
  $canonical = Resolve-CanonicalLedgerId $TaskId
  foreach ($checkId in @($TaskId, $canonical)) {
    $t = Get-LedgerTaskById $ledger $checkId
    if ($null -eq $t) { continue }
    $st = ([string]$t.state).Trim()
    if ($st -eq 'VERIFIED' -or $st -eq 'SUPERSEDED' -or $st -eq 'BLOCKED_AC' -or $st -eq 'FAILED') {
      return $true
    }
  }
  return $false
}

function Test-LedgerTaskFulfilled($ledger, [string]$TaskId) {
  return (Test-LedgerTaskDone $ledger $TaskId)
}

function Test-InboundHandoffFulfilled($ledger, [string]$FileName) {
  if ($null -eq $ledger) { return $false }
  $path = Join-Path $script:NTEInboundHandoffs $FileName
  if (-not (Test-Path $path)) { return $false }
  $text = Get-Content $path -Raw
  $specs = Get-LedgerSpecForHandoff $FileName $text
  if ($specs.Count -eq 0) {
    $rel = "Handoffs/$FileName"
    $hit = @($ledger.tasks | Where-Object { $_.source_handoff -eq $rel -and $_.state -eq 'VERIFIED' })
    return ($hit.Count -gt 0)
  }
  foreach ($s in $specs) {
    if (-not (Test-LedgerTaskDone $ledger $s.id)) { return $false }
  }
  return $true
}

function Add-LedgerTaskIfMissing($ledger, $spec) {
  if (-not (Test-StrictLedgerId $spec.id)) {
    Write-InboundLog "promote_reject bad_id $($spec.id)"
    return 'reject'
  }
  if (Test-LedgerTaskDone $ledger $spec.id) {
    return 'done'
  }
  $existing = Get-LedgerTaskById $ledger $spec.id
  if ($null -ne $existing) {
    $st = ([string]$existing.state).Trim()
    if ($st -in @('VERIFIED', 'SUPERSEDED', 'QUEUED', 'TODO', 'CLAIMED', 'IN_PROGRESS', 'BLOCKED_AC', 'FAILED')) {
      return 'exists'
    }
  }
  $row = [ordered]@{
    id = $spec.id
    state = 'QUEUED'
    priority = if ($spec.priority) { [int]$spec.priority } else { 5 }
    stream = $spec.stream
    gate = 'zeroparam'
    title = $spec.title
    result_file_required = $true
    source_handoff = $spec.source_handoff
    promoted_at = (Get-Date -Format 'o')
    promoted_from = $spec.source_handoff
  }
  if ($spec.blocked_by) { $row.blocked_by = @($spec.blocked_by) }
  if ($spec.alias_of) { $row.alias_of = $spec.alias_of }
  $ledger.tasks += [pscustomobject]$row
  return 'added'
}

function Promote-InboundHandoffToLedger([string]$FileName) {
  if (Test-InboundSkipFile $FileName) { return @() }
  if (-not (Test-InboundMandatoryPromote $FileName) -and $FileName -notmatch 'P5_TWOBRANCH_KEYWORDS|P5-TWOBRANCH-KEYWORDS|masssaw|Kappa_Trilogy|KAPPA-CLEAN|P5_Flux_Dial|FLUX.DIAL|^CONSOLIDATED_') {
    Write-InboundLog "promote_skip non_mandatory $FileName"
    return @()
  }

  $ledger = Ensure-LedgerOnDisk
  if ($null -eq $ledger) {
    Write-InboundLog "promote_skip no_ledger $FileName"
    return @()
  }
  if (Test-InboundHandoffFulfilled $ledger $FileName) {
    Write-InboundLog "promote_skip fulfilled $FileName"
    return @()
  }

  $path = Join-Path $script:NTEInboundHandoffs $FileName
  if (-not (Test-Path $path)) { return @() }
  $text = Get-Content $path -Raw
  $specs = Get-LedgerSpecForHandoff $FileName $text
  if ($specs.Count -eq 0) {
    Write-InboundLog "promote_skip no_specs $FileName"
    return @()
  }

  $added = @()
  foreach ($spec in $specs) {
    if (Test-LedgerTaskDone $ledger $spec.id) { continue }
    $result = Add-LedgerTaskIfMissing $ledger $spec
    if ($result -eq 'added') {
      $added += $spec.id
      Write-InboundLog "promoted $($spec.id) <- $FileName"
    }
  }
  if ($added.Count -gt 0) { Save-LedgerInbound $ledger | Out-Null }
  return $added
}

function Scan-AndPromoteMandatoryInbounds([string]$Stream = 'main') {
  $promoted = @()
  if (-not (Test-Path $script:NTEInboundHandoffs)) { return $promoted }

  Get-ChildItem -Path $script:NTEInboundHandoffs -File -ErrorAction SilentlyContinue |
    Where-Object {
      $n = $_.Name
      -not (Test-InboundSkipFile $n) -and
      (Test-InboundMandatoryPromote $n) -and
      (((Get-InboundTargetStream $n) -eq $Stream) -or ($Stream -eq 'main'))
    } |
    Sort-Object LastWriteTime |
    ForEach-Object {
      $ids = Promote-InboundHandoffToLedger $_.Name
      if ($ids.Count -gt 0) { $promoted += $ids }
    }
  return $promoted
}

function Get-UnfulfilledMandatoryInbounds() {
  $ledger = Get-LedgerFromDisk
  $pending = @()
  if (-not (Test-Path $script:NTEInboundHandoffs)) { return $pending }

  Get-ChildItem -Path $script:NTEInboundHandoffs -File -ErrorAction SilentlyContinue |
    Where-Object {
      $n = $_.Name
      -not (Test-InboundSkipFile $n) -and
      (
        (Test-InboundMandatoryPromote $n) -or
        ($n -match '^Handoff_Claude_Jammer_to_.*Cursor') -or
        ($n -match '^SEED_(REISSUE_)?(AC|Greg)?_to_Cursor')
      )
    } |
    Sort-Object LastWriteTime -Descending |
    ForEach-Object {
      if (-not (Test-InboundHandoffFulfilled $ledger $_.Name)) {
        $pending += $_.Name
      }
    }
  return $pending
}

. (Join-Path $PSScriptRoot 'Resolve-NteRoots.ps1')

$wfRoot = $NteWorkflowRoot

