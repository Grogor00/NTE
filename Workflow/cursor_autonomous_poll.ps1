# NTE Cursor autonomous poll — parameterized stream worker
# Usage: -Stream main|ac_jammer|pc_scratch
# NOTE: .cursor_autonomous_seen_* tracks READING only — never retires work.
#       Task completion lives in Working/cursor_task_ledger.json (VERIFIED).
# Respects Workflow/.cursor_autonomous_toggle.json (Greg toggle off/on)

param(
  [Parameter(Mandatory = $true)]
  [ValidateSet('main', 'ac_jammer', 'pc_scratch')]
  [string]$Stream
)

. (Join-Path $PSScriptRoot 'Resolve-NteRoots.ps1')
$root = $NteCorpusRoot


$ErrorActionPreference = 'Stop'

$handoffs = Join-Path $root 'Handoffs'
$togglePath = Join-Path $root 'Workflow\.cursor_autonomous_toggle.json'
$inboundLib = Join-Path $root 'Workflow\cursor_autonomous_inbound.ps1'
if (Test-Path $inboundLib) { . $inboundLib }

# Greg 2026-09-25: poll must inventory ALL Handoffs (any To:), and flag Greg-attention items.
$allHandoffsPattern = '(?i)^(.*\.(md))$'  # narrowed in loop to Handoffs folder only
$config = @{
  main = @{
    Sentinel = 'AGENT_LOOP_TICK_cursor_main'
    StatePath = Join-Path $root 'Workflow\.cursor_autonomous_seen_main.json'
    # Main: every Handoff/Directive/Arbitration/Register — do not filter on To: Cursor
    Pattern = if (Get-Command Get-InboundPollPattern -ErrorAction SilentlyContinue) { Get-InboundPollPattern 'main' } else { '(?i)^((P0_|ROOT_P0_|CONSOLIDATED_|PRIORITY_|DIRECTIVE_|SEED_|Handoff_|Directive_|Arbitration_|Register_|Directive_).*)\.md$' }
    Identity = 'Cursor Main'
    IdlePrompt = 'CR2 MAIN (sign as **Cursor Main**): **Read ALL new/updated Handoffs regardless of To:**; apply Cursor-executable work; flag Greg-attention (PROPOSED / awaiting Greg / DO NOT APPLY) in Working/.cursor_handoff_greg_flags.md; promote mandatory inbound then drain.'
    SweepAllHandoffs = $true
  }
  ac_jammer = @{
    Sentinel = 'AGENT_LOOP_TICK_cursor_ac_jammer'
    StatePath = Join-Path $root 'Workflow\.cursor_autonomous_seen_ac_jammer.json'
    Pattern = if (Get-Command Get-InboundPollPattern -ErrorAction SilentlyContinue) { Get-InboundPollPattern 'ac_jammer' } else { '(?i)^((SEED_.*Jammer|Handoff_(AC|Jammer|CR|Claude).*|Directive_.*Jammer|Directive_.*Scratch|Handoff_.*Scratch|Handoff_.*Jammer).*)\.md$' }
    Identity = 'Cursor AC or Cursor Jammer (match inbound From:)'
    IdlePrompt = 'CR2 AC/JAMMER: poll AC/Jammer/Scratch directives + handoffs (all To: lines that name AC/Jammer/Scratch/Cursor); promote ledger rows then drain; honor AC OVERRIDE; run §II.0 / item-(a) investigations when directed.'
    SweepAllHandoffs = $true
  }
  pc_scratch = @{
    Sentinel = 'AGENT_LOOP_TICK_cursor_pc_scratch'
    StatePath = Join-Path $root 'Workflow\.cursor_autonomous_seen_pc_scratch.json'
    Pattern = '(?i)^((Handoff_(PC|Scratch)_.*|Directive_.*Scratch|Handoff_.*_to_.*PC|Handoff_AC_to_PC).*)\.md$'
    Identity = 'Cursor PC or Cursor Scratch (match inbound From:)'
    IdlePrompt = 'CR2 PC/SCRATCH: **Sunshine/Rabbit Hole FIRST**; poll PC/Scratch handoffs (all To:); campaign grep; no bridge while sunshine pending.'
    SweepAllHandoffs = $true
  }
}

function Get-Toggle {
  if (-not (Test-Path $togglePath)) { return @{ enabled = $true; streams = @{} } }
  try { return (Get-Content $togglePath -Raw | ConvertFrom-Json) } catch { return @{ enabled = $true; streams = @{} } }
}

function Stream-Enabled {
  param($Toggle)
  if (-not $Toggle.enabled) { return $false }
  $s = $Toggle.streams.$Stream
  if ($null -eq $s) { return $true }
  return [bool]$s.enabled
}

function Get-TickSeconds {
  param($Toggle)
  $defaults = @{ main = 3; ac_jammer = 5; pc_scratch = 7 }
  $def = $defaults[$Stream]
  $s = $Toggle.streams.$Stream
  if ($null -ne $s -and $null -ne $s.tick_minutes) { return [int]$s.tick_minutes * 60 }
  return $def * 60
}

function Load-Seen {
  param([string]$Path)
  # Values: ISO mtime string (preferred) or $true (legacy name-only)
  $seen = @{}
  if (Test-Path $Path) {
    try {
      $raw = Get-Content $Path -Raw -Encoding UTF8
      $loaded = $raw | ConvertFrom-Json
      if ($loaded -is [System.Array] -or $loaded.PSObject.TypeNames -contains 'System.Object[]') {
        foreach ($p in @($loaded)) {
          if ($null -ne $p -and "$p" -ne '') { $seen["$p"] = $true }
        }
      } elseif ($loaded -is [string]) {
        $seen[$loaded] = $true
      } else {
        # object map: name -> mtime (or bool)
        foreach ($p in $loaded.PSObject.Properties) {
          $seen[$p.Name] = [string]$p.Value
        }
      }
    } catch { }
  }
  return $seen
}

function Save-Seen {
  param([hashtable]$Seen, [string]$Path)
  # Persist name -> mtime so Directive updates re-trigger
  $obj = [ordered]@{}
  foreach ($k in @($Seen.Keys | Sort-Object)) {
    $obj[$k] = [string]$Seen[$k]
  }
  ($obj | ConvertTo-Json -Depth 4) | Set-Content $Path -Encoding UTF8
}

function Test-SeenNeedsFire {
  param([hashtable]$Seen, [System.IO.FileInfo]$File, [bool]$Mandatory)
  $name = $File.Name
  $stamp = $File.LastWriteTime.ToString('o')
  if (-not $Seen.ContainsKey($name)) { return $true }
  if (-not $Mandatory) { return $false }  # legacy: name-only fire once for ordinary handoffs
  $prev = [string]$Seen[$name]
  if ($prev -eq 'True' -or $prev -eq 'true' -or $prev -eq '') {
    # Upgrading legacy bool → fire once more so mtime gets recorded; after that only mtime deltas fire
    return $true
  }
  return ($prev -ne $stamp)
}

function Test-MandatoryName([string]$Name) {
  return ($Name -match '(?i)^(Directive_|DIRECTIVE_|P0_|ROOT_P0_|CONSOLIDATED_|PRIORITY_|SEED_REISSUE_)' -or
          $Name -match '(?i)Sunshine|Rabbit.?Hole')
}

$c = $config[$Stream]
$execScript = Join-Path $root 'Workflow\cursor_autonomous_execute_tick.ps1'
$tick = Get-TickSeconds (Get-Toggle)
$seen = Load-Seen $c.StatePath
$initSeed = -not (Test-Path $c.StatePath)

if ($initSeed -and $c.Pattern) {
  Get-ChildItem -Path $handoffs -File | Where-Object { $_.Name -match $c.Pattern } | ForEach-Object {
    # Seed with mtime so later updates to Directive_* still fire
    $seen[$_.Name] = $_.LastWriteTime.ToString('o')
  }
}

Write-Output ($c.Sentinel + ' {"event":"start","stream":"' + $Stream + '","tick_min":' + ($tick / 60) + ',"programme":"CR2"}')

if (Test-Path $execScript) {
  & $execScript -Stream $Stream 2>&1 | ForEach-Object { Write-Output $_ }
}

while ($true) {
  $toggle = Get-Toggle
  if (-not (Stream-Enabled $toggle)) {
    Write-Output ($c.Sentinel + ' {"event":"stopped","stream":"' + $Stream + '","reason":"toggle off"}')
    break
  }

  $tick = Get-TickSeconds $toggle
  Start-Sleep -Seconds $tick

  try {
    # Universal inventory + Greg-attention board (all To: lines)
    $sweepLib = Join-Path $PSScriptRoot 'cursor_autonomous_handoff_sweep.ps1'
    if ($c.SweepAllHandoffs) {
      if (-not (Test-Path $sweepLib)) {
        Write-Output ($c.Sentinel + ' {"event":"error","stream":"' + $Stream + '","error":"HANDOFF_SWEEP_MISSING lib=' + $sweepLib.Replace('\','\\') + ' — poll is not on canonical Workflow"}')
        $stallAlert = Join-Path $root 'Working\.cursor_handoff_sweep_STALL.md'
        $stallMsg = "# Handoff sweep MISSING`n`nPoll stream=$Stream PSScriptRoot=$PSScriptRoot`nExpected: $sweepLib`nFix: launch auto.ps1 only from C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Workflow (OneDrive is not used).`n"
        [System.IO.File]::WriteAllText($stallAlert, $stallMsg, [System.Text.UTF8Encoding]::new($false))
      } else {
        . $sweepLib
        Invoke-NteHandoffSweep -Stream $Stream -Quiet
        # Stall check: sweep state must advance
        $sweepStatePath = Join-Path $root 'Working\.cursor_handoff_sweep_state.json'
        if (Test-Path $sweepStatePath) {
          try {
            $ss = Get-Content $sweepStatePath -Raw -Encoding UTF8 | ConvertFrom-Json
            if ($ss.last_poll) {
              $lp = [datetime]::Parse([string]$ss.last_poll)
              $age = ((Get-Date) - $lp).TotalMinutes
              if ($age -gt (2.0 * ($tick / 60.0))) {
                Write-Output ($c.Sentinel + ' {"event":"sweep_stall","stream":"' + $Stream + '","age_min":' + [math]::Round($age,1) + ',"last_poll":"' + $ss.last_poll + '"}')
              }
            }
          } catch { }
        }
      }
    }

    # Drain sweep auto-queue (Directive_/ALL) even if filename was previously seen
    $execQueuePath = Join-Path $root 'Working\.cursor_handoff_execute_queue.json'
    if ((Test-Path $execQueuePath) -and (Test-Path $execScript)) {
      try {
        $qraw = Get-Content $execQueuePath -Raw -Encoding UTF8
        $qitems = @($qraw | ConvertFrom-Json)
        foreach ($qi in $qitems) {
          if (-not $qi.file) { continue }
          if ($qi.stream -and $qi.stream -ne $Stream -and -not ($Stream -eq 'main' -and $qi.stream -eq 'main')) {
            if ($qi.stream -ne $Stream) { continue }
          }
          Write-Output ($c.Sentinel + ' {"event":"sweep_auto_queue","stream":"' + $Stream + '","file":"' + $qi.file + '"}')
          & $execScript -Stream $Stream -HandoffFile $qi.file 2>&1 | ForEach-Object { Write-Output $_ }
          $seen[$qi.file] = (Get-Item (Join-Path $handoffs $qi.file) -ErrorAction SilentlyContinue).LastWriteTime.ToString('o')
          if (-not $seen[$qi.file]) { $seen[$qi.file] = [string]$qi.last_write }
        }
        if ($qitems.Count -gt 0 -and $Stream -eq 'main') {
          Set-Content $execQueuePath -Value '[]' -Encoding UTF8
        }
      } catch {
        Write-Output ($c.Sentinel + ' {"event":"error","stream":"' + $Stream + '","error":"exec_queue: ' + $_.Exception.Message + '"}')
      }
    }

    $newAny = $false
    if ($c.Pattern) {
      Get-ChildItem -Path $handoffs -File -ErrorAction Stop |
        Where-Object {
          if ($_.Name -notmatch $c.Pattern) { return $false }
          # Main stream: do NOT drop non-Cursor To: lines (Greg 2026-09-25)
          if ($Stream -eq 'main') { return $true }
          if (Get-Command Test-InboundHandoffPollCandidate -ErrorAction SilentlyContinue) {
            return (Test-InboundHandoffPollCandidate $_.Name)
          }
          if (Get-Command Test-InboundMandatoryPromote -ErrorAction SilentlyContinue) {
            if (Test-InboundMandatoryPromote $_.Name) { return $false }
          }
          return $true
        } |
        Sort-Object LastWriteTime |
        ForEach-Object {
          $mandatory = Test-MandatoryName $_.Name
          if (Test-SeenNeedsFire -Seen $seen -File $_ -Mandatory:$mandatory) {
            $seen[$_.Name] = $_.LastWriteTime.ToString('o')
            $newAny = $true
            $evt = if ($mandatory) { 'handoff_mandatory' } else { 'handoff' }
            Write-Output ($c.Sentinel + ' {"event":"' + $evt + '","stream":"' + $Stream + '","file":"' + $_.Name + '","tick_min":' + ($tick / 60) + '}')
            if (Test-Path $execScript) {
              & $execScript -Stream $Stream -HandoffFile $_.Name 2>&1 | ForEach-Object { Write-Output $_ }
            }
          }
        }
    }
    if (-not $newAny) {
      $esc = $c.IdlePrompt -replace '"', '\"'
      Write-Output ($c.Sentinel + ' {"event":"idle","stream":"' + $Stream + '","prompt":"' + $esc + '","tick_min":' + ($tick / 60) + ',"programme":"CR2"}')
    }
    if (Test-Path $execScript) {
      & $execScript -Stream $Stream 2>&1 | ForEach-Object { Write-Output $_ }
    }
    Save-Seen $seen $c.StatePath
  } catch {
    Write-Output ($c.Sentinel + ' {"event":"error","stream":"' + $Stream + '","error":"' + $_.Exception.Message + '"}')
    Start-Sleep -Seconds 60
  }
}
