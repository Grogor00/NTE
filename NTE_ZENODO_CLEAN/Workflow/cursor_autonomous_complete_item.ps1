# Mark a CR2 execution queue item complete and clear stream chain/inbox
param(
  [Parameter(Mandatory = $true)]
  [ValidateSet('main', 'ac_jammer', 'pc_scratch')]
  [string]$Stream,
  [Parameter(Mandatory = $true)]
  [string]$ItemId
)

. (Join-Path $PSScriptRoot 'Resolve-NteRoots.ps1')
$root = $NteCorpusRoot



$queuePath = Join-Path $root 'Working\NTE_CR2_Execution_Queue.json'
$wf = Join-Path $root 'Workflow'
$chainFile = Join-Path $wf ".cursor_autonomous_chain\$Stream.json"
$inboxFile = Join-Path $wf ".cursor_autonomous_agent_inbox\$Stream.md"

if (Test-Path $queuePath) {
  $queue = Get-Content $queuePath -Raw | ConvertFrom-Json
  foreach ($item in $queue.items) {
    if ($item.id -eq $ItemId -and $item.stream -eq $Stream) {
      $item.status = 'completed'
      $item | Add-Member -NotePropertyName completed_at -NotePropertyValue (Get-Date -Format 'yyyy-MM-dd HH:mm:ss') -Force
    }
  }
  [System.IO.File]::WriteAllText($queuePath, ($queue | ConvertTo-Json -Depth 6), [System.Text.UTF8Encoding]::new($false))
}

if (Test-Path $chainFile) { Remove-Item $chainFile -Force -ErrorAction SilentlyContinue }
if (Test-Path $inboxFile) { Remove-Item $inboxFile -Force -ErrorAction SilentlyContinue }

$registryPath = Join-Path $root 'Working\NTE_CR2_Open_Work_Registry.json'
if (Test-Path $registryPath) {
  try {
    $reg = Get-Content $registryPath -Raw | ConvertFrom-Json
    foreach ($b in $reg.backlog) {
      if ($b.id -eq $ItemId) {
        $b.status = 'completed'
        $b | Add-Member -NotePropertyName completed_at -NotePropertyValue (Get-Date -Format 'yyyy-MM-dd HH:mm:ss') -Force
      }
    }
    [System.IO.File]::WriteAllText($registryPath, ($reg | ConvertTo-Json -Depth 6), [System.Text.UTF8Encoding]::new($false))
    $pendingLeft = @($reg.backlog | Where-Object { $_.status -eq 'pending' })
    if ($pendingLeft.Count -eq 0 -and -not $reg.programme_closed) {
      $replenishScript = Join-Path $wf 'cursor_autonomous_replenish_registry.ps1'
      if (Test-Path $replenishScript) {
        & $replenishScript 2>&1 | ForEach-Object { Write-Output $_ }
      }
    }
  } catch { }
}

Write-Output "COMPLETED $Stream $ItemId"

. (Join-Path $PSScriptRoot 'Resolve-NteRoots.ps1')

$wfRoot = $NteWorkflowRoot
