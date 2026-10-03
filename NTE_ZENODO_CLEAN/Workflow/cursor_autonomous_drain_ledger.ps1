# Drain cursor_task_ledger — queue next work to main chain (never self-supervision)
param(
  [ValidateSet('main', 'ac_jammer', 'pc_scratch')]
  [string]$Stream = 'main'
)

. (Join-Path $PSScriptRoot 'Resolve-NteRoots.ps1')
$root = $NteCorpusRoot


$ErrorActionPreference = 'Stop'

$ledgerPath = Join-Path $root 'Working\cursor_task_ledger.json'
$wf = Join-Path $root 'Workflow'
$chainDir = Join-Path $wf '.cursor_autonomous_chain'
$lockDir = Join-Path $wf '.cursor_autonomous_locks'
$grepPy = Join-Path $root 'Working\cursor_grep_gates.py'
$toggleScript = Join-Path $wf 'cursor_autonomous_toggle.ps1'
$logPath = Join-Path $wf '.cursor_autonomous_ledger.log'
$inboundLib = Join-Path $wf 'cursor_autonomous_inbound.ps1'
if (Test-Path $inboundLib) { . $inboundLib }

if (-not (Test-Path $ledgerPath)) {
  Write-Output 'LEDGER_MISSING'
  exit 2
}
if (-not (Test-Path $lockDir)) { New-Item -ItemType Directory -Path $lockDir -Force | Out-Null }
if (-not (Test-Path $chainDir)) { New-Item -ItemType Directory -Path $chainDir -Force | Out-Null }

function Write-LedgerLog([string]$Msg) {
  $line = ('{0} [ledger] {1}' -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $Msg)
  try { [System.IO.File]::AppendAllText($logPath, $line + [Environment]::NewLine) } catch { }
  Write-Output $line
}

function Save-Ledger($ledger) {
  if (Get-Command Save-LedgerInbound -ErrorAction SilentlyContinue) {
    if (-not (Save-LedgerInbound $ledger)) {
      Write-LedgerLog 'ledger_save_failed (lock/guard)'
    }
    return
  }
  $ledger.updated_at = (Get-Date -Format 'o')
  $json = $ledger | ConvertTo-Json -Depth 8
  [System.IO.File]::WriteAllText($ledgerPath, $json, [System.Text.UTF8Encoding]::new($false))
}

function Test-WorkerAlive([string]$Name) {
  $hit = Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" -ErrorAction SilentlyContinue |
    Where-Object { $_.CommandLine -like '*cursor_autonomous_poll.ps1*' -and $_.CommandLine -like "*-Stream $Name*" } |
    Select-Object -First 1
  return ($null -ne $hit)
}

function Reset-StrandedTasks($ledger) {
  $changed = $false
  foreach ($t in $ledger.tasks) {
    if ($t.state -in @('CLAIMED', 'IN_PROGRESS') -and $t.stream -eq $Stream) {
      $worker = if ($t.stream) { $t.stream } else { 'main' }
      if (-not (Test-WorkerAlive $worker)) {
        $t.state = 'QUEUED'
        $t | Add-Member -NotePropertyName reset_reason -NotePropertyValue 'dead_worker' -Force
        $changed = $true
        Write-LedgerLog ("reset stranded $($t.id) -> QUEUED (worker dead)")
      }
    }
  }
  if ($changed) { Save-Ledger $ledger }
}

function Get-Counts($ledger) {
  $states = @('QUEUED', 'TODO', 'CLAIMED', 'IN_PROGRESS', 'VERIFIED', 'BLOCKED_AC', 'FAILED')
  $counts = @{}
  foreach ($s in $states) { $counts[$s] = 0 }
  foreach ($t in $ledger.tasks) {
    if ($counts.ContainsKey($t.state)) { $counts[$t.state]++ }
  }
  return $counts
}

$ledger = Get-Content $ledgerPath -Raw | ConvertFrom-Json
Reset-StrandedTasks $ledger

$counts = Get-Counts $ledger
$blocked = @($ledger.tasks | Where-Object { $_.state -eq 'BLOCKED_AC' } | ForEach-Object { $_.id })
$countLine = ($counts.GetEnumerator() | Sort-Object Name | ForEach-Object { "$($_.Key)=$($_.Value)" }) -join ' '
Write-LedgerLog "counts $countLine"
if ($blocked.Count -gt 0) { Write-LedgerLog ("BLOCKED_AC: " + ($blocked -join ', ')) }

# Run gate report for tick (source + PDF artifact layers)
if (Test-Path $grepPy) {
  $gateOut = python $grepPy --gate mojibake --gate pdf-mojibake --gate kphi --gate kappa --gate a4 --gate eta --report 2>&1 | Out-String
  if ($gateOut -match '\[FAIL\]') {
    Write-LedgerLog ('gate_FAIL: ' + ($gateOut -replace '\s+', ' ').Substring(0, [Math]::Min(300, ($gateOut -replace '\s+', ' ').Length)))
  }
}

$next = $ledger.tasks |
  Where-Object {
    $_.state -in @('QUEUED', 'TODO') -and $_.stream -eq $Stream -and
    (-not $_.blocked_by -or @($_.blocked_by | ForEach-Object {
        $dep = $ledger.tasks | Where-Object { $_.id -eq $_ }
        $dep -and $dep.state -eq 'VERIFIED'
      }).Count -eq @($_.blocked_by).Count)
  } |
  Sort-Object priority, id |
  Select-Object -First 1

$alreadyClaimed = @($ledger.tasks | Where-Object { $_.state -eq 'CLAIMED' -and $_.stream -eq $Stream })
if ($alreadyClaimed.Count -gt 0) {
  $next = $alreadyClaimed[0]
  Write-LedgerLog ("resume CLAIMED $($next.id)")
} elseif (-not $next) {
  Write-Output "LEDGER_IDLE counts=$countLine"
  exit 0
} else {
  $next.state = 'CLAIMED'
  $next | Add-Member -NotePropertyName claimed_at -NotePropertyValue (Get-Date -Format 'o') -Force
  Save-Ledger $ledger
}

$title = if ($next.title) { $next.title } else { $next.id }
$prompt = @"
NTE CR2 autonomous chain — **drain ledger** (not supervisor self-report). **Sign as Cursor Main.**

**Task:** $($next.id) — $title
**State flow:** CLAIMED → execute → gate verify on disk → VERIFIED (or BLOCKED_AC after 3 fails)

**Hard rules:**
- ``Working/cursor_task_ledger.json`` is the single source of truth for WORK.
- ``.cursor_autonomous_seen_*`` = read tracking only; NEVER retires a task.
- DONE = gate PASS on actual post-edit file. Your say-so is not verification.
- OLD text mismatch → BLOCKED_AC; do not improvise.
- Patch Part 3 monolith AND AC split when both apply.

**This tick:** Execute $($next.id). Update ledger state. Report counts by state + any BLOCKED_AC + any gate FAIL.

Ledger path: Working/cursor_task_ledger.json
Verifier: python Working/cursor_grep_gates.py --gate <name> --report
PDF artifact (deposit carriers): python Working/pdf_artifact_gate.py --report
Calibration: Workflow/NTE_PDF_Artifact_Sight_Calibration_v0_1_20260618.md
"@


$chainFile = Join-Path $chainDir ("{0}.json" -f $Stream)
@{
  requested_at = (Get-Date -Format 'o')
  stream = $Stream
  item_id = $next.id
  title = "Ledger: $title"
  prompt = $prompt
} | ConvertTo-Json | Set-Content $chainFile -Encoding UTF8

Write-LedgerLog ("chain -> $Stream.json task=$($next.id)")
Write-Output "LEDGER_QUEUED task=$($next.id) counts=$countLine"

. (Join-Path $PSScriptRoot 'Resolve-NteRoots.ps1')

$wfRoot = $NteWorkflowRoot
