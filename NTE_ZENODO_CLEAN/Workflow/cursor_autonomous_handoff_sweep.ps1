# Universal Handoffs sweep for AFK Cursor Main (and any stream that calls it).
# Reads ALL new/updated files under Handoffs\ regardless of To: line.
# Classifies Cursor-executable work vs Greg-attention flags vs inventory notes.
# HARDENING 2026-09-26: Directive_*/To:ALL/To:Cursor always queue Main chain
#   (inventory alone is not sufficient — write execute queue + chain file).
#
#   . .\cursor_autonomous_handoff_sweep.ps1
#   Invoke-NteHandoffSweep -Stream main

function Invoke-NteHandoffSweep {
  param(
    [ValidateSet('main', 'ac_jammer', 'pc_scratch', 'supervisor')]
    [string]$Stream = 'main',
    [switch]$Quiet
  )

  if (-not $NteCorpusRoot) {
    . (Join-Path $PSScriptRoot 'Resolve-NteRoots.ps1')
  }
  $corpus = $NteCorpusRoot
  $wf = Join-Path $corpus 'Workflow'

  $handoffsDir = Join-Path $corpus 'Handoffs'
  $workingDir = Join-Path $corpus 'Working'
  $statePath = Join-Path $workingDir '.cursor_handoff_sweep_state.json'
  $flagsPath = Join-Path $workingDir '.cursor_handoff_greg_flags.md'
  $watchPath = Join-Path $workingDir '.cursor_handoff_watch_state.json'
  $execQueuePath = Join-Path $workingDir '.cursor_handoff_execute_queue.json'
  $stallPath = Join-Path $workingDir '.cursor_handoff_sweep_STALL.md'
  $chainDir = Join-Path $wf '.cursor_autonomous_chain'
  $inboxDir = Join-Path $wf '.cursor_autonomous_agent_inbox'

  if (-not (Test-Path $handoffsDir)) {
    Write-Output 'HANDOFF_SWEEP_FAIL missing Handoffs'
    return
  }
  if (-not (Test-Path $chainDir)) { New-Item -ItemType Directory -Path $chainDir -Force | Out-Null }
  if (-not (Test-Path $inboxDir)) { New-Item -ItemType Directory -Path $inboxDir -Force | Out-Null }

  $prevSeen = @{}
  $lastPoll = [datetime]'1970-01-01T00:00:00'
  if (Test-Path $statePath) {
    try {
      $loaded = Get-Content $statePath -Raw -Encoding UTF8 | ConvertFrom-Json
      if ($loaded.last_poll) { $lastPoll = [datetime]::Parse([string]$loaded.last_poll) }
      if ($loaded.seen) {
        foreach ($p in $loaded.seen.PSObject.Properties) { $prevSeen[$p.Name] = [string]$p.Value }
      }
    } catch { }
  }

  $now = Get-Date
  # Stall self-check: if prior last_poll is older than 6 minutes, raise alert file
  if ($lastPoll -gt [datetime]'1970-01-01T00:00:01') {
    $ageMin = ($now - $lastPoll).TotalMinutes
    if ($ageMin -gt 6) {
      $stallBody = @"
# Handoff sweep STALL alert

Detected: $($now.ToString('yyyy-MM-dd HH:mm:ss'))
Prior last_poll: $($lastPoll.ToString('yyyy-MM-dd HH:mm:ss'))
Age minutes: $([math]::Round($ageMin, 1))
Stream now: $Stream
Corpus: ``$corpus``

Rule: sweep last_poll must advance every poll tick (~3m main). If this file persists, poll workers are not running the canonical Workflow (launch auto.ps1 from C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Workflow only).
"@
      [System.IO.File]::WriteAllText($stallPath, $stallBody, [System.Text.UTF8Encoding]::new($false))
      Write-Output ("HANDOFF_SWEEP_STALL age_min={0:N1} last_poll={1}" -f $ageMin, $lastPoll.ToString('o'))
    } elseif (Test-Path $stallPath) {
      Remove-Item $stallPath -Force -ErrorAction SilentlyContinue
    }
  }

  $files = @(Get-ChildItem $handoffsDir -Filter '*.md' -File -ErrorAction SilentlyContinue | Sort-Object LastWriteTime)

  # Cold start: empty seen map => baseline inventory only (do not flood Greg with history).
  $coldStart = ($prevSeen.Count -eq 0)

  $newOrUpdated = @()
  if (-not $coldStart) {
    foreach ($f in $files) {
      $stamp = $f.LastWriteTime.ToString('o')
      $prevStamp = $prevSeen[$f.Name]
      if (-not $prevStamp -or $f.LastWriteTime -gt $lastPoll -or $prevStamp -ne $stamp) {
        $newOrUpdated += $f
      }
    }
  }

  $gregFlags = New-Object System.Collections.Generic.List[string]
  $cursorApply = New-Object System.Collections.Generic.List[string]
  $routeNotes = New-Object System.Collections.Generic.List[string]
  $mustExecute = New-Object System.Collections.Generic.List[object]
  $seenNow = @{}
  foreach ($f in $files) { $seenNow[$f.Name] = $f.LastWriteTime.ToString('o') }

  $gregPatterns = @(
    '(?i)awaiting Greg',
    '(?i)awaits Greg',
    '(?i)PROPOSED\s*[-]+\s*not ratified',
    '(?i)Status:\s*PROPOSED',
    '(?i)\*\*PROPOSED\*\*',
    '(?i)DO NOT APPLY',
    '(?i)do-not-apply',
    '(?i)Greg.?s (ruling|call|decision|ratification)',
    '(?i)needs Greg',
    '(?i)Greg to (rule|ratify|decide)',
    '(?i)awaiting ratification'
  )

  function Test-MandatoryAutoQueue([string]$Name, [string]$Head) {
    if ($Name -match '^(?i)(Directive_|DIRECTIVE_|P0_|ROOT_P0_|CONSOLIDATED_|PRIORITY_|SEED_REISSUE_)') { return $true }
    if ($Name -match '(?i)Sunshine|Rabbit.?Hole') { return $true }
    if ($Head -match '(?im)^\*\*To:\*\*\s*.*\b(ALL|Cursor(\s+Main)?)\b') { return $true }
    if ($Head -match '(?im)^To:\s*.*\b(ALL|Cursor(\s+Main)?)\b') { return $true }
    return $false
  }

  function Get-QueueTargetStream([string]$Name) {
    if ($Name -match '(?i)^Handoff_(PC|Scratch)_to_') { return 'pc_scratch' }
    if ($Name -match '(?i)Jammer' -and $Name -match '(?i)^Handoff_') { return 'ac_jammer' }
    if ($Name -match '(?i)^Handoff_(Jammer|CR)_to_') { return 'ac_jammer' }
    if ($Name -match '(?i)SEED_.*Jammer') { return 'ac_jammer' }
    if ($Name -match '(?i)Directive_.*Jammer' -and $Name -notmatch '(?i)ALL|Cursor') { return 'ac_jammer' }
    return 'main'
  }

  foreach ($f in $newOrUpdated) {
    if ($f.Name -match '^Handoff_Cursor') { continue }

    $head = $f.Name
    try {
      $raw = Get-Content $f.FullName -TotalCount 100 -Encoding UTF8 -ErrorAction Stop
      $head = ($raw -join "`n")
    } catch { }

    $needsGreg = $false
    foreach ($gp in $gregPatterns) {
      if ($head -match $gp -or $f.Name -match '(?i)DRAFT|PROPOSED|for_Greg|Awaiting_Greg') {
        $needsGreg = $true
        break
      }
    }

    $forCursor = $false
    if ($f.Name -match '(?i)Cursor' -or $head -match '(?i)To:\s*.*Cursor|(?i)then Cursor|(?i)Cursor \(apply\)|(?m)^OLD:') {
      $forCursor = $true
    }

    $autoQueue = Test-MandatoryAutoQueue $f.Name $head
    # Directives / ALL always queue even if body mentions PROPOSED for a sub-item
    if ($autoQueue) {
      $forCursor = $true
      $target = Get-QueueTargetStream $f.Name
      [void]$mustExecute.Add([pscustomobject]@{
          file         = $f.Name
          stream       = $target
          reason       = 'directive_or_all_or_sunshine'
          last_write   = $f.LastWriteTime.ToString('o')
          queued_at    = $now.ToString('o')
        })
    }

    $line = ('- `{0}` ({1:yyyy-MM-dd HH:mm})' -f $f.Name, $f.LastWriteTime)

    if ($needsGreg -and -not $autoQueue) {
      [void]$gregFlags.Add("$line - **Greg attention** (decision / ratification / do-not-apply)")
      Write-Output ("HANDOFF_SWEEP_GREG_FLAG file=" + $f.Name)
    } elseif ($needsGreg -and $autoQueue) {
      [void]$gregFlags.Add("$line - Greg flags present BUT auto-queued (Directive/ALL)")
      Write-Output ("HANDOFF_SWEEP_GREG_FLAG_AND_QUEUE file=" + $f.Name)
    }
    if ($forCursor) {
      [void]$cursorApply.Add("$line - Cursor-relevant")
      Write-Output ("HANDOFF_SWEEP_CURSOR file=" + $f.Name)
    }
    if ($autoQueue) {
      Write-Output ("HANDOFF_SWEEP_AUTO_QUEUE file=" + $f.Name + " stream=" + (Get-QueueTargetStream $f.Name))
    }
    if (-not $needsGreg -and -not $forCursor) {
      [void]$routeNotes.Add("$line - inventoried (read-all rule)")
      Write-Output ("HANDOFF_SWEEP_NOTED file=" + $f.Name)
    }
  }

  # Persist execute queue (ToArray avoids PS 5.1 List[object] @() cast failure)
  $queueRows = @($mustExecute.ToArray())
  if ($queueRows.Count -gt 0) {
    if ($queueRows.Count -eq 1) {
      # ConvertTo-Json scalar unwrap — force array
      ,$queueRows | ConvertTo-Json -Depth 5 | Set-Content $execQueuePath -Encoding UTF8
    } else {
      ($queueRows | ConvertTo-Json -Depth 5) | Set-Content $execQueuePath -Encoding UTF8
    }

    # Highest-priority: write Main (or target) chain so stop-hook / execute path cannot miss it.
    # Prefer To:ALL / Sunshine / RabbitHole over ordinary Directive_*.
    $mainRows = @($queueRows | Where-Object { $_.stream -eq 'main' })
    $pick = @(
      $mainRows | Where-Object { $_.file -match '(?i)_to_ALL_|Sunshine|Rabbit.?Hole' } | Select-Object -First 1
    )
    if ($pick.Count -eq 0) { $pick = @($mainRows | Select-Object -First 1) }
    if ($pick.Count -eq 0) { $pick = @($queueRows | Select-Object -First 1) }
    $row = $pick[0]
    $handoffPath = Join-Path $handoffsDir $row.file
    if (Test-Path $handoffPath) {
      $txt = Get-Content $handoffPath -Raw -Encoding UTF8
      $idMap = @{
        main = 'Cursor Main'
        ac_jammer = 'Cursor AC or Cursor Jammer'
        pc_scratch = 'Cursor PC or Cursor Scratch'
      }
      $label = $idMap[$row.stream]
      if (-not $label) { $label = 'Cursor Main' }
      $prompt = @"
CR2 $($row.stream) MANDATORY auto-queue from handoff sweep: $($row.file)

**Corpus identity:** Sign as **$label**. Standard: Workflow/NTE_Cursor_Agent_Identity_Standard_v0_1_20260601.md

Execute this Directive/ALL/Sunshine handoff now. Do not inventory-only.

---

$txt
"@
      $chainFile = Join-Path $chainDir ("{0}.json" -f $row.stream)
      @{
        requested_at = $now.ToString('o')
        stream       = $row.stream
        item_id      = 'SWEEP-AUTO'
        title        = $row.file
        prompt       = $prompt
        source       = 'handoff_sweep_auto_queue'
      } | ConvertTo-Json | Set-Content $chainFile -Encoding UTF8

      $inboxFile = Join-Path $inboxDir ("{0}.md" -f $row.stream)
      Set-Content -Path $inboxFile -Value $prompt -Encoding UTF8
      Write-Output ("HANDOFF_SWEEP_CHAIN_WRITTEN stream={0} file={1}" -f $row.stream, $row.file)
    }
  } elseif (Test-Path $execQueuePath) {
    # Clear stale empty queue only when we had a delta pass with nothing mandatory
    if (-not $coldStart) {
      Set-Content $execQueuePath -Value '[]' -Encoding UTF8
    }
  }

  $nl = "`r`n"
  $sb = New-Object System.Text.StringBuilder
  [void]$sb.AppendLine('# Cursor Main - Greg attention board')
  [void]$sb.AppendLine('')
  [void]$sb.AppendLine(('Updated: {0:yyyy-MM-dd HH:mm:ss} (handoff sweep, stream={1})' -f $now, $Stream))
  [void]$sb.AppendLine(('Corpus: `{0}`' -f $corpus))
  [void]$sb.AppendLine('')
  [void]$sb.AppendLine('## Rule')
  [void]$sb.AppendLine('Sweep reads **all** `Handoffs\*.md` each poll tick, regardless of To: line.')
  [void]$sb.AppendLine('Anything awaiting Greg / PROPOSED / DO NOT APPLY is listed until cleared.')
  [void]$sb.AppendLine('`Directive_*` / To:ALL / Sunshine always auto-queue Main chain (not inventory-only).')
  [void]$sb.AppendLine('')
  [void]$sb.AppendLine('## New / updated since last sweep - Greg flags')
  [void]$sb.AppendLine('')
  if ($coldStart) {
    [void]$sb.AppendLine(('_Cold-start baseline: {0} handoffs inventoried; Greg flags begin on next delta._' -f $files.Count))
  } elseif ($gregFlags.Count -eq 0) { [void]$sb.AppendLine('_None this tick._') }
  else { foreach ($g in $gregFlags) { [void]$sb.AppendLine($g) } }
  [void]$sb.AppendLine('')
  [void]$sb.AppendLine('## New / updated - Cursor-relevant')
  [void]$sb.AppendLine('')
  if ($cursorApply.Count -eq 0) { [void]$sb.AppendLine('_None this tick._') }
  else { foreach ($c in $cursorApply) { [void]$sb.AppendLine($c) } }
  [void]$sb.AppendLine('')
  [void]$sb.AppendLine('## Auto-queued for execute (Directive/ALL/Sunshine)')
  [void]$sb.AppendLine('')
  if ($mustExecute.Count -eq 0) { [void]$sb.AppendLine('_None this tick._') }
  else { foreach ($m in $mustExecute) { [void]$sb.AppendLine(('- `{0}` -> {1} ({2})' -f $m.file, $m.stream, $m.reason)) } }
  [void]$sb.AppendLine('')
  [void]$sb.AppendLine('## New / updated - inventoried (other)')
  [void]$sb.AppendLine('')
  if ($routeNotes.Count -eq 0) { [void]$sb.AppendLine('_None this tick._') }
  else { foreach ($r in $routeNotes) { [void]$sb.AppendLine($r) } }
  [void]$sb.AppendLine('')
  [void]$sb.AppendLine('## Persistent open queue (from watch state)')
  [void]$sb.AppendLine('')
  if (Test-Path $watchPath) {
    try {
      $w = Get-Content $watchPath -Raw -Encoding UTF8 | ConvertFrom-Json
      if ($w.open_queue -and @($w.open_queue).Count -gt 0) {
        foreach ($q in @($w.open_queue)) { [void]$sb.AppendLine("- $q") }
      } else { [void]$sb.AppendLine('_Empty._') }
    } catch { [void]$sb.AppendLine('_Watch state unreadable._') }
  } else { [void]$sb.AppendLine('_No watch state file._') }
  [void]$sb.AppendLine('')
  [void]$sb.AppendLine('- Cursor Main handoff sweep')
  [void]$sb.AppendLine('')

  [System.IO.File]::WriteAllText($flagsPath, $sb.ToString(), [System.Text.UTF8Encoding]::new($false))

  $stateObj = [ordered]@{
    last_poll       = $now.ToString('yyyy-MM-ddTHH:mm:ss+12:00')
    stream          = $Stream
    scanned         = $files.Count
    delta           = $newOrUpdated.Count
    greg_flag_count = $gregFlags.Count
    cursor_count    = $cursorApply.Count
    auto_queue_count = $mustExecute.Count
    seen            = $seenNow
  }
  ($stateObj | ConvertTo-Json -Depth 6) | Set-Content $statePath -Encoding UTF8

  if (-not $Quiet) {
    if ($coldStart) {
      Write-Output ("HANDOFF_SWEEP_OK cold_start_baseline scanned={0} delta=0 greg_flags=0 cursor=0 auto_queue=0" -f $files.Count)
    } else {
      Write-Output ("HANDOFF_SWEEP_OK scanned={0} delta={1} greg_flags={2} cursor={3} auto_queue={4}" -f $files.Count, $newOrUpdated.Count, $gregFlags.Count, $cursorApply.Count, $mustExecute.Count)
    }
  }
}
